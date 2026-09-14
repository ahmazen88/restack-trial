# Power Automate Desktop inventory

Step 1 of this documentation set: every **usable item** in Power Automate for desktop (PAD), grouped the way the designer presents them.

- Built-in actions with a fixed designer name: **444**
- Action modules / pane groups: **52**
- Plus expression functions, data-type properties, and designer assets listed in [usable items](usable-items.md).

Source of action names: [Microsoft Learn actions reference](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference).

## How to read this list

| Kind | Where you use it | Count in this catalog |
|---|---|---|
| Actions | Actions pane, search box, recorder | 444 named actions |
| Classic expression functions | `%Function(...)%` in non-Power Fx flows | 8 text tests + operators |
| Power Fx functions | `=` formula bar when Power Fx is enabled | 130 functions |
| Data-type properties | `%Variable.Property%` | 20+ types |
| Designer assets | Variables, UI elements, images, credentials, subflows | see [usable items](usable-items.md) |

## Action modules

### Access (5)

Open, query, and close local Microsoft Access databases.

Docs: [Access](actions/access.md)

- Launch Access
- Read Access table
- Run Access query
- Run Access macro
- Close Access

### Active Directory (15)

Connect to Active Directory and manage users, groups, and objects.

Docs: [Active Directory](actions/activedirectory.md)

- Create group
- Get group info
- Get group members
- Modify group
- Create object
- Delete object
- Move object
- Rename object
- Create user
- Get user info
- Modify user
- Unlock user
- Update user info
- Connect to server
- Close connection

### AI Builder (preview) (1)

Call AI Builder models from a desktop flow.

Docs: [AI Builder (preview)](actions/aibuilder.md)

- Create text with GPT (preview)

### AWS (15)

Manage Amazon EC2, S3, and related AWS resources from a desktop flow.

Docs: [AWS](actions/aws.md)

- Start EC2 instance
- Stop EC2 instance
- Reboot EC2 instance
- Get available EC2 instances
- Describe instances
- Create snapshot
- Describe snapshots
- Delete snapshot
- Create volume
- Attach volume
- Detach volume
- Describe volumes
- Delete volume
- Create EC2 session
- End EC2 session

### Azure (20)

Manage Azure resource groups, disks, blobs, and related cloud resources.

Docs: [Azure](actions/azure.md)

- Get resource groups
- Create resource group
- Delete resource group
- Get disks
- Attach disk
- Detach disk
- Create managed disk
- Delete disk
- Get snapshots
- Create snapshot
- Delete snapshot
- Get virtual machines
- Describe virtual machine
- Start virtual machine
- Stop virtual machine
- Shut down virtual machine
- Restart virtual machine
- Create session
- Get subscriptions
- End session

### Browser automation (23)

Launch browsers and interact with web pages and web elements.

Docs: [Browser automation](actions/webautomation.md)

- Extract data from web page
- Get details of web page
- Get details of element on web page
- Take screenshot of web page
- Focus text field on web page
- Populate text field on web page
- Set check box state on web page
- Select radio button on web page
- Set drop-down list value on web page
- Press button on web page
- If web page contains
- Wait for web page content
- Launch new Internet Explorer
- Launch new Firefox
- Launch new Chrome
- Launch new Microsoft Edge
- Create new tab
- Go to web page
- Click link on web page
- Click download link on web page
- Run JavaScript function on web page
- Hover mouse over element on web page
- Close web browser

### Clipboard (3)

Read, write, and clear Windows clipboard text.

Docs: [Clipboard](actions/clipboard.md)

- Get clipboard text
- Set clipboard Text
- Clear clipboard contents

### Cloud connectors (0)

Run Power Automate cloud connector operations inside a desktop flow.

Docs: [Cloud connectors](actions/cloudconnectors.md)

Dynamic catalog (connector operations, custom modules, or environment-specific items).

### CMD session (5)

Open a command prompt session and send commands interactively.

Docs: [CMD session](actions/cmd.md)

- Open CMD session
- Read from CMD session
- Write to CMD session
- Wait for text on CMD session
- Close CMD session

### Compression (2)

Zip and unzip files and folders.

Docs: [Compression](actions/compression.md)

- ZIP files
- Unzip files

### Conditionals (6)

Branch the flow with If, Else if, Else, Switch, and Case.

Docs: [Conditionals](actions/conditionals.md)

- Case
- Default case
- Else
- Else if
- If
- Switch

### Cryptography (8)

Hash, encrypt, decrypt, and encode values.

Docs: [Cryptography](actions/cryptography.md)

- Encrypt text with AES
- Decrypt text with AES
- Encrypt from file with AES
- Decrypt to file with AES
- Hash text
- Hash from file
- Hash text with key
- Hash from file with key

