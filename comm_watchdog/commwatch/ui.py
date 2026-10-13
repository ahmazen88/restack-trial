"""Live window (Tkinter, ships with Python on Windows)."""

from __future__ import annotations

import json
import os
import tkinter as tk
from tkinter import ttk

from commwatch.events import Event
from commwatch.watchdog import Watchdog

COLUMNS = ("time", "source", "sender", "title", "preview")
HEADINGS = {
    "time": "Time",
    "source": "Source",
    "sender": "From",
    "title": "Subject / Chat",
    "preview": "Preview",
}
WIDTHS = {"time": 70, "source": 70, "sender": 220, "title": 260, "preview": 520}


class LiveWindow:
    def __init__(self, watchdog: Watchdog) -> None:
        self.wd = watchdog
        self.max_rows = int(watchdog.cfg.get("max_rows", 2000))
        self.events: list[Event] = []  # newest last
        self.by_iid: dict[str, Event] = {}
        self.counts = {"outlook": 0, "teams": 0}
        self.health = {"outlook": "starting…", "teams": "starting…"}
        self.paused = False

        self.root = tk.Tk()
        self.root.title("CommWatch - Outlook & Teams")
        self.root.geometry("1250x700")
        self._build()
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    # -- layout ------------------------------------------------------
    def _build(self) -> None:
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
        self.tree = ttk.Treeview(table, columns=COLUMNS, show="headings", selectmode="browse")
        for col in COLUMNS:
            self.tree.heading(col, text=HEADINGS[col])
            self.tree.column(col, width=WIDTHS[col], stretch=col == "preview", anchor="w")
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

    # -- data flow ---------------------------------------------------
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
        children = self.tree.get_children()
        for iid in children[self.max_rows :]:
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

    # -- actions -----------------------------------------------------
    def toggle_pause(self) -> None:
        self.paused = not self.paused
        self.pause_btn.config(text="Resume" if self.paused else "Pause")
        if not self.paused:
            self.refresh()
        self._update_labels()

    def clear(self) -> None:
        self.events.clear()
        self.refresh()

    def _selected(self) -> Event | None:
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
                from commwatch.sources.outlook import open_in_outlook  # noqa: PLC0415

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
