# Power Automate secret variables

Fetch credentials stored in the Power Automate environment.

- Actions in this module: **1**
- Official docs: [Power Automate secret variables actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/powerautomatesecretvariables)

## Actions

### Get credential

Returns the values of a credential created through Power Automate's portal page for this environment.

Designer name: **Get credential**. Official reference: [Power Automate secret variables / Get credential](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/powerautomatesecretvariables#getcredentialaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Credential | Required | Text value | — |
| Timeout | Required | Numeric value | 0 |

**Outputs**

| Variable | Type |
|---|---|
| Credential | Credential |

**On error:** `Failed to get credential`, `Invalid credentials configuration`, `Credential timed out`, `Failed to contact credentials vault`.

---
