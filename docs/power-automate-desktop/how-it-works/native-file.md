# File — how each function works

Native Actions pane module **File**.

16 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Convert Base64 to file

- **Id:** `file/convert-base64-to-file`
- **Kind:** native-action
- **Purpose:** Converts base64 to file.

**Use case.** In PDFs and CSVs landing in a watch folder, drop **Convert Base64 to file** on the canvas. Converts base64 to file.

**Demonstration.**

```text
**Convert Base64 to file**
- Base64 encoded text: `INV-1042`
- File path: `C:\RPA\Invoices\INV-1042.pdf`
- If file exists: `C:\RPA\Invoices\INV-1042.pdf`
```

**Analogy.** One tool in that kit: a filing cabinet: copy, rename, read, or shred a single folder of papers.

**In combination.** If file exists or Wait for file, then copy/move/read; convert to binary before cloud connectors.

### Convert binary data to file

- **Id:** `file/convert-binary-data-to-file`
- **Kind:** native-action
- **Purpose:** Converts binary data to file.

**Use case.** Required after cloud connector download before Excel/PDF/File actions.

**Demonstration.**

```text
**Convert binary data to file**
- Binary data: `INV-1042`
- File path: `C:\RPA\Invoices\INV-1042.pdf`
- If file exists: `C:\RPA\Invoices\INV-1042.pdf`
```

**Analogy.** One tool in that kit: a filing cabinet: copy, rename, read, or shred a single folder of papers.

**In combination.** If file exists or Wait for file, then copy/move/read; convert to binary before cloud connectors. Bridge native File/Excel actions and cloud connector operations.

### Convert file to Base64

- **Id:** `file/convert-file-to-base64`
- **Kind:** native-action
- **Purpose:** Converts file to Base64.

**Use case.** In PDFs and CSVs landing in a watch folder, drop **Convert file to Base64** on the canvas. Converts file to Base64.

**Demonstration.**

```text
**Convert file to Base64**
- File path: `C:\RPA\Invoices\INV-1042.pdf`
Produces:
- `%Base64Text%` (Text value)
```

**Analogy.** One tool in that kit: a filing cabinet: copy, rename, read, or shred a single folder of papers.

**In combination.** If file exists or Wait for file, then copy/move/read; convert to binary before cloud connectors.

### Convert file to binary data

- **Id:** `file/convert-file-to-binary-data`
- **Kind:** native-action
- **Purpose:** Converts file to binary data.

**Use case.** Required before most cloud connector upload/attach parameters.

**Demonstration.**

```text
**Convert file to binary data**
- File path: `C:\RPA\Invoices\INV-1042.pdf`
Produces:
- `%BinaryData%` (Text value)
```

**Analogy.** One tool in that kit: a filing cabinet: copy, rename, read, or shred a single folder of papers.

**In combination.** If file exists or Wait for file, then copy/move/read; convert to binary before cloud connectors. Bridge native File/Excel actions and cloud connector operations.

### Copy file(s)

- **Id:** `file/copy-file-s`
- **Kind:** native-action
- **Purpose:** Copies file(s).

**Use case.** In PDFs and CSVs landing in a watch folder, drop **Copy file(s)** on the canvas. Copies file(s).

**Demonstration.**

```text
**Copy file(s)**
- File(s) to copy: `%Files%`
- Destination folder: `C:\RPA\Invoices`
- If file exists: `C:\RPA\Invoices\INV-1042.pdf`
Produces:
- `%CopiedFiles%` (List of Files)
```

**Analogy.** One tool in that kit: a filing cabinet: copy, rename, read, or shred a single folder of papers.

**In combination.** If file exists or Wait for file, then copy/move/read; convert to binary before cloud connectors.

### Delete file(s)

- **Id:** `file/delete-file-s`
- **Kind:** native-action
- **Purpose:** Deletes file(s).

**Use case.** In PDFs and CSVs landing in a watch folder, drop **Delete file(s)** on the canvas. Deletes file(s).

**Demonstration.**

