# Access

Open local Microsoft Access databases, read tables, and run queries or macros.

This page documents every **native action** in this group (5 items).

## Actions

### Close Access

- **Inventory id:** `access/close-access`
- **Kind:** native-action
- **Purpose:** Closes access.
- **Key inputs:** `Access instance` (Access instance); `Before closing Access` (Do not save changes, Save changes)
- **Produces:** None listed
- **Exceptions:** `Failed to close Access`
- **Microsoft Learn:** [Close Access](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/access#closeaccess)

### Launch Access

- **Inventory id:** `access/launch-access`
- **Kind:** native-action
- **Purpose:** Starts Access and returns an instance later actions can reuse.
- **Key inputs:** `Database path` (Path of database); `User interaction mode` (Boolean value); `Make instance visible` (Boolean value); `Database password` (Direct encrypted input or Text value; optional); `Exclusive` (Boolean value)
- **Produces:** ``AccessInstance`` (Access instance)
- **Exceptions:** `The Access database was not found`; `Failed to open existing Access database`; `Failed to launch Access`; `Access application is not installed`
- **Microsoft Learn:** [Launch Access](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/access#launchaccess)

### Read Access table

- **Inventory id:** `access/read-access-table`
- **Kind:** native-action
- **Purpose:** Reads access table.
- **Key inputs:** `Access instance` (Access instance); `Table name` (Text)
- **Produces:** `Result` (Text)
- **Exceptions:** `Failed to read an Access table`
- **Microsoft Learn:** [Read Access table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/access#readaccesstable)

### Run Access macro

- **Inventory id:** `access/run-access-macro`
- **Kind:** native-action
- **Purpose:** Runs access macro.
- **Key inputs:** `Access instance` (Access instance); `Macro name` (Text); `Is VBA Macro` (Boolean); `Contains parameter` (Boolean; optional)
- **Produces:** None listed
- **Exceptions:** `Failed to run an Access macro`
- **Microsoft Learn:** [Run Access macro](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/access#runaccessmacro)

### Run Access query

- **Inventory id:** `access/run-access-query`
- **Kind:** native-action
- **Purpose:** Runs access query.
- **Key inputs:** `Access instance` (Access instance); `Query name` (Text); `Query type` (Select query, Action query); `Contains parameter` (Boolean; optional)
- **Produces:** `QueryResult` (Text); `AffectedRows` (Text)
- **Exceptions:** `Failed to run an Access query`
- **Microsoft Learn:** [Run Access query](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/access#runaccessquery)
