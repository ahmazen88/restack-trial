# Triggers — how each function works

Native Actions pane module **Triggers**.

1 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### UI element event trigger

- **Id:** `triggers/ui-element-event-trigger`
- **Kind:** native-action
- **Purpose:** Pauses the flow until a mouse click or key event occurs on a chosen UI element, then runs the nested actions.

**Use case.** In starting nested steps when a user clicks a control, drop **UI element event trigger** on the canvas. Pauses the flow until a mouse click or key event occurs on a chosen UI element, then runs the nested actions.

**Demonstration.**

```text
**UI element event trigger**
- Trigger name: `INV-1042`
- UI element: `UI element: Submit button`
- Event: `(set in designer)`
- Scheduling mode: `(set in designer)`
- Fail with timeout error: `True`
Produces:
- `%TriggerEventInstanceHandle%` (TriggerEventInstanceHandle)
Place the actions that should run inside this block, then End.
```

**Analogy.** One tool in that kit: a doorbell: the house stays quiet until someone presses it.

**In combination.** UI element event trigger wraps the actions that should run after the click or key.
