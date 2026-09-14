# SAP automation

Launch SAP GUI, start transactions, and interact with SAP UI elements.

This page documents every **native action** in this group (11 items).

## Actions

### Attach

- **Inventory id:** `sap/attach`
- **Kind:** native-action
- **Purpose:** Attach the running SAP GUI application to an SAP instance.
- **Key inputs:** `Attach mode` (Foreground or last activated, Window title); `Window title` (Text; optional)
- **Produces:** ``SAPInstance`` (SAP instance)
- **Exceptions:** `Attach to SAP error`
- **Microsoft Learn:** [Attach](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#attachtorunning)

### Click SAP UI element

- **Inventory id:** `sap/click-sap-ui-element`
- **Kind:** native-action
- **Purpose:** Clicks SAP UI element.
- **Key inputs:** ``SAPInstance`` (SAP instance); `Element type` (Basic SAP element, Checkbox, Label, Drop-down list, Grid element); `SAP element ID` (Numeric); `SAP element ID` (Numeric); `Set SAP checkbox state to` (Checked, Unchecked; optional); `SAP label operation` (Expand, Collapse, Choose; optional); `Drop-down option value` (Text value; optional); `SAP grid element` (Cell, Row, Header, List, Button, Toolbar Button, Checkbox, Radio Button; optional)
- **Produces:** None listed
- **Exceptions:** `Click Sap GUI Element error`
- **Microsoft Learn:** [Click SAP UI element](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#clicksapguielement)

### Close SAP connection

- **Inventory id:** `sap/close-sap-connection`
- **Kind:** native-action
- **Purpose:** Closes SAP connection.
- **Key inputs:** ``SAPInstance`` (SAP instance)
- **Produces:** None listed
- **Exceptions:** `Close SAP session action fails`
- **Microsoft Learn:** [Close SAP connection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#closesapconnection)

### Create new SAP session

- **Inventory id:** `sap/create-new-sap-session`
- **Kind:** native-action
- **Purpose:** Creates new SAP session.
- **Key inputs:** ``SAPInstance`` (SAP instance)
- **Produces:** ``SAPInstance`` (SAP instance)
- **Exceptions:** `Create new SAP session action fails`
- **Microsoft Learn:** [Create new SAP session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#createnewsession)

### End SAP transaction

- **Inventory id:** `sap/end-sap-transaction`
- **Kind:** native-action
- **Purpose:** Ends SAP transaction.
- **Key inputs:** ``SAPInstance`` (SAP instance)
- **Produces:** None listed
- **Exceptions:** `End SAP transaction action fails`
- **Microsoft Learn:** [End SAP transaction](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#endtransaction)

### Get details of SAP UI element

- **Inventory id:** `sap/get-details-of-sap-ui-element`
- **Kind:** native-action
- **Purpose:** Reads details of SAP UI element into a flow variable.
- **Key inputs:** ``SAPInstance`` (SAP instance); `SAP element ID` (Numeric); `Attribute name` (Text value)
- **Produces:** `AttributeValue` (Text value)
- **Exceptions:** `Get SAP element detail error`
- **Microsoft Learn:** [Get details of SAP UI element](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#getsapelementdetail)

### Launch SAP

- **Inventory id:** `sap/launch-sap`
- **Kind:** native-action
- **Purpose:** Starts SAP and returns an instance later actions can reuse.
- **Key inputs:** `Connection mode` (Server description and server connection string); `Login mode` (Manual login and single sign-on (SSO)); `Server description` (Text value; optional); `Connection string` (Text value; optional); `Client` (Text value); `Username` (Text value); `Password` (Text value; optional); `Language` (Text value); `Multiple logon options` (Terminate this logon, continue this logon and end any other logons, Continue this logon without ending any other logons in the system)
- **Produces:** ``SAPInstance`` (SAP instance); ``CurrentSAPLoginTerminated`` (Boolean value); ``OtherSAPLoginTerminated`` (Boolean value)
- **Exceptions:** `SAP GUI login action fails`
- **Microsoft Learn:** [Launch SAP](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#saplogin)

### Populate SAP text field in element

- **Inventory id:** `sap/populate-sap-text-field-in-element`
- **Kind:** native-action
- **Purpose:** Types or fills SAP text field in element.
- **Key inputs:** ``SAPInstance`` (SAP instance); `SAP element ID` (Numeric); `Text to fill in` (Direct encrypted input or Text value); `If field isn't empty` (Replace text, Append text; optional)
- **Produces:** None listed
- **Exceptions:** `Populate Sap Text Field Value error`
- **Microsoft Learn:** [Populate SAP text field in element](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#populatetextfield)

### Select SAP menu item

- **Inventory id:** `sap/select-sap-menu-item`
- **Kind:** native-action
- **Purpose:** Selects SAP menu item.
- **Key inputs:** ``SAPInstance`` (SAP instance); `Menu item name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Select SAP menu item action fails`
- **Microsoft Learn:** [Select SAP menu item](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#sapselectmenuitem)

### Select SAP navigation item

- **Inventory id:** `sap/select-sap-navigation-item`
- **Kind:** native-action
- **Purpose:** Selects SAP navigation item.
- **Key inputs:** ``SAPInstance`` (SAP instance); `Navigation item name` (Text value)
- **Produces:** None listed
- **Exceptions:** `SAP GUI select navigation toolbar item error`
- **Microsoft Learn:** [Select SAP navigation item](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#selectnavigationbaritem)

### Start SAP transaction

- **Inventory id:** `sap/start-sap-transaction`
- **Kind:** native-action
- **Purpose:** Starts SAP transaction.
- **Key inputs:** ``SAPInstance`` (SAP instance); `Transaction code` (Text value)
- **Produces:** None listed
- **Exceptions:** `Start SAP transaction action fails`
- **Microsoft Learn:** [Start SAP transaction](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sap#starttransaction)
