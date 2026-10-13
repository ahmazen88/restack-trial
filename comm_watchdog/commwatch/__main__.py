"""python -m commwatch [--config FILE] [--console] [--list-apps]"""

from __future__ import annotations

import argparse
import sys
import time

from commwatch import config
from commwatch.watchdog import Watchdog


def main() -> int:
    parser = argparse.ArgumentParser(prog="commwatch", description="Live watchdog for Outlook mail and Teams messages.")
    parser.add_argument("--config", help="JSON settings file (see config.example.json)")
    parser.add_argument("--console", action="store_true", help="print events instead of opening the window")
    parser.add_argument("--list-apps", action="store_true", help="list apps that raise Windows notifications, then exit")
    parser.add_argument("--no-outlook", action="store_true")
    parser.add_argument("--no-teams", action="store_true")
    parser.add_argument("--backfill", type=int, metavar="MIN", help="also show items from the last MIN minutes")
    args = parser.parse_args()

    if sys.platform != "win32":
        print("Warning: CommWatch reads Outlook (COM) and Windows notifications; it only works on Windows.")

    if args.list_apps:
        from commwatch.sources.teams import list_apps  # noqa: PLC0415

        for app_id, count in list_apps():
            print(f"{count:5}  {app_id}")
        return 0

    cfg = config.load(args.config)
    if args.no_outlook:
        cfg["outlook"]["enabled"] = False
    if args.no_teams:
        cfg["teams"]["enabled"] = False
    if args.backfill is not None:
        cfg["backfill_minutes"] = args.backfill

    wd = Watchdog(cfg)
    wd.start()

    if not args.console:
        from commwatch.ui import LiveWindow  # noqa: PLC0415

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
