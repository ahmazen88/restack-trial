#!/usr/bin/env python3
"""CommWatch - single-file live watchdog for Outlook mail and Teams messages.

Everything is in this one file so it can be copied onto a machine in one
paste. It is the same tool as the comm_watchdog/ package, just flattened.

WHAT IT DOES
    Opens one live window that shows new Outlook mail and new Teams
    messages as they arrive. No Microsoft Graph, no Azure app, no admin
    rights - it reads your own Outlook (via COM) and your own Windows
    notifications (which is how it sees Teams).

REQUIREMENTS
    * Windows
    * Classic Outlook for Windows, running (the "new Outlook" has no COM)
    * pip install pywin32
    * Teams notification style set to "Windows" (Teams Settings ->
      Notifications) so Teams messages raise toasts this tool can read

RUN
    python commwatch_single.py                 live window
    python commwatch_single.py --backfill 30   also show the last 30 min
    python commwatch_single.py --console       print instead of a window
    python commwatch_single.py --list-apps     list notification app ids
    python commwatch_single.py --no-teams      Outlook only
    python commwatch_single.py --no-outlook    Teams only

Every event is also appended to commwatch_events.jsonl (one JSON per line)
for later filtering / MiniLM work.
"""

from __future__ import annotations

import argparse
import json
import os
import queue
import re
import shutil
import sqlite3
import sys
import tempfile
import threading
import time
import xml.etree.ElementTree as ET
from collections import OrderedDict
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ======================================================================
# Settings - edit these defaults, or pass a JSON file via --config.
# ======================================================================

DEFAULTS: dict = {
    "outlook": {
        "enabled": True,
        # Watch the Inbox of every mailbox in the profile (incl. shared
        # mailboxes added to Outlook), not just the default one.
        "all_mailboxes": True,
        # Extra folders by path, e.g. "Inbox/Alerts" or
        # "shared@corp.com/Inbox".
        "extra_folders": [],
        # Safety-net sweep: events can be dropped when many mails arrive
        # at once, so recent items are re-checked periodically.
        "sweep_seconds": 60,
        "preview_chars": 300,
    },
    "teams": {
        "enabled": True,
        # Substrings matched (case-insensitive) against the app id that
        # raised the notification. Run --list-apps to see the real ids.
        "app_ids": ["teams"],
        "poll_seconds": 2,
        "preview_chars": 300,
    },
    # Show items that arrived up to N minutes before start-up.
    "backfill_minutes": 0,
    "log_file": "commwatch_events.jsonl",
    "max_rows": 2000,
}


def _merge(base: dict, override: dict) -> dict:
    out = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = _merge(out[key], value)
        else:
            out[key] = value
    return out


def load_config(path: str | None) -> dict:
    import copy

    if not path:
        return copy.deepcopy(DEFAULTS)
    with Path(path).open(encoding="utf-8") as fh:
        return _merge(copy.deepcopy(DEFAULTS), json.load(fh))


# ======================================================================
# Event - the one shape shared by both sources, the UI and the log.
# ======================================================================


@dataclass
class Event:
    source: str  # "outlook" | "teams" | "system"
    received: datetime
    sender: str
    title: str
    preview: str
    uid: str
    extra: dict = field(default_factory=dict)

    def to_json(self) -> str:
        data = asdict(self)
        data["received"] = self.received.isoformat(timespec="seconds")
        return json.dumps(data, ensure_ascii=False)


def status(text: str) -> Event:
    now = datetime.now()
    return Event("system", now, "", text, "", f"sys-{now.timestamp()}")


_WS = re.compile(r"\s+")


def clean_preview(text: str, limit: int) -> str:
    text = _WS.sub(" ", text or "").strip()
    return text if len(text) <= limit else text[: limit - 1] + "…"


class SeenSet:
    """Bounded set of ids so long sessions don't grow forever."""

    def __init__(self, limit: int = 20000) -> None:
        self._items: OrderedDict[str, None] = OrderedDict()
        self._limit = limit

    def add(self, key: str) -> bool:
        if key in self._items:
            return False
        self._items[key] = None
        if len(self._items) > self._limit:
            self._items.popitem(last=False)
        return True


# ======================================================================
# Outlook source - COM events (Items.ItemAdd) plus a periodic sweep.
# ======================================================================

OL_FOLDER_INBOX = 6


def _naive_local(value) -> datetime:
    return datetime(value.year, value.month, value.day, value.hour, value.minute, value.second)


