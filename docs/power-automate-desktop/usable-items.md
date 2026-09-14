# Usable items in Power Automate for desktop

Actions are only one pane. This page lists every **kind of thing you can use** while building or running a desktop flow.

## Console (before the designer)

| Item | What you do with it |
|---|---|
| My flows | Create, edit, copy, run, stop, and delete desktop flows. |
| New flow | Names the flow and optionally enables **Power Fx**. That choice is permanent for the flow. |
| Examples | Microsoft sample flows. |
| Shared with me | Flows others own that you can run or co-own. |
| Monitor / run history | Open recent runs and logs. |
| Machines / machine groups | Register the PC that will run attended or unattended flows. |
| Assets library | Environment custom actions and UI element collections. |
| Settings | Console, recording, and update options. |
| Copilot (console) | Describe a flow in natural language to draft actions. |

## Designer chrome

| Item | What you do with it |
|---|---|
| Actions pane | Search (`Ctrl+F` focuses designer search; the pane has its own search) and drag actions. Mark favorites. |
| Workspace | Ordered list of actions in the current subflow. Drag to reorder. Disable to skip at runtime. |
| Subflow tabs | `Main` plus any extra subflows. `Run subflow` jumps into another tab. |
| Variables pane | Input, output, and flow variables; captured UI/web values; sensitive flags. |
| UI elements pane | Desktop and web selectors used by UI / browser actions. |
| Images pane | Screenshots used by image actions (`If image`, `Wait for image`, `Move mouse to image`). |
| Recorder | Desktop recorder and web recorder drop UI or browser actions into the workspace. |
| Copilot in designer | Draft or explain actions; natural language to script / Power Fx where enabled. |
| Flow checker | Static analysis (unused variables, empty blocks, and similar issues). |
| Breakpoints / debug run | Run, run from here, step, and inspect variables. |
| Errors pane | Failed action, message, and subflow location. |

## Flow structure items

| Item | Notes |
|---|---|
| Main subflow | Always runs first. Cannot be renamed or reordered off the top. |
| Additional subflows | Called with **Run subflow**. Support a dynamic subflow name. |
| Input variables | Values the parent cloud flow, another desktop flow, or the console supplies. |
| Output variables | Values returned to the caller. |
| Flow variables | Created by **Set variable** or produced by actions. |
| Sensitive variables | Masked in logs (passwords, secrets). |
| Scoped variables | Limit visibility to a subflow where supported. |
| Regions | **Region** / **End region** — visual grouping only. |
| Labels + Go to | Jump to a named point. Avoid inside error blocks and across subflows. |
| On block error | Catch action failures, retries, custom errors. |
| Throw custom error | Raise a named error that **On block error** handles. |
| Comment | Non-executing note on the canvas. |

## UI automation assets

| Item | Notes |
|---|---|
| Desktop UI element | Selector for a Windows control. Used by UI automation actions. |
| Web UI element | Selector for a DOM element. Used by browser automation. |
| Selector editor | Edit attributes, add fallback selectors, test, and repair. |
| UI element collections | Share selectors across flows in an environment. |
| Image | Bitmap used when the control has no reliable selector. |
| Window instance | Handle produced by **Get window** / launch actions. |
| Browser instance | Produced by **Launch new Edge/Chrome/Firefox/IE**. |

## Security and configuration assets

| Item | Notes |
|---|---|
| Credential (environment) | **Get credential** — username/password from Power Automate. |
| CyberArk credential | **Get password from CyberArk**. |
| Environment variable | **Retrieve environment variable** (text, number, boolean, JSON, secret). |
| Connection / connection reference | Required by cloud connector, SharePoint, and Office 365 Outlook operations. |
| Embedded connection references | Let co-owners run the same connector actions. |
| Custom action module | `.dll` uploaded to the environment; appears as extra pane groups. |

## Recorders and authoring helpers

| Item | Produces |
|---|---|
| Desktop recorder | UI automation actions + UI elements. |
| Web recorder | Browser automation actions + web elements. |
| AI recorder | Draft flow from a recorded session (where available). |
| Record into current flow | Inserts at the cursor instead of creating a new flow. |

## Run-time and operations items (not on the canvas)

These are usable, but they live outside the action list:

| Item | Notes |
|---|---|
| Attended run | User is at the console / machine. |
| Unattended run | Cloud or schedule starts the flow on a registered machine. |
| Picture-in-picture | Run in an isolated Windows session on the same PC. |
| Safe stop | Request a controlled stop; handle with **If safe stop requested**. |
| Work queues | Queue items processed by **Work queues** actions or cloud triggers. |
| Keyboard shortcut / URL / desktop shortcut | Start a flow without opening the designer. |
| Cloud flow trigger | **Run a flow built with Power Automate for desktop** from a cloud flow. |
| Tags | Organize flows in the console. |
| Version control (preview) | Flow versions where enabled. |
| Test cases | **Testing** module: **Assert**, **Test a desktop flow**. |

## Data you pass around

See [data types](functions/data-types.md) and [properties](functions/data-type-properties.md). The types you will use constantly:

- Text, number, boolean, datetime
- List, datatable, datarow, custom object
- File, folder, binary data
- Instances (Excel, Word, Outlook, browser, SQL, FTP, CMD, terminal, Access, SAP)
- Mail messages, credentials, error objects

## Reserved words (cannot be variable names)

`ACTION`, `AND`, `AS`, `BLOCK`, `CALL`, `CASE`, `DEFAULT`, `DISABLE`, `ELSE`, `END`, `ERROR`, `EXIT`, `FALSE`, `FOR`, `FOREACH`, `FROM`, `FUNCTION`, `GLOBAL`, `GOTO`, `IF`, `IMPORT`, `IN`, `INPUT`, `LABEL`, `LOOP`, `MAIN`, `MOD`, `NEXT`, `NO`, `NOT`, `ON`, `OR`, `OUTPUT`, `REPEAT`, `SET`, `STEP`, `SWITCH`, `THEN`, `THROW`, `TIMES`, `TO`, `TRUE`, `WAIT`, `WHILE`, `XOR`, `YES`

Keywords are case-insensitive. Full list: [Reserved keywords](https://learn.microsoft.com/en-us/power-automate/desktop-flows/reserved-keywords).

## What is not a PAD “function”

These look similar in conversation and are **out of scope** for this catalog:

- Power Automate **cloud** connector actions used only in make.powerautomate.com cloud flows (unless added through the desktop **Cloud connectors** pane).
- Power Apps formulas that are not in the [desktop-flow formula list](functions/power-fx.md).
- Windows APIs you call only from **Run PowerShell** / **Run .NET script**.
