# Power Fx functions — how each function works

Only in Power Fx–enabled desktop flows. Formulas start with `=`. `Index` is 1-based.

130 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Abs

- **Id:** `power-fx/abs`
- **Kind:** power-fx-function
- **Purpose:** Distance of a number from zero.

**Use case.** Put **Abs** in an `=` formula when you need this: Distance of a number from zero.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Abs(InvoiceVariance)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Abs: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Acos

- **Id:** `power-fx/acos`
- **Kind:** power-fx-function
- **Purpose:** Arccosine of a number, in radians.

**Use case.** Put **Acos** in an `=` formula when you need this: Arccosine of a number, in radians.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Acos(0.5)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Acos: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Acot

- **Id:** `power-fx/acot`
- **Kind:** power-fx-function
- **Purpose:** Arccotangent of a number, in radians.

**Use case.** Put **Acot** in an `=` formula when you need this: Arccotangent of a number, in radians.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Acot(1)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Acot: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### AddColumns

- **Id:** `power-fx/addcolumns`
- **Kind:** power-fx-function
- **Purpose:** Returns a table with extra calculated columns.

**Use case.** Put **AddColumns** in an `=` formula when you need this: Returns a table with extra calculated columns.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=AddColumns(Orders, "Tax", Amount * 0.2)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled AddColumns: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### And

- **Id:** `power-fx/and`
- **Kind:** power-fx-function
- **Purpose:** True only when every argument is true (`&&`).

**Use case.** Put **And** in an `=` formula when you need this: True only when every argument is true (`&&`).

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=And(Amount > 0, Status = "Open")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled And: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Asin

- **Id:** `power-fx/asin`
- **Kind:** power-fx-function
- **Purpose:** Arcsine of a number, in radians.

**Use case.** Put **Asin** in an `=` formula when you need this: Arcsine of a number, in radians.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Asin(0.5)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Asin: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Atan

- **Id:** `power-fx/atan`
- **Kind:** power-fx-function
- **Purpose:** Arctangent of a number, in radians.

**Use case.** Put **Atan** in an `=` formula when you need this: Arctangent of a number, in radians.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Atan(1)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Atan: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Atan2

- **Id:** `power-fx/atan2`
- **Kind:** power-fx-function
- **Purpose:** Arctangent from an (x, y) pair, in radians.

**Use case.** Put **Atan2** in an `=` formula when you need this: Arctangent from an (x, y) pair, in radians.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Atan2(1, 1)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Atan2: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Average

- **Id:** `power-fx/average`
- **Kind:** power-fx-function
- **Purpose:** Mean of a table expression or argument list.

**Use case.** Put **Average** in an `=` formula when you need this: Mean of a table expression or argument list.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Average(AmountColumn)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Average: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Blank

- **Id:** `power-fx/blank`
- **Kind:** power-fx-function
- **Purpose:** A blank/null value for data sources.

**Use case.** Put **Blank** in an `=` formula when you need this: A blank/null value for data sources.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Blank()
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Blank: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Boolean

- **Id:** `power-fx/boolean`
- **Kind:** power-fx-function
- **Purpose:** Coerce text, number, or dynamic data to true/false.

**Use case.** Put **Boolean** in an `=` formula when you need this: Coerce text, number, or dynamic data to true/false.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Boolean("true")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Boolean: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Char

- **Id:** `power-fx/char`
- **Kind:** power-fx-function
- **Purpose:** Character for a numeric code.

**Use case.** Put **Char** in an `=` formula when you need this: Character for a numeric code.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Char(65)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Char: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Clear

- **Id:** `power-fx/clear`
- **Kind:** power-fx-function
- **Purpose:** Empty a collection.

**Use case.** Put **Clear** in an `=` formula when you need this: Empty a collection.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Clear(Scratch)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Clear: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### ClearCollect

- **Id:** `power-fx/clearcollect`
- **Kind:** power-fx-function
- **Purpose:** Empty a collection, then add records.

**Use case.** Put **ClearCollect** in an `=` formula when you need this: Empty a collection, then add records.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=ClearCollect(Scratch, FilteredRows)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled ClearCollect: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Coalesce

- **Id:** `power-fx/coalesce`
- **Kind:** power-fx-function
- **Purpose:** First non-blank argument.

**Use case.** Put **Coalesce** in an `=` formula when you need this: First non-blank argument.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Coalesce(PreferredEmail, BackupEmail, "unknown")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Coalesce: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Collect

- **Id:** `power-fx/collect`
- **Kind:** power-fx-function
- **Purpose:** Create a collection or append records.

