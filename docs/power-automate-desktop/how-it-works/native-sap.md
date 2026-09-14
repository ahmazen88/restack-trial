# SAP automation — how each function works

Native Actions pane module **SAP automation**.

11 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Attach

- **Id:** `sap/attach`
- **Kind:** native-action
- **Purpose:** Attach the running SAP GUI application to an SAP instance.

**Use case.** In posting a document in SAP GUI, drop **Attach** on the canvas. Attach the running SAP GUI application to an SAP instance.

**Demonstration.**

```text
**Attach**
- Attach mode: `Window title`
- Window title: `INV-1042`
Produces:
- `%`SAPInstance`%` (SAP instance)
```

**Analogy.** One tool in that kit: a green-screen clerk: log in, run a transaction, type, leave.

**In combination.** Launch SAP, Start SAP transaction, populate/click, End SAP transaction, Close SAP connection.

### Click SAP UI element

- **Id:** `sap/click-sap-ui-element`
- **Kind:** native-action
- **Purpose:** Clicks SAP UI element.

**Use case.** In posting a document in SAP GUI, drop **Click SAP UI element** on the canvas. Clicks SAP UI element.

**Demonstration.**

```text
**Click SAP UI element**
- `SAPInstance`: `(set in designer)`
- Element type: `%Files%`
- SAP element ID: `1`
- SAP element ID: `1`
- Set SAP checkbox state to: `Checked`
- SAP label operation: `Expand`
- Drop-down option value: `INV-1042`
- SAP grid element: `%Files%`
```

**Analogy.** Pushing the exact button a trained operator would push.

**In combination.** Launch SAP, Start SAP transaction, populate/click, End SAP transaction, Close SAP connection.

### Close SAP connection

- **Id:** `sap/close-sap-connection`
- **Kind:** native-action
- **Purpose:** Closes SAP connection.

**Use case.** In posting a document in SAP GUI, drop **Close SAP connection** on the canvas. Closes SAP connection.

**Demonstration.**

```text
**Close SAP connection**
- `SAPInstance`: `(set in designer)`
```

**Analogy.** Turning out the lights when the work in that room is done.

**In combination.** Launch SAP, Start SAP transaction, populate/click, End SAP transaction, Close SAP connection. Call this only after the last use of the instance so you do not break later steps.

### Create new SAP session

- **Id:** `sap/create-new-sap-session`
- **Kind:** native-action
- **Purpose:** Creates new SAP session.

**Use case.** In posting a document in SAP GUI, drop **Create new SAP session** on the canvas. Creates new SAP session.

**Demonstration.**

```text
**Create new SAP session**
- `SAPInstance`: `(set in designer)`
Produces:
- `%`SAPInstance`%` (SAP instance)
```

**Analogy.** One tool in that kit: a green-screen clerk: log in, run a transaction, type, leave.

**In combination.** Launch SAP, Start SAP transaction, populate/click, End SAP transaction, Close SAP connection.

### End SAP transaction

- **Id:** `sap/end-sap-transaction`
- **Kind:** native-action
- **Purpose:** Ends SAP transaction.

**Use case.** In posting a document in SAP GUI, drop **End SAP transaction** on the canvas. Ends SAP transaction.

**Demonstration.**

```text
**End SAP transaction**
- `SAPInstance`: `(set in designer)`
```

**Analogy.** Turning out the lights when the work in that room is done.

**In combination.** Launch SAP, Start SAP transaction, populate/click, End SAP transaction, Close SAP connection. Call this only after the last use of the instance so you do not break later steps.

### Get details of SAP UI element

- **Id:** `sap/get-details-of-sap-ui-element`
- **Kind:** native-action
- **Purpose:** Reads details of SAP UI element into a flow variable.

**Use case.** In posting a document in SAP GUI, drop **Get details of SAP UI element** on the canvas. Reads details of SAP UI element into a flow variable.

**Demonstration.**

