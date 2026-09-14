# Power Automate Desktop inventory

This is **step 1**: a complete catalog of usable items in Power Automate for desktop (PAD). Each native action and Power Fx function is documented on its module page.

## Counts

- Native designer actions: **448**
- Cloud connector operations (default pane set): **185**
- Power Fx functions (Power Fx–enabled flows): **130**
- Designer / console usable items: **35**
- Variable data types: **39**
- Native action modules: **50**

Machine-readable copy: [`inventory.json`](inventory.json).

## How PAD is organized

1. **Designer surfaces** — panes, recorders, variables, UI elements, images, errors.
2. **Native actions** — modules in the actions pane (Variables, Excel, UI automation, …).
3. **Cloud connectors** — the same operations as cloud flows, run inside PAD.
4. **Power Fx functions** — formula language when the flow is Power Fx–enabled.
5. **Data types** — values that variables and action outputs hold.

## Native action modules

| Module | Items | Documentation |
| --- | ---: | --- |
| Access | 5 | [access.md](modules/access.md) |
| Active Directory | 15 | [activedirectory.md](modules/activedirectory.md) |
| AI Builder (preview) | 1 | [aibuilder.md](modules/aibuilder.md) |
| AWS | 15 | [aws.md](modules/aws.md) |
| Azure | 20 | [azure.md](modules/azure.md) |
| Browser automation | 23 | [webautomation.md](modules/webautomation.md) |
| Clipboard | 3 | [clipboard.md](modules/clipboard.md) |
| CMD session | 5 | [cmd.md](modules/cmd.md) |
| Compression | 2 | [compression.md](modules/compression.md) |
| Conditionals | 6 | [conditionals.md](modules/conditionals.md) |
| Cryptography | 8 | [cryptography.md](modules/cryptography.md) |
| CyberArk | 1 | [cyberark.md](modules/cyberark.md) |
| Database | 3 | [database.md](modules/database.md) |
| Date time | 3 | [datetime.md](modules/datetime.md) |
| Email | 3 | [email.md](modules/email.md) |
| Excel | 41 | [excel.md](modules/excel.md) |
| Exchange Server | 4 | [exchange.md](modules/exchange.md) |
| File | 16 | [file.md](modules/file.md) |
| Flow control | 14 | [flowcontrol.md](modules/flowcontrol.md) |
| Folder | 10 | [folder.md](modules/folder.md) |
| FTP | 15 | [ftp.md](modules/ftp.md) |
| Google Cognitive | 9 | [googlecognitive.md](modules/googlecognitive.md) |
| HTTP | 3 | [web.md](modules/web.md) |
| IBM Cognitive | 5 | [ibmcognitive.md](modules/ibmcognitive.md) |
| Logging | 1 | [logging.md](modules/logging.md) |
| Loops | 5 | [loops.md](modules/loops.md) |
| Message boxes | 7 | [display.md](modules/display.md) |
| Microsoft Cognitive | 8 | [microsoftcognitive.md](modules/microsoftcognitive.md) |
| Mouse and keyboard | 12 | [mouseandkeyboard.md](modules/mouseandkeyboard.md) |
| OCR | 3 | [ocr.md](modules/ocr.md) |
| Outlook | 7 | [outlook.md](modules/outlook.md) |
| PDF | 5 | [pdf.md](modules/pdf.md) |
| Power Automate environment | 1 | [powerautomateenvironment.md](modules/powerautomateenvironment.md) |
| Power Automate secret variables | 1 | [powerautomatesecretvariables.md](modules/powerautomatesecretvariables.md) |
| Power Platform | 1 | [power-platform.md](modules/power-platform.md) |
| Run flow | 1 | [runflow.md](modules/runflow.md) |
| SAP automation | 11 | [sap.md](modules/sap.md) |
| Scripting | 6 | [scripting.md](modules/scripting.md) |
| System | 8 | [system.md](modules/system.md) |
| Terminal emulation | 8 | [terminalemulation.md](modules/terminalemulation.md) |
| Testing | 2 | [testing.md](modules/testing.md) |
| Text | 19 | [text.md](modules/text.md) |
| Triggers | 1 | [triggers.md](modules/triggers.md) |
| UI automation | 33 | [uiautomation.md](modules/uiautomation.md) |
| Variables | 36 | [variables.md](modules/variables.md) |
| Windows services | 6 | [services.md](modules/services.md) |
| Word | 8 | [word.md](modules/word.md) |
| Work queues | 5 | [workqueues.md](modules/workqueues.md) |
| Workstation | 13 | [workstation.md](modules/workstation.md) |
| XML | 10 | [xml.md](modules/xml.md) |

## Native actions (complete list)