**Use case.** Put **Collect** in an `=` formula when you need this: Create a collection or append records.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Collect(Results, CurrentRow)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Collect: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Concat

- **Id:** `power-fx/concat`
- **Kind:** power-fx-function
- **Purpose:** Join strings produced from a table.

**Use case.** Put **Concat** in an `=` formula when you need this: Join strings produced from a table.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Concat(Names, Value & ", ")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Concat: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Concatenate

- **Id:** `power-fx/concatenate`
- **Kind:** power-fx-function
- **Purpose:** Join two or more strings.

**Use case.** Put **Concatenate** in an `=` formula when you need this: Join two or more strings.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Concatenate(FirstName, " ", LastName)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Concatenate: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Cos

- **Id:** `power-fx/cos`
- **Kind:** power-fx-function
- **Purpose:** Cosine of an angle in radians.

**Use case.** Put **Cos** in an `=` formula when you need this: Cosine of an angle in radians.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Cos(Radians(60))
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Cos: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Cot

- **Id:** `power-fx/cot`
- **Kind:** power-fx-function
- **Purpose:** Cotangent of an angle in radians.

**Use case.** Put **Cot** in an `=` formula when you need this: Cotangent of an angle in radians.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Cot(Radians(45))
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Cot: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Count

- **Id:** `power-fx/count`
- **Kind:** power-fx-function
- **Purpose:** Count records that hold numbers.

**Use case.** Put **Count** in an `=` formula when you need this: Count records that hold numbers.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Count(AmountColumn)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Count: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### CountA

- **Id:** `power-fx/counta`
- **Kind:** power-fx-function
- **Purpose:** Count records that are not empty.

**Use case.** Put **CountA** in an `=` formula when you need this: Count records that are not empty.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=CountA(NameColumn)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled CountA: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### CountIf

- **Id:** `power-fx/countif`
- **Kind:** power-fx-function
- **Purpose:** Count records that match a condition.

**Use case.** Put **CountIf** in an `=` formula when you need this: Count records that match a condition.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=CountIf(Orders, Status = "Open")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled CountIf: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### CountRows

- **Id:** `power-fx/countrows`
- **Kind:** power-fx-function
- **Purpose:** Count all records.

**Use case.** Put **CountRows** in an `=` formula when you need this: Count all records.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=CountRows(Orders)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled CountRows: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Date

- **Id:** `power-fx/date`
- **Kind:** power-fx-function
- **Purpose:** Build a date from year, month, and day.

**Use case.** Put **Date** in an `=` formula when you need this: Build a date from year, month, and day.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Date(2026, 9, 14)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Date: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### DateAdd

- **Id:** `power-fx/dateadd`
- **Kind:** power-fx-function
- **Purpose:** Add days, months, quarters, or years.

**Use case.** Put **DateAdd** in an `=` formula when you need this: Add days, months, quarters, or years.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=DateAdd(Today(), 7, TimeUnit.Days)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled DateAdd: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### DateDiff

- **Id:** `power-fx/datediff`
- **Kind:** power-fx-function
- **Purpose:** Difference between two dates in a chosen unit.

**Use case.** Put **DateDiff** in an `=` formula when you need this: Difference between two dates in a chosen unit.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=DateDiff(StartDate, EndDate)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled DateDiff: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### DateTime

- **Id:** `power-fx/datetime`
- **Kind:** power-fx-function
- **Purpose:** Build a date/time from date and time parts.

**Use case.** Put **DateTime** in an `=` formula when you need this: Build a date/time from date and time parts.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=DateTime(2026, 9, 14, 9, 30, 0)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled DateTime: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### DateTimeValue

- **Id:** `power-fx/datetimevalue`
- **Kind:** power-fx-function
- **Purpose:** Parse a date-and-time string.

**Use case.** Put **DateTimeValue** in an `=` formula when you need this: Parse a date-and-time string.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=DateTimeValue("2026-09-14 09:30")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled DateTimeValue: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### DateValue

- **Id:** `power-fx/datevalue`
- **Kind:** power-fx-function
- **Purpose:** Parse a date-only string.

**Use case.** Put **DateValue** in an `=` formula when you need this: Parse a date-only string.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=DateValue("2026-09-14")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled DateValue: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Day

- **Id:** `power-fx/day`
- **Kind:** power-fx-function
- **Purpose:** Day-of-month from a date/time.

**Use case.** Put **Day** in an `=` formula when you need this: Day-of-month from a date/time.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Day(Today())
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Day: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Dec2Hex

- **Id:** `power-fx/dec2hex`
- **Kind:** power-fx-function
- **Purpose:** Number to hexadecimal text.

