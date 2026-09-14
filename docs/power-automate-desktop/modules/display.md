# Message boxes

Prompt the user with messages, inputs, file pickers, and custom forms.

This page documents every **native action** in this group (7 items).

## Actions

### Display custom form

- **Inventory id:** `display/display-custom-form`
- **Kind:** native-action
- **Purpose:** Shows custom form to the user.
- **Key inputs:** None
- **Produces:** `CustomFormData` (Custom object); `ButtonPressed` (Text value)
- **Exceptions:** `Failed to display custom form`
- **Microsoft Learn:** [Display custom form](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/display#showcustomdialog)

### Display input dialog

- **Inventory id:** `display/display-input-dialog`
- **Kind:** native-action
- **Purpose:** Shows input dialog to the user.
- **Key inputs:** `Input dialog title` (Text value; optional); `Input dialog message` (Text value; optional); `Default value` (Text value; optional); `Input type` (Single line, Password, Multiline); `Keep input dialog always on top` (Boolean value)
- **Produces:** `UserInput` (Text value); `ButtonPressed` (Text value)
- **Exceptions:** `Failed to display input dialog`; `Can't display input dialog in non interactive mode`
- **Microsoft Learn:** [Display input dialog](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/display#inputdialog)

### Display message

- **Inventory id:** `display/display-message`
- **Kind:** native-action
- **Purpose:** Shows message to the user.
- **Key inputs:** `Message box title` (Text value; optional); `Message to display` (Text value; optional); `Message box icon` (None, Information, Question, Warning, Error); `Message box buttons` (OK, OK - Cancel, Yes - No, Yes - No - Cancel, Abort - Retry - Ignore, Retry - Cancel); `Default button` (First button, Second button, Third button); `Keep message box always on top` (Boolean value); `Close message box automatically` (Boolean value); `Timeout` (Numeric value; optional)
- **Produces:** `ButtonPressed` (Text value)
- **Exceptions:** `Failed to display message box`; `Can't display message box in noninteractive mode`
- **Microsoft Learn:** [Display message](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/display#showmessagedialog)

### Display select  file dialog

- **Inventory id:** `display/display-select-file-dialog`
- **Kind:** native-action
- **Purpose:** Shows select  file dialog to the user.
- **Key inputs:** `Dialog title` (Text value; optional); `Initial folder` (Folder; optional); `File filter` (Text value; optional); `Keep file selection dialog always on top` (Boolean value); `Allow multiple selections` (Boolean value); `Check if file exists` (Boolean value)
- **Produces:** `SelectedFile` (File); `SelectedFiles` (List of Files); `ButtonPressed` (Text value)
- **Exceptions:** `Failed to display select file dialog`; `Can't display select file dialog in noninteractive mode`
- **Microsoft Learn:** [Display select  file dialog](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/display#selectfiledialog)

### Display select date dialog

- **Inventory id:** `display/display-select-date-dialog`
- **Kind:** native-action
- **Purpose:** Shows select date dialog to the user.
- **Key inputs:** `Dialog title` (Text value; optional); `Dialog message` (Text value; optional); `Dialog type` (Single date, Date range (two Dates)); `Prompt for` (Date only, Date and time); `Default value` (Datetime; optional); `Default value for second date` (Datetime; optional); `Keep date selection dialog always on top` (Boolean value)
- **Produces:** `SelectedDate` (Datetime); `SecondSelectedDate` (Datetime); `ButtonPressed` (Text value)
- **Exceptions:** `Failed to display select date dialog`; `Can't display select date dialog in non interactive mode`
- **Microsoft Learn:** [Display select date dialog](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/display#selectdatedialog)

### Display select folder dialog

- **Inventory id:** `display/display-select-folder-dialog`
- **Kind:** native-action
- **Purpose:** Shows select folder dialog to the user.
- **Key inputs:** `Dialog description` (Text value; optional); `Initial folder` (Folder; optional); `Keep folder selection dialog always on top` (Boolean value)
- **Produces:** `SelectedFolder` (Folder); `ButtonPressed` (Text value)
- **Exceptions:** `Failed to display select folder dialog`; `Can't display select folder dialog in noninteractive mode`
- **Microsoft Learn:** [Display select folder dialog](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/display#selectfolder)

### Display select from list dialog

- **Inventory id:** `display/display-select-from-list-dialog`
- **Kind:** native-action
- **Purpose:** Shows select from list dialog to the user.
- **Key inputs:** `Dialog title` (Text value; optional); `Dialog message` (Text value; optional); `List to choose from` (General value); `Keep select dialog always on top` (Boolean value); `Limit to list` (Boolean value); `Allow empty selection` (Boolean value); `Allow multiple selections` (Boolean value); `Preselect items starting with a + sign` (Boolean value)
- **Produces:** `SelectedItem` (Text value); `SelectedItems` (List of Text values); `SelectedIndex` (Numeric value); `SelectedIndexes` (List of Numeric values); `ButtonPressed` (Text value)
- **Exceptions:** `Failed to display select dialog`; `Can't display select dialog in noninteractive mode`
- **Microsoft Learn:** [Display select from list dialog](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/display#selectfromlistdialog)
