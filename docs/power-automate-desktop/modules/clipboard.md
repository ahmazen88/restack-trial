# Clipboard

Read, write, or clear the Windows clipboard.

This page documents every **native action** in this group (3 items).

## Actions

### Clear clipboard contents

- **Inventory id:** `clipboard/clear-clipboard-contents`
- **Kind:** native-action
- **Purpose:** Clears clipboard contents.
- **Key inputs:** None
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Clear clipboard contents](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/clipboard#clear)

### Get clipboard text

- **Inventory id:** `clipboard/get-clipboard-text`
- **Kind:** native-action
- **Purpose:** Reads clipboard text into a flow variable.
- **Key inputs:** None
- **Produces:** `ClipboardText` (Text value)
- **Exceptions:** `Can't retrieve clipboard contents`
- **Microsoft Learn:** [Get clipboard text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/clipboard#gettext)

### Set clipboard Text

- **Inventory id:** `clipboard/set-clipboard-text`
- **Kind:** native-action
- **Purpose:** Writes clipboard Text.
- **Key inputs:** `Clipboard text` (Text value)
- **Produces:** None listed
- **Exceptions:** `Can't set clipboard contents`
- **Microsoft Learn:** [Set clipboard Text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/clipboard#settext)
