# Browser automation

Launch browsers, fill web forms, extract data, and run page JavaScript.

This page documents every **native action** in this group (23 items).

## Actions

### Click download link on web page

- **Inventory id:** `webautomation/click-download-link-on-web-page`
- **Kind:** native-action
- **Purpose:** Clicks download link on web page.
- **Key inputs:** `Web browser instance` (Web browser instance); `UI element` (UI element); `Destination folder` (Folder)
- **Produces:** ``DownloadedFile`` (File)
- **Exceptions:** `Failed to download file.`; `Element with specified CSS selector not found.`; `Failed to click UI element.`; `Failed to save file.`
- **Microsoft Learn:** [Click download link on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#clickdownloadlink)

### Click link on web page

- **Inventory id:** `webautomation/click-link-on-web-page`
- **Kind:** native-action
- **Purpose:** Clicks link on web page.
- **Key inputs:** `Web browser instance` (Web browser instance); `UI element` (UI element); `Click type` (Left clickRight clickDouble clickLeft button downLeft button upRight button downRight button upMiddle click); `Send physical click` (Boolean value); `Wait for page to load` (Boolean value); `Timeout for webpage to load` (Numeric value); `If a pop-up dialog appears` (Close itPress a buttonDo nothing); `Dialog button to press` (Text value; optional)
- **Produces:** None listed
- **Exceptions:** `Element with specified CSS selector not found.`; `Failed to click UI element.`
- **Microsoft Learn:** [Click link on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#clickbase)

### Close web browser

- **Inventory id:** `webautomation/close-web-browser`
- **Kind:** native-action
- **Purpose:** Closes web browser.
- **Key inputs:** `Web browser instance` (Web browser instance)
- **Produces:** None listed
- **Exceptions:** `Failed to close the web browser.`
- **Microsoft Learn:** [Close web browser](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#closewebbrowser)

### Create new tab

- **Inventory id:** `webautomation/create-new-tab`
- **Kind:** native-action
- **Purpose:** Creates new tab.
- **Key inputs:** `Web browser instance` (Web browser instance); `URL to go to` (Text value); `Wait for page to load` (Boolean value); `Timeout for webpage to load` (Numeric value); `If a pop-up dialog appears` (Close itPress a buttonDo nothing); `Dialog button to press` (Text value; optional)
- **Produces:** ``NewBrowser`` (Web browser instance)
- **Exceptions:** `Invalid URL`; `Failed to create a new tab.`
- **Microsoft Learn:** [Create new tab](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#createnewtabbase)

### Extract data from web page

- **Inventory id:** `webautomation/extract-data-from-web-page`
- **Kind:** native-action
- **Purpose:** Extracts data from web page.
- **Key inputs:** `Web browser instance` (Web browser instance); `UI element` (UI element); `Extraction parameters` (Datatable); `Max web pages to process` (Numeric value); `Send physical click for next page` (Boolean value); `Page CSS selector` (Text value); `Extraction mode` (UndefinedSingle valueHandpicked valuesListTableEntire HTML table); `Use paging` (Boolean value); `Get all web pages` (Boolean value); `Process data upon extraction` (Boolean value); `Timeout` (Numeric value; optional); `Store data mode` (VariableExcel spreadsheet)
- **Produces:** ``ExcelInstance`` (Excel instance); ``DataFromWebPage`` (Datatable)
- **Exceptions:** `Failed to extract data.`; `Failed to launch Excel instance.`; `Failed to write values to Excel.`
- **Microsoft Learn:** [Extract data from web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#extractdata)

### Focus text field on web page

- **Inventory id:** `webautomation/focus-text-field-on-web-page`
- **Kind:** native-action
- **Purpose:** Gives focus to text field on web page.
- **Key inputs:** `Web browser instance` (Web browser instance); `UI element` (UI element); `Wait for page to load` (Boolean value); `Timeout for webpage to load` (Numeric value); `If a pop-up dialog appears` (Close itPress a buttonDo nothing); `Dialog button to press` (Text value; optional)
- **Produces:** None listed
- **Exceptions:** `Element with specified CSS selector not found.`; `Failed to set input focus on web page text field.`
- **Microsoft Learn:** [Focus text field on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#focusbase)

### Get details of element on web page

- **Inventory id:** `webautomation/get-details-of-element-on-web-page`
- **Kind:** native-action
- **Purpose:** Reads details of element on web page into a flow variable.
- **Key inputs:** `Web browser instance` (Web browser instance); `UI element` (UI element); `Attribute name` (Text value)
- **Produces:** ``AttributeValue`` (Text value)
- **Exceptions:** `Failed to retrieve attribute of UI element on web page.`
- **Microsoft Learn:** [Get details of element on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#getdetailsofelement)

### Get details of web page

- **Inventory id:** `webautomation/get-details-of-web-page`
- **Kind:** native-action
- **Purpose:** Reads details of web page into a flow variable.
- **Key inputs:** `Web browser instance` (Web browser instance); `Get` (Web page descriptionWeb page meta keywordsWeb page titleWeb page textWeb page sourceWeb browser's current URL address)
- **Produces:** ``WebPageProperty`` (Text value)
- **Exceptions:** `Failed to get details of web page.`
- **Microsoft Learn:** [Get details of web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#getdetailsofwebpage)

### Go to web page

- **Inventory id:** `webautomation/go-to-web-page`
- **Kind:** native-action
- **Purpose:** Navigates to web page.
- **Key inputs:** `Web browser instance` (Web browser instance); `Navigate` (To URLBackForwardReload web page); `URL` (Text value); `Wait for page to load` (Boolean value); `Timeout for webpage to load` (Numeric value); `If a pop-up dialog appears` (Close itPress a buttonDo nothing); `Dialog button to press` (Text value; optional)
- **Produces:** None listed
- **Exceptions:** `Failed to navigate to web page.`; `Invalid URL`
- **Microsoft Learn:** [Go to web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#gotowebpagebase)

### Hover mouse over element on web page

- **Inventory id:** `webautomation/hover-mouse-over-element-on-web-page`
- **Kind:** native-action
- **Purpose:** Hovers mouse over element on web page.
- **Key inputs:** `Web browser instance` (Web browser instance); `UI element` (UI element); `Move mouse to hover` (Boolean value)
- **Produces:** None listed
- **Exceptions:** `Failed to hover over element.`
- **Microsoft Learn:** [Hover mouse over element on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#hoveroverelement)

### If web page contains

- **Inventory id:** `webautomation/if-web-page-contains`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when web page contains.
- **Key inputs:** `Web browser instance` (Web browser instance); `Check if web page` (Contains elementDoesn't contain elementContains textDoesn't contain text); `UI element` (UI element); `Text` (Text value)
- **Produces:** None listed
- **Exceptions:** `Failed to communicate with the browser.`
- **Microsoft Learn:** [If web page contains](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#ifwebpagecontainsaction)

### Launch new Chrome

- **Inventory id:** `webautomation/launch-new-chrome`
- **Kind:** native-action
- **Purpose:** Starts new Chrome and returns an instance later actions can reuse.
- **Key inputs:** `Launch mode` (Launch new InstanceAttach to running instance); `Attach to Chrome tab` (By titleBy URLUse foreground window); `Initial URL` (Text value); `Tab title` (Text value); `Tab URL` (Text value); `Window state` (NormalMaximizedMinimized); `Target desktop` (Local computerAny virtual desktop that is either currently connected or has at least one UI element captured); `Browser interaction method` (Browser extensionWebDriver); `Clear cache` (Boolean value); `Clear cookies` (Boolean value); `Wait for page to load` (Boolean value); `Timeout for webpage to load` (Numeric value); `If a pop-up dialog appears` (Close itPress a buttonDo nothing); `Dialog button to press` (Text value; optional); `Timeout` (Numeric value); `User data folder` (Picture-in-Picture defaultBrowser defaultCustom); `User data folder path` (Folder)
- **Produces:** `Browser` (Web browser instance)
- **Exceptions:** `Failed to launch Chrome`; `Invalid URL`
- **Microsoft Learn:** [Launch new Chrome](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#launchchromebase)

### Launch new Firefox

- **Inventory id:** `webautomation/launch-new-firefox`
- **Kind:** native-action
- **Purpose:** Starts new Firefox and returns an instance later actions can reuse.
- **Key inputs:** `Launch mode` (Launch new Instance Attach to running instance); `Attach to Firefox tab` (By titleBy URLUse foreground window); `Initial URL` (Text value); `Tab title` (Text value); `Tab URL` (Text value); `Window state` (NormalMaximizedMinimized); `Target desktop` (Local computerAny virtual desktop that is either currently connected or has at least one UI element captured); `Browser interaction method` (Browser extensionWebDriver); `Clear cache` (Boolean value); `Clear cookies` (Boolean value); `Wait for page to load` (Boolean value); `Timeout for webpage to load` (Numeric value); `If a pop-up dialog appears` (Close itPress a buttonDo nothing); `Dialog button to press` (Text value; optional); `Timeout` (Numeric value); `User data folder` (Picture-in-Picture defaultBrowser defaultCustom); `User data folder path` (Folder)
- **Produces:** `Browser` (Web browser instance)
- **Exceptions:** `Failed to launch Firefox.`; `Invalid URL`
- **Microsoft Learn:** [Launch new Firefox](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#launchfirefoxbase)

### Launch new Internet Explorer

- **Inventory id:** `webautomation/launch-new-internet-explorer`
- **Kind:** native-action
- **Purpose:** Starts new Internet Explorer and returns an instance later actions can reuse.
- **Key inputs:** `Launch mode` (Launch automation browserLaunch new Internet ExplorerAttach to running Internet Explorer); `Attach to Internet Explorer tab` (By titleBy URLUse foreground window); `Initial URL` (Text value); `Tab title` (Text value); `Tab URL` (Text value); `Window state` (NormalMaximizedMinimized); `Target desktop` (Local computerAny virtual desktop that is either currently connected or has at least one UI element captured); `Clear cache` (Boolean value); `Clear cookies` (Boolean value); `Wait for page to load` (Boolean value); `Timeout for webpage to load` (Numeric value); `If a pop-up dialog appears` (Close it, Press a button, Do nothing); `Dialog button to press` (Text value; optional); `Custom user agent string` (Text value; optional)
- **Produces:** ``InternetExplorer`` (Web browser instance)
- **Exceptions:** `Failed to launch Internet Explorer.`; `Invalid URL`
- **Microsoft Learn:** [Launch new Internet Explorer](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#launchinternetexplorerbase)

### Launch new Microsoft Edge

- **Inventory id:** `webautomation/launch-new-microsoft-edge`
- **Kind:** native-action
- **Purpose:** Starts new Microsoft Edge and returns an instance later actions can reuse.
- **Key inputs:** `Launch mode` (Launch new InstanceAttach to running instance); `Attach to Microsoft Edge tab` (By titleBy URLUse foreground window); `Initial URL` (Text value); `Tab title` (Text value); `Tab URL` (Text value); `Window state` (NormalMaximizedMinimized); `Target desktop` (Local computerAny virtual desktop that is either currently connected or has at least one UI element captured); `Browser interaction method` (Browser extensionWebDriver); `Clear cache` (Boolean value); `Clear cookies` (Boolean value); `Wait for page to load` (Boolean value); `Timeout for webpage to load` (Numeric value); `If a pop-up dialog appears` (Close itPress a buttonDo nothing); `Dialog button to press` (Text value; optional); `Timeout` (Numeric value); `User data folder` (Picture-in-Picture defaultBrowser defaultCustom); `User data folder path` (Folder)
- **Produces:** `Browser` (Web browser instance)
- **Exceptions:** `Failed to launch Microsoft Edge.`; `Invalid URL`
- **Microsoft Learn:** [Launch new Microsoft Edge](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)

### Populate text field on web page

- **Inventory id:** `webautomation/populate-text-field-on-web-page`
- **Kind:** native-action
- **Purpose:** Types or fills text field on web page.
- **Key inputs:** `Web browser instance` (Web browser instance); `UI element` (UI element); `Text` (Direct encrypted inputText value); `If field isn't empty` (Replace textAppend text; optional); `Populate text using physical keystrokes` (Boolean value); `Emulate typing` (Boolean value); `Unfocus text box after filling it` (Boolean value); `Wait for page to load` (Boolean value); `Timeout for webpage to load` (Numeric value); `If a pop-up dialog appears` (Close itPress a buttonDo nothing); `Dialog button to press` (Text value; optional)
- **Produces:** None listed
- **Exceptions:** `Element with specified CSS selector not found.`; `Failed to write on text field.`
- **Microsoft Learn:** [Populate text field on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#populatetextfieldbase)

### Press button on web page

- **Inventory id:** `webautomation/press-button-on-web-page`
- **Kind:** native-action
- **Purpose:** Presses button on web page.
- **Key inputs:** `Web browser instance` (Web browser instance); `UI element` (UI element); `Wait for page to load` (Boolean value); `Timeout for webpage to load` (Numeric value); `If a pop-up dialog appears` (Close itPress a buttonDo nothing); `Dialog button to press` (Text value; optional)
- **Produces:** None listed
- **Exceptions:** `Element with specified CSS selector not found.`; `Failed to click on web page button.`
- **Microsoft Learn:** [Press button on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#pressbuttonbase)

### Run JavaScript function on web page

- **Inventory id:** `webautomation/run-javascript-function-on-web-page`
- **Kind:** native-action
- **Purpose:** Runs javaScript function on web page.
- **Key inputs:** `Web browser instance` (Web browser instance); `JavaScript function` (Text value; optional)
- **Produces:** ``Result`` (Text value)
- **Exceptions:** `Failed to run :::no-loc text="JavaScript":::.`
- **Microsoft Learn:** [Run JavaScript function on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#executejavascript)

### Select radio button on web page

- **Inventory id:** `webautomation/select-radio-button-on-web-page`
- **Kind:** native-action
- **Purpose:** Selects radio button on web page.
- **Key inputs:** `Web browser instance` (Web browser instance); `UI element` (UI element); `Wait for page to load` (Boolean value); `Timeout for webpage to load` (Numeric value); `If a pop-up dialog appears` (Close itPress a buttonDo nothing); `Dialog button to press` (Text value; optional)
- **Produces:** None listed
- **Exceptions:** `Element with specified CSS selector not found`; `Failed to select radio button`
- **Microsoft Learn:** [Select radio button on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#selectradiobuttonbase)

### Set check box state on web page

- **Inventory id:** `webautomation/set-check-box-state-on-web-page`
- **Kind:** native-action
- **Purpose:** Writes check box state on web page.
- **Key inputs:** `Web browser instance` (Web browser instance); `UI element` (UI element); `Check box state` (CheckedUnchecked); `Wait for page to load` (Boolean value); `Timeout for webpage to load` (Numeric value); `If a pop-up dialog appears` (Close itPress a buttonDo nothing); `Dialog button to press` (Text value; optional)
- **Produces:** None listed
- **Exceptions:** `Element with specified CSS selector not found.`; `Failed to set the state of the checkbox.`
- **Microsoft Learn:** [Set check box state on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#setcheckboxstatebase)

### Set drop-down list value on web page

- **Inventory id:** `webautomation/set-drop-down-list-value-on-web-page`
- **Kind:** native-action
- **Purpose:** Writes drop-down list value on web page.
- **Key inputs:** `Web browser instance` (Web browser instance); `UI element` (UI element); `Operation` (Clear all optionsSelect options by nameSelect options by index); `Option names` (List of Text values); `Use regular expressions` (Boolean value); `Option indices` (List of Numeric values); `Wait for page to load` (Boolean value); `Timeout for webpage load` (Numeric value); `If a pop-up dialog appears` (Close itPress a buttonDo nothing); `Dialog button to press` (Text value; optional)
- **Produces:** None listed
- **Exceptions:** `Element with specified CSS selector not found.`; `Failed to set the selected option.`
- **Microsoft Learn:** [Set drop-down list value on web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#setdropdownlistvaluebase)

### Take screenshot of web page

- **Inventory id:** `webautomation/take-screenshot-of-web-page`
- **Kind:** native-action
- **Purpose:** Captures screenshot of web page.
- **Key inputs:** `Web browser instance` (Web browser instance); `Capture` (Entire web pageSpecific element); `UI element` (UI element); `Save mode` (ClipboardFile); `Image file` (File); `File format` (BMPEMFEXIFGIFJPGPNGTIFFWMF)
- **Produces:** None listed
- **Exceptions:** `Element with specified CSS selector not found.`; `Failed to save file.`; `Failed to save in the clipboard.`; `Failed to take screenshot.`
- **Microsoft Learn:** [Take screenshot of web page](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#takescreenshotbase)

### Wait for web page content

- **Inventory id:** `webautomation/wait-for-web-page-content`
- **Kind:** native-action
- **Purpose:** Pauses the flow until web page content.
- **Key inputs:** `Web browser instance` (Web browser instance); `Wait for web page to` (Contain elementNot contain elementContain textNot contain text); `UI element` (UI element); `Text` (Text value)
- **Produces:** None listed
- **Exceptions:** `Wait for web page content failed.`
- **Microsoft Learn:** [Wait for web page content](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation#waitforwebpagecontentaction)
