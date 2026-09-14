# CMD session — how each function works

Native Actions pane module **CMD session**.

5 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Close CMD session

- **Id:** `cmd/close-cmd-session`
- **Kind:** native-action
- **Purpose:** Closes CMD session.

**Use case.** In a legacy CLI tool the business still runs overnight, drop **Close CMD session** on the canvas. Closes CMD session.

**Demonstration.**

```text
**Close CMD session**
- CMD session: `%CMDSession%`
```

**Analogy.** Turning out the lights when the work in that room is done.

**In combination.** Open CMD session, Write/Wait/Read, Close CMD session. Call this only after the last use of the instance so you do not break later steps.

### Open CMD session

- **Id:** `cmd/open-cmd-session`
- **Kind:** native-action
- **Purpose:** Opens CMD session.

**Use case.** In a legacy CLI tool the business still runs overnight, drop **Open CMD session** on the canvas. Opens CMD session.

**Demonstration.**

```text
**Open CMD session**
- Working folder: `C:\RPA\Invoices`
- Change code page: `False`
- Encoding: `utf-8 : Unicode (UTF-8)`
Produces:
- `%CmdSession%` (CMD session)
```

**Analogy.** Unlocking the room before you work. Same family as: dictating commands to a clerk at a terminal and waiting for the printout.

**In combination.** Open CMD session, Write/Wait/Read, Close CMD session. Keep the produced instance/connection and pass it into every later action in this module.

### Read from CMD session

- **Id:** `cmd/read-from-cmd-session`
- **Kind:** native-action
- **Purpose:** Reads from CMD session.

**Use case.** In a legacy CLI tool the business still runs overnight, drop **Read from CMD session** on the canvas. Reads from CMD session.

**Demonstration.**

```text
**Read from CMD session**
- CMD session: `%CMDSession%`
- Separate output from error: `False`
Produces:
- `%CmdOutput%` (Text value)
- `%CmdError%` (Text value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Open CMD session, Write/Wait/Read, Close CMD session.

### Wait for text on CMD session

- **Id:** `cmd/wait-for-text-on-cmd-session`
- **Kind:** native-action
- **Purpose:** Pauses the flow until text on CMD session.

**Use case.** In a legacy CLI tool the business still runs overnight, drop **Wait for text on CMD session** on the canvas. Pauses the flow until text on CMD session.

**Demonstration.**

```text
**Wait for text on CMD session**
- CMD session: `%CMDSession%`
- Text to wait: `INV-1042`
- Is regular expression: `False`
- Ignore case: `True`
- Timeout: `30`
```

**Analogy.** Standing at the microwave until it beeps, so you do not grab a cold plate.

**In combination.** Open CMD session, Write/Wait/Read, Close CMD session.

### Write to CMD session

- **Id:** `cmd/write-to-cmd-session`
- **Kind:** native-action
- **Purpose:** Writes to CMD session.

**Use case.** In a legacy CLI tool the business still runs overnight, drop **Write to CMD session** on the canvas. Writes to CMD session.

**Demonstration.**

```text
**Write to CMD session**
- CMD session: `%CMDSession%`
- Command: `INV-1042`
- Send **Enter** after command: `True`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Open CMD session, Write/Wait/Read, Close CMD session.
