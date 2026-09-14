# Database

Open SQL connections and run statements against databases.

This page documents every **native action** in this group (3 items).

## Actions

### Close SQL connection

- **Inventory id:** `database/close-sql-connection`
- **Kind:** native-action
- **Purpose:** Closes SQL connection.
- **Key inputs:** `SQL connection` (SQL connection)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Close SQL connection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/database#close)

### Execute SQL statement

- **Inventory id:** `database/execute-sql-statement`
- **Kind:** native-action
- **Purpose:** Connect to a database and execute a SQL statement.
- **Key inputs:** `Get connection by` (Connection string, [SQL connection variable]); `SQL connection` (SQL connection); `Connection string` (Text value); `SQL statement` (Text value); `Timeout` (Numeric value; optional)
- **Produces:** `QueryResult` (Datatable)
- **Exceptions:** `Can't connect to data source`; `Invalid connection string`; `Error in SQL statement`
- **Microsoft Learn:** [Execute SQL statement](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/database#executesqlstatement)

### Open SQL connection

- **Inventory id:** `database/open-sql-connection`
- **Kind:** native-action
- **Purpose:** Opens SQL connection.
- **Key inputs:** `Connection string` (Text value)
- **Produces:** `SQLConnection` (SQL connection)
- **Exceptions:** `Can't connect to data source`; `Invalid connection string`
- **Microsoft Learn:** [Open SQL connection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/database#connect)