def _get(obj, dotted: str):
    try:
        for part in dotted.split("."):
            obj = getattr(obj, part)
    except Exception:  # noqa: BLE001
        return None
    return obj


def _received(item) -> datetime | None:
    for attr in ("ReceivedTime", "CreationTime"):
        value = _get(item, attr)
        if value is not None:
            return _naive_local(value)
    return None


def _sender(item) -> str:
    name = _get(item, "SenderName") or ""
    address = _get(item, "SenderEmailAddress") or ""
    if _get(item, "SenderEmailType") == "EX":
        getter = _get(item, "Sender.GetExchangeUser")
        try:
            address = getter().PrimarySmtpAddress if getter else address
        except Exception:  # noqa: BLE001
            pass
    if name and address and address.lower() != name.lower():
        return f"{name} <{address}>"
    return name or address or "(unknown)"


def outlook_backfill_start(minutes: int) -> datetime:
    start = datetime.now().replace(microsecond=0)
    return start - timedelta(minutes=max(0, minutes), seconds=5)


class _ItemsEvents:
    """COM event sink attached to one folder's Items collection."""

    watcher: "OutlookSource"
    label: str

    def OnItemAdd(self, item) -> None:  # noqa: N802 - COM name
        self.watcher.handle_item(item, self.label)


class OutlookSource(threading.Thread):
    name = "outlook"

    def __init__(self, cfg: dict, out: queue.Queue, since: datetime, stop: threading.Event) -> None:
        super().__init__(daemon=True, name="outlook-watcher")
        self.cfg = cfg
        self.out = out
        self.since = since
        self.stop_flag = stop
        self.seen = SeenSet()
        self._sinks: list = []

    def run(self) -> None:
        try:
            import pythoncom
        except ImportError:
            self.out.put(status("Outlook: pywin32 not installed (pip install pywin32)"))
            return
        pythoncom.CoInitialize()
        try:
            self._run(pythoncom)
        except Exception as exc:  # noqa: BLE001
            self.out.put(status(f"Outlook: stopped - {exc}"))
        finally:
            self._sinks.clear()
            pythoncom.CoUninitialize()

    def _run(self, pythoncom) -> None:
        import win32com.client

        app = win32com.client.Dispatch("Outlook.Application")
        ns = app.GetNamespace("MAPI")
        folders = self._resolve_folders(ns)
        if not folders:
            self.out.put(status("Outlook: no folders to watch"))
            return

        for label, folder in folders:
            items = folder.Items
            sink = win32com.client.WithEvents(items, _ItemsEvents)
            sink.watcher = self
            sink.label = label
            self._sinks.append((items, sink))  # keep referenced or events stop

        self.out.put(status("Outlook: watching " + ", ".join(label for label, _ in folders)))

        self._sweep(folders)
        every = max(10, int(self.cfg["sweep_seconds"]))
        next_sweep = time.monotonic() + every
        while not self.stop_flag.is_set():
            pythoncom.PumpWaitingMessages()
            if time.monotonic() >= next_sweep:
                self._sweep(folders)
                next_sweep = time.monotonic() + every
            time.sleep(0.2)

    def _resolve_folders(self, ns) -> list:
        found: list = []
        if self.cfg.get("all_mailboxes", True):
            for store in ns.Stores:
                try:
                    inbox = store.GetDefaultFolder(OL_FOLDER_INBOX)
                except Exception:  # noqa: BLE001, S112
                    continue
                found.append((f"{store.DisplayName}/Inbox", inbox))
        if not found:
            found.append(("Inbox", ns.GetDefaultFolder(OL_FOLDER_INBOX)))

        for path in self.cfg.get("extra_folders", []):
            try:
                found.append((path, self._folder_by_path(ns, path)))
            except Exception as exc:  # noqa: BLE001
                self.out.put(status(f"Outlook: folder '{path}' not found ({exc})"))
        return found

    @staticmethod
    def _folder_by_path(ns, path: str):
        parts = [p for p in path.replace("\\", "/").split("/") if p]
        root = None
        for store in ns.Stores:
            if store.DisplayName.lower() == parts[0].lower():
                root = store.GetRootFolder()
                parts = parts[1:]
                break
        if root is None:
            root = ns.DefaultStore.GetRootFolder()
        folder = root
        for part in parts:
            folder = folder.Folders.Item(part)
        return folder

    def _sweep(self, folders) -> None:
        for label, folder in folders:
            try:
                items = folder.Items
                items.Sort("[ReceivedTime]", True)
                item = items.GetFirst()
                checked = 0
                while item is not None and checked < 200:
                    checked += 1
                    when = _received(item)
                    if when is not None and when < self.since:
                        break
                    self.handle_item(item, label)
                    item = items.GetNext()
            except Exception as exc:  # noqa: BLE001
                self.out.put(status(f"Outlook: sweep of {label} failed ({exc})"))

    def handle_item(self, item, label: str) -> None:
        try:
            entry_id = item.EntryID
            if not self.seen.add(entry_id):
                return
            received = _received(item) or datetime.now()
            if received < self.since:
                return
            self.out.put(self._to_event(item, label, entry_id, received))
        except Exception as exc:  # noqa: BLE001
            self.out.put(status(f"Outlook: could not read item ({exc})"))

    def _to_event(self, item, label, entry_id, received) -> Event:
        limit = int(self.cfg["preview_chars"])
        try:
            body = item.Body
        except Exception:  # noqa: BLE001 - blocked by security policy
            body = ""
        try:
            attachments = item.Attachments.Count
        except Exception:  # noqa: BLE001
            attachments = 0
        return Event(
            source="outlook",
            received=received,
            sender=_sender(item),
            title=_get(item, "Subject") or "(no subject)",
            preview=clean_preview(body, limit),
            uid=f"outlook-{entry_id}",
            extra={
                "folder": label,
                "entry_id": entry_id,
                "store_id": _get(item, "Parent.StoreID"),
                "importance": _get(item, "Importance"),
                "unread": _get(item, "UnRead"),
                "attachments": attachments,
                "categories": _get(item, "Categories"),
                "to": _get(item, "To"),
                "cc": _get(item, "CC"),
            },
        )


