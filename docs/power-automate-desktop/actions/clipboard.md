# Clipboard

Read, write, and clear Windows clipboard text.

- Actions in this module: **3**
- Official docs: [Clipboard actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/clipboard)

## Actions

### Get clipboard text

Reads clipboard text.

Designer name: **Get clipboard text**. Official reference: [Clipboard / Get clipboard text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/clipboard#gettext).

This action has no input parameters.

**Outputs**

| Variable | Type |
|---|---|
| ClipboardText | Text value |

**On error:** `Can't retrieve clipboard contents`.

---

### Set clipboard Text

Writes clipboard text.

Designer name: **Set clipboard Text**. Official reference: [Clipboard / Set clipboard Text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/clipboard#settext).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Clipboard text | Required | Text value | — |

Produces no variables.

**On error:** `Can't set clipboard contents`.

---

### Clear clipboard contents

Clears clipboard contents.

Designer name: **Clear clipboard contents**. Official reference: [Clipboard / Clear clipboard contents](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/clipboard#clear).

This action has no input parameters.

Produces no variables.

No module-specific exceptions are listed for this action.

---
