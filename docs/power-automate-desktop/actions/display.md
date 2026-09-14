# Message boxes

Show dialogs, input boxes, and custom forms to the user.

- Actions in this module: **7**
- Official docs: [Message boxes actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/display)

## Actions

### Display message

Displays a message box.

Designer name: **Display message**. Official reference: [Message boxes / Display message](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/display#showmessagedialog).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Message box title | Optional | Text value | — |
| Message to display | Optional | Text value | — |
| Message box icon | Choice | None, Information, Question, Warning, Error | None |
| Message box buttons | Choice | OK, OK - Cancel, Yes - No, Yes - No - Cancel, Abort - Retry - Ignore, Retry - Cancel | OK |
| Default button | Choice | First button, Second button, Third button | First button |
| Keep message box always on top | Choice | Boolean value | False |
| Close message box automatically | Choice | Boolean value | False |
| Timeout | Optional | Numeric value | 3 |

**Outputs**

| Variable | Type |
|---|---|
| ButtonPressed | Text value |

**On error:** `Failed to display message box`, `Can't display message box in noninteractive mode`.

---

### Display input dialog

Displays a dialog box that prompts the user to enter text.

Designer name: **Display input dialog**. Official reference: [Message boxes / Display input dialog](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/display#inputdialog).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Input dialog title | Optional | Text value | — |
| Input dialog message | Optional | Text value | — |
| Default value | Optional | Text value | — |
| Input type | Choice | Single line, Password, Multiline | Single line |
| Keep input dialog always on top | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| UserInput | Text value |
| ButtonPressed | Text value |

**On error:** `Failed to display input dialog`, `Can't display input dialog in non interactive mode`.

---

### Display select date dialog

Displays a dialog box that prompts the user to enter a date or date range.

Designer name: **Display select date dialog**. Official reference: [Message boxes / Display select date dialog](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/display#selectdatedialog).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Dialog title | Optional | Text value | — |
| Dialog message | Optional | Text value | — |
| Dialog type | Choice | Single date, Date range (two Dates) | Single date |
| Prompt for | Choice | Date only, Date and time | Date only |
| Default value | Optional | Datetime | — |
| Default value for second date | Optional | Datetime | — |
| Keep date selection dialog always on top | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| SelectedDate | Datetime |
| SecondSelectedDate | Datetime |
| ButtonPressed | Text value |

**On error:** `Failed to display select date dialog`, `Can't display select date dialog in non interactive mode`.

---

### Display select from list dialog

Displays a dialog box with options that lets the user select from a list.

Designer name: **Display select from list dialog**. Official reference: [Message boxes / Display select from list dialog](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/display#selectfromlistdialog).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Dialog title | Optional | Text value | — |
| Dialog message | Optional | Text value | — |
| List to choose from | Required | General value | — |
| Keep select dialog always on top | Choice | Boolean value | False |
| Limit to list | Choice | Boolean value | True |
| Allow empty selection | Choice | Boolean value | False |
| Allow multiple selections | Choice | Boolean value | False |
| Preselect items starting with a + sign | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| SelectedItem | Text value |
| SelectedItems | List of Text values |
| SelectedIndex | Numeric value |
| SelectedIndexes | List of Numeric values |
| ButtonPressed | Text value |

**On error:** `Failed to display select dialog`, `Can't display select dialog in noninteractive mode`.

---

### Display select  file dialog

Displays the select file dialog and prompts the user to select one or more files.

Designer name: **Display select  file dialog**. Official reference: [Message boxes / Display select  file dialog](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/display#selectfiledialog).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Dialog title | Optional | Text value | — |
| Initial folder | Optional | Folder | — |
| File filter | Optional | Text value | — |
| Keep file selection dialog always on top | Choice | Boolean value | False |
| Allow multiple selections | Choice | Boolean value | False |
| Check if file exists | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| SelectedFile | File |
| SelectedFiles | List of Files |
| ButtonPressed | Text value |

**On error:** `Failed to display select file dialog`, `Can't display select file dialog in noninteractive mode`.

---

### Display select folder dialog

Displays the select folder dialog and prompts the user to select a folder.

Designer name: **Display select folder dialog**. Official reference: [Message boxes / Display select folder dialog](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/display#selectfolder).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Dialog description | Optional | Text value | — |
| Initial folder | Optional | Folder | — |
| Keep folder selection dialog always on top | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| SelectedFolder | Folder |
| ButtonPressed | Text value |

**On error:** `Failed to display select folder dialog`, `Can't display select folder dialog in noninteractive mode`.

---

### Display custom form

Display a customized form that can include multiple types of elements, like text, number or file inputs etc.

Designer name: **Display custom form**. Official reference: [Message boxes / Display custom form](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/display#showcustomdialog).

This action has no input parameters.

**Outputs**

| Variable | Type |
|---|---|
| CustomFormData | Custom object |
| ButtonPressed | Text value |

**On error:** `Failed to display custom form`.

---
