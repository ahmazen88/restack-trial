# Variables

Set variables and work with lists, data tables, JSON, and Power Fx.

- Actions in this module: **36**
- Official docs: [Variables actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables)

## Actions

### Create new data table

Creates a new data table variable.

Designer name: **Create new data table**. Official reference: [Variables / Create new data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#createnewdatatable).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| New table | Required | Datatable | — |

**Outputs**

| Variable | Type |
|---|---|
| DataTable | Datatable |

No module-specific exceptions are listed for this action.

---

### Insert row into data table

Inserts a row at the end or before a specific index value.

Designer name: **Insert row into data table**. Official reference: [Variables / Insert row into data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#addrowtodatatable).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Data table | Required | Datatable | — |
| Into location | Choice | End of data table, Before row index | End of data table |
| Row index | Required | Numeric value | — |
| New value(s) | Required | List, Datarow | — |

Produces no variables.

**On error:** `Item index is out of range`, `Invalid input arguments`, `Incompatible type error`.

---

### Delete row from data table

Delete a data table row at the corresponding row index.

Designer name: **Delete row from data table**. Official reference: [Variables / Delete row from data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#deleterowfromdatatable).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Data table | Required | Datatable | — |
| Row index | Required | Numeric value | — |

Produces no variables.

**On error:** `Item index is out of range`.

---

### Update data table item

Update a data table row item on a defined column.

Designer name: **Update data table item**. Official reference: [Variables / Update data table item](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#modifydatatableitem).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Data table | Required | Datatable | — |
| Column | Required | Text value | — |
| Row | Required | Numeric value | — |
| New value | Required | Text value | — |

Produces no variables.

**On error:** `Item index is out of range`, `Column name doesn't exist`, `Column index is out of range`, `Incompatible type error`.

---

### Find or replace in data table

Finds and/or replaces data table values.

Designer name: **Find or replace in data table**. Official reference: [Variables / Find or replace in data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#findorreplaceindatatable).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Data table | Required | Datatable | — |
| Search mode | Choice | Find, Find and replace | Find |
| All matches | Choice | Boolean value | True |
| Text to find | Required | Text value | — |
| Find using a regular expression | Choice | Boolean value | False |
| Match case | Choice | Boolean value | False |
| Match entire cell contents | Choice | Boolean value | False |
| Text to replace with | Required | Text value | — |
| Search by | Choice | Everywhere, On column | Everywhere |
| Column index or name | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| DataTableMatches | Datatable |

**On error:** `Provided regular expression is invalid`, `Column name doesn't exist`, `Column index is out of range`, `Incompatible type error`.

---

### Insert column into data table

Inserts a column at the end or before a specific index value.

Designer name: **Insert column into data table**. Official reference: [Variables / Insert column into data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#addcolumntodatatableaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Data table | Required | Datatable | — |
| Into location | Choice | End of data table, Before column index | End of data table |
| Column name | Required | Text value | — |
| Column index | Required | Numeric value | — |

Produces no variables.

**On error:** `Column index is out of range`, `Duplicate column name`.

---

### Delete column from data table

Delete a data table column at the specified column index or column name.

Designer name: **Delete column from data table**. Official reference: [Variables / Delete column from data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#deletecolumnfromdatatableaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Data table | Required | Datatable | — |
| Specify column with | Choice | Name, Index | Name |
| Column name | Required | Text value | — |
| Column index | Required | Numeric value | — |

Produces no variables.

**On error:** `Column name doesn't exist`, `Column index is out of range`.

---

### Delete empty rows from data table

Deletes the rows of the data table that have all of their cells empty.

Designer name: **Delete empty rows from data table**. Official reference: [Variables / Delete empty rows from data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#deleteemptyrowsfromdatatableaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Data table | Required | Datatable | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Delete duplicate rows from data table

Deletes all the rows that are duplicate from the data table, if the values have the same data type in each column.

Designer name: **Delete duplicate rows from data table**. Official reference: [Variables / Delete duplicate rows from data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#deleteduplicaterowsfromdatatableaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Data table | Required | Datatable | — |

Produces no variables.

**On error:** `Type mismatch in the cells of a column`.

---

### Clear data table

Deletes all the rows of the data table, keeping table headers unaffected.

Designer name: **Clear data table**. Official reference: [Variables / Clear data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#cleardatatableaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Data table | Required | Datatable | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Sort data table

Sorts the data table rows in ascending or descending order by the specified column, if all its values have the same data type.

Designer name: **Sort data table**. Official reference: [Variables / Sort data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#sortdatatableaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Data table | Required | Datatable | — |
| Specify column with | Choice | Name, Index | Name |
| Column name | Required | Text value | — |
| Column index | Required | Numeric value | — |
| Order | Choice | Ascending, Descending | Ascending |

Produces no variables.

**On error:** `Column name doesn't exist`, `Column index is out of range`, `Type mismatch in the cells of a column`.

---

### Filter data table

Filters the data table rows based on the applied rules.

Designer name: **Filter data table**. Official reference: [Variables / Filter data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#filterdatatableaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Data table | Required | Datatable | — |
| Filters to apply | Required | Filtering rules as defined by the user | N/A |
| Match case | Choice | Boolean value | True |

**Outputs**

| Variable | Type |
|---|---|
| FilteredDataTable | Datatable |

**On error:** `Column name doesn't exist`, `Column index is out of range`, `Type mismatch in the cells of a column`.

---

### Merge data tables

Merges two data tables together, specifying the merging behavior in case their number of columns is different.

Designer name: **Merge data tables**. Official reference: [Variables / Merge data tables](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#mergedatatablesaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| First data table | Required | Datatable | — |
| Second data table | Required | Datatable | — |
| Merge mode | Choice | Add extra columns, Ignore extra columns, Error on extra columns | Add extra columns |

Produces no variables.

**On error:** `Missing Schema`.

---

### Join data tables

Joins two data tables based on the specified join rule.

Designer name: **Join data tables**. Official reference: [Variables / Join data tables](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#joindatatableaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| First data table | Required | Datatable | — |
| Second data table | Required | Datatable | — |
| Join operation | Choice | Inner, Left, Full | Inner |
| Join rules | Required | Join rules as defined by the user | N/A |

**Outputs**

| Variable | Type |
|---|---|
| JoinedDataTable | Datatable |

**On error:** `Column name doesn't exist`, `Column index is out of range`.

---

### Read from CSV text variable

Generates a data table from a CSV text.

Designer name: **Read from CSV text variable**. Official reference: [Variables / Read from CSV text variable](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#generatedatatablefromcsv).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| CSV text | Required | Text value | — |
| Trim fields | Choice | Boolean value | True |
| First line contains column names | Choice | Boolean value | False |
| Get CSV fields as text | Choice | Boolean value | False |
| Columns separator | Choice | Predefined, Custom, Fixed Column Widths | Predefined |
| Separator | Choice | System default, Comma, Semicolon, Tab | System default |
| Custom separator | Required | Text value | — |
| Fixed column widths | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| CSVTable | Datatable |

**On error:** `CSV parsing failed`.

---

### Convert data table to text

Converts a data table to a CSV text.

Designer name: **Convert data table to text**. Official reference: [Variables / Convert data table to text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#convertdatatabletocsvaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Data table | Required | Datatable | — |
| Include column names | Choice | Boolean value | False |
| Use custom columns separator | Choice | Boolean value | False |
| Separator | Choice | System default, Comma, Semicolon, Tab | System default |
| Custom columns separator | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| CSVText | Text value |

**On error:** `Conversion failed`.

---

### Truncate number

Reads the integral or fractional digits of a numeric value, or round up the value to a specified number of decimal places.

Designer name: **Truncate number**. Official reference: [Variables / Truncate number](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#truncatenumber).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Number to truncate | Required | Numeric value | — |
| Operation | Choice | Get integer part, Get decimal part, Round number | Get integer part |
| Decimal places | Optional | Numeric value | 3 |

**Outputs**

| Variable | Type |
|---|---|
| TruncatedValue | Numeric value |

No module-specific exceptions are listed for this action.

---

### Generate random number

Generate a random number or a list of random numbers that fall between a minimum and maximum value.

Designer name: **Generate random number**. Official reference: [Variables / Generate random number](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#generaterandomnumber).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Minimum value | Optional | Numeric value | 0 |
| Maximum value | Optional | Numeric value | 100 |
| Generate multiple numbers | Choice | Boolean value | False |
| How many numbers | Optional | Numeric value | 10 |
| Allow duplicates | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| RandomNumber | Numeric value |
| RandomNumbers | List of Numeric values |

**On error:** `Failed to generate random number`.

---

### Clear list

Remove all items from a list.

Designer name: **Clear list**. Official reference: [Variables / Clear list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#clearlist).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| List to clear | Required | List of General values | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Remove item from list

Remove one or multiple items from a list.

Designer name: **Remove item from list**. Official reference: [Variables / Remove item from list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#removeitemfromlist).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Remove item by | Choice | Index, Value | Index |
| At index | Required | Numeric value | — |
| With value | Required | General value | — |
| Remove all item occurrences | Choice | Boolean value | False |
| From list | Required | List of General values | — |

Produces no variables.

**On error:** `Item index is out of range`, `Item not found`.

---

### Sort list

Sort the items of a list.

Designer name: **Sort list**. Official reference: [Variables / Sort list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#sortlistbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| List to sort | Required | List of General values | — |
| Sort by list item's properties | Choice | Boolean value | False |
| First property to sort by | Optional | Text value | — |
| Sort | Choice | Ascending, Descending | Ascending |
| Second property to sort by | Optional | Text value | — |
| Sort | Choice | Ascending, Descending | Ascending |
| Third property to sort by | Optional | Text value | — |
| Sort | Choice | Ascending, Descending | Ascending |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Shuffle list

Create a random permutation of a list.

Designer name: **Shuffle list**. Official reference: [Variables / Shuffle list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#shufflelist).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| List to shuffle | Required | List of General values | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Merge lists

Merge two lists into one.

Designer name: **Merge lists**. Official reference: [Variables / Merge lists](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#mergelists).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| First list | Required | List of General values | — |
| Second list | Required | List of General values | — |

**Outputs**

| Variable | Type |
|---|---|
| OutputList | List of General values |

**On error:** `The lists supplied are of incompatible types`.

---

### Reverse list

Reverse the order of the items of a list.

Designer name: **Reverse list**. Official reference: [Variables / Reverse list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#reverselist).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| List to reverse | Required | List of General values | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Remove duplicate items from list

Remove the multiple occurrences of items in a list, so that in the resulting list each item is unique.

Designer name: **Remove duplicate items from list**. Official reference: [Variables / Remove duplicate items from list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#removeduplicateitemsfromlist).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| List to remove duplicate items from | Required | List of General values | — |
| Ignore text case while searching for duplicate items | Choice | Boolean value | False |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Find common list items

Compare two lists and create a new list with the items that are common to both.

Designer name: **Find common list items**. Official reference: [Variables / Find common list items](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#findcommonlistitems).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| First list | Required | List of General values | — |
| Second list | Required | List of General values | — |

**Outputs**

| Variable | Type |
|---|---|
| IntersectionList | List of General values |

No module-specific exceptions are listed for this action.

---

### Subtract lists

Compare two lists and create a new list with the items that are in the first list but not in the second.

Designer name: **Subtract lists**. Official reference: [Variables / Subtract lists](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#subtractlists).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| First list | Required | List of General values | — |
| Second list | Required | List of General values | — |

**Outputs**

| Variable | Type |
|---|---|
| ListDifference | List of General values |

No module-specific exceptions are listed for this action.

---

### Retrieve data table column into list

Convert the contents of a data table column into a list.

Designer name: **Retrieve data table column into list**. Official reference: [Variables / Retrieve data table column into list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#retrievedatatablecolumnintolist).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Data table | Required | Datatable | — |
| Column name or index | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| ColumnAsList | List of General values |

**On error:** `Column name doesn't exist`, `Column index is out of range`.

---

### Convert JSON to custom object

Convert a JSON string to a custom object.

Designer name: **Convert JSON to custom object**. Official reference: [Variables / Convert JSON to custom object](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#convertjsontocustomobject).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| JSON | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| JsonAsCustomObject | General value |

**On error:** `Error parsing the JSON`.

---

### Convert custom object to JSON

Convert a custom object to a JSON string.

Designer name: **Convert custom object to JSON**. Official reference: [Variables / Convert custom object to JSON](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#convertcustomobjecttojson).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Custom object | Required | Custom object | — |

**Outputs**

| Variable | Type |
|---|---|
| CustomObjectAsJson | Text value |

**On error:** `Error parsing the custom object`.

---

### Add item to list

Append a new item to a list.

Designer name: **Add item to list**. Official reference: [Variables / Add item to list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#additemtolist).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Add item | Required | General value | — |
| Into list | Required | List of General values | — |

**Outputs**

| Variable | Type |
|---|---|
| NewList | List of General values |

No module-specific exceptions are listed for this action.

---

### Create new list

Create a new empty list.

Designer name: **Create new list**. Official reference: [Variables / Create new list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#createnewlist).

This action has no input parameters.

**Outputs**

| Variable | Type |
|---|---|
| List | List of General values |

No module-specific exceptions are listed for this action.

---

### Increase variable

Increase the value of a variable by a specific amount.

Designer name: **Increase variable**. Official reference: [Variables / Increase variable](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#increasevariable).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Variable name | Required | Numeric value | — |
| Increase by | Required | Numeric value | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Decrease variable

Decrease the value of a variable by a specific amount.

Designer name: **Decrease variable**. Official reference: [Variables / Decrease variable](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#decreasevariable).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Variable name | Required | Numeric value | — |
| Decrease by | Required | Numeric value | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Run Power Fx expression

Runs the provided Power Fx expression.

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Expression | Required | * | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Set variable

Writes the value of a new or existing variable, create a new variable or overwrite a previously created variable.

Designer name: **Set variable**. Official reference: [Variables / Set variable](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#assign).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| To | Required | * | — |

**Outputs**

| Variable | Type |
|---|---|
| NewVar | * |

No module-specific exceptions are listed for this action.

---
