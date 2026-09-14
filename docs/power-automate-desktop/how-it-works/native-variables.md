# Variables — how each function works

Native Actions pane module **Variables**.

36 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Add item to list

- **Id:** `variables/add-item-to-list`
- **Kind:** native-action
- **Purpose:** Adds item to list.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Add item to list** on the canvas. Adds item to list.

**Demonstration.**

```text
**Add item to list**
- Add item: `(set in designer)`
- Into list: `%Files%`
Produces:
- `%NewList%` (List of General values)
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Clear data table

- **Id:** `variables/clear-data-table`
- **Kind:** native-action
- **Purpose:** Clears data table.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Clear data table** on the canvas. Clears data table.

**Demonstration.**

```text
**Clear data table**
- Data table: `%InvoiceTable%`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Clear list

- **Id:** `variables/clear-list`
- **Kind:** native-action
- **Purpose:** Clears list.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Clear list** on the canvas. Clears list.

**Demonstration.**

```text
**Clear list**
- List to clear: `%Files%`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Convert custom object to JSON

- **Id:** `variables/convert-custom-object-to-json`
- **Kind:** native-action
- **Purpose:** Converts custom object to JSON.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Convert custom object to JSON** on the canvas. Converts custom object to JSON.

**Demonstration.**

```text
**Convert custom object to JSON**
- Custom object: `(set in designer)`
Produces:
- `%CustomObjectAsJson%` (Text value)
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Convert data table to text

- **Id:** `variables/convert-data-table-to-text`
- **Kind:** native-action
- **Purpose:** Converts data table to text.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Convert data table to text** on the canvas. Converts data table to text.

**Demonstration.**

```text
**Convert data table to text**
- Data table: `%InvoiceTable%`
- Include column names: `False`
- Use custom columns separator: `False`
- Separator: `System default`
- Custom columns separator: `INV-1042`
Produces:
- `%CSVText%` (Text value)
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Convert JSON to custom object

- **Id:** `variables/convert-json-to-custom-object`
- **Kind:** native-action
- **Purpose:** Converts JSON to custom object.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Convert JSON to custom object** on the canvas. Converts JSON to custom object.

**Demonstration.**

```text
**Convert JSON to custom object**
- JSON: `{ "InvoiceId": "INV-1042", "Amount": 190.5 }`
Produces:
- `%JsonAsCustomObject%` (General value)
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Create new data table

- **Id:** `variables/create-new-data-table`
- **Kind:** native-action
- **Purpose:** Creates new data table.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Create new data table** on the canvas. Creates new data table.

**Demonstration.**

```text
**Create new data table**
- New table: `%InvoiceTable%`
Produces:
- `%DataTable%` (Datatable)
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Create new list

- **Id:** `variables/create-new-list`
- **Kind:** native-action
- **Purpose:** Creates new list.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Create new list** on the canvas. Creates new list.

**Demonstration.**

```text
**Create new list**
- (no inputs)
Produces:
- `%List%` (List of General values)
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Decrease variable

- **Id:** `variables/decrease-variable`
- **Kind:** native-action
- **Purpose:** Subtracts a number from a numeric variable.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Decrease variable** on the canvas. Subtracts a number from a numeric variable.

**Demonstration.**

```text
**Decrease variable**
- Variable name: `1`
- Decrease by: `1`
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Delete column from data table

- **Id:** `variables/delete-column-from-data-table`
- **Kind:** native-action
- **Purpose:** Deletes column from data table.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Delete column from data table** on the canvas. Deletes column from data table.

**Demonstration.**

```text
**Delete column from data table**
- Data table: `%InvoiceTable%`
- Specify column with: `Name`
- Column name: `Amount`
- Column index: `1`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Delete duplicate rows from data table

- **Id:** `variables/delete-duplicate-rows-from-data-table`
- **Kind:** native-action
- **Purpose:** Deletes duplicate rows from data table.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Delete duplicate rows from data table** on the canvas. Deletes duplicate rows from data table.

**Demonstration.**

```text
**Delete duplicate rows from data table**
- Data table: `%InvoiceTable%`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Delete empty rows from data table

- **Id:** `variables/delete-empty-rows-from-data-table`
- **Kind:** native-action
- **Purpose:** Deletes empty rows from data table.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Delete empty rows from data table** on the canvas. Deletes empty rows from data table.

**Demonstration.**

```text
**Delete empty rows from data table**
- Data table: `%InvoiceTable%`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Delete row from data table

- **Id:** `variables/delete-row-from-data-table`
- **Kind:** native-action
- **Purpose:** Deletes row from data table.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Delete row from data table** on the canvas. Deletes row from data table.

**Demonstration.**

