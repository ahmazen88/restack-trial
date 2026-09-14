# System — how each function works

Native Actions pane module **System**.

8 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Delete Windows environment variable

- **Id:** `system/delete-windows-environment-variable`
- **Kind:** native-action
- **Purpose:** Deletes windows environment variable.

**Use case.** In starting a local EXE or killing a hung process, drop **Delete Windows environment variable** on the canvas. Deletes windows environment variable.

**Demonstration.**

```text
**Delete Windows environment variable**
- Environment variable name: `INV-1042`
- Type: `User`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Run application, Wait for process, Terminate process if it hangs.

### Get Windows environment variable

- **Id:** `system/get-windows-environment-variable`
- **Kind:** native-action
- **Purpose:** Reads windows environment variable into a flow variable.

**Use case.** In starting a local EXE or killing a hung process, drop **Get Windows environment variable** on the canvas. Reads windows environment variable into a flow variable.

**Demonstration.**

```text
**Get Windows environment variable**
- Environment variable name: `INV-1042`
- Search for variable only in scope: `False`
- Scope: `User`
Produces:
- `%EnvironmentVariableValue%` (Text value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Run application, Wait for process, Terminate process if it hangs.

### If process

- **Id:** `system/if-process`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when process.

**Use case.** In starting a local EXE or killing a hung process, drop **If process** on the canvas. Opens a conditional branch that runs when process.

**Demonstration.**

```text
**If process**
- If process: `Is running`
- Process name: `INV-1042`
- From User: `False`
- User name: `CONTOSO\rpa.bot`
Place the actions that should run inside this block, then End.
```

**Analogy.** Checking a condition on a clipboard before you choose a door.

**In combination.** Run application, Wait for process, Terminate process if it hangs. Combine with Else / Else if and End. Put Wait or If file exists before brittle UI/browser steps.

### Ping

- **Id:** `system/ping`
- **Kind:** native-action
- **Purpose:** Checks whether a remote host answers on the network.

**Use case.** In starting a local EXE or killing a hung process, drop **Ping** on the canvas. Checks whether a remote host answers on the network.

**Demonstration.**

```text
**Ping**
- Host name: `INV-1042`
- Timeout: `30`
Produces:
- `%PingResult%` (Text value)
- `%RoundTripTime%` (Numeric value)
```

**Analogy.** One tool in that kit: launching a program from the Start menu or ending it in Task Manager.

**In combination.** Run application, Wait for process, Terminate process if it hangs.

### Run application

- **Id:** `system/run-application`
- **Kind:** native-action
- **Purpose:** Runs application.

**Use case.** In starting a local EXE or killing a hung process, drop **Run application** on the canvas. Runs application.

**Demonstration.**

```text
**Run application**
- Application path: `C:\RPA\Invoices\INV-1042.pdf`
- Command line arguments: `INV-1042`
- Working folder: `C:\RPA\Invoices`
- Window style: `Normal`
- After application launch: `Continue immediately`
- Timeout: `30`
Produces:
- `%AppProcessId%` (Numeric value)
- `%AppExitCode%` (Numeric value)
- `%WindowHandle%` (Numeric value)
```

**Analogy.** One tool in that kit: launching a program from the Start menu or ending it in Task Manager.

**In combination.** Run application, Wait for process, Terminate process if it hangs.

### Set Windows environment variable

- **Id:** `system/set-windows-environment-variable`
- **Kind:** native-action
- **Purpose:** Writes windows environment variable.

**Use case.** In starting a local EXE or killing a hung process, drop **Set Windows environment variable** on the canvas. Writes windows environment variable.

**Demonstration.**

```text
**Set Windows environment variable**
- Environment variable name: `INV-1042`
- New environment variable value: `INV-1042`
- Type: `User`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Run application, Wait for process, Terminate process if it hangs.

### Terminate process

- **Id:** `system/terminate-process`
- **Kind:** native-action
- **Purpose:** Immediately stops a running process.

**Use case.** In starting a local EXE or killing a hung process, drop **Terminate process** on the canvas. Immediately stops a running process.

**Demonstration.**

```text
**Terminate process**
- Specify process by: `Process name`
- Process ID: `1`
- Process name: `INV-1042`
- From User: `False`
- User name: `CONTOSO\rpa.bot`
```

**Analogy.** One tool in that kit: launching a program from the Start menu or ending it in Task Manager.

**In combination.** Run application, Wait for process, Terminate process if it hangs.

### Wait for process

- **Id:** `system/wait-for-process`
- **Kind:** native-action
- **Purpose:** Pauses the flow until process.

**Use case.** In starting a local EXE or killing a hung process, drop **Wait for process** on the canvas. Pauses the flow until process.

**Demonstration.**

```text
**Wait for process**
- Process name: `INV-1042`
- From User: `False`
- User name: `CONTOSO\rpa.bot`
- Wait for process to: `Start`
- Fail with timeout error: `False`
```

**Analogy.** Standing at the microwave until it beeps, so you do not grab a cold plate.

**In combination.** Run application, Wait for process, Terminate process if it hangs.