**Use case.** Put **Dec2Hex** in an `=` formula when you need this: Number to hexadecimal text.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Dec2Hex(255)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Dec2Hex: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Decimal

- **Id:** `power-fx/decimal`
- **Kind:** power-fx-function
- **Purpose:** Text to a decimal number.

**Use case.** Put **Decimal** in an `=` formula when you need this: Text to a decimal number.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Decimal("19.50")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Decimal: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Degrees

- **Id:** `power-fx/degrees`
- **Kind:** power-fx-function
- **Purpose:** Radians to degrees.

**Use case.** Put **Degrees** in an `=` formula when you need this: Radians to degrees.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Degrees(Pi()/2)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Degrees: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Distinct

- **Id:** `power-fx/distinct`
- **Kind:** power-fx-function
- **Purpose:** Unique records from a table.

**Use case.** Put **Distinct** in an `=` formula when you need this: Unique records from a table.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Distinct(Orders, Customer)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Distinct: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### DropColumns

- **Id:** `power-fx/dropcolumns`
- **Kind:** power-fx-function
- **Purpose:** Table without the named columns.

**Use case.** Put **DropColumns** in an `=` formula when you need this: Table without the named columns.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=DropColumns(Orders, "InternalId")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled DropColumns: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### EDate

- **Id:** `power-fx/edate`
- **Kind:** power-fx-function
- **Purpose:** Add months without changing the day-of-month.

**Use case.** Put **EDate** in an `=` formula when you need this: Add months without changing the day-of-month.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=EDate(Today(), 1)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled EDate: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### EncodeHTML

- **Id:** `power-fx/encodehtml`
- **Kind:** power-fx-function
- **Purpose:** Escape characters for HTML.

**Use case.** Put **EncodeHTML** in an `=` formula when you need this: Escape characters for HTML.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=EncodeHTML(RawComment)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled EncodeHTML: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### EncodeUrl

- **Id:** `power-fx/encodeurl`
- **Kind:** power-fx-function
- **Purpose:** Percent-encode a URL fragment.

**Use case.** Put **EncodeUrl** in an `=` formula when you need this: Percent-encode a URL fragment.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=EncodeUrl(SearchTerm)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled EncodeUrl: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### EndsWith

- **Id:** `power-fx/endswith`
- **Kind:** power-fx-function
- **Purpose:** True when a string ends with another string.

**Use case.** Put **EndsWith** in an `=` formula when you need this: True when a string ends with another string.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=EndsWith(FileName, ".pdf")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled EndsWith: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### EOMonth

- **Id:** `power-fx/eomonth`
- **Kind:** power-fx-function
- **Purpose:** Last day of a month after adding months.

**Use case.** Put **EOMonth** in an `=` formula when you need this: Last day of a month after adding months.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=EOMonth(Today(), 0)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled EOMonth: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Error

- **Id:** `power-fx/error`
- **Kind:** power-fx-function
- **Purpose:** Raise or forward an error.

**Use case.** Put **Error** in an `=` formula when you need this: Raise or forward an error.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Error("Row is missing Amount")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Error: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Exp

- **Id:** `power-fx/exp`
- **Kind:** power-fx-function
- **Purpose:** e raised to a power.

**Use case.** Put **Exp** in an `=` formula when you need this: e raised to a power.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Exp(1)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Exp: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Filter

- **Id:** `power-fx/filter`
- **Kind:** power-fx-function
- **Purpose:** Rows that match one or more conditions.

**Use case.** Put **Filter** in an `=` formula when you need this: Rows that match one or more conditions.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Filter(Orders, Status = "Open")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Filter: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Find

- **Id:** `power-fx/find`
- **Kind:** power-fx-function
- **Purpose:** Start position of one string inside another.

**Use case.** Put **Find** in an `=` formula when you need this: Start position of one string inside another.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Find("INV-", InvoiceText)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Find: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### First

- **Id:** `power-fx/first`
- **Kind:** power-fx-function
- **Purpose:** First record.

**Use case.** Put **First** in an `=` formula when you need this: First record.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=First(Orders)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled First: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### FirstN

- **Id:** `power-fx/firstn`
- **Kind:** power-fx-function
- **Purpose:** First N records.

**Use case.** Put **FirstN** in an `=` formula when you need this: First N records.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=FirstN(Orders, 10)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled FirstN: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Float

- **Id:** `power-fx/float`
- **Kind:** power-fx-function
- **Purpose:** Text to a floating-point number.

**Use case.** Put **Float** in an `=` formula when you need this: Text to a floating-point number.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Float("3.14")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Float: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### ForAll

