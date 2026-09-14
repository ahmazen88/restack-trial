# Access

Open, query, and close local Microsoft Access databases.

- Actions in this module: **5**
- Official docs: [Access actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/access)

## Actions

### Launch Access

Starts an Access database.

Designer name: **Launch Access**. Official reference: [Access / Launch Access](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/access#launchaccess).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Database path | Choice | Path of database | — |
| User interaction mode | Choice | Boolean value | False |
| Make instance visible | Choice | Boolean value | True |
| Database password | Optional | Direct encrypted input or Text value | — |
| Exclusive | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| AccessInstance | Access instance |

**On error:** `The Access database was not found`, `Failed to open existing Access database`, `Failed to launch Access`, `Access application is not installed`.

---

### Read Access table

Reads an Access table.

Designer name: **Read Access table**. Official reference: [Access / Read Access table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/access#readaccesstable).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Access instance | Choice | Access instance | — |
| Table name | Choice | Text | — |

**Outputs**

| Variable | Type |
|---|---|
| Result | Text |

**On error:** `Failed to read an Access table`.

---

### Run Access query

Runs a stored Access query.

Designer name: **Run Access query**. Official reference: [Access / Run Access query](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/access#runaccessquery).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Access instance | Choice | Access instance | — |
| Query name | Choice | Text | — |
| Query type | Choice | Select query, Action query | Select query |
| Contains parameter | Optional | Boolean | False |

**Outputs**

| Variable | Type |
|---|---|
| QueryResult | Text |
| AffectedRows | Text |

**On error:** `Failed to run an Access query`.

---

### Run Access macro

Runs a stored Access macro.

Designer name: **Run Access macro**. Official reference: [Access / Run Access macro](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/access#runaccessmacro).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Access instance | Choice | Access instance | — |
| Macro name | Choice | Text | — |
| Is VBA Macro | Required | Boolean | False |
| Contains parameter | Optional | Boolean | False |

Produces no variables.

**On error:** `Failed to run an Access macro`.

---

### Close Access

Closes an Access instance.

Designer name: **Close Access**. Official reference: [Access / Close Access](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/access#closeaccess).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Access instance | Choice | Access instance | — |
| Before closing Access | Choice | Do not save changes, Save changes | Do not save changes |

Produces no variables.

**On error:** `Failed to close Access`.

---
