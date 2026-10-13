"""Settings: built-in defaults, optionally overridden by a JSON file."""

from __future__ import annotations

import copy
import json
from pathlib import Path

DEFAULTS: dict = {
    "outlook": {
        "enabled": True,
        # Watch the Inbox of every mailbox in the profile (incl. shared
        # mailboxes added to Outlook), not just the default one.
        "all_mailboxes": True,
        # Extra folders by path, e.g. "Inbox/Alerts" or
        # "shared@corp.com/Inbox". Resolved from the default mailbox
        # unless the first segment names a mailbox.
        "extra_folders": [],
        # Safety-net sweep: events can be dropped when many mails
        # arrive at once, so recent items are re-checked periodically.
        "sweep_seconds": 60,
        "preview_chars": 300,
    },
    "teams": {
        "enabled": True,
        # Substrings matched (case-insensitive) against the app id that
        # raised the Windows notification. Run with --list-apps to see ids.
        "app_ids": ["teams"],
        "poll_seconds": 2,
        "preview_chars": 300,
    },
    # Show items that arrived up to N minutes before start-up.
    "backfill_minutes": 0,
    # Append every event as one JSON line (for later filtering/MiniLM).
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


def load(path: str | None) -> dict:
    if not path:
        return copy.deepcopy(DEFAULTS)
    with Path(path).open(encoding="utf-8") as fh:
        return _merge(copy.deepcopy(DEFAULTS), json.load(fh))