### Custom actions (0)

Use organization-uploaded custom action modules in a desktop flow.

Docs: [Custom actions](actions/custommodule.md)

Dynamic catalog (connector operations, custom modules, or environment-specific items).

### CyberArk (1)

Retrieve secrets from CyberArk vaults at runtime.

Docs: [CyberArk](actions/cyberark.md)

- Get password from CyberArk

### Database (2)

Open SQL connections and run statements against databases.

Docs: [Database](actions/database.md)

- Open SQL connection
- Close SQL connection

### Date time (3)

Read the current datetime and add or subtract time units.

Docs: [Date time](actions/datetime.md)

- Add to datetime
- Subtract dates
- Get current date and time

### Email (3)

Send and retrieve mail through IMAP, POP3, and SMTP.

Docs: [Email](actions/email.md)

- Retrieve email messages
- Process email messages
- Send email

### Excel (41)

Launch Excel, read and write cells, and manage worksheets and macros.

Docs: [Excel](actions/excel.md)

- Resize columns/rows in Excel worksheet
- Run Excel macro
- Get active Excel worksheet
- Get all Excel worksheets
- Delete Excel worksheet
- Rename Excel worksheet
- Copy Excel worksheet
- Activate cell in Excel worksheet
- Select cells in Excel worksheet
- Get selected cell range from Excel worksheet
- Copy cells from Excel worksheet
- Paste cells to Excel worksheet
- Delete from Excel worksheet
- Insert row to Excel worksheet
- Delete row from Excel worksheet
- Insert column to Excel worksheet
- Delete column from Excel worksheet
- Find and replace cells in Excel worksheet
- Get first free row on column from Excel worksheet
- Read formula from Excel
- Get table range from Excel worksheet
- Auto fill cells in Excel worksheet
- Append cells in Excel worksheet
- Lookup range in Excel worksheet
- Set color of cells in Excel worksheet
- Launch Excel
- Attach to running Excel
- Read from Excel worksheet
- Get active cell on Excel worksheet
- Save Excel
- Write to Excel worksheet
- Close Excel
- Set active Excel worksheet
- Add new worksheet
- Get first free column/row from Excel worksheet
- Get column name on Excel worksheet
- Clear cells in Excel worksheet
- Sort cells in Excel worksheet
- Filter cells in Excel worksheet
- Clear filters in Excel worksheet
- Get empty cell

### Exchange Server (4)

Connect to Exchange and process mailbox messages.

Docs: [Exchange Server](actions/exchange.md)

- Connect to Exchange server
- Retrieve Exchange email messages
- Send Exchange email message
- Process Exchange email messages

### File (16)

Create, copy, move, read, write, and convert files.

Docs: [File](actions/file.md)

- If file exists
- Wait for file
- Copy file(s)
- Move file(s)
- Delete file(s)
- Rename file(s)
- Read text from file
- Write text to file
- Read from CSV file
- Write to CSV file
- Get file path part
- Get temporary file
- Convert file to Base64
- Convert Base64 to file
- Convert file to binary data
- Convert binary data to file

### Flow control (14)

Control execution order, errors, subflows, waits, and regions.

Docs: [Flow control](actions/flowcontrol.md)

- If safe stop requested
- Comment
- End
- End region
- Exit subflow
- Get last error
- Go to
- Label
- Throw custom error
- On block error
- Region
- Run subflow
- Stop flow
- Wait

### Folder (10)

Create, copy, move, list, and delete folders.

Docs: [Folder](actions/folder.md)

- If folder exists
- Get files in folder
- Get subfolders in folder
- Create folder
- Delete folder
- Empty folder
- Copy folder
- Move folder
- Rename folder
- Get special folder

### FTP (15)

Connect to FTP/FTPS servers and transfer files.

Docs: [FTP](actions/ftp.md)

- Open FTP connection
- List FTP directory
- Open secure FTP connection
- Close connection
- Change working directory
- Download file(s) from FTP
- Download folder(s) from FTP
- Upload File(s) to FTP
- Upload folder(s) to FTP
- Delete FTP file
- Rename FTP File
- Create FTP directory
- Delete FTP directory
- Invoke FTP command
- Synchronize directories

### Google Cognitive (9)

Call Google Cloud Vision and Natural Language APIs.

Docs: [Google Cognitive](actions/googlecognitive.md)

- Analyze sentiment
- Analyze entities
- Analyze syntax
- Label detection
- Landmark detection
- Text Detection
- Logo detection
- Image properties detection
- Safe search detection

### HTTP (3)

Call REST and SOAP endpoints and download files over HTTP.

Docs: [HTTP](actions/web.md)

- Download from web
- Invoke SOAP web service
- Invoke web service

