# Triggers

Pause until a configured mouse or keyboard event hits a UI element.

This page documents every **native action** in this group (1 items).

## Actions

### UI element event trigger

- **Inventory id:** `triggers/ui-element-event-trigger`
- **Kind:** native-action
- **Purpose:** Pauses the flow until a mouse click or key event occurs on a chosen UI element, then runs the nested actions.
- **Key inputs:** `Trigger name` (Text); `UI element` (UI element); `Event` (Mouse click, Keyboard); `Scheduling mode` (One time, Sequential); `Fail with timeout error` (Boolean)
- **Produces:** `TriggerEventInstanceHandle` (TriggerEventInstanceHandle)
- **Exceptions:** `UI element event trigger failed`; `UI element event trigger failed with timeout error`
- **Microsoft Learn:** [UI element event trigger](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/triggers#ui-element-event-trigger)
