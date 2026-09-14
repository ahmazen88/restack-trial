# Classic `%` notation — operators and functions

Use this language when the desktop flow does **not** have Power Fx enabled. Every expression sits between percent signs.

Escape a literal percent character as `%%`.

Official reference: [Variable manipulation and the % notation](https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-manipulation).

## How an expression is evaluated

| You write | Meaning |
|---|---|
| `%CustomerName%` | Value of variable `CustomerName`. |
| `%5 * Quantity%` | Arithmetic using a variable. |
| `%'Hello ' + Name%` | Text concatenate (`+` also joins text). |
| `Prefix-%Id%-suffix` | Variable interpolated inside surrounding text. |
| `%% complete` | Literal `% complete`. |

Text literals inside `%...%` use **single quotes**: `%'invoice'`.

Boolean literals: `%True%`, `%False%`. Empty / null: assign **Blank** where the field allows it.

Datetime literal:

```text
%d"yyyy-MM-dd HH:mm:ss.ff+zzz"%
```

Example: `%d"2026-09-14"%` is midnight on 14 September 2026.

## Indexing and slicing (not functions, but used like them)

Lists are **zero-based**.

| Expression | Result |
|---|---|
| `%Cities[0]%` | First item. |
| `%Cities[1]%` | Second item. |
| `%Cities[2:4]%` | Third and fourth items (stop index excluded). |
| `%Cities[:3]%` | First three items. |
| `%Cities[2:]%` | From the third item to the end. |
| `%Table[0][1]%` | First row, second column of a datatable. |
| `%Table[0]['Amount']%` | First row, column named Amount (when headers exist). |
| `%Person['Email']%` | Property on a custom object. |
| `%Files.Count%` | Data-type property (see [properties](data-type-properties.md)). |

## Arithmetic operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Add numbers, or concatenate text | `%3 + 4%` | `7` |
| `+` | Concatenate when either side is text | `%'PO-' + 1042%` | `PO-1042` |
| `-` | Subtract | `%Total - Tax%` | number |
| `*` | Multiply | `%Qty * Price%` | number |
| `/` | Divide | `%10 / 4%` | `2.5` |

Parentheses change order: `%(A + B) * C%`.

## Comparison operators

Comparisons return `%True%` or `%False%`. Both sides must be the same type.

| Operator | Meaning |
|---|---|
| `=` | Equal |
| `<>` | Not equal |
| `<` | Less than |
| `<=` | Less than or equal |
| `>` | Greater than |
| `>=` | Greater than or equal |

Example: `%Status = 'Closed'%`

## Logical operators

| Operator | Meaning | Example |
|---|---|---|
| `AND` | True only if both sides are true | `%Index = 1 AND Ready%` |
| `OR` | True if either side is true | `%Index = 1 OR Index = 2%` |
| `NOT` | Negate | `%NOT(Failed)%` |

`NOT` is written as a function-like form: `%NOT(expression)%`.

## Text test functions

These eight functions are the **entire** classic function library. They return boolean values and are what you use inside **If**, **Wait**, and **Loop condition** when you do not want a separate **Parse text** action.

Ignore-case arguments are `%True%` or `%False%`.

### StartsWith

```text
%StartsWith(text, prefix, ignoreCase)%
```

**Returns:** Boolean.

True when `text` begins with `prefix`.

```text
%StartsWith(File.Name, 'INV', True)%
```

### NotStartsWith

```text
%NotStartsWith(text, prefix, ignoreCase)%
```

**Returns:** Boolean.

True when `text` does not begin with `prefix`.

```text
%NotStartsWith(File.Extension, '.tmp', True)%
```

### EndsWith

```text
%EndsWith(text, suffix, ignoreCase)%
```

**Returns:** Boolean.

True when `text` ends with `suffix`.

```text
%EndsWith(File.Name, '.xlsx', True)%
```

### NotEndsWith

```text
%NotEndsWith(text, suffix, ignoreCase)%
```

**Returns:** Boolean.

True when `text` does not end with `suffix`.

### Contains

```text
%Contains(text, search, ignoreCase)%
```

**Returns:** Boolean.

True when `search` occurs anywhere inside `text`.

```text
%Contains(Email.Subject, 'urgent', True)%
```

### NotContains

```text
%NotContains(text, search, ignoreCase)%
```

**Returns:** Boolean.

True when `search` does not occur in `text`.

### IsEmpty

```text
%IsEmpty(text)%
```

**Returns:** Boolean.

True when `text` has length 0. Does not treat Blank the same way as the **Is blank** operator on conditionals — use **If** with *Is blank* / *Is not blank* for nulls.

```text
%IsEmpty(TrimmedName)%
```

### IsNotEmpty

```text
%IsNotEmpty(text)%
```

**Returns:** Boolean.

True when `text` contains one or more characters.

## What classic mode does *not* have

There is no classic `Substring()`, `Length()`, `Replace()`, `Upper()`, or `Now()` function. Use:

| Need | Action or property |
|---|---|
| Length | `%MyText.Length%` or **Get subtext** |
| Upper / lower | `%MyText.ToUpper%` / `.ToLower` or **Change text case** |
| Trim | `%MyText.Trimmed%` or **Trim text** |
| Replace / split / join | **Replace text**, **Split text**, **Join text** |
| Parse / regex | **Parse text** |
| Current time | **Get current date and time** |
| Random | **Generate random number** / **Create random text** |
| JSON | **Convert JSON to custom object** |

If you need Excel-style formulas in the field, create the flow with **Power Fx** enabled and use [power-fx.md](power-fx.md).
