# Data types

PAD assigns a type from the value you store. Actions refuse inputs of the wrong type (you cannot add a text invoice number without converting it first).

Official reference: [Variable data types](https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-data-types).

## Simple types

| Type | How you typically create it | Notes |
|---|---|---|
| Text | **Set variable** with unquoted text in classic mode, or a quoted string in `%...%` | Most file names, selectors, and messages. |
| Numeric | **Set variable** with a number, or math inside `%...%` | Only numbers participate in `-`, `*`, `/`. |
| Boolean | `%True%` / `%False%` (classic) or `true` / `false` (Power Fx) | Produced by comparisons and the eight `%` text functions. |

## Collection types

| Type | How you typically create it | Access |
|---|---|---|
| List | **Create new list**, **Get files in folder**, **Split text** | `%List[0]%`, `%List.Count%` |
| Datatable | **Create new data table**, **Read from Excel worksheet**, **Execute SQL statement**, **Extract data from web page** | `%T[row][col]%` or `%T[row]['Name']%` |
| Datarow | A single row from a datatable or **For each** over a table | `%Row['Name']%`, `%Row.ColumnsCount%` |
| Custom object | **Convert JSON to custom object**, or `%{ 'Name': 'Ada' }%` | `%Obj['Name']%` |

Create a datatable in classic notation:

```text
%{{^['Product', 'Price'], ['A', 10], ['B', 20]}}%
```

(Exact builder UI is easier than hand-writing the array form.)

## Files, folders, mail, binary

| Type | Typical producer | See properties |
|---|---|---|
| File | **Get files in folder**, **Wait for file** | `.FullName`, `.Name`, `.Extension`, `.Size` |
| Folder | **Get subfolders in folder** | `.FullName`, `.FilesCount` |
| Binary data | **Convert file to binary data**, HTTP / connector file bodies | Convert back with **Convert binary data to file** |
| Mail message | **Retrieve email messages** (IMAP/Outlook/Exchange) | `.From`, `.Subject`, `.Body`, `.Attachments` |
| Credential | **Get credential** | `.Username`, `.Password` (sensitive) |
| Error | **Get last error** | `.Message`, `.ActionName`, `.SubflowName` |

## Instance types (handles)

These are not printable business values. You pass them into later actions in the same module.

| Type | Produced by | Closed by |
|---|---|---|
| Excel instance | Launch Excel / Attach to running Excel | Close Excel |
| Word instance | Launch Word / Attach to running Word | Close Word |
| Access instance | Launch Access | Close Access |
| Outlook instance | Launch Outlook | Close Outlook |
| Browser instance | Launch Edge / Chrome / Firefox / IE | Close web browser |
| Window instance | Get window | Close window |
| SQL connection | Open SQL connection | Close SQL connection |
| FTP connection | Open FTP connection | Close FTP connection |
| CMD session | Open CMD session | Close CMD session |
| Terminal session | Open terminal session | Close terminal session |
| Exchange connection | Connect to Exchange server | Close Exchange connection |
| SAP instance | Launch SAP | Close SAP connection |
| XML node / document | Read XML from file, XPath | Write XML to file |

Each instance type has a small property set (`.Handle`, `.IsAlive`, and similar) documented in [data-type-properties.md](data-type-properties.md).

## Cloud and directory objects

Returned by Azure, AWS, and Active Directory actions: resource groups, managed disks, snapshots, EBS volumes, AD user info, AD group info. Treat them as custom objects with the properties listed on the properties page.

## Blank

Any variable can hold Blank. In conditionals, use operators **Is blank** / **Is not blank**. Passing Blank into a non-nullable parameter fails the action.

## Power Fx types

When Power Fx is on, lists and tables follow Power Fx records/tables. Use `Index()`, `First()`, `Table()`, and `Value()` instead of `%List[0]%`. See [power-fx.md](power-fx.md).