def open_in_outlook(event: Event) -> None:
    import win32com.client

    ns = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    store_id = event.extra.get("store_id")
    if store_id:
        item = ns.GetItemFromID(event.extra["entry_id"], store_id)
    else:
        item = ns.GetItemFromID(event.extra["entry_id"])
    item.Display()


# ======================================================================
# Teams source - reads the toasts Teams raises through Windows.
# ======================================================================

DEFAULT_DB = (
    Path(os.environ.get("LOCALAPPDATA", ""))
    / "Microsoft"
    / "Windows"
    / "Notifications"
    / "wpndatabase.db"
)

UTC = timezone.utc
_FILETIME_EPOCH = datetime(1601, 1, 1, tzinfo=UTC)

_TOAST_QUERY = """
SELECT n.Id, n.ArrivalTime, n.Payload, h.PrimaryId
FROM Notification AS n
JOIN NotificationHandler AS h ON n.HandlerId = h.RecordId
WHERE n.Type = 'toast' AND n.ArrivalTime >= ?
ORDER BY n.ArrivalTime
"""

_APPS_QUERY = """
SELECT h.PrimaryId, COUNT(n.Id)
FROM NotificationHandler AS h
LEFT JOIN Notification AS n ON n.HandlerId = h.RecordId
GROUP BY h.PrimaryId
ORDER BY COUNT(n.Id) DESC
"""