| Action | Module | Purpose |
| --- | --- | --- |
| [Close Access](modules/access.md#close-access) | Access | Closes access. |
| [Launch Access](modules/access.md#launch-access) | Access | Starts Access and returns an instance later actions can reuse. |
| [Read Access table](modules/access.md#read-access-table) | Access | Reads access table. |
| [Run Access macro](modules/access.md#run-access-macro) | Access | Runs access macro. |
| [Run Access query](modules/access.md#run-access-query) | Access | Runs access query. |
| [Close connection](modules/activedirectory.md#close-connection) | Active Directory | Closes connection. |
| [Connect to server](modules/activedirectory.md#connect-to-server) | Active Directory | Connects to an Active Directory server. |
| [Create group](modules/activedirectory.md#create-group) | Active Directory | Creates group. |
| [Create object](modules/activedirectory.md#create-object) | Active Directory | Creates object. |
| [Create user](modules/activedirectory.md#create-user) | Active Directory | Creates user. |
| [Delete object](modules/activedirectory.md#delete-object) | Active Directory | Deletes object. |
| [Get group info](modules/activedirectory.md#get-group-info) | Active Directory | Reads group info into a flow variable. |
| [Get group members](modules/activedirectory.md#get-group-members) | Active Directory | Reads group members into a flow variable. |
| [Get user info](modules/activedirectory.md#get-user-info) | Active Directory | Reads user info into a flow variable. |
| [Modify group](modules/activedirectory.md#modify-group) | Active Directory | Modifies a group in the Active Directory. |
| [Modify user](modules/activedirectory.md#modify-user) | Active Directory | Modify a user in the Active Directory. |
| [Move object](modules/activedirectory.md#move-object) | Active Directory | Moves object. |
| [Rename object](modules/activedirectory.md#rename-object) | Active Directory | Renames object. |
| [Unlock user](modules/activedirectory.md#unlock-user) | Active Directory | Unlocks an Active Directory user. |
| [Update user info](modules/activedirectory.md#update-user-info) | Active Directory | Updates user info. |
| [Create text with GPT (preview)](modules/aibuilder.md#create-text-with-gpt-preview) | AI Builder (preview) | Creates text with GPT (preview). |
| [Attach volume](modules/aws.md#attach-volume) | AWS | Connects the flow to volume that is already running. |
| [Create EC2 session](modules/aws.md#create-ec2-session) | AWS | Creates EC2 session. |
| [Create snapshot](modules/aws.md#create-snapshot) | AWS | Creates snapshot. |
| [Create volume](modules/aws.md#create-volume) | AWS | Creates volume. |
| [Delete snapshot](modules/aws.md#delete-snapshot) | AWS | Deletes snapshot. |
| [Delete volume](modules/aws.md#delete-volume) | AWS | Deletes volume. |
| [Describe instances](modules/aws.md#describe-instances) | AWS | Returns all the information for the specified EC2 instance(s). |
| [Describe snapshots](modules/aws.md#describe-snapshots) | AWS | Describes the specified EBS snapshots available. |
| [Describe volumes](modules/aws.md#describe-volumes) | AWS | Describe the specified EBS volumes. |
| [Detach volume](modules/aws.md#detach-volume) | AWS | Detach an EBS volume from an EC2 instance. |
| [End EC2 session](modules/aws.md#end-ec2-session) | AWS | Ends EC2 session. |
| [Get available EC2 instances](modules/aws.md#get-available-ec2-instances) | AWS | Reads available EC2 instances into a flow variable. |
| [Reboot EC2 instance](modules/aws.md#reboot-ec2-instance) | AWS | Reboot EC2 instance(s). |
| [Start EC2 instance](modules/aws.md#start-ec2-instance) | AWS | Starts EC2 instance. |
| [Stop EC2 instance](modules/aws.md#stop-ec2-instance) | AWS | Stops EC2 instance. |
| [Attach disk](modules/azure.md#attach-disk) | Azure | Connects the flow to disk that is already running. |
| [Create managed disk](modules/azure.md#create-managed-disk) | Azure | Creates managed disk. |
| [Create resource group](modules/azure.md#create-resource-group) | Azure | Creates resource group. |
| [Create session](modules/azure.md#create-session) | Azure | Creates session. |
| [Create snapshot](modules/azure.md#create-snapshot) | Azure | Creates snapshot. |
| [Delete disk](modules/azure.md#delete-disk) | Azure | Deletes disk. |
| [Delete resource group](modules/azure.md#delete-resource-group) | Azure | Deletes resource group. |
| [Delete snapshot](modules/azure.md#delete-snapshot) | Azure | Deletes snapshot. |
| [Describe virtual machine](modules/azure.md#describe-virtual-machine) | Azure | Gets all the information for the virtual machine(s) based on the specified criteria. |
| [Detach disk](modules/azure.md#detach-disk) | Azure | Detaches the disk from the virtual machine with the specified name and resource group. |
| [End session](modules/azure.md#end-session) | Azure | Ends session. |
| [Get disks](modules/azure.md#get-disks) | Azure | Reads disks into a flow variable. |
| [Get resource groups](modules/azure.md#get-resource-groups) | Azure | Reads resource groups into a flow variable. |
| [Get snapshots](modules/azure.md#get-snapshots) | Azure | Reads snapshots into a flow variable. |
| [Get subscriptions](modules/azure.md#get-subscriptions) | Azure | Reads subscriptions into a flow variable. |
| [Get virtual machines](modules/azure.md#get-virtual-machines) | Azure | Reads virtual machines into a flow variable. |
| [Restart virtual machine](modules/azure.md#restart-virtual-machine) | Azure | Restarts a virtual machine. |
| [Shut down virtual machine](modules/azure.md#shut-down-virtual-machine) | Azure | Shuts down the operating system of a virtual machine. |
| [Start virtual machine](modules/azure.md#start-virtual-machine) | Azure | Starts virtual machine. |
| [Stop virtual machine](modules/azure.md#stop-virtual-machine) | Azure | Stops virtual machine. |
| [Clear clipboard contents](modules/clipboard.md#clear-clipboard-contents) | Clipboard | Clears clipboard contents. |
| [Get clipboard text](modules/clipboard.md#get-clipboard-text) | Clipboard | Reads clipboard text into a flow variable. |
| [Set clipboard Text](modules/clipboard.md#set-clipboard-text) | Clipboard | Writes clipboard Text. |
| [Close CMD session](modules/cmd.md#close-cmd-session) | CMD session | Closes CMD session. |
| [Open CMD session](modules/cmd.md#open-cmd-session) | CMD session | Opens CMD session. |
| [Read from CMD session](modules/cmd.md#read-from-cmd-session) | CMD session | Reads from CMD session. |
| [Wait for text on CMD session](modules/cmd.md#wait-for-text-on-cmd-session) | CMD session | Pauses the flow until text on CMD session. |
| [Write to CMD session](modules/cmd.md#write-to-cmd-session) | CMD session | Writes to CMD session. |
| [Unzip files](modules/compression.md#unzip-files) | Compression | Extracts files from a ZIP archive. |
| [ZIP files](modules/compression.md#zip-files) | Compression | Compresses files or folders into a ZIP archive. |
| [Case](modules/conditionals.md#case) | Conditionals | One match arm inside a Switch block. |
| [Default case](modules/conditionals.md#default-case) | Conditionals | Fallback arm when no Case in a Switch matches. |
| [Else](modules/conditionals.md#else) | Conditionals | Runs when no earlier If / Else if condition was true. |
| [Else if](modules/conditionals.md#else-if) | Conditionals | Tests another condition after an If that did not match. |
| [If](modules/conditionals.md#if) | Conditionals | Marks the beginning of a block of actions that is run if the condition specified in this statement is met. |
| [Switch](modules/conditionals.md#switch) | Conditionals | Routes execution to the Case that matches an expression. |
| [Decrypt text with AES](modules/cryptography.md#decrypt-text-with-aes) | Cryptography | Decrypts text with AES. |
| [Decrypt to file with AES](modules/cryptography.md#decrypt-to-file-with-aes) | Cryptography | Decrypts to file with AES. |
| [Encrypt from file with AES](modules/cryptography.md#encrypt-from-file-with-aes) | Cryptography | Encrypts from file with AES. |
| [Encrypt text with AES](modules/cryptography.md#encrypt-text-with-aes) | Cryptography | Encrypts text with AES. |
| [Hash from file](modules/cryptography.md#hash-from-file) | Cryptography | Hashes from file. |
| [Hash from file with key](modules/cryptography.md#hash-from-file-with-key) | Cryptography | Hashes from file with key. |
| [Hash text](modules/cryptography.md#hash-text) | Cryptography | Hashes text. |
| [Hash text with key](modules/cryptography.md#hash-text-with-key) | Cryptography | Hashes text with key. |
| [Get password from CyberArk](modules/cyberark.md#get-password-from-cyberark) | CyberArk | Reads password from CyberArk into a flow variable. |
| [Close SQL connection](modules/database.md#close-sql-connection) | Database | Closes SQL connection. |
| [Execute SQL statement](modules/database.md#execute-sql-statement) | Database | Connect to a database and execute a SQL statement. |
| [Open SQL connection](modules/database.md#open-sql-connection) | Database | Opens SQL connection. |
| [Add to datetime](modules/datetime.md#add-to-datetime) | Date time | Adds to datetime. |
| [Get current date and time](modules/datetime.md#get-current-date-and-time) | Date time | Reads current date and time into a flow variable. |
| [Subtract dates](modules/datetime.md#subtract-dates) | Date time | Finds the time difference between two given dates in days, hours, minutes, or seconds. |
| [Display custom form](modules/display.md#display-custom-form) | Message boxes | Shows custom form to the user. |
| [Display input dialog](modules/display.md#display-input-dialog) | Message boxes | Shows input dialog to the user. |
| [Display message](modules/display.md#display-message) | Message boxes | Shows message to the user. |
| [Display select  file dialog](modules/display.md#display-select-file-dialog) | Message boxes | Shows select  file dialog to the user. |
| [Display select date dialog](modules/display.md#display-select-date-dialog) | Message boxes | Shows select date dialog to the user. |
| [Display select folder dialog](modules/display.md#display-select-folder-dialog) | Message boxes | Shows select folder dialog to the user. |
| [Display select from list dialog](modules/display.md#display-select-from-list-dialog) | Message boxes | Shows select from list dialog to the user. |
| [Process email messages](modules/email.md#process-email-messages) | Email | Processes email messages. |
| [Retrieve email messages](modules/email.md#retrieve-email-messages) | Email | Retrieves email messages. |
| [Send email](modules/email.md#send-email) | Email | Sends email. |
| [Activate cell in Excel worksheet](modules/excel.md#activate-cell-in-excel-worksheet) | Excel | Activate a cell in the active worksheet of an Excel instance, by providing column, row, and offset. |
| [Add new worksheet](modules/excel.md#add-new-worksheet) | Excel | Adds new worksheet. |
| [Append cells in Excel worksheet](modules/excel.md#append-cells-in-excel-worksheet) | Excel | Appends a range of cells to the active worksheet of an Excel instance. |
| [Attach to running Excel](modules/excel.md#attach-to-running-excel) | Excel | Connects the flow to running Excel that is already running. |
| [Auto fill cells in Excel worksheet](modules/excel.md#auto-fill-cells-in-excel-worksheet) | Excel | Auto fills a range with data, based on the data of another range, in the active worksheet of an Excel instance. |
| [Clear cells in Excel worksheet](modules/excel.md#clear-cells-in-excel-worksheet) | Excel | Clears cells in Excel worksheet. |
| [Clear filters in Excel worksheet](modules/excel.md#clear-filters-in-excel-worksheet) | Excel | Clears filters in Excel worksheet. |
| [Close Excel](modules/excel.md#close-excel) | Excel | Closes excel. |
| [Copy cells from Excel worksheet](modules/excel.md#copy-cells-from-excel-worksheet) | Excel | Copies cells from Excel worksheet. |
| [Copy Excel worksheet](modules/excel.md#copy-excel-worksheet) | Excel | Copies excel worksheet. |
| [Delete column from Excel worksheet](modules/excel.md#delete-column-from-excel-worksheet) | Excel | Deletes column from Excel worksheet. |
| [Delete Excel worksheet](modules/excel.md#delete-excel-worksheet) | Excel | Deletes excel worksheet. |
| [Delete from Excel worksheet](modules/excel.md#delete-from-excel-worksheet) | Excel | Deletes from Excel worksheet. |
| [Delete row from Excel worksheet](modules/excel.md#delete-row-from-excel-worksheet) | Excel | Deletes row from Excel worksheet. |
| [Filter cells in Excel worksheet](modules/excel.md#filter-cells-in-excel-worksheet) | Excel | Filters cells in Excel worksheet. |
| [Find and replace cells in Excel worksheet](modules/excel.md#find-and-replace-cells-in-excel-worksheet) | Excel | Finds and replace cells in Excel worksheet. |
| [Get active cell on Excel worksheet](modules/excel.md#get-active-cell-on-excel-worksheet) | Excel | Reads active cell on Excel worksheet into a flow variable. |
| [Get active Excel worksheet](modules/excel.md#get-active-excel-worksheet) | Excel | Reads active Excel worksheet into a flow variable. |
| [Get all Excel worksheets](modules/excel.md#get-all-excel-worksheets) | Excel | Reads all Excel worksheets into a flow variable. |
| [Get column name on Excel worksheet](modules/excel.md#get-column-name-on-excel-worksheet) | Excel | Reads column name on Excel worksheet into a flow variable. |
| [Get empty cell](modules/excel.md#get-empty-cell) | Excel | Reads empty cell into a flow variable. |
| [Get first free column/row from Excel worksheet](modules/excel.md#get-first-free-column-row-from-excel-worksheet) | Excel | Reads first free column/row from Excel worksheet into a flow variable. |
| [Get first free row on column from Excel worksheet](modules/excel.md#get-first-free-row-on-column-from-excel-worksheet) | Excel | Reads first free row on column from Excel worksheet into a flow variable. |
| [Get selected cell range from Excel worksheet](modules/excel.md#get-selected-cell-range-from-excel-worksheet) | Excel | Reads selected cell range from Excel worksheet into a flow variable. |
| [Get table range from Excel worksheet](modules/excel.md#get-table-range-from-excel-worksheet) | Excel | Reads table range from Excel worksheet into a flow variable. |
| [Insert column to Excel worksheet](modules/excel.md#insert-column-to-excel-worksheet) | Excel | Inserts column to Excel worksheet. |
| [Insert row to Excel worksheet](modules/excel.md#insert-row-to-excel-worksheet) | Excel | Inserts row to Excel worksheet. |
| [Launch Excel](modules/excel.md#launch-excel) | Excel | Starts Excel and returns an instance later actions can reuse. |
| [Lookup range in Excel worksheet](modules/excel.md#lookup-range-in-excel-worksheet) | Excel | Finds and returns the result of Excel's LOOKUP function. |
| [Paste cells to Excel worksheet](modules/excel.md#paste-cells-to-excel-worksheet) | Excel | Pastes a range of cells to the active worksheet of an Excel instance. |
| [Read formula from Excel](modules/excel.md#read-formula-from-excel) | Excel | Reads formula from Excel. |
| [Read from Excel worksheet](modules/excel.md#read-from-excel-worksheet) | Excel | Reads from Excel worksheet. |
| [Rename Excel worksheet](modules/excel.md#rename-excel-worksheet) | Excel | Renames excel worksheet. |
| [Resize columns/rows in Excel worksheet](modules/excel.md#resize-columns-rows-in-excel-worksheet) | Excel | Resizes a selection of columns or rows in the active worksheet of an Excel instance. |
| [Run Excel macro](modules/excel.md#run-excel-macro) | Excel | Runs excel macro. |
| [Save Excel](modules/excel.md#save-excel) | Excel | Saves excel. |
| [Select cells in Excel worksheet](modules/excel.md#select-cells-in-excel-worksheet) | Excel | Selects cells in Excel worksheet. |
| [Set active Excel worksheet](modules/excel.md#set-active-excel-worksheet) | Excel | Writes active Excel worksheet. |
| [Set color of cells in Excel worksheet](modules/excel.md#set-color-of-cells-in-excel-worksheet) | Excel | Writes color of cells in Excel worksheet. |
| [Sort cells in Excel worksheet](modules/excel.md#sort-cells-in-excel-worksheet) | Excel | Sorts cells in Excel worksheet. |
| [Write to Excel worksheet](modules/excel.md#write-to-excel-worksheet) | Excel | Writes to Excel worksheet. |
| [Connect to Exchange server](modules/exchange.md#connect-to-exchange-server) | Exchange Server | Open a new connection to an Exchange server. |
| [Process Exchange email messages](modules/exchange.md#process-exchange-email-messages) | Exchange Server | Processes exchange email messages. |
| [Retrieve Exchange email messages](modules/exchange.md#retrieve-exchange-email-messages) | Exchange Server | Retrieves exchange email messages. |
| [Send Exchange email message](modules/exchange.md#send-exchange-email-message) | Exchange Server | Sends exchange email message. |
| [Convert Base64 to file](modules/file.md#convert-base64-to-file) | File | Converts base64 to file. |
| [Convert binary data to file](modules/file.md#convert-binary-data-to-file) | File | Converts binary data to file. |
| [Convert file to Base64](modules/file.md#convert-file-to-base64) | File | Converts file to Base64. |
| [Convert file to binary data](modules/file.md#convert-file-to-binary-data) | File | Converts file to binary data. |
| [Copy file(s)](modules/file.md#copy-file-s) | File | Copies file(s). |
| [Delete file(s)](modules/file.md#delete-file-s) | File | Deletes file(s). |
| [Get file path part](modules/file.md#get-file-path-part) | File | Reads file path part into a flow variable. |
| [Get temporary file](modules/file.md#get-temporary-file) | File | Reads temporary file into a flow variable. |
| [If file exists](modules/file.md#if-file-exists) | File | Opens a conditional branch that runs when file exists. |
| [Move file(s)](modules/file.md#move-file-s) | File | Moves file(s). |
| [Read from CSV file](modules/file.md#read-from-csv-file) | File | Reads from CSV file. |
| [Read text from file](modules/file.md#read-text-from-file) | File | Reads text from file. |
| [Rename file(s)](modules/file.md#rename-file-s) | File | Renames file(s). |
| [Wait for file](modules/file.md#wait-for-file) | File | Pauses the flow until file. |
| [Write text to file](modules/file.md#write-text-to-file) | File | Writes text to file. |
| [Write to CSV file](modules/file.md#write-to-csv-file) | File | Writes to CSV file. |
| [Comment](modules/flowcontrol.md#comment) | Flow control | Adds a note on the canvas. It does not run. |
| [End](modules/flowcontrol.md#end) | Flow control | Closes the current block (condition, loop, or error block). |
| [End region](modules/flowcontrol.md#end-region) | Flow control | Ends region. |
| [Exit subflow](modules/flowcontrol.md#exit-subflow) | Flow control | Returns from the current subflow to its caller. |
| [Get last error](modules/flowcontrol.md#get-last-error) | Flow control | Reads last error into a flow variable. |
| [Go to](modules/flowcontrol.md#go-to) | Flow control | Jumps execution to a Label in the same subflow. |
| [If safe stop requested](modules/flowcontrol.md#if-safe-stop-requested) | Flow control | Opens a conditional branch that runs when safe stop requested. |
| [Label](modules/flowcontrol.md#label) | Flow control | Named jump target for a Go to action. |
| [On block error](modules/flowcontrol.md#on-block-error) | Flow control | Starts a block whose nested failures are handled together. |
| [Region](modules/flowcontrol.md#region) | Flow control | Starts a named visual group of actions. |
| [Run subflow](modules/flowcontrol.md#run-subflow) | Flow control | Runs subflow. |
| [Stop flow](modules/flowcontrol.md#stop-flow) | Flow control | Stops flow. |
| [Throw custom error](modules/flowcontrol.md#throw-custom-error) | Flow control | Raises a maker-defined error for On block error to catch. |
| [Wait](modules/flowcontrol.md#wait) | Flow control | Pauses the flow for a number of seconds. |
| [Copy folder](modules/folder.md#copy-folder) | Folder | Copies folder. |
| [Create folder](modules/folder.md#create-folder) | Folder | Creates folder. |
| [Delete folder](modules/folder.md#delete-folder) | Folder | Deletes folder. |
| [Empty folder](modules/folder.md#empty-folder) | Folder | Delete all the contents of a folder (files and subfolders) without deleting the folder itself. |
| [Get files in folder](modules/folder.md#get-files-in-folder) | Folder | Reads files in folder into a flow variable. |
| [Get special folder](modules/folder.md#get-special-folder) | Folder | Reads special folder into a flow variable. |
| [Get subfolders in folder](modules/folder.md#get-subfolders-in-folder) | Folder | Reads subfolders in folder into a flow variable. |
| [If folder exists](modules/folder.md#if-folder-exists) | Folder | Opens a conditional branch that runs when folder exists. |
| [Move folder](modules/folder.md#move-folder) | Folder | Moves folder. |
| [Rename folder](modules/folder.md#rename-folder) | Folder | Renames folder. |
| [Change working directory](modules/ftp.md#change-working-directory) | FTP | This action sets the current working directory for an FTP connection. |
| [Close connection](modules/ftp.md#close-connection) | FTP | Closes connection. |
| [Create FTP directory](modules/ftp.md#create-ftp-directory) | FTP | Creates FTP directory. |
| [Delete FTP directory](modules/ftp.md#delete-ftp-directory) | FTP | Deletes FTP directory. |
| [Delete FTP file](modules/ftp.md#delete-ftp-file) | FTP | Deletes FTP file. |
| [Download file(s) from FTP](modules/ftp.md#download-file-s-from-ftp) | FTP | Downloads file(s) from FTP. |
| [Download folder(s) from FTP](modules/ftp.md#download-folder-s-from-ftp) | FTP | Downloads folder(s) from FTP. |
| [Invoke FTP command](modules/ftp.md#invoke-ftp-command) | FTP | Calls FTP command. |
| [List FTP directory](modules/ftp.md#list-ftp-directory) | FTP | Lists FTP directory. |
| [Open FTP connection](modules/ftp.md#open-ftp-connection) | FTP | Opens FTP connection. |
| [Open secure FTP connection](modules/ftp.md#open-secure-ftp-connection) | FTP | Opens secure FTP connection. |
| [Rename FTP File](modules/ftp.md#rename-ftp-file) | FTP | Renames FTP File. |
| [Synchronize directories](modules/ftp.md#synchronize-directories) | FTP | Synchronize the files and subdirectories of a given Folder with a given remote FTP directory. |
| [Upload File(s) to FTP](modules/ftp.md#upload-file-s-to-ftp) | FTP | Uploads file(s) to FTP. |
| [Upload folder(s) to FTP](modules/ftp.md#upload-folder-s-to-ftp) | FTP | Uploads folder(s) to FTP. |
| [Analyze entities](modules/googlecognitive.md#analyze-entities) | Google Cognitive | Invokes the Google Cloud Natural Language service named 'Analyze Entities'. |
| [Analyze sentiment](modules/googlecognitive.md#analyze-sentiment) | Google Cognitive | Invokes the Google Cloud Natural Language service named 'Analyze Sentiment'. |
| [Analyze syntax](modules/googlecognitive.md#analyze-syntax) | Google Cognitive | Invokes the Google Cloud Natural Language service named 'Analyze Syntax'. |
| [Image properties detection](modules/googlecognitive.md#image-properties-detection) | Google Cognitive | Invokes the Google Cloud Vision service named 'Image Properties Detection'. |
| [Label detection](modules/googlecognitive.md#label-detection) | Google Cognitive | Invokes the Google Cloud Vision service named 'Label Detection'. |
| [Landmark detection](modules/googlecognitive.md#landmark-detection) | Google Cognitive | Invokes the Google Cloud Vision service named 'Landmark Detection'. |
| [Logo detection](modules/googlecognitive.md#logo-detection) | Google Cognitive | Invokes the Google Cloud Vision service named 'Logo Detection'. |
| [Safe search detection](modules/googlecognitive.md#safe-search-detection) | Google Cognitive | Invokes the Google Cloud Vision service named 'Safe Search Detection'. |
| [Text Detection](modules/googlecognitive.md#text-detection) | Google Cognitive | Invokes the Google Cloud Vision service named 'Text Detection'. |
| [Analyze tone](modules/ibmcognitive.md#analyze-tone) | IBM Cognitive | Invokes the IBM service named 'Analyze Tone'. |
| [Classify Image](modules/ibmcognitive.md#classify-image) | IBM Cognitive | Invokes the IBM service named 'Classify Image'. |
| [Convert document](modules/ibmcognitive.md#convert-document) | IBM Cognitive | Converts document. |
| [Identify language](modules/ibmcognitive.md#identify-language) | IBM Cognitive | Invokes the IBM service named 'Identify Language'. |
| [Translate](modules/ibmcognitive.md#translate) | IBM Cognitive | Invokes the IBM service named 'Translate'. |
| [Log message](modules/logging.md#log-message) | Logging | Writes a custom Info, Warning, or Error line into run details. |
| [Exit loop](modules/loops.md#exit-loop) | Loops | Leaves the current loop and continues with the next action after it. |
| [For each](modules/loops.md#for-each) | Loops | Repeats nested actions once for every item in a list, table, or row. |
| [Loop](modules/loops.md#loop) | Loops | Repeats nested actions a fixed number of times. |
| [Loop condition](modules/loops.md#loop-condition) | Loops | Repeats nested actions while a condition stays true. |
| [Next loop](modules/loops.md#next-loop) | Loops | Skips the rest of this iteration and starts the next one. |
| [Analyze image](modules/microsoftcognitive.md#analyze-image) | Microsoft Cognitive | Runs **Analyze image** from the actions pane. |
| [Describe image](modules/microsoftcognitive.md#describe-image) | Microsoft Cognitive | Runs **Describe image** from the actions pane. |
| [Detect language](modules/microsoftcognitive.md#detect-language) | Microsoft Cognitive | Runs **Detect language** from the actions pane. |
| [Key phrases](modules/microsoftcognitive.md#key-phrases) | Microsoft Cognitive | Runs **Key phrases** from the actions pane. |
| [OCR](modules/microsoftcognitive.md#ocr) | Microsoft Cognitive | Runs **OCR** from the actions pane. |
| [Sentiment](modules/microsoftcognitive.md#sentiment) | Microsoft Cognitive | Runs **Sentiment** from the actions pane. |
| [Spell check](modules/microsoftcognitive.md#spell-check) | Microsoft Cognitive | Runs **Spell check** from the actions pane. |
| [Tag image](modules/microsoftcognitive.md#tag-image) | Microsoft Cognitive | Runs **Tag image** from the actions pane. |
| [Block Input](modules/mouseandkeyboard.md#block-input) | Mouse and keyboard | Temporarily blocks the user's mouse and keyboard. |
| [Get keyboard identifier](modules/mouseandkeyboard.md#get-keyboard-identifier) | Mouse and keyboard | Reads keyboard identifier into a flow variable. |
| [Get mouse position](modules/mouseandkeyboard.md#get-mouse-position) | Mouse and keyboard | Reads mouse position into a flow variable. |
| [Move mouse](modules/mouseandkeyboard.md#move-mouse) | Mouse and keyboard | Moves mouse. |
| [Move mouse to image](modules/mouseandkeyboard.md#move-mouse-to-image) | Mouse and keyboard | Moves mouse to image. |
| [Move mouse to text on screen (OCR)](modules/mouseandkeyboard.md#move-mouse-to-text-on-screen-ocr) | Mouse and keyboard | Moves mouse to text on screen (OCR). |
| [Press/release key](modules/mouseandkeyboard.md#press-release-key) | Mouse and keyboard | Presses (and holds) or releases one or more modifier keys (Alt, Control, or Shift). |
| [Send keys](modules/mouseandkeyboard.md#send-keys) | Mouse and keyboard | Sends keys. |
| [Send mouse click](modules/mouseandkeyboard.md#send-mouse-click) | Mouse and keyboard | Sends mouse click. |
| [Set key state](modules/mouseandkeyboard.md#set-key-state) | Mouse and keyboard | Writes key state. |
| [Wait for mouse](modules/mouseandkeyboard.md#wait-for-mouse) | Mouse and keyboard | Pauses the flow until mouse. |
| [Wait for shortcut key](modules/mouseandkeyboard.md#wait-for-shortcut-key) | Mouse and keyboard | Pauses the flow until shortcut key. |
| [Extract text with OCR](modules/ocr.md#extract-text-with-ocr) | OCR | Extracts text with OCR. |
| [If text on screen (OCR)](modules/ocr.md#if-text-on-screen-ocr) | OCR | Opens a conditional branch that runs when text on screen (OCR). |
| [Wait for text on screen (OCR)](modules/ocr.md#wait-for-text-on-screen-ocr) | OCR | Pauses the flow until text on screen (OCR). |
| [Close Outlook](modules/outlook.md#close-outlook) | Outlook | Closes outlook. |
| [Launch Outlook](modules/outlook.md#launch-outlook) | Outlook | Starts Outlook and returns an instance later actions can reuse. |
| [Process email messages in Outlook](modules/outlook.md#process-email-messages-in-outlook) | Outlook | Processes email messages in Outlook. |
| [Respond to Outlook mail message](modules/outlook.md#respond-to-outlook-mail-message) | Outlook | Respond to an Outlook message, by replying, replying to all or forwarding it. |
| [Retrieve email messages from Outlook](modules/outlook.md#retrieve-email-messages-from-outlook) | Outlook | Retrieves email messages from Outlook. |
| [Save Outlook email messages](modules/outlook.md#save-outlook-email-messages) | Outlook | Saves outlook email messages. |
| [Send email through Outlook](modules/outlook.md#send-email-through-outlook) | Outlook | Sends email through Outlook. |
| [Extract images from PDF](modules/pdf.md#extract-images-from-pdf) | PDF | Extracts images from PDF. |
| [Extract PDF file pages to new PDF file](modules/pdf.md#extract-pdf-file-pages-to-new-pdf-file) | PDF | Extracts PDF file pages to new PDF file. |
| [Extract tables from PDF](modules/pdf.md#extract-tables-from-pdf) | PDF | Extracts tables from PDF. |
| [Extract text from PDF](modules/pdf.md#extract-text-from-pdf) | PDF | Extracts text from PDF. |
| [Merge PDF files](modules/pdf.md#merge-pdf-files) | PDF | Merges PDF files. |
| [Run Power App (preview)](modules/power-platform.md#run-power-app-preview) | Power Platform | Launches a canvas app from the desktop flow, passes values in, and collects values the app returns. Needs PAD 2.68+. |
| [Retrieve environment variable](modules/powerautomateenvironment.md#retrieve-environment-variable) | Power Automate environment | Retrieves environment variable. |
| [Get credential](modules/powerautomatesecretvariables.md#get-credential) | Power Automate secret variables | Reads credential into a flow variable. |
| [Run desktop flow](modules/runflow.md#run-desktop-flow) | Run flow | Runs desktop flow. |
| [Attach](modules/sap.md#attach) | SAP automation | Attach the running SAP GUI application to an SAP instance. |
| [Click SAP UI element](modules/sap.md#click-sap-ui-element) | SAP automation | Clicks SAP UI element. |
| [Close SAP connection](modules/sap.md#close-sap-connection) | SAP automation | Closes SAP connection. |
| [Create new SAP session](modules/sap.md#create-new-sap-session) | SAP automation | Creates new SAP session. |
| [End SAP transaction](modules/sap.md#end-sap-transaction) | SAP automation | Ends SAP transaction. |
| [Get details of SAP UI element](modules/sap.md#get-details-of-sap-ui-element) | SAP automation | Reads details of SAP UI element into a flow variable. |
| [Launch SAP](modules/sap.md#launch-sap) | SAP automation | Starts SAP and returns an instance later actions can reuse. |
| [Populate SAP text field in element](modules/sap.md#populate-sap-text-field-in-element) | SAP automation | Types or fills SAP text field in element. |
| [Select SAP menu item](modules/sap.md#select-sap-menu-item) | SAP automation | Selects SAP menu item. |
| [Select SAP navigation item](modules/sap.md#select-sap-navigation-item) | SAP automation | Selects SAP navigation item. |
| [Start SAP transaction](modules/sap.md#start-sap-transaction) | SAP automation | Starts SAP transaction. |
| [Run .NET script](modules/scripting.md#run-net-script) | Scripting | Runs .NET script. |
| [Run DOS command](modules/scripting.md#run-dos-command) | Scripting | Runs DOS command. |
| [Run JavaScript](modules/scripting.md#run-javascript) | Scripting | Runs javaScript. |
| [Run PowerShell script](modules/scripting.md#run-powershell-script) | Scripting | Runs powerShell script. |
| [Run Python script](modules/scripting.md#run-python-script) | Scripting | Runs python script. |
| [Run VBScript](modules/scripting.md#run-vbscript) | Scripting | Runs VBScript. |
| [If service](modules/services.md#if-service) | Windows services | Opens a conditional branch that runs when service. |
| [Pause service](modules/services.md#pause-service) | Windows services | Pause a running Windows service. |
| [Resume service](modules/services.md#resume-service) | Windows services | Resume a paused Windows service. |
| [Start service](modules/services.md#start-service) | Windows services | Starts service. |
| [Stop service](modules/services.md#stop-service) | Windows services | Stops service. |
| [Wait for service](modules/services.md#wait-for-service) | Windows services | Pauses the flow until service. |
| [Delete Windows environment variable](modules/system.md#delete-windows-environment-variable) | System | Deletes windows environment variable. |
| [Get Windows environment variable](modules/system.md#get-windows-environment-variable) | System | Reads windows environment variable into a flow variable. |
| [If process](modules/system.md#if-process) | System | Opens a conditional branch that runs when process. |
| [Ping](modules/system.md#ping) | System | Checks whether a remote host answers on the network. |
| [Run application](modules/system.md#run-application) | System | Runs application. |
| [Set Windows environment variable](modules/system.md#set-windows-environment-variable) | System | Writes windows environment variable. |
| [Terminate process](modules/system.md#terminate-process) | System | Immediately stops a running process. |
| [Wait for process](modules/system.md#wait-for-process) | System | Pauses the flow until process. |
| [Close terminal session](modules/terminalemulation.md#close-terminal-session) | Terminal emulation | Closes terminal session. |
| [Get text from terminal session](modules/terminalemulation.md#get-text-from-terminal-session) | Terminal emulation | Reads text from terminal session into a flow variable. |
| [Move cursor on terminal session](modules/terminalemulation.md#move-cursor-on-terminal-session) | Terminal emulation | Moves cursor on terminal session. |
| [Open terminal session](modules/terminalemulation.md#open-terminal-session) | Terminal emulation | Opens terminal session. |
| [Search for text on terminal session](modules/terminalemulation.md#search-for-text-on-terminal-session) | Terminal emulation | Runs **Search for text on terminal session** from the actions pane. |
| [Send key to terminal session](modules/terminalemulation.md#send-key-to-terminal-session) | Terminal emulation | Sends key to terminal session. |
| [Set text on terminal session](modules/terminalemulation.md#set-text-on-terminal-session) | Terminal emulation | Writes text on terminal session. |
| [Wait for text on terminal session](modules/terminalemulation.md#wait-for-text-on-terminal-session) | Terminal emulation | Pauses the flow until text on terminal session. |
| [Assert](modules/testing.md#assert) | Testing | Fails a test when an expression is not true. |
| [Test a desktop flow](modules/testing.md#test-a-desktop-flow) | Testing | Test a desktop flow that receives input variables and might produce output variables. |
| [Append line to text](modules/text.md#append-line-to-text) | Text | Appends a new line of text to a text value. |
| [Change text case](modules/text.md#change-text-case) | Text | Changes the casing of a text to uppercase, lowercase, title case or sentence case. |
| [Convert datetime to text](modules/text.md#convert-datetime-to-text) | Text | Converts datetime to text. |
| [Convert number to text](modules/text.md#convert-number-to-text) | Text | Converts number to text. |
| [Convert text to datetime](modules/text.md#convert-text-to-datetime) | Text | Converts text to datetime. |
| [Convert text to number](modules/text.md#convert-text-to-number) | Text | Converts text to number. |
| [Create HTML content](modules/text.md#create-html-content) | Text | Creates HTML content. |
| [Create random text](modules/text.md#create-random-text) | Text | Creates random text. |
| [Crop text](modules/text.md#crop-text) | Text | Retrieves a text value that occurs before, after or between the specified text flag(s) in a given text. |
| [Escape text for regular expression](modules/text.md#escape-text-for-regular-expression) | Text | Escapes a minimal set of characters (\, *, +, ?, \|, {, , (,), ^, $,., #, and white space) by replacing them with their escape codes. |
| [Get subtext](modules/text.md#get-subtext) | Text | Reads subtext into a flow variable. |
| [Join text](modules/text.md#join-text) | Text | Joins text. |
| [Pad text](modules/text.md#pad-text) | Text | Pads text. |
| [Parse text](modules/text.md#parse-text) | Text | Parses text. |
| [Recognize entities in text](modules/text.md#recognize-entities-in-text) | Text | Recognizes entities in text, such as numbers, units, data/time and others expressed in natural language across multiple languages. |
| [Replace text](modules/text.md#replace-text) | Text | Replaces text. |
| [Reverse text](modules/text.md#reverse-text) | Text | Reverses the order of letters in a text string. |
| [Split text](modules/text.md#split-text) | Text | Splits text. |
| [Trim text](modules/text.md#trim-text) | Text | Trims text. |
| [UI element event trigger](modules/triggers.md#ui-element-event-trigger) | Triggers | Pauses the flow until a mouse click or key event occurs on a chosen UI element, then runs the nested actions. |
| [Click UI element in window](modules/uiautomation.md#click-ui-element-in-window) | UI automation | Clicks UI element in window. |
| [Close window](modules/uiautomation.md#close-window) | UI automation | Closes window. |
| [Drag and drop UI element in window](modules/uiautomation.md#drag-and-drop-ui-element-in-window) | UI automation | Drags and drops UI element in window. |
| [Expand/collapse tree node in window](modules/uiautomation.md#expand-collapse-tree-node-in-window) | UI automation | Expands or collapses tree node in window. |
| [Extract data from table](modules/uiautomation.md#extract-data-from-table) | UI automation | Extracts data from table. |
| [Extract data from window](modules/uiautomation.md#extract-data-from-window) | UI automation | Extracts data from window. |
| [Focus text field in window](modules/uiautomation.md#focus-text-field-in-window) | UI automation | Gives focus to text field in window. |
| [Focus window](modules/uiautomation.md#focus-window) | UI automation | Gives focus to window. |
| [Get details of a UI element in window](modules/uiautomation.md#get-details-of-a-ui-element-in-window) | UI automation | Reads details of a UI element in window into a flow variable. |
| [Get details of window](modules/uiautomation.md#get-details-of-window) | UI automation | Reads details of window into a flow variable. |
| [Get selected checkboxes in window](modules/uiautomation.md#get-selected-checkboxes-in-window) | UI automation | Reads selected checkboxes in window into a flow variable. |
| [Get selected radio button in window](modules/uiautomation.md#get-selected-radio-button-in-window) | UI automation | Reads selected radio button in window into a flow variable. |
| [Get window](modules/uiautomation.md#get-window) | UI automation | Reads window into a flow variable. |
| [Hover mouse over UI element in window](modules/uiautomation.md#hover-mouse-over-ui-element-in-window) | UI automation | Hovers mouse over UI element in window. |
| [If image](modules/uiautomation.md#if-image) | UI automation | Opens a conditional branch that runs when image. |
| [If window](modules/uiautomation.md#if-window) | UI automation | Opens a conditional branch that runs when window. |
| [If window contains](modules/uiautomation.md#if-window-contains) | UI automation | Opens a conditional branch that runs when window contains. |
| [Move window](modules/uiautomation.md#move-window) | UI automation | Moves window. |
| [Populate text field in window](modules/uiautomation.md#populate-text-field-in-window) | UI automation | Types or fills text field in window. |
| [Press button in window](modules/uiautomation.md#press-button-in-window) | UI automation | Presses button in window. |
| [Resize window](modules/uiautomation.md#resize-window) | UI automation | Sets the size of a specific window. |
| [Select menu option in window](modules/uiautomation.md#select-menu-option-in-window) | UI automation | Selects menu option in window. |
| [Select radio button in window](modules/uiautomation.md#select-radio-button-in-window) | UI automation | Selects radio button in window. |
| [Select tab in window](modules/uiautomation.md#select-tab-in-window) | UI automation | Selects tab in window. |
| [Set checkbox state in window](modules/uiautomation.md#set-checkbox-state-in-window) | UI automation | Writes checkbox state in window. |
| [Set drop-down list value in window](modules/uiautomation.md#set-drop-down-list-value-in-window) | UI automation | Writes drop-down list value in window. |
| [Set window state](modules/uiautomation.md#set-window-state) | UI automation | Writes window state. |
| [Set window visibility](modules/uiautomation.md#set-window-visibility) | UI automation | Writes window visibility. |
| [Take screenshot of UI element](modules/uiautomation.md#take-screenshot-of-ui-element) | UI automation | Captures screenshot of UI element. |
| [Use desktop](modules/uiautomation.md#use-desktop) | UI automation | Performs desktop and taskbar related operations. |
| [Wait for image](modules/uiautomation.md#wait-for-image) | UI automation | Pauses the flow until image. |
| [Wait for window](modules/uiautomation.md#wait-for-window) | UI automation | Pauses the flow until window. |
| [Wait for window content](modules/uiautomation.md#wait-for-window-content) | UI automation | Pauses the flow until window content. |
| [Add item to list](modules/variables.md#add-item-to-list) | Variables | Adds item to list. |
| [Clear data table](modules/variables.md#clear-data-table) | Variables | Clears data table. |
| [Clear list](modules/variables.md#clear-list) | Variables | Clears list. |
| [Convert custom object to JSON](modules/variables.md#convert-custom-object-to-json) | Variables | Converts custom object to JSON. |
| [Convert data table to text](modules/variables.md#convert-data-table-to-text) | Variables | Converts data table to text. |
| [Convert JSON to custom object](modules/variables.md#convert-json-to-custom-object) | Variables | Converts JSON to custom object. |
| [Create new data table](modules/variables.md#create-new-data-table) | Variables | Creates new data table. |
| [Create new list](modules/variables.md#create-new-list) | Variables | Creates new list. |
| [Decrease variable](modules/variables.md#decrease-variable) | Variables | Subtracts a number from a numeric variable. |
| [Delete column from data table](modules/variables.md#delete-column-from-data-table) | Variables | Deletes column from data table. |
| [Delete duplicate rows from data table](modules/variables.md#delete-duplicate-rows-from-data-table) | Variables | Deletes duplicate rows from data table. |
| [Delete empty rows from data table](modules/variables.md#delete-empty-rows-from-data-table) | Variables | Deletes empty rows from data table. |
| [Delete row from data table](modules/variables.md#delete-row-from-data-table) | Variables | Deletes row from data table. |
| [Filter data table](modules/variables.md#filter-data-table) | Variables | Filters data table. |
| [Find common list items](modules/variables.md#find-common-list-items) | Variables | Finds common list items. |
| [Find or replace in data table](modules/variables.md#find-or-replace-in-data-table) | Variables | Finds or replace in data table. |
| [Generate random number](modules/variables.md#generate-random-number) | Variables | Generate a random number or a list of random numbers that fall between a minimum and maximum value. |
| [Increase variable](modules/variables.md#increase-variable) | Variables | Adds a number to a numeric variable. |
| [Insert column into data table](modules/variables.md#insert-column-into-data-table) | Variables | Inserts column into data table. |
| [Insert row into data table](modules/variables.md#insert-row-into-data-table) | Variables | Inserts row into data table. |
| [Join data tables](modules/variables.md#join-data-tables) | Variables | Joins data tables. |
| [Merge data tables](modules/variables.md#merge-data-tables) | Variables | Merges data tables. |
| [Merge lists](modules/variables.md#merge-lists) | Variables | Merges lists. |
| [Read from CSV text variable](modules/variables.md#read-from-csv-text-variable) | Variables | Reads from CSV text variable. |
| [Remove duplicate items from list](modules/variables.md#remove-duplicate-items-from-list) | Variables | Removes duplicate items from list. |
| [Remove item from list](modules/variables.md#remove-item-from-list) | Variables | Removes item from list. |
| [Retrieve data table column into list](modules/variables.md#retrieve-data-table-column-into-list) | Variables | Retrieves data table column into list. |
| [Reverse list](modules/variables.md#reverse-list) | Variables | Reverse the order of the items of a list. |
| [Run Power Fx expression](modules/variables.md#run-power-fx-expression) | Variables | Runs power Fx expression. |
| [Set variable](modules/variables.md#set-variable) | Variables | Writes variable. |
| [Shuffle list](modules/variables.md#shuffle-list) | Variables | Create a random permutation of a list. |
| [Sort data table](modules/variables.md#sort-data-table) | Variables | Sorts data table. |
| [Sort list](modules/variables.md#sort-list) | Variables | Sorts list. |
| [Subtract lists](modules/variables.md#subtract-lists) | Variables | Compare two lists and create a new list with the items that are in the first list but not in the second. |
| [Truncate number](modules/variables.md#truncate-number) | Variables | Get the integral or fractional digits of a numeric value, or round up the value to a specified number of decimal places. |
| [Update data table item](modules/variables.md#update-data-table-item) | Variables | Updates data table item. |
| [Download from web](modules/web.md#download-from-web) | HTTP | Downloads from web. |
| [Invoke SOAP web service](modules/web.md#invoke-soap-web-service) | HTTP | Calls SOAP web service. |
| [Invoke web service](modules/web.md#invoke-web-service) | HTTP | Calls web service. |
| [Click download link on web page](modules/webautomation.md#click-download-link-on-web-page) | Browser automation | Clicks download link on web page. |
| [Click link on web page](modules/webautomation.md#click-link-on-web-page) | Browser automation | Clicks link on web page. |
| [Close web browser](modules/webautomation.md#close-web-browser) | Browser automation | Closes web browser. |
| [Create new tab](modules/webautomation.md#create-new-tab) | Browser automation | Creates new tab. |
| [Extract data from web page](modules/webautomation.md#extract-data-from-web-page) | Browser automation | Extracts data from web page. |
| [Focus text field on web page](modules/webautomation.md#focus-text-field-on-web-page) | Browser automation | Gives focus to text field on web page. |
| [Get details of element on web page](modules/webautomation.md#get-details-of-element-on-web-page) | Browser automation | Reads details of element on web page into a flow variable. |
| [Get details of web page](modules/webautomation.md#get-details-of-web-page) | Browser automation | Reads details of web page into a flow variable. |
| [Go to web page](modules/webautomation.md#go-to-web-page) | Browser automation | Navigates to web page. |
| [Hover mouse over element on web page](modules/webautomation.md#hover-mouse-over-element-on-web-page) | Browser automation | Hovers mouse over element on web page. |
| [If web page contains](modules/webautomation.md#if-web-page-contains) | Browser automation | Opens a conditional branch that runs when web page contains. |
| [Launch new Chrome](modules/webautomation.md#launch-new-chrome) | Browser automation | Starts new Chrome and returns an instance later actions can reuse. |
| [Launch new Firefox](modules/webautomation.md#launch-new-firefox) | Browser automation | Starts new Firefox and returns an instance later actions can reuse. |
| [Launch new Internet Explorer](modules/webautomation.md#launch-new-internet-explorer) | Browser automation | Starts new Internet Explorer and returns an instance later actions can reuse. |
| [Launch new Microsoft Edge](modules/webautomation.md#launch-new-microsoft-edge) | Browser automation | Starts new Microsoft Edge and returns an instance later actions can reuse. |
| [Populate text field on web page](modules/webautomation.md#populate-text-field-on-web-page) | Browser automation | Types or fills text field on web page. |
| [Press button on web page](modules/webautomation.md#press-button-on-web-page) | Browser automation | Presses button on web page. |
| [Run JavaScript function on web page](modules/webautomation.md#run-javascript-function-on-web-page) | Browser automation | Runs javaScript function on web page. |
| [Select radio button on web page](modules/webautomation.md#select-radio-button-on-web-page) | Browser automation | Selects radio button on web page. |
| [Set check box state on web page](modules/webautomation.md#set-check-box-state-on-web-page) | Browser automation | Writes check box state on web page. |
| [Set drop-down list value on web page](modules/webautomation.md#set-drop-down-list-value-on-web-page) | Browser automation | Writes drop-down list value on web page. |
| [Take screenshot of web page](modules/webautomation.md#take-screenshot-of-web-page) | Browser automation | Captures screenshot of web page. |
| [Wait for web page content](modules/webautomation.md#wait-for-web-page-content) | Browser automation | Pauses the flow until web page content. |
| [Attach to running Word](modules/word.md#attach-to-running-word) | Word | Connects the flow to running Word that is already running. |
| [Close Word](modules/word.md#close-word) | Word | Closes word. |
| [Find and replace words in Word document](modules/word.md#find-and-replace-words-in-word-document) | Word | Finds and replace words in Word document. |
| [Insert image in Word document](modules/word.md#insert-image-in-word-document) | Word | Inserts image in Word document. |
| [Launch Word](modules/word.md#launch-word) | Word | Starts Word and returns an instance later actions can reuse. |
| [Read from Word document](modules/word.md#read-from-word-document) | Word | Reads from Word document. |
| [Save Word](modules/word.md#save-word) | Word | Saves word. |
| [Write to Word document](modules/word.md#write-to-word-document) | Word | Writes to Word document. |
| [Add multiple work queue items](modules/workqueues.md#add-multiple-work-queue-items) | Work queues | Adds multiple work queue items. |
| [Add work queue item](modules/workqueues.md#add-work-queue-item) | Work queues | Adds work queue item. |
| [Get work queue items by filter](modules/workqueues.md#get-work-queue-items-by-filter) | Work queues | Reads work queue items by filter into a flow variable. |
| [Process work queue items](modules/workqueues.md#process-work-queue-items) | Work queues | Processes work queue items. |
| [Requeue item with delay](modules/workqueues.md#requeue-item-with-delay) | Work queues | The **Requeue item with delay** action allows users to readd a queue item being processed in the desktop flow, back into its originating queue. |
| [Control screen saver](modules/workstation.md#control-screen-saver) | Workstation | Enables, disables, starts or stops the screensaver. |
| [Empty recycle bin](modules/workstation.md#empty-recycle-bin) | Workstation | Deletes all files from the windows recycle bin. |
| [Get default printer](modules/workstation.md#get-default-printer) | Workstation | Reads default printer into a flow variable. |
| [Get screen resolution](modules/workstation.md#get-screen-resolution) | Workstation | Reads screen resolution into a flow variable. |
| [Lock workstation](modules/workstation.md#lock-workstation) | Workstation | Locks the workstation's display to protect it from unauthorized use. |
| [Log off user](modules/workstation.md#log-off-user) | Workstation | Logs off the current user. |
| [Play sound](modules/workstation.md#play-sound) | Workstation | Plays a system sound or a wav file. |
| [Print document](modules/workstation.md#print-document) | Workstation | Prints a document on the default printer. |
| [Set default printer](modules/workstation.md#set-default-printer) | Workstation | Writes default printer. |
| [Set screen resolution](modules/workstation.md#set-screen-resolution) | Workstation | Writes screen resolution. |
| [Show desktop](modules/workstation.md#show-desktop) | Workstation | Shows the desktop. |
| [Shutdown computer](modules/workstation.md#shutdown-computer) | Workstation | Instructs the computer to shut down. |
| [Take screenshot](modules/workstation.md#take-screenshot) | Workstation | Captures screenshot. |
| [Execute XPath expression](modules/xml.md#execute-xpath-expression) | XML | Extract values from an XML document based on the provided XPath query. |
| [Get XML element attribute](modules/xml.md#get-xml-element-attribute) | XML | Reads XML element attribute into a flow variable. |
| [Get XML element value](modules/xml.md#get-xml-element-value) | XML | Reads XML element value into a flow variable. |
| [Insert XML element](modules/xml.md#insert-xml-element) | XML | Inserts XML element. |
| [Read XML from file](modules/xml.md#read-xml-from-file) | XML | Reads XML from file. |
| [Remove XML element](modules/xml.md#remove-xml-element) | XML | Removes XML element. |
| [Remove XML element attribute](modules/xml.md#remove-xml-element-attribute) | XML | Removes XML element attribute. |
| [Set XML element attribute](modules/xml.md#set-xml-element-attribute) | XML | Writes XML element attribute. |
| [Set XML element value](modules/xml.md#set-xml-element-value) | XML | Writes XML element value. |
| [Write XML to file](modules/xml.md#write-xml-to-file) | XML | Writes XML to file. |

## Default cloud connectors

| Operation | Connector | Purpose |
| --- | --- | --- |
| [Add a key column to a table](modules/excel-online.md#add-a-key-column-to-a-table) | Excel Online (Business) (cloud connector) | Adds a key column to a table. |
| [Add a row into a table](modules/excel-online.md#add-a-row-into-a-table) | Excel Online (Business) (cloud connector) | Adds a row into a table. |
| [Create table](modules/excel-online.md#create-table) | Excel Online (Business) (cloud connector) | Creates table. |
| [Create worksheet](modules/excel-online.md#create-worksheet) | Excel Online (Business) (cloud connector) | Creates worksheet. |
| [Delete a row](modules/excel-online.md#delete-a-row) | Excel Online (Business) (cloud connector) | Deletes a row. |
| [Get a row](modules/excel-online.md#get-a-row) | Excel Online (Business) (cloud connector) | Reads a row into a flow variable. |
| [Get tables](modules/excel-online.md#get-tables) | Excel Online (Business) (cloud connector) | Reads tables into a flow variable. |
| [Get worksheets](modules/excel-online.md#get-worksheets) | Excel Online (Business) (cloud connector) | Reads worksheets into a flow variable. |
| [List rows present in a table](modules/excel-online.md#list-rows-present-in-a-table) | Excel Online (Business) (cloud connector) | Lists rows present in a table. |
| [Run script](modules/excel-online.md#run-script) | Excel Online (Business) (cloud connector) | Runs script. |
| [Run script from SharePoint library](modules/excel-online.md#run-script-from-sharepoint-library) | Excel Online (Business) (cloud connector) | Runs script from SharePoint library. |
| [Update a row](modules/excel-online.md#update-a-row) | Excel Online (Business) (cloud connector) | Updates a row. |
| [Add a new row to selected environment](modules/microsoft-dataverse.md#add-a-new-row-to-selected-environment) | Microsoft Dataverse (cloud connector) | Adds a new row to selected environment. |
| [Delete a row from selected environment](modules/microsoft-dataverse.md#delete-a-row-from-selected-environment) | Microsoft Dataverse (cloud connector) | Deletes a row from selected environment. |
| [Download a file or an image from selected environment](modules/microsoft-dataverse.md#download-a-file-or-an-image-from-selected-environment) | Microsoft Dataverse (cloud connector) | Downloads a file or an image from selected environment. |
| [Get a row by ID from selected environment](modules/microsoft-dataverse.md#get-a-row-by-id-from-selected-environment) | Microsoft Dataverse (cloud connector) | Reads a row by ID from selected environment into a flow variable. |
| [List rows from selected environment](modules/microsoft-dataverse.md#list-rows-from-selected-environment) | Microsoft Dataverse (cloud connector) | Lists rows from selected environment. |
| [Perform a bound action in selected environment](modules/microsoft-dataverse.md#perform-a-bound-action-in-selected-environment) | Microsoft Dataverse (cloud connector) | Runs **Perform a bound action in selected environment** from the actions pane. |
| [Perform an unbound action in selected environment](modules/microsoft-dataverse.md#perform-an-unbound-action-in-selected-environment) | Microsoft Dataverse (cloud connector) | Runs **Perform an unbound action in selected environment** from the actions pane. |
| [Relate rows in selected environment](modules/microsoft-dataverse.md#relate-rows-in-selected-environment) | Microsoft Dataverse (cloud connector) | Runs **Relate rows in selected environment** from the actions pane. |
| [Unrelate rows in selected environment](modules/microsoft-dataverse.md#unrelate-rows-in-selected-environment) | Microsoft Dataverse (cloud connector) | Runs **Unrelate rows in selected environment** from the actions pane. |
| [Upload a file or an image to selected environment](modules/microsoft-dataverse.md#upload-a-file-or-an-image-to-selected-environment) | Microsoft Dataverse (cloud connector) | Uploads a file or an image to selected environment. |
| [Upsert a row in selected environment](modules/microsoft-dataverse.md#upsert-a-row-in-selected-environment) | Microsoft Dataverse (cloud connector) | Runs **Upsert a row in selected environment** from the actions pane. |
| [Get response details](modules/microsoft-forms.md#get-response-details) | Microsoft Forms (cloud connector) | Reads response details into a flow variable. |
| [Add a member to a tag](modules/microsoft-teams.md#add-a-member-to-a-tag) | Microsoft Teams (cloud connector) | Adds a member to a tag. |
| [Add a member to a team](modules/microsoft-teams.md#add-a-member-to-a-team) | Microsoft Teams (cloud connector) | Adds a member to a team. |
| [Create a channel](modules/microsoft-teams.md#create-a-channel) | Microsoft Teams (cloud connector) | Creates a channel. |
| [Create a chat](modules/microsoft-teams.md#create-a-chat) | Microsoft Teams (cloud connector) | Creates a chat. |
| [Create a tag for a team](modules/microsoft-teams.md#create-a-tag-for-a-team) | Microsoft Teams (cloud connector) | Creates a tag for a team. |
| [Create a team](modules/microsoft-teams.md#create-a-team) | Microsoft Teams (cloud connector) | Creates a team. |
| [Create a Teams meeting](modules/microsoft-teams.md#create-a-teams-meeting) | Microsoft Teams (cloud connector) | Creates a Teams meeting. |
| [Delete a member from a tag](modules/microsoft-teams.md#delete-a-member-from-a-tag) | Microsoft Teams (cloud connector) | Deletes a member from a tag. |
| [Delete a tag](modules/microsoft-teams.md#delete-a-tag) | Microsoft Teams (cloud connector) | Deletes a tag. |
| [Get a team](modules/microsoft-teams.md#get-a-team) | Microsoft Teams (cloud connector) | Reads a team into a flow variable. |
| [Get an @mention token for a tag](modules/microsoft-teams.md#get-an-mention-token-for-a-tag) | Microsoft Teams (cloud connector) | Reads an @mention token for a tag into a flow variable. |
| [Get an @mention token for a user](modules/microsoft-teams.md#get-an-mention-token-for-a-user) | Microsoft Teams (cloud connector) | Reads an @mention token for a user into a flow variable. |
| [Get message details](modules/microsoft-teams.md#get-message-details) | Microsoft Teams (cloud connector) | Reads message details into a flow variable. |
| [Get messages](modules/microsoft-teams.md#get-messages) | Microsoft Teams (cloud connector) | Reads messages into a flow variable. |
| [List all tags for a team](modules/microsoft-teams.md#list-all-tags-for-a-team) | Microsoft Teams (cloud connector) | Lists all tags for a team. |
| [List channels](modules/microsoft-teams.md#list-channels) | Microsoft Teams (cloud connector) | Lists channels. |
| [List chats](modules/microsoft-teams.md#list-chats) | Microsoft Teams (cloud connector) | Lists chats. |
| [List members](modules/microsoft-teams.md#list-members) | Microsoft Teams (cloud connector) | Lists members. |
| [List teams](modules/microsoft-teams.md#list-teams) | Microsoft Teams (cloud connector) | Lists teams. |
| [List the members for a tag](modules/microsoft-teams.md#list-the-members-for-a-tag) | Microsoft Teams (cloud connector) | Lists the members for a tag. |
| [Post a feed notification](modules/microsoft-teams.md#post-a-feed-notification) | Microsoft Teams (cloud connector) | Runs **Post a feed notification** from the actions pane. |
| [Post card in a chat or channel](modules/microsoft-teams.md#post-card-in-a-chat-or-channel) | Microsoft Teams (cloud connector) | Runs **Post card in a chat or channel** from the actions pane. |
| [Post message in a chat or channel](modules/microsoft-teams.md#post-message-in-a-chat-or-channel) | Microsoft Teams (cloud connector) | Runs **Post message in a chat or channel** from the actions pane. |
| [Reply with a message in a channel](modules/microsoft-teams.md#reply-with-a-message-in-a-channel) | Microsoft Teams (cloud connector) | Runs **Reply with a message in a channel** from the actions pane. |
| [Reply with adaptive card in a channel](modules/microsoft-teams.md#reply-with-adaptive-card-in-a-channel) | Microsoft Teams (cloud connector) | Runs **Reply with adaptive card in a channel** from the actions pane. |
| [Send a Microsoft Graph HTTP request](modules/microsoft-teams.md#send-a-microsoft-graph-http-request) | Microsoft Teams (cloud connector) | Sends a Microsoft Graph HTTP request. |
| [Update an adaptive card in a chat or channel](modules/microsoft-teams.md#update-an-adaptive-card-in-a-chat-or-channel) | Microsoft Teams (cloud connector) | Updates an adaptive card in a chat or channel. |
| [Create contact (V2)](modules/office365outlook.md#create-contact-v2) | Office 365 Outlook (cloud connector) | Creates contact (V2). |
| [Create event (V4)](modules/office365outlook.md#create-event-v4) | Office 365 Outlook (cloud connector) | Creates event (V4). |
| [Delete contact (V2)](modules/office365outlook.md#delete-contact-v2) | Office 365 Outlook (cloud connector) | Deletes contact (V2). |
| [Delete email (V2)](modules/office365outlook.md#delete-email-v2) | Office 365 Outlook (cloud connector) | Deletes email (V2). |
| [Delete event (V2)](modules/office365outlook.md#delete-event-v2) | Office 365 Outlook (cloud connector) | Deletes event (V2). |
| [Export email (V2)](modules/office365outlook.md#export-email-v2) | Office 365 Outlook (cloud connector) | Runs **Export email (V2)** from the actions pane. |
| [Find meeting times (V2)](modules/office365outlook.md#find-meeting-times-v2) | Office 365 Outlook (cloud connector) | Finds meeting times (V2). |
| [Flag email (V2)](modules/office365outlook.md#flag-email-v2) | Office 365 Outlook (cloud connector) | Runs **Flag email (V2)** from the actions pane. |
| [Forward an email (V2)](modules/office365outlook.md#forward-an-email-v2) | Office 365 Outlook (cloud connector) | Runs **Forward an email (V2)** from the actions pane. |
| [Get Attachment (V2)](modules/office365outlook.md#get-attachment-v2) | Office 365 Outlook (cloud connector) | Reads attachment (V2) into a flow variable. |
| [Get calendar view of events (V3)](modules/office365outlook.md#get-calendar-view-of-events-v3) | Office 365 Outlook (cloud connector) | Reads calendar view of events (V3) into a flow variable. |
| [Get calendars (V2)](modules/office365outlook.md#get-calendars-v2) | Office 365 Outlook (cloud connector) | Reads calendars (V2) into a flow variable. |
| [Get contact (V2)](modules/office365outlook.md#get-contact-v2) | Office 365 Outlook (cloud connector) | Reads contact (V2) into a flow variable. |
| [Get contacts (V2)](modules/office365outlook.md#get-contacts-v2) | Office 365 Outlook (cloud connector) | Reads contacts (V2) into a flow variable. |
| [Get email (V2)](modules/office365outlook.md#get-email-v2) | Office 365 Outlook (cloud connector) | Reads email (V2) into a flow variable. |
| [Get emails (V3)](modules/office365outlook.md#get-emails-v3) | Office 365 Outlook (cloud connector) | Reads emails (V3) into a flow variable. |
| [Get event (V3)](modules/office365outlook.md#get-event-v3) | Office 365 Outlook (cloud connector) | Reads event (V3) into a flow variable. |
| [Get events (V4)](modules/office365outlook.md#get-events-v4) | Office 365 Outlook (cloud connector) | Reads events (V4) into a flow variable. |
| [Get room lists (V2)](modules/office365outlook.md#get-room-lists-v2) | Office 365 Outlook (cloud connector) | Reads room lists (V2) into a flow variable. |
| [Get rooms (V2)](modules/office365outlook.md#get-rooms-v2) | Office 365 Outlook (cloud connector) | Reads rooms (V2) into a flow variable. |
| [Get rooms in room list (V2)](modules/office365outlook.md#get-rooms-in-room-list-v2) | Office 365 Outlook (cloud connector) | Reads rooms in room list (V2) into a flow variable. |
| [Mark as read or unread (V3)](modules/office365outlook.md#mark-as-read-or-unread-v3) | Office 365 Outlook (cloud connector) | Runs **Mark as read or unread (V3)** from the actions pane. |
| [Move email (V2)](modules/office365outlook.md#move-email-v2) | Office 365 Outlook (cloud connector) | Moves email (V2). |
| [Reply to email (V3)](modules/office365outlook.md#reply-to-email-v3) | Office 365 Outlook (cloud connector) | Runs **Reply to email (V3)** from the actions pane. |
| [Respond to an event invite (V2)](modules/office365outlook.md#respond-to-an-event-invite-v2) | Office 365 Outlook (cloud connector) | Runs **Respond to an event invite (V2)** from the actions pane. |
| [Send an email (V2)](modules/office365outlook.md#send-an-email-v2) | Office 365 Outlook (cloud connector) | Sends an email (V2). |
| [Send an email from a shared mailbox (V2)](modules/office365outlook.md#send-an-email-from-a-shared-mailbox-v2) | Office 365 Outlook (cloud connector) | Sends an email from a shared mailbox (V2). |
| [Send an HTTP request](modules/office365outlook.md#send-an-http-request) | Office 365 Outlook (cloud connector) | Sends an HTTP request. |
| [Set up automatic replies (V2)](modules/office365outlook.md#set-up-automatic-replies-v2) | Office 365 Outlook (cloud connector) | Writes up automatic replies (V2). |
| [Update contact (V2)](modules/office365outlook.md#update-contact-v2) | Office 365 Outlook (cloud connector) | Updates contact (V2). |
| [Update event (V4)](modules/office365outlook.md#update-event-v4) | Office 365 Outlook (cloud connector) | Updates event (V4). |
| [Add file tag](modules/onedrive.md#add-file-tag) | OneDrive (cloud connector) | Adds file tag. |
| [Convert file](modules/onedrive.md#convert-file) | OneDrive (cloud connector) | Converts file. |
| [Convert file using path](modules/onedrive.md#convert-file-using-path) | OneDrive (cloud connector) | Converts file using path. |
| [Copy file](modules/onedrive.md#copy-file) | OneDrive (cloud connector) | Copies file. |
| [Copy file using path](modules/onedrive.md#copy-file-using-path) | OneDrive (cloud connector) | Copies file using path. |
| [Create file](modules/onedrive.md#create-file) | OneDrive (cloud connector) | Creates file. |
| [Create share link](modules/onedrive.md#create-share-link) | OneDrive (cloud connector) | Creates share link. |
| [Create share link by path](modules/onedrive.md#create-share-link-by-path) | OneDrive (cloud connector) | Creates share link by path. |
| [Delete file](modules/onedrive.md#delete-file) | OneDrive (cloud connector) | Deletes file. |
| [Extract archive to folder](modules/onedrive.md#extract-archive-to-folder) | OneDrive (cloud connector) | Extracts archive to folder. |
| [Find files in folder](modules/onedrive.md#find-files-in-folder) | OneDrive (cloud connector) | Finds files in folder. |
| [Find files in folder by path](modules/onedrive.md#find-files-in-folder-by-path) | OneDrive (cloud connector) | Finds files in folder by path. |
| [Get file content](modules/onedrive.md#get-file-content) | OneDrive (cloud connector) | Reads file content into a flow variable. |
| [Get file content using path](modules/onedrive.md#get-file-content-using-path) | OneDrive (cloud connector) | Reads file content using path into a flow variable. |
| [Get file metadata](modules/onedrive.md#get-file-metadata) | OneDrive (cloud connector) | Reads file metadata into a flow variable. |
| [Get file metadata using path](modules/onedrive.md#get-file-metadata-using-path) | OneDrive (cloud connector) | Reads file metadata using path into a flow variable. |
| [Get file tags](modules/onedrive.md#get-file-tags) | OneDrive (cloud connector) | Reads file tags into a flow variable. |
| [Get file thumbnail](modules/onedrive.md#get-file-thumbnail) | OneDrive (cloud connector) | Reads file thumbnail into a flow variable. |
| [List files in folder](modules/onedrive.md#list-files-in-folder) | OneDrive (cloud connector) | Lists files in folder. |
| [List files in root folder](modules/onedrive.md#list-files-in-root-folder) | OneDrive (cloud connector) | Lists files in root folder. |
| [Move or rename a file](modules/onedrive.md#move-or-rename-a-file) | OneDrive (cloud connector) | Moves or rename a file. |
| [Move or rename a file using path](modules/onedrive.md#move-or-rename-a-file-using-path) | OneDrive (cloud connector) | Moves or rename a file using path. |
| [Remove file tag](modules/onedrive.md#remove-file-tag) | OneDrive (cloud connector) | Removes file tag. |
| [Update file](modules/onedrive.md#update-file) | OneDrive (cloud connector) | Updates file. |
| [Upload file from URL](modules/onedrive.md#upload-file-from-url) | OneDrive (cloud connector) | Uploads file from URL. |
| [Convert file](modules/onedrive-business.md#convert-file) | OneDrive for work or school (cloud connector) | Converts file. |
| [Convert file using path](modules/onedrive-business.md#convert-file-using-path) | OneDrive for work or school (cloud connector) | Converts file using path. |
| [Copy file](modules/onedrive-business.md#copy-file) | OneDrive for work or school (cloud connector) | Copies file. |
| [Copy file using path](modules/onedrive-business.md#copy-file-using-path) | OneDrive for work or school (cloud connector) | Copies file using path. |
| [Create file](modules/onedrive-business.md#create-file) | OneDrive for work or school (cloud connector) | Creates file. |
| [Create share link](modules/onedrive-business.md#create-share-link) | OneDrive for work or school (cloud connector) | Creates share link. |
| [Create share link by path](modules/onedrive-business.md#create-share-link-by-path) | OneDrive for work or school (cloud connector) | Creates share link by path. |
| [Delete file](modules/onedrive-business.md#delete-file) | OneDrive for work or school (cloud connector) | Deletes file. |
| [Extract archive to folder](modules/onedrive-business.md#extract-archive-to-folder) | OneDrive for work or school (cloud connector) | Extracts archive to folder. |
| [Find files in folder](modules/onedrive-business.md#find-files-in-folder) | OneDrive for work or school (cloud connector) | Finds files in folder. |
| [Find files in folder by path](modules/onedrive-business.md#find-files-in-folder-by-path) | OneDrive for work or school (cloud connector) | Finds files in folder by path. |
| [Get file content](modules/onedrive-business.md#get-file-content) | OneDrive for work or school (cloud connector) | Reads file content into a flow variable. |
| [Get file content using path](modules/onedrive-business.md#get-file-content-using-path) | OneDrive for work or school (cloud connector) | Reads file content using path into a flow variable. |
| [Get file metadata](modules/onedrive-business.md#get-file-metadata) | OneDrive for work or school (cloud connector) | Reads file metadata into a flow variable. |
| [Get file metadata using path](modules/onedrive-business.md#get-file-metadata-using-path) | OneDrive for work or school (cloud connector) | Reads file metadata using path into a flow variable. |
| [Get file thumbnail](modules/onedrive-business.md#get-file-thumbnail) | OneDrive for work or school (cloud connector) | Reads file thumbnail into a flow variable. |
| [List files in folder](modules/onedrive-business.md#list-files-in-folder) | OneDrive for work or school (cloud connector) | Lists files in folder. |
| [List files in root folder](modules/onedrive-business.md#list-files-in-root-folder) | OneDrive for work or school (cloud connector) | Lists files in root folder. |
| [Move or rename a file](modules/onedrive-business.md#move-or-rename-a-file) | OneDrive for work or school (cloud connector) | Moves or rename a file. |
| [Move or rename a file using path](modules/onedrive-business.md#move-or-rename-a-file-using-path) | OneDrive for work or school (cloud connector) | Moves or rename a file using path. |
| [Update file](modules/onedrive-business.md#update-file) | OneDrive for work or school (cloud connector) | Updates file. |
| [Upload file from URL](modules/onedrive-business.md#upload-file-from-url) | OneDrive for work or school (cloud connector) | Uploads file from URL. |
| [Create a page in Quick Notes](modules/onenote.md#create-a-page-in-quick-notes) | OneNote (Business) (cloud connector) | Creates a page in Quick Notes. |
| [Create page in a section](modules/onenote.md#create-page-in-a-section) | OneNote (Business) (cloud connector) | Creates page in a section. |
| [Create section in a notebook](modules/onenote.md#create-section-in-a-notebook) | OneNote (Business) (cloud connector) | Creates section in a notebook. |
| [Delete a page](modules/onenote.md#delete-a-page) | OneNote (Business) (cloud connector) | Deletes a page. |
| [Get page content](modules/onenote.md#get-page-content) | OneNote (Business) (cloud connector) | Reads page content into a flow variable. |
| [Get pages for a specific section](modules/onenote.md#get-pages-for-a-specific-section) | OneNote (Business) (cloud connector) | Reads pages for a specific section into a flow variable. |
| [Get recent notebooks](modules/onenote.md#get-recent-notebooks) | OneNote (Business) (cloud connector) | Reads recent notebooks into a flow variable. |
| [Get sections in notebook](modules/onenote.md#get-sections-in-notebook) | OneNote (Business) (cloud connector) | Reads sections in notebook into a flow variable. |
| [Update page content](modules/onenote.md#update-page-content) | OneNote (Business) (cloud connector) | Updates page content. |
| [List all RSS feed items](modules/rss.md#list-all-rss-feed-items) | RSS (cloud connector) | Lists all RSS feed items. |
| [Add attachment](modules/sharepoint.md#add-attachment) | SharePoint (cloud connector) | Adds attachment. |
| [Check in file](modules/sharepoint.md#check-in-file) | SharePoint (cloud connector) | Runs **Check in file** from the actions pane. |
| [Check out file](modules/sharepoint.md#check-out-file) | SharePoint (cloud connector) | Runs **Check out file** from the actions pane. |
| [Copy file](modules/sharepoint.md#copy-file) | SharePoint (cloud connector) | Copies file. |
| [Copy folder](modules/sharepoint.md#copy-folder) | SharePoint (cloud connector) | Copies folder. |
| [Create file](modules/sharepoint.md#create-file) | SharePoint (cloud connector) | Creates file. |
| [Create item](modules/sharepoint.md#create-item) | SharePoint (cloud connector) | Creates item. |
| [Create new document set](modules/sharepoint.md#create-new-document-set) | SharePoint (cloud connector) | Creates new document set. |
| [Create new folder](modules/sharepoint.md#create-new-folder) | SharePoint (cloud connector) | Creates new folder. |
| [Create sharing link for a file or folder](modules/sharepoint.md#create-sharing-link-for-a-file-or-folder) | SharePoint (cloud connector) | Creates sharing link for a file or folder. |
| [Delete attachment](modules/sharepoint.md#delete-attachment) | SharePoint (cloud connector) | Deletes attachment. |
| [Delete file](modules/sharepoint.md#delete-file) | SharePoint (cloud connector) | Deletes file. |
| [Delete item](modules/sharepoint.md#delete-item) | SharePoint (cloud connector) | Deletes item. |
| [Discard check out](modules/sharepoint.md#discard-check-out) | SharePoint (cloud connector) | Runs **Discard check out** from the actions pane. |
| [Extract folder](modules/sharepoint.md#extract-folder) | SharePoint (cloud connector) | Extracts folder. |
| [Generate document using Microsoft Syntex](modules/sharepoint.md#generate-document-using-microsoft-syntex) | SharePoint (cloud connector) | Runs **Generate document using Microsoft Syntex** from the actions pane. |
| [Get all lists and libraries](modules/sharepoint.md#get-all-lists-and-libraries) | SharePoint (cloud connector) | Reads all lists and libraries into a flow variable. |
| [Get attachment content](modules/sharepoint.md#get-attachment-content) | SharePoint (cloud connector) | Reads attachment content into a flow variable. |
| [Get attachments](modules/sharepoint.md#get-attachments) | SharePoint (cloud connector) | Reads attachments into a flow variable. |
| [Get changes for an item or a file (properties only)](modules/sharepoint.md#get-changes-for-an-item-or-a-file-properties-only) | SharePoint (cloud connector) | Reads changes for an item or a file (properties only) into a flow variable. |
| [Get file content](modules/sharepoint.md#get-file-content) | SharePoint (cloud connector) | Reads file content into a flow variable. |
| [Get file content using path](modules/sharepoint.md#get-file-content-using-path) | SharePoint (cloud connector) | Reads file content using path into a flow variable. |
| [Get file metadata](modules/sharepoint.md#get-file-metadata) | SharePoint (cloud connector) | Reads file metadata into a flow variable. |
| [Get file metadata using path](modules/sharepoint.md#get-file-metadata-using-path) | SharePoint (cloud connector) | Reads file metadata using path into a flow variable. |
| [Get file properties](modules/sharepoint.md#get-file-properties) | SharePoint (cloud connector) | Reads file properties into a flow variable. |
| [Get files (properties only)](modules/sharepoint.md#get-files-properties-only) | SharePoint (cloud connector) | Reads files (properties only) into a flow variable. |
| [Get folder metadata](modules/sharepoint.md#get-folder-metadata) | SharePoint (cloud connector) | Reads folder metadata into a flow variable. |
| [Get folder metadata using path](modules/sharepoint.md#get-folder-metadata-using-path) | SharePoint (cloud connector) | Reads folder metadata using path into a flow variable. |
| [Get item](modules/sharepoint.md#get-item) | SharePoint (cloud connector) | Reads item into a flow variable. |
| [Get items](modules/sharepoint.md#get-items) | SharePoint (cloud connector) | Reads items into a flow variable. |
| [Get list views](modules/sharepoint.md#get-list-views) | SharePoint (cloud connector) | Reads list views into a flow variable. |
| [Get lists](modules/sharepoint.md#get-lists) | SharePoint (cloud connector) | Reads lists into a flow variable. |
| [Grant access to an item or a folder](modules/sharepoint.md#grant-access-to-an-item-or-a-folder) | SharePoint (cloud connector) | Runs **Grant access to an item or a folder** from the actions pane. |
| [List folder](modules/sharepoint.md#list-folder) | SharePoint (cloud connector) | Lists folder. |
| [List root folder](modules/sharepoint.md#list-root-folder) | SharePoint (cloud connector) | Lists root folder. |
| [Move file](modules/sharepoint.md#move-file) | SharePoint (cloud connector) | Moves file. |
| [Move folder](modules/sharepoint.md#move-folder) | SharePoint (cloud connector) | Moves folder. |
| [Send an HTTP request to SharePoint](modules/sharepoint.md#send-an-http-request-to-sharepoint) | SharePoint (cloud connector) | Sends an HTTP request to SharePoint. |
| [Set content approval status](modules/sharepoint.md#set-content-approval-status) | SharePoint (cloud connector) | Writes content approval status. |
| [Stop sharing an item or a file](modules/sharepoint.md#stop-sharing-an-item-or-a-file) | SharePoint (cloud connector) | Stops sharing an item or a file. |
| [Update file](modules/sharepoint.md#update-file) | SharePoint (cloud connector) | Updates file. |
| [Update file properties](modules/sharepoint.md#update-file-properties) | SharePoint (cloud connector) | Updates file properties. |
| [Update file properties using AI Builder model results](modules/sharepoint.md#update-file-properties-using-ai-builder-model-results) | SharePoint (cloud connector) | Updates file properties using AI Builder model results. |
| [Update item](modules/sharepoint.md#update-item) | SharePoint (cloud connector) | Updates item. |
| [Convert Word Document to PDF](modules/word-online.md#convert-word-document-to-pdf) | Word Online (Business) (cloud connector) | Converts word Document to PDF. |
| [Populate a Microsoft Word template](modules/word-online.md#populate-a-microsoft-word-template) | Word Online (Business) (cloud connector) | Types or fills a Microsoft Word template. |

## Power Fx functions

Used only in **Power Fx–enabled** desktop flows. Expressions start with `=`. Indexes are **1-based**. See [Power Fx functions](03-power-fx-functions.md).

| Function | Category | Purpose |
| --- | --- | --- |
| [Abs](03-power-fx-functions.md#abs) | Math | Distance of a number from zero. |
| [Acos](03-power-fx-functions.md#acos) | Math | Arccosine of a number, in radians. |
| [Acot](03-power-fx-functions.md#acot) | Math | Arccotangent of a number, in radians. |
| [AddColumns](03-power-fx-functions.md#addcolumns) | Table | Returns a table with extra calculated columns. |
| [And](03-power-fx-functions.md#and) | Logic | True only when every argument is true (`&&`). |
| [Asin](03-power-fx-functions.md#asin) | Math | Arcsine of a number, in radians. |
| [Atan](03-power-fx-functions.md#atan) | Math | Arctangent of a number, in radians. |
| [Atan2](03-power-fx-functions.md#atan2) | Math | Arctangent from an (x, y) pair, in radians. |
| [Average](03-power-fx-functions.md#average) | Math | Mean of a table expression or argument list. |
| [Blank](03-power-fx-functions.md#blank) | Utility | A blank/null value for data sources. |
| [Boolean](03-power-fx-functions.md#boolean) | Conversion | Coerce text, number, or dynamic data to true/false. |
| [Char](03-power-fx-functions.md#char) | Text | Character for a numeric code. |
| [Clear](03-power-fx-functions.md#clear) | Collection | Empty a collection. |
| [ClearCollect](03-power-fx-functions.md#clearcollect) | Collection | Empty a collection, then add records. |
| [Coalesce](03-power-fx-functions.md#coalesce) | Utility | First non-blank argument. |
| [Collect](03-power-fx-functions.md#collect) | Collection | Create a collection or append records. |
| [Concat](03-power-fx-functions.md#concat) | Text | Join strings produced from a table. |
| [Concatenate](03-power-fx-functions.md#concatenate) | Text | Join two or more strings. |
| [Cos](03-power-fx-functions.md#cos) | Math | Cosine of an angle in radians. |
| [Cot](03-power-fx-functions.md#cot) | Math | Cotangent of an angle in radians. |
| [Count](03-power-fx-functions.md#count) | Table | Count records that hold numbers. |
| [CountA](03-power-fx-functions.md#counta) | Table | Count records that are not empty. |
| [CountIf](03-power-fx-functions.md#countif) | Table | Count records that match a condition. |
| [CountRows](03-power-fx-functions.md#countrows) | Table | Count all records. |
| [Date](03-power-fx-functions.md#date) | Date | Build a date from year, month, and day. |
| [DateAdd](03-power-fx-functions.md#dateadd) | Date | Add days, months, quarters, or years. |
| [DateDiff](03-power-fx-functions.md#datediff) | Date | Difference between two dates in a chosen unit. |
| [DateTime](03-power-fx-functions.md#datetime) | Date | Build a date/time from date and time parts. |
| [DateTimeValue](03-power-fx-functions.md#datetimevalue) | Date | Parse a date-and-time string. |
| [DateValue](03-power-fx-functions.md#datevalue) | Date | Parse a date-only string. |
| [Day](03-power-fx-functions.md#day) | Date | Day-of-month from a date/time. |
| [Dec2Hex](03-power-fx-functions.md#dec2hex) | Conversion | Number to hexadecimal text. |
| [Decimal](03-power-fx-functions.md#decimal) | Conversion | Text to a decimal number. |
| [Degrees](03-power-fx-functions.md#degrees) | Math | Radians to degrees. |
| [Distinct](03-power-fx-functions.md#distinct) | Table | Unique records from a table. |
| [DropColumns](03-power-fx-functions.md#dropcolumns) | Table | Table without the named columns. |
| [EDate](03-power-fx-functions.md#edate) | Date | Add months without changing the day-of-month. |
| [EncodeHTML](03-power-fx-functions.md#encodehtml) | Text | Escape characters for HTML. |
| [EncodeUrl](03-power-fx-functions.md#encodeurl) | Text | Percent-encode a URL fragment. |
| [EndsWith](03-power-fx-functions.md#endswith) | Text | True when a string ends with another string. |
| [EOMonth](03-power-fx-functions.md#eomonth) | Date | Last day of a month after adding months. |
| [Error](03-power-fx-functions.md#error) | Logic | Raise or forward an error. |
| [Exp](03-power-fx-functions.md#exp) | Math | e raised to a power. |
| [Filter](03-power-fx-functions.md#filter) | Table | Rows that match one or more conditions. |
| [Find](03-power-fx-functions.md#find) | Text | Start position of one string inside another. |
| [First](03-power-fx-functions.md#first) | Table | First record. |
| [FirstN](03-power-fx-functions.md#firstn) | Table | First N records. |
| [Float](03-power-fx-functions.md#float) | Conversion | Text to a floating-point number. |
| [ForAll](03-power-fx-functions.md#forall) | Table | Evaluate a formula for every record. |
| [GUID](03-power-fx-functions.md#guid) | Utility | Parse or create a GUID. |
| [Hex2Dec](03-power-fx-functions.md#hex2dec) | Conversion | Hexadecimal text to a number. |
| [Hour](03-power-fx-functions.md#hour) | Date | Hour portion of a date/time. |
| [If](03-power-fx-functions.md#if) | Logic | Pick a result from a true/false test. |
| [IfError](03-power-fx-functions.md#iferror) | Logic | Fallback value or action when an error occurs. |
| [Index](03-power-fx-functions.md#index) | Table | Record at a 1-based position. |
| [Int](03-power-fx-functions.md#int) | Math | Round down to the nearest integer. |
| [IsBlank](03-power-fx-functions.md#isblank) | Logic | True when the value is blank. |
| [IsBlankOrError](03-power-fx-functions.md#isblankorerror) | Logic | True when the value is blank or an error. |
| [IsEmpty](03-power-fx-functions.md#isempty) | Logic | True when a table has no records. |
| [IsError](03-power-fx-functions.md#iserror) | Logic | True when the value is an error. |
| [IsNumeric](03-power-fx-functions.md#isnumeric) | Logic | True when the value is numeric. |
| [IsToday](03-power-fx-functions.md#istoday) | Date | True when the value falls on today's local date. |
| [Language](03-power-fx-functions.md#language) | Utility | Language tag of the current user. |
| [Last](03-power-fx-functions.md#last) | Table | Last record. |
| [LastN](03-power-fx-functions.md#lastn) | Table | Last N records. |
| [Left](03-power-fx-functions.md#left) | Text | Leftmost characters of a string. |
| [Len](03-power-fx-functions.md#len) | Text | Character length. |
| [Ln](03-power-fx-functions.md#ln) | Math | Natural logarithm. |
| [Log](03-power-fx-functions.md#log) | Math | Logarithm in a chosen base. |
| [LookUp](03-power-fx-functions.md#lookup) | Table | First record that matches a condition. |
| [Lower](03-power-fx-functions.md#lower) | Text | Lowercase letters. |
| [Max](03-power-fx-functions.md#max) | Math | Largest value in a set or table. |
| [Mid](03-power-fx-functions.md#mid) | Text | Substring from a start position. |
| [Min](03-power-fx-functions.md#min) | Math | Smallest value in a set or table. |
| [Minute](03-power-fx-functions.md#minute) | Date | Minute portion of a date/time. |
| [Mod](03-power-fx-functions.md#mod) | Math | Remainder after division. |
| [Month](03-power-fx-functions.md#month) | Date | Month number from a date/time. |
| [Not](03-power-fx-functions.md#not) | Logic | Boolean negation (`!`). |
| [Now](03-power-fx-functions.md#now) | Date | Current local date and time. |
| [Or](03-power-fx-functions.md#or) | Logic | True when any argument is true (`||`). |
| [Patch](03-power-fx-functions.md#patch) | Table | Create or merge records. |
| [Pi](03-power-fx-functions.md#pi) | Math | The constant π. |
| [PlainText](03-power-fx-functions.md#plaintext) | Text | Strip HTML/XML tags. |
| [Power](03-power-fx-functions.md#power) | Math | Base raised to an exponent (`^`). |
| [Proper](03-power-fx-functions.md#proper) | Text | Capitalize the first letter of each word. |
| [Radians](03-power-fx-functions.md#radians) | Math | Degrees to radians. |
| [Rand](03-power-fx-functions.md#rand) | Math | Pseudo-random number between 0 and 1. |
| [RandBetween](03-power-fx-functions.md#randbetween) | Math | Pseudo-random integer in a range. |
| [Remove](03-power-fx-functions.md#remove) | Table | Delete specific records from a source. |
| [RenameColumns](03-power-fx-functions.md#renamecolumns) | Table | Rename one or more columns. |
| [Replace](03-power-fx-functions.md#replace) | Text | Overwrite characters by start position. |
| [Right](03-power-fx-functions.md#right) | Text | Rightmost characters of a string. |
| [Round](03-power-fx-functions.md#round) | Math | Nearest value at a given precision. |
| [RoundDown](03-power-fx-functions.md#rounddown) | Math | Round toward zero/down. |
| [RoundUp](03-power-fx-functions.md#roundup) | Math | Round away from zero/up. |
| [Search](03-power-fx-functions.md#search) | Table | Rows whose selected columns contain a string. |
| [Second](03-power-fx-functions.md#second) | Date | Second portion of a date/time. |
| [Sequence](03-power-fx-functions.md#sequence) | Table | Table of sequential numbers. |
| [Set](03-power-fx-functions.md#set) | Utility | Assign a global; limited support in PAD. |
| [ShowColumns](03-power-fx-functions.md#showcolumns) | Table | Keep only the named columns. |
| [Shuffle](03-power-fx-functions.md#shuffle) | Table | Randomize record order. |
| [Sin](03-power-fx-functions.md#sin) | Math | Sine of an angle in radians. |
| [Sort](03-power-fx-functions.md#sort) | Table | Sort records by a formula. |
| [SortByColumns](03-power-fx-functions.md#sortbycolumns) | Table | Sort records by column names. |
| [Split](03-power-fx-functions.md#split) | Text | Break a string into a table of pieces. |
| [Sqrt](03-power-fx-functions.md#sqrt) | Math | Square root. |
| [StartsWith](03-power-fx-functions.md#startswith) | Text | True when a string begins with another string. |
| [StdevP](03-power-fx-functions.md#stdevp) | Math | Population standard deviation. |
| [Substitute](03-power-fx-functions.md#substitute) | Text | Replace matching substrings. |
| [Sum](03-power-fx-functions.md#sum) | Math | Total of a table expression or argument list. |
| [Summarize](03-power-fx-functions.md#summarize) | Table | Group rows and aggregate the rest. |
| [Switch](03-power-fx-functions.md#switch) | Logic | Match a value and evaluate the matching formula. |
| [Table](03-power-fx-functions.md#table) | Table | Build a temporary table from records. |
| [Tan](03-power-fx-functions.md#tan) | Math | Tangent of an angle in radians. |
| [Text](03-power-fx-functions.md#text) | Conversion | Format any value as text. |
| [Time](03-power-fx-functions.md#time) | Date | Build a time from hour, minute, and second. |
| [TimeValue](03-power-fx-functions.md#timevalue) | Date | Parse a time-only string. |
| [TimeZoneOffset](03-power-fx-functions.md#timezoneoffset) | Date | Minutes between UTC and local time. |
| [Today](03-power-fx-functions.md#today) | Date | Current local date (no time). |
| [Trim](03-power-fx-functions.md#trim) | Text | Collapse extra interior and edge spaces. |
| [TrimEnds](03-power-fx-functions.md#trimends) | Text | Strip leading and trailing spaces only. |
| [Trunc](03-power-fx-functions.md#trunc) | Math | Drop the fractional part of a number. |
| [UniChar](03-power-fx-functions.md#unichar) | Text | Character for a Unicode code point. |
| [Upper](03-power-fx-functions.md#upper) | Text | Uppercase letters. |
| [Value](03-power-fx-functions.md#value) | Conversion | Parse text as a number. |
| [VarP](03-power-fx-functions.md#varp) | Math | Population variance. |
| [Weekday](03-power-fx-functions.md#weekday) | Date | Weekday number from a date/time. |
| [WeekNum](03-power-fx-functions.md#weeknum) | Date | Week number of a date/time. |
| [With](03-power-fx-functions.md#with) | Utility | Evaluate a formula against a named record. |
| [Year](03-power-fx-functions.md#year) | Date | Year from a date/time. |

## Designer and console items

See [Designer usable items](01-designer-usable-items.md).

| Item | Purpose |
| --- | --- |
| Actions pane | Left-side catalog of modules and actions, with search and favorites. |
| Workspace canvas | Ordered list of deployed actions for the active subflow. |
| Subflows | Tabs besides Main; invoke with Run subflow, including dynamic names. |
| Variables pane | Input, output, and flow variables, including sensitive and optional flags. |
| UI elements pane | Captured desktop and web elements plus their selectors. |
| UI element collections | Reusable shared UI element sets across flows. |
| Images pane | Captured bitmaps used by image-based mouse and wait actions. |
| Errors pane | Design-time and run-time errors and warnings with line and subflow. |
| Action modal | Inputs, produced variables, and On error handling for one action. |
| On error handling | Retry, continue, throw, or go-to-label when an action fails. |
| Breakpoints | Pause a designer run on a chosen action. |
| Run / Run from here / Step | Designer debug controls for the current flow. |
| Desktop recorder | Capture clicks and typing against desktop apps as UI actions. |
| Web recorder | Capture browser interactions as web automation actions. |
| Copilot / natural language | Describe a task in English to draft actions or Power Fx. |
| Assets library | Add extra cloud connectors and custom actions to the pane. |
| Custom actions | Environment-level .dll action groups uploaded by the organization. |
| Credentials | Portal, Azure Key Vault, or CyberArk secrets resolved at runtime. |
| Connection references | Cloud connector connections embedded or brought-your-own. |
| Environment variables | Text, number, JSON, boolean, or secret values from the environment. |
| Work queues | Orchestrated item processing across unattended machines. |
| Console - My flows | Create, run, stop, and schedule desktop flows on this machine. |
| Console - examples | Starter flows shipped with PAD. |
| Keyboard shortcut run | Start a flow from a hotkey registered in the console. |
| URL / scheme run | Start a flow from a PAD URL shortcut. |
| Machine registration | Register this PC for attended or unattended cloud-initiated runs. |
| Machine groups | Pool machines for unattended scale-out. |
| Hosted machines / groups | Microsoft-hosted bots for unattended runs. |
| Flow designer menus | Save, save as, undo/redo, find, comments, and enable/disable actions. |
| Safe stop | Cooperative stop check via If safe stop requested. |
| Sensitive variables | Mask values in logs and the variables viewer. |
| Input / output variables | Contract used when a cloud flow or another desktop flow calls this flow. |
| Selectors | Text-based (and repaired) locators behind UI and web elements. |
| Custom forms designer | Layout used by Display custom form. |
| Power Fx toggle | Per-flow choice of classic % expressions versus Power Fx. |

## Data types

See [Variable data types](02-data-types.md).

| Type | Purpose |
| --- | --- |
| Text value | Any string, including paths and file contents. |
| Numeric value | A number; the only type allowed in math expressions. |
| Boolean value | True or False, often written `%True%` / `%False%`. |
| List | Zero-based collection of items of a common type. |
| Datatable | Rows and columns; like a two-dimensional array. |
| Datarow | One row of a datatable, including For each current items. |
| Custom object | Property/value map, JSON-serializable. |
| Connector object | Structured result from a cloud connector operation. |
| General value | Design-time unknown type; resolved at runtime. |
| File | A file on disk. |
| Folder | A folder on disk. |
| FileSystemObject | Either a file or a folder. |
| Datetime | Date and time, including `%d"yyyy-MM-dd HH:mm:ss"%` literals. |
| SensitiveValue | Masked text such as passwords and secret environment variables. |
| Credential | Username/password (or similar) from Get credential. |
| Web browser instance | Chrome, Edge, Firefox, or IE session. |
| Window instance | A desktop window from Get window. |
| Excel instance | A running Excel workbook from Launch/Attach Excel. |
| Word instance | A running Word document from Launch/Attach Word. |
| Outlook instance | A running Outlook profile from Launch Outlook. |
| Access instance | A running Access database from Launch Access. |
| SQL connection | Open database session. |
| Exchange connection | Open Exchange session. |
| FTP connection | Open FTP or secure FTP session. |
| CMD session | Open Command Prompt session. |
| Terminal session | Open terminal emulator session. |
| OCR Engine | Windows OCR or Tesseract engine object. |
| XML node | Loaded XML document or fragment. |
| Mail message | IMAP/SMTP message from Retrieve email messages. |
| Outlook mail message | Message from Retrieve email messages from Outlook. |
| Exchange mail message | Message from Retrieve Exchange email messages. |
| Error | Last error object from Get last error. |
| Active Directory entry | AD server connection. |
| Group info / Group member / User info | AD group and user records. |
| EC2 client / instance / volume / snapshot | AWS automation objects. |
| Azure client / VM / disk / snapshot / subscription / resource group | Azure automation objects. |
| FTP file / FTP directory | Remote FTP items. |
| List of PDF table info | Tables extracted from a PDF, with page metadata. |
| TriggerEventInstanceHandle | Handle raised by a UI element event trigger. |
