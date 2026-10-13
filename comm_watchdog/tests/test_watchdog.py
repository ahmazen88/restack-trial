"""Platform-independent tests: fake notification DB and fake Outlook items."""

import json
import queue
import sqlite3
import threading
from datetime import datetime, timedelta

from commwatch import config
from commwatch.events import Event
from commwatch.sources.outlook import OutlookSource
from commwatch.sources.teams import (
    TeamsSource,
    filetime_to_local,
    local_to_filetime,
    parse_toast,
)
from commwatch.watchdog import Watchdog

TEAMS_APP = "MSTeams_8wekyb3d8bbwe!MSTeams"

TOAST = """<toast launch="msteams:chat?id=1">
  <visual><binding template="ToastGeneric">
    <text>Jane Doe</text>
    <text>Prod is down, can you join the bridge?</text>
    <text placement="attribution">Incident Room</text>
  </binding></visual>
</toast>"""


def make_db(path, rows):
    con = sqlite3.connect(path)
    con.executescript(
        """
        CREATE TABLE NotificationHandler (RecordId INTEGER PRIMARY KEY, PrimaryId TEXT);
        CREATE TABLE Notification (
            "Order" INTEGER, Id INTEGER, HandlerId INTEGER, Type TEXT,
            Payload BLOB, ArrivalTime INTEGER);
        """
    )
    con.execute("INSERT INTO NotificationHandler VALUES (1, ?)", (TEAMS_APP,))
    con.execute("INSERT INTO NotificationHandler VALUES (2, 'Microsoft.Office.OUTLOOK.EXE.15')")
    con.executemany(
        "INSERT INTO Notification (Id, HandlerId, Type, Payload, ArrivalTime) VALUES (?,?,?,?,?)",
        rows,
    )
    con.commit()
    con.close()


def test_filetime_round_trip():
    now = datetime.now().replace(microsecond=0)
    assert filetime_to_local(local_to_filetime(now)) == now


def test_parse_toast():
    toast = parse_toast(TOAST.encode())
    assert toast["lines"] == ["Jane Doe", "Prod is down, can you join the bridge?"]
    assert toast["attribution"] == "Incident Room"
    assert toast["launch"] == "msteams:chat?id=1"


def test_teams_poll_filters_dedupes_and_skips_old(tmp_path):
    db = tmp_path / "wpndatabase.db"
    start = datetime.now() - timedelta(minutes=1)
    old = local_to_filetime(start - timedelta(hours=1))
    new = local_to_filetime(start + timedelta(seconds=10))
    make_db(
        db,
        [
            (1, 1, "toast", TOAST.encode(), old),  # before start
            (2, 1, "toast", TOAST.encode(), new),  # wanted
            (3, 2, "toast", TOAST.encode(), new),  # Outlook toast, ignored
            (4, 1, "tile", b"<tile/>", new),  # not a toast
        ],
    )
    out = queue.Queue()
    cfg = config.load(None)["teams"]
    src = TeamsSource(cfg, out, start, threading.Event(), db_path=db)

    assert src.poll() == 1
    assert src.poll() == 0  # same row is not emitted twice
    event = out.get_nowait()
    assert event.source == "teams"
    assert event.sender == "Jane Doe"
    assert event.title == "Incident Room"
    assert event.preview.startswith("Prod is down")


class FakeItem:
    def __init__(self, entry_id, received, subject="Hello"):
        self.EntryID = entry_id
        self.ReceivedTime = received
        self.Subject = subject
        self.SenderName = "Bob"
        self.SenderEmailAddress = "bob@corp.com"
        self.SenderEmailType = "SMTP"
        self.Body = "Line one\r\n\r\n  line two"
        self.UnRead = True

        class _Att:
            Count = 2

        self.Attachments = _Att()


def test_outlook_item_conversion_and_dedupe():
    out = queue.Queue()
    since = datetime.now() - timedelta(minutes=5)
    src = OutlookSource(config.load(None)["outlook"], out, since, threading.Event())
    item = FakeItem("AAA", datetime.now())

    src.handle_item(item, "Inbox")
    src.handle_item(item, "Inbox")  # event + sweep both see it
    src.handle_item(FakeItem("OLD", since - timedelta(hours=1)), "Inbox")

    event = out.get_nowait()
    assert out.empty()
    assert event.sender == "Bob <bob@corp.com>"
    assert event.preview == "Line one line two"
    assert event.extra["attachments"] == 2
    assert event.extra["unread"] is True


def test_config_override(tmp_path):
    path = tmp_path / "cfg.json"
    path.write_text(json.dumps({"teams": {"poll_seconds": 5}}))
    cfg = config.load(str(path))
    assert cfg["teams"]["poll_seconds"] == 5
    assert cfg["teams"]["app_ids"] == ["teams"]
    assert config.load(None)["teams"]["poll_seconds"] == 2


def test_watchdog_drain_logs_events(tmp_path):
    cfg = config.load(None)
    cfg["log_file"] = str(tmp_path / "log.jsonl")
    wd = Watchdog(cfg)
    wd.queue.put(Event("teams", datetime.now(), "Jane", "Chat", "hi", "t-1"))
    assert [e.uid for e in wd.drain()] == ["t-1"]
    wd.stop()
    line = json.loads((tmp_path / "log.jsonl").read_text().strip())
    assert line["sender"] == "Jane"
