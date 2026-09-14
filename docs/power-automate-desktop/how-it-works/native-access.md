# Access — how each function works

Native Actions pane module **Access**.

5 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Close Access

- **Id:** `access/close-access`
- **Kind:** native-action
- **Purpose:** Closes access.

**Use case.** In claims database on a shared drive, drop **Close Access** on the canvas. Closes access.

**Demonstration.**

```text
**Close Access**
- Access instance: `%AccessInstance%`
- Before closing Access: `Do not save changes`
```

**Analogy.** Turning out the lights when the work in that room is done.

**In combination.** Launch Access first; Close Access when the query work is done so the .accdb file is not left locked. Call this only after the last use of the instance so you do not break later steps.

### Launch Access

- **Id:** `access/launch-access`
- **Kind:** native-action
- **Purpose:** Starts Access and returns an instance later actions can reuse.

**Use case.** In claims database on a shared drive, drop **Launch Access** on the canvas. Starts Access and returns an instance later actions can reuse.

**Demonstration.**

```text
**Launch Access**
- Database path: `C:\RPA\Invoices\INV-1042.pdf`
- User interaction mode: `False`
- Make instance visible: `True`
- Database password: `%Credential.Password%  (sensitive)`
- Exclusive: `False`
Produces:
- `%`AccessInstance`%` (Access instance)
```

**Analogy.** Unlocking the room before you work. Same family as: opening a locked filing cabinet, working the folders, then shutting the drawer.

**In combination.** Launch Access first; Close Access when the query work is done so the .accdb file is not left locked. Keep the produced instance/connection and pass it into every later action in this module.

### Read Access table

- **Id:** `access/read-access-table`
- **Kind:** native-action
- **Purpose:** Reads access table.

**Use case.** In claims database on a shared drive, drop **Read Access table** on the canvas. Reads access table.

**Demonstration.**

```text
**Read Access table**
- Access instance: `%AccessInstance%`
- Table name: `INV-1042`
Produces:
- `%Result%` (Text)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Launch Access first; Close Access when the query work is done so the .accdb file is not left locked.

### Run Access macro

- **Id:** `access/run-access-macro`
- **Kind:** native-action
- **Purpose:** Runs access macro.

**Use case.** In claims database on a shared drive, drop **Run Access macro** on the canvas. Runs access macro.

**Demonstration.**

```text
**Run Access macro**
- Access instance: `%AccessInstance%`
- Macro name: `RefreshAll`
- Is VBA Macro: `False`
- Contains parameter: `False`
```

**Analogy.** One tool in that kit: opening a locked filing cabinet, working the folders, then shutting the drawer.

**In combination.** Launch Access first; Close Access when the query work is done so the .accdb file is not left locked.

### Run Access query

- **Id:** `access/run-access-query`
- **Kind:** native-action
- **Purpose:** Runs access query.

**Use case.** In claims database on a shared drive, drop **Run Access query** on the canvas. Runs access query.

**Demonstration.**

```text
**Run Access query**
- Access instance: `%AccessInstance%`
- Query name: `INV-1042`
- Query type: `Select query`
- Contains parameter: `False`
Produces:
- `%QueryResult%` (Text)
- `%AffectedRows%` (Text)
```

**Analogy.** One tool in that kit: opening a locked filing cabinet, working the folders, then shutting the drawer.

**In combination.** Launch Access first; Close Access when the query work is done so the .accdb file is not left locked.