- **Id:** `power-fx/forall`
- **Kind:** power-fx-function
- **Purpose:** Evaluate a formula for every record.

**Use case.** Put **ForAll** in an `=` formula when you need this: Evaluate a formula for every record.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=ForAll(Orders, Amount * 1.2)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled ForAll: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### GUID

- **Id:** `power-fx/guid`
- **Kind:** power-fx-function
- **Purpose:** Parse or create a GUID.

**Use case.** Put **GUID** in an `=` formula when you need this: Parse or create a GUID.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=GUID()
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled GUID: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Hex2Dec

- **Id:** `power-fx/hex2dec`
- **Kind:** power-fx-function
- **Purpose:** Hexadecimal text to a number.

**Use case.** Put **Hex2Dec** in an `=` formula when you need this: Hexadecimal text to a number.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Hex2Dec("FF")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Hex2Dec: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Hour

- **Id:** `power-fx/hour`
- **Kind:** power-fx-function
- **Purpose:** Hour portion of a date/time.

**Use case.** Put **Hour** in an `=` formula when you need this: Hour portion of a date/time.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Hour(Now())
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Hour: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### If

- **Id:** `power-fx/if`
- **Kind:** power-fx-function
- **Purpose:** Pick a result from a true/false test.

**Use case.** Run one branch when a check is true (file exists, row count > 0, status = 'Open').

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=If(Amount > 0, "OK", "Missing")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** Looking at a traffic light before you cross.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set. Combine with Else / Else if and End. Put Wait or If file exists before brittle UI/browser steps.

### IfError

- **Id:** `power-fx/iferror`
- **Kind:** power-fx-function
- **Purpose:** Fallback value or action when an error occurs.

**Use case.** Put **IfError** in an `=` formula when you need this: Fallback value or action when an error occurs.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=IfError(Value(RawAmount), 0)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled IfError: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Index

- **Id:** `power-fx/index`
- **Kind:** power-fx-function
- **Purpose:** Record at a 1-based position.

**Use case.** Put **Index** in an `=` formula when you need this: Record at a 1-based position.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Index(Orders, 1)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Index: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Int

- **Id:** `power-fx/int`
- **Kind:** power-fx-function
- **Purpose:** Round down to the nearest integer.

**Use case.** Put **Int** in an `=` formula when you need this: Round down to the nearest integer.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Int(19.8)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Int: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### IsBlank

- **Id:** `power-fx/isblank`
- **Kind:** power-fx-function
- **Purpose:** True when the value is blank.

**Use case.** Put **IsBlank** in an `=` formula when you need this: True when the value is blank.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=IsBlank(CustomerName)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled IsBlank: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### IsBlankOrError

- **Id:** `power-fx/isblankorerror`
- **Kind:** power-fx-function
- **Purpose:** True when the value is blank or an error.

**Use case.** Put **IsBlankOrError** in an `=` formula when you need this: True when the value is blank or an error.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=IsBlankOrError(LookedUpRow)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled IsBlankOrError: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### IsEmpty

- **Id:** `power-fx/isempty`
- **Kind:** power-fx-function
- **Purpose:** True when a table has no records.

**Use case.** Put **IsEmpty** in an `=` formula when you need this: True when a table has no records.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=IsEmpty(Orders)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled IsEmpty: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### IsError

- **Id:** `power-fx/iserror`
- **Kind:** power-fx-function
- **Purpose:** True when the value is an error.

**Use case.** Put **IsError** in an `=` formula when you need this: True when the value is an error.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=IsError(Value(RawAmount))
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled IsError: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### IsNumeric

- **Id:** `power-fx/isnumeric`
- **Kind:** power-fx-function
- **Purpose:** True when the value is numeric.

**Use case.** Put **IsNumeric** in an `=` formula when you need this: True when the value is numeric.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=IsNumeric(RawAmount)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled IsNumeric: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### IsToday

- **Id:** `power-fx/istoday`
- **Kind:** power-fx-function
- **Purpose:** True when the value falls on today's local date.

**Use case.** Put **IsToday** in an `=` formula when you need this: True when the value falls on today's local date.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=IsToday(DueDate)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled IsToday: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Language

- **Id:** `power-fx/language`
- **Kind:** power-fx-function
- **Purpose:** Language tag of the current user.

**Use case.** Put **Language** in an `=` formula when you need this: Language tag of the current user.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Language()
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Language: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Last

- **Id:** `power-fx/last`
- **Kind:** power-fx-function
- **Purpose:** Last record.

**Use case.** Put **Last** in an `=` formula when you need this: Last record.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Last(Orders)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Last: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### LastN

- **Id:** `power-fx/lastn`
- **Kind:** power-fx-function
- **Purpose:** Last N records.

