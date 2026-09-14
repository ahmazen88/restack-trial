# SAP automation

Drive SAP GUI: login, transactions, and UI element interaction.

- Actions in this module: **11**
- Official docs: [SAP automation actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap)

## Actions

### Launch SAP

Open the SAP GUI application and connect to an SAP system.

Designer name: **Launch SAP**. Official reference: [SAP automation / Launch SAP](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#saplogin).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Connection mode | Choice | Server description and server connection string | Server description |
| Login mode | Choice | Manual login and single sign-on (SSO) | Manual login |
| Server description | Optional | Text value | — |
| Connection string | Optional | Text value | — |
| Client | Required | Text value | — |
| Username | Required | Text value | — |
| Password | Optional | Text value | — |
| Language | Required | Text value | — |
| Multiple logon options | Required | Terminate this logon, continue this logon and end any other logons, Continue this logon without ending any other logons in the system | Terminate this logon |

**Outputs**

| Variable | Type |
|---|---|
| SAPInstance | SAP instance |
| CurrentSAPLoginTerminated | Boolean value |
| OtherSAPLoginTerminated | Boolean value |

**On error:** `SAP GUI login action fails`.

---

### Attach

Attach the running SAP GUI application to an SAP instance.

Designer name: **Attach**. Official reference: [SAP automation / Attach](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#attachtorunning).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Attach mode | Required | Foreground or last activated, Window title | Window title |
| Window title | Optional | Text | — |

**Outputs**

| Variable | Type |
|---|---|
| SAPInstance | SAP instance |

**On error:** `Attach to SAP error`.

---

### Create new SAP session

Creates a new SAP session based on the same SAP instance.

Designer name: **Create new SAP session**. Official reference: [SAP automation / Create new SAP session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#createnewsession).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| SAPInstance | Required | SAP instance | — |

**Outputs**

| Variable | Type |
|---|---|
| SAPInstance | SAP instance |

**On error:** `Create new SAP session action fails`.

---

### Select SAP navigation item

Select an SAP menu item in the application toolbar of the SAP window.

Designer name: **Select SAP navigation item**. Official reference: [SAP automation / Select SAP navigation item](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#selectnavigationbaritem).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| SAPInstance | Required | SAP instance | — |
| Navigation item name | Required | Text value | — |

Produces no variables.

**On error:** `SAP GUI select navigation toolbar item error`.

---

### Select SAP menu item

Select an SAP menu item in the window tool bar.

Designer name: **Select SAP menu item**. Official reference: [SAP automation / Select SAP menu item](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#sapselectmenuitem).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| SAPInstance | Required | SAP instance | — |
| Menu item name | Required | Text value | — |

Produces no variables.

**On error:** `Select SAP menu item action fails`.

---

### Close SAP connection

Close the SAP connection of the selected SAP instance.

Designer name: **Close SAP connection**. Official reference: [SAP automation / Close SAP connection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#closesapconnection).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| SAPInstance | Required | SAP instance | — |

Produces no variables.

**On error:** `Close SAP session action fails`.

---

### Start SAP transaction

Opens a specific transaction code in existing session.

Designer name: **Start SAP transaction**. Official reference: [SAP automation / Start SAP transaction](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#starttransaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| SAPInstance | Required | SAP instance | — |
| Transaction code | Required | Text value | — |

Produces no variables.

**On error:** `Start SAP transaction action fails`.

---

### End SAP transaction

Closes the SAP transaction in a specific SAP instance and returns to the SAP easy access menu.

Designer name: **End SAP transaction**. Official reference: [SAP automation / End SAP transaction](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#endtransaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| SAPInstance | Required | SAP instance | — |

Produces no variables.

**On error:** `End SAP transaction action fails`.

---

### Click SAP UI element

Interacts through click action on any UI element of an SAP window.

Designer name: **Click SAP UI element**. Official reference: [SAP automation / Click SAP UI element](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#clicksapguielement).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| SAPInstance | Required | SAP instance | — |
| Element type | Required | Basic SAP element, Checkbox, Label, Drop-down list, Grid element | Basic SAP element |
| SAP element ID | Required | Numeric | — |
| SAP element ID | Required | Numeric | — |
| Set SAP checkbox state to | Optional | Checked, Unchecked | Checked |
| SAP label operation | Optional | Expand, Collapse, Choose | Expand |
| Drop-down option value | Optional | Text value | — |
| SAP grid element | Optional | Cell, Row, Header, List, Button, Toolbar Button, Checkbox, Radio Button | Cell |

Produces no variables.

**On error:** `Click Sap GUI Element error`.

---

### Get details of SAP UI element

Reads the value of an SAP UI element's attribute in an SAP window.

Designer name: **Get details of SAP UI element**. Official reference: [SAP automation / Get details of SAP UI element](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#getsapelementdetail).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| SAPInstance | Required | SAP instance | — |
| SAP element ID | Required | Numeric | — |
| Attribute name | Required | Text value | Own text |

**Outputs**

| Variable | Type |
|---|---|
| AttributeValue | Text value |

**On error:** `Get SAP element detail error`.

---

### Populate SAP text field in element

Fills a text box in an SAP window with the specified text.

Designer name: **Populate SAP text field in element**. Official reference: [SAP automation / Populate SAP text field in element](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#populatetextfield).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| SAPInstance | Required | SAP instance | — |
| SAP element ID | Required | Numeric | — |
| Text to fill in | Required | Direct encrypted input or Text value | — |
| If field isn't empty | Optional | Replace text, Append text | Replace text |

Produces no variables.

**On error:** `Populate Sap Text Field Value error`.

---
