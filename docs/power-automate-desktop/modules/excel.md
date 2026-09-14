# Excel

Launch Excel, read and write cells, and run worksheet operations.

This page documents every **native action** in this group (41 items).

## Actions

### Activate cell in Excel worksheet

- **Inventory id:** `excel/activate-cell-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Activate a cell in the active worksheet of an Excel instance, by providing column, row, and offset.
- **Key inputs:** `Excel instance` (Excel instance); `Activate` (Absolutely specified cell, Relatively specified cell); `Column` (Text value); `Direction` (Left, Right, Above, Below); `Offset from active cell` (Numeric value); `Row` (Numeric value)
- **Produces:** None listed
- **Exceptions:** `Failed to activate cell`
- **Microsoft Learn:** [Activate cell in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#activatecellinexcel)

### Add new worksheet

- **Inventory id:** `excel/add-new-worksheet`
- **Kind:** native-action
- **Purpose:** Adds new worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `New worksheet name` (Text value); `Add worksheet as` (First worksheet, Last worksheet)
- **Produces:** None listed
- **Exceptions:** `A worksheet with the same name already exists`; `Failed to add worksheet`
- **Microsoft Learn:** [Add new worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#addworksheet)

### Append cells in Excel worksheet

- **Inventory id:** `excel/append-cells-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Appends a range of cells to the active worksheet of an Excel instance.
- **Key inputs:** `Excel instance` (Excel instance); `Append mode` (To active sheet, To named cells); `Name` (Text value); `First row has headers` (Boolean value); `Starting column` (Text value; optional); `Starting column header` (Text value; optional)
- **Produces:** None listed
- **Exceptions:** `Failed to append cells`
- **Microsoft Learn:** [Append cells in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#appendcells)

### Attach to running Excel

- **Inventory id:** `excel/attach-to-running-excel`
- **Kind:** native-action
- **Purpose:** Connects the flow to running Excel that is already running.
- **Key inputs:** `Document name` (File)
- **Produces:** `ExcelInstance` (Excel instance)
- **Exceptions:** `Specified Excel document not found`; `Failed to attach to Excel document`
- **Microsoft Learn:** [Attach to running Excel](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#attach)

### Auto fill cells in Excel worksheet

- **Inventory id:** `excel/auto-fill-cells-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Auto fills a range with data, based on the data of another range, in the active worksheet of an Excel instance.
- **Key inputs:** `Excel instance` (Excel instance); `Ranges format` (Named cells, Specific ranges); `Source cells name` (Text value); `Destination cells name` (Text value); `Start column` (Text value); `Start row` (Numeric value); `Source end column` (Text value); `Source end row` (Numeric value); `Destination end column` (Text value); `Destination end row` (Numeric value)
- **Produces:** None listed
- **Exceptions:** `Failed to auto fill cells`
- **Microsoft Learn:** [Auto fill cells in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#autofillcells)

### Clear cells in Excel worksheet

- **Inventory id:** `excel/clear-cells-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Clears cells in Excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Clear` (Range of cells, Range of cells relative to active cell, Named cells, Single cell); `X Axis Direction` (Left, Right); `Start column` (Text value); `X Offset` (Numeric value); `Start row` (Numeric value); `End column` (Text value); `Y Axis Direction` (Above, Below); `End row` (Numeric value); `Y Offset` (Numeric value); `Name` (Text value); `Column` (Text value); `Row` (Numeric value)
- **Produces:** None listed
- **Exceptions:** `Failed to clear cells`
- **Microsoft Learn:** [Clear cells in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#clearcellsfromexcel)

### Clear filters in Excel worksheet

- **Inventory id:** `excel/clear-filters-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Clears filters in Excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Clear filters in` (Active sheet, Table); `Table name` (Text value); `Clear filters from specific column` (Boolean value; optional); `Clear filter in column` (Text value)
- **Produces:** None listed
- **Exceptions:** `Failed to clear filter on cells in worksheet`
- **Microsoft Learn:** [Clear filters in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#clearfilterfromexcel)

### Close Excel

- **Inventory id:** `excel/close-excel`
- **Kind:** native-action
- **Purpose:** Closes excel.
- **Key inputs:** `Excel instance` (Excel instance); `Before closing Excel` (Do not save document, Save document, Save document as); `Document format` (Default (From Extension), Excel Workbook (.xlsx), Excel Workbook Macro Enabled (.xlsm), Excel 97-2003 Workbook (.xls), Web Page (.htm, .html), Excel Template (.xltx), Excel Template Macro Enabled (.xltm), Excel 97-2003 Template (.xlt), Text (.txt), Unicode Text (.txt), Text Macintosh (.txt), Text DOS (.txt), XML Spreadsheet (.xml), Excel 95 (.xls), CSV (.csv), DIF (.dif), SYLK (.slk), Excel add-in (.xlam), Excel 97-2003 add-in (.xla), Strict Open XML Workbook (.xlsx), OpenDocument Spreadsheet (.ods), XML Data (.xml), Excel Binary Workbook (.xlsb)); `Document path` (File)
- **Produces:** None listed
- **Exceptions:** `Failed to save Excel document`; `Failed to close Excel instance`
- **Microsoft Learn:** [Close Excel](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#closeexcel)

### Copy cells from Excel worksheet

- **Inventory id:** `excel/copy-cells-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Copies cells from Excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Copy mode` (Single Cell's Values, Values from a Range of Cells, Values from Selection); `Start column` (Text value); `Start row` (Numeric value); `End column` (Text value); `End row` (Numeric value)
- **Produces:** None listed
- **Exceptions:** `Failed to copy cells`
- **Microsoft Learn:** [Copy cells from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#copycellsfromexcel)

### Copy Excel worksheet

- **Inventory id:** `excel/copy-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Copies excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Copy worksheet with` (Index, Name); `Worksheet index` (Numeric value); `Worksheet name` (Text value); `Target Excel instance` (Excel instance); `Worksheet new name` (Text value); `Paste worksheet as` (First worksheet, Last worksheet)
- **Produces:** None listed
- **Exceptions:** `Failed to copy worksheet`; `Can't copy worksheet with this name`
- **Microsoft Learn:** [Copy Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#copyexcelworksheet)

### Delete column from Excel worksheet

- **Inventory id:** `excel/delete-column-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Deletes column from Excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Delete column` (Text value)
- **Produces:** None listed
- **Exceptions:** `Can't find column`; `Failed to delete column`
- **Microsoft Learn:** [Delete column from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#deletecolumn)

### Delete Excel worksheet

- **Inventory id:** `excel/delete-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Deletes excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Delete worksheet with` (Index, Name); `Worksheet index` (Numeric value); `Worksheet name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Can't find worksheet`; `Failed to delete worksheet`
- **Microsoft Learn:** [Delete Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#deleteworksheet)

### Delete from Excel worksheet

- **Inventory id:** `excel/delete-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Deletes from Excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Retrieve` (The value of a single cell, Values from a range of cells); `Start column` (Text value); `Start row` (Numeric value); `End column` (Text value); `End row` (Numeric value); `Shift direction` (Left, Up)
- **Produces:** None listed
- **Exceptions:** `Failed to delete cells`
- **Microsoft Learn:** [Delete from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#deletecellsaction)

### Delete row from Excel worksheet

- **Inventory id:** `excel/delete-row-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Deletes row from Excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Delete row` (Numeric value)
- **Produces:** None listed
- **Exceptions:** `Can't find row`; `Failed to delete row`
- **Microsoft Learn:** [Delete row from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#deleterow)

### Filter cells in Excel worksheet

- **Inventory id:** `excel/filter-cells-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Filters cells in Excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Filter column in` (Active sheet, Table, Range); `Table name` (Text value); `Range` (Named cells, Specific range); `Cells name` (Text value); `Start column` (Text value); `Start row` (Numeric value); `End column` (Text value); `End row` (Numeric value); `Column to filter` (Text value); `Filters to apply` (Filtering rules as defined by the user; optional)
- **Produces:** None listed
- **Exceptions:** `Failed to apply filter on cells in worksheet`
- **Microsoft Learn:** [Filter cells in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#filtercellsfromexcel)

### Find and replace cells in Excel worksheet

- **Inventory id:** `excel/find-and-replace-cells-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Finds and replace cells in Excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Search mode` (Find, Find and replace); `All matches` (Boolean value); `Text to find` (Text value); `Text to replace with` (Text value); `Match case` (Boolean value); `Match entire cell contents` (Boolean value); `Search by` (Rows, Columns)
- **Produces:** `FoundColumnIndex` (Numeric value); `FoundRowIndex` (Numeric value); `Cells` (Datatable)
- **Exceptions:** `Failed to find and/or replace text`
- **Microsoft Learn:** [Find and replace cells in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#findandreplaceaction)

### Get active cell on Excel worksheet

- **Inventory id:** `excel/get-active-cell-on-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Reads active cell on Excel worksheet into a flow variable.
- **Key inputs:** `Excel instance` (Excel instance)
- **Produces:** `ActiveCellColumnIndex` (Numeric value); `ActiveCellRowIndex` (Numeric value)
- **Exceptions:** `Failed to get active cell`
- **Microsoft Learn:** [Get active cell on Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#getactivecell)

### Get active Excel worksheet

- **Inventory id:** `excel/get-active-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Reads active Excel worksheet into a flow variable.
- **Key inputs:** `Excel instance` (Excel instance)
- **Produces:** `SheetName` (Text value); `SheetIndex` (Numeric value)
- **Exceptions:** `Failed to retrieve active worksheet`
- **Microsoft Learn:** [Get active Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#getactiveworksheet)

### Get all Excel worksheets

- **Inventory id:** `excel/get-all-excel-worksheets`
- **Kind:** native-action
- **Purpose:** Reads all Excel worksheets into a flow variable.
- **Key inputs:** `Excel instance` (Excel instance)
- **Produces:** `SheetNames` (List of Text values)
- **Exceptions:** `Failed to retrieve all worksheet names`
- **Microsoft Learn:** [Get all Excel worksheets](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#getallworksheets)

### Get column name on Excel worksheet

- **Inventory id:** `excel/get-column-name-on-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Reads column name on Excel worksheet into a flow variable.
- **Key inputs:** `Column number` (Numeric value)
- **Produces:** `ColumnName` (Text value)
- **Exceptions:** none listed
- **Microsoft Learn:** [Get column name on Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#getcolumnname)

### Get empty cell

- **Inventory id:** `excel/get-empty-cell`
- **Kind:** native-action
- **Purpose:** Reads empty cell into a flow variable.
- **Key inputs:** `Excel instance` (Excel instance); `Operation` (First empty cell, First empty cell in column, First empty cell in row, All empty cells); `Search direction` (By row, By column); `Search in` (Named cells, Specific range); `Cells name` (Text value); `Column` (Text value); `Row` (Numeric value); `Start column` (Text value); `Start row` (Numeric value); `End column` (Text value); `End row` (Numeric value)
- **Produces:** `EmptyCellColumnIndex` (Numeric value); `EmptyCellRowIndex` (Numeric value); `EmptyCells` (Datatable)
- **Exceptions:** `Get empty cells failed`
- **Microsoft Learn:** [Get empty cell](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#getemptycellfromexcel)

### Get first free column/row from Excel worksheet

- **Inventory id:** `excel/get-first-free-column-row-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Reads first free column/row from Excel worksheet into a flow variable.
- **Key inputs:** `Excel instance` (Excel instance)
- **Produces:** `FirstFreeColumn` (Numeric value); `FirstFreeRow` (Numeric value)
- **Exceptions:** `Failed to retrieve first free column/row`
- **Microsoft Learn:** [Get first free column/row from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#getfirstfreecolumnrow)

### Get first free row on column from Excel worksheet

- **Inventory id:** `excel/get-first-free-row-on-column-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Reads first free row on column from Excel worksheet into a flow variable.
- **Key inputs:** `Excel instance` (Excel instance); `Column` (Text value)
- **Produces:** `FirstFreeRowOnColumn` (Numeric value)
- **Exceptions:** `Failed to retrieve first free row`
- **Microsoft Learn:** [Get first free row on column from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#getfirstfreerowoncolumn)

### Get selected cell range from Excel worksheet

- **Inventory id:** `excel/get-selected-cell-range-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Reads selected cell range from Excel worksheet into a flow variable.
- **Key inputs:** `Excel instance` (Excel instance)
- **Produces:** `FirstColumnIndex` (Numeric value); `FirstRowIndex` (Numeric value); `LastColumnIndex` (Numeric value); `LastRowIndex` (Numeric value)
- **Exceptions:** `Failed to retrieve the selected range of cells`
- **Microsoft Learn:** [Get selected cell range from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#getselectedcellrange)

### Get table range from Excel worksheet

- **Inventory id:** `excel/get-table-range-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Reads table range from Excel worksheet into a flow variable.
- **Key inputs:** `Excel instance` (Excel instance); `Table name` (Text value); `Is pivot` (Boolean value)
- **Produces:** `FirstColumnIndex` (Numeric value); `FirstRowIndex` (Numeric value); `LastColumnIndex` (Numeric value); `LastRowIndex` (Numeric value)
- **Exceptions:** `Failed to get the range from table`
- **Microsoft Learn:** [Get table range from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#gettablerange)

### Insert column to Excel worksheet

- **Inventory id:** `excel/insert-column-to-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Inserts column to Excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Column` (Text value)
- **Produces:** None listed
- **Exceptions:** `Can't find column`; `Failed to insert column`
- **Microsoft Learn:** [Insert column to Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#insertcolumn)

### Insert row to Excel worksheet

- **Inventory id:** `excel/insert-row-to-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Inserts row to Excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Row index` (Numeric value)
- **Produces:** None listed
- **Exceptions:** `Can't find row`; `Failed to insert row`
- **Microsoft Learn:** [Insert row to Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#insertrow)

### Launch Excel

- **Inventory id:** `excel/launch-excel`
- **Kind:** native-action
- **Purpose:** Starts Excel and returns an instance later actions can reuse.
- **Key inputs:** `Launch Excel` (With a blank document, and open the following document); `Document path` (File); `Make instance visible` (Boolean value); `Nest under a new Excel process` (Boolean value); `Password` (Direct encrypted input or Text value; optional); `Open as ReadOnly` (Boolean value); `Load add-ins and macros` (Boolean value)
- **Produces:** `ExcelInstance` (Excel instance)
- **Exceptions:** `Failed to launch Excel`; `Failed to open Excel document`
- **Microsoft Learn:** [Launch Excel](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#launchexcel)

### Lookup range in Excel worksheet

- **Inventory id:** `excel/lookup-range-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Finds and returns the result of Excel's LOOKUP function.
- **Key inputs:** `Excel instance` (Excel instance); `Lookup value` (Text value); `Ranges format` (Named cells, Specific ranges); `Cells name` (Text value); `Start column` (Text value); `Start row` (Numeric value); `End column` (Text value); `End row` (Numeric value); `Array form` (Boolean value); `Cells name of results source` (Text value; optional); `Start column of results source` (Text value); `Start row of results source` (Numeric value); `End column of results source` (Text value); `End row of results source` (Numeric value)
- **Produces:** `LookupResult` (Text value)
- **Exceptions:** `Failed to lookup`
- **Microsoft Learn:** [Lookup range in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#lookuprange)

### Paste cells to Excel worksheet

- **Inventory id:** `excel/paste-cells-to-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Pastes a range of cells to the active worksheet of an Excel instance.
- **Key inputs:** `Excel instance` (Excel instance); `Paste mode` (On specified cell, On currently active cell); `Column` (Text value); `Row` (Numeric value)
- **Produces:** None listed
- **Exceptions:** `Failed to paste cells`
- **Microsoft Learn:** [Paste cells to Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#pastecellstoexcel)

### Read formula from Excel

- **Inventory id:** `excel/read-formula-from-excel`
- **Kind:** native-action
- **Purpose:** Reads formula from Excel.
- **Key inputs:** `Excel instance` (Excel instance); `Retrieve` (The formula of a single cell, The formula of a named cell); `Start column` (Text value); `Start row` (Numeric value); `Name` (Text value)
- **Produces:** `CellFormula` (Text value)
- **Exceptions:** `Failed to read the formula from cell`
- **Microsoft Learn:** [Read formula from Excel](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#readcellformula)

### Read from Excel worksheet

- **Inventory id:** `excel/read-from-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Reads from Excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Retrieve` (The value of a single cell, Values from a range of cells, Values from selection, All available values from worksheet); `Start column` (Text value); `Start row` (Numeric value); `End column` (Text value); `End row` (Numeric value); `Get cell(s) contents as` (Typed values,Plain text,Formatted text values); `First line of range contains column names` (Boolean value)
- **Produces:** `ExcelData` (General value); `ExcelData` (Datatable)
- **Exceptions:** `Failed to read cell values`
- **Microsoft Learn:** [Read from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#readfromexcel)

### Rename Excel worksheet

- **Inventory id:** `excel/rename-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Renames excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Rename worksheet with` (Index, Name); `Worksheet index` (Numeric value); `Worksheet name` (Text value); `Worksheet new name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Can't find worksheet`; `Failed to rename worksheet`
- **Microsoft Learn:** [Rename Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#renameworksheet)

### Resize columns/rows in Excel worksheet

- **Inventory id:** `excel/resize-columns-rows-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Resizes a selection of columns or rows in the active worksheet of an Excel instance.
- **Key inputs:** `Excel instance` (Excel instance); `Resize target` (Column, Row); `Selection range` (Single, Range, All available); `Column` (Text value); `Start column` (Text value); `End column` (Text value); `Row` (Numeric value); `Start row` (Numeric value); `End row` (Numeric value); `Resize type` (Autofit, Custom size); `Width` (Numeric value); `Height` (Numeric value)
- **Produces:** None listed
- **Exceptions:** `Failed to resize columns/rows`
- **Microsoft Learn:** [Resize columns/rows in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#resizecolumnsorrowsaction)

### Run Excel macro

- **Inventory id:** `excel/run-excel-macro`
- **Kind:** native-action
- **Purpose:** Runs excel macro.
- **Key inputs:** `Excel instance` (Excel instance); `Macro` (Text value)
- **Produces:** None listed
- **Exceptions:** `Failed to run macro`
- **Microsoft Learn:** [Run Excel macro](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#runmacro)

### Save Excel

- **Inventory id:** `excel/save-excel`
- **Kind:** native-action
- **Purpose:** Saves excel.
- **Key inputs:** `Excel instance` (Excel instance); `Save mode` (Save document, Save document as); `Document format` (Default (From Extension), Excel Workbook (.xlsx), Excel Workbook Macro Enabled (.xlsm), Excel 97-2003 Workbook (.xls), Web Page (.htm, .html), Excel Template (.xltx), Excel Template Macro Enabled (.xltm), Excel 97-2003 Template (.xlt), Text (.txt), Unicode Text (.txt), Text Macintosh (.txt), Text DOS (.txt), XML Spreadsheet (.xml), Excel 95 (.xls), CSV (.csv), DIF (.dif), SYLK (.slk), Excel add-in (.xlam), Excel 97-2003 add-In (.xla), Strict Open XML Workbook (.xlsx), OpenDocument Spreadsheet (.ods), XML Data (.xml), Excel Binary Workbook (.xlsb)); `Document path` (File)
- **Produces:** None listed
- **Exceptions:** `Failed to save Excel document`
- **Microsoft Learn:** [Save Excel](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#saveexcel)

### Select cells in Excel worksheet

- **Inventory id:** `excel/select-cells-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Selects cells in Excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Select` (Absolutely specified cell, Relatively specified cell); `X Axis Direction` (Left, Right); `Start column` (Text value); `X Offset` (Numeric value); `Start row` (Numeric value); `End column` (Text value); `Y Axis Direction` (Above, Below); `End row` (Numeric value); `Y Offset` (Numeric value)
- **Produces:** None listed
- **Exceptions:** `Failed to select cells`
- **Microsoft Learn:** [Select cells in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#selectcellsfromexcel)

### Set active Excel worksheet

- **Inventory id:** `excel/set-active-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Writes active Excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Activate worksheet with` (Index, Name); `Worksheet index` (Numeric value); `Worksheet name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Can't find worksheet`; `Failed to activate worksheet`
- **Microsoft Learn:** [Set active Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#setactiveworksheet)

### Set color of cells in Excel worksheet

- **Inventory id:** `excel/set-color-of-cells-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Writes color of cells in Excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Set color of` (Single cell, Range of cells, Named cells); `Start column` (Text value); `Start row` (Numeric value); `End column` (Text value); `End row` (Numeric value); `Cells name` (Text value); `Color format` (Name, Hexadecimal value); `Color name` (Text value); `Color hexadecimal value` (Text value)
- **Produces:** None listed
- **Exceptions:** `Failed to set color`
- **Microsoft Learn:** [Set color of cells in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#setcolor)

### Sort cells in Excel worksheet

- **Inventory id:** `excel/sort-cells-in-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Sorts cells in Excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Sort column in` (Active sheet, Table, Range); `Table name` (Text value); `Range` (Named cells, Specific range); `Cells name` (Text value); `Start column` (Text value); `Start row` (Numeric value); `End column` (Text value); `End row` (Numeric value); `Sort by` (Sorting rules as defined by the user; optional); `First row is header` (Boolean value; optional)
- **Produces:** None listed
- **Exceptions:** `Failed to sort cells in worksheet`
- **Microsoft Learn:** [Sort cells in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#sortcellsfromexcel)

### Write to Excel worksheet

- **Inventory id:** `excel/write-to-excel-worksheet`
- **Kind:** native-action
- **Purpose:** Writes to Excel worksheet.
- **Key inputs:** `Excel instance` (Excel instance); `Value to write` (General value); `Write mode` (On specified cell, On currently active cell); `Column` (Text value); `Row` (Numeric value)
- **Produces:** None listed
- **Exceptions:** `Failed to write value to Excel`
- **Microsoft Learn:** [Write to Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#writetoexcel)