**Use case.** Put **LastN** in an `=` formula when you need this: Last N records.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=LastN(Orders, 5)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled LastN: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Left

- **Id:** `power-fx/left`
- **Kind:** power-fx-function
- **Purpose:** Leftmost characters of a string.

**Use case.** Put **Left** in an `=` formula when you need this: Leftmost characters of a string.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Left(AccountCode, 3)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Left: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Len

- **Id:** `power-fx/len`
- **Kind:** power-fx-function
- **Purpose:** Character length.

**Use case.** Put **Len** in an `=` formula when you need this: Character length.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Len(CustomerName)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Len: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Ln

- **Id:** `power-fx/ln`
- **Kind:** power-fx-function
- **Purpose:** Natural logarithm.

**Use case.** Put **Ln** in an `=` formula when you need this: Natural logarithm.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Ln(10)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Ln: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Log

- **Id:** `power-fx/log`
- **Kind:** power-fx-function
- **Purpose:** Logarithm in a chosen base.

**Use case.** Put **Log** in an `=` formula when you need this: Logarithm in a chosen base.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Log(100, 10)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Log: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### LookUp

- **Id:** `power-fx/lookup`
- **Kind:** power-fx-function
- **Purpose:** First record that matches a condition.

**Use case.** Put **LookUp** in an `=` formula when you need this: First record that matches a condition.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=LookUp(Orders, OrderId = TargetId)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled LookUp: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Lower

- **Id:** `power-fx/lower`
- **Kind:** power-fx-function
- **Purpose:** Lowercase letters.

**Use case.** Put **Lower** in an `=` formula when you need this: Lowercase letters.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Lower(EmailAddress)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Lower: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Max

- **Id:** `power-fx/max`
- **Kind:** power-fx-function
- **Purpose:** Largest value in a set or table.

**Use case.** Put **Max** in an `=` formula when you need this: Largest value in a set or table.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Max(AmountColumn)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Max: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Mid

- **Id:** `power-fx/mid`
- **Kind:** power-fx-function
- **Purpose:** Substring from a start position.

**Use case.** Put **Mid** in an `=` formula when you need this: Substring from a start position.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Mid(AccountCode, 4, 2)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Mid: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Min

- **Id:** `power-fx/min`
- **Kind:** power-fx-function
- **Purpose:** Smallest value in a set or table.

**Use case.** Put **Min** in an `=` formula when you need this: Smallest value in a set or table.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Min(AmountColumn)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Min: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Minute

- **Id:** `power-fx/minute`
- **Kind:** power-fx-function
- **Purpose:** Minute portion of a date/time.

**Use case.** Put **Minute** in an `=` formula when you need this: Minute portion of a date/time.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Minute(Now())
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Minute: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Mod

- **Id:** `power-fx/mod`
- **Kind:** power-fx-function
- **Purpose:** Remainder after division.

**Use case.** Put **Mod** in an `=` formula when you need this: Remainder after division.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Mod(RowNumber, 2)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Mod: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Month

- **Id:** `power-fx/month`
- **Kind:** power-fx-function
- **Purpose:** Month number from a date/time.

**Use case.** Put **Month** in an `=` formula when you need this: Month number from a date/time.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Month(Today())
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Month: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Not

- **Id:** `power-fx/not`
- **Kind:** power-fx-function
- **Purpose:** Boolean negation (`!`).

**Use case.** Put **Not** in an `=` formula when you need this: Boolean negation (`!`).

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Not(IsEmpty(Orders))
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Not: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Now

- **Id:** `power-fx/now`
- **Kind:** power-fx-function
- **Purpose:** Current local date and time.

**Use case.** Put **Now** in an `=` formula when you need this: Current local date and time.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Now()
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Now: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Or

- **Id:** `power-fx/or`
- **Kind:** power-fx-function
- **Purpose:** True when any argument is true (`||`).

**Use case.** Put **Or** in an `=` formula when you need this: True when any argument is true (`||`).

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Or(Status = "Open", Status = "Held")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Or: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Patch

- **Id:** `power-fx/patch`
- **Kind:** power-fx-function
- **Purpose:** Create or merge records.

**Use case.** Put **Patch** in an `=` formula when you need this: Create or merge records.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Patch(Orders, First(Orders), {Status: "Posted"})
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Patch: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Pi

- **Id:** `power-fx/pi`
- **Kind:** power-fx-function
- **Purpose:** The constant π.

**Use case.** Put **Pi** in an `=` formula when you need this: The constant π.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Pi()
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Pi: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### PlainText

