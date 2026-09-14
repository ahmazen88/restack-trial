# UI automation

Click, type, extract, and wait on Windows UI elements and images.

- Actions in this module: **33**
- Official docs: [UI automation actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation)

## Actions

### Get details of window

Reads a property of a window such as its title or its source text.

Designer name: **Get details of window**. Official reference: [UI automation / Get details of window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#getwindowdetails).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Window | Required | UI element | — |
| Window property | Choice | Get window title, Get window text, Get window location and size, Get process name | Get window title |
| Bring to front | Choice | Boolean value | True |

**Outputs**

| Variable | Type |
|---|---|
| WindowProperty | General value |

**On error:** `Failed to retrieve property of window`.

---

### Get details of a UI element in window

Reads the value of a UI element's attribute in a window.

Designer name: **Get details of a UI element in window**. Official reference: [UI automation / Get details of a UI element in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#getelementdetails).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| UI element | Required | UI element | — |
| Attribute name | Optional | Text value | Own Text |
| Bring to front | Choice | Boolean value | True |

**Outputs**

| Variable | Type |
|---|---|
| AttributeValue | Text value |

**On error:** `Failed to retrieve attribute of UI element`.

---

### Get selected checkboxes in window

Returns the names of the selected checkboxes in a checkbox group or the state of a specific checkbox.

Designer name: **Get selected checkboxes in window**. Official reference: [UI automation / Get selected checkboxes in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#getselectedcheckboxesinwindow).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| UI element | Required | UI element | — |
| Operation | Choice | Get names of selected checkboxes in group, Get state of checkbox | Get names of selected checkboxes in group |
| Bring to front | Choice | Boolean value | True |

**Outputs**

| Variable | Type |
|---|---|
| IsChecked | Boolean value |
| SelectedCheckboxes | List of Text values |

**On error:** `Failed to retrieve checkbox state(s)`.

---

### Get selected radio button in window

Returns the names of the selected radio button in a radio button group or the state of a specific radio button.

Designer name: **Get selected radio button in window**. Official reference: [UI automation / Get selected radio button in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#getselectedradiobuttoninwindow).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| UI element | Required | UI element | — |
| Operation | Choice | Get selected radio button name in group, Get state of radio button | Get selected radio button name in group |
| Bring to front | Choice | Boolean value | True |

**Outputs**

| Variable | Type |
|---|---|
| IsSelected | Boolean value |
| SelectedRadiobutton | Text value |

**On error:** `Failed to retrieve radio button state`.

---

### Extract data from window

Extracts data from specific parts of a window in the form of single values, lists, or tables.

Designer name: **Extract data from window**. Official reference: [UI automation / Extract data from window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#extractdatafromwindow).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Window | Required | UI element | — |
| Store extracted data in | Choice | an Excel spreadsheet, A variable | an Excel spreadsheet |
| Bring to front | Choice | Boolean value | True |

**Outputs**

| Variable | Type |
|---|---|
| ExcelInstance | Excel instance |
| DataFromWindow | General value |

**On error:** `Extraction failed`.

---

### Extract data from table

Extracts data from a table in the form of a datatable.

Designer name: **Extract data from table**. Official reference: [UI automation / Extract data from table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#extractdatafromtable).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Table | Required | UI element | — |
| Store extracted data in | Choice | an Excel spreadsheet, A variable | an Excel spreadsheet |
| Bring to front | Choice | Boolean value | True |

**Outputs**

| Variable | Type |
|---|---|
| ExcelInstance | Excel instance |
| DataFromTable | General value |

**On error:** `Extraction failed`.

---

### Take screenshot of UI element

Takes a screenshot of a UI element in window.

Designer name: **Take screenshot of UI element**. Official reference: [UI automation / Take screenshot of UI element](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#takescreenshot).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| UI element | Required | UI element | — |
| Save mode | Choice | Clipboard, File | Clipboard |
| Image file path | Required | File | — |
| File format | Choice | BMP, EMF, EXIF, GIF, JPG, PNG, TIFF, WMF | BMP |

**Outputs**

| Variable | Type |
|---|---|
| ImageFile | File |

**On error:** `Failed to retrieve UI element`, `Failed to save image`, `Failed to take screenshot of UI element`.

---

### Focus text field in window

Writes the focus on a text box of a window and scrolls it into view.

Designer name: **Focus text field in window**. Official reference: [UI automation / Focus text field in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#focustextfield).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Text field | Required | UI element | — |

Produces no variables.

**On error:** `Failed to set input focus in window text box`.

---

### Populate text field in window

Fills a text box in a window with the specified text.

Designer name: **Populate text field in window**. Official reference: [UI automation / Populate text field in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#populatetextfield).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Text box | Required | UI element | — |
| Text to fill in | Required | Direct encrypted input or Text value | — |
| Simulate action | Choice | Boolean value | False |
| If field isn't empty | Optional | Replace text, Append text | Replace text |
| Click before populating | Optional | Left-click, Double-click, No | Left-click |

Produces no variables.

**On error:** `Failed to write in textbox`.

---

### Press button in window

Presses a window button.

Designer name: **Press button in window**. Official reference: [UI automation / Press button in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#pressbutton).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| UI element | Required | UI element | — |

Produces no variables.

**On error:** `Failed to press button`.

---

### Select radio button in window

Selects a radio button on a window.

Designer name: **Select radio button in window**. Official reference: [UI automation / Select radio button in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#selectradiobutton).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Radio button | Required | UI element | — |

Produces no variables.

**On error:** `Failed to select radio button UI element`.

---

### Set checkbox state in window

Checks or unchecks a checkbox in a window form.

Designer name: **Set checkbox state in window**. Official reference: [UI automation / Set checkbox state in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#setcheckboxstate).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Checkbox | Required | UI element | — |
| Set checkbox state to | Choice | Checked, Unchecked | Checked |

Produces no variables.

**On error:** `Failed to set checkbox state`.

---

### Set drop-down list value in window

Writes or clears the selected options for a drop-down list in a window form.

Designer name: **Set drop-down list value in window**. Official reference: [UI automation / Set drop-down list value in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#setdropdownlistvalueinwindow).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Drop-down list | Required | UI element | — |
| Operation | Choice | Clear selected options, Select options by name, Select options by index | Clear selected options |
| Option names | Required | List of Text values | — |
| Use regular expressions | Choice | Boolean value | False |
| Options indices | Required | List of Numeric values | — |

Produces no variables.

**On error:** `Failed to select the specified options in the drop-down list`.

---

### Get window

Reads a running window, for automating desktop applications.

Designer name: **Get window**. Official reference: [UI automation / Get window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#getwindowbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Get window | Choice | Specific window, Foreground window | Specific window |
| UI element | Required | UI element | — |
| Bring window to front | Choice | Boolean value | False |
| Fail if window isn't found | Choice | Boolean value | True |
| Timeout | Required | Numeric value | — |

**Outputs**

| Variable | Type |
|---|---|
| WindowTitle | Text value |
| AutomationWindow | Window instance |

**On error:** `Failed to get window`.

---

### Focus window

Activates and brings to the foreground a specific window.

Designer name: **Focus window**. Official reference: [UI automation / Focus window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#focuswindowbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Find window mode | Choice | By window UI element, By window instance/handle, By title and/or class | By window UI element |
| Window | Required | UI element | — |
| Window title | Optional | Text value | — |
| Window instance | Required | Numeric value | — |
| Window class | Optional | Text value | — |

Produces no variables.

**On error:** `Window wasn't found`, `Can't focus window`, `Can't perform window-related action in noninteractive mode`.

---

### Set window state

Restores, maximizes or minimizes a specific window.

Designer name: **Set window state**. Official reference: [UI automation / Set window state](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#setwindowstatebase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Find window mode | Choice | By window UI element, By window instance/handle, By title and/or class | By window UI element |
| Window | Required | UI element | — |
| Window title | Optional | Text value | — |
| Window instance | Required | Numeric value | — |
| Window class | Optional | Text value | — |
| Window state | Choice | Restored, Maximized, Minimized | Restored |

Produces no variables.

**On error:** `Window wasn't found`, `Can't set window state`, `Can't perform window-related action in noninteractive mode`.

---

### Set window visibility

Shows a hidden window or hides a visible window.

Designer name: **Set window visibility**. Official reference: [UI automation / Set window visibility](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#setwindowvisibilitybase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Find window mode | Choice | By window UI element, By window instance/handle, By title and/or class | By window UI element |
| Window | Required | UI element | — |
| Window title | Optional | Text value | — |
| Window instance | Required | Numeric value | — |
| Window class | Optional | Text value | — |
| Visibility | Choice | Visible, Hidden | Hidden |

Produces no variables.

**On error:** `Window wasn't found`, `Can't set window visibility`, `Can't perform window-related action in noninteractive mode`.

---

### Move window

Writes the position of a specific window.

Designer name: **Move window**. Official reference: [UI automation / Move window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#movewindowbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Find window mode | Choice | By window UI element, By window instance/handle, By title and/or class | By window UI element |
| Window | Required | UI element | — |
| Window title | Optional | Text value | — |
| Window instance | Required | Numeric value | — |
| Window class | Optional | Text value | — |
| Position X | Required | Numeric value | — |
| Position Y | Required | Numeric value | — |

Produces no variables.

**On error:** `Window wasn't found`, `Can't move window`, `Can't perform window-related action in noninteractive mode`.

---

### Resize window

Writes the size of a specific window.

Designer name: **Resize window**. Official reference: [UI automation / Resize window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#resizewindowbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Find window mode | Choice | By window UI element, By window instance/handle, By title and/or class | By window UI element |
| Window | Required | UI element | — |
| Window title | Optional | Text value | — |
| Window instance | Required | Numeric value | — |
| Window class | Optional | Text value | — |
| Width | Required | Numeric value | — |
| Height | Required | Numeric value | — |

Produces no variables.

**On error:** `Window wasn't found`, `Can't resize window`, `Can't perform window-related action in noninteractive mode`.

---

### Close window

Closes a specific window.

Designer name: **Close window**. Official reference: [UI automation / Close window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#closewindowbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Find window mode | Choice | By window UI element, By window instance/handle, By title and/or class | By window UI element |
| Window | Required | UI element | — |
| Window title | Optional | Text value | — |
| Window instance | Required | Numeric value | — |
| Window class | Optional | Text value | — |

Produces no variables.

**On error:** `Window wasn't found`, `Can't close window`, `Can't perform window-related action in noninteractive mode`.

---

### If window contains

Marks the beginning of a conditional block of actions depending on whether a specific piece of text or UI element exists in a window.

Designer name: **If window contains**. Official reference: [UI automation / If window contains](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#ifwindowcontainsaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Check if window | Choice | Contains UI element, Doesn't contain UI element, Contains text, Doesn't contain text | Contains UI element |
| Check UI element state | Choice | Boolean value | False |
| Text | Required | Text value | — |
| UI element | Required | UI element | — |
| Window | Required | UI element | — |
| State | Choice | Enabled, Disabled | Enabled |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Wait for window content

Suspends the execution of the automation until a specific piece of text or UI element appears or disappears from a Window.

Designer name: **Wait for window content**. Official reference: [UI automation / Wait for window content](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#waitforwindowcontentaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Wait until window | Choice | Contains UI element, Doesn't contain UI element, Contains text, Doesn't contain text | Contains UI element |
| Check UI element state | Choice | Boolean value | False |
| Text | Required | Text value | — |
| UI element | Required | UI element | — |
| Window | Required | UI element | — |
| State | Choice | Enabled, Disabled | Enabled |

Produces no variables.

**On error:** `Wait for window content failed`.

---

### If image

This action marks the beginning of a conditional block of actions depending on whether a selected image is found on the screen or not.

Designer name: **If image**. Official reference: [UI automation / If image](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#ifimageaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| If image | Choice | exists, doesn't exist | exists |
| Image | Required | List of Images | — |
| Search for image on | Choice | Entire screen, Foreground window only | Entire screen |
| Search mode | Choice | Search whole screen or foreground window, Search on specified subregion of screen or foreground window | Search whole screen or foreground window |
| Find all images in the list | Choice | Boolean value | False |
| X1 | Optional | Numeric value | — |
| X2 | Optional | Numeric value | — |
| Y1 | Optional | Numeric value | — |
| Y2 | Optional | Numeric value | — |
| Tolerance | Optional | Numeric value | 10 |
| Image matching algorithm | Choice | Basic, Advanced | Basic |

Produces no variables.

**On error:** `Can't check image in noninteractive mode`, `Invalid subregion coordinates`.

---

### Use desktop

Performs desktop and taskbar related operations.

Designer name: **Use desktop**. Official reference: [UI automation / Use desktop](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#usedesktop).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| UI element | Required | UI element | — |
| Click type | Choice | Left-click, Right-click, Double-click | Left-click |
| Launch new application when left-clicking on the taskbar | Choice | Boolean value | True |

Produces no variables.

**On error:** `Taskbar operation failed`.

---

### Select tab in window

Selects a tab from a group of tabs.

Designer name: **Select tab in window**. Official reference: [UI automation / Select tab in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#selecttab).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Tab | Required | UI element | — |

Produces no variables.

**On error:** `Selecting tab failed`.

---

### Wait for image

This action waits until a specific image appears on the screen or on the foreground window.

Designer name: **Wait for image**. Official reference: [UI automation / Wait for image](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#waitforimageaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Wait for image to | Choice | Appear, Disappear | Appear |
| Image to wait for | Required | List of Images | — |
| Search for image on | Choice | Entire screen, Foreground window only | Entire screen |
| Search mode | Choice | Search whole screen or foreground window, Search on specified subregion of screen or foreground window | Search whole screen or foreground window |
| Wait for all images | Choice | Boolean value | False |
| X1 | Optional | Numeric value | — |
| X2 | Optional | Numeric value | — |
| Y1 | Optional | Numeric value | — |
| Y2 | Optional | Numeric value | — |
| Tolerance | Optional | Numeric value | 10 |
| Image matching algorithm | Choice | Basic, Advanced | Basic |
| Fail with timeout error | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| X | Numeric value |
| Y | Numeric value |

**On error:** `Wait for image failed`, `Can't check image in noninteractive mode`, `Invalid subregion coordinates`.

---

### Hover mouse over UI element in window

Hover the mouse over any UI element on window.

Designer name: **Hover mouse over UI element in window**. Official reference: [UI automation / Hover mouse over UI element in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#hoveronelement).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| UI element | Required | UI element | — |

Produces no variables.

**On error:** `Failed to hover over element`.

---

### Click UI element in window

Clicks on any UI element of a window.

Designer name: **Click UI element in window**. Official reference: [UI automation / Click UI element in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#click).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| UI element | Required | UI element | — |
| Click type | Choice | Left-click, Right-click, Double-click, Middle-click, Left button down, Left button up, Right button down, Right button up | Left-click |
| Simulate action | Choice | Boolean value | False |
| Mouse position relative to UI element | Choice | Top left, Top center, Top right, Middle left, Middle center, Middle right, Bottom left, Bottom center, Bottom right | Middle center |
| Offset X | Optional | Text value | 0 |
| Offset Y | Optional | Text value | 0 |

Produces no variables.

**On error:** `Click failed`.

---

### Select menu option in window

Selects an option in a menu of a window.

Designer name: **Select menu option in window**. Official reference: [UI automation / Select menu option in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#selectmenuoption).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| UI element | Required | UI element | — |

Produces no variables.

**On error:** `Failed to select option`.

---

### Drag and drop UI element in window

Drags and drops a UI element of a window.

Designer name: **Drag and drop UI element in window**. Official reference: [UI automation / Drag and drop UI element in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#draganddropelement).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| UI element to drag | Required | UI element | — |
| UI element to drop over | Required | UI element | — |
| Click type | Choice | Left-click, Right-click | Left-click |
| Mouse down offset X | Optional | Text value | 0 |
| Mouse down offset Y | Optional | Text value | 0 |
| Mouse down position relative to drag-target UI element | Choice | Top left, Top center, Top right, Middle left, Middle center, Middle right, Bottom left, Bottom center, Bottom right | Middle center |
| Mouse up offset X | Optional | Text value | 0 |
| Mouse up offset Y | Optional | Text value | 0 |
| Mouse up position relative to drop-target UI element | Choice | Top left, Top center, Top right, Middle left, Middle center, Middle right, Bottom left, Bottom center, Bottom right | Middle center |

Produces no variables.

**On error:** `UI element to drag wasn't found`, `Drop target UI element wasn't found`, `Drag and drop failed`.

---

### Expand/collapse tree node in window

Expands or collapses a node of a tree view residing in a window.

Designer name: **Expand/collapse tree node in window**. Official reference: [UI automation / Expand/collapse tree node in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#expandcollapsetreenode).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| UI element | Required | UI element | — |
| Folders path | Optional | Text value | — |
| Use regular expressions | Choice | Boolean value | False |
| Operation | Choice | Expand, Collapse | Expand |

Produces no variables.

**On error:** `Failed to set tree node to the specified state`.

---

### If window

This action marks the beginning of a conditional block of actions depending on whether a window is open or not or whether a window is the focused (foreground) window.

Designer name: **If window**. Official reference: [UI automation / If window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#ifwindowaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Get window | Choice | By window UI element, By window instance/handle, By title and/or class | By window UI element |
| Window title | Optional | Text value | — |
| Window | Required | UI element | — |
| Window instance | Required | Numeric value | — |
| Window class | Optional | Text value | — |
| Check if window | Choice | Is open, Isn't open, Is focused, Isn't focused | Is open |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Wait for window

Suspends the execution or the process until a specific window opens, closes, get or loses the focus.

Designer name: **Wait for window**. Official reference: [UI automation / Wait for window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#waitforwindowaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Find window | Choice | By window UI element, By window instance/handle, By title and/or class | By window UI element |
| Window title | Optional | Text value | — |
| Window | Required | UI element | — |
| Window instance | Required | Numeric value | — |
| Window class | Optional | Text value | — |
| Wait for window to | Choice | Open, Close, Become focused, Lose focus | Open |
| Focus window after it opens | Choice | Boolean value | False |

Produces no variables.

**On error:** `Can't focus window`, `Wait for window failed`, `Can't perform window-related action in noninteractive mode`.

---
