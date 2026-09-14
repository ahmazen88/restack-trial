# Excel — how each function works

Native Actions pane module **Excel**.

41 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Activate cell in Excel worksheet

- **Id:** `excel/activate-cell-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Activate a cell in the active worksheet of an Excel instance, by providing column, row, and offset.

**Use case.** In the monthly close workbook, drop **Activate cell in Excel worksheet** on the canvas. Activate a cell in the active worksheet of an Excel instance, by providing column, row, and offset.

**Demonstration.**

```text
**Activate cell in Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Activate: `Absolutely specified cell`
- Column: `Amount`
- Direction: `Left`
- Offset from active cell: `1`
- Row: `1`
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Add new worksheet

- **Id:** `excel/add-new-worksheet`
- **Kind:** native-action
- **Purpose:** Adds new worksheet.

**Use case.** In the monthly close workbook, drop **Add new worksheet** on the canvas. Adds new worksheet.

**Demonstration.**

```text
**Add new worksheet**
- Excel instance: `%ExcelInstance%`
- New worksheet name: `TrialBalance`
- Add worksheet as: `TrialBalance`
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Append cells in Excel worksheet

- **Id:** `excel/append-cells-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Appends a range of cells to the active worksheet of an Excel instance.

**Use case.** In the monthly close workbook, drop **Append cells in Excel worksheet** on the canvas. Appends a range of cells to the active worksheet of an Excel instance.

**Demonstration.**

```text
**Append cells in Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Append mode: `To active sheet`
- Name: `INV-1042`
- First row has headers: `False`
- Starting column: `INV-1042`
- Starting column header: `INV-1042`
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Attach to running Excel

- **Id:** `excel/attach-to-running-excel`
- **Kind:** native-action
- **Purpose:** Connects the flow to running Excel that is already running.

**Use case.** In the monthly close workbook, drop **Attach to running Excel** on the canvas. Connects the flow to running Excel that is already running.

**Demonstration.**

```text
**Attach to running Excel**
- Document name: `(set in designer)`
Produces:
- `%ExcelInstance%` (Excel instance)
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Auto fill cells in Excel worksheet

- **Id:** `excel/auto-fill-cells-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Auto fills a range with data, based on the data of another range, in the active worksheet of an Excel instance.

**Use case.** In the monthly close workbook, drop **Auto fill cells in Excel worksheet** on the canvas. Auto fills a range with data, based on the data of another range, in the active worksheet of an Excel instance.

**Demonstration.**

```text
**Auto fill cells in Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Ranges format: `Named cells`
- Source cells name: `INV-1042`
- Destination cells name: `INV-1042`
- Start column: `INV-1042`
- Start row: `1`
- Source end column: `INV-1042`
- Source end row: `1`
- … 2 more parameter(s) in the action modal
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Clear cells in Excel worksheet

- **Id:** `excel/clear-cells-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Clears cells in Excel worksheet.

**Use case.** In the monthly close workbook, drop **Clear cells in Excel worksheet** on the canvas. Clears cells in Excel worksheet.

**Demonstration.**

```text
**Clear cells in Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Clear: `Range of cells`
- X Axis Direction: `Left`
- Start column: `INV-1042`
- X Offset: `1`
- Start row: `1`
- End column: `INV-1042`
- Y Axis Direction: `Above`
- … 5 more parameter(s) in the action modal
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Clear filters in Excel worksheet

- **Id:** `excel/clear-filters-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Clears filters in Excel worksheet.

**Use case.** In the monthly close workbook, drop **Clear filters in Excel worksheet** on the canvas. Clears filters in Excel worksheet.

**Demonstration.**

```text
**Clear filters in Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Clear filters in: `Active sheet`
- Table name: `INV-1042`
- Clear filters from specific column: `True`
- Clear filter in column: `INV-1042`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Close Excel

- **Id:** `excel/close-excel`
- **Kind:** native-action
- **Purpose:** Closes excel.

**Use case.** In the monthly close workbook, drop **Close Excel** on the canvas. Closes excel.

**Demonstration.**

```text
**Close Excel**
- Excel instance: `%ExcelInstance%`
- Before closing Excel: `Don't save document`
- Document format: `%XmlDoc%`
- Document path: `C:\RPA\Close\FY26-P9.xlsx`
```

**Analogy.** Closing the ledger so nobody else trips over an open book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel. Call this only after the last use of the instance so you do not break later steps.

### Copy cells from Excel worksheet

- **Id:** `excel/copy-cells-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Copies cells from Excel worksheet.

