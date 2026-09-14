# Scripting — how each function works

Native Actions pane module **Scripting**.

6 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Run .NET script

- **Id:** `scripting/run-net-script`
- **Kind:** native-action
- **Purpose:** Runs .NET script.

**Use case.** In a one-liner PowerShell or Python cannot express as PAD actions, drop **Run .NET script** on the canvas. Runs .NET script.

**Demonstration.**

```text
**Run .NET script**
- Language: `C#`
- .NET script imports: `INV-1042`
- References to be loaded: `(set in designer)`
- Script parameters: `(set in designer)`
- .NET code to run: `INV-1042`
```

**Analogy.** One tool in that kit: stepping into a side workshop for a custom tool, then returning with the part.

**In combination.** Run PowerShell/Python/.NET and capture output variables; keep scripts short.

### Run DOS command

- **Id:** `scripting/run-dos-command`
- **Kind:** native-action
- **Purpose:** Runs DOS command.

**Use case.** In a one-liner PowerShell or Python cannot express as PAD actions, drop **Run DOS command** on the canvas. Runs DOS command.

**Demonstration.**

```text
**Run DOS command**
- DOS command or application: `(set in designer)`
- Working folder: `C:\RPA\Invoices`
- Fail after timeout: `True`
- Timeout: `30`
- Change code page: `False`
- Encoding: `utf-8: Unicode (UTF-8)`
Produces:
- `%CommandOutput%` (Text value)
- `%CommandErrorOutput%` (Text value)
- `%CommandExitCode%` (Numeric value)
```

**Analogy.** One tool in that kit: stepping into a side workshop for a custom tool, then returning with the part.

**In combination.** Run PowerShell/Python/.NET and capture output variables; keep scripts short.

### Run JavaScript

- **Id:** `scripting/run-javascript`
- **Kind:** native-action
- **Purpose:** Runs javaScript.

**Use case.** In a one-liner PowerShell or Python cannot express as PAD actions, drop **Run JavaScript** on the canvas. Runs javaScript.

**Demonstration.**

```text
**Run JavaScript**
- JavaScript to run: `INV-1042`
- Fail after timeout: `True`
- Timeout: `30`
Produces:
- `%JavascriptOutput%` (Text value)
- `%ScriptError%` (Text value)
```

**Analogy.** One tool in that kit: stepping into a side workshop for a custom tool, then returning with the part.

**In combination.** Run PowerShell/Python/.NET and capture output variables; keep scripts short.

### Run PowerShell script

- **Id:** `scripting/run-powershell-script`
- **Kind:** native-action
- **Purpose:** Runs powerShell script.

**Use case.** In a one-liner PowerShell or Python cannot express as PAD actions, drop **Run PowerShell script** on the canvas. Runs powerShell script.

**Demonstration.**

```text
**Run PowerShell script**
- PowerShell code to run: `INV-1042`
- Fail after timeout: `True`
- Timeout: `30`
Produces:
- `%PowershellOutput%` (Text value)
- `%ScriptError%` (Text value)
```

**Analogy.** One tool in that kit: stepping into a side workshop for a custom tool, then returning with the part.

**In combination.** Run PowerShell/Python/.NET and capture output variables; keep scripts short.

### Run Python script

- **Id:** `scripting/run-python-script`
- **Kind:** native-action
- **Purpose:** Runs python script.

**Use case.** In a one-liner PowerShell or Python cannot express as PAD actions, drop **Run Python script** on the canvas. Runs python script.

**Demonstration.**

```text
**Run Python script**
- Python script to run: `INV-1042`
- Python version: `Python 2.7`
- Module folder paths: `%Files%`
Produces:
- `%PythonScriptOutput%` (Text value)
- `%ScriptError%` (Text value)
```

**Analogy.** One tool in that kit: stepping into a side workshop for a custom tool, then returning with the part.

**In combination.** Run PowerShell/Python/.NET and capture output variables; keep scripts short.

### Run VBScript

- **Id:** `scripting/run-vbscript`
- **Kind:** native-action
- **Purpose:** Runs VBScript.

**Use case.** In a one-liner PowerShell or Python cannot express as PAD actions, drop **Run VBScript** on the canvas. Runs VBScript.

**Demonstration.**

```text
**Run VBScript**
- VBScript to run: `INV-1042`
- Fail after timeout: `N/A`
- Timeout: `30`
Produces:
- `%VBScriptOutput%` (Text value)
- `%ScriptError%` (Text value)
```

**Analogy.** One tool in that kit: stepping into a side workshop for a custom tool, then returning with the part.

**In combination.** Run PowerShell/Python/.NET and capture output variables; keep scripts short.
