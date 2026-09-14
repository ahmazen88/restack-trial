# Database — how each function works

Native Actions pane module **Database**.

3 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Close SQL connection

- **Id:** `database/close-sql-connection`
- **Kind:** native-action
- **Purpose:** Closes SQL connection.

**Use case.** In reading open orders from SQL Server, drop **Close SQL connection** on the canvas. Closes SQL connection.

**Demonstration.**

```text
**Close SQL connection**
- SQL connection: `%SQLConnection%`
```

**Analogy.** Turning out the lights when the work in that room is done.

**In combination.** Open SQL connection, Execute SQL statement, Close SQL connection. Call this only after the last use of the instance so you do not break later steps.

### Execute SQL statement

- **Id:** `database/execute-sql-statement`
- **Kind:** native-action
- **Purpose:** Connect to a database and execute a SQL statement.

**Use case.** In reading open orders from SQL Server, drop **Execute SQL statement** on the canvas. Connect to a database and execute a SQL statement.

**Demonstration.**

```text
**Execute SQL statement**
- Get connection by: `%SQLConnection%`
- SQL connection: `%SQLConnection%`
- Connection string: `INV-1042`
- SQL statement: `SELECT TOP 100 * FROM dbo.OpenOrders`
- Timeout: `30`
Produces:
- `%QueryResult%` (Datatable)
```

**Analogy.** One tool in that kit: calling the warehouse on a dedicated phone line, asking a question, hanging up.

**In combination.** Open SQL connection, Execute SQL statement, Close SQL connection.

### Open SQL connection

- **Id:** `database/open-sql-connection`
- **Kind:** native-action
- **Purpose:** Opens SQL connection.

**Use case.** In reading open orders from SQL Server, drop **Open SQL connection** on the canvas. Opens SQL connection.

**Demonstration.**

```text
**Open SQL connection**
- Connection string: `INV-1042`
Produces:
- `%SQLConnection%` (SQL connection)
```

**Analogy.** Unlocking the room before you work. Same family as: calling the warehouse on a dedicated phone line, asking a question, hanging up.

**In combination.** Open SQL connection, Execute SQL statement, Close SQL connection. Keep the produced instance/connection and pass it into every later action in this module.
