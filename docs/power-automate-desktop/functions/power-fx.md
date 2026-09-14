# Power Fx functions in desktop flows

Enable **Power Fx** when you create the flow. After that:

- Formulas start with `=`.
- Interpolated text uses `${expression}`.
- Variable names are **case-sensitive**.
- Use **Run Power Fx expression** (Variables module) when a formula must talk to a data source (`Collect`, `Patch`, `Clear`, …).

Official list: [Formula reference — desktop flows](https://learn.microsoft.com/en-us/power-platform/power-fx/formula-reference-desktop-flows).

**130 functions** are documented below. Signatures use Power Fx names. Examples are what you type in a PAD field (including the leading `=`).

## Operators (used with the functions)

| Operator | Meaning |
|---|---|
| `+` `-` `*` `/` | Arithmetic |
| `^` | Power (same as `Power()`) |
| `=` `<>` `>` `>=` `<` `<=` | Compare |
| `&&` / `And()` | Logical and |
| `\|\|` / `Or()` | Logical or |
| `!` / `Not()` | Logical not |
| `&` | Concatenate text (same idea as `Concatenate`) |
| `in` / `exactin` | Membership / substring tests |

Interpolation:

```text
The total is ${Sum(LineAmounts)}
```

Escape a literal `${` as `$${`.

---

## Logical and error handling

### And
`And(bool1, bool2, ...)` → boolean. True when every argument is true. Same as `&&`.
Example: `=And(Value(Age) >= 18, HasConsent)`

### Or
`Or(bool1, bool2, ...)` → boolean. True when any argument is true. Same as `||`.
Example: `=Or(Status = "Open", Status = "Retry")`

### Not
`Not(bool)` → boolean. Negates a value. Same as `!`.
Example: `=Not(IsBlank(Email))`

### If
`If(condition, thenValue [, elseIf, elseValue, ...] [, default])` → any.
Example: `=If(Amount > 1000, "Review", "Auto")`

### Switch
`Switch(value, match1, result1 [, match2, result2, ...] [, default])` → any.
Example: `=Switch(Country, "US", "USD", "DE", "EUR", "UNKNOWN")`

### Boolean
`Boolean(value)` → boolean. Coerces text, number, or dynamic values.
Example: `=Boolean("true")`

### Blank
`Blank()` → blank. Use when you need to clear a value.
Example: `=Blank()`

### Coalesce
`Coalesce(value1, value2, ...)` → first non-blank argument.
Example: `=Coalesce(Nickname, FullName, "Guest")`

### IsBlank
`IsBlank(value)` → boolean. True for blank / empty string in Power Fx.
Example: `=IsBlank(CustomerEmail)`

### IsEmpty
`IsEmpty(table)` → boolean. True when a table or collection has no rows.
Example: `=IsEmpty(Matches)`

### IsBlankOrError
`IsBlankOrError(value)` → boolean.
Example: `=If(IsBlankOrError(Result), 0, Result)`

### IsError
`IsError(value)` → boolean.
Example: `=IsError(Value(RawAmount))`

### IfError
`IfError(value, fallback [, value2, fallback2, ...] [, default])` → any. Returns fallback when value errors.
Example: `=IfError(Value(TextAmount), 0)`

### Error
`Error(message)` or `Error({Kind: ..., Message: ...})` → error. Raise or rethrow.
Example: `=If(Amount < 0, Error("Amount cannot be negative"), Amount)`

### IsNumeric
`IsNumeric(value)` → boolean.
Example: `=IsNumeric(RawAmount)`

### IsToday
`IsToday(datetime)` → boolean. True if the value is today in the user time zone.
Example: `=IsToday(InvoiceDate)`

### With
`With({name: value, ...}, formula)` → any. Names intermediate values.
Example: `=With({net: Price * Qty}, net * (1 + TaxRate))`

---

## Text

### Char
`Char(code)` → text. Character from a code point (ANSI-style in Power Fx).
Example: `=Char(10)` (line feed)

### UniChar
`UniChar(code)` → text. Character from a Unicode code point.
Example: `=UniChar(0x20AC)`

### Concatenate
`Concatenate(text1, text2, ...)` → text. Joins arguments.
Example: `=Concatenate("INV-", Text(Id), "-", Text(Today(), "yymmdd"))`

### Concat
`Concat(table, formula [, separator])` → text. Joins a column/formula across rows.
Example: `=Concat(Names, Value, ", ")`

### Left
`Left(text, count)` → text. Leading characters.
Example: `=Left(Account, 4)`

### Right
`Right(text, count)` → text. Trailing characters.
Example: `=Right(IBAN, 4)`

### Mid
`Mid(text, start [, count])` → text. `start` is 1-based.
Example: `=Mid(Sku, 3, 4)`

### Len
`Len(text)` → number. Length in characters.
Example: `=Len(Notes)`

### Lower
`Lower(text)` → text.
Example: `=Lower(Email)`

### Upper
`Upper(text)` → text.
Example: `=Upper(CountryCode)`

### Proper
`Proper(text)` → text. Capitalizes each word.
Example: `=Proper(fullName)`

### Trim
`Trim(text)` → text. Removes extra interior and end spaces.
Example: `=Trim(AddressLine)`

### TrimEnds
`TrimEnds(text)` → text. Removes only leading/trailing spaces.
Example: `=TrimEnds(PastedValue)`

### Replace
`Replace(text, start, count, replacement)` → text. Replaces by position (1-based).
Example: `=Replace(Account, 5, 4, "****")`

### Substitute
`Substitute(text, old, new [, instance])` → text. Replaces by match. Omit instance to replace all.
Example: `=Substitute(Path, "\\", "/")`

### Find
`Find(findText, withinText [, start])` → number. 1-based position, blank if missing.
Example: `=Find("@", Email)`

### Split
`Split(text, separator)` → table of `{Value: ...}` rows.
Example: `=First(Split(FullName, " ")).Value`

### StartsWith
`StartsWith(text, prefix)` → boolean. Case-insensitive.
Example: `=StartsWith(FileName, "INV")`

### EndsWith
`EndsWith(text, suffix)` → boolean. Case-insensitive.
Example: `=EndsWith(FileName, ".pdf")`

### Text
`Text(value [, format] [, language])` → text. Formats numbers and datetimes.
Example: `=Text(Amount, "$#,##0.00")`

### Value
`Value(text [, language])` → number. Parses a numeric string.
Example: `=Value(Mid(Cell, 2, 10))`

### Decimal
`Decimal(text [, language])` → decimal number. Prefer for currency-style values.
Example: `=Decimal(PriceText)`

### Float
`Float(text [, language])` → floating-point number.
Example: `=Float(Measurement)`

### EncodeUrl
`EncodeUrl(text)` → text. Percent-encodes for URLs.
Example: `=EncodeUrl(SearchTerm)`

### EncodeHTML
`EncodeHTML(text)` → text. Escapes HTML special characters.
Example: `=EncodeHTML(UserComment)`

### PlainText
`PlainText(html)` → text. Strips HTML/XML tags.
Example: `=PlainText(Mail.Body)`

---

## Numbers and math

### Abs
`Abs(number)` → number. Absolute value.
Example: `=Abs(Balance)`

### Average
`Average(number1, number2, ...)` or `Average(table, formula)` → number.
Example: `=Average(Score1, Score2, Score3)`

### Sum
`Sum(number1, ...)` or `Sum(table, formula)` → number.
Example: `=Sum(Lines, Amount)`

### Min / Max
`Min(...)` / `Max(...)` → number. Over arguments or a table formula.
Example: `=Max(Qty, 0)`

### Mod
`Mod(dividend, divisor)` → number. Remainder.
Example: `=Mod(Index, 2)`

### Int
`Int(number)` → number. Rounds toward −∞ to an integer.
Example: `=Int(3.9)` → `3`

### Trunc
`Trunc(number [, digits])` → number. Drops decimal digits toward zero.
Example: `=Trunc(3.9)` → `3`

### Round
`Round(number, digits)` → number. Round-half away from zero toward nearest.
Example: `=Round(Amount, 2)`

### RoundDown
`RoundDown(number, digits)` → number. Toward zero.
Example: `=RoundDown(Amount, 0)`

### RoundUp
`RoundUp(number, digits)` → number. Away from zero.
Example: `=RoundUp(Minutes / 15, 0)`

### Sqrt
`Sqrt(number)` → number.
Example: `=Sqrt(Area)`

### Power
`Power(base, exponent)` → number. Same as `base^exponent`.
Example: `=Power(1 + Rate, Years)`

### Exp
`Exp(number)` → number. *e* raised to `number`.
Example: `=Exp(1)`

### Ln
`Ln(number)` → number. Natural logarithm.
Example: `=Ln(Value)`

### Log
`Log(number [, base])` → number. Default base 10.
Example: `=Log(1000)` → `3`

### Pi
`Pi()` → number. π.
Example: `=Pi() * Radius * Radius`

### Sin / Cos / Tan
`Sin(radians)` `Cos(radians)` `Tan(radians)` → number.
Example: `=Sin(Radians(90))`

### Asin / Acos / Atan
Inverse trig, result in radians.
Example: `=Degrees(Asin(1))` → `90`

### Atan2
`Atan2(x, y)` → radians. Angle of the point `(x, y)`.
Example: `=Atan2(Adjacent, Opposite)`

### Acot / Cot
Arccotangent and cotangent, in radians.
Example: `=Cot(Pi() / 4)`

### Degrees
`Degrees(radians)` → number.
Example: `=Degrees(Pi())` → `180`

### Radians
`Radians(degrees)` → number.
Example: `=Radians(180)` → `π`

### Rand
`Rand()` → number. Uniform 0–1.
Example: `=Rand()`

### RandBetween
`RandBetween(low, high)` → integer between the bounds inclusive.
Example: `=RandBetween(1, 6)`

### StdevP
`StdevP(number1, ...)` or over a table. Population standard deviation.
Example: `=StdevP(Col1, Col2, Col3)`

### VarP
`VarP(...)` → number. Population variance.
Example: `=VarP(Sample1, Sample2, Sample3)`

### Sequence
`Sequence(count [, start [, step]])` → table of `{Value: n}`.
Example: `=Sequence(10)` 

### Hex2Dec
`Hex2Dec(hexText)` → number.
Example: `=Hex2Dec("FF")` → `255`

### Dec2Hex
`Dec2Hex(number [, places])` → text.
Example: `=Dec2Hex(255)` → `"FF"`

---

## Date and time

### Now
`Now()` → datetime. Current local date and time.
Example: `=Now()`

### Today
`Today()` → datetime. Current local date at midnight.
Example: `=Today()`

### Date
`Date(year, month, day)` → datetime.
Example: `=Date(2026, 9, 14)`

### Time
`Time(hour, minute, second)` → datetime (time of day).
Example: `=Time(17, 30, 0)`

### DateTime
`DateTime(year, month, day, hour, minute, second)` → datetime.
Example: `=DateTime(2026, 9, 14, 9, 0, 0)`

### DateValue
`DateValue(text [, language])` → datetime. Parses a date string.
Example: `=DateValue("14/9/2026")`

### TimeValue
`TimeValue(text [, language])` → datetime.
Example: `=TimeValue("17:30")`

### DateTimeValue
`DateTimeValue(text [, language])` → datetime.
Example: `=DateTimeValue("2026-09-14 17:30")`

### DateAdd
`DateAdd(datetime, units, unitName)` → datetime. `unitName` is `TimeUnit.Days` / `Months` / `Quarters` / `Years` (and similar time units supported in desktop).
Example: `=DateAdd(Today(), 7, TimeUnit.Days)`

### DateDiff
`DateDiff(start, end [, unit])` → number.
Example: `=DateDiff(StartDate, Now(), TimeUnit.Hours)`

### EDate
`EDate(datetime, months)` → datetime. Same day of month, shifted by months.
Example: `=EDate(Start, 3)`

### EOMonth
`EOMonth(datetime, months)` → datetime. Last day of the month after shifting.
Example: `=EOMonth(Today(), 0)`

### Year / Month / Day
`Year(datetime)` `Month(datetime)` `Day(datetime)` → number.
Example: `=Year(InvoiceDate)`

### Hour / Minute / Second
Extract time parts as numbers.
Example: `=Hour(Now())`

### Weekday
`Weekday(datetime [, startOfWeek])` → number. Day-of-week index.
Example: `=Weekday(Today())`

### WeekNum
`WeekNum(datetime [, startOfWeek])` → number. Week of year.
Example: `=WeekNum(Today())`

### TimeZoneOffset
`TimeZoneOffset([datetime])` → number. Minutes from UTC to local.
Example: `=TimeZoneOffset()`

---

## Tables, records, and lists

In desktop Power Fx, a PAD list of numbers is a table. `Index(table, n)` is **1-based**.

### Table
`Table(record1, record2, ...)` or `Table({...}, {...})` → table.
Example: `=Table({Name: "A", Qty: 1}, {Name: "B", Qty: 2})`

### Index
`Index(table, n)` → record. Row `n` (first row is 1).
Example: `=Index(Cities, 1)`

Nested cell (row 1, column 2 of a datatable): `=Index(Index(Data, 1), 2)`

### First
`First(table)` → record.
Example: `=First(Files).Name`

### Last
`Last(table)` → record.
Example: `=Last(LogLines)`

### FirstN
`FirstN(table, n)` → table. First `n` rows.
Example: `=FirstN(Results, 5)`

### LastN
`LastN(table, n)` → table.
Example: `=LastN(Events, 10)`

### Filter
`Filter(table, condition1 [, condition2, ...])` → table.
Example: `=Filter(Lines, Amount > 0)`

### Search
`Search(table, text, column1 [, column2, ...])` → table. Substring match in named columns.
Example: `=Search(Contacts, Box, "Name", "Email")`

### LookUp
`LookUp(table, condition [, resultFormula])` → record or value. First match.
Example: `=LookUp(Rates, Currency = "EUR", Rate)`

### Sort
`Sort(table, formula [, SortOrder.Ascending|Descending])` → table.
Example: `=Sort(Lines, Amount, SortOrder.Descending)`

### SortByColumns
`SortByColumns(table, column [, order] [, column2, order2, ...])` → table.
Example: `=SortByColumns(People, "LastName", SortOrder.Ascending)`

### Distinct
`Distinct(table, formula)` → table of unique `{Value: ...}`.
Example: `=Distinct(Orders, CustomerId)`

### Shuffle
`Shuffle(table)` → table. Random row order.
Example: `=First(Shuffle(Pool))`

### AddColumns
`AddColumns(table, name, formula [, name2, formula2, ...])` → table.
Example: `=AddColumns(Lines, Net, Qty * Price)`

### DropColumns
`DropColumns(table, column1 [, column2, ...])` → table.
Example: `=DropColumns(Data, "Temp")`

### ShowColumns
`ShowColumns(table, column1 [, column2, ...])` → table. Keeps only listed columns.
Example: `=ShowColumns(People, "Email", "Name")`

### RenameColumns
`RenameColumns(table, old, new [, old2, new2, ...])` → table.
Example: `=RenameColumns(Data, "F1", "Name")`

### CountRows
`CountRows(table)` → number.
Example: `=CountRows(Files)`

### Count
`Count(table)` → number. Rows whose formula/value is numeric.
Example: `=Count(Measures)`

### CountA
`CountA(table)` → number. Rows that are not blank.
Example: `=CountA(Answers)`

### CountIf
`CountIf(table, condition)` → number.
Example: `=CountIf(Lines, Amount < 0)`

### ForAll
`ForAll(table, formula)` → table or void. Evaluates formula per row.
Example: `=ForAll(Sequence(3), Rand())`

### Summarize
`Summarize(table, groupCol1 [, groupCol2, ...], name1, formula1, ...)` → table. Group and aggregate.
Example: `=Summarize(Lines, Customer, Total, Sum(Amount))`

---

## Collections and data sources

These write to collections or connected data. In PAD they are typically run from **Run Power Fx expression**.

### Collect
`Collect(collection, item_or_table)` → table. Creates or appends.
Example: `=Collect(Log, {At: Now(), Msg: "start"})`

### Clear
`Clear(collection)` → void. Deletes all rows.
Example: `=Clear(Log)`

### ClearCollect
`ClearCollect(collection, item_or_table)` → table. Clear then collect.
Example: `=ClearCollect(Batch, IncomingRows)`

### Patch
`Patch(source, record, change1 [, change2, ...])` or `Patch(source, tableOfChanges)` → record/table. Create or update.
Example: `=Patch(Items, First(Items), {Status: "Done"})`

### Remove
`Remove(source, record1 [, record2, ...] [, All])` → table. Deletes matching records.
Example: `=Remove(Log, First(Log))`

### Set
`Set(variable, value)` → value. Sets a global Power Fx variable.
Example: `=Set(Counter, Counter + 1)`

---

## Identity, language, GUID

### GUID
`GUID()` → new GUID. `GUID(text)` parses a GUID string.
Example: `=GUID()`

### Language
`Language()` → text. Current user language tag (`en-US`, …).
Example: `=Language()`

---

## Quick mapping from classic PAD habits

| Classic | Power Fx |
|---|---|
| `%StartsWith(A, B, True)%` | `StartsWith(A, B)` |
| `%Contains(A, B, True)%` | `B in A` or `Find(B, A)` |
| `%IsEmpty(A)%` | `IsBlank(A)` or `Len(A) = 0` |
| `%List[0]%` | `Index(List, 1)` or `First(List)` |
| `%List.Count%` | `CountRows(List)` |
| `%d"2026-09-14"%` | `Date(2026, 9, 14)` or `DateValue("2026-09-14")` |
| **Get current date and time** | `Now()` / `Today()` |
| **Join text** | `Concat(list, Value, ",")` or `Concatenate(...)` |
| **Split text** | `Split(text, ",")` |
| **Change text case** | `Upper` / `Lower` / `Proper` |
| **Replace text** | `Substitute` or `Replace` |
| **Convert text to number** | `Value` / `Decimal` / `Float` |
| **Add to datetime** | `DateAdd` |
| **Set variable** | `Set` or assign in the action still named **Set variable** |

## Function picker

In a Power Fx flow, open a field, choose **fx**, and browse the same list the designer currently supports. If a function appears in the picker but not here, the product added it after this catalog was built — prefer the picker plus the Microsoft formula reference.