- **Id:** `power-fx/plaintext`
- **Kind:** power-fx-function
- **Purpose:** Strip HTML/XML tags.

**Use case.** Put **PlainText** in an `=` formula when you need this: Strip HTML/XML tags.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=PlainText(HtmlBody)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled PlainText: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Power

- **Id:** `power-fx/power`
- **Kind:** power-fx-function
- **Purpose:** Base raised to an exponent (`^`).

**Use case.** Put **Power** in an `=` formula when you need this: Base raised to an exponent (`^`).

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Power(2, 8)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Power: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Proper

- **Id:** `power-fx/proper`
- **Kind:** power-fx-function
- **Purpose:** Capitalize the first letter of each word.

**Use case.** Put **Proper** in an `=` formula when you need this: Capitalize the first letter of each word.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Proper(CustomerName)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Proper: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Radians

- **Id:** `power-fx/radians`
- **Kind:** power-fx-function
- **Purpose:** Degrees to radians.

**Use case.** Put **Radians** in an `=` formula when you need this: Degrees to radians.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Radians(180)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Radians: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Rand

- **Id:** `power-fx/rand`
- **Kind:** power-fx-function
- **Purpose:** Pseudo-random number between 0 and 1.

**Use case.** Put **Rand** in an `=` formula when you need this: Pseudo-random number between 0 and 1.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Rand()
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Rand: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### RandBetween

- **Id:** `power-fx/randbetween`
- **Kind:** power-fx-function
- **Purpose:** Pseudo-random integer in a range.

**Use case.** Put **RandBetween** in an `=` formula when you need this: Pseudo-random integer in a range.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=RandBetween(1, 6)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled RandBetween: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Remove

- **Id:** `power-fx/remove`
- **Kind:** power-fx-function
- **Purpose:** Delete specific records from a source.

**Use case.** Put **Remove** in an `=` formula when you need this: Delete specific records from a source.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Remove(Scratch, First(Scratch))
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Remove: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### RenameColumns

- **Id:** `power-fx/renamecolumns`
- **Kind:** power-fx-function
- **Purpose:** Rename one or more columns.

**Use case.** Put **RenameColumns** in an `=` formula when you need this: Rename one or more columns.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=RenameColumns(Orders, "Amt", "Amount")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled RenameColumns: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Replace

- **Id:** `power-fx/replace`
- **Kind:** power-fx-function
- **Purpose:** Overwrite characters by start position.

**Use case.** Put **Replace** in an `=` formula when you need this: Overwrite characters by start position.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Replace(AccountCode, 1, 3, "XX-")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Replace: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Right

- **Id:** `power-fx/right`
- **Kind:** power-fx-function
- **Purpose:** Rightmost characters of a string.

**Use case.** Put **Right** in an `=` formula when you need this: Rightmost characters of a string.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Right(FileName, 4)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Right: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Round

- **Id:** `power-fx/round`
- **Kind:** power-fx-function
- **Purpose:** Nearest value at a given precision.

**Use case.** Put **Round** in an `=` formula when you need this: Nearest value at a given precision.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Round(Amount, 2)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Round: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### RoundDown

- **Id:** `power-fx/rounddown`
- **Kind:** power-fx-function
- **Purpose:** Round toward zero/down.

**Use case.** Put **RoundDown** in an `=` formula when you need this: Round toward zero/down.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=RoundDown(Amount, 0)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled RoundDown: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### RoundUp

- **Id:** `power-fx/roundup`
- **Kind:** power-fx-function
- **Purpose:** Round away from zero/up.

**Use case.** Put **RoundUp** in an `=` formula when you need this: Round away from zero/up.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=RoundUp(Amount, 0)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled RoundUp: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Search

- **Id:** `power-fx/search`
- **Kind:** power-fx-function
- **Purpose:** Rows whose selected columns contain a string.

**Use case.** Put **Search** in an `=` formula when you need this: Rows whose selected columns contain a string.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Search(Orders, "acme", "Customer")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Search: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Second

- **Id:** `power-fx/second`
- **Kind:** power-fx-function
- **Purpose:** Second portion of a date/time.

**Use case.** Put **Second** in an `=` formula when you need this: Second portion of a date/time.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Second(Now())
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Second: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Sequence

- **Id:** `power-fx/sequence`
- **Kind:** power-fx-function
- **Purpose:** Table of sequential numbers.

**Use case.** Put **Sequence** in an `=` formula when you need this: Table of sequential numbers.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Sequence(10)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Sequence: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Set

- **Id:** `power-fx/set`
- **Kind:** power-fx-function
- **Purpose:** Assign a global; limited support in PAD.