```text
**Delete file(s)**
- File(s) to delete: `%Files%`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** If file exists or Wait for file, then copy/move/read; convert to binary before cloud connectors.

### Get file path part

- **Id:** `file/get-file-path-part`
- **Kind:** native-action
- **Purpose:** Reads file path part into a flow variable.

**Use case.** In PDFs and CSVs landing in a watch folder, drop **Get file path part** on the canvas. Reads file path part into a flow variable.

**Demonstration.**

```text
**Get file path part**
- File path: `C:\RPA\Invoices\INV-1042.pdf`
Produces:
- `%RootPath%` (File)
- `%Directory%` (Folder)
- `%FileName%` (Text value)
- `%FileNameNoExtension%` (Text value)
- `%FileExtension%` (Text value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** If file exists or Wait for file, then copy/move/read; convert to binary before cloud connectors.

### Get temporary file

- **Id:** `file/get-temporary-file`
- **Kind:** native-action
- **Purpose:** Reads temporary file into a flow variable.

**Use case.** In PDFs and CSVs landing in a watch folder, drop **Get temporary file** on the canvas. Reads temporary file into a flow variable.

**Demonstration.**

```text
**Get temporary file**
- (no inputs)
Produces:
- `%TempFile%` (File)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** If file exists or Wait for file, then copy/move/read; convert to binary before cloud connectors.

### If file exists

- **Id:** `file/if-file-exists`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when file exists.

**Use case.** In PDFs and CSVs landing in a watch folder, drop **If file exists** on the canvas. Opens a conditional branch that runs when file exists.

**Demonstration.**

```text
**If file exists**
- If file: `C:\RPA\Invoices\INV-1042.pdf`
- File path: `C:\RPA\Invoices\INV-1042.pdf`
Place the actions that should run inside this block, then End.
```

**Analogy.** Checking a condition on a clipboard before you choose a door.

**In combination.** If file exists or Wait for file, then copy/move/read; convert to binary before cloud connectors. Combine with Else / Else if and End. Put Wait or If file exists before brittle UI/browser steps.

### Move file(s)

- **Id:** `file/move-file-s`
- **Kind:** native-action
- **Purpose:** Moves file(s).

**Use case.** In PDFs and CSVs landing in a watch folder, drop **Move file(s)** on the canvas. Moves file(s).

**Demonstration.**

```text
**Move file(s)**
- File(s) to move: `%Files%`
- Destination folder: `C:\RPA\Invoices`
- If file exists: `C:\RPA\Invoices\INV-1042.pdf`
Produces:
- `%MovedFiles%` (List of Files)
```

**Analogy.** One tool in that kit: a filing cabinet: copy, rename, read, or shred a single folder of papers.

**In combination.** If file exists or Wait for file, then copy/move/read; convert to binary before cloud connectors.

### Read from CSV file

- **Id:** `file/read-from-csv-file`
- **Kind:** native-action
- **Purpose:** Reads from CSV file.

**Use case.** In PDFs and CSVs landing in a watch folder, drop **Read from CSV file** on the canvas. Reads from CSV file.

**Demonstration.**

```text
**Read from CSV file**
- File path: `C:\RPA\Invoices\batch.csv`
- Encoding: `UTF-8`
- Trim fields: `True`
- First line contains column names: `False`
- Columns separator: `Predefined`
- Separator: `System default`
- Custom separator: `INV-1042`
- Fixed column widths: `INV-1042`
Produces:
- `%CSVTable%` (Datatable)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** If file exists or Wait for file, then copy/move/read; convert to binary before cloud connectors.

### Read text from file

- **Id:** `file/read-text-from-file`
- **Kind:** native-action
- **Purpose:** Reads text from file.

**Use case.** In PDFs and CSVs landing in a watch folder, drop **Read text from file** on the canvas. Reads text from file.

**Demonstration.**

```text
**Read text from file**
- File path: `C:\RPA\Invoices\INV-1042.pdf`
- Store content as: `%Files%`
- Encoding: `UTF-8`
Produces:
- `%FileContents%` (Text value)
- `%FileContents%` (List of Text values)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** If file exists or Wait for file, then copy/move/read; convert to binary before cloud connectors.

### Rename file(s)

- **Id:** `file/rename-file-s`
- **Kind:** native-action
- **Purpose:** Renames file(s).

**Use case.** In PDFs and CSVs landing in a watch folder, drop **Rename file(s)** on the canvas. Renames file(s).

**Demonstration.**

```text
**Rename file(s)**
- File to rename: `%Files%`
- Add number to: `True`
- Rename scheme: `Set new name`
- New file name: `C:\RPA\Invoices\INV-1042.pdf`
- New extension: `INV-1042`
- New file name: `C:\RPA\Invoices\INV-1042.pdf`
- Add number to: `After name`
- Text to add: `INV-1042`
- … 17 more parameter(s) in the action modal
Produces:
- `%RenamedFiles%` (List of Files)
```

**Analogy.** One tool in that kit: a filing cabinet: copy, rename, read, or shred a single folder of papers.

**In combination.** If file exists or Wait for file, then copy/move/read; convert to binary before cloud connectors.

### Wait for file

- **Id:** `file/wait-for-file`
- **Kind:** native-action
- **Purpose:** Pauses the flow until file.

**Use case.** In PDFs and CSVs landing in a watch folder, drop **Wait for file** on the canvas. Pauses the flow until file.

**Demonstration.**

```text
**Wait for file**
- Wait for file to be: `C:\RPA\Invoices\INV-1042.pdf`
- File path: `C:\RPA\Invoices\INV-1042.pdf`
```

**Analogy.** Standing at the microwave until it beeps, so you do not grab a cold plate.

**In combination.** If file exists or Wait for file, then copy/move/read; convert to binary before cloud connectors.

### Write text to file

- **Id:** `file/write-text-to-file`
- **Kind:** native-action
- **Purpose:** Writes text to file.

**Use case.** In PDFs and CSVs landing in a watch folder, drop **Write text to file** on the canvas. Writes text to file.

**Demonstration.**

```text
**Write text to file**
- File path: `C:\RPA\Invoices\INV-1042.pdf`
- Text to write: `(set in designer)`
- Append new line: `True`
- If file exists: `C:\RPA\Invoices\INV-1042.pdf`
- Encoding: `Unicode`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** If file exists or Wait for file, then copy/move/read; convert to binary before cloud connectors.

### Write to CSV file

- **Id:** `file/write-to-csv-file`
- **Kind:** native-action
- **Purpose:** Writes to CSV file.

**Use case.** In PDFs and CSVs landing in a watch folder, drop **Write to CSV file** on the canvas. Writes to CSV file.

**Demonstration.**

```text
**Write to CSV file**
- Variable to write: `(set in designer)`
- File path: `C:\RPA\Invoices\batch.csv`
- Encoding: `UTF-8`
- Include column names: `False`
- If file exists: `C:\RPA\Invoices\batch.csv`
- Separator: `System default`
- Custom columns separator: `INV-1042`
- Use custom columns separator: `False`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** If file exists or Wait for file, then copy/move/read; convert to binary before cloud connectors.
