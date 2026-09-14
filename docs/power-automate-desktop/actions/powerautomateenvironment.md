# Power Automate environment

Read Dataverse / Power Platform environment variables.

- Actions in this module: **1**
- Official docs: [Power Automate environment actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/powerautomateenvironment)

## Actions

### Retrieve environment variable

Returns a Power Automate environment variable.

Designer name: **Retrieve environment variable**. Official reference: [Power Automate environment / Retrieve environment variable](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/powerautomateenvironment#retrieveenvironmentvariable).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Environment variable | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| EnvironmentVariableValue | *Depends on the selected environment variable type* |

**On error:** `Retrieve environment variable failed`.

---
