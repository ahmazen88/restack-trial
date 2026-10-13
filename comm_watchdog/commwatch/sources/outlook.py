"""Outlook watcher: COM events (Items.ItemAdd) plus a periodic sweep.

Needs classic Outlook for Windows running in the same user session and
pywin32. The "new Outlook" has no COM interface and cannot be watched.
"""

from __future__ import annotations

import queue
import re
import threading
import time
from collections import OrderedDict
from datetime import datetime, timedelta

from commwatch.events import Event, status

OL_FOLDER_INBOX = 6
_WS = re.compile(r"\s+")


def naive_local(value) -> datetime:
    """pywin32 COM dates carry a misleading tzinfo; keep wall-clock time."""
    return datetime(
        value.year,
        value.month,
        value.day,
        value.hour,
        value.minute,
        value.second,
    )


def clean_preview(text: str, limit: int) -> str:
    text = _WS.sub(" ", text or "").strip()
    return text if len(text) <= limit else text[: limit - 1] + "…"


class SeenSet:
    """Bounded set of ids so long-running sessions don't grow forever."""

    def __init__(self, limit: int = 20000) -> None:
        self._items: OrderedDict[str, None] = OrderedDict()
        self._limit = limit

    def add(self, key: str) -> bool:
        """Return True if the key is new."""
        if key in self._items:
            return False
        self._items[key] = None
        if len(self._items) > self._limit:
            self._items.popitem(last=False)
        return True


class _ItemsEvents:
    """COM event sink attached to one folder's Items collection."""

    watcher: OutlookSource
    label: str

    def OnItemAdd(self, item) -> None:  # noqa: N802 - COM name
        self.watcher.handle_item(item, self.label)


class OutlookSource(threading.Thread):
    name = "outlook"

    def __init__(
        self,
        cfg: dict,
        out: queue.Queue,
        since: datetime,
        stop: threading.Event,
    ) -> None:
        super().__init__(daemon=True, name="outlook-watcher")
        self.cfg = cfg
        self.out = out
        self.since = since
        self.stop_flag = stop
        self.seen = SeenSet()
        self._sinks: list = []  # keep COM sinks alive

    # -- thread entry ------------------------------------------------
    def run(self) -> None:
        try:
            import pythoncom  # noqa: PLC0415
        except ImportError:
            self.out.put(status("Outlook: pywin32 not installed (pip install pywin32)"))
            return
        pythoncom.CoInitialize()
        try:
            self._run(pythoncom)
        except Exception as exc:  # noqa: BLE001 - report and stop
            self.out.put(status(f"Outlook: stopped - {exc}"))
        finally:
            self._sinks.clear()
            pythoncom.CoUninitialize()

    def _run(self, pythoncom) -> None:
        import win32com.client  # noqa: PLC0415

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
            # The Items object must stay referenced or events stop.
            self._sinks.append((items, sink))

        names = ", ".join(label for label, _ in folders)
        self.out.put(status(f"Outlook: watching {names}"))

        self._sweep(folders)
        every = max(10, int(self.cfg["sweep_seconds"]))
        next_sweep = time.monotonic() + every
        while not self.stop_flag.is_set():
            pythoncom.PumpWaitingMessages()
            if time.monotonic() >= next_sweep:
                self._sweep(folders)
                next_sweep = time.monotonic() + every
            time.sleep(0.2)

    # -- folders -----------------------------------------------------
    def _resolve_folders(self, ns) -> list[tuple[str, object]]:
        found: list[tuple[str, object]] = []
        if self.cfg.get("all_mailboxes", True):
            for store in ns.Stores:
                try:
                    inbox = store.GetDefaultFolder(OL_FOLDER_INBOX)
                except Exception:  # noqa: BLE001, S112 - archives/public folders
                    continue
                found.append((f"{store.DisplayName}/Inbox", inbox))
        if not found:
            inbox = ns.GetDefaultFolder(OL_FOLDER_INBOX)
            found.append(("Inbox", inbox))

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

    # -- items -------------------------------------------------------
    def _sweep(self, folders) -> None:
        """Re-check the newest items; catches events Outlook dropped."""
        for label, folder in folders:
            try:
                items = folder.Items
                items.Sort("[ReceivedTime]", True)  # newest first
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
                "message_class": _get(item, "MessageClass"),
                "importance": _get(item, "Importance"),
                "unread": _get(item, "UnRead"),
                "attachments": attachments,
                "categories": _get(item, "Categories"),
                "to": _get(item, "To"),
                "cc": _get(item, "CC"),
            },
        )


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
            return naive_local(value)
    return None


def _sender(item) -> str:
    name = _get(item, "SenderName") or ""
    address = _get(item, "SenderEmailAddress") or ""
    if _get(item, "SenderEmailType") == "EX":
        # Exchange users come back as an X500 path; ask for the SMTP one.
        smtp = _get(item, "Sender.GetExchangeUser")
        try:
            address = smtp().PrimarySmtpAddress if smtp else address
        except Exception:  # noqa: BLE001
            pass
    if name and address and address.lower() != name.lower():
        return f"{name} <{address}>"
    return name or address or "(unknown)"


def open_in_outlook(event: Event) -> None:
    """Display the mail in Outlook (called from the UI thread)."""
    import win32com.client  # noqa: PLC0415

    ns = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    store_id = event.extra.get("store_id")
    if store_id:
        item = ns.GetItemFromID(event.extra["entry_id"], store_id)
    else:
        item = ns.GetItemFromID(event.extra["entry_id"])
    item.Display()


def backfill_start(minutes: int) -> datetime:
    # Outlook times have 1 s precision; a little slack avoids losing a
    # mail that lands in the same second the watchdog starts.
    start = datetime.now().replace(microsecond=0)
    return start - timedelta(minutes=max(0, minutes), seconds=5)