**Use case.** Put **Set** in an `=` formula when you need this: Assign a global; limited support in PAD.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Set(Index(Scratch, 1), 42)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Set: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### ShowColumns

- **Id:** `power-fx/showcolumns`
- **Kind:** power-fx-function
- **Purpose:** Keep only the named columns.

**Use case.** Put **ShowColumns** in an `=` formula when you need this: Keep only the named columns.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=ShowColumns(Orders, "OrderId", "Amount")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled ShowColumns: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Shuffle

- **Id:** `power-fx/shuffle`
- **Kind:** power-fx-function
- **Purpose:** Randomize record order.

**Use case.** Put **Shuffle** in an `=` formula when you need this: Randomize record order.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Shuffle(Orders)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Shuffle: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Sin

- **Id:** `power-fx/sin`
- **Kind:** power-fx-function
- **Purpose:** Sine of an angle in radians.

**Use case.** Put **Sin** in an `=` formula when you need this: Sine of an angle in radians.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Sin(Radians(30))
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Sin: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Sort

- **Id:** `power-fx/sort`
- **Kind:** power-fx-function
- **Purpose:** Sort records by a formula.

**Use case.** Put **Sort** in an `=` formula when you need this: Sort records by a formula.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Sort(Orders, Amount, Descending)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Sort: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### SortByColumns

- **Id:** `power-fx/sortbycolumns`
- **Kind:** power-fx-function
- **Purpose:** Sort records by column names.

**Use case.** Put **SortByColumns** in an `=` formula when you need this: Sort records by column names.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=SortByColumns(Orders, "Customer")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled SortByColumns: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Split

- **Id:** `power-fx/split`
- **Kind:** power-fx-function
- **Purpose:** Break a string into a table of pieces.

**Use case.** Put **Split** in an `=` formula when you need this: Break a string into a table of pieces.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Split(FileName, ".")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Split: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Sqrt

- **Id:** `power-fx/sqrt`
- **Kind:** power-fx-function
- **Purpose:** Square root.

**Use case.** Put **Sqrt** in an `=` formula when you need this: Square root.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Sqrt(9)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Sqrt: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### StartsWith

- **Id:** `power-fx/startswith`
- **Kind:** power-fx-function
- **Purpose:** True when a string begins with another string.

**Use case.** Put **StartsWith** in an `=` formula when you need this: True when a string begins with another string.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=StartsWith(InvoiceNumber, "INV")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled StartsWith: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### StdevP

- **Id:** `power-fx/stdevp`
- **Kind:** power-fx-function
- **Purpose:** Population standard deviation.

**Use case.** Put **StdevP** in an `=` formula when you need this: Population standard deviation.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=StdevP(AmountColumn)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled StdevP: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Substitute

- **Id:** `power-fx/substitute`
- **Kind:** power-fx-function
- **Purpose:** Replace matching substrings.

**Use case.** Put **Substitute** in an `=` formula when you need this: Replace matching substrings.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Substitute(FileName, " ", "_")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Substitute: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Sum

- **Id:** `power-fx/sum`
- **Kind:** power-fx-function
- **Purpose:** Total of a table expression or argument list.

**Use case.** Put **Sum** in an `=` formula when you need this: Total of a table expression or argument list.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Sum(Orders, Amount)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Sum: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Summarize

- **Id:** `power-fx/summarize`
- **Kind:** power-fx-function
- **Purpose:** Group rows and aggregate the rest.

**Use case.** Put **Summarize** in an `=` formula when you need this: Group rows and aggregate the rest.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Summarize(Orders, Customer, "Total", Sum(Amount))
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Summarize: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Switch

- **Id:** `power-fx/switch`
- **Kind:** power-fx-function
- **Purpose:** Match a value and evaluate the matching formula.

**Use case.** Put **Switch** in an `=` formula when you need this: Match a value and evaluate the matching formula.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Switch(Status, "Open", 1, "Closed", 2, 0)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Switch: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Table

- **Id:** `power-fx/table`
- **Kind:** power-fx-function
- **Purpose:** Build a temporary table from records.

**Use case.** Put **Table** in an `=` formula when you need this: Build a temporary table from records.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Table({Name: "Ada", Amount: 10})
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Table: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Tan

- **Id:** `power-fx/tan`
- **Kind:** power-fx-function
- **Purpose:** Tangent of an angle in radians.

**Use case.** Put **Tan** in an `=` formula when you need this: Tangent of an angle in radians.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Tan(Radians(45))
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Tan: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Text

- **Id:** `power-fx/text`
- **Kind:** power-fx-function
- **Purpose:** Format any value as text.

