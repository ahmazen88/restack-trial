# Loops

Repeat actions with Loop, Loop condition, and For each.

- Actions in this module: **5**
- Official docs: [Loops actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)

## Actions

### Exit loop

Stops the loop and the flow resumes at the next action or statement following the loop.

Designer name: **Exit loop**. Official reference: [Loops / Exit loop](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops#break).

This action has no input parameters.

Produces no variables.

No module-specific exceptions are listed for this action.

---

### For each

Iterates over items in a list, data table or data row, allowing a block of actions to be executed repeatedly.

Designer name: **For each**. Official reference: [Loops / For each](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops#foreach).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Value to iterate | Required | * | — |

**Outputs**

| Variable | Type |
|---|---|
| (designer-named) | * |

No module-specific exceptions are listed for this action.

---

### Loop

Iterates a block of actions for a specified number of times.

Designer name: **Loop**. Official reference: [Loops / Loop](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops#loop).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Start from | Required | Numeric value | — |
| Increment by | Required | Numeric value | — |
| End to | Required | Numeric value | — |

**Outputs**

| Variable | Type |
|---|---|
| (designer-named) | * |

No module-specific exceptions are listed for this action.

---

### Loop condition

Iterates a block of actions as long as a specified condition proves to be true.

Designer name: **Loop condition**. Official reference: [Loops / Loop condition](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops#while).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Operator | Choice | Equal to (=), Not equal to (<>), Greater than (>), Greater than or equal to (>=), Less than (<), Less than or equal to (<=) | Equal to (=) |
| First operand | Required | * | — |
| Second operand | Required | * | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Next loop

Forces the next iteration of the block to take place, skipping any actions in between.

Designer name: **Next loop**. Official reference: [Loops / Next loop](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops#continue).

This action has no input parameters.

Produces no variables.

No module-specific exceptions are listed for this action.

---