### IBM Cognitive (5)

Call IBM Watson language and visual recognition APIs.

Docs: [IBM Cognitive](actions/ibmcognitive.md)

- Convert document
- Translate
- Identify language
- Analyze tone
- Classify Image

### Logging (1)

Write custom log entries during a desktop flow run.

Docs: [Logging](actions/logging.md)

- Log message

### Loops (5)

Repeat actions with Loop, Loop condition, and For each.

Docs: [Loops](actions/loops.md)

- Exit loop
- For each
- Loop
- Loop condition
- Next loop

### Message boxes (7)

Show dialogs, input boxes, and custom forms to the user.

Docs: [Message boxes](actions/display.md)

- Display message
- Display input dialog
- Display select date dialog
- Display select from list dialog
- Display select  file dialog
- Display select folder dialog
- Display custom form

### Microsoft Cognitive (8)

Call Azure Cognitive Services for text, vision, and language.

Docs: [Microsoft Cognitive](actions/microsoftcognitive.md)

- Spell check
- Analyze image
- Describe image
- OCR
- Tag image
- Detect language
- Key phrases
- Sentiment

### Mouse and keyboard (12)

Move the mouse, send clicks and keystrokes, and wait for input.

Docs: [Mouse and keyboard](actions/mouseandkeyboard.md)

- Block Input
- Get mouse position
- Move mouse
- Move mouse to image
- Move mouse to text on screen (OCR)
- Send mouse click
- Send keys
- Press/release key
- Set key state
- Wait for mouse
- Get keyboard identifier
- Wait for shortcut key

### OCR (2)

Extract or wait for on-screen text with Windows or Tesseract OCR.

Docs: [OCR](actions/ocr.md)

- Wait for text on screen (OCR)
- Extract text with OCR

### Office 365 Outlook (0)

Use the Office 365 Outlook cloud connector from a desktop flow.

Docs: [Office 365 Outlook](actions/office365outlook.md)

Dynamic catalog (connector operations, custom modules, or environment-specific items).

### Outlook (7)

Automate the local Outlook desktop client.

Docs: [Outlook](actions/outlook.md)

- Launch Outlook
- Retrieve email messages from Outlook
- Send email through Outlook
- Process email messages in Outlook
- Save Outlook email messages
- Respond to Outlook mail message
- Close Outlook

### PDF (5)

Extract text, tables, and images from PDFs and merge or split files.

Docs: [PDF](actions/pdf.md)

- Extract text from PDF
- Extract tables from PDF
- Extract images from PDF
- Extract PDF file pages to new PDF file
- Merge PDF files

### Power Automate environment (1)

Read Dataverse / Power Platform environment variables.

Docs: [Power Automate environment](actions/powerautomateenvironment.md)

- Retrieve environment variable

### Power Automate secret variables (1)

Fetch credentials stored in the Power Automate environment.

Docs: [Power Automate secret variables](actions/powerautomatesecretvariables.md)

- Get credential

### Run flow (1)

Call another desktop flow and wait for its outputs.

Docs: [Run flow](actions/runflow.md)

- Run desktop flow

### SAP automation (11)

Drive SAP GUI: login, transactions, and UI element interaction.

Docs: [SAP automation](actions/sap.md)

- Launch SAP
- Attach
- Create new SAP session
- Select SAP navigation item
- Select SAP menu item
- Close SAP connection
- Start SAP transaction
- End SAP transaction
- Click SAP UI element
- Get details of SAP UI element
- Populate SAP text field in element

### Scripting (6)

Run DOS, VBScript, JavaScript, PowerShell, Python, and .NET scripts.

Docs: [Scripting](actions/scripting.md)

- Run DOS command
- Run VBScript
- Run JavaScript
- Run PowerShell script
- Run Python script
- Run .NET script

### SharePoint (0)

Use the SharePoint cloud connector from a desktop flow.

Docs: [SharePoint](actions/sharepoint.md)

Dynamic catalog (connector operations, custom modules, or environment-specific items).

### System (8)

Run processes, ping hosts, and manage Windows environment variables.

Docs: [System](actions/system.md)

- If process
- Wait for process
- Run application
- Terminate process
- Ping
- Set Windows environment variable
- Get Windows environment variable
- Delete Windows environment variable

### Terminal emulation (8)

Automate mainframe and terminal sessions (HLLAPI / terminal emulators).

Docs: [Terminal emulation](actions/terminalemulation.md)

- Open terminal session
- Close terminal session
- Move cursor on terminal session
- Get text from terminal session
- Set text on terminal session
- Send key to terminal session
- Wait for text on terminal session
- Search for text on terminal session

### Testing (2)

Build desktop-flow test cases with Assert and Test a desktop flow.

Docs: [Testing](actions/testing.md)

