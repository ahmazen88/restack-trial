# Terminal emulation — how each function works

Native Actions pane module **Terminal emulation**.

8 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Close terminal session

- **Id:** `terminalemulation/close-terminal-session`
- **Kind:** native-action
- **Purpose:** Closes terminal session.

**Use case.** In an AS/400 or mainframe screen, drop **Close terminal session** on the canvas. Closes terminal session.

**Demonstration.**

```text
**Close terminal session**
- Terminal session to close: `%TerminalSession%`
```

**Analogy.** Turning out the lights when the work in that room is done.

**In combination.** Open terminal session, Wait for text, Set text / Send key, Close terminal session. Call this only after the last use of the instance so you do not break later steps.

### Get text from terminal session

- **Id:** `terminalemulation/get-text-from-terminal-session`
- **Kind:** native-action
- **Purpose:** Reads text from terminal session into a flow variable.

**Use case.** In an AS/400 or mainframe screen, drop **Get text from terminal session** on the canvas. Reads text from terminal session into a flow variable.

**Demonstration.**

```text
**Get text from terminal session**
- Terminal session: `%TerminalSession%`
- Get text from: `Field`
- Get field by: `Label`
- Label: `INV-1042`
- Index: `1`
- Text length: `1`
- Row: `1`
- Column: `Amount`
Produces:
- `%TerminalText%` (Text value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Open terminal session, Wait for text, Set text / Send key, Close terminal session.

### Move cursor on terminal session

- **Id:** `terminalemulation/move-cursor-on-terminal-session`
- **Kind:** native-action
- **Purpose:** Moves cursor on terminal session.

**Use case.** In an AS/400 or mainframe screen, drop **Move cursor on terminal session** on the canvas. Moves cursor on terminal session.

**Demonstration.**

```text
**Move cursor on terminal session**
- Terminal session: `%TerminalSession%`
- Row: `1`
- Column: `Amount`
```

**Analogy.** One tool in that kit: a typewriter conversation: move the carriage, type, wait for the reply.

**In combination.** Open terminal session, Wait for text, Set text / Send key, Close terminal session.

### Open terminal session

- **Id:** `terminalemulation/open-terminal-session`
- **Kind:** native-action
- **Purpose:** Opens terminal session.

**Use case.** In an AS/400 or mainframe screen, drop **Open terminal session** on the canvas. Opens terminal session.

**Demonstration.**

```text
**Open terminal session**
- Provider: `Micro focus reflection`
- HLLAPI DLL path: `C:\RPA\Invoices\INV-1042.pdf`
- Installation path: `C:\RPA\Invoices\INV-1042.pdf`
- Configuration: `Existing profile`
- Session name: `INV-1042`
- Host type: `IBM 3270`
- Profile: `C:\RPA\Invoices\INV-1042.pdf`
- Host address: `INV-1042`
- … 2 more parameter(s) in the action modal
Produces:
- `%TerminalSession%` (Terminal session)
```

**Analogy.** Unlocking the room before you work. Same family as: a typewriter conversation: move the carriage, type, wait for the reply.

**In combination.** Open terminal session, Wait for text, Set text / Send key, Close terminal session. Keep the produced instance/connection and pass it into every later action in this module.

### Search for text on terminal session

- **Id:** `terminalemulation/search-for-text-on-terminal-session`
- **Kind:** native-action
- **Purpose:** Runs **Search for text on terminal session** from the actions pane.

**Use case.** In an AS/400 or mainframe screen, drop **Search for text on terminal session** on the canvas. Runs **Search for text on terminal session** from the actions pane.

**Demonstration.**

```text
**Search for text on terminal session**
- Terminal session: `%TerminalSession%`
- Text to search for: `INV-1042`
- Regular expression: `False`
- Column size: `80`
Produces:
- `%FindResults%` (Datatable)
```

**Analogy.** One tool in that kit: a typewriter conversation: move the carriage, type, wait for the reply.

**In combination.** Open terminal session, Wait for text, Set text / Send key, Close terminal session.

### Send key to terminal session

- **Id:** `terminalemulation/send-key-to-terminal-session`
- **Kind:** native-action
- **Purpose:** Sends key to terminal session.

**Use case.** In an AS/400 or mainframe screen, drop **Send key to terminal session** on the canvas. Sends key to terminal session.

**Demonstration.**

```text
**Send key to terminal session**
- Terminal session: `%TerminalSession%`
- Control key: `Transmit`
```

**Analogy.** Handing a finished envelope to the mailroom.

**In combination.** Open terminal session, Wait for text, Set text / Send key, Close terminal session.

### Set text on terminal session

- **Id:** `terminalemulation/set-text-on-terminal-session`
- **Kind:** native-action
- **Purpose:** Writes text on terminal session.

**Use case.** In an AS/400 or mainframe screen, drop **Set text on terminal session** on the canvas. Writes text on terminal session.

**Demonstration.**

```text
**Set text on terminal session**
- Terminal session: `%TerminalSession%`
- Text: `INV-1042`
- Set text: `Field`
- Get field by: `Label`
- Label: `INV-1042`
- Index: `1`
- Row: `1`
- Column: `Amount`
- … 1 more parameter(s) in the action modal
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Open terminal session, Wait for text, Set text / Send key, Close terminal session.

### Wait for text on terminal session

- **Id:** `terminalemulation/wait-for-text-on-terminal-session`
- **Kind:** native-action
- **Purpose:** Pauses the flow until text on terminal session.

**Use case.** In an AS/400 or mainframe screen, drop **Wait for text on terminal session** on the canvas. Pauses the flow until text on terminal session.

**Demonstration.**

```text
**Wait for text on terminal session**
- Terminal session: `%TerminalSession%`
- Text to wait for: `INV-1042`
- Regular expression: `False`
- Wait for text location: `Screen`
- Get field by: `Label`
- Label: `INV-1042`
- Index: `1`
- Row: `1`
- … 2 more parameter(s) in the action modal
```

**Analogy.** Standing at the microwave until it beeps, so you do not grab a cold plate.

**In combination.** Open terminal session, Wait for text, Set text / Send key, Close terminal session.
