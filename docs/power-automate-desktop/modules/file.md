# File

Copy, move, read, write, and convert local files, including CSV and binary.

This page documents every **native action** in this group (16 items).

## Actions

### Convert Base64 to file

- **Inventory id:** `file/convert-base64-to-file`
- **Kind:** native-action
- **Purpose:** Converts base64 to file.
- **Key inputs:** `Base64 encoded text` (Text value); `File path` (File); `If file exists` (Do nothing, Overwrite)
- **Produces:** None listed
- **Exceptions:** `Invalid directory for file`; `Can't convert Base64 to file`
- **Microsoft Learn:** [Convert Base64 to file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#convertbase64tofileaction)

### Convert binary data to file

- **Inventory id:** `file/convert-binary-data-to-file`
- **Kind:** native-action
- **Purpose:** Converts binary data to file.
- **Key inputs:** `Binary data` (Text value); `File path` (File); `If file exists` (Do nothing, Overwrite)
- **Produces:** None listed
- **Exceptions:** `Invalid directory for file`; `Can't convert binary file to file`
- **Microsoft Learn:** [Convert binary data to file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#convertbinarytofileaction)

### Convert file to Base64

- **Inventory id:** `file/convert-file-to-base64`
- **Kind:** native-action
- **Purpose:** Converts file to Base64.
- **Key inputs:** `File path` (File)
- **Produces:** `Base64Text` (Text value)
- **Exceptions:** `File not found`; `Can't convert file to Base64`
- **Microsoft Learn:** [Convert file to Base64](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#convertfiletobase64action)

### Convert file to binary data

- **Inventory id:** `file/convert-file-to-binary-data`
- **Kind:** native-action
- **Purpose:** Converts file to binary data.
- **Key inputs:** `File path` (File)
- **Produces:** `BinaryData` (Text value)
- **Exceptions:** `File not found`; `Can't convert file to binary data`
- **Microsoft Learn:** [Convert file to binary data](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#convertfiletobinaryaction)

### Copy file(s)

- **Inventory id:** `file/copy-file-s`
- **Kind:** native-action
- **Purpose:** Copies file(s).
- **Key inputs:** `File(s) to copy` (List of Files); `Destination folder` (Folder); `If file exists` (Do nothing, Overwrite)
- **Produces:** `CopiedFiles` (List of Files)
- **Exceptions:** `Source folder doesn't exist`; `Destination folder doesn't exist`; `File not found`; `Can't copy file`
- **Microsoft Learn:** [Copy file(s)](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#copy)

### Delete file(s)

- **Inventory id:** `file/delete-file-s`
- **Kind:** native-action
- **Purpose:** Deletes file(s).
- **Key inputs:** `File(s) to delete` (List of Files)
- **Produces:** None listed
- **Exceptions:** `File path doesn't exist`; `File not found`; `Can't delete file`
- **Microsoft Learn:** [Delete file(s)](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#delete)

### Get file path part

- **Inventory id:** `file/get-file-path-part`
- **Kind:** native-action
- **Purpose:** Reads file path part into a flow variable.
- **Key inputs:** `File path` (File)
- **Produces:** `RootPath` (File); `Directory` (Folder); `FileName` (Text value); `FileNameNoExtension` (Text value); `FileExtension` (Text value)
- **Exceptions:** `File path contains invalid characters`
- **Microsoft Learn:** [Get file path part](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#getpathpart)

### Get temporary file

- **Inventory id:** `file/get-temporary-file`
- **Kind:** native-action
- **Purpose:** Reads temporary file into a flow variable.
- **Key inputs:** None
- **Produces:** `TempFile` (File)
- **Exceptions:** `Failed to create temporary file`
- **Microsoft Learn:** [Get temporary file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#gettemppath)

### If file exists

- **Inventory id:** `file/if-file-exists`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when file exists.
- **Key inputs:** `If file` (Exists, Doesn't exist); `File path` (File)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [If file exists](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#iffileaction)

### Move file(s)

- **Inventory id:** `file/move-file-s`
- **Kind:** native-action
- **Purpose:** Moves file(s).
- **Key inputs:** `File(s) to move` (List of Files); `Destination folder` (Folder); `If file exists` (Do nothing, Overwrite)
- **Produces:** `MovedFiles` (List of Files)
- **Exceptions:** `Source folder doesn't exist`; `Destination folder doesn't exist`; `File not found`; `Can't move file`
- **Microsoft Learn:** [Move file(s)](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#move)

### Read from CSV file

- **Inventory id:** `file/read-from-csv-file`
- **Kind:** native-action
- **Purpose:** Reads from CSV file.
- **Key inputs:** `File path` (File); `Encoding` (UTF-8, Unicode, Unicode (big-endian), UTF-8 (No byte order mark), Unicode (no byte order mark), System default, ASCII); `Trim fields` (Boolean value); `First line contains column names` (Boolean value); `Columns separator` (Predefined, Custom, Fixed column widths); `Separator` (System default, Comma, Semicolon, Tab); `Custom separator` (Text value); `Fixed column widths` (Text value)
- **Produces:** `CSVTable` (Datatable)
- **Exceptions:** `Read from CSV failed`
- **Microsoft Learn:** [Read from CSV file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#readfromcsvfile)

### Read text from file

- **Inventory id:** `file/read-text-from-file`
- **Kind:** native-action
- **Purpose:** Reads text from file.
- **Key inputs:** `File path` (File); `Store content as` (Single text value, List (each is a list item)); `Encoding` (System default, ASCII, Unicode, Unicode (big-endian), UTF-8)
- **Produces:** `FileContents` (Text value); `FileContents` (List of Text values)
- **Exceptions:** `Directory not found`; `File not found`; `Failed to read from file`
- **Microsoft Learn:** [Read text from file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#readtextfromfile)

### Rename file(s)

- **Inventory id:** `file/rename-file-s`
- **Kind:** native-action
- **Purpose:** Renames file(s).
- **Key inputs:** `File to rename` (List of Files); `Add number to` (Boolean value); `Rename scheme` (Set new name, Add text, Remove text, Replace text, Change extension, Add datetime, Make sequential); `New file name` (Text value); `New extension` (Text value; optional); `New file name` (Text value); `Add number to` (After name, Before name); `Text to add` (Text value; optional); `Text to remove` (Text value; optional); `Text to replace` (Text value); `Use custom datetime` (Boolean value); `Datetime to add` (Current datetime, Creation time, Last accessed, Last modified); `Keep extension` (Boolean value); `Replace with` (Text value; optional); `Start numbering at` (Numeric value); `Add text` (After name, Before name); `Custom datetime` (Datetime); `Increment by` (Numeric value); `Add datetime` (After name, Before name); `Separator` (Nothing, Space, Dash, Period, Underscore); `Separator` (Nothing, Space, Dash, Period, Underscore); `Use padding` (Boolean value); `Datetime format` (Text value); `Make each number at least` (Numeric value; optional); `If file exists` (Do nothing, Overwrite)
- **Produces:** `RenamedFiles` (List of Files)
- **Exceptions:** `Directory not found`; `File not found`; `Can't rename file`
- **Microsoft Learn:** [Rename file(s)](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#renamefiles)

### Wait for file

- **Inventory id:** `file/wait-for-file`
- **Kind:** native-action
- **Purpose:** Pauses the flow until file.
- **Key inputs:** `Wait for file to be` (Created, Deleted); `File path` (File)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Wait for file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#waitforfileaction)

### Write text to file

- **Inventory id:** `file/write-text-to-file`
- **Kind:** native-action
- **Purpose:** Writes text to file.
- **Key inputs:** `File path` (File); `Text to write` (General value; optional); `Append new line` (Boolean value); `If file exists` (Overwrite existing content, Append content); `Encoding` (System default, ASCII, Unicode, Unicode (big-endian), UTF-8, Unicode (without byte order mask), UTF-8 (without byte order mask))
- **Produces:** None listed
- **Exceptions:** `Failed to write text to file`; `Invalid directory for file`
- **Microsoft Learn:** [Write text to file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#writetext)

### Write to CSV file

- **Inventory id:** `file/write-to-csv-file`
- **Kind:** native-action
- **Purpose:** Writes to CSV file.
- **Key inputs:** `Variable to write` (General value); `File path` (File); `Encoding` (UTF-8, Unicode, Unicode (big-endian), UTF-8 (No byte order mark), Unicode (no byte order mark), System default, ASCII); `Include column names` (Boolean value); `If file exists` (Overwrite existing content, Append content); `Separator` (System default, Comma, Semicolon, Tab); `Custom columns separator` (Text value); `Use custom columns separator` (Boolean value)
- **Produces:** None listed
- **Exceptions:** `Write failed`
- **Microsoft Learn:** [Write to CSV file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#writetocsvfile)