**Use case.** In the monthly close workbook, drop **Copy cells from Excel worksheet** on the canvas. Copies cells from Excel worksheet.

**Demonstration.**

```text
**Copy cells from Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Copy mode: `Single Cell's Values`
- Start column: `INV-1042`
- Start row: `1`
- End column: `INV-1042`
- End row: `1`
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Copy Excel worksheet

- **Id:** `excel/copy-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Copies excel worksheet.

**Use case.** In the monthly close workbook, drop **Copy Excel worksheet** on the canvas. Copies excel worksheet.

**Demonstration.**

```text
**Copy Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Copy worksheet with: `TrialBalance`
- Worksheet index: `TrialBalance`
- Worksheet name: `TrialBalance`
- Target Excel instance: `%ExcelInstance%`
- Worksheet new name: `TrialBalance`
- Paste worksheet as: `TrialBalance`
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Delete column from Excel worksheet

- **Id:** `excel/delete-column-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Deletes column from Excel worksheet.

**Use case.** In the monthly close workbook, drop **Delete column from Excel worksheet** on the canvas. Deletes column from Excel worksheet.

**Demonstration.**

```text
**Delete column from Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Delete column: `INV-1042`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Delete Excel worksheet

- **Id:** `excel/delete-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Deletes excel worksheet.

**Use case.** In the monthly close workbook, drop **Delete Excel worksheet** on the canvas. Deletes excel worksheet.

**Demonstration.**

```text
**Delete Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Delete worksheet with: `TrialBalance`
- Worksheet index: `TrialBalance`
- Worksheet name: `TrialBalance`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Delete from Excel worksheet

- **Id:** `excel/delete-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Deletes from Excel worksheet.

**Use case.** In the monthly close workbook, drop **Delete from Excel worksheet** on the canvas. Deletes from Excel worksheet.

**Demonstration.**

```text
**Delete from Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Retrieve: `The value of a single cell`
- Start column: `INV-1042`
- Start row: `1`
- End column: `INV-1042`
- End row: `1`
- Shift direction: `Left`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Delete row from Excel worksheet

- **Id:** `excel/delete-row-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Deletes row from Excel worksheet.

**Use case.** In the monthly close workbook, drop **Delete row from Excel worksheet** on the canvas. Deletes row from Excel worksheet.

**Demonstration.**

```text
**Delete row from Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Delete row: `1`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Filter cells in Excel worksheet

- **Id:** `excel/filter-cells-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Filters cells in Excel worksheet.

**Use case.** In the monthly close workbook, drop **Filter cells in Excel worksheet** on the canvas. Filters cells in Excel worksheet.

**Demonstration.**

```text
**Filter cells in Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Filter column in: `Active sheet`
- Table name: `INV-1042`
- Range: `Named cells`
- Cells name: `INV-1042`
- Start column: `INV-1042`
- Start row: `1`
- End column: `INV-1042`
- … 3 more parameter(s) in the action modal
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Find and replace cells in Excel worksheet

- **Id:** `excel/find-and-replace-cells-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Finds and replace cells in Excel worksheet.

**Use case.** In the monthly close workbook, drop **Find and replace cells in Excel worksheet** on the canvas. Finds and replace cells in Excel worksheet.

**Demonstration.**

```text
**Find and replace cells in Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Search mode: `Find`
- All matches: `False`
- Text to find: `INV-1042`
- Text to replace with: `INV-1042`
- Match case: `False`
- Match entire cell contents: `False`
- Search by: `Rows`
Produces:
- `%FoundColumnIndex%` (Numeric value)
- `%FoundRowIndex%` (Numeric value)
- `%Cells%` (Datatable)
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Get active cell on Excel worksheet

