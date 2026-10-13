"""Common event shape shared by every source, the UI and the log."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime


@dataclass
class Event:
    source: str  # "outlook" | "teams" | "system"
    received: datetime
    sender: str
    title: str  # mail subject / Teams chat or channel name
    preview: str  # first part of the body / message text
    uid: str  # stable id used for de-duplication
    extra: dict = field(default_factory=dict)

    def to_json(self) -> str:
        data = asdict(self)
        data["received"] = self.received.isoformat(timespec="seconds")
        return json.dumps(data, ensure_ascii=False)


def status(text: str) -> Event:
    """Health/diagnostic message from a source, shown in the status bar."""
    now = datetime.now()
    return Event("system", now, "", text, "", f"sys-{now.timestamp()}")
