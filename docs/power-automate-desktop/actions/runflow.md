# Run flow

Call another desktop flow and wait for its outputs.

- Actions in this module: **1**
- Official docs: [Run flow actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/runflow)

## Actions

### Run desktop flow

Runs a desktop flow that can receive input variables and might produce output variables.

Designer name: **Run desktop flow**. Official reference: [Run flow / Run desktop flow](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/runflow#runflow).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Desktop flow | Required | Desktop flow | — |
| Wait for flow to complete | Choice | Boolean value | True |

**Outputs**

| Variable | Type |
|---|---|
| (flow outputs) | * |

**On error:** `Run desktop flow failed`, `Desktop flow timed out`.

---
