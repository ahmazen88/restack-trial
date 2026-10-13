"""Teams watcher: reads the toasts Teams raises through Windows.

New Teams posts every chat/channel/mention/call notification to the
Windows notification platform, which keeps them in a per-user SQLite
database. Reading that database needs no Graph, no Azure app and no
admin rights. Limits worth knowing:

* Only messages Teams decides to notify about show up. Teams does not
  raise a toast for a chat you are currently looking at, and Focus
  assist / Do-not-disturb / muted chats suppress them.
* Toasts carry a truncated preview, not the full message.
* Teams' toast layout is not documented, so the sender/title split is
  best effort; the raw text lines are kept in ``extra["lines"]``.
"""

from __future__ import annotations

import os
import queue
import shutil
import sqlite3
import tempfile
import threading
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

from commwatch.events import Event, status
from commwatch.sources.outlook import SeenSet, clean_preview

DEFAULT_DB = (
    Path(os.environ.get("LOCALAPPDATA", ""))
    / "Microsoft"
    / "Windows"
    / "Notifications"
    / "wpndatabase.db"
)

UTC = timezone.utc
_FILETIME_EPOCH = datetime(1601, 1, 1, tzinfo=UTC)

QUERY = """
SELECT n.Id, n.ArrivalTime, n.Payload, h.PrimaryId
FROM Notification AS n
JOIN NotificationHandler AS h ON n.HandlerId = h.RecordId
WHERE n.Type = 'toast' AND n.ArrivalTime >= ?
ORDER BY n.ArrivalTime
"""

APPS_QUERY = """
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


def parse_toast(payload: bytes | str) -> dict:
    """Pull the visible text lines out of a toast's XML payload."""
    if isinstance(payload, bytes):
        payload = payload.decode("utf-8", "replace")
    root = ET.fromstring(payload)  # noqa: S314 - local, user-owned data
    lines: list[str] = []
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


def toast_to_event(
    row_id: int,
    arrival: int,
    payload: bytes | str,
    app_id: str,
    preview_chars: int,
) -> Event:
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

    def query(self, sql: str, params: tuple = ()) -> list[tuple]:
        try:
            return self._query(self.path, sql, params)
        except sqlite3.OperationalError:
            # Locked or WAL side files not readable: read a snapshot.
            with tempfile.TemporaryDirectory() as tmp:
                copy = Path(tmp) / self.path.name
                for suffix in ("", "-wal", "-shm"):
                    src = Path(str(self.path) + suffix)
                    if src.exists():
                        shutil.copy2(src, Path(str(copy) + suffix))
                return self._query(copy, sql, params)

    @staticmethod
    def _query(path: Path, sql: str, params: tuple) -> list[tuple]:
        uri = f"{path.resolve().as_uri()}?mode=ro"
        con = sqlite3.connect(uri, uri=True, timeout=2)
        try:
            return con.execute(sql, params).fetchall()
        finally:
            con.close()


def list_apps(db_path: Path = DEFAULT_DB) -> list[tuple[str, int]]:
    return NotificationDb(db_path).query(APPS_QUERY)


class TeamsSource(threading.Thread):
    name = "teams"

    def __init__(
        self,
        cfg: dict,
        out: queue.Queue,
        since: datetime,
        stop: threading.Event,
        db_path: Path | None = None,
    ) -> None:
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
            except Exception as exc:  # noqa: BLE001 - keep watching
                if healthy:
                    self.out.put(status(f"Teams: read failed ({exc})"))
                healthy = False
            self.stop_flag.wait(float(self.cfg["poll_seconds"]))

    def matches(self, app_id: str) -> bool:
        lowered = (app_id or "").lower()
        return any(a in lowered for a in self.app_ids)

    def poll(self) -> int:
        """Emit new Teams toasts; returns how many were emitted."""
        emitted = 0
        newest = self.cursor
        for row_id, arrival, payload, app_id in self.db.query(QUERY, (self.cursor,)):
            newest = max(newest, int(arrival))
            if not self.matches(app_id):
                continue
            if not self.seen.add(f"{row_id}-{arrival}"):
                continue
            try:
                event = toast_to_event(
                    row_id,
                    arrival,
                    payload,
                    app_id,
                    int(self.cfg["preview_chars"]),
                )
            except ET.ParseError as exc:
                self.out.put(status(f"Teams: unreadable toast {row_id} ({exc})"))
                continue
            self.out.put(event)
            emitted += 1
        # Re-read the last few seconds each time: rows can be committed
        # slightly out of order. SeenSet stops duplicates.
        self.cursor = max(self.cursor, newest - 5 * 10_000_000)
        return emitted
