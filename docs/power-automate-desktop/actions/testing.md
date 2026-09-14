# Testing

Build desktop-flow test cases with Assert and Test a desktop flow.

- Actions in this module: **2**
- Official docs: [Testing actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/testing)

## Actions

### Test a desktop flow

Test a desktop flow that receives input variables and might produce output variables.

Designer name: **Test a desktop flow**. Official reference: [Testing / Test a desktop flow](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/testing#runtestflow).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Desktop flow | Required | Desktop flow | — |

**Outputs**

| Variable | Type |
|---|---|
| (flow outputs) | * |

No module-specific exceptions are listed for this action.

---

### Assert

Validates output against expected results using operators like equals, contains, or greater than.

Designer name: **Assert**. Official reference: [Testing / Assert](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/testing#assertaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Assert expression | Optional | Text value | — |
| Assert message | Optional | Text value | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---