```text
**Get details of SAP UI element**
- `SAPInstance`: `(set in designer)`
- SAP element ID: `1`
- Attribute name: `Own text`
Produces:
- `%AttributeValue%` (Text value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Launch SAP, Start SAP transaction, populate/click, End SAP transaction, Close SAP connection.

### Launch SAP

- **Id:** `sap/launch-sap`
- **Kind:** native-action
- **Purpose:** Starts SAP and returns an instance later actions can reuse.

**Use case.** In posting a document in SAP GUI, drop **Launch SAP** on the canvas. Starts SAP and returns an instance later actions can reuse.

**Demonstration.**

```text
**Launch SAP**
- Connection mode: `Server description`
- Login mode: `Manual login`
- Server description: `INV-1042`
- Connection string: `INV-1042`
- Client: `INV-1042`
- Username: `CONTOSO\rpa.bot`
- Password: `%Credential.Password%  (sensitive)`
- Language: `INV-1042`
- … 1 more parameter(s) in the action modal
Produces:
- `%`SAPInstance`%` (SAP instance)
- `%`CurrentSAPLoginTerminated`%` (Boolean value)
- `%`OtherSAPLoginTerminated`%` (Boolean value)
```

**Analogy.** Unlocking the room before you work. Same family as: a green-screen clerk: log in, run a transaction, type, leave.

**In combination.** Launch SAP, Start SAP transaction, populate/click, End SAP transaction, Close SAP connection. Keep the produced instance/connection and pass it into every later action in this module.

### Populate SAP text field in element

- **Id:** `sap/populate-sap-text-field-in-element`
- **Kind:** native-action
- **Purpose:** Types or fills SAP text field in element.

**Use case.** In posting a document in SAP GUI, drop **Populate SAP text field in element** on the canvas. Types or fills SAP text field in element.

**Demonstration.**

```text
**Populate SAP text field in element**
- `SAPInstance`: `(set in designer)`
- SAP element ID: `1`
- Text to fill in: `INV-1042`
- If field isn't empty: `Replace text`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Launch SAP, Start SAP transaction, populate/click, End SAP transaction, Close SAP connection.

### Select SAP menu item

- **Id:** `sap/select-sap-menu-item`
- **Kind:** native-action
- **Purpose:** Selects SAP menu item.

**Use case.** In posting a document in SAP GUI, drop **Select SAP menu item** on the canvas. Selects SAP menu item.

**Demonstration.**

```text
**Select SAP menu item**
- `SAPInstance`: `(set in designer)`
- Menu item name: `INV-1042`
```

**Analogy.** One tool in that kit: a green-screen clerk: log in, run a transaction, type, leave.

**In combination.** Launch SAP, Start SAP transaction, populate/click, End SAP transaction, Close SAP connection.

### Select SAP navigation item

- **Id:** `sap/select-sap-navigation-item`
- **Kind:** native-action
- **Purpose:** Selects SAP navigation item.

**Use case.** In posting a document in SAP GUI, drop **Select SAP navigation item** on the canvas. Selects SAP navigation item.

**Demonstration.**

```text
**Select SAP navigation item**
- `SAPInstance`: `(set in designer)`
- Navigation item name: `INV-1042`
```

**Analogy.** One tool in that kit: a green-screen clerk: log in, run a transaction, type, leave.

**In combination.** Launch SAP, Start SAP transaction, populate/click, End SAP transaction, Close SAP connection.

### Start SAP transaction

- **Id:** `sap/start-sap-transaction`
- **Kind:** native-action
- **Purpose:** Starts SAP transaction.

**Use case.** In posting a document in SAP GUI, drop **Start SAP transaction** on the canvas. Starts SAP transaction.

**Demonstration.**

```text
**Start SAP transaction**
- `SAPInstance`: `(set in designer)`
- Transaction code: `FB60`
```

**Analogy.** One tool in that kit: a green-screen clerk: log in, run a transaction, type, leave.

**In combination.** Launch SAP, Start SAP transaction, populate/click, End SAP transaction, Close SAP connection.
