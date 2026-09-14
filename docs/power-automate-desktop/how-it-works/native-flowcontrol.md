# Flow control — how each function works

Native Actions pane module **Flow control**.

14 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Comment

- **Id:** `flowcontrol/comment`
- **Kind:** native-action
- **Purpose:** Adds a note on the canvas. It does not run.

**Use case.** In a long flow that must pause, jump, or fail in a controlled way, drop **Comment** on the canvas. Adds a note on the canvas. It does not run.

**Demonstration.**

```text
**Comment**
- Comment: `Processed by desktop flow Close-P9`
```

**Analogy.** One tool in that kit: stage directions in a play: wait, jump to a scene, or stop the show.

**In combination.** Use Wait, Label/Go to, Run subflow, On block error, and Stop flow together.

### End

- **Id:** `flowcontrol/end`
- **Kind:** native-action
- **Purpose:** Closes the current block (condition, loop, or error block).

**Use case.** In a long flow that must pause, jump, or fail in a controlled way, drop **End** on the canvas. Closes the current block (condition, loop, or error block).

**Demonstration.**

```text
**End**
- (no inputs)
```

**Analogy.** One tool in that kit: stage directions in a play: wait, jump to a scene, or stop the show.

**In combination.** Use Wait, Label/Go to, Run subflow, On block error, and Stop flow together.

### End region

- **Id:** `flowcontrol/end-region`
- **Kind:** native-action
- **Purpose:** Ends region.

**Use case.** In a long flow that must pause, jump, or fail in a controlled way, drop **End region** on the canvas. Ends region.

**Demonstration.**

```text
**End region**
- (no inputs)
```

**Analogy.** Turning out the lights when the work in that room is done.

**In combination.** Use Wait, Label/Go to, Run subflow, On block error, and Stop flow together. Call this only after the last use of the instance so you do not break later steps.

### Exit subflow

- **Id:** `flowcontrol/exit-subflow`
- **Kind:** native-action
- **Purpose:** Returns from the current subflow to its caller.

**Use case.** In a long flow that must pause, jump, or fail in a controlled way, drop **Exit subflow** on the canvas. Returns from the current subflow to its caller.

**Demonstration.**

```text
**Exit subflow**
- (no inputs)
```

**Analogy.** One tool in that kit: stage directions in a play: wait, jump to a scene, or stop the show.

**In combination.** Use Wait, Label/Go to, Run subflow, On block error, and Stop flow together.

### Get last error

- **Id:** `flowcontrol/get-last-error`
- **Kind:** native-action
- **Purpose:** Reads last error into a flow variable.

**Use case.** In a long flow that must pause, jump, or fail in a controlled way, drop **Get last error** on the canvas. Reads last error into a flow variable.

**Demonstration.**

