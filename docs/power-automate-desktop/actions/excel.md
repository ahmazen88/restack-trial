# Excel

Launch Excel, read and write cells, and manage worksheets and macros.

- Actions in this module: **41**
- Official docs: [Excel actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel)

## Actions

### Resize columns/rows in Excel worksheet

Resizes a selection of columns or rows in the active worksheet of an Excel instance.

Designer name: **Resize columns/rows in Excel worksheet**. Official reference: [Excel / Resize columns/rows in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#resizecolumnsorrowsaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Resize target | Choice | Column, Row | Column |
| Selection range | Choice | Single, Range, All available | Single |
| Column | Required | Text value | — |
| Start column | Required | Text value | — |
| End column | Required | Text value | — |
| Row | Required | Numeric value | — |
| Start row | Required | Numeric value | — |
| End row | Required | Numeric value | — |
| Resize type | Choice | Autofit, Custom size | Autofit |
| Width | Required | Numeric value | — |
| Height | Required | Numeric value | — |

Produces no variables.

**On error:** `Failed to resize columns/rows`.

---

### Run Excel macro

Runs a specified macro on the document of an Excel instance.

Designer name: **Run Excel macro**. Official reference: [Excel / Run Excel macro](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#runmacro).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Macro | Required | Text value | — |

Produces no variables.

**On error:** `Failed to run macro`.

---

### Get active Excel worksheet

Returns an Excel document's active worksheet.

Designer name: **Get active Excel worksheet**. Official reference: [Excel / Get active Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#getactiveworksheet).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |

**Outputs**

| Variable | Type |
|---|---|
| SheetName | Text value |
| SheetIndex | Numeric value |

**On error:** `Failed to retrieve active worksheet`.

---

### Get all Excel worksheets

Returns all worksheet names of an Excel document.

Designer name: **Get all Excel worksheets**. Official reference: [Excel / Get all Excel worksheets](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#getallworksheets).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |

**Outputs**

| Variable | Type |
|---|---|
| SheetNames | List of Text values |

**On error:** `Failed to retrieve all worksheet names`.

---

### Delete Excel worksheet

Deletes a specific worksheet from an Excel instance.

Designer name: **Delete Excel worksheet**. Official reference: [Excel / Delete Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#deleteworksheet).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Delete worksheet with | Choice | Index, Name | Name |
| Worksheet index | Required | Numeric value | — |
| Worksheet name | Required | Text value | — |

Produces no variables.

**On error:** `Can't find worksheet`, `Failed to delete worksheet`.

---

### Rename Excel worksheet

Renames a specific worksheet of an Excel instance.

Designer name: **Rename Excel worksheet**. Official reference: [Excel / Rename Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#renameworksheet).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Rename worksheet with | Choice | Index, Name | Name |
| Worksheet index | Required | Numeric value | — |
| Worksheet name | Required | Text value | — |
| Worksheet new name | Required | Text value | — |

Produces no variables.

**On error:** `Can't find worksheet`, `Failed to rename worksheet`.

---

### Copy Excel worksheet

Copies a worksheet from an Excel document and paste it to the Excel document of the same or different Excel instance.

Designer name: **Copy Excel worksheet**. Official reference: [Excel / Copy Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#copyexcelworksheet).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Copy worksheet with | Choice | Index, Name | Name |
| Worksheet index | Required | Numeric value | — |
| Worksheet name | Required | Text value | — |
| Target Excel instance | Νο | Excel instance | — |
| Worksheet new name | Required | Text value | — |
| Paste worksheet as | Choice | First worksheet, Last worksheet | First worksheet |

Produces no variables.

**On error:** `Failed to copy worksheet`, `Can't copy worksheet with this name`.

---

### Activate cell in Excel worksheet

Activate a cell in the active worksheet of an Excel instance, by providing column, row, and offset.

Designer name: **Activate cell in Excel worksheet**. Official reference: [Excel / Activate cell in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#activatecellinexcel).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Activate | Choice | Absolutely specified cell, Relatively specified cell | Absolutely specified cell |
| Column | Required | Text value | — |
| Direction | Choice | Left, Right, Above, Below | Left |
| Offset from active cell | Required | Numeric value | — |
| Row | Required | Numeric value | — |

Produces no variables.

**On error:** `Failed to activate cell`.

---

### Select cells in Excel worksheet

Selects a range of cells in the active worksheet of an Excel instance.

Designer name: **Select cells in Excel worksheet**. Official reference: [Excel / Select cells in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#selectcellsfromexcel).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Select | Choice | Absolutely specified cell, Relatively specified cell | Absolutely specified cell |
| X Axis Direction | Choice | Left, Right | Left |
| Start column | Required | Text value | — |
| X Offset | Required | Numeric value | — |
| Start row | Required | Numeric value | — |
| End column | Required | Text value | — |
| Y Axis Direction | Choice | Above, Below | Above |
| End row | Required | Numeric value | — |
| Y Offset | Required | Numeric value | — |

Produces no variables.

**On error:** `Failed to select cells`.

---

### Get selected cell range from Excel worksheet

Retrieve the selected range of cells in a structure consisting of first column, first row, last column, and last row.

Designer name: **Get selected cell range from Excel worksheet**. Official reference: [Excel / Get selected cell range from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#getselectedcellrange).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |

**Outputs**

| Variable | Type |
|---|---|
| FirstColumnIndex | Numeric value |
| FirstRowIndex | Numeric value |
| LastColumnIndex | Numeric value |
| LastRowIndex | Numeric value |

**On error:** `Failed to retrieve the selected range of cells`.

---

### Copy cells from Excel worksheet

Copies a range of cells from the active worksheet of an Excel instance.

Designer name: **Copy cells from Excel worksheet**. Official reference: [Excel / Copy cells from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#copycellsfromexcel).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Copy mode | Choice | Single Cell's Values, Values from a Range of Cells, Values from Selection | Single Cell's Values |
| Start column | Required | Text value | — |
| Start row | Required | Numeric value | — |
| End column | Required | Text value | — |
| End row | Required | Numeric value | — |

Produces no variables.

**On error:** `Failed to copy cells`.

---

### Paste cells to Excel worksheet

Pastes a range of cells to the active worksheet of an Excel instance.

Designer name: **Paste cells to Excel worksheet**. Official reference: [Excel / Paste cells to Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#pastecellstoexcel).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Paste mode | Choice | On specified cell, On currently active cell | On specified cell |
| Column | Required | Text value | — |
| Row | Required | Numeric value | — |

Produces no variables.

**On error:** `Failed to paste cells`.

---

### Delete from Excel worksheet

Deletes a cell or a range of cells from the active worksheet of an Excel instance.

Designer name: **Delete from Excel worksheet**. Official reference: [Excel / Delete from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#deletecellsaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Retrieve | Choice | The value of a single cell, Values from a range of cells | The value of a single cell |
| Start column | Required | Text value | — |
| Start row | Required | Numeric value | — |
| End column | Required | Text value | — |
| End row | Required | Numeric value | — |
| Shift direction | Choice | Left, Up | Left |

Produces no variables.

**On error:** `Failed to delete cells`.

---

### Insert row to Excel worksheet

Inserts a row above a selected row of an Excel instance.

Designer name: **Insert row to Excel worksheet**. Official reference: [Excel / Insert row to Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#insertrow).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Row index | Required | Numeric value | — |

Produces no variables.

**On error:** `Can't find row`, `Failed to insert row`.

---

### Delete row from Excel worksheet

Deletes a selected row from an Excel instance.

Designer name: **Delete row from Excel worksheet**. Official reference: [Excel / Delete row from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#deleterow).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Delete row | Required | Numeric value | — |

Produces no variables.

**On error:** `Can't find row`, `Failed to delete row`.

---

### Insert column to Excel worksheet

Inserts a column to the left of a selected column of an Excel instance.

Designer name: **Insert column to Excel worksheet**. Official reference: [Excel / Insert column to Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#insertcolumn).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Column | Required | Text value | — |

Produces no variables.

**On error:** `Can't find column`, `Failed to insert column`.

---

### Delete column from Excel worksheet

Deletes a selected column from an Excel instance.

Designer name: **Delete column from Excel worksheet**. Official reference: [Excel / Delete column from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#deletecolumn).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Delete column | Required | Text value | — |

Produces no variables.

**On error:** `Can't find column`, `Failed to delete column`.

---

### Find and replace cells in Excel worksheet

Finds text and replaces it with another in the active worksheet of an Excel instance.

Designer name: **Find and replace cells in Excel worksheet**. Official reference: [Excel / Find and replace cells in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#findandreplaceaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Search mode | Choice | Find, Find and replace | Find |
| All matches | Choice | Boolean value | False |
| Text to find | Required | Text value | — |
| Text to replace with | Required | Text value | — |
| Match case | Choice | Boolean value | False |
| Match entire cell contents | Choice | Boolean value | False |
| Search by | Choice | Rows, Columns | Rows |

**Outputs**

| Variable | Type |
|---|---|
| FoundColumnIndex | Numeric value |
| FoundRowIndex | Numeric value |
| Cells | Datatable |

**On error:** `Failed to find and/or replace text`.

---

### Get first free row on column from Excel worksheet

Retrieve the first free row, given the column of the active worksheet.

Designer name: **Get first free row on column from Excel worksheet**. Official reference: [Excel / Get first free row on column from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#getfirstfreerowoncolumn).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Column | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| FirstFreeRowOnColumn | Numeric value |

**On error:** `Failed to retrieve first free row`.

---

### Read formula from Excel

Reads the formula inside a cell in Excel.

Designer name: **Read formula from Excel**. Official reference: [Excel / Read formula from Excel](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#readcellformula).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Retrieve | Choice | The formula of a single cell, The formula of a named cell | The formula of a single cell |
| Start column | Required | Text value | — |
| Start row | Required | Numeric value | — |
| Name | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| CellFormula | Text value |

**On error:** `Failed to read the formula from cell`.

---

### Get table range from Excel worksheet

Returns the range of a table in the active worksheet of an Excel instance.

Designer name: **Get table range from Excel worksheet**. Official reference: [Excel / Get table range from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#gettablerange).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Table name | Required | Text value | — |
| Is pivot | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| FirstColumnIndex | Numeric value |
| FirstRowIndex | Numeric value |
| LastColumnIndex | Numeric value |
| LastRowIndex | Numeric value |

**On error:** `Failed to get the range from table`.

---

### Auto fill cells in Excel worksheet

Auto fills a range with data, based on the data of another range, in the active worksheet of an Excel instance.

Designer name: **Auto fill cells in Excel worksheet**. Official reference: [Excel / Auto fill cells in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#autofillcells).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Ranges format | Choice | Named cells, Specific ranges | Named cells |
| Source cells name | Required | Text value | — |
| Destination cells name | Required | Text value | — |
| Start column | Required | Text value | — |
| Start row | Required | Numeric value | — |
| Source end column | Required | Text value | — |
| Source end row | Required | Numeric value | — |
| Destination end column | Required | Text value | — |
| Destination end row | Required | Numeric value | — |

Produces no variables.

**On error:** `Failed to auto fill cells`.

---

### Append cells in Excel worksheet

Appends a range of cells to the active worksheet of an Excel instance.

Designer name: **Append cells in Excel worksheet**. Official reference: [Excel / Append cells in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#appendcells).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Append mode | Choice | To active sheet, To named cells | To active sheet |
| Name | Required | Text value | — |
| First row has headers | Choice | Boolean value | False |
| Starting column | Optional | Text value | — |
| Starting column header | Optional | Text value | — |

Produces no variables.

**On error:** `Failed to append cells`.

---

### Lookup range in Excel worksheet

Finds and returns the result of Excel's LOOKUP function.

Designer name: **Lookup range in Excel worksheet**. Official reference: [Excel / Lookup range in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#lookuprange).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Lookup value | Required | Text value | — |
| Ranges format | Choice | Named cells, Specific ranges | Named cells |
| Cells name | Required | Text value | — |
| Start column | Required | Text value | — |
| Start row | Required | Numeric value | — |
| End column | Required | Text value | — |
| End row | Required | Numeric value | — |
| Array form | Choice | Boolean value | False |
| Cells name of results source | Optional | Text value | — |
| Start column of results source | Required | Text value | — |
| Start row of results source | Required | Numeric value | — |
| End column of results source | Required | Text value | — |
| End row of results source | Required | Numeric value | — |

**Outputs**

| Variable | Type |
|---|---|
| LookupResult | Text value |

**On error:** `Failed to lookup`.

---

### Set color of cells in Excel worksheet

Fills the background of the selected cells with the specified color, in the active worksheet of an Excel instance.

Designer name: **Set color of cells in Excel worksheet**. Official reference: [Excel / Set color of cells in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#setcolor).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Set color of | Choice | Single cell, Range of cells, Named cells | Single cell |
| Start column | Required | Text value | — |
| Start row | Required | Numeric value | — |
| End column | Required | Text value | — |
| End row | Required | Numeric value | — |
| Cells name | Required | Text value | — |
| Color format | Choice | Name, Hexadecimal value | Name |
| Color name | Required | Text value | — |
| Color hexadecimal value | Required | Text value | — |

Produces no variables.

**On error:** `Failed to set color`.

---

### Launch Excel

Starts a new Excel instance or opens an Excel document.

Designer name: **Launch Excel**. Official reference: [Excel / Launch Excel](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#launchexcel).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Launch Excel | Choice | With a blank document, and open the following document | With a blank document |
| Document path | Required | File | — |
| Make instance visible | Choice | Boolean value | True |
| Nest under a new Excel process | Choice | Boolean value | False |
| Password | Optional | Direct encrypted input or Text value | — |
| Open as ReadOnly | Choice | Boolean value | False |
| Load add-ins and macros | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| ExcelInstance | Excel instance |

**On error:** `Failed to launch Excel`, `Failed to open Excel document`.

---

### Attach to running Excel

Attaches to an Excel document that's already open.

Designer name: **Attach to running Excel**. Official reference: [Excel / Attach to running Excel](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#attach).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Document name | Required | File | — |

**Outputs**

| Variable | Type |
|---|---|
| ExcelInstance | Excel instance |

**On error:** `Specified Excel document not found`, `Failed to attach to Excel document`.

---

### Read from Excel worksheet

Reads the value of a cell or a range of cells from the active worksheet of an Excel instance.

Designer name: **Read from Excel worksheet**. Official reference: [Excel / Read from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#readfromexcel).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Retrieve | Choice | The value of a single cell, Values from a range of cells, Values from selection, All available values from worksheet | The value of a single cell |
| Start column | Required | Text value | — |
| Start row | Required | Numeric value | — |
| End column | Required | Text value | — |
| End row | Required | Numeric value | — |
| Get cell(s) contents as | Choice | Typed values,Plain text,Formatted text values | Typed values |
| First line of range contains column names | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| ExcelData | General value |
| ExcelData | Datatable |

**On error:** `Failed to read cell values`.

---

### Get active cell on Excel worksheet

Reads the active cell in the active worksheet of the Excel document.

Designer name: **Get active cell on Excel worksheet**. Official reference: [Excel / Get active cell on Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#getactivecell).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |

**Outputs**

| Variable | Type |
|---|---|
| ActiveCellColumnIndex | Numeric value |
| ActiveCellRowIndex | Numeric value |

**On error:** `Failed to get active cell`.

---

### Save Excel

Saves a previously launched Excel instance.

Designer name: **Save Excel**. Official reference: [Excel / Save Excel](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#saveexcel).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Save mode | Choice | Save document, Save document as | Save document |
| Document format | Choice | Default (From Extension), Excel Workbook (.xlsx), Excel Workbook Macro Enabled (.xlsm), Excel 97-2003 Workbook (.xls), Web Page (.htm, .html), Excel Template (.xltx), Excel Template Macro Enabled (.xltm), Excel 97-2003 Template (.xlt), Text (.txt), Unicode Text (.txt), Text Macintosh (.txt), Text DOS (.txt), XML Spreadsheet (.xml), Excel 95 (.xls), CSV (.csv), DIF (.dif), SYLK (.slk), Excel add-in (.xlam), Excel 97-2003 add-In (.xla), Strict Open XML Workbook (.xlsx), OpenDocument Spreadsheet (.ods), XML Data (.xml), Excel Binary Workbook (.xlsb) | Default (From Extension) |
| Document path | Required | File | — |

Produces no variables.

**On error:** `Failed to save Excel document`.

---

### Write to Excel worksheet

Writes a value into a cell or a range of cells of an Excel instance.

Designer name: **Write to Excel worksheet**. Official reference: [Excel / Write to Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#writetoexcel).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Value to write | Required | General value | — |
| Write mode | Choice | On specified cell, On currently active cell | On specified cell |
| Column | Required | Text value | — |
| Row | Required | Numeric value | — |

Produces no variables.

**On error:** `Failed to write value to Excel`.

---

### Close Excel

Closes an Excel instance.

Designer name: **Close Excel**. Official reference: [Excel / Close Excel](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#closeexcel).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Before closing Excel | Choice | Do not save document, Save document, Save document as | Don't save document |
| Document format | Choice | Default (From Extension), Excel Workbook (.xlsx), Excel Workbook Macro Enabled (.xlsm), Excel 97-2003 Workbook (.xls), Web Page (.htm, .html), Excel Template (.xltx), Excel Template Macro Enabled (.xltm), Excel 97-2003 Template (.xlt), Text (.txt), Unicode Text (.txt), Text Macintosh (.txt), Text DOS (.txt), XML Spreadsheet (.xml), Excel 95 (.xls), CSV (.csv), DIF (.dif), SYLK (.slk), Excel add-in (.xlam), Excel 97-2003 add-in (.xla), Strict Open XML Workbook (.xlsx), OpenDocument Spreadsheet (.ods), XML Data (.xml), Excel Binary Workbook (.xlsb) | Default (From Extension) |
| Document path | Required | File | — |

Produces no variables.

**On error:** `Failed to save Excel document`, `Failed to close Excel instance`.

---

### Set active Excel worksheet

Activates a specific worksheet of an Excel instance.

Designer name: **Set active Excel worksheet**. Official reference: [Excel / Set active Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#setactiveworksheet).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Activate worksheet with | Choice | Index, Name | Name |
| Worksheet index | Required | Numeric value | — |
| Worksheet name | Required | Text value | — |

Produces no variables.

**On error:** `Can't find worksheet`, `Failed to activate worksheet`.

---

### Add new worksheet

Adds a new worksheet to the document of an Excel instance.

Designer name: **Add new worksheet**. Official reference: [Excel / Add new worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#addworksheet).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| New worksheet name | Required | Text value | — |
| Add worksheet as | Choice | First worksheet, Last worksheet | First worksheet |

Produces no variables.

**On error:** `A worksheet with the same name already exists`, `Failed to add worksheet`.

---

### Get first free column/row from Excel worksheet

Returns the first free column and/or row of the active worksheet.

Designer name: **Get first free column/row from Excel worksheet**. Official reference: [Excel / Get first free column/row from Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#getfirstfreecolumnrow).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |

**Outputs**

| Variable | Type |
|---|---|
| FirstFreeColumn | Numeric value |
| FirstFreeRow | Numeric value |

**On error:** `Failed to retrieve first free column/row`.

---

### Get column name on Excel worksheet

Reads the name of the column.

Designer name: **Get column name on Excel worksheet**. Official reference: [Excel / Get column name on Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#getcolumnname).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Column number | Required | Numeric value | — |

**Outputs**

| Variable | Type |
|---|---|
| ColumnName | Text value |

No module-specific exceptions are listed for this action.

---

### Clear cells in Excel worksheet

Clears a range of cells or a named cell in the active worksheet of an Excel instance.

Designer name: **Clear cells in Excel worksheet**. Official reference: [Excel / Clear cells in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#clearcellsfromexcel).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Clear | Choice | Range of cells, Range of cells relative to active cell, Named cells, Single cell | Range of cells |
| X Axis Direction | Choice | Left, Right | Left |
| Start column | Required | Text value | — |
| X Offset | Required | Numeric value | — |
| Start row | Required | Numeric value | — |
| End column | Required | Text value | — |
| Y Axis Direction | Choice | Above, Below | Above |
| End row | Required | Numeric value | — |
| Y Offset | Required | Numeric value | — |
| Name | Required | Text value | — |
| Column | Required | Text value | — |
| Row | Required | Numeric value | — |

Produces no variables.

**On error:** `Failed to clear cells`.

---

### Sort cells in Excel worksheet

Runs the **Sort cells in Excel worksheet** action.

Designer name: **Sort cells in Excel worksheet**. Official reference: [Excel / Sort cells in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#sortcellsfromexcel).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Sort column in | Choice | Active sheet, Table, Range | Active sheet |
| Table name | Required | Text value | — |
| Range | Choice | Named cells, Specific range | Named cells |
| Cells name | Required | Text value | — |
| Start column | Required | Text value | — |
| Start row | Required | Numeric value | — |
| End column | Required | Text value | — |
| End row | Required | Numeric value | — |
| Sort by | Optional | Sorting rules as defined by the user | N/A |
| First row is header | Optional | Boolean value | — |

Produces no variables.

**On error:** `Failed to sort cells in worksheet`.

---

### Filter cells in Excel worksheet

The **Filter cells in Excel worksheet** allows makers to create and apply a filter in the active sheet, table, or range on the values of a specified column.

Designer name: **Filter cells in Excel worksheet**. Official reference: [Excel / Filter cells in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#filtercellsfromexcel).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Filter column in | Choice | Active sheet, Table, Range | Active sheet |
| Table name | Required | Text value | — |
| Range | Choice | Named cells, Specific range | Named cells |
| Cells name | Required | Text value | — |
| Start column | Required | Text value | — |
| Start row | Required | Numeric value | — |
| End column | Required | Text value | — |
| End row | Required | Numeric value | — |
| Column to filter | Required | Text value | — |
| Filters to apply | Optional | Filtering rules as defined by the user | N/A |

Produces no variables.

**On error:** `Failed to apply filter on cells in worksheet`.

---

### Clear filters in Excel worksheet

Runs the **Clear filters in Excel worksheet** action.

Designer name: **Clear filters in Excel worksheet**. Official reference: [Excel / Clear filters in Excel worksheet](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#clearfilterfromexcel).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Clear filters in | Choice | Active sheet, Table | Active sheet |
| Table name | Required | Text value | — |
| Clear filters from specific column | Optional | Boolean value | — |
| Clear filter in column | Required | Text value | — |

Produces no variables.

**On error:** `Failed to clear filter on cells in worksheet`.

---

### Get empty cell

Runs the **Get empty cell** action.

Designer name: **Get empty cell**. Official reference: [Excel / Get empty cell](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/excel#getemptycellfromexcel).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Excel instance | Required | Excel instance | — |
| Operation | Choice | First empty cell, First empty cell in column, First empty cell in row, All empty cells | First empty cell |
| Search direction | Choice | By row, By column | By row |
| Search in | Choice | Named cells, Specific range | Named cells |
| Cells name | Required | Text value | — |
| Column | Required | Text value | — |
| Row | Required | Numeric value | — |
| Start column | Required | Text value | — |
| Start row | Required | Numeric value | — |
| End column | Required | Text value | — |
| End row | Required | Numeric value | — |

**Outputs**

| Variable | Type |
|---|---|
| EmptyCellColumnIndex | Numeric value |
| EmptyCellRowIndex | Numeric value |
| EmptyCells | Datatable |

**On error:** `Get empty cells failed`.

---