```text
**Delete row from data table**
- Data table: `%InvoiceTable%`
- Row index: `1`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Filter data table

- **Id:** `variables/filter-data-table`
- **Kind:** native-action
- **Purpose:** Filters data table.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Filter data table** on the canvas. Filters data table.

**Demonstration.**

```text
**Filter data table**
- Data table: `%InvoiceTable%`
- Filters to apply: `N/A`
- Match case: `True`
Produces:
- `%FilteredDataTable%` (Datatable)
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Find common list items

- **Id:** `variables/find-common-list-items`
- **Kind:** native-action
- **Purpose:** Finds common list items.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Find common list items** on the canvas. Finds common list items.

**Demonstration.**

```text
**Find common list items**
- First list: `%Files%`
- Second list: `%Files%`
Produces:
- `%IntersectionList%` (List of General values)
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Find or replace in data table

- **Id:** `variables/find-or-replace-in-data-table`
- **Kind:** native-action
- **Purpose:** Finds or replace in data table.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Find or replace in data table** on the canvas. Finds or replace in data table.

**Demonstration.**

```text
**Find or replace in data table**
- Data table: `%InvoiceTable%`
- Search mode: `Find`
- All matches: `True`
- Text to find: `INV-1042`
- Find using a regular expression: `False`
- Match case: `False`
- Match entire cell contents: `False`
- Text to replace with: `INV-1042`
- … 2 more parameter(s) in the action modal
Produces:
- `%DataTableMatches%` (Datatable)
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Generate random number

- **Id:** `variables/generate-random-number`
- **Kind:** native-action
- **Purpose:** Generate a random number or a list of random numbers that fall between a minimum and maximum value.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Generate random number** on the canvas. Generate a random number or a list of random numbers that fall between a minimum and maximum value.

**Demonstration.**

```text
**Generate random number**
- Minimum value: `0`
- Maximum value: `100`
- Generate multiple numbers: `False`
- How many numbers: `10`
- Allow duplicates: `False`
Produces:
- `%RandomNumber%` (Numeric value)
- `%RandomNumbers%` (List of Numeric values)
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Increase variable

- **Id:** `variables/increase-variable`
- **Kind:** native-action
- **Purpose:** Adds a number to a numeric variable.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Increase variable** on the canvas. Adds a number to a numeric variable.

**Demonstration.**

```text
**Increase variable**
- Variable name: `1`
- Increase by: `1`
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Insert column into data table

- **Id:** `variables/insert-column-into-data-table`
- **Kind:** native-action
- **Purpose:** Inserts column into data table.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Insert column into data table** on the canvas. Inserts column into data table.

**Demonstration.**

```text
**Insert column into data table**
- Data table: `%InvoiceTable%`
- Into location: `End of data table`
- Column name: `Amount`
- Column index: `1`
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Insert row into data table

- **Id:** `variables/insert-row-into-data-table`
- **Kind:** native-action
- **Purpose:** Inserts row into data table.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Insert row into data table** on the canvas. Inserts row into data table.

**Demonstration.**

```text
**Insert row into data table**
- Data table: `%InvoiceTable%`
- Into location: `End of data table`
- Row index: `1`
- New value(s): `%CurrentRow%`
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Join data tables

- **Id:** `variables/join-data-tables`
- **Kind:** native-action
- **Purpose:** Joins data tables.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Join data tables** on the canvas. Joins data tables.

**Demonstration.**

```text
**Join data tables**
- First data table: `%InvoiceTable%`
- Second data table: `%InvoiceTable%`
- Join operation: `Inner`
- Join rules: `N/A`
Produces:
- `%JoinedDataTable%` (Datatable)
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Merge data tables

- **Id:** `variables/merge-data-tables`
- **Kind:** native-action
- **Purpose:** Merges data tables.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Merge data tables** on the canvas. Merges data tables.

**Demonstration.**

```text
**Merge data tables**
- First data table: `%InvoiceTable%`
- Second data table: `%InvoiceTable%`
- Merge mode: `Add extra columns`
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Merge lists

- **Id:** `variables/merge-lists`
- **Kind:** native-action
- **Purpose:** Merges lists.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Merge lists** on the canvas. Merges lists.

**Demonstration.**

```text
**Merge lists**
- First list: `%Files%`
- Second list: `%Files%`
Produces:
- `%OutputList%` (List of General values)
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Read from CSV text variable

- **Id:** `variables/read-from-csv-text-variable`
- **Kind:** native-action
- **Purpose:** Reads from CSV text variable.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Read from CSV text variable** on the canvas. Reads from CSV text variable.

**Demonstration.**

```text
**Read from CSV text variable**
- CSV text: `INV-1042`
- Trim fields: `True`
- First line contains column names: `False`
- Get CSV fields as text: `False`
- Columns separator: `Predefined`
- Separator: `System default`
- Custom separator: `INV-1042`
- Fixed column widths: `INV-1042`
Produces:
- `%CSVTable%` (Datatable)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Remove duplicate items from list

- **Id:** `variables/remove-duplicate-items-from-list`
- **Kind:** native-action
- **Purpose:** Removes duplicate items from list.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Remove duplicate items from list** on the canvas. Removes duplicate items from list.

