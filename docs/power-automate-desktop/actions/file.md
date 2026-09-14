# File

Create, copy, move, read, write, and convert files.

- Actions in this module: **16**
- Official docs: [File actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file)

## Actions

### If file exists

Marks the beginning of a conditional block of actions depending on whether a file exists or not.

Designer name: **If file exists**. Official reference: [File / If file exists](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#iffileaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| If file | Choice | Exists, Doesn't exist | Exists |
| File path | Required | File | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Wait for file

Suspend the execution of the automation until a file is created or deleted.

Designer name: **Wait for file**. Official reference: [File / Wait for file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#waitforfileaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Wait for file to be | Choice | Created, Deleted | Created |
| File path | Required | File | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Copy file(s)

Copy one or more files into a destination folder.

Designer name: **Copy file(s)**. Official reference: [File / Copy file(s)](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#copy).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| File(s) to copy | Required | List of Files | — |
| Destination folder | Required | Folder | — |
| If file exists | Choice | Do nothing, Overwrite | Do nothing |

**Outputs**

| Variable | Type |
|---|---|
| CopiedFiles | List of Files |

**On error:** `Source folder doesn't exist`, `Destination folder doesn't exist`, `File not found`, `Can't copy file`.

---

### Move file(s)

Move one or more files into a destination folder.

Designer name: **Move file(s)**. Official reference: [File / Move file(s)](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#move).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| File(s) to move | Required | List of Files | — |
| Destination folder | Required | Folder | — |
| If file exists | Choice | Do nothing, Overwrite | Do nothing |

**Outputs**

| Variable | Type |
|---|---|
| MovedFiles | List of Files |

**On error:** `Source folder doesn't exist`, `Destination folder doesn't exist`, `File not found`, `Can't move file`.

---

### Delete file(s)

Delete one or more files.

Designer name: **Delete file(s)**. Official reference: [File / Delete file(s)](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#delete).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| File(s) to delete | Required | List of Files | — |

Produces no variables.

**On error:** `File path doesn't exist`, `File not found`, `Can't delete file`.

---

### Rename file(s)

Change the name of one or more files.

Designer name: **Rename file(s)**. Official reference: [File / Rename file(s)](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#renamefiles).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| File to rename | Required | List of Files | — |
| Add number to | Choice | Boolean value | True |
| Rename scheme | Choice | Set new name, Add text, Remove text, Replace text, Change extension, Add datetime, Make sequential | Set new name |
| New file name | Required | Text value | — |
| New extension | Optional | Text value | — |
| New file name | Required | Text value | — |
| Add number to | Choice | After name, Before name | After name |
| Text to add | Optional | Text value | — |
| Text to remove | Optional | Text value | — |
| Text to replace | Required | Text value | — |
| Use custom datetime | Choice | Boolean value | False |
| Datetime to add | Choice | Current datetime, Creation time, Last accessed, Last modified | Current datetime |
| Keep extension | Choice | Boolean value | True |
| Replace with | Optional | Text value | — |
| Start numbering at | Required | Numeric value | — |
| Add text | Choice | After name, Before name | After name |
| Custom datetime | Required | Datetime | — |
| Increment by | Required | Numeric value | — |
| Add datetime | Choice | After name, Before name | After name |
| Separator | Choice | Nothing, Space, Dash, Period, Underscore | Space |
| Separator | Choice | Nothing, Space, Dash, Period, Underscore | Space |
| Use padding | Choice | Boolean value | False |
| Datetime format | Required | Text value | yyyyMMdd |
| Make each number at least | Optional | Numeric value | 3 |
| If file exists | Choice | Do nothing, Overwrite | Do nothing |

**Outputs**

| Variable | Type |
|---|---|
| RenamedFiles | List of Files |

**On error:** `Directory not found`, `File not found`, `Can't rename file`.

---

### Read text from file

Read the contents of a text file.

Designer name: **Read text from file**. Official reference: [File / Read text from file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#readtextfromfile).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| File path | Required | File | — |
| Store content as | Choice | Single text value, List (each is a list item) | Single text value |
| Encoding | Choice | System default, ASCII, Unicode, Unicode (big-endian), UTF-8 | UTF-8 |

**Outputs**

| Variable | Type |
|---|---|
| FileContents | Text value |
| FileContents | List of Text values |

**On error:** `Directory not found`, `File not found`, `Failed to read from file`.

---

### Write text to file

Write or appends text to a file.

Designer name: **Write text to file**. Official reference: [File / Write text to file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#writetext).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| File path | Required | File | — |
| Text to write | Optional | General value | — |
| Append new line | Choice | Boolean value | True |
| If file exists | Choice | Overwrite existing content, Append content | Overwrite existing content |
| Encoding | Choice | System default, ASCII, Unicode, Unicode (big-endian), UTF-8, Unicode (without byte order mask), UTF-8 (without byte order mask) | Unicode |

Produces no variables.

**On error:** `Failed to write text to file`, `Invalid directory for file`.

---

### Read from CSV file

Read a CSV file into a data table.

Designer name: **Read from CSV file**. Official reference: [File / Read from CSV file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#readfromcsvfile).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| File path | Required | File | — |
| Encoding | Choice | UTF-8, Unicode, Unicode (big-endian), UTF-8 (No byte order mark), Unicode (no byte order mark), System default, ASCII | UTF-8 |
| Trim fields | Choice | Boolean value | True |
| First line contains column names | Choice | Boolean value | False |
| Columns separator | Choice | Predefined, Custom, Fixed column widths | Predefined |
| Separator | Choice | System default, Comma, Semicolon, Tab | System default |
| Custom separator | Required | Text value | — |
| Fixed column widths | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| CSVTable | Datatable |

**On error:** `Read from CSV failed`.

---

### Write to CSV file

Write a data table, data row or list to a CSV file.

Designer name: **Write to CSV file**. Official reference: [File / Write to CSV file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#writetocsvfile).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Variable to write | Required | General value | — |
| File path | Required | File | — |
| Encoding | Choice | UTF-8, Unicode, Unicode (big-endian), UTF-8 (No byte order mark), Unicode (no byte order mark), System default, ASCII | UTF-8 |
| Include column names | Choice | Boolean value | False |
| If file exists | Choice | Overwrite existing content, Append content | Overwrite existing content |
| Separator | Choice | System default, Comma, Semicolon, Tab | System default |
| Custom columns separator | Required | Text value | — |
| Use custom columns separator | Choice | Boolean value | False |

Produces no variables.

**On error:** `Write failed`.

---

### Get file path part

Retrieve one or more parts (directory, filename, extension, etc.) from a text that represents a file path.

Designer name: **Get file path part**. Official reference: [File / Get file path part](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#getpathpart).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| File path | Required | File | — |

**Outputs**

| Variable | Type |
|---|---|
| RootPath | File |
| Directory | Folder |
| FileName | Text value |
| FileNameNoExtension | Text value |
| FileExtension | Text value |

**On error:** `File path contains invalid characters`.

---

### Get temporary file

Create a uniquely named, empty temporary file on disk, and get the file object (which is a representation, and can access the file and all its information).

Designer name: **Get temporary file**. Official reference: [File / Get temporary file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#gettemppath).

This action has no input parameters.

**Outputs**

| Variable | Type |
|---|---|
| TempFile | File |

**On error:** `Failed to create temporary file`.

---

### Convert file to Base64

Convert a file to Base64 encoded text.

Designer name: **Convert file to Base64**. Official reference: [File / Convert file to Base64](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#convertfiletobase64action).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| File path | Required | File | — |

**Outputs**

| Variable | Type |
|---|---|
| Base64Text | Text value |

**On error:** `File not found`, `Can't convert file to Base64`.

---

### Convert Base64 to file

Convert a Base64 encoded text to file.

Designer name: **Convert Base64 to file**. Official reference: [File / Convert Base64 to file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#convertbase64tofileaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Base64 encoded text | Required | Text value | — |
| File path | Required | File | — |
| If file exists | Choice | Do nothing, Overwrite | Do nothing |

Produces no variables.

**On error:** `Invalid directory for file`, `Can't convert Base64 to file`.

---

### Convert file to binary data

Convert a file to binary data.

Designer name: **Convert file to binary data**. Official reference: [File / Convert file to binary data](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#convertfiletobinaryaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| File path | Required | File | — |

**Outputs**

| Variable | Type |
|---|---|
| BinaryData | Text value |

**On error:** `File not found`, `Can't convert file to binary data`.

---

### Convert binary data to file

Runs the **Convert binary data to file** action.

Designer name: **Convert binary data to file**. Official reference: [File / Convert binary data to file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/file#convertbinarytofileaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Binary data | Required | Text value | — |
| File path | Required | File | — |
| If file exists | Choice | Do nothing, Overwrite | Do nothing |

Produces no variables.

**On error:** `Invalid directory for file`, `Can't convert binary file to file`.

---
