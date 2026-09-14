# Browser automation — how each function works

Native Actions pane module **Browser automation**.

23 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Click download link on web page

- **Id:** `webautomation/click-download-link-on-web-page`
- **Kind:** native-action
- **Purpose:** Clicks download link on web page.

**Use case.** In a web portal with no stable API, drop **Click download link on web page** on the canvas. Clicks download link on web page.

**Demonstration.**

```text
**Click download link on web page**
- Web browser instance: `%Browser%`
- UI element: `UI element: Submit button`
- Destination folder: `C:\RPA\Invoices`
Produces:
- `%`DownloadedFile`%` (File)
```

**Analogy.** Pushing the exact button a trained operator would push.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.

### Click link on web page

- **Id:** `webautomation/click-link-on-web-page`
- **Kind:** native-action
- **Purpose:** Clicks link on web page.

**Use case.** In a web portal with no stable API, drop **Click link on web page** on the canvas. Clicks link on web page.

**Demonstration.**

```text
**Click link on web page**
- Web browser instance: `%Browser%`
- UI element: `UI element: Submit button`
- Click type: `(set in designer)`
- Send physical click: `True`
- Wait for page to load: `True`
- Timeout for webpage to load: `1`
- If a pop-up dialog appears: `(set in designer)`
- Dialog button to press: `INV-1042`
```

**Analogy.** Pushing the exact button a trained operator would push.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.

### Close web browser

- **Id:** `webautomation/close-web-browser`
- **Kind:** native-action
- **Purpose:** Closes web browser.

**Use case.** In a web portal with no stable API, drop **Close web browser** on the canvas. Closes web browser.

**Demonstration.**

```text
**Close web browser**
- Web browser instance: `%Browser%`
```

**Analogy.** Logging off that browser so the next job starts clean.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser. Call this only after the last use of the instance so you do not break later steps.

### Create new tab

- **Id:** `webautomation/create-new-tab`
- **Kind:** native-action
- **Purpose:** Creates new tab.

**Use case.** In a web portal with no stable API, drop **Create new tab** on the canvas. Creates new tab.

**Demonstration.**

