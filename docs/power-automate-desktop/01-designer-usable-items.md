# Designer and console usable items

These are the surfaces you actually click in Power Automate for desktop. They are not actions, but every flow uses them.

## Flow designer

### Actions pane

Left-side catalog. Actions are grouped in modules (Variables, Excel, UI automation, …). Search matches action names and module names (two or more characters). Star an action to pin it under favorites.

### Workspace canvas

The ordered list of actions for the **active subflow**. Drag to reorder. Disabled actions are skipped at runtime. Double-click an action to open its modal.

### Subflows

Every flow has **Main**. Add more tabs for reusable chunks. Call them with **Run subflow**. The name can be a variable so the callee is chosen at runtime. Main always stays first in the tab list.

### Variables pane

Three groups:

- **Input variables** — values the caller (console, cloud flow, or another desktop flow) must or may pass in. Can be optional, sensitive, and typed (text, number, boolean, list, datatable, custom object, instance/session).
- **Output variables** — values returned to the caller.
- **Flow variables** — created by **Set variable** or produced by actions.

Mark secrets as **sensitive** so the designer and logs mask them.

### UI elements pane

Captured **desktop** and **web** locators. UI automation actions take desktop elements; browser actions take web elements. Each element has one or more **selectors**. Capture modes: UIA (default), UIA3 Raw, MSAA (legacy apps).

**UI element collections** share locators across flows in the environment.

### Images pane

Bitmaps used by **Move mouse to image**, **Wait for image**, **If image**, and OCR subregion search. Capture immediately or on a timer. Unused images can be bulk-removed.

### Errors pane

Design-time configuration errors and run-time exceptions, with subflow and line. Double-click for correlation id and (for some Excel errors) suggested fixes.

### Action modal

Every action has:

- **Input parameters** — text, dropdowns, toggles, UI elements, images.
- **Variables produced** — named outputs.
- **On error** — continue, throw, retry, go to label, set a variable.

### Debugging

- **Run** the whole flow from the designer.
- **Run from here** starts at the selected action.
- **Step** runs one action.
- **Breakpoints** pause on a line.
- The variables viewer shows live values.

### Recorders

- **Desktop recorder** emits UI automation actions from clicks and typing.
- **Web recorder** emits browser automation actions.

Recorders are a fast way to capture locators; you still tidy selectors and waits afterward.

### Copilot / natural language

Describe a task in plain language to draft actions or Power Fx. Availability depends on region and admin Copilot settings.

### Assets library

Add extra **cloud connectors** and **custom actions** (uploaded .NET packages) so they appear in the actions pane.

### Custom forms designer

Layout editor used by **Display custom form** (labels, inputs, drop-downs, file pickers, buttons).

### Power Fx toggle

Created per flow. Classic flows use `%Expression%`. Power Fx flows use `=` formulas, 1-based `Index`, and case-sensitive names. You cannot mix the two languages in one flow.

## Console (PAD home window)

### My flows / Shared with me

Create, edit, run, stop, rename, and see last run status.

### Examples

Starter flows that ship with the product.

### Keyboard shortcut run

Bind a hotkey so the flow starts without opening the designer.

### URL / scheme run

Start a flow from a `ms-powerautomate://` (or similar) shortcut.

### Machine registration

Register this PC so **cloud flows** can start it attended or unattended.

### Machine groups and hosted machines

Pool local PCs, or use Microsoft-hosted bots, for unattended scale-out.

## Runtime controls

### Safe stop

From the portal run details (or designer), request a cooperative stop. The flow notices it only if it contains **If safe stop requested**.

### Connection references

Cloud connector actions need a connection. Co-owners can **embed** a connection in the flow; run-only users **bring their own** at console run time.

### Credentials

Resolve secrets from the Power Automate portal, **Azure Key Vault**, or **CyberArk** rather than storing passwords in the flow.

### Environment variables

Read environment-scoped text, number, boolean, JSON, or secret values with **Retrieve environment variable**. Secrets are resolved only at runtime and are not logged.

### Work queues

Shared item lists processed by one or more unattended machines. Native actions add, dequeue, update, requeue, and filter items.

### Selectors

The real identity of a UI/web element. Text-based selectors can include variables. Power Fx flows can interpolate `${ formula }` inside a selector.

## Item index

| Item | Purpose |
| --- | --- |
| Actions pane | Catalog of modules and actions, with search and favorites. |
| Workspace canvas | Ordered list of deployed actions for the active subflow. |
| Subflows | Tabs besides Main; invoke with Run subflow, including dynamic names. |
| Variables pane | Input, output, and flow variables, including sensitive and optional flags. |
| UI elements pane | Captured desktop and web elements plus their selectors. |
| UI element collections | Reusable shared UI element sets across flows. |
| Images pane | Captured bitmaps used by image-based mouse and wait actions. |
| Errors pane | Design-time and run-time errors and warnings with line and subflow. |
| Action modal | Inputs, produced variables, and On error handling for one action. |
| On error handling | Retry, continue, throw, or go-to-label when an action fails. |
| Breakpoints | Pause a designer run on a chosen action. |
| Run / Run from here / Step | Designer debug controls for the current flow. |
| Desktop recorder | Capture clicks and typing against desktop apps as UI actions. |
| Web recorder | Capture browser interactions as web automation actions. |
| Copilot / natural language | Describe a task in English to draft actions or Power Fx. |
| Assets library | Add extra cloud connectors and custom actions to the pane. |
| Custom actions | Environment-level action groups uploaded by the organization. |
| Credentials | Portal, Azure Key Vault, or CyberArk secrets resolved at runtime. |
| Connection references | Cloud connector connections embedded or brought-your-own. |
| Environment variables | Text, number, JSON, boolean, or secret values from the environment. |
| Work queues | Orchestrated item processing across unattended machines. |
| Console - My flows | Create, run, stop, and schedule desktop flows on this machine. |
| Console - examples | Starter flows shipped with PAD. |
| Keyboard shortcut run | Start a flow from a hotkey registered in the console. |
| URL / scheme run | Start a flow from a PAD URL shortcut. |
| Machine registration | Register this PC for attended or unattended cloud-initiated runs. |
| Machine groups | Pool machines for unattended scale-out. |
| Hosted machines / groups | Microsoft-hosted bots for unattended runs. |
| Flow designer menus | Save, save as, undo/redo, find, comments, and enable/disable actions. |
| Safe stop | Cooperative stop check via If safe stop requested. |
| Sensitive variables | Mask values in logs and the variables viewer. |
| Input / output variables | Contract used when a cloud or desktop flow calls this flow. |
| Selectors | Text-based locators behind UI and web elements. |
| Custom forms designer | Layout used by Display custom form. |
| Power Fx toggle | Per-flow choice of classic % expressions versus Power Fx. |