**Use case.** Put **Text** in an `=` formula when you need this: Format any value as text.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Text(Today(), "yyyy-mm-dd")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Text: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Time

- **Id:** `power-fx/time`
- **Kind:** power-fx-function
- **Purpose:** Build a time from hour, minute, and second.

**Use case.** Put **Time** in an `=` formula when you need this: Build a time from hour, minute, and second.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Time(9, 30, 0)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Time: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### TimeValue

- **Id:** `power-fx/timevalue`
- **Kind:** power-fx-function
- **Purpose:** Parse a time-only string.

**Use case.** Put **TimeValue** in an `=` formula when you need this: Parse a time-only string.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=TimeValue("09:30")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled TimeValue: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### TimeZoneOffset

- **Id:** `power-fx/timezoneoffset`
- **Kind:** power-fx-function
- **Purpose:** Minutes between UTC and local time.

**Use case.** Put **TimeZoneOffset** in an `=` formula when you need this: Minutes between UTC and local time.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=TimeZoneOffset()
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled TimeZoneOffset: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Today

- **Id:** `power-fx/today`
- **Kind:** power-fx-function
- **Purpose:** Current local date (no time).

**Use case.** Put **Today** in an `=` formula when you need this: Current local date (no time).

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Today()
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Today: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Trim

- **Id:** `power-fx/trim`
- **Kind:** power-fx-function
- **Purpose:** Collapse extra interior and edge spaces.

**Use case.** Put **Trim** in an `=` formula when you need this: Collapse extra interior and edge spaces.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Trim(CustomerName)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Trim: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### TrimEnds

- **Id:** `power-fx/trimends`
- **Kind:** power-fx-function
- **Purpose:** Strip leading and trailing spaces only.

**Use case.** Put **TrimEnds** in an `=` formula when you need this: Strip leading and trailing spaces only.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=TrimEnds(CustomerName)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled TrimEnds: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Trunc

- **Id:** `power-fx/trunc`
- **Kind:** power-fx-function
- **Purpose:** Drop the fractional part of a number.

**Use case.** Put **Trunc** in an `=` formula when you need this: Drop the fractional part of a number.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Trunc(19.8)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Trunc: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### UniChar

- **Id:** `power-fx/unichar`
- **Kind:** power-fx-function
- **Purpose:** Character for a Unicode code point.

**Use case.** Put **UniChar** in an `=` formula when you need this: Character for a Unicode code point.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=UniChar(9731)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled UniChar: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Upper

- **Id:** `power-fx/upper`
- **Kind:** power-fx-function
- **Purpose:** Uppercase letters.

**Use case.** Put **Upper** in an `=` formula when you need this: Uppercase letters.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Upper(CountryCode)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Upper: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Value

- **Id:** `power-fx/value`
- **Kind:** power-fx-function
- **Purpose:** Parse text as a number.

**Use case.** Put **Value** in an `=` formula when you need this: Parse text as a number.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Value("19.50")
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Value: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### VarP

- **Id:** `power-fx/varp`
- **Kind:** power-fx-function
- **Purpose:** Population variance.

**Use case.** Put **VarP** in an `=` formula when you need this: Population variance.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=VarP(AmountColumn)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled VarP: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Weekday

- **Id:** `power-fx/weekday`
- **Kind:** power-fx-function
- **Purpose:** Weekday number from a date/time.

**Use case.** Put **Weekday** in an `=` formula when you need this: Weekday number from a date/time.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Weekday(Today())
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Weekday: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### WeekNum

- **Id:** `power-fx/weeknum`
- **Kind:** power-fx-function
- **Purpose:** Week number of a date/time.

**Use case.** Put **WeekNum** in an `=` formula when you need this: Week number of a date/time.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=WeekNum(Today())
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled WeekNum: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### With

- **Id:** `power-fx/with`
- **Kind:** power-fx-function
- **Purpose:** Evaluate a formula against a named record.

**Use case.** Put **With** in an `=` formula when you need this: Evaluate a formula against a named record.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=With({Rate: 0.2}, Amount * Rate)
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled With: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.

### Year

- **Id:** `power-fx/year`
- **Kind:** power-fx-function
- **Purpose:** Year from a date/time.

**Use case.** Put **Year** in an `=` formula when you need this: Year from a date/time.

**Demonstration.**

In a Power Fx–enabled flow, type this in an input that accepts a formula:

```powerfx
=Year(Today())
```

Store the result with Set / a produced variable, or nest it inside If / Filter.

**Analogy.** A calculator button labeled Year: same idea as Excel, used inside `=` formulas.

**In combination.** Nest in If / Filter / With; write the result with Excel, File, or Set.
