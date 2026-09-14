# Classic expression syntax (`% … %`)

Classic desktop flows (Power Fx **off**) evaluate expressions inside percent signs. This page is the language used in most production PAD flows. Power Fx flows are documented in [03-power-fx-functions.md](03-power-fx-functions.md).

## Basics

- Wrap expressions in `%` … `%`.
- Variable names are **not** case-sensitive (`MyVar` and `myvar` are the same).
- Lists and tables are **0-based**.
- Strings in expressions use single quotes: `%Concat + ' done'%`.

## Variables

```
%CustomerName%
%Total + 1%
%FirstName + ' ' + LastName%
```

## Booleans and logic

```
%True%
%False%
%Amount > 100 and Status = 'Open'%
%not IsEmpty%
```

Operators: `=`, `<>`, `<`, `<=`, `>`, `>=`, `and`, `or`, `not`.

## Numbers

```
%Price * Quantity%
%Counter + 1%
%Value mod 2%
```

Only **numeric** values can be used in arithmetic. Convert text first with **Convert text to number**.

## Datetime literals

```
%d"2026-09-14"%
%d"2026-09-14 09:30:00"%
```

## Lists

```
%Names[0]%              // first item
%Names[1]%              // second item
%Names[2:5]%            // items 3 and 4 (stop is exclusive)
%Names[:3]%             // first three
%Names[2:]%             // from the third to the end
```

Create a list literal:

```
%['A', 'B', 'C']%
```

## Datatables

```
%ExcelData[0][1]%                 // row 1, column 2
%ExcelData[0]['Amount']%          // named column
%ExcelData[1:4]%                  // rows 2–4
```

Literal table, with headers on the first row:

```
%{ ^['Product', 'Price'], ['Apples', 10], ['Pears', 12] }%
```

Append a row with `+`:

```
%ExcelData + ['Oranges', 9]%
```

## Custom objects

```
%{{ }}%
%{ 'Name': 'Ada', 'Id': 1 }%
%Person['Name']%
%Person.Name%
```

## Index versus Power Fx

| Task | Classic | Power Fx |
| --- | --- | --- |
| First list item | `%Items[0]%` | `=Index(Items, 1)` |
| Length | use **Parse text** / list properties | `=CountRows(Items)` |
| Start an expression | `%` | `=` |
| Variable names | case-insensitive | case-sensitive |

## UI / web selectors

You can embed a classic variable in a selector string. In Power Fx flows, use `${ formula }` interpolation instead.

## Common mistakes

- Forgetting `%` so PAD treats the text as a literal.
- Using 1-based indexes in a classic flow.
- Doing math on text that still has currency symbols — convert first.
- Using reserved keywords as variable names (`if`, `loop`, `end`, …).
