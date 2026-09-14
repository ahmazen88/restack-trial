# Office 365 Outlook

Office 365 Outlook **cloud connector** operations inside a desktop flow (Graph/REST), not the local Outlook COM add-in. For the desktop client use the [Outlook](outlook.md) module instead (`Launch Outlook`, `Retrieve email messages from Outlook`, …).

Official docs: [Office 365 Outlook in desktop flows](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/office365outlook).

Requires an Attended RPA license. DLP and a machine admin registry value can hide the group.

## Operations you will search for

Names follow the cloud connector. Version suffixes such as `(V2)` / `(V3)` / `(V4)` are normal.

### Mail

| Operation | Purpose |
|---|---|
| Send an email (V2) | Send mail; attachments are a list of `{Name, ContentBytes}`. |
| Get emails (V3) | List messages in a folder. |
| Get email (V2) | One message by id. |
| Delete email (V2) | Delete. |
| Move email (V2) | Move to a folder. |
| Flag email (V2) | Flag / complete / unflag. |
| Mark as read or unread (V3) | Read state. |
| Reply to email (V3) | Reply. |
| Reply to all (V3) | Reply all. |
| Forward an email (V2) | Forward. |
| Export email (V2) | Export payload. |

### Calendar

| Operation | Purpose |
|---|---|
| Get calendars (V2) | List calendars. |
| Get events (V4) | List events. |
| Create event (V4) | New event. |
| Update event (V4) | Patch event. |
| Delete event (V4) | Remove event. |

### Attachments

To send files:

1. **Convert file to binary data** for each path.
2. Build a **list** of custom objects `{ Name: "a.pdf", ContentBytes: BinaryData }`.
3. Pass that list to **Send an email (V2)** → Attachments.

When the count is unknown, **Create new list**, **For each** path, **Add item to list** with a custom object, then pass the list.

## When to use this vs Outlook desktop

| Use Office 365 Outlook (this module) | Use Outlook (desktop) |
|---|---|
| Shared mailboxes in Exchange Online, Graph, unattended cloud-started runs | Local PST/OST, COM add-ins, classic desktop-only profiles |
| You already have a cloud Outlook connection | Outlook must be installed and signed in on the machine |
