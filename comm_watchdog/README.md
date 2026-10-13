# CommWatch: live Outlook + Teams watchdog

CommWatch monitors incoming **Outlook mail** and **Teams messages** on a corporate Windows PC and streams them into one live window. It doesn't need Microsoft Graph, an Azure app registration, or admin consent.

| Source | How it's read | Needs |
|---|---|---|
| Outlook | COM events (`Items.ItemAdd`) on every mailbox's Inbox and any extra folders, plus a sweep every 60 s for events Outlook drops | Classic Outlook for Windows running, `pywin32` |
| Teams | The toasts Teams raises through Windows, read from the per-user notification database (`%LOCALAPPDATA%\Microsoft\Windows\Notifications\wpndatabase.db`) | New Teams with Windows notifications on |

Every event is also appended to `commwatch_events.jsonl`, one JSON object per line, ready for the filtering and MiniLM stage.

## Run

```bat
pip install pywin32
cd comm_watchdog
run.bat                      :: live window
run.bat --backfill 30        :: also show the last 30 minutes
run.bat --console            :: print to the terminal instead
run.bat --list-apps          :: which apps raise Windows notifications (check Teams' id)
run.bat --config config.example.json
```

In the live window:
- **Filter box:** words must all match the sender, subject/chat, or preview.
- **Outlook / Teams checkboxes:** show or hide each source.
- **Pause / Resume:** freezes the view while events keep being collected.
- **Always on top**
- **Select a row** to see full details, including folder, recipients, attachments, and the raw Teams lines.
- **Double-click** opens the mail in Outlook, or brings Teams to the front.
- **Status bar:** shows each source's health.

## Teams caveats

CommWatch only sees messages Teams *notifies* about:
- In Teams **Settings → Notifications**, set the style to **Windows** (the default) and turn on notifications for chats, mentions, and channels you care about.
- Windows **Focus / Do not disturb** and muted chats suppress toasts.
- Teams doesn't notify for the chat you currently have open.
- Toasts carry a preview, not always the full message. The first line is treated as the sender, and the rest as the message.

If `--list-apps` shows Teams under an id that doesn't contain "teams", put that id in `teams.app_ids`.

## Outlook caveats

- The **new Outlook** has no COM interface. Use classic Outlook.
- If IT policy blocks programmatic access, reading the body may trigger a security prompt or come back empty. The rest of the event still shows.
- Shared mailboxes are picked up when they're added to your Outlook profile. Other folders go in `outlook.extra_folders`, written as `Inbox/Sub` or `mailbox name/Inbox`.

## Tests

The tests run on any OS, using a fake notification database and fake Outlook items:

```
pip install pytest && python -m pytest -q tests
```