- Test a desktop flow
- Assert

### Text (19)

Parse, split, join, convert, and transform text values.

Docs: [Text](actions/text.md)

- Append line to text
- Get subtext
- Crop text
- Pad text
- Trim text
- Reverse text
- Change text case
- Convert text to number
- Convert number to text
- Convert text to datetime
- Convert datetime to text
- Create random text
- Join text
- Split text
- Parse text
- Replace text
- Escape text for regular expression
- Recognize entities in text
- Create HTML content

### UI automation (33)

Click, type, extract, and wait on Windows UI elements and images.

Docs: [UI automation](actions/uiautomation.md)

- Get details of window
- Get details of a UI element in window
- Get selected checkboxes in window
- Get selected radio button in window
- Extract data from window
- Extract data from table
- Take screenshot of UI element
- Focus text field in window
- Populate text field in window
- Press button in window
- Select radio button in window
- Set checkbox state in window
- Set drop-down list value in window
- Get window
- Focus window
- Set window state
- Set window visibility
- Move window
- Resize window
- Close window
- If window contains
- Wait for window content
- If image
- Use desktop
- Select tab in window
- Wait for image
- Hover mouse over UI element in window
- Click UI element in window
- Select menu option in window
- Drag and drop UI element in window
- Expand/collapse tree node in window
- If window
- Wait for window

### Variables (36)

Set variables and work with lists, data tables, JSON, and Power Fx.

Docs: [Variables](actions/variables.md)

- Create new data table
- Insert row into data table
- Delete row from data table
- Update data table item
- Find or replace in data table
- Insert column into data table
- Delete column from data table
- Delete empty rows from data table
- Delete duplicate rows from data table
- Clear data table
- Sort data table
- Filter data table
- Merge data tables
- Join data tables
- Read from CSV text variable
- Convert data table to text
- Truncate number
- Generate random number
- Clear list
- Remove item from list
- Sort list
- Shuffle list
- Merge lists
- Reverse list
- Remove duplicate items from list
- Find common list items
- Subtract lists
- Retrieve data table column into list
- Convert JSON to custom object
- Convert custom object to JSON
- Add item to list
- Create new list
- Increase variable
- Decrease variable
- Run Power Fx expression
- Set variable

### Windows services (6)

Start, stop, pause, resume, and wait for Windows services.

Docs: [Windows services](actions/services.md)

- If service
- Wait for service
- Start service
- Stop service
- Pause service
- Resume service

### Word (8)

Launch Word and read, write, or replace document content.

Docs: [Word](actions/word.md)

- Launch Word
- Attach to running Word
- Save Word
- Close Word
- Read from Word document
- Write to Word document
- Insert image in Word document
- Find and replace words in Word document

### Work queues (5)

Add, process, and update Power Automate work queue items.

Docs: [Work queues](actions/workqueues.md)

- Process work queue items
- Add work queue item
- Add multiple work queue items
- Requeue item with delay
- Get work queue items by filter

### Workstation (13)

Control the local workstation: screenshots, printers, lock, shutdown.

Docs: [Workstation](actions/workstation.md)

- Print document
- Get default printer
- Set default printer
- Show desktop
- Lock workstation
- Play sound
- Empty recycle bin
- Take screenshot
- Control screen saver
- Get screen resolution
- Set screen resolution
- Log off user
- Shutdown computer

### XML (10)

Read, query, and edit XML documents and nodes.

Docs: [XML](actions/xml.md)

- Read XML from file
- Write XML to file
- Execute XPath expression
- Get XML element attribute
- Set XML element attribute
- Remove XML element attribute
- Get XML element value
- Set XML element value
- Insert XML element
- Remove XML element

Named built-in actions counted above: **444**.

## Expression functions (not in the Actions pane)

### Classic `%` functions (8)

Documented in [functions/percent-notation.md](functions/percent-notation.md).

- `StartsWith`
- `NotStartsWith`
- `EndsWith`
- `NotEndsWith`
- `Contains`
- `NotContains`
- `IsEmpty`
- `IsNotEmpty`

Plus operators `+` `-` `*` `/` `=` `<>` `<` `<=` `>` `>=` `AND` `OR` `NOT`.

### Power Fx functions (130)

Documented in [functions/power-fx.md](functions/power-fx.md). Enabled per flow at creation time.

## Designer assets (usable, not functions)

See [usable-items.md](usable-items.md): variables, UI elements, images, credentials, connections, subflows, recorders, Copilot, work queues, machines, custom action modules, environment variables, test cases.

Microsoft Learn also mentions a **Triggers** group in some indexes. In current PAD, starting a flow is done from the console, a cloud flow, a shortcut, or work queues — not a separate 445th action module in this catalog.
