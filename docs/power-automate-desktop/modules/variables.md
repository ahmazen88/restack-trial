# Variables

Set values and manipulate lists, data tables, JSON, and numbers.

This page documents every **native action** in this group (36 items).

## Actions

### Add item to list

- **Inventory id:** `variables/add-item-to-list`
- **Kind:** native-action
- **Purpose:** Adds item to list.
- **Key inputs:** `Add item` (General value); `Into list` (List of General values)
- **Produces:** `NewList` (List of General values)
- **Exceptions:** none listed
- **Microsoft Learn:** [Add item to list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#additemtolist)

### Clear data table

- **Inventory id:** `variables/clear-data-table`
- **Kind:** native-action
- **Purpose:** Clears data table.
- **Key inputs:** `Data table` (Datatable)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Clear data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#cleardatatableaction)

### Clear list

- **Inventory id:** `variables/clear-list`
- **Kind:** native-action
- **Purpose:** Clears list.
- **Key inputs:** `List to clear` (List of General values)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Clear list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#clearlist)

### Convert custom object to JSON

- **Inventory id:** `variables/convert-custom-object-to-json`
- **Kind:** native-action
- **Purpose:** Converts custom object to JSON.
- **Key inputs:** `Custom object` (Custom object)
- **Produces:** `CustomObjectAsJson` (Text value)
- **Exceptions:** `Error parsing the custom object`
- **Microsoft Learn:** [Convert custom object to JSON](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#convertcustomobjecttojson)

### Convert data table to text

- **Inventory id:** `variables/convert-data-table-to-text`
- **Kind:** native-action
- **Purpose:** Converts data table to text.
- **Key inputs:** `Data table` (Datatable); `Include column names` (Boolean value); `Use custom columns separator` (Boolean value); `Separator` (System default, Comma, Semicolon, Tab); `Custom columns separator` (Text value)
- **Produces:** `CSVText` (Text value)
- **Exceptions:** `Conversion failed`
- **Microsoft Learn:** [Convert data table to text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#convertdatatabletocsvaction)

### Convert JSON to custom object

- **Inventory id:** `variables/convert-json-to-custom-object`
- **Kind:** native-action
- **Purpose:** Converts JSON to custom object.
- **Key inputs:** `JSON` (Text value)
- **Produces:** `JsonAsCustomObject` (General value)
- **Exceptions:** `Error parsing the JSON`
- **Microsoft Learn:** [Convert JSON to custom object](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#convertjsontocustomobject)

### Create new data table

- **Inventory id:** `variables/create-new-data-table`
- **Kind:** native-action
- **Purpose:** Creates new data table.
- **Key inputs:** `New table` (Datatable)
- **Produces:** `DataTable` (Datatable)
- **Exceptions:** none listed
- **Microsoft Learn:** [Create new data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#createnewdatatable)

### Create new list

- **Inventory id:** `variables/create-new-list`
- **Kind:** native-action
- **Purpose:** Creates new list.
- **Key inputs:** None
- **Produces:** `List` (List of General values)
- **Exceptions:** none listed
- **Microsoft Learn:** [Create new list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#createnewlist)

### Decrease variable

- **Inventory id:** `variables/decrease-variable`
- **Kind:** native-action
- **Purpose:** Subtracts a number from a numeric variable.
- **Key inputs:** `Variable name` (Numeric value); `Decrease by` (Numeric value)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Decrease variable](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#decreasevariable)

### Delete column from data table

- **Inventory id:** `variables/delete-column-from-data-table`
- **Kind:** native-action
- **Purpose:** Deletes column from data table.
- **Key inputs:** `Data table` (Datatable); `Specify column with` (Name, Index); `Column name` (Text value); `Column index` (Numeric value)
- **Produces:** None listed
- **Exceptions:** `Column name doesn't exist`; `Column index is out of range`
- **Microsoft Learn:** [Delete column from data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#deletecolumnfromdatatableaction)

### Delete duplicate rows from data table

- **Inventory id:** `variables/delete-duplicate-rows-from-data-table`
- **Kind:** native-action
- **Purpose:** Deletes duplicate rows from data table.
- **Key inputs:** `Data table` (Datatable)
- **Produces:** None listed
- **Exceptions:** `Type mismatch in the cells of a column`
- **Microsoft Learn:** [Delete duplicate rows from data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#deleteduplicaterowsfromdatatableaction)

### Delete empty rows from data table

- **Inventory id:** `variables/delete-empty-rows-from-data-table`
- **Kind:** native-action
- **Purpose:** Deletes empty rows from data table.
- **Key inputs:** `Data table` (Datatable)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Delete empty rows from data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#deleteemptyrowsfromdatatableaction)

### Delete row from data table

- **Inventory id:** `variables/delete-row-from-data-table`
- **Kind:** native-action
- **Purpose:** Deletes row from data table.
- **Key inputs:** `Data table` (Datatable); `Row index` (Numeric value)
- **Produces:** None listed
- **Exceptions:** `Item index is out of range`
- **Microsoft Learn:** [Delete row from data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#deleterowfromdatatable)

### Filter data table

- **Inventory id:** `variables/filter-data-table`
- **Kind:** native-action
- **Purpose:** Filters data table.
- **Key inputs:** `Data table` (Datatable); `Filters to apply` (Filtering rules as defined by the user); `Match case` (Boolean value)
- **Produces:** `FilteredDataTable` (Datatable)
- **Exceptions:** `Column name doesn't exist`; `Column index is out of range`; `Type mismatch in the cells of a column`
- **Microsoft Learn:** [Filter data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#filterdatatableaction)

### Find common list items

- **Inventory id:** `variables/find-common-list-items`
- **Kind:** native-action
- **Purpose:** Finds common list items.
- **Key inputs:** `First list` (List of General values); `Second list` (List of General values)
- **Produces:** `IntersectionList` (List of General values)
- **Exceptions:** none listed
- **Microsoft Learn:** [Find common list items](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#findcommonlistitems)

### Find or replace in data table

- **Inventory id:** `variables/find-or-replace-in-data-table`
- **Kind:** native-action
- **Purpose:** Finds or replace in data table.
- **Key inputs:** `Data table` (Datatable); `Search mode` (Find, Find and replace); `All matches` (Boolean value); `Text to find` (Text value); `Find using a regular expression` (Boolean value); `Match case` (Boolean value); `Match entire cell contents` (Boolean value); `Text to replace with` (Text value); `Search by` (Everywhere, On column); `Column index or name` (Text value)
- **Produces:** `DataTableMatches` (Datatable)
- **Exceptions:** `Provided regular expression is invalid`; `Column name doesn't exist`; `Column index is out of range`; `Incompatible type error`
- **Microsoft Learn:** [Find or replace in data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#findorreplaceindatatable)

### Generate random number

- **Inventory id:** `variables/generate-random-number`
- **Kind:** native-action
- **Purpose:** Generate a random number or a list of random numbers that fall between a minimum and maximum value.
- **Key inputs:** `Minimum value` (Numeric value; optional); `Maximum value` (Numeric value; optional); `Generate multiple numbers` (Boolean value); `How many numbers` (Numeric value; optional); `Allow duplicates` (Boolean value)
- **Produces:** `RandomNumber` (Numeric value); `RandomNumbers` (List of Numeric values)
- **Exceptions:** `Failed to generate random number`
- **Microsoft Learn:** [Generate random number](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#generaterandomnumber)

### Increase variable

- **Inventory id:** `variables/increase-variable`
- **Kind:** native-action
- **Purpose:** Adds a number to a numeric variable.
- **Key inputs:** `Variable name` (Numeric value); `Increase by` (Numeric value)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Increase variable](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#increasevariable)

### Insert column into data table

- **Inventory id:** `variables/insert-column-into-data-table`
- **Kind:** native-action
- **Purpose:** Inserts column into data table.
- **Key inputs:** `Data table` (Datatable); `Into location` (End of data table, Before column index); `Column name` (Text value); `Column index` (Numeric value)
- **Produces:** None listed
- **Exceptions:** `Column index is out of range`; `Duplicate column name`
- **Microsoft Learn:** [Insert column into data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#addcolumntodatatableaction)

### Insert row into data table

- **Inventory id:** `variables/insert-row-into-data-table`
- **Kind:** native-action
- **Purpose:** Inserts row into data table.
- **Key inputs:** `Data table` (Datatable); `Into location` (End of data table, Before row index); `Row index` (Numeric value); `New value(s)` (List, Datarow)
- **Produces:** None listed
- **Exceptions:** `Item index is out of range`; `Invalid input arguments`; `Incompatible type error`
- **Microsoft Learn:** [Insert row into data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#addrowtodatatable)

### Join data tables

- **Inventory id:** `variables/join-data-tables`
- **Kind:** native-action
- **Purpose:** Joins data tables.
- **Key inputs:** `First data table` (Datatable); `Second data table` (Datatable); `Join operation` (Inner, Left, Full); `Join rules` (Join rules as defined by the user)
- **Produces:** `JoinedDataTable` (Datatable)
- **Exceptions:** `Column name doesn't exist`; `Column index is out of range`
- **Microsoft Learn:** [Join data tables](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#joindatatableaction)

### Merge data tables

- **Inventory id:** `variables/merge-data-tables`
- **Kind:** native-action
- **Purpose:** Merges data tables.
- **Key inputs:** `First data table` (Datatable); `Second data table` (Datatable); `Merge mode` (Add extra columns, Ignore extra columns, Error on extra columns)
- **Produces:** None listed
- **Exceptions:** `Missing Schema`
- **Microsoft Learn:** [Merge data tables](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#mergedatatablesaction)

### Merge lists

- **Inventory id:** `variables/merge-lists`
- **Kind:** native-action
- **Purpose:** Merges lists.
- **Key inputs:** `First list` (List of General values); `Second list` (List of General values)
- **Produces:** `OutputList` (List of General values)
- **Exceptions:** `The lists supplied are of incompatible types`
- **Microsoft Learn:** [Merge lists](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#mergelists)

### Read from CSV text variable

- **Inventory id:** `variables/read-from-csv-text-variable`
- **Kind:** native-action
- **Purpose:** Reads from CSV text variable.
- **Key inputs:** `CSV text` (Text value); `Trim fields` (Boolean value); `First line contains column names` (Boolean value); `Get CSV fields as text` (Boolean value); `Columns separator` (Predefined, Custom, Fixed Column Widths); `Separator` (System default, Comma, Semicolon, Tab); `Custom separator` (Text value); `Fixed column widths` (Text value)
- **Produces:** `CSVTable` (Datatable)
- **Exceptions:** `CSV parsing failed`
- **Microsoft Learn:** [Read from CSV text variable](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#generatedatatablefromcsv)

### Remove duplicate items from list

- **Inventory id:** `variables/remove-duplicate-items-from-list`
- **Kind:** native-action
- **Purpose:** Removes duplicate items from list.
- **Key inputs:** `List to remove duplicate items from` (List of General values); `Ignore text case while searching for duplicate items` (Boolean value)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Remove duplicate items from list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#removeduplicateitemsfromlist)

### Remove item from list

- **Inventory id:** `variables/remove-item-from-list`
- **Kind:** native-action
- **Purpose:** Removes item from list.
- **Key inputs:** `Remove item by` (Index, Value); `At index` (Numeric value); `With value` (General value); `Remove all item occurrences` (Boolean value); `From list` (List of General values)
- **Produces:** None listed
- **Exceptions:** `Item index is out of range`; `Item not found`
- **Microsoft Learn:** [Remove item from list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#removeitemfromlist)

### Retrieve data table column into list

- **Inventory id:** `variables/retrieve-data-table-column-into-list`
- **Kind:** native-action
- **Purpose:** Retrieves data table column into list.
- **Key inputs:** `Data table` (Datatable); `Column name or index` (Text value)
- **Produces:** `ColumnAsList` (List of General values)
- **Exceptions:** `Column name doesn't exist`; `Column index is out of range`
- **Microsoft Learn:** [Retrieve data table column into list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#retrievedatatablecolumnintolist)

### Reverse list

- **Inventory id:** `variables/reverse-list`
- **Kind:** native-action
- **Purpose:** Reverse the order of the items of a list.
- **Key inputs:** `List to reverse` (List of General values)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Reverse list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#reverselist)

### Run Power Fx expression

- **Inventory id:** `variables/run-power-fx-expression`
- **Kind:** native-action
- **Purpose:** Runs power Fx expression.
- **Key inputs:** `Expression` (*)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Run Power Fx expression](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables)

### Set variable

- **Inventory id:** `variables/set-variable`
- **Kind:** native-action
- **Purpose:** Writes variable.
- **Key inputs:** `To` (*)
- **Produces:** `NewVar` (*)
- **Exceptions:** none listed
- **Microsoft Learn:** [Set variable](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#assign)

### Shuffle list

- **Inventory id:** `variables/shuffle-list`
- **Kind:** native-action
- **Purpose:** Create a random permutation of a list.
- **Key inputs:** `List to shuffle` (List of General values)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Shuffle list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#shufflelist)

### Sort data table

- **Inventory id:** `variables/sort-data-table`
- **Kind:** native-action
- **Purpose:** Sorts data table.
- **Key inputs:** `Data table` (Datatable); `Specify column with` (Name, Index); `Column name` (Text value); `Column index` (Numeric value); `Order` (Ascending, Descending)
- **Produces:** None listed
- **Exceptions:** `Column name doesn't exist`; `Column index is out of range`; `Type mismatch in the cells of a column`
- **Microsoft Learn:** [Sort data table](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#sortdatatableaction)

### Sort list

- **Inventory id:** `variables/sort-list`
- **Kind:** native-action
- **Purpose:** Sorts list.
- **Key inputs:** `List to sort` (List of General values); `Sort by list item's properties` (Boolean value); `First property to sort by` (Text value; optional); `Sort` (Ascending, Descending); `Second property to sort by` (Text value; optional); `Sort` (Ascending, Descending); `Third property to sort by` (Text value; optional); `Sort` (Ascending, Descending)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Sort list](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#sortlistbase)

### Subtract lists

- **Inventory id:** `variables/subtract-lists`
- **Kind:** native-action
- **Purpose:** Compare two lists and create a new list with the items that are in the first list but not in the second.
- **Key inputs:** `First list` (List of General values); `Second list` (List of General values)
- **Produces:** `ListDifference` (List of General values)
- **Exceptions:** none listed
- **Microsoft Learn:** [Subtract lists](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#subtractlists)

### Truncate number

- **Inventory id:** `variables/truncate-number`
- **Kind:** native-action
- **Purpose:** Get the integral or fractional digits of a numeric value, or round up the value to a specified number of decimal places.
- **Key inputs:** `Number to truncate` (Numeric value); `Operation` (Get integer part, Get decimal part, Round number); `Decimal places` (Numeric value; optional)
- **Produces:** `TruncatedValue` (Numeric value)
- **Exceptions:** none listed
- **Microsoft Learn:** [Truncate number](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#truncatenumber)

### Update data table item

- **Inventory id:** `variables/update-data-table-item`
- **Kind:** native-action
- **Purpose:** Updates data table item.
- **Key inputs:** `Data table` (Datatable); `Column` (Text value); `Row` (Numeric value); `New value` (Text value)
- **Produces:** None listed
- **Exceptions:** `Item index is out of range`; `Column name doesn't exist`; `Column index is out of range`; `Incompatible type error`
- **Microsoft Learn:** [Update data table item](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables#modifydatatableitem)
