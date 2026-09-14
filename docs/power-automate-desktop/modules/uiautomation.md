# UI automation

Click, fill, extract, and wait on desktop application UI elements.

This page documents every **native action** in this group (33 items).

## Actions

### Click UI element in window

- **Inventory id:** `uiautomation/click-ui-element-in-window`
- **Kind:** native-action
- **Purpose:** Clicks UI element in window.
- **Key inputs:** `UI element` (UI element); `Click type` (Left-click, Right-click, Double-click, Middle-click, Left button down, Left button up, Right button down, Right button up); `Simulate action` (Boolean value); `Mouse position relative to UI element` (Top left, Top center, Top right, Middle left, Middle center, Middle right, Bottom left, Bottom center, Bottom right); `Offset X` (Text value; optional); `Offset Y` (Text value; optional)
- **Produces:** None listed
- **Exceptions:** `Click failed`
- **Microsoft Learn:** [Click UI element in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#click)

### Close window

- **Inventory id:** `uiautomation/close-window`
- **Kind:** native-action
- **Purpose:** Closes window.
- **Key inputs:** `Find window mode` (By window UI element, By window instance/handle, By title and/or class); `Window` (UI element); `Window title` (Text value; optional); `Window instance` (Numeric value); `Window class` (Text value; optional)
- **Produces:** None listed
- **Exceptions:** `Window wasn't found`; `Can't close window`; `Can't perform window-related action in noninteractive mode`
- **Microsoft Learn:** [Close window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#closewindowbase)

### Drag and drop UI element in window

- **Inventory id:** `uiautomation/drag-and-drop-ui-element-in-window`
- **Kind:** native-action
- **Purpose:** Drags and drops UI element in window.
- **Key inputs:** `UI element to drag` (UI element); `UI element to drop over` (UI element); `Click type` (Left-click, Right-click); `Mouse down offset X` (Text value; optional); `Mouse down offset Y` (Text value; optional); `Mouse down position relative to drag-target UI element` (Top left, Top center, Top right, Middle left, Middle center, Middle right, Bottom left, Bottom center, Bottom right); `Mouse up offset X` (Text value; optional); `Mouse up offset Y` (Text value; optional); `Mouse up position relative to drop-target UI element` (Top left, Top center, Top right, Middle left, Middle center, Middle right, Bottom left, Bottom center, Bottom right)
- **Produces:** None listed
- **Exceptions:** `UI element to drag wasn't found`; `Drop target UI element wasn't found`; `Drag and drop failed`
- **Microsoft Learn:** [Drag and drop UI element in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#draganddropelement)

### Expand/collapse tree node in window

- **Inventory id:** `uiautomation/expand-collapse-tree-node-in-window`
- **Kind:** native-action
- **Purpose:** Expands or collapses tree node in window.
- **Key inputs:** `UI element` (UI element); `Folders path` (Text value; optional); `Use regular expressions` (Boolean value); `Operation` (Expand, Collapse)
- **Produces:** None listed
- **Exceptions:** `Failed to set tree node to the specified state`
- **Microsoft Learn:** [Expand/collapse tree node in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#expandcollapsetreenode)

### Extract data from table

- **Inventory id:** `uiautomation/extract-data-from-table`
- **Kind:** native-action
- **Purpose:** Extracts data from table.
- **Key inputs:** `Table` (UI element); `Store extracted data in` (an Excel spreadsheet, A variable); `Bring to front` (Boolean value)
- **Produces:** `ExcelInstance` (Excel instance); `DataFromTable` (General value)
- **Exceptions:** `Extraction failed`
- **Microsoft Learn:** [Extract data from table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#extractdatafromtable)

### Extract data from window

- **Inventory id:** `uiautomation/extract-data-from-window`
- **Kind:** native-action
- **Purpose:** Extracts data from window.
- **Key inputs:** `Window` (UI element); `Store extracted data in` (an Excel spreadsheet, A variable); `Bring to front` (Boolean value)
- **Produces:** `ExcelInstance` (Excel instance); `DataFromWindow` (General value)
- **Exceptions:** `Extraction failed`
- **Microsoft Learn:** [Extract data from window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#extractdatafromwindow)

### Focus text field in window

- **Inventory id:** `uiautomation/focus-text-field-in-window`
- **Kind:** native-action
- **Purpose:** Gives focus to text field in window.
- **Key inputs:** `Text field` (UI element)
- **Produces:** None listed
- **Exceptions:** `Failed to set input focus in window text box`
- **Microsoft Learn:** [Focus text field in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#focustextfield)

### Focus window

- **Inventory id:** `uiautomation/focus-window`
- **Kind:** native-action
- **Purpose:** Gives focus to window.
- **Key inputs:** `Find window mode` (By window UI element, By window instance/handle, By title and/or class); `Window` (UI element); `Window title` (Text value; optional); `Window instance` (Numeric value); `Window class` (Text value; optional)
- **Produces:** None listed
- **Exceptions:** `Window wasn't found`; `Can't focus window`; `Can't perform window-related action in noninteractive mode`
- **Microsoft Learn:** [Focus window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#focuswindowbase)

### Get details of a UI element in window

- **Inventory id:** `uiautomation/get-details-of-a-ui-element-in-window`
- **Kind:** native-action
- **Purpose:** Reads details of a UI element in window into a flow variable.
- **Key inputs:** `UI element` (UI element); `Attribute name` (Text value; optional); `Bring to front` (Boolean value)
- **Produces:** `AttributeValue` (Text value)
- **Exceptions:** `Failed to retrieve attribute of UI element`
- **Microsoft Learn:** [Get details of a UI element in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#getelementdetails)

### Get details of window

- **Inventory id:** `uiautomation/get-details-of-window`
- **Kind:** native-action
- **Purpose:** Reads details of window into a flow variable.
- **Key inputs:** `Window` (UI element); `Window property` (Get window title, Get window text, Get window location and size, Get process name); `Bring to front` (Boolean value)
- **Produces:** `WindowProperty` (General value)
- **Exceptions:** `Failed to retrieve property of window`
- **Microsoft Learn:** [Get details of window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#getwindowdetails)

### Get selected checkboxes in window

- **Inventory id:** `uiautomation/get-selected-checkboxes-in-window`
- **Kind:** native-action
- **Purpose:** Reads selected checkboxes in window into a flow variable.
- **Key inputs:** `UI element` (UI element); `Operation` (Get names of selected checkboxes in group, Get state of checkbox); `Bring to front` (Boolean value)
- **Produces:** `IsChecked` (Boolean value); `SelectedCheckboxes` (List of Text values)
- **Exceptions:** `Failed to retrieve checkbox state(s)`
- **Microsoft Learn:** [Get selected checkboxes in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#getselectedcheckboxesinwindow)

### Get selected radio button in window

- **Inventory id:** `uiautomation/get-selected-radio-button-in-window`
- **Kind:** native-action
- **Purpose:** Reads selected radio button in window into a flow variable.
- **Key inputs:** `UI element` (UI element); `Operation` (Get selected radio button name in group, Get state of radio button); `Bring to front` (Boolean value)
- **Produces:** `IsSelected` (Boolean value); `SelectedRadiobutton` (Text value)
- **Exceptions:** `Failed to retrieve radio button state`
- **Microsoft Learn:** [Get selected radio button in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#getselectedradiobuttoninwindow)

### Get window

- **Inventory id:** `uiautomation/get-window`
- **Kind:** native-action
- **Purpose:** Reads window into a flow variable.
- **Key inputs:** `Get window` (Specific window, Foreground window); `UI element` (UI element); `Bring window to front` (Boolean value); `Fail if window isn't found` (Boolean value); `Timeout` (Numeric value)
- **Produces:** `WindowTitle` (Text value); `AutomationWindow` (Window instance)
- **Exceptions:** `Failed to get window`
- **Microsoft Learn:** [Get window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#getwindowbase)

### Hover mouse over UI element in window

- **Inventory id:** `uiautomation/hover-mouse-over-ui-element-in-window`
- **Kind:** native-action
- **Purpose:** Hovers mouse over UI element in window.
- **Key inputs:** `UI element` (UI element)
- **Produces:** None listed
- **Exceptions:** `Failed to hover over element`
- **Microsoft Learn:** [Hover mouse over UI element in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#hoveronelement)

### If image

- **Inventory id:** `uiautomation/if-image`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when image.
- **Key inputs:** `If image` (exists, doesn't exist); `Image` (List of Images); `Search for image on` (Entire screen, Foreground window only); `Search mode` (Search whole screen or foreground window, Search on specified subregion of screen or foreground window); `Find all images in the list` (Boolean value); `X1` (Numeric value; optional); `X2` (Numeric value; optional); `Y1` (Numeric value; optional); `Y2` (Numeric value; optional); `Tolerance` (Numeric value; optional); `Image matching algorithm` (Basic, Advanced)
- **Produces:** None listed
- **Exceptions:** `Can't check image in noninteractive mode`; `Invalid subregion coordinates`
- **Microsoft Learn:** [If image](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#ifimageaction)

### If window

- **Inventory id:** `uiautomation/if-window`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when window.
- **Key inputs:** `Get window` (By window UI element, By window instance/handle, By title and/or class); `Window title` (Text value; optional); `Window` (UI element); `Window instance` (Numeric value); `Window class` (Text value; optional); `Check if window` (Is open, Isn't open, Is focused, Isn't focused)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [If window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#ifwindowaction)

### If window contains

- **Inventory id:** `uiautomation/if-window-contains`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when window contains.
- **Key inputs:** `Check if window` (Contains UI element, Doesn't contain UI element, Contains text, Doesn't contain text); `Check UI element state` (Boolean value); `Text` (Text value); `UI element` (UI element); `Window` (UI element); `State` (Enabled, Disabled)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [If window contains](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#ifwindowcontainsaction)

### Move window

- **Inventory id:** `uiautomation/move-window`
- **Kind:** native-action
- **Purpose:** Moves window.
- **Key inputs:** `Find window mode` (By window UI element, By window instance/handle, By title and/or class); `Window` (UI element); `Window title` (Text value; optional); `Window instance` (Numeric value); `Window class` (Text value; optional); `Position X` (Numeric value); `Position Y` (Numeric value)
- **Produces:** None listed
- **Exceptions:** `Window wasn't found`; `Can't move window`; `Can't perform window-related action in noninteractive mode`
- **Microsoft Learn:** [Move window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#movewindowbase)

### Populate text field in window

- **Inventory id:** `uiautomation/populate-text-field-in-window`
- **Kind:** native-action
- **Purpose:** Types or fills text field in window.
- **Key inputs:** `Text box` (UI element); `Text to fill in` (Direct encrypted input or Text value); `Simulate action` (Boolean value); `If field isn't empty` (Replace text, Append text; optional); `Click before populating` (Left-click, Double-click, No; optional)
- **Produces:** None listed
- **Exceptions:** `Failed to write in textbox`
- **Microsoft Learn:** [Populate text field in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#populatetextfield)

### Press button in window

- **Inventory id:** `uiautomation/press-button-in-window`
- **Kind:** native-action
- **Purpose:** Presses button in window.
- **Key inputs:** `UI element` (UI element)
- **Produces:** None listed
- **Exceptions:** `Failed to press button`
- **Microsoft Learn:** [Press button in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#pressbutton)

### Resize window

- **Inventory id:** `uiautomation/resize-window`
- **Kind:** native-action
- **Purpose:** Sets the size of a specific window.
- **Key inputs:** `Find window mode` (By window UI element, By window instance/handle, By title and/or class); `Window` (UI element); `Window title` (Text value; optional); `Window instance` (Numeric value); `Window class` (Text value; optional); `Width` (Numeric value); `Height` (Numeric value)
- **Produces:** None listed
- **Exceptions:** `Window wasn't found`; `Can't resize window`; `Can't perform window-related action in noninteractive mode`
- **Microsoft Learn:** [Resize window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#resizewindowbase)

### Select menu option in window

- **Inventory id:** `uiautomation/select-menu-option-in-window`
- **Kind:** native-action
- **Purpose:** Selects menu option in window.
- **Key inputs:** `UI element` (UI element)
- **Produces:** None listed
- **Exceptions:** `Failed to select option`
- **Microsoft Learn:** [Select menu option in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#selectmenuoption)

### Select radio button in window

- **Inventory id:** `uiautomation/select-radio-button-in-window`
- **Kind:** native-action
- **Purpose:** Selects radio button in window.
- **Key inputs:** `Radio button` (UI element)
- **Produces:** None listed
- **Exceptions:** `Failed to select radio button UI element`
- **Microsoft Learn:** [Select radio button in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#selectradiobutton)

### Select tab in window

- **Inventory id:** `uiautomation/select-tab-in-window`
- **Kind:** native-action
- **Purpose:** Selects tab in window.
- **Key inputs:** `Tab` (UI element)
- **Produces:** None listed
- **Exceptions:** `Selecting tab failed`
- **Microsoft Learn:** [Select tab in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#selecttab)

### Set checkbox state in window

- **Inventory id:** `uiautomation/set-checkbox-state-in-window`
- **Kind:** native-action
- **Purpose:** Writes checkbox state in window.
- **Key inputs:** `Checkbox` (UI element); `Set checkbox state to` (Checked, Unchecked)
- **Produces:** None listed
- **Exceptions:** `Failed to set checkbox state`
- **Microsoft Learn:** [Set checkbox state in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#setcheckboxstate)

### Set drop-down list value in window

- **Inventory id:** `uiautomation/set-drop-down-list-value-in-window`
- **Kind:** native-action
- **Purpose:** Writes drop-down list value in window.
- **Key inputs:** `Drop-down list` (UI element); `Operation` (Clear selected options, Select options by name, Select options by index); `Option names` (List of Text values); `Use regular expressions` (Boolean value); `Options indices` (List of Numeric values)
- **Produces:** None listed
- **Exceptions:** `Failed to select the specified options in the drop-down list`
- **Microsoft Learn:** [Set drop-down list value in window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#setdropdownlistvalueinwindow)

### Set window state

- **Inventory id:** `uiautomation/set-window-state`
- **Kind:** native-action
- **Purpose:** Writes window state.
- **Key inputs:** `Find window mode` (By window UI element, By window instance/handle, By title and/or class); `Window` (UI element); `Window title` (Text value; optional); `Window instance` (Numeric value); `Window class` (Text value; optional); `Window state` (Restored, Maximized, Minimized)
- **Produces:** None listed
- **Exceptions:** `Window wasn't found`; `Can't set window state`; `Can't perform window-related action in noninteractive mode`
- **Microsoft Learn:** [Set window state](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#setwindowstatebase)

### Set window visibility

- **Inventory id:** `uiautomation/set-window-visibility`
- **Kind:** native-action
- **Purpose:** Writes window visibility.
- **Key inputs:** `Find window mode` (By window UI element, By window instance/handle, By title and/or class); `Window` (UI element); `Window title` (Text value; optional); `Window instance` (Numeric value); `Window class` (Text value; optional); `Visibility` (Visible, Hidden)
- **Produces:** None listed
- **Exceptions:** `Window wasn't found`; `Can't set window visibility`; `Can't perform window-related action in noninteractive mode`
- **Microsoft Learn:** [Set window visibility](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#setwindowvisibilitybase)

### Take screenshot of UI element

- **Inventory id:** `uiautomation/take-screenshot-of-ui-element`
- **Kind:** native-action
- **Purpose:** Captures screenshot of UI element.
- **Key inputs:** `UI element` (UI element); `Save mode` (Clipboard, File); `Image file path` (File); `File format` (BMP, EMF, EXIF, GIF, JPG, PNG, TIFF, WMF)
- **Produces:** `ImageFile` (File)
- **Exceptions:** `Failed to retrieve UI element`; `Failed to save image`; `Failed to take screenshot of UI element`
- **Microsoft Learn:** [Take screenshot of UI element](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#takescreenshot)

### Use desktop

- **Inventory id:** `uiautomation/use-desktop`
- **Kind:** native-action
- **Purpose:** Performs desktop and taskbar related operations.
- **Key inputs:** `UI element` (UI element); `Click type` (Left-click, Right-click, Double-click); `Launch new application when left-clicking on the taskbar` (Boolean value)
- **Produces:** None listed
- **Exceptions:** `Taskbar operation failed`
- **Microsoft Learn:** [Use desktop](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#usedesktop)

### Wait for image

- **Inventory id:** `uiautomation/wait-for-image`
- **Kind:** native-action
- **Purpose:** Pauses the flow until image.
- **Key inputs:** `Wait for image to` (Appear, Disappear); `Image to wait for` (List of Images); `Search for image on` (Entire screen, Foreground window only); `Search mode` (Search whole screen or foreground window, Search on specified subregion of screen or foreground window); `Wait for all images` (Boolean value); `X1` (Numeric value; optional); `X2` (Numeric value; optional); `Y1` (Numeric value; optional); `Y2` (Numeric value; optional); `Tolerance` (Numeric value; optional); `Image matching algorithm` (Basic, Advanced); `Fail with timeout error` (Boolean value)
- **Produces:** `X` (Numeric value); `Y` (Numeric value)
- **Exceptions:** `Wait for image failed`; `Can't check image in noninteractive mode`; `Invalid subregion coordinates`
- **Microsoft Learn:** [Wait for image](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#waitforimageaction)

### Wait for window

- **Inventory id:** `uiautomation/wait-for-window`
- **Kind:** native-action
- **Purpose:** Pauses the flow until window.
- **Key inputs:** `Find window` (By window UI element, By window instance/handle, By title and/or class); `Window title` (Text value; optional); `Window` (UI element); `Window instance` (Numeric value); `Window class` (Text value; optional); `Wait for window to` (Open, Close, Become focused, Lose focus); `Focus window after it opens` (Boolean value)
- **Produces:** None listed
- **Exceptions:** `Can't focus window`; `Wait for window failed`; `Can't perform window-related action in noninteractive mode`
- **Microsoft Learn:** [Wait for window](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#waitforwindowaction)

### Wait for window content

- **Inventory id:** `uiautomation/wait-for-window-content`
- **Kind:** native-action
- **Purpose:** Pauses the flow until window content.
- **Key inputs:** `Wait until window` (Contains UI element, Doesn't contain UI element, Contains text, Doesn't contain text); `Check UI element state` (Boolean value); `Text` (Text value); `UI element` (UI element); `Window` (UI element); `State` (Enabled, Disabled)
- **Produces:** None listed
- **Exceptions:** `Wait for window content failed`
- **Microsoft Learn:** [Wait for window content](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/uiautomation#waitforwindowcontentaction)
