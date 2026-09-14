# Conditionals

Branch the flow with If, Else if, Else, Switch, and Case.

- Actions in this module: **6**
- Official docs: [Conditionals actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/conditionals)

## Actions

### Case

An expression that, if met, a block of actions associated with that particular case runs.

Designer name: **Case**. Official reference: [Conditionals / Case](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/conditionals#case).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Operator | Choice | Equal to (=), Not equal to (<>), Greater than (>), Greater than or equal to (>=), Less than (<), Less than or equal to (<=), Contains, Does not contain, Is empty, Is not empty, Starts with, Does not start with, Ends with, Does not end with, Is blank, Is not blank | Equal to (=) |
| Value to compare | Required | * | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Default case

A block of actions that is run, if no case expression has been met in the switch body.

Designer name: **Default case**. Official reference: [Conditionals / Default case](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/conditionals#casedefault).

This action has no input parameters.

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Else

Marks the beginning of a block of actions that ran if the condition specified in the preceding 'If' statements aren't met.

Designer name: **Else**. Official reference: [Conditionals / Else](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/conditionals#else).

This action has no input parameters.

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Else if

Marks the beginning of a block of actions that run if the conditions specified in the preceding 'If' statements aren't met, but the condition specified in this statement is met.

Designer name: **Else if**. Official reference: [Conditionals / Else if](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/conditionals#elseif).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Operator | Choice | Equal to (=), Not equal to (<>), Greater than (>), Greater than or equal to (>=), Less than (<), Less than or equal to (<=), Contains, Does not contain, Is empty, Is not empty, Starts with, Does not start with, Ends with, Does not end with, Is blank, Is not blank | Equal to (=) |
| First operand | Required | * | — |
| Second operand | Required | * | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### If

Marks the beginning of a block of actions that is run if the condition specified in this statement is met.

Designer name: **If**. Official reference: [Conditionals / If](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/conditionals#if).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Operator | Choice | Equal to (=), Not equal to (<>), Greater than (>), Greater than or equal to (>=), Less than (<), Less than or equal to (<=), Contains, Does not contain, Is empty, Is not empty, Starts with, Does not start with, Ends with, Does not end with, Is blank, Is not blank | Equal to (=) |
| First operand | Required | * | — |
| Second operand | Required | * | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Switch

Dispatches execution to different parts of the switch body based on the value of the expression.

Designer name: **Switch**. Official reference: [Conditionals / Switch](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/conditionals#switch).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Value to check | Required | * | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---
