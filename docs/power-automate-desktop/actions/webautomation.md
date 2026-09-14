# Browser automation

Launch browsers and interact with web pages and web elements.

- Actions in this module: **23**
- Official docs: [Browser automation actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)

## Actions

### Extract data from web page

Extract data from specific parts of a web page as single values, lists, rows, or tables.

Designer name: **Extract data from web page**. Official reference: [Browser automation / Extract data from web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#extractdata).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| UI element | Required | UI element | — |
| Extraction parameters | Required | Datatable | — |
| Max web pages to process | Required | Numeric value | — |
| Send physical click for next page | Choice | Boolean value | False |
| Page CSS selector | Required | Text value | — |
| Extraction mode | Choice | UndefinedSingle valueHandpicked valuesListTableEntire HTML table | Single value |
| Use paging | Choice | Boolean value | False |
| Get all web pages | Choice | Boolean value | False |
| Process data upon extraction | Choice | Boolean value | False |
| Timeout | Optional | Numeric value | 60 |
| Store data mode | Choice | VariableExcel spreadsheet | Variable |

**Outputs**

| Variable | Type |
|---|---|
| ExcelInstance | Excel instance |
| DataFromWebPage | Datatable |

**On error:** `Failed to extract data.`, `Failed to launch Excel instance.`, `Failed to write values to Excel.`.

---

### Get details of web page

Reads a property of a web page, such as its title or its source text.

Designer name: **Get details of web page**. Official reference: [Browser automation / Get details of web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#getdetailsofwebpage).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| Get | Choice | Web page descriptionWeb page meta keywordsWeb page titleWeb page textWeb page sourceWeb browser's current URL address | Web page description |

**Outputs**

| Variable | Type |
|---|---|
| WebPageProperty | Text value |

**On error:** `Failed to get details of web page.`.

---

### Get details of element on web page

Reads the value of an element's attribute on a web page.

Designer name: **Get details of element on web page**. Official reference: [Browser automation / Get details of element on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#getdetailsofelement).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| UI element | Required | UI element | — |
| Attribute name | Required | Text value | Own Text |

**Outputs**

| Variable | Type |
|---|---|
| AttributeValue | Text value |

**On error:** `Failed to retrieve attribute of UI element on web page.`.

---

### Take screenshot of web page

Takes a screenshot of the web page (or an element of the web page) currently displayed in the browser and saves the image to a file or the clipboard.

Designer name: **Take screenshot of web page**. Official reference: [Browser automation / Take screenshot of web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#takescreenshotbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| Capture | Choice | Entire web pageSpecific element | Entire web page |
| UI element | Required | UI element | — |
| Save mode | Choice | ClipboardFile | Clipboard |
| Image file | Required | File | — |
| File format | Choice | BMPEMFEXIFGIFJPGPNGTIFFWMF | BMP |

Produces no variables.

**On error:** `Element with specified CSS selector not found.`, `Failed to save file.`, `Failed to save in the clipboard.`, `Failed to take screenshot.`.

---

### Focus text field on web page

Writes the focus on an input element of a web page and scroll it into view.

Designer name: **Focus text field on web page**. Official reference: [Browser automation / Focus text field on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#focusbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| UI element | Required | UI element | — |
| Wait for page to load | Choice | Boolean value | True |
| Timeout for webpage to load | Required | Numeric value | 60 |
| If a pop-up dialog appears | Choice | Close itPress a buttonDo nothing | Do nothing |
| Dialog button to press | Optional | Text value | OK |

Produces no variables.

**On error:** `Element with specified CSS selector not found.`, `Failed to set input focus on web page text field.`.

---

### Populate text field on web page

Fill a text field in a web page with the specified text.

Designer name: **Populate text field on web page**. Official reference: [Browser automation / Populate text field on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#populatetextfieldbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| UI element | Required | UI element | — |
| Text | Required | Direct encrypted inputText value | — |
| If field isn't empty | Optional | Replace textAppend text | Replace text |
| Populate text using physical keystrokes | Choice | Boolean value | False |
| Emulate typing | Choice | Boolean value | True |
| Unfocus text box after filling it | Choice | Boolean value | False |
| Wait for page to load | Choice | Boolean value | True |
| Timeout for webpage to load | Required | Numeric value | 60 |
| If a pop-up dialog appears | Choice | Close itPress a buttonDo nothing | Do nothing |
| Dialog button to press | Optional | Text value | OK |

Produces no variables.

**On error:** `Element with specified CSS selector not found.`, `Failed to write on text field.`.

---

### Set check box state on web page

Check or uncheck a check box in a web form.

Designer name: **Set check box state on web page**. Official reference: [Browser automation / Set check box state on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#setcheckboxstatebase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| UI element | Required | UI element | — |
| Check box state | Choice | CheckedUnchecked | Checked |
| Wait for page to load | Choice | Boolean value | True |
| Timeout for webpage to load | Required | Numeric value | 60 |
| If a pop-up dialog appears | Choice | Close itPress a buttonDo nothing | Do nothing |
| Dialog button to press | Optional | Text value | OK |

Produces no variables.

**On error:** `Element with specified CSS selector not found.`, `Failed to set the state of the checkbox.`.

---

### Select radio button on web page

Select a radio button on the web page.

Designer name: **Select radio button on web page**. Official reference: [Browser automation / Select radio button on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#selectradiobuttonbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| UI element | Required | UI element | — |
| Wait for page to load | Choice | Boolean value | True |
| Timeout for webpage to load | Required | Numeric value | 60 |
| If a pop-up dialog appears | Choice | Close itPress a buttonDo nothing | Do nothing |
| Dialog button to press | Optional | Text value | OK |

Produces no variables.

**On error:** `Element with specified CSS selector not found`, `Failed to select radio button`.

---

### Set drop-down list value on web page

Writes or clear the selected options for a drop-down list in a web form.

Designer name: **Set drop-down list value on web page**. Official reference: [Browser automation / Set drop-down list value on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#setdropdownlistvaluebase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| UI element | Required | UI element | — |
| Operation | Choice | Clear all optionsSelect options by nameSelect options by index | Clear all options |
| Option names | Required | List of Text values | — |
| Use regular expressions | Choice | Boolean value | False |
| Option indices | Required | List of Numeric values | — |
| Wait for page to load | Choice | Boolean value | True |
| Timeout for webpage load | Required | Numeric value | 60 |
| If a pop-up dialog appears | Choice | Close itPress a buttonDo nothing | Do nothing |
| Dialog button to press | Optional | Text value | OK |

Produces no variables.

**On error:** `Element with specified CSS selector not found.`, `Failed to set the selected option.`.

---

### Press button on web page

Press a web page button.

Designer name: **Press button on web page**. Official reference: [Browser automation / Press button on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#pressbuttonbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| UI element | Required | UI element | — |
| Wait for page to load | Choice | Boolean value | True |
| Timeout for webpage to load | Required | Numeric value | 60 |
| If a pop-up dialog appears | Choice | Close itPress a buttonDo nothing | Do nothing |
| Dialog button to press | Optional | Text value | OK |

Produces no variables.

**On error:** `Element with specified CSS selector not found.`, `Failed to click on web page button.`.

---

### If web page contains

Mark the beginning of a conditional block of actions, depending on whether a specific piece of text or element exists in a web page.

Designer name: **If web page contains**. Official reference: [Browser automation / If web page contains](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#ifwebpagecontainsaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| Check if web page | Choice | Contains elementDoesn't contain elementContains textDoesn't contain text | Contains element |
| UI element | Required | UI element | — |
| Text | Required | Text value | — |

Produces no variables.

**On error:** `Failed to communicate with the browser.`.

---

### Wait for web page content

Suspend the flow until a specific piece of text or web page element appears or disappears from a web page.

Designer name: **Wait for web page content**. Official reference: [Browser automation / Wait for web page content](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#waitforwebpagecontentaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| Wait for web page to | Choice | Contain elementNot contain elementContain textNot contain text | Contain element |
| UI element | Required | UI element | — |
| Text | Required | Text value | — |

Produces no variables.

**On error:** `Wait for web page content failed.`.

---

### Launch new Internet Explorer

Launch a new instance or attach to a running instance of Internet Explorer for automating websites and web applications.

Designer name: **Launch new Internet Explorer**. Official reference: [Browser automation / Launch new Internet Explorer](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#launchinternetexplorerbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Launch mode | Choice | Launch automation browserLaunch new Internet ExplorerAttach to running Internet Explorer | Launch automation browser |
| Attach to Internet Explorer tab | Choice | By titleBy URLUse foreground window | By title |
| Initial URL | Required | Text value | — |
| Tab title | Required | Text value | — |
| Tab URL | Required | Text value | — |
| Window state | Choice | NormalMaximizedMinimized | Normal |
| Target desktop | Choice | Local computerAny virtual desktop that is either currently connected or has at least one UI element captured | Local computer |
| Clear cache | Choice | Boolean value | False |
| Clear cookies | Choice | Boolean value | False |
| Wait for page to load | Choice | Boolean value | True |
| Timeout for webpage to load | Required | Numeric value | 60 |
| If a pop-up dialog appears | Choice | Close it, Press a button, Do nothing | Do nothing |
| Dialog button to press | Optional | Text value | OK |
| Custom user agent string | Optional | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| InternetExplorer | Web browser instance |

**On error:** `Failed to launch Internet Explorer.`, `Invalid URL`.

---

### Launch new Firefox

Launch a new instance or attach to a running instance of Firefox for automating websites and web applications.

Designer name: **Launch new Firefox**. Official reference: [Browser automation / Launch new Firefox](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#launchfirefoxbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Launch mode | Choice | Launch new Instance Attach to running instance | Launch new Instance |
| Attach to Firefox tab | Choice | By titleBy URLUse foreground window | By title |
| Initial URL | Required | Text value | — |
| Tab title | Required | Text value | — |
| Tab URL | Required | Text value | — |
| Window state | Choice | NormalMaximizedMinimized | Normal |
| Target desktop | Choice | Local computerAny virtual desktop that is either currently connected or has at least one UI element captured | Local computer |
| Browser interaction method | Choice | Browser extensionWebDriver | Browser extension |
| Clear cache | Choice | Boolean value | False |
| Clear cookies | Choice | Boolean value | False |
| Wait for page to load | Choice | Boolean value | True |
| Timeout for webpage to load | Required | Numeric value | 60 |
| If a pop-up dialog appears | Choice | Close itPress a buttonDo nothing | Do nothing |
| Dialog button to press | Optional | Text value | OK |
| Timeout | Required | Numeric value | 60 |
| User data folder | Choice | Picture-in-Picture defaultBrowser defaultCustom | Picture-in-Picture default |
| User data folder path | Required | Folder | — |

**Outputs**

| Variable | Type |
|---|---|
| Browser | Web browser instance |

**On error:** `Failed to launch Firefox.`, `Invalid URL`.

---

### Launch new Chrome

Launch a new instance or attach to a running instance of Chrome for automating websites and web applications.

Designer name: **Launch new Chrome**. Official reference: [Browser automation / Launch new Chrome](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#launchchromebase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Launch mode | Choice | Launch new InstanceAttach to running instance | Launch new Instance |
| Attach to Chrome tab | Choice | By titleBy URLUse foreground window | By title |
| Initial URL | Required | Text value | — |
| Tab title | Required | Text value | — |
| Tab URL | Required | Text value | — |
| Window state | Choice | NormalMaximizedMinimized | Normal |
| Target desktop | Choice | Local computerAny virtual desktop that is either currently connected or has at least one UI element captured | Local computer |
| Browser interaction method | Choice | Browser extensionWebDriver | Browser extension |
| Clear cache | Choice | Boolean value | False |
| Clear cookies | Choice | Boolean value | False |
| Wait for page to load | Choice | Boolean value | True |
| Timeout for webpage to load | Required | Numeric value | 60 |
| If a pop-up dialog appears | Choice | Close itPress a buttonDo nothing | Do nothing |
| Dialog button to press | Optional | Text value | OK |
| Timeout | Required | Numeric value | 60 |
| User data folder | Choice | Picture-in-Picture defaultBrowser defaultCustom | Picture-in-Picture default |
| User data folder path | Required | Folder | — |

**Outputs**

| Variable | Type |
|---|---|
| Browser | Web browser instance |

**On error:** `Failed to launch Chrome`, `Invalid URL`.

---

### Launch new Microsoft Edge

Launch a new instance or attach to a running instance of Microsoft Edge for automating websites and web applications.

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Launch mode | Choice | Launch new InstanceAttach to running instance | Launch new Instance |
| Attach to Microsoft Edge tab | Choice | By titleBy URLUse foreground window | By title |
| Initial URL | Required | Text value | — |
| Tab title | Required | Text value | — |
| Tab URL | Required | Text value | — |
| Window state | Choice | NormalMaximizedMinimized | Normal |
| Target desktop | Choice | Local computerAny virtual desktop that is either currently connected or has at least one UI element captured | Local computer |
| Browser interaction method | Choice | Browser extensionWebDriver | Browser extension |
| Clear cache | Choice | Boolean value | False |
| Clear cookies | Choice | Boolean value | False |
| Wait for page to load | Choice | Boolean value | True |
| Timeout for webpage to load | Required | Numeric value | 60 |
| If a pop-up dialog appears | Choice | Close itPress a buttonDo nothing | Do nothing |
| Dialog button to press | Optional | Text value | OK |
| Timeout | Required | Numeric value | 60 |
| User data folder | Choice | Picture-in-Picture defaultBrowser defaultCustom | Picture-in-Picture default |
| User data folder path | Required | Folder | — |

**Outputs**

| Variable | Type |
|---|---|
| Browser | Web browser instance |

**On error:** `Failed to launch Microsoft Edge.`, `Invalid URL`.

---

### Create new tab

Create a new tab and go to the given URL (supported in Microsoft Edge, Chrome, and Firefox).

Designer name: **Create new tab**. Official reference: [Browser automation / Create new tab](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#createnewtabbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| URL to go to | Required | Text value | — |
| Wait for page to load | Choice | Boolean value | True |
| Timeout for webpage to load | Required | Numeric value | 60 |
| If a pop-up dialog appears | Choice | Close itPress a buttonDo nothing | Do nothing |
| Dialog button to press | Optional | Text value | OK |

**Outputs**

| Variable | Type |
|---|---|
| NewBrowser | Web browser instance |

**On error:** `Invalid URL`, `Failed to create a new tab.`.

---

### Go to web page

Navigate the web browser to a new page.

Designer name: **Go to web page**. Official reference: [Browser automation / Go to web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#gotowebpagebase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| Navigate | Choice | To URLBackForwardReload web page | To URL |
| URL | Required | Text value | — |
| Wait for page to load | Choice | Boolean value | True |
| Timeout for webpage to load | Required | Numeric value | 60 |
| If a pop-up dialog appears | Choice | Close itPress a buttonDo nothing | Do nothing |
| Dialog button to press | Optional | Text value | OK |

Produces no variables.

**On error:** `Failed to navigate to web page.`, `Invalid URL`.

---

### Click link on web page

Click on a link or any other element of a web page.

Designer name: **Click link on web page**. Official reference: [Browser automation / Click link on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#clickbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| UI element | Required | UI element | — |
| Click type | Choice | Left clickRight clickDouble clickLeft button downLeft button upRight button downRight button upMiddle click | Left click |
| Send physical click | Choice | Boolean value | False |
| Wait for page to load | Choice | Boolean value | True |
| Timeout for webpage to load | Required | Numeric value | 60 |
| If a pop-up dialog appears | Choice | Close itPress a buttonDo nothing | Do nothing |
| Dialog button to press | Optional | Text value | OK |

Produces no variables.

**On error:** `Element with specified CSS selector not found.`, `Failed to click UI element.`.

---

### Click download link on web page

Select a link in a web page that results in downloading a file.

Designer name: **Click download link on web page**. Official reference: [Browser automation / Click download link on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#clickdownloadlink).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| UI element | Required | UI element | — |
| Destination folder | Required | Folder | — |

**Outputs**

| Variable | Type |
|---|---|
| DownloadedFile | File |

**On error:** `Failed to download file.`, `Element with specified CSS selector not found.`, `Failed to click UI element.`, `Failed to save file.`.

---

### Run JavaScript function on web page

Run a JavaScript function on the web page and get the returned result.

Designer name: **Run JavaScript function on web page**. Official reference: [Browser automation / Run JavaScript function on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#executejavascript).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| JavaScript function | Optional | Text value | function ExecuteScript() { /*your code here, return something (optionally); */ } |

**Outputs**

| Variable | Type |
|---|---|
| Result | Text value |

**On error:** `Failed to run :::no-loc text="JavaScript":::.`.

---

### Hover mouse over element on web page

Hover the mouse over an element of a web page.

Designer name: **Hover mouse over element on web page**. Official reference: [Browser automation / Hover mouse over element on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#hoveroverelement).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |
| UI element | Required | UI element | — |
| Move mouse to hover | Required | Boolean value | False |

Produces no variables.

**On error:** `Failed to hover over element.`.

---

### Close web browser

Closes a web browser window.

Designer name: **Close web browser**. Official reference: [Browser automation / Close web browser](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#closewebbrowser).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Web browser instance | Required | Web browser instance | — |

Produces no variables.

**On error:** `Failed to close the web browser.`.

---
