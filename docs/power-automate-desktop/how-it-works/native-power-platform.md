# Power Platform — how each function works

Native Actions pane module **Power Platform**.

1 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Run Power App (preview)

- **Id:** `power-platform/run-power-app`
- **Kind:** native-action
- **Purpose:** Launches a canvas app from the desktop flow, passes values in, and collects values the app returns. Needs PAD 2.68+.

**Use case.** In an attended form that is nicer than Display custom form, drop **Run Power App (preview)** on the canvas. Launches a canvas app from the desktop flow, passes values in, and collects values the app returns. Needs PAD 2.68+.

**Demonstration.**

```text
**Run Power App (preview)**
- App: `(set in designer)`
```

**Analogy.** One tool in that kit: handing the customer a tablet app, then taking the filled clipboard back.

**In combination.** Run Power App, pass inputs, read outputs when the user closes the app.
