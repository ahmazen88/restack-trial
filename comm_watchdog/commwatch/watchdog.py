"""Starts the sources and hands their events to a consumer."""

from __future__ import annotations

import queue
import threading
from pathlib import Path

from commwatch.events import Event
from commwatch.sources.outlook import OutlookSource, backfill_start
from commwatch.sources.teams import TeamsSource


class Watchdog:
    def __init__(self, cfg: dict) -> None:
        self.cfg = cfg
        self.queue: queue.Queue[Event] = queue.Queue()
        self.stop_flag = threading.Event()
        self.since = backfill_start(int(cfg.get("backfill_minutes", 0)))
        self.sources: list[threading.Thread] = []
        log = cfg.get("log_file")
        self._log = Path(log).open("a", encoding="utf-8") if log else None  # noqa: SIM115

    def start(self) -> None:
        if self.cfg["outlook"]["enabled"]:
            self.sources.append(OutlookSource(self.cfg["outlook"], self.queue, self.since, self.stop_flag))
        if self.cfg["teams"]["enabled"]:
            self.sources.append(TeamsSource(self.cfg["teams"], self.queue, self.since, self.stop_flag))
        for src in self.sources:
            src.start()

    def drain(self, limit: int = 500) -> list[Event]:
        """Non-blocking: return the events that arrived since last call."""
        events: list[Event] = []
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
