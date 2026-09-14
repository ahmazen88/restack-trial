# Message boxes — how each function works

Native Actions pane module **Message boxes**.

7 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Display custom form

- **Id:** `display/display-custom-form`
- **Kind:** native-action
- **Purpose:** Shows custom form to the user.

**Use case.** In an attended bot that must ask a person which file to use, drop **Display custom form** on the canvas. Shows custom form to the user.

**Demonstration.**

```text
**Display custom form**
- (no inputs)
Produces:
- `%CustomFormData%` (Custom object)
- `%ButtonPressed%` (Text value)
```

**Analogy.** One tool in that kit: tapping a coworker on the shoulder and waiting for an answer.

**In combination.** Use Display select file/folder or Display message, then branch on the result.

### Display input dialog

- **Id:** `display/display-input-dialog`
- **Kind:** native-action
- **Purpose:** Shows input dialog to the user.

**Use case.** In an attended bot that must ask a person which file to use, drop **Display input dialog** on the canvas. Shows input dialog to the user.

**Demonstration.**

```text
**Display input dialog**
- Input dialog title: `INV-1042`
- Input dialog message: `Processed by desktop flow Close-P9`
- Default value: `INV-1042`
- Input type: `Single line`
- Keep input dialog always on top: `False`
Produces:
- `%UserInput%` (Text value)
- `%ButtonPressed%` (Text value)
```

**Analogy.** One tool in that kit: tapping a coworker on the shoulder and waiting for an answer.

**In combination.** Use Display select file/folder or Display message, then branch on the result.

### Display message

- **Id:** `display/display-message`
- **Kind:** native-action
- **Purpose:** Shows message to the user.

**Use case.** Stop an attended run and tell the person what happened or what to do next.

**Demonstration.**

```text
**Display message**
- Message box title: `Processed by desktop flow Close-P9`
- Message to display: `Processed by desktop flow Close-P9`
- Message box icon: `Processed by desktop flow Close-P9`
- Message box buttons: `Processed by desktop flow Close-P9`
- Default button: `First button`
- Keep message box always on top: `False`
- Close message box automatically: `False`
- Timeout: `30`
Produces:
- `%ButtonPressed%` (Text value)
```

**Analogy.** One tool in that kit: tapping a coworker on the shoulder and waiting for an answer.

**In combination.** Use Display select file/folder or Display message, then branch on the result.

### Display select  file dialog

- **Id:** `display/display-select-file-dialog`
- **Kind:** native-action
- **Purpose:** Shows select  file dialog to the user.

**Use case.** In an attended bot that must ask a person which file to use, drop **Display select  file dialog** on the canvas. Shows select  file dialog to the user.

**Demonstration.**

```text
**Display select  file dialog**
- Dialog title: `INV-1042`
- Initial folder: `C:\RPA\Invoices`
- File filter: `*.pdf`
- Keep file selection dialog always on top: `False`
- Allow multiple selections: `False`
- Check if file exists: `False`
Produces:
- `%SelectedFile%` (File)
- `%SelectedFiles%` (List of Files)
- `%ButtonPressed%` (Text value)
```

**Analogy.** One tool in that kit: tapping a coworker on the shoulder and waiting for an answer.

**In combination.** Use Display select file/folder or Display message, then branch on the result.

### Display select date dialog

- **Id:** `display/display-select-date-dialog`
- **Kind:** native-action
- **Purpose:** Shows select date dialog to the user.

**Use case.** In an attended bot that must ask a person which file to use, drop **Display select date dialog** on the canvas. Shows select date dialog to the user.

**Demonstration.**

```text
**Display select date dialog**
- Dialog title: `INV-1042`
- Dialog message: `Processed by desktop flow Close-P9`
- Dialog type: `Single date`
- Prompt for: `Date only`
- Default value: `(set in designer)`
- Default value for second date: `(set in designer)`
- Keep date selection dialog always on top: `False`
Produces:
- `%SelectedDate%` (Datetime)
- `%SecondSelectedDate%` (Datetime)
- `%ButtonPressed%` (Text value)
```

**Analogy.** One tool in that kit: tapping a coworker on the shoulder and waiting for an answer.

**In combination.** Use Display select file/folder or Display message, then branch on the result.

### Display select folder dialog

- **Id:** `display/display-select-folder-dialog`
- **Kind:** native-action
- **Purpose:** Shows select folder dialog to the user.

**Use case.** In an attended bot that must ask a person which file to use, drop **Display select folder dialog** on the canvas. Shows select folder dialog to the user.

**Demonstration.**

```text
**Display select folder dialog**
- Dialog description: `INV-1042`
- Initial folder: `C:\RPA\Invoices`
- Keep folder selection dialog always on top: `False`
Produces:
- `%SelectedFolder%` (Folder)
- `%ButtonPressed%` (Text value)
```

**Analogy.** One tool in that kit: tapping a coworker on the shoulder and waiting for an answer.

**In combination.** Use Display select file/folder or Display message, then branch on the result.

### Display select from list dialog

- **Id:** `display/display-select-from-list-dialog`
- **Kind:** native-action
- **Purpose:** Shows select from list dialog to the user.

**Use case.** In an attended bot that must ask a person which file to use, drop **Display select from list dialog** on the canvas. Shows select from list dialog to the user.

**Demonstration.**

```text
**Display select from list dialog**
- Dialog title: `INV-1042`
- Dialog message: `Processed by desktop flow Close-P9`
- List to choose from: `(set in designer)`
- Keep select dialog always on top: `False`
- Limit to list: `True`
- Allow empty selection: `False`
- Allow multiple selections: `False`
- Preselect items starting with a + sign: `False`
Produces:
- `%SelectedItem%` (Text value)
- `%SelectedItems%` (List of Text values)
- `%SelectedIndex%` (Numeric value)
- `%SelectedIndexes%` (List of Numeric values)
- `%ButtonPressed%` (Text value)
```

**Analogy.** One tool in that kit: tapping a coworker on the shoulder and waiting for an answer.

**In combination.** Use Display select file/folder or Display message, then branch on the result.
