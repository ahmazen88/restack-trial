# Flow control

Control execution order, errors, subflows, waits, and regions.

- Actions in this module: **14**
- Official docs: [Flow control actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol)

## Actions

### If safe stop requested

Checks whether safe stop is requested for the specific flow.

Designer name: **If safe stop requested**. Official reference: [Flow control / If safe stop requested](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#ifsafestopaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Stop the flow | Choice | Boolean value | False |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Comment

User comment.

Designer name: **Comment**. Official reference: [Flow control / Comment](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#comment).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Comment | Optional | Text value | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### End

Signifies the end of a block.

Designer name: **End**. Official reference: [Flow control / End](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#end).

This action has no input parameters.

Produces no variables.

No module-specific exceptions are listed for this action.

---

### End region

Marks the end of a group of actions.

Designer name: **End region**. Official reference: [Flow control / End region](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#endregion).

This action has no input parameters.

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Exit subflow

Exits current subflow and returns to the point it was called from.

Designer name: **Exit subflow**. Official reference: [Flow control / Exit subflow](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#exitfunction).

This action has no input parameters.

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Get last error

Returns the last error that occurred in the flow.

Designer name: **Get last error**. Official reference: [Flow control / Get last error](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#getlasterror).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Clear error | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| LastError | Error |

No module-specific exceptions are listed for this action.

---

### Go to

Transfers the flow of execution to another point, indicated by a label.

Designer name: **Go to**. Official reference: [Flow control / Go to](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#goto).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Go to label | Required | Text value | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Label

Acts as the destination of a 'go to' statement.

Designer name: **Label**. Official reference: [Flow control / Label](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#label).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Label name | Required | Text value | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Throw custom error

Raises a user-defined error by using a specified error name and message.

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Error name | Required | Text value | None |
| Error message | Required | Text value | None |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### On block error

Marks the beginning of a block to handle actions errors.

Designer name: **On block error**. Official reference: [Flow control / On block error](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#block).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Name | Required | Text value | — |
| Retry policy | Choice | None, Fixed, Exponential | None |
| Handle flow terminating errors | Choice | Boolean value | False |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Region

Marks the beginning of a group of actions.

Designer name: **Region**. Official reference: [Flow control / Region](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#region).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Name | Optional | Text value | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Run subflow

Runs a subflow and specifies any required arguments.

Designer name: **Run subflow**. Official reference: [Flow control / Run subflow](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#callfunction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Subflow name | Required | Subflow | — |
| Input as expression | Choice | Boolean value | False |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Stop flow

Stops the flow.

Designer name: **Stop flow**. Official reference: [Flow control / Stop flow](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#exit).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| End flow | Required | Successfully, With error message | Successfully |
| Error message | Required | Text value | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Wait

Suspends the execution of the flow for a specified number of seconds.

Designer name: **Wait**. Official reference: [Flow control / Wait](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#wait).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Duration | Required | Numeric value | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---
