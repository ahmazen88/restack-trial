# UI automation — how each function works

Native Actions pane module **UI automation**.

33 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Click UI element in window

- **Id:** `uiautomation/click-ui-element-in-window`
- **Kind:** native-action
- **Purpose:** Clicks UI element in window.

**Use case.** Press a real button in a desktop app when selectors are available.

**Demonstration.**

```text
**Click UI element in window**
- UI element: `UI element: Submit button`
- Click type: `Left-click`
- Simulate action: `False`
- Mouse position relative to UI element: `Middle center`
- Offset X: `0`
- Offset Y: `0`
```

**Analogy.** Pressing a labeled button with your finger.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Close window

- **Id:** `uiautomation/close-window`
- **Kind:** native-action
- **Purpose:** Closes window.

**Use case.** In a Windows app with no API, drop **Close window** on the canvas. Closes window.

**Demonstration.**

```text
**Close window**
- Find window mode: `%Window%`
- Window: `%Window%`
- Window title: `INV-1042`
- Window instance: `1`
- Window class: `INV-1042`
```

**Analogy.** Turning out the lights when the work in that room is done.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window. Call this only after the last use of the instance so you do not break later steps.

### Drag and drop UI element in window

- **Id:** `uiautomation/drag-and-drop-ui-element-in-window`
- **Kind:** native-action
- **Purpose:** Drags and drops UI element in window.

**Use case.** In a Windows app with no API, drop **Drag and drop UI element in window** on the canvas. Drags and drops UI element in window.

**Demonstration.**

```text
**Drag and drop UI element in window**
- UI element to drag: `UI element: Submit button`
- UI element to drop over: `UI element: Submit button`
- Click type: `Left-click`
- Mouse down offset X: `0`
- Mouse down offset Y: `0`
- Mouse down position relative to drag-target UI element: `Middle center`
- Mouse up offset X: `0`
- Mouse up offset Y: `0`
- … 1 more parameter(s) in the action modal
```

**Analogy.** One tool in that kit: a person who can see buttons and type into boxes on a window.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Expand/collapse tree node in window

- **Id:** `uiautomation/expand-collapse-tree-node-in-window`
- **Kind:** native-action
- **Purpose:** Expands or collapses tree node in window.

**Use case.** In a Windows app with no API, drop **Expand/collapse tree node in window** on the canvas. Expands or collapses tree node in window.

**Demonstration.**

```text
**Expand/collapse tree node in window**
- UI element: `UI element: Submit button`
- Folders path: `C:\RPA\Invoices`
- Use regular expressions: `False`
- Operation: `Expand`
```

**Analogy.** One tool in that kit: a person who can see buttons and type into boxes on a window.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Extract data from table

- **Id:** `uiautomation/extract-data-from-table`
- **Kind:** native-action
- **Purpose:** Extracts data from table.

**Use case.** In a Windows app with no API, drop **Extract data from table** on the canvas. Extracts data from table.

**Demonstration.**

```text
**Extract data from table**
- Table: `UI element: Submit button`
- Store extracted data in: `an Excel spreadsheet`
- Bring to front: `True`
Produces:
- `%ExcelInstance%` (Excel instance)
- `%DataFromTable%` (General value)
```

**Analogy.** One tool in that kit: a person who can see buttons and type into boxes on a window.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Extract data from window

- **Id:** `uiautomation/extract-data-from-window`
- **Kind:** native-action
- **Purpose:** Extracts data from window.

**Use case.** In a Windows app with no API, drop **Extract data from window** on the canvas. Extracts data from window.

**Demonstration.**

```text
**Extract data from window**
- Window: `%Window%`
- Store extracted data in: `an Excel spreadsheet`
- Bring to front: `True`
Produces:
- `%ExcelInstance%` (Excel instance)
- `%DataFromWindow%` (General value)
```

**Analogy.** One tool in that kit: a person who can see buttons and type into boxes on a window.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Focus text field in window

- **Id:** `uiautomation/focus-text-field-in-window`
- **Kind:** native-action
- **Purpose:** Gives focus to text field in window.

**Use case.** In a Windows app with no API, drop **Focus text field in window** on the canvas. Gives focus to text field in window.

**Demonstration.**

```text
**Focus text field in window**
- Text field: `UI element: Submit button`
```

**Analogy.** One tool in that kit: a person who can see buttons and type into boxes on a window.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Focus window

- **Id:** `uiautomation/focus-window`
- **Kind:** native-action
- **Purpose:** Gives focus to window.

**Use case.** In a Windows app with no API, drop **Focus window** on the canvas. Gives focus to window.

**Demonstration.**

```text
**Focus window**
- Find window mode: `%Window%`
- Window: `%Window%`
- Window title: `INV-1042`
- Window instance: `1`
- Window class: `INV-1042`
```

