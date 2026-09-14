# Clipboard — how each function works

Native Actions pane module **Clipboard**.

3 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Clear clipboard contents

- **Id:** `clipboard/clear-clipboard-contents`
- **Kind:** native-action
- **Purpose:** Clears clipboard contents.

**Use case.** In a hand-off between two apps that have no API, drop **Clear clipboard contents** on the canvas. Clears clipboard contents.

**Demonstration.**

```text
**Clear clipboard contents**
- (no inputs)
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Copy with Get/Set clipboard; Clear clipboard contents when the secret should not linger.

### Get clipboard text

- **Id:** `clipboard/get-clipboard-text`
- **Kind:** native-action
- **Purpose:** Reads clipboard text into a flow variable.

**Use case.** In a hand-off between two apps that have no API, drop **Get clipboard text** on the canvas. Reads clipboard text into a flow variable.

**Demonstration.**

```text
**Get clipboard text**
- (no inputs)
Produces:
- `%ClipboardText%` (Text value)
```

**Analogy.** Reading whatever is currently on the sticky note.

**In combination.** Copy with Get/Set clipboard; Clear clipboard contents when the secret should not linger.

### Set clipboard Text

- **Id:** `clipboard/set-clipboard-text`
- **Kind:** native-action
- **Purpose:** Writes clipboard Text.

**Use case.** In a hand-off between two apps that have no API, drop **Set clipboard Text** on the canvas. Writes clipboard Text.

**Demonstration.**

```text
**Set clipboard Text**
- Clipboard text: `INV-1042`
```

**Analogy.** Replacing the sticky note with a new one.

**In combination.** Copy with Get/Set clipboard; Clear clipboard contents when the secret should not linger.