```text
**Create new tab**
- Web browser instance: `%Browser%`
- URL to go to: `https://api.contoso.example/v1/invoices`
- Wait for page to load: `True`
- Timeout for webpage to load: `1`
- If a pop-up dialog appears: `(set in designer)`
- Dialog button to press: `INV-1042`
Produces:
- `%`NewBrowser`%` (Web browser instance)
```

**Analogy.** One tool in that kit: a clerk using Chrome at a desk: open, wait, type, copy, close.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.

### Extract data from web page

- **Id:** `webautomation/extract-data-from-web-page`
- **Kind:** native-action
- **Purpose:** Extracts data from web page.

**Use case.** In a web portal with no stable API, drop **Extract data from web page** on the canvas. Extracts data from web page.

**Demonstration.**

```text
**Extract data from web page**
- Web browser instance: `%Browser%`
- UI element: `UI element: Submit button`
- Extraction parameters: `%InvoiceTable%`
- Max web pages to process: `1`
- Send physical click for next page: `True`
- Page CSS selector: `INV-1042`
- Extraction mode: `%Files%`
- Use paging: `True`
- … 4 more parameter(s) in the action modal
Produces:
- `%`ExcelInstance`%` (Excel instance)
- `%`DataFromWebPage`%` (Datatable)
```

**Analogy.** One tool in that kit: a clerk using Chrome at a desk: open, wait, type, copy, close.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.

### Focus text field on web page

- **Id:** `webautomation/focus-text-field-on-web-page`
- **Kind:** native-action
- **Purpose:** Gives focus to text field on web page.

**Use case.** In a web portal with no stable API, drop **Focus text field on web page** on the canvas. Gives focus to text field on web page.

**Demonstration.**

```text
**Focus text field on web page**
- Web browser instance: `%Browser%`
- UI element: `UI element: Submit button`
- Wait for page to load: `True`
- Timeout for webpage to load: `1`
- If a pop-up dialog appears: `(set in designer)`
- Dialog button to press: `INV-1042`
```

**Analogy.** One tool in that kit: a clerk using Chrome at a desk: open, wait, type, copy, close.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.

### Get details of element on web page

- **Id:** `webautomation/get-details-of-element-on-web-page`
- **Kind:** native-action
- **Purpose:** Reads details of element on web page into a flow variable.

**Use case.** In a web portal with no stable API, drop **Get details of element on web page** on the canvas. Reads details of element on web page into a flow variable.

**Demonstration.**

```text
**Get details of element on web page**
- Web browser instance: `%Browser%`
- UI element: `UI element: Submit button`
- Attribute name: `INV-1042`
Produces:
- `%`AttributeValue`%` (Text value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.

### Get details of web page

- **Id:** `webautomation/get-details-of-web-page`
- **Kind:** native-action
- **Purpose:** Reads details of web page into a flow variable.

**Use case.** In a web portal with no stable API, drop **Get details of web page** on the canvas. Reads details of web page into a flow variable.

**Demonstration.**

```text
**Get details of web page**
- Web browser instance: `%Browser%`
- Get: `%Browser%`
Produces:
- `%`WebPageProperty`%` (Text value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.

### Go to web page

- **Id:** `webautomation/go-to-web-page`
- **Kind:** native-action
- **Purpose:** Navigates to web page.

**Use case.** In a web portal with no stable API, drop **Go to web page** on the canvas. Navigates to web page.

**Demonstration.**

```text
**Go to web page**
- Web browser instance: `%Browser%`
- Navigate: `(set in designer)`
- URL: `https://api.contoso.example/v1/invoices`
- Wait for page to load: `True`
- Timeout for webpage to load: `1`
- If a pop-up dialog appears: `(set in designer)`
- Dialog button to press: `INV-1042`
```

**Analogy.** One tool in that kit: a clerk using Chrome at a desk: open, wait, type, copy, close.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.

### Hover mouse over element on web page

- **Id:** `webautomation/hover-mouse-over-element-on-web-page`
- **Kind:** native-action
- **Purpose:** Hovers mouse over element on web page.

**Use case.** In a web portal with no stable API, drop **Hover mouse over element on web page** on the canvas. Hovers mouse over element on web page.

**Demonstration.**

```text
**Hover mouse over element on web page**
- Web browser instance: `%Browser%`
- UI element: `UI element: Submit button`
- Move mouse to hover: `True`
```

**Analogy.** One tool in that kit: a clerk using Chrome at a desk: open, wait, type, copy, close.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.

### If web page contains

- **Id:** `webautomation/if-web-page-contains`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when web page contains.

**Use case.** In a web portal with no stable API, drop **If web page contains** on the canvas. Opens a conditional branch that runs when web page contains.

**Demonstration.**

```text
**If web page contains**
- Web browser instance: `%Browser%`
- Check if web page: `INV-1042`
- UI element: `UI element: Submit button`
- Text: `INV-1042`
Place the actions that should run inside this block, then End.
```

**Analogy.** Checking a condition on a clipboard before you choose a door.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser. Combine with Else / Else if and End. Put Wait or If file exists before brittle UI/browser steps.

### Launch new Chrome

- **Id:** `webautomation/launch-new-chrome`
- **Kind:** native-action
- **Purpose:** Starts new Chrome and returns an instance later actions can reuse.

**Use case.** Start the browser session that all web actions on this site will reuse.

**Demonstration.**

```text
**Launch new Chrome**
- Launch mode: `(set in designer)`
- Attach to Chrome tab: `(set in designer)`
- Initial URL: `https://api.contoso.example/v1/invoices`
- Tab title: `INV-1042`
- Tab URL: `https://api.contoso.example/v1/invoices`
- Window state: `(set in designer)`
- Target desktop: `UI element: Submit button`
- Browser interaction method: `%Browser%`
- … 9 more parameter(s) in the action modal
Produces:
- `%Browser%` (Web browser instance)
```

**Analogy.** Sitting down at a computer and opening the browser.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser. Keep the produced instance/connection and pass it into every later action in this module.

### Launch new Firefox

- **Id:** `webautomation/launch-new-firefox`
- **Kind:** native-action
- **Purpose:** Starts new Firefox and returns an instance later actions can reuse.

**Use case.** In a web portal with no stable API, drop **Launch new Firefox** on the canvas. Starts new Firefox and returns an instance later actions can reuse.

**Demonstration.**

```text
**Launch new Firefox**
- Launch mode: `(set in designer)`
- Attach to Firefox tab: `(set in designer)`
- Initial URL: `https://api.contoso.example/v1/invoices`
- Tab title: `INV-1042`
- Tab URL: `https://api.contoso.example/v1/invoices`
- Window state: `(set in designer)`
- Target desktop: `UI element: Submit button`
- Browser interaction method: `%Browser%`
- … 9 more parameter(s) in the action modal
Produces:
- `%Browser%` (Web browser instance)
```

**Analogy.** Unlocking the room before you work. Same family as: a clerk using Chrome at a desk: open, wait, type, copy, close.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser. Keep the produced instance/connection and pass it into every later action in this module.

### Launch new Internet Explorer

- **Id:** `webautomation/launch-new-internet-explorer`
- **Kind:** native-action
- **Purpose:** Starts new Internet Explorer and returns an instance later actions can reuse.

**Use case.** In a web portal with no stable API, drop **Launch new Internet Explorer** on the canvas. Starts new Internet Explorer and returns an instance later actions can reuse.

**Demonstration.**

```text
**Launch new Internet Explorer**
- Launch mode: `%Browser%`
- Attach to Internet Explorer tab: `(set in designer)`
- Initial URL: `https://api.contoso.example/v1/invoices`
- Tab title: `INV-1042`
- Tab URL: `https://api.contoso.example/v1/invoices`
- Window state: `(set in designer)`
- Target desktop: `UI element: Submit button`
- Clear cache: `True`
- … 6 more parameter(s) in the action modal
Produces:
- `%`InternetExplorer`%` (Web browser instance)
```

**Analogy.** Unlocking the room before you work. Same family as: a clerk using Chrome at a desk: open, wait, type, copy, close.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser. Keep the produced instance/connection and pass it into every later action in this module.

### Launch new Microsoft Edge

- **Id:** `webautomation/launch-new-microsoft-edge`
- **Kind:** native-action
- **Purpose:** Starts new Microsoft Edge and returns an instance later actions can reuse.

**Use case.** In a web portal with no stable API, drop **Launch new Microsoft Edge** on the canvas. Starts new Microsoft Edge and returns an instance later actions can reuse.

**Demonstration.**

```text
**Launch new Microsoft Edge**
- Launch mode: `(set in designer)`
- Attach to Microsoft Edge tab: `(set in designer)`
- Initial URL: `https://api.contoso.example/v1/invoices`
- Tab title: `INV-1042`
- Tab URL: `https://api.contoso.example/v1/invoices`
- Window state: `(set in designer)`
- Target desktop: `UI element: Submit button`
- Browser interaction method: `%Browser%`
- … 9 more parameter(s) in the action modal
Produces:
- `%Browser%` (Web browser instance)
```

**Analogy.** Unlocking the room before you work. Same family as: a clerk using Chrome at a desk: open, wait, type, copy, close.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser. Keep the produced instance/connection and pass it into every later action in this module.

### Populate text field on web page

- **Id:** `webautomation/populate-text-field-on-web-page`
- **Kind:** native-action
- **Purpose:** Types or fills text field on web page.

**Use case.** In a web portal with no stable API, drop **Populate text field on web page** on the canvas. Types or fills text field on web page.

**Demonstration.**

```text
**Populate text field on web page**
- Web browser instance: `%Browser%`
- UI element: `UI element: Submit button`
- Text: `INV-1042`
- If field isn't empty: `INV-1042`
- Populate text using physical keystrokes: `True`
- Emulate typing: `True`
- Unfocus text box after filling it: `True`
- Wait for page to load: `True`
- … 3 more parameter(s) in the action modal
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.

### Press button on web page

- **Id:** `webautomation/press-button-on-web-page`
- **Kind:** native-action
- **Purpose:** Presses button on web page.

**Use case.** In a web portal with no stable API, drop **Press button on web page** on the canvas. Presses button on web page.

**Demonstration.**

```text
**Press button on web page**
- Web browser instance: `%Browser%`
- UI element: `UI element: Submit button`
- Wait for page to load: `True`
- Timeout for webpage to load: `1`
- If a pop-up dialog appears: `(set in designer)`
- Dialog button to press: `INV-1042`
```

**Analogy.** Pushing the exact button a trained operator would push.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.

### Run JavaScript function on web page

- **Id:** `webautomation/run-javascript-function-on-web-page`
- **Kind:** native-action
- **Purpose:** Runs javaScript function on web page.

**Use case.** In a web portal with no stable API, drop **Run JavaScript function on web page** on the canvas. Runs javaScript function on web page.

**Demonstration.**

```text
**Run JavaScript function on web page**
- Web browser instance: `%Browser%`
- JavaScript function: `INV-1042`
Produces:
- `%`Result`%` (Text value)
```

**Analogy.** One tool in that kit: a clerk using Chrome at a desk: open, wait, type, copy, close.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.

### Select radio button on web page

- **Id:** `webautomation/select-radio-button-on-web-page`
- **Kind:** native-action
- **Purpose:** Selects radio button on web page.

**Use case.** In a web portal with no stable API, drop **Select radio button on web page** on the canvas. Selects radio button on web page.

**Demonstration.**

```text
**Select radio button on web page**
- Web browser instance: `%Browser%`
- UI element: `UI element: Submit button`
- Wait for page to load: `True`
- Timeout for webpage to load: `1`
- If a pop-up dialog appears: `(set in designer)`
- Dialog button to press: `INV-1042`
```

**Analogy.** One tool in that kit: a clerk using Chrome at a desk: open, wait, type, copy, close.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.

### Set check box state on web page

- **Id:** `webautomation/set-check-box-state-on-web-page`
- **Kind:** native-action
- **Purpose:** Writes check box state on web page.

**Use case.** In a web portal with no stable API, drop **Set check box state on web page** on the canvas. Writes check box state on web page.

**Demonstration.**

```text
**Set check box state on web page**
- Web browser instance: `%Browser%`
- UI element: `UI element: Submit button`
- Check box state: `(set in designer)`
- Wait for page to load: `True`
- Timeout for webpage to load: `1`
- If a pop-up dialog appears: `(set in designer)`
- Dialog button to press: `INV-1042`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.

### Set drop-down list value on web page

- **Id:** `webautomation/set-drop-down-list-value-on-web-page`
- **Kind:** native-action
- **Purpose:** Writes drop-down list value on web page.

**Use case.** In a web portal with no stable API, drop **Set drop-down list value on web page** on the canvas. Writes drop-down list value on web page.

**Demonstration.**

```text
**Set drop-down list value on web page**
- Web browser instance: `%Browser%`
- UI element: `UI element: Submit button`
- Operation: `(set in designer)`
- Option names: `%Files%`
- Use regular expressions: `True`
- Option indices: `%Files%`
- Wait for page to load: `True`
- Timeout for webpage load: `1`
- … 2 more parameter(s) in the action modal
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.

### Take screenshot of web page

- **Id:** `webautomation/take-screenshot-of-web-page`
- **Kind:** native-action
- **Purpose:** Captures screenshot of web page.

**Use case.** In a web portal with no stable API, drop **Take screenshot of web page** on the canvas. Captures screenshot of web page.

**Demonstration.**

```text
**Take screenshot of web page**
- Web browser instance: `%Browser%`
- Capture: `(set in designer)`
- UI element: `UI element: Submit button`
- Save mode: `(set in designer)`
- Image file: `C:\RPA\Invoices\INV-1042.pdf`
- File format: `C:\RPA\Invoices\INV-1042.pdf`
```

**Analogy.** One tool in that kit: a clerk using Chrome at a desk: open, wait, type, copy, close.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.

### Wait for web page content

- **Id:** `webautomation/wait-for-web-page-content`
- **Kind:** native-action
- **Purpose:** Pauses the flow until web page content.

**Use case.** In a web portal with no stable API, drop **Wait for web page content** on the canvas. Pauses the flow until web page content.

**Demonstration.**

```text
**Wait for web page content**
- Web browser instance: `%Browser%`
- Wait for web page to: `INV-1042`
- UI element: `UI element: Submit button`
- Text: `INV-1042`
```

**Analogy.** Standing at the microwave until it beeps, so you do not grab a cold plate.

**In combination.** Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.