def filetime_to_local(value: int) -> datetime:
    utc = _FILETIME_EPOCH + timedelta(microseconds=int(value) // 10)
    return utc.astimezone().replace(tzinfo=None)


def local_to_filetime(value: datetime) -> int:
    utc = value.astimezone(UTC)
    return int((utc - _FILETIME_EPOCH) / timedelta(microseconds=1)) * 10


def parse_toast(payload) -> dict:
    if isinstance(payload, bytes):
        payload = payload.decode("utf-8", "replace")
    root = ET.fromstring(payload)  # noqa: S314 - local, user-owned data
    lines: list = []
    attribution = ""
    for el in root.iter("text"):
        text = (el.text or "").strip()
        if not text:
            continue
        if el.get("placement") == "attribution":
            attribution = text
        else:
            lines.append(text)
    header = root.find(".//header")
    return {
        "lines": lines,
        "attribution": attribution,
        "header": header.get("title", "") if header is not None else "",
        "launch": root.get("launch", ""),
    }


def toast_to_event(row_id, arrival, payload, app_id, preview_chars) -> Event:
    toast = parse_toast(payload)
    lines = toast["lines"]
    sender = lines[0] if lines else "(Teams)"
    message = " ".join(lines[1:]) if len(lines) > 1 else ""
    title = toast["header"] or toast["attribution"] or "Teams"
    return Event(
        source="teams",
        received=filetime_to_local(arrival),
        sender=sender,
        title=title,
        preview=clean_preview(message, preview_chars),
        uid=f"teams-{row_id}-{arrival}",
        extra={"app_id": app_id, **toast},
    )


class NotificationDb:
    """Read-only access that copes with Windows holding the file open."""

    def __init__(self, path: Path) -> None:
        self.path = path

    def query(self, sql: str, params: tuple = ()) -> list:
        try:
            return self._query(self.path, sql, params)
        except sqlite3.OperationalError:
            with tempfile.TemporaryDirectory() as tmp:
                copy = Path(tmp) / self.path.name
                for suffix in ("", "-wal", "-shm"):
                    src = Path(str(self.path) + suffix)
                    if src.exists():
                        shutil.copy2(src, Path(str(copy) + suffix))
                return self._query(copy, sql, params)

    @staticmethod
    def _query(path: Path, sql: str, params: tuple) -> list:
        uri = f"{path.resolve().as_uri()}?mode=ro"
        con = sqlite3.connect(uri, uri=True, timeout=2)
        try:
            return con.execute(sql, params).fetchall()
        finally:
            con.close()


def list_apps(db_path: Path = DEFAULT_DB) -> list:
    return NotificationDb(db_path).query(_APPS_QUERY)


class TeamsSource(threading.Thread):
    name = "teams"

    def __init__(self, cfg, out, since, stop, db_path=None) -> None:
        super().__init__(daemon=True, name="teams-watcher")
        self.cfg = cfg
        self.out = out
        self.stop_flag = stop
        self.db = NotificationDb(Path(db_path or cfg.get("db_path") or DEFAULT_DB))
        self.cursor = local_to_filetime(since)
        self.seen = SeenSet()
        self.app_ids = [a.lower() for a in cfg["app_ids"]]

    def run(self) -> None:
        if not self.db.path.exists():
            self.out.put(status(f"Teams: notification database not found at {self.db.path}"))
            return
        self.out.put(status("Teams: watching Windows notifications"))
        healthy = True
        while not self.stop_flag.is_set():
            try:
                self.poll()
                if not healthy:
                    self.out.put(status("Teams: reading notifications again"))
                healthy = True
            except Exception as exc:  # noqa: BLE001
                if healthy:
                    self.out.put(status(f"Teams: read failed ({exc})"))
                healthy = False
            self.stop_flag.wait(float(self.cfg["poll_seconds"]))

    def matches(self, app_id: str) -> bool:
        lowered = (app_id or "").lower()
        return any(a in lowered for a in self.app_ids)

    def poll(self) -> int:
        emitted = 0
        newest = self.cursor
        for row_id, arrival, payload, app_id in self.db.query(_TOAST_QUERY, (self.cursor,)):
            newest = max(newest, int(arrival))
            if not self.matches(app_id):
                continue
            if not self.seen.add(f"{row_id}-{arrival}"):
                continue
            try:
                event = toast_to_event(row_id, arrival, payload, app_id, int(self.cfg["preview_chars"]))
            except ET.ParseError as exc:
                self.out.put(status(f"Teams: unreadable toast {row_id} ({exc})"))
                continue
            self.out.put(event)
            emitted += 1
        self.cursor = max(self.cursor, newest - 5 * 10_000_000)
        return emitted


# ======================================================================
# Watchdog - starts the sources and collects their events.
# ======================================================================


class Watchdog:
    def __init__(self, cfg: dict) -> None:
        self.cfg = cfg
        self.queue: queue.Queue = queue.Queue()
        self.stop_flag = threading.Event()
        self.since = outlook_backfill_start(int(cfg.get("backfill_minutes", 0)))
        self.sources: list = []
        log = cfg.get("log_file")
        self._log = Path(log).open("a", encoding="utf-8") if log else None  # noqa: SIM115

    def start(self) -> None:
        if self.cfg["outlook"]["enabled"]:
            self.sources.append(OutlookSource(self.cfg["outlook"], self.queue, self.since, self.stop_flag))
        if self.cfg["teams"]["enabled"]:
            self.sources.append(TeamsSource(self.cfg["teams"], self.queue, self.since, self.stop_flag))
        for src in self.sources:
            src.start()

    def drain(self, limit: int = 500) -> list:
        events: list = []
        while len(events) < limit:
            try:
                event = self.queue.get_nowait()
            except queue.Empty:
                break
            events.append(event)
            if self._log and event.source != "system":
                self._log.write(event.to_json() + "\n")
        if self._log and events:
            self._log.flush()
        return events

    def stop(self) -> None:
        self.stop_flag.set()
        for src in self.sources:
            src.join(timeout=3)
        if self._log:
            self._log.close()


# ======================================================================
# Live window (Tkinter, ships with Python on Windows).
# ======================================================================

_COLUMNS = ("time", "source", "sender", "title", "preview")
_HEADINGS = {"time": "Time", "source": "Source", "sender": "From", "title": "Subject / Chat", "preview": "Preview"}
_WIDTHS = {"time": 70, "source": 70, "sender": 220, "title": 260, "preview": 520}


class LiveWindow:
    def __init__(self, watchdog: Watchdog) -> None:
        import tkinter as tk
        from tkinter import ttk

        self.tk = tk
        self.ttk = ttk
        self.wd = watchdog
        self.max_rows = int(watchdog.cfg.get("max_rows", 2000))
        self.events: list = []
        self.by_iid: dict = {}
        self.counts = {"outlook": 0, "teams": 0}
        self.health = {"outlook": "starting…", "teams": "starting…"}
        self.paused = False

        self.root = tk.Tk()
        self.root.title("CommWatch - Outlook & Teams")
        self.root.geometry("1250x700")
        self._build()
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def _build(self) -> None:
        tk, ttk = self.tk, self.ttk
        bar = ttk.Frame(self.root, padding=6)
        bar.pack(fill="x")

        ttk.Label(bar, text="Filter:").pack(side="left")
        self.filter_var = tk.StringVar()
        self.filter_var.trace_add("write", lambda *_: self.refresh())
        ttk.Entry(bar, textvariable=self.filter_var, width=35).pack(side="left", padx=(4, 12))

        self.show = {s: tk.BooleanVar(value=True) for s in ("outlook", "teams")}
        for src, var in self.show.items():
            ttk.Checkbutton(bar, text=src.title(), variable=var, command=self.refresh).pack(side="left")

        self.pause_btn = ttk.Button(bar, text="Pause", command=self.toggle_pause)
        self.pause_btn.pack(side="left", padx=(12, 4))
        ttk.Button(bar, text="Clear", command=self.clear).pack(side="left")

        self.top_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            bar,
            text="Always on top",
            variable=self.top_var,
            command=lambda: self.root.attributes("-topmost", self.top_var.get()),
        ).pack(side="left", padx=12)

        self.count_lbl = ttk.Label(bar, text="")
        self.count_lbl.pack(side="right")

        panes = ttk.PanedWindow(self.root, orient="vertical")
        panes.pack(fill="both", expand=True, padx=6)

        table = ttk.Frame(panes)
        self.tree = ttk.Treeview(table, columns=_COLUMNS, show="headings", selectmode="browse")
        for col in _COLUMNS:
            self.tree.heading(col, text=_HEADINGS[col])
            self.tree.column(col, width=_WIDTHS[col], stretch=col == "preview", anchor="w")
        self.tree.tag_configure("outlook", background="#e8f0fe")
        self.tree.tag_configure("teams", background="#efe9fb")
        self.tree.tag_configure("unread", font=("Segoe UI", 9, "bold"))
        scroll = ttk.Scrollbar(table, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        self.tree.bind("<<TreeviewSelect>>", self.show_detail)
        self.tree.bind("<Double-1>", self.open_selected)
        panes.add(table, weight=4)

        self.detail = tk.Text(panes, height=10, wrap="word", state="disabled")
        panes.add(self.detail, weight=1)

        self.status = ttk.Label(self.root, text="", anchor="w", padding=(6, 3))
        self.status.pack(fill="x")
        self._update_labels()

    def tick(self) -> None:
        for event in self.wd.drain():
            if event.source == "system":
                src = event.title.split(":", 1)[0].lower()
                self.health[src if src in self.health else "outlook"] = event.title.split(":", 1)[-1].strip()
                continue
            self.counts[event.source] += 1
            self.events.append(event)
            if len(self.events) > self.max_rows:
                self.events = self.events[-self.max_rows :]
            if not self.paused and self._visible(event):
                self._insert(event, top=True)
        self._trim_tree()
        self._update_labels()
        self.root.after(250, self.tick)

    def _visible(self, event: Event) -> bool:
        if not self.show[event.source].get():
            return False
        needle = self.filter_var.get().strip().lower()
        if not needle:
            return True
        hay = f"{event.sender} {event.title} {event.preview}".lower()
        return all(word in hay for word in needle.split())

    def _insert(self, event: Event, *, top: bool) -> None:
        tags = [event.source]
        if event.extra.get("unread"):
            tags.append("unread")
        iid = self.tree.insert(
            "",
            0 if top else "end",
            values=(
                event.received.strftime("%H:%M:%S"),
                event.source.title(),
                event.sender,
                event.title,
                event.preview,
            ),
            tags=tags,
        )
        self.by_iid[iid] = event

    def _trim_tree(self) -> None:
        for iid in self.tree.get_children()[self.max_rows :]:
            self.by_iid.pop(iid, None)
            self.tree.delete(iid)

    def refresh(self) -> None:
        self.tree.delete(*self.tree.get_children())
        self.by_iid.clear()
        for event in reversed(self.events):
            if self._visible(event):
                self._insert(event, top=False)

    def _update_labels(self) -> None:
        self.count_lbl.config(
            text=f"Outlook: {self.counts['outlook']}   Teams: {self.counts['teams']}"
            + ("   [PAUSED]" if self.paused else "")
        )
        self.status.config(text=f"Outlook - {self.health['outlook']}    |    Teams - {self.health['teams']}")

    def toggle_pause(self) -> None:
        self.paused = not self.paused
        self.pause_btn.config(text="Resume" if self.paused else "Pause")
        if not self.paused:
            self.refresh()
        self._update_labels()

    def clear(self) -> None:
        self.events.clear()
        self.refresh()

    def _selected(self):
        sel = self.tree.selection()
        return self.by_iid.get(sel[0]) if sel else None

    def show_detail(self, _evt=None) -> None:
        event = self._selected()
        if not event:
            return
        text = (
            f"{event.source.upper()}  {event.received:%Y-%m-%d %H:%M:%S}\n"
            f"From:  {event.sender}\nTitle: {event.title}\n\n{event.preview}\n\n"
            f"{json.dumps(event.extra, indent=2, ensure_ascii=False, default=str)}"
        )
        self.detail.config(state="normal")
        self.detail.delete("1.0", "end")
        self.detail.insert("1.0", text)
        self.detail.config(state="disabled")

    def open_selected(self, _evt=None) -> None:
        event = self._selected()
        if not event:
            return
        try:
            if event.source == "outlook":
                open_in_outlook(event)
            else:
                os.startfile("msteams:")  # type: ignore[attr-defined]  # noqa: S606
        except Exception as exc:  # noqa: BLE001
            self.health[event.source] = f"could not open item ({exc})"
            self._update_labels()

    def close(self) -> None:
        self.wd.stop()
        self.root.destroy()

    def run(self) -> None:
        self.root.after(250, self.tick)
        self.root.mainloop()


# ======================================================================
# Entry point.
# ======================================================================


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="commwatch_single",
        description="Live watchdog for Outlook mail and Teams messages.",
    )
    parser.add_argument("--config", help="JSON settings file (optional)")
    parser.add_argument("--console", action="store_true", help="print events instead of opening the window")
    parser.add_argument("--list-apps", action="store_true", help="list apps that raise Windows notifications, then exit")
    parser.add_argument("--no-outlook", action="store_true")
    parser.add_argument("--no-teams", action="store_true")
    parser.add_argument("--backfill", type=int, metavar="MIN", help="also show items from the last MIN minutes")
    args = parser.parse_args()

    if sys.platform != "win32":
        print("Warning: CommWatch reads Outlook (COM) and Windows notifications; it only works on Windows.")

    if args.list_apps:
        for app_id, count in list_apps():
            print(f"{count:5}  {app_id}")
        return 0

    cfg = load_config(args.config)
    if args.no_outlook:
        cfg["outlook"]["enabled"] = False
    if args.no_teams:
        cfg["teams"]["enabled"] = False
    if args.backfill is not None:
        cfg["backfill_minutes"] = args.backfill

    wd = Watchdog(cfg)
    wd.start()

    if not args.console:
        LiveWindow(wd).run()
        return 0

    try:
        while True:
            for e in wd.drain():
                if e.source == "system":
                    print(f"-- {e.title}")
                else:
                    print(f"{e.received:%H:%M:%S} [{e.source:7}] {e.sender} | {e.title} | {e.preview[:120]}")
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        wd.stop()
    return 0


if __name__ == "__main__":
    sys.exit(main())