```text
**Get last error**
- Clear error: `False`
Produces:
- `%LastError%` (Error)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Use Wait, Label/Go to, Run subflow, On block error, and Stop flow together.

### Go to

- **Id:** `flowcontrol/go-to`
- **Kind:** native-action
- **Purpose:** Jumps execution to a Label in the same subflow.

**Use case.** In a long flow that must pause, jump, or fail in a controlled way, drop **Go to** on the canvas. Jumps execution to a Label in the same subflow.

**Demonstration.**

```text
**Go to**
- Go to label: `INV-1042`
```

**Analogy.** One tool in that kit: stage directions in a play: wait, jump to a scene, or stop the show.

**In combination.** Use Wait, Label/Go to, Run subflow, On block error, and Stop flow together.

### If safe stop requested

- **Id:** `flowcontrol/if-safe-stop-requested`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when safe stop requested.

**Use case.** In a long flow that must pause, jump, or fail in a controlled way, drop **If safe stop requested** on the canvas. Opens a conditional branch that runs when safe stop requested.

**Demonstration.**

```text
**If safe stop requested**
- Stop the flow: `False`
Place the actions that should run inside this block, then End.
```

**Analogy.** Checking a condition on a clipboard before you choose a door.

**In combination.** Use Wait, Label/Go to, Run subflow, On block error, and Stop flow together. Combine with Else / Else if and End. Put Wait or If file exists before brittle UI/browser steps.

### Label

- **Id:** `flowcontrol/label`
- **Kind:** native-action
- **Purpose:** Named jump target for a Go to action.

**Use case.** In a long flow that must pause, jump, or fail in a controlled way, drop **Label** on the canvas. Named jump target for a Go to action.

**Demonstration.**

```text
**Label**
- Label name: `INV-1042`
```

**Analogy.** One tool in that kit: stage directions in a play: wait, jump to a scene, or stop the show.

**In combination.** Use Wait, Label/Go to, Run subflow, On block error, and Stop flow together.

### On block error

- **Id:** `flowcontrol/on-block-error`
- **Kind:** native-action
- **Purpose:** Starts a block whose nested failures are handled together.

**Use case.** Catch failures from a group of actions and email, log, or retry instead of dying.

**Demonstration.**

```text
**On block error**
- Name: `INV-1042`
- Retry policy: `None`
- Handle flow terminating errors: `False`
Place the actions that should run inside this block, then End.
```

**Analogy.** A safety net under a trapeze act.

**In combination.** Use Wait, Label/Go to, Run subflow, On block error, and Stop flow together.

### Region

- **Id:** `flowcontrol/region`
- **Kind:** native-action
- **Purpose:** Starts a named visual group of actions.

**Use case.** In a long flow that must pause, jump, or fail in a controlled way, drop **Region** on the canvas. Starts a named visual group of actions.

**Demonstration.**

```text
**Region**
- Name: `INV-1042`
Place the actions that should run inside this block, then End.
```

**Analogy.** One tool in that kit: stage directions in a play: wait, jump to a scene, or stop the show.

**In combination.** Use Wait, Label/Go to, Run subflow, On block error, and Stop flow together.

### Run subflow

- **Id:** `flowcontrol/run-subflow`
- **Kind:** native-action
- **Purpose:** Runs subflow.

**Use case.** Call a named slice of this flow (Extract, Transform, Load) without copy-paste.

**Demonstration.**

```text
**Run subflow**
- Subflow name: `(set in designer)`
- Input as expression: `False`
```

**Analogy.** One tool in that kit: stage directions in a play: wait, jump to a scene, or stop the show.

**In combination.** Use Wait, Label/Go to, Run subflow, On block error, and Stop flow together.

### Stop flow

- **Id:** `flowcontrol/stop-flow`
- **Kind:** native-action
- **Purpose:** Stops flow.

**Use case.** In a long flow that must pause, jump, or fail in a controlled way, drop **Stop flow** on the canvas. Stops flow.

**Demonstration.**

```text
**Stop flow**
- End flow: `Successfully`
- Error message: `Processed by desktop flow Close-P9`
```

**Analogy.** One tool in that kit: stage directions in a play: wait, jump to a scene, or stop the show.

**In combination.** Use Wait, Label/Go to, Run subflow, On block error, and Stop flow together.

### Throw custom error

- **Id:** `flowcontrol/throw-custom-error`
- **Kind:** native-action
- **Purpose:** Raises a maker-defined error for On block error to catch.

**Use case.** In a long flow that must pause, jump, or fail in a controlled way, drop **Throw custom error** on the canvas. Raises a maker-defined error for On block error to catch.

**Demonstration.**

```text
**Throw custom error**
- Error name: `None`
- Error message: `Processed by desktop flow Close-P9`
```

**Analogy.** Pulling the fire alarm on purpose so the net can catch it.

**In combination.** Use Wait, Label/Go to, Run subflow, On block error, and Stop flow together.

### Wait

- **Id:** `flowcontrol/wait`
- **Kind:** native-action
- **Purpose:** Pauses the flow for a number of seconds.

**Use case.** In a long flow that must pause, jump, or fail in a controlled way, drop **Wait** on the canvas. Pauses the flow for a number of seconds.

**Demonstration.**

```text
**Wait**
- Duration: `30`
```

**Analogy.** Setting a kitchen timer and not touching the next step until it rings.

**In combination.** Use Wait, Label/Go to, Run subflow, On block error, and Stop flow together.