**Analogy.** One tool in that kit: a person who can see buttons and type into boxes on a window.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Get details of a UI element in window

- **Id:** `uiautomation/get-details-of-a-ui-element-in-window`
- **Kind:** native-action
- **Purpose:** Reads details of a UI element in window into a flow variable.

**Use case.** In a Windows app with no API, drop **Get details of a UI element in window** on the canvas. Reads details of a UI element in window into a flow variable.

**Demonstration.**

```text
**Get details of a UI element in window**
- UI element: `UI element: Submit button`
- Attribute name: `Own Text`
- Bring to front: `True`
Produces:
- `%AttributeValue%` (Text value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Get details of window

- **Id:** `uiautomation/get-details-of-window`
- **Kind:** native-action
- **Purpose:** Reads details of window into a flow variable.

**Use case.** In a Windows app with no API, drop **Get details of window** on the canvas. Reads details of window into a flow variable.

**Demonstration.**

```text
**Get details of window**
- Window: `%Window%`
- Window property: `Get window title`
- Bring to front: `True`
Produces:
- `%WindowProperty%` (General value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Get selected checkboxes in window

- **Id:** `uiautomation/get-selected-checkboxes-in-window`
- **Kind:** native-action
- **Purpose:** Reads selected checkboxes in window into a flow variable.

**Use case.** In a Windows app with no API, drop **Get selected checkboxes in window** on the canvas. Reads selected checkboxes in window into a flow variable.

**Demonstration.**

```text
**Get selected checkboxes in window**
- UI element: `UI element: Submit button`
- Operation: `Get names of selected checkboxes in group`
- Bring to front: `True`
Produces:
- `%IsChecked%` (Boolean value)
- `%SelectedCheckboxes%` (List of Text values)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Get selected radio button in window

- **Id:** `uiautomation/get-selected-radio-button-in-window`
- **Kind:** native-action
- **Purpose:** Reads selected radio button in window into a flow variable.

**Use case.** In a Windows app with no API, drop **Get selected radio button in window** on the canvas. Reads selected radio button in window into a flow variable.

**Demonstration.**

```text
**Get selected radio button in window**
- UI element: `UI element: Submit button`
- Operation: `Get selected radio button name in group`
- Bring to front: `True`
Produces:
- `%IsSelected%` (Boolean value)
- `%SelectedRadiobutton%` (Text value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Get window

- **Id:** `uiautomation/get-window`
- **Kind:** native-action
- **Purpose:** Reads window into a flow variable.

**Use case.** In a Windows app with no API, drop **Get window** on the canvas. Reads window into a flow variable.

**Demonstration.**

```text
**Get window**
- Get window: `Specific window`
- UI element: `UI element: Submit button`
- Bring window to front: `False`
- Fail if window isn't found: `True`
- Timeout: `30`
Produces:
- `%WindowTitle%` (Text value)
- `%AutomationWindow%` (Window instance)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Hover mouse over UI element in window

- **Id:** `uiautomation/hover-mouse-over-ui-element-in-window`
- **Kind:** native-action
- **Purpose:** Hovers mouse over UI element in window.

**Use case.** In a Windows app with no API, drop **Hover mouse over UI element in window** on the canvas. Hovers mouse over UI element in window.

**Demonstration.**

```text
**Hover mouse over UI element in window**
- UI element: `UI element: Submit button`
```

**Analogy.** One tool in that kit: a person who can see buttons and type into boxes on a window.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### If image

- **Id:** `uiautomation/if-image`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when image.

**Use case.** In a Windows app with no API, drop **If image** on the canvas. Opens a conditional branch that runs when image.

**Demonstration.**

```text
**If image**
- If image: `exists`
- Image: `%Files%`
- Search for image on: `Entire screen`
- Search mode: `Search whole screen or foreground window`
- Find all images in the list: `False`
- X1: `1`
- X2: `1`
- Y1: `1`
- … 3 more parameter(s) in the action modal
Place the actions that should run inside this block, then End.
```

**Analogy.** Checking a condition on a clipboard before you choose a door.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window. Combine with Else / Else if and End. Put Wait or If file exists before brittle UI/browser steps.

### If window

- **Id:** `uiautomation/if-window`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when window.

**Use case.** In a Windows app with no API, drop **If window** on the canvas. Opens a conditional branch that runs when window.

**Demonstration.**

```text
**If window**
- Get window: `%Window%`
- Window title: `INV-1042`
- Window: `%Window%`
- Window instance: `1`
- Window class: `INV-1042`
- Check if window: `Is open`
Place the actions that should run inside this block, then End.
```

**Analogy.** Checking a condition on a clipboard before you choose a door.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window. Combine with Else / Else if and End. Put Wait or If file exists before brittle UI/browser steps.

### If window contains

- **Id:** `uiautomation/if-window-contains`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when window contains.

**Use case.** In a Windows app with no API, drop **If window contains** on the canvas. Opens a conditional branch that runs when window contains.

**Demonstration.**

```text
**If window contains**
- Check if window: `UI element: Submit button`
- Check UI element state: `False`
- Text: `INV-1042`
- UI element: `UI element: Submit button`
- Window: `%Window%`
- State: `Enabled`
Place the actions that should run inside this block, then End.
```

**Analogy.** Checking a condition on a clipboard before you choose a door.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window. Combine with Else / Else if and End. Put Wait or If file exists before brittle UI/browser steps.

### Move window

- **Id:** `uiautomation/move-window`
- **Kind:** native-action
- **Purpose:** Moves window.

**Use case.** In a Windows app with no API, drop **Move window** on the canvas. Moves window.

**Demonstration.**

```text
**Move window**
- Find window mode: `%Window%`
- Window: `%Window%`
- Window title: `INV-1042`
- Window instance: `1`
- Window class: `INV-1042`
- Position X: `1`
- Position Y: `1`
```

**Analogy.** One tool in that kit: a person who can see buttons and type into boxes on a window.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Populate text field in window

- **Id:** `uiautomation/populate-text-field-in-window`
- **Kind:** native-action
- **Purpose:** Types or fills text field in window.

**Use case.** In a Windows app with no API, drop **Populate text field in window** on the canvas. Types or fills text field in window.

**Demonstration.**

```text
**Populate text field in window**
- Text box: `UI element: Submit button`
- Text to fill in: `INV-1042`
- Simulate action: `False`
- If field isn't empty: `Replace text`
- Click before populating: `Left-click`
```

**Analogy.** Filling a paper form field with a pen.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Press button in window

- **Id:** `uiautomation/press-button-in-window`
- **Kind:** native-action
- **Purpose:** Presses button in window.

**Use case.** In a Windows app with no API, drop **Press button in window** on the canvas. Presses button in window.

**Demonstration.**

```text
**Press button in window**
- UI element: `UI element: Submit button`
```

**Analogy.** Pushing the exact button a trained operator would push.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Resize window

- **Id:** `uiautomation/resize-window`
- **Kind:** native-action
- **Purpose:** Sets the size of a specific window.

**Use case.** In a Windows app with no API, drop **Resize window** on the canvas. Sets the size of a specific window.

**Demonstration.**

```text
**Resize window**
- Find window mode: `%Window%`
- Window: `%Window%`
- Window title: `INV-1042`
- Window instance: `1`
- Window class: `INV-1042`
- Width: `1`
- Height: `1`
```

**Analogy.** One tool in that kit: a person who can see buttons and type into boxes on a window.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Select menu option in window

- **Id:** `uiautomation/select-menu-option-in-window`
- **Kind:** native-action
- **Purpose:** Selects menu option in window.

**Use case.** In a Windows app with no API, drop **Select menu option in window** on the canvas. Selects menu option in window.

**Demonstration.**

```text
**Select menu option in window**
- UI element: `UI element: Submit button`
```

**Analogy.** One tool in that kit: a person who can see buttons and type into boxes on a window.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Select radio button in window

- **Id:** `uiautomation/select-radio-button-in-window`
- **Kind:** native-action
- **Purpose:** Selects radio button in window.

**Use case.** In a Windows app with no API, drop **Select radio button in window** on the canvas. Selects radio button in window.

**Demonstration.**

```text
**Select radio button in window**
- Radio button: `UI element: Submit button`
```

**Analogy.** One tool in that kit: a person who can see buttons and type into boxes on a window.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Select tab in window

- **Id:** `uiautomation/select-tab-in-window`
- **Kind:** native-action
- **Purpose:** Selects tab in window.

**Use case.** In a Windows app with no API, drop **Select tab in window** on the canvas. Selects tab in window.

**Demonstration.**

```text
**Select tab in window**
- Tab: `UI element: Submit button`
```

**Analogy.** One tool in that kit: a person who can see buttons and type into boxes on a window.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Set checkbox state in window

- **Id:** `uiautomation/set-checkbox-state-in-window`
- **Kind:** native-action
- **Purpose:** Writes checkbox state in window.

**Use case.** In a Windows app with no API, drop **Set checkbox state in window** on the canvas. Writes checkbox state in window.

**Demonstration.**

```text
**Set checkbox state in window**
- Checkbox: `UI element: Submit button`
- Set checkbox state to: `Checked`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Set drop-down list value in window

- **Id:** `uiautomation/set-drop-down-list-value-in-window`
- **Kind:** native-action
- **Purpose:** Writes drop-down list value in window.

**Use case.** In a Windows app with no API, drop **Set drop-down list value in window** on the canvas. Writes drop-down list value in window.

**Demonstration.**

```text
**Set drop-down list value in window**
- Drop-down list: `UI element: Submit button`
- Operation: `Clear selected options`
- Option names: `%Files%`
- Use regular expressions: `False`
- Options indices: `%Files%`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Set window state

- **Id:** `uiautomation/set-window-state`
- **Kind:** native-action
- **Purpose:** Writes window state.

**Use case.** In a Windows app with no API, drop **Set window state** on the canvas. Writes window state.

**Demonstration.**

```text
**Set window state**
- Find window mode: `%Window%`
- Window: `%Window%`
- Window title: `INV-1042`
- Window instance: `1`
- Window class: `INV-1042`
- Window state: `Restored`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Set window visibility

- **Id:** `uiautomation/set-window-visibility`
- **Kind:** native-action
- **Purpose:** Writes window visibility.

**Use case.** In a Windows app with no API, drop **Set window visibility** on the canvas. Writes window visibility.

**Demonstration.**

```text
**Set window visibility**
- Find window mode: `%Window%`
- Window: `%Window%`
- Window title: `INV-1042`
- Window instance: `1`
- Window class: `INV-1042`
- Visibility: `Hidden`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Take screenshot of UI element

- **Id:** `uiautomation/take-screenshot-of-ui-element`
- **Kind:** native-action
- **Purpose:** Captures screenshot of UI element.

**Use case.** In a Windows app with no API, drop **Take screenshot of UI element** on the canvas. Captures screenshot of UI element.

**Demonstration.**

```text
**Take screenshot of UI element**
- UI element: `UI element: Submit button`
- Save mode: `Clipboard`
- Image file path: `C:\RPA\Invoices\INV-1042.pdf`
- File format: `C:\RPA\Invoices\INV-1042.pdf`
Produces:
- `%ImageFile%` (File)
```

**Analogy.** One tool in that kit: a person who can see buttons and type into boxes on a window.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Use desktop

- **Id:** `uiautomation/use-desktop`
- **Kind:** native-action
- **Purpose:** Performs desktop and taskbar related operations.

**Use case.** In a Windows app with no API, drop **Use desktop** on the canvas. Performs desktop and taskbar related operations.

**Demonstration.**

```text
**Use desktop**
- UI element: `UI element: Submit button`
- Click type: `Left-click`
- Launch new application when left-clicking on the taskbar: `True`
```

**Analogy.** One tool in that kit: a person who can see buttons and type into boxes on a window.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Wait for image

- **Id:** `uiautomation/wait-for-image`
- **Kind:** native-action
- **Purpose:** Pauses the flow until image.

**Use case.** In a Windows app with no API, drop **Wait for image** on the canvas. Pauses the flow until image.

**Demonstration.**

```text
**Wait for image**
- Wait for image to: `Appear`
- Image to wait for: `%Files%`
- Search for image on: `Entire screen`
- Search mode: `Search whole screen or foreground window`
- Wait for all images: `False`
- X1: `1`
- X2: `1`
- Y1: `1`
- … 4 more parameter(s) in the action modal
Produces:
- `%X%` (Numeric value)
- `%Y%` (Numeric value)
```

**Analogy.** Standing at the microwave until it beeps, so you do not grab a cold plate.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Wait for window

- **Id:** `uiautomation/wait-for-window`
- **Kind:** native-action
- **Purpose:** Pauses the flow until window.

**Use case.** In a Windows app with no API, drop **Wait for window** on the canvas. Pauses the flow until window.

**Demonstration.**

```text
**Wait for window**
- Find window: `%Window%`
- Window title: `INV-1042`
- Window: `%Window%`
- Window instance: `1`
- Window class: `INV-1042`
- Wait for window to: `Open`
- Focus window after it opens: `False`
```

**Analogy.** Standing at the microwave until it beeps, so you do not grab a cold plate.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.

### Wait for window content

- **Id:** `uiautomation/wait-for-window-content`
- **Kind:** native-action
- **Purpose:** Pauses the flow until window content.

**Use case.** In a Windows app with no API, drop **Wait for window content** on the canvas. Pauses the flow until window content.

**Demonstration.**

```text
**Wait for window content**
- Wait until window: `UI element: Submit button`
- Check UI element state: `False`
- Text: `INV-1042`
- UI element: `UI element: Submit button`
- Window: `%Window%`
- State: `Enabled`
```

**Analogy.** Standing at the microwave until it beeps, so you do not grab a cold plate.

**In combination.** Get window, populate/click UI elements, Wait for window content, Close window.
