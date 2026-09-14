# Database

Open SQL connections and run statements against databases.

- Actions in this module: **2**
- Official docs: [Database actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/database)

## Actions

### Open SQL connection

Open a new connection to a database.

Designer name: **Open SQL connection**. Official reference: [Database / Open SQL connection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/database#connect).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Connection string | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| SQLConnection | SQL connection |

**On error:** `Can't connect to data source`, `Invalid connection string`.

---

### Close SQL connection

Close an open connection to a database.

Designer name: **Close SQL connection**. Official reference: [Database / Close SQL connection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/database#close).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| SQL connection | Required | SQL connection | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---