**Demonstration.**

```text
**Remove duplicate items from list**
- List to remove duplicate items from: `%Files%`
- Ignore text case while searching for duplicate items: `False`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Remove item from list

- **Id:** `variables/remove-item-from-list`
- **Kind:** native-action
- **Purpose:** Removes item from list.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Remove item from list** on the canvas. Removes item from list.

**Demonstration.**

```text
**Remove item from list**
- Remove item by: `Index`
- At index: `1`
- With value: `(set in designer)`
- Remove all item occurrences: `False`
- From list: `%Files%`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Retrieve data table column into list

- **Id:** `variables/retrieve-data-table-column-into-list`
- **Kind:** native-action
- **Purpose:** Retrieves data table column into list.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Retrieve data table column into list** on the canvas. Retrieves data table column into list.

**Demonstration.**

```text
**Retrieve data table column into list**
- Data table: `%InvoiceTable%`
- Column name or index: `INV-1042`
Produces:
- `%ColumnAsList%` (List of General values)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Reverse list

- **Id:** `variables/reverse-list`
- **Kind:** native-action
- **Purpose:** Reverse the order of the items of a list.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Reverse list** on the canvas. Reverse the order of the items of a list.

**Demonstration.**

```text
**Reverse list**
- List to reverse: `%Files%`
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Run Power Fx expression

- **Id:** `variables/run-power-fx-expression`
- **Kind:** native-action
- **Purpose:** Runs power Fx expression.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Run Power Fx expression** on the canvas. Runs power Fx expression.

**Demonstration.**

```text
**Run Power Fx expression**
- Expression: `%Count% > 0`
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Set variable

- **Id:** `variables/set-variable`
- **Kind:** native-action
- **Purpose:** Writes variable.

**Use case.** Keep a path, counter, flag, or JSON blob that later actions and % expressions will read.

**Demonstration.**

```text
**Set variable**
- To: `ap@contoso.example`
Produces:
- `%NewVar%` (*)
```

**Analogy.** Writing a name on a jar, then putting something in it.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Shuffle list

- **Id:** `variables/shuffle-list`
- **Kind:** native-action
- **Purpose:** Create a random permutation of a list.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Shuffle list** on the canvas. Create a random permutation of a list.

**Demonstration.**

```text
**Shuffle list**
- List to shuffle: `%Files%`
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Sort data table

- **Id:** `variables/sort-data-table`
- **Kind:** native-action
- **Purpose:** Sorts data table.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Sort data table** on the canvas. Sorts data table.

**Demonstration.**

```text
**Sort data table**
- Data table: `%InvoiceTable%`
- Specify column with: `Name`
- Column name: `Amount`
- Column index: `1`
- Order: `Ascending`
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Sort list

- **Id:** `variables/sort-list`
- **Kind:** native-action
- **Purpose:** Sorts list.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Sort list** on the canvas. Sorts list.

**Demonstration.**

```text
**Sort list**
- List to sort: `%Files%`
- Sort by list item's properties: `False`
- First property to sort by: `INV-1042`
- Sort: `Ascending`
- Second property to sort by: `INV-1042`
- Sort: `Ascending`
- Third property to sort by: `INV-1042`
- Sort: `Ascending`
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Subtract lists

- **Id:** `variables/subtract-lists`
- **Kind:** native-action
- **Purpose:** Compare two lists and create a new list with the items that are in the first list but not in the second.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Subtract lists** on the canvas. Compare two lists and create a new list with the items that are in the first list but not in the second.

**Demonstration.**

```text
**Subtract lists**
- First list: `%Files%`
- Second list: `%Files%`
Produces:
- `%ListDifference%` (List of General values)
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Truncate number

- **Id:** `variables/truncate-number`
- **Kind:** native-action
- **Purpose:** Get the integral or fractional digits of a numeric value, or round up the value to a specified number of decimal places.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Truncate number** on the canvas. Get the integral or fractional digits of a numeric value, or round up the value to a specified number of decimal places.

**Demonstration.**

```text
**Truncate number**
- Number to truncate: `1`
- Operation: `Get integer part`
- Decimal places: `3`
Produces:
- `%TruncatedValue%` (Numeric value)
```

**Analogy.** One tool in that kit: labeled jars on a workbench you fill, sort, and pour from.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.

### Update data table item

- **Id:** `variables/update-data-table-item`
- **Kind:** native-action
- **Purpose:** Updates data table item.

**Use case.** In lists, tables, JSON, and counters the rest of the flow shares, drop **Update data table item** on the canvas. Updates data table item.

**Demonstration.**

```text
**Update data table item**
- Data table: `%InvoiceTable%`
- Column: `Amount`
- Row: `1`
- New value: `INV-1042`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Set variable to start; list and data table actions reshape data between Excel/files/HTTP.