- **Id:** `excel/get-active-cell-on-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Reads active cell on Excel worksheet into a flow variable.

**Use case.** In the monthly close workbook, drop **Get active cell on Excel worksheet** on the canvas. Reads active cell on Excel worksheet into a flow variable.

**Demonstration.**

```text
**Get active cell on Excel worksheet**
- Excel instance: `%ExcelInstance%`
Produces:
- `%ActiveCellColumnIndex%` (Numeric value)
- `%ActiveCellRowIndex%` (Numeric value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Get active Excel worksheet

- **Id:** `excel/get-active-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Reads active Excel worksheet into a flow variable.

**Use case.** In the monthly close workbook, drop **Get active Excel worksheet** on the canvas. Reads active Excel worksheet into a flow variable.

**Demonstration.**

```text
**Get active Excel worksheet**
- Excel instance: `%ExcelInstance%`
Produces:
- `%SheetName%` (Text value)
- `%SheetIndex%` (Numeric value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Get all Excel worksheets

- **Id:** `excel/get-all-excel-worksheets`
- **Kind:** native-action
- **Purpose:** Reads all Excel worksheets into a flow variable.

**Use case.** In the monthly close workbook, drop **Get all Excel worksheets** on the canvas. Reads all Excel worksheets into a flow variable.

**Demonstration.**

```text
**Get all Excel worksheets**
- Excel instance: `%ExcelInstance%`
Produces:
- `%SheetNames%` (List of Text values)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Get column name on Excel worksheet

- **Id:** `excel/get-column-name-on-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Reads column name on Excel worksheet into a flow variable.

**Use case.** In the monthly close workbook, drop **Get column name on Excel worksheet** on the canvas. Reads column name on Excel worksheet into a flow variable.

**Demonstration.**

```text
**Get column name on Excel worksheet**
- Column number: `1`
Produces:
- `%ColumnName%` (Text value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Get empty cell

- **Id:** `excel/get-empty-cell`
- **Kind:** native-action
- **Purpose:** Reads empty cell into a flow variable.

**Use case.** In the monthly close workbook, drop **Get empty cell** on the canvas. Reads empty cell into a flow variable.

**Demonstration.**

```text
**Get empty cell**
- Excel instance: `%ExcelInstance%`
- Operation: `First empty cell`
- Search direction: `By row`
- Search in: `Named cells`
- Cells name: `INV-1042`
- Column: `Amount`
- Row: `1`
- Start column: `INV-1042`
- … 3 more parameter(s) in the action modal
Produces:
- `%EmptyCellColumnIndex%` (Numeric value)
- `%EmptyCellRowIndex%` (Numeric value)
- `%EmptyCells%` (Datatable)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Get first free column/row from Excel worksheet

- **Id:** `excel/get-first-free-column-row-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Reads first free column/row from Excel worksheet into a flow variable.

**Use case.** In the monthly close workbook, drop **Get first free column/row from Excel worksheet** on the canvas. Reads first free column/row from Excel worksheet into a flow variable.

**Demonstration.**

```text
**Get first free column/row from Excel worksheet**
- Excel instance: `%ExcelInstance%`
Produces:
- `%FirstFreeColumn%` (Numeric value)
- `%FirstFreeRow%` (Numeric value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Get first free row on column from Excel worksheet

- **Id:** `excel/get-first-free-row-on-column-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Reads first free row on column from Excel worksheet into a flow variable.

**Use case.** In the monthly close workbook, drop **Get first free row on column from Excel worksheet** on the canvas. Reads first free row on column from Excel worksheet into a flow variable.

**Demonstration.**

```text
**Get first free row on column from Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Column: `Amount`
Produces:
- `%FirstFreeRowOnColumn%` (Numeric value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Get selected cell range from Excel worksheet

- **Id:** `excel/get-selected-cell-range-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Reads selected cell range from Excel worksheet into a flow variable.

**Use case.** In the monthly close workbook, drop **Get selected cell range from Excel worksheet** on the canvas. Reads selected cell range from Excel worksheet into a flow variable.

**Demonstration.**

```text
**Get selected cell range from Excel worksheet**
- Excel instance: `%ExcelInstance%`
Produces:
- `%FirstColumnIndex%` (Numeric value)
- `%FirstRowIndex%` (Numeric value)
- `%LastColumnIndex%` (Numeric value)
- `%LastRowIndex%` (Numeric value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Get table range from Excel worksheet

- **Id:** `excel/get-table-range-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Reads table range from Excel worksheet into a flow variable.

**Use case.** In the monthly close workbook, drop **Get table range from Excel worksheet** on the canvas. Reads table range from Excel worksheet into a flow variable.

**Demonstration.**

```text
**Get table range from Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Table name: `INV-1042`
- Is pivot: `False`
Produces:
- `%FirstColumnIndex%` (Numeric value)
- `%FirstRowIndex%` (Numeric value)
- `%LastColumnIndex%` (Numeric value)
- `%LastRowIndex%` (Numeric value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Insert column to Excel worksheet

- **Id:** `excel/insert-column-to-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Inserts column to Excel worksheet.

**Use case.** In the monthly close workbook, drop **Insert column to Excel worksheet** on the canvas. Inserts column to Excel worksheet.

**Demonstration.**

```text
**Insert column to Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Column: `Amount`
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Insert row to Excel worksheet

- **Id:** `excel/insert-row-to-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Inserts row to Excel worksheet.

**Use case.** In the monthly close workbook, drop **Insert row to Excel worksheet** on the canvas. Inserts row to Excel worksheet.

**Demonstration.**

```text
**Insert row to Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Row index: `1`
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Launch Excel

- **Id:** `excel/launch-excel`
- **Kind:** native-action
- **Purpose:** Starts Excel and returns an instance later actions can reuse.

**Use case.** Open or create the workbook every later Excel action will share as ExcelInstance.

**Demonstration.**

```text
**Launch Excel**
- Launch Excel: `With a blank document`
- Document path: `C:\RPA\Close\FY26-P9.xlsx`
- Make instance visible: `True`
- Nest under a new Excel process: `False`
- Password: `%Credential.Password%  (sensitive)`
- Open as ReadOnly: `False`
- Load add-ins and macros: `False`
Produces:
- `%ExcelInstance%` (Excel instance)
```

**Analogy.** Opening the ledger so a pen can write in it.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel. Keep the produced instance/connection and pass it into every later action in this module.

### Lookup range in Excel worksheet

- **Id:** `excel/lookup-range-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Finds and returns the result of Excel's LOOKUP function.

**Use case.** In the monthly close workbook, drop **Lookup range in Excel worksheet** on the canvas. Finds and returns the result of Excel's LOOKUP function.

**Demonstration.**

```text
**Lookup range in Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Lookup value: `INV-1042`
- Ranges format: `Named cells`
- Cells name: `INV-1042`
- Start column: `INV-1042`
- Start row: `1`
- End column: `INV-1042`
- End row: `1`
- … 6 more parameter(s) in the action modal
Produces:
- `%LookupResult%` (Text value)
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Paste cells to Excel worksheet

- **Id:** `excel/paste-cells-to-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Pastes a range of cells to the active worksheet of an Excel instance.

**Use case.** In the monthly close workbook, drop **Paste cells to Excel worksheet** on the canvas. Pastes a range of cells to the active worksheet of an Excel instance.

**Demonstration.**

```text
**Paste cells to Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Paste mode: `On specified cell`
- Column: `Amount`
- Row: `1`
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Read formula from Excel

- **Id:** `excel/read-formula-from-excel`
- **Kind:** native-action
- **Purpose:** Reads formula from Excel.

**Use case.** In the monthly close workbook, drop **Read formula from Excel** on the canvas. Reads formula from Excel.

**Demonstration.**

```text
**Read formula from Excel**
- Excel instance: `%ExcelInstance%`
- Retrieve: `The formula of a single cell`
- Start column: `INV-1042`
- Start row: `1`
- Name: `INV-1042`
Produces:
- `%CellFormula%` (Text value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Read from Excel worksheet

- **Id:** `excel/read-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Reads from Excel worksheet.

**Use case.** In the monthly close workbook, drop **Read from Excel worksheet** on the canvas. Reads from Excel worksheet.

**Demonstration.**

```text
**Read from Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Retrieve: `The value of a single cell`
- Start column: `INV-1042`
- Start row: `1`
- End column: `INV-1042`
- End row: `1`
- Get cell(s) contents as: `Typed values`
- First line of range contains column names: `False`
Produces:
- `%ExcelData%` (General value)
- `%ExcelData%` (Datatable)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Rename Excel worksheet

- **Id:** `excel/rename-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Renames excel worksheet.

**Use case.** In the monthly close workbook, drop **Rename Excel worksheet** on the canvas. Renames excel worksheet.

**Demonstration.**

```text
**Rename Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Rename worksheet with: `TrialBalance`
- Worksheet index: `TrialBalance`
- Worksheet name: `TrialBalance`
- Worksheet new name: `TrialBalance`
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Resize columns/rows in Excel worksheet

- **Id:** `excel/resize-columns-rows-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Resizes a selection of columns or rows in the active worksheet of an Excel instance.

**Use case.** In the monthly close workbook, drop **Resize columns/rows in Excel worksheet** on the canvas. Resizes a selection of columns or rows in the active worksheet of an Excel instance.

**Demonstration.**

```text
**Resize columns/rows in Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Resize target: `Column`
- Selection range: `Single`
- Column: `Amount`
- Start column: `INV-1042`
- End column: `INV-1042`
- Row: `1`
- Start row: `1`
- … 4 more parameter(s) in the action modal
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Run Excel macro

- **Id:** `excel/run-excel-macro`
- **Kind:** native-action
- **Purpose:** Runs excel macro.

**Use case.** In the monthly close workbook, drop **Run Excel macro** on the canvas. Runs excel macro.

**Demonstration.**

```text
**Run Excel macro**
- Excel instance: `%ExcelInstance%`
- Macro: `RefreshAll`
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Save Excel

- **Id:** `excel/save-excel`
- **Kind:** native-action
- **Purpose:** Saves excel.

**Use case.** In the monthly close workbook, drop **Save Excel** on the canvas. Saves excel.

**Demonstration.**

```text
**Save Excel**
- Excel instance: `%ExcelInstance%`
- Save mode: `Save document`
- Document format: `%XmlDoc%`
- Document path: `C:\RPA\Close\FY26-P9.xlsx`
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Select cells in Excel worksheet

- **Id:** `excel/select-cells-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Selects cells in Excel worksheet.

**Use case.** In the monthly close workbook, drop **Select cells in Excel worksheet** on the canvas. Selects cells in Excel worksheet.

**Demonstration.**

```text
**Select cells in Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Select: `Absolutely specified cell`
- X Axis Direction: `Left`
- Start column: `INV-1042`
- X Offset: `1`
- Start row: `1`
- End column: `INV-1042`
- Y Axis Direction: `Above`
- … 2 more parameter(s) in the action modal
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Set active Excel worksheet

- **Id:** `excel/set-active-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Writes active Excel worksheet.

**Use case.** In the monthly close workbook, drop **Set active Excel worksheet** on the canvas. Writes active Excel worksheet.

**Demonstration.**

```text
**Set active Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Activate worksheet with: `TrialBalance`
- Worksheet index: `TrialBalance`
- Worksheet name: `TrialBalance`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Set color of cells in Excel worksheet

- **Id:** `excel/set-color-of-cells-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Writes color of cells in Excel worksheet.

**Use case.** In the monthly close workbook, drop **Set color of cells in Excel worksheet** on the canvas. Writes color of cells in Excel worksheet.

**Demonstration.**

```text
**Set color of cells in Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Set color of: `Single cell`
- Start column: `INV-1042`
- Start row: `1`
- End column: `INV-1042`
- End row: `1`
- Cells name: `INV-1042`
- Color format: `Name`
- … 2 more parameter(s) in the action modal
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Sort cells in Excel worksheet

- **Id:** `excel/sort-cells-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Sorts cells in Excel worksheet.

**Use case.** In the monthly close workbook, drop **Sort cells in Excel worksheet** on the canvas. Sorts cells in Excel worksheet.

**Demonstration.**

```text
**Sort cells in Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Sort column in: `Active sheet`
- Table name: `INV-1042`
- Range: `Named cells`
- Cells name: `INV-1042`
- Start column: `INV-1042`
- Start row: `1`
- End column: `INV-1042`
- … 3 more parameter(s) in the action modal
```

**Analogy.** One tool in that kit: opening a paper ledger, writing lines, closing the book.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.

### Write to Excel worksheet

- **Id:** `excel/write-to-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Writes to Excel worksheet.

**Use case.** In the monthly close workbook, drop **Write to Excel worksheet** on the canvas. Writes to Excel worksheet.

**Demonstration.**

```text
**Write to Excel worksheet**
- Excel instance: `%ExcelInstance%`
- Value to write: `(set in designer)`
- Write mode: `On specified cell`
- Column: `Amount`
- Row: `1`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.
