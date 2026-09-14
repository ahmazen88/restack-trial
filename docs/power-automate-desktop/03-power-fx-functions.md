# Power Fx functions in desktop flows

These functions are available when a desktop flow is **Power Fx–enabled**. Type `=` in an input to start a formula. Variable names are case-sensitive. `Index` is **1-based** (unlike classic `%List[0]%` indexing).

Classic flows keep the `%Expression%` language instead of this list.

Official catalog: [Formula reference - desktop flows](https://learn.microsoft.com/en-us/power-platform/power-fx/formula-reference-desktop-flows).

## Functions

## Collection

### Clear

- **Kind:** power-fx-function
- **Purpose:** Empty a collection.
- **Example shape:** `=Clear(...)`

### ClearCollect

- **Kind:** power-fx-function
- **Purpose:** Empty a collection, then add records.
- **Example shape:** `=ClearCollect(...)`

### Collect

- **Kind:** power-fx-function
- **Purpose:** Create a collection or append records.
- **Example shape:** `=Collect(...)`


## Conversion

### Boolean

- **Kind:** power-fx-function
- **Purpose:** Coerce text, number, or dynamic data to true/false.
- **Example shape:** `=Boolean(...)`

### Dec2Hex

- **Kind:** power-fx-function
- **Purpose:** Number to hexadecimal text.
- **Example shape:** `=Dec2Hex(...)`

### Decimal

- **Kind:** power-fx-function
- **Purpose:** Text to a decimal number.
- **Example shape:** `=Decimal(...)`

### Float

- **Kind:** power-fx-function
- **Purpose:** Text to a floating-point number.
- **Example shape:** `=Float(...)`

### Hex2Dec

- **Kind:** power-fx-function
- **Purpose:** Hexadecimal text to a number.
- **Example shape:** `=Hex2Dec(...)`

### Text

- **Kind:** power-fx-function
- **Purpose:** Format any value as text.
- **Example shape:** `=Text(...)`

### Value

- **Kind:** power-fx-function
- **Purpose:** Parse text as a number.
- **Example shape:** `=Value(...)`


## Date

### Date

- **Kind:** power-fx-function
- **Purpose:** Build a date from year, month, and day.
- **Example shape:** `=Date(...)`

### DateAdd

- **Kind:** power-fx-function
- **Purpose:** Add days, months, quarters, or years.
- **Example shape:** `=DateAdd(...)`

### DateDiff

- **Kind:** power-fx-function
- **Purpose:** Difference between two dates in a chosen unit.
- **Example shape:** `=DateDiff(...)`

### DateTime

- **Kind:** power-fx-function
- **Purpose:** Build a date/time from date and time parts.
- **Example shape:** `=DateTime(...)`

### DateTimeValue

- **Kind:** power-fx-function
- **Purpose:** Parse a date-and-time string.
- **Example shape:** `=DateTimeValue(...)`

### DateValue

- **Kind:** power-fx-function
- **Purpose:** Parse a date-only string.
- **Example shape:** `=DateValue(...)`

### Day

- **Kind:** power-fx-function
- **Purpose:** Day-of-month from a date/time.
- **Example shape:** `=Day(...)`

### EDate

- **Kind:** power-fx-function
- **Purpose:** Add months without changing the day-of-month.
- **Example shape:** `=EDate(...)`

### EOMonth

- **Kind:** power-fx-function
- **Purpose:** Last day of a month after adding months.
- **Example shape:** `=EOMonth(...)`

### Hour

- **Kind:** power-fx-function
- **Purpose:** Hour portion of a date/time.
- **Example shape:** `=Hour(...)`

### IsToday

- **Kind:** power-fx-function
- **Purpose:** True when the value falls on today's local date.
- **Example shape:** `=IsToday(...)`

### Minute

- **Kind:** power-fx-function
- **Purpose:** Minute portion of a date/time.
- **Example shape:** `=Minute(...)`

### Month

- **Kind:** power-fx-function
- **Purpose:** Month number from a date/time.
- **Example shape:** `=Month(...)`

### Now

- **Kind:** power-fx-function
- **Purpose:** Current local date and time.
- **Example shape:** `=Now(...)`

### Second

- **Kind:** power-fx-function
- **Purpose:** Second portion of a date/time.
- **Example shape:** `=Second(...)`

### Time

- **Kind:** power-fx-function
- **Purpose:** Build a time from hour, minute, and second.
- **Example shape:** `=Time(...)`

### TimeValue

- **Kind:** power-fx-function
- **Purpose:** Parse a time-only string.
- **Example shape:** `=TimeValue(...)`

### TimeZoneOffset

- **Kind:** power-fx-function
- **Purpose:** Minutes between UTC and local time.
- **Example shape:** `=TimeZoneOffset(...)`

### Today

- **Kind:** power-fx-function
- **Purpose:** Current local date (no time).
- **Example shape:** `=Today(...)`

### Weekday

- **Kind:** power-fx-function
- **Purpose:** Weekday number from a date/time.
- **Example shape:** `=Weekday(...)`

### WeekNum

- **Kind:** power-fx-function
- **Purpose:** Week number of a date/time.
- **Example shape:** `=WeekNum(...)`

### Year

- **Kind:** power-fx-function
- **Purpose:** Year from a date/time.
- **Example shape:** `=Year(...)`


## Logic

### And

- **Kind:** power-fx-function
- **Purpose:** True only when every argument is true (`&&`).
- **Example shape:** `=And(...)`

### Error

- **Kind:** power-fx-function
- **Purpose:** Raise or forward an error.
- **Example shape:** `=Error(...)`

### If

- **Kind:** power-fx-function
- **Purpose:** Pick a result from a true/false test.
- **Example shape:** `=If(...)`

### IfError

- **Kind:** power-fx-function
- **Purpose:** Fallback value or action when an error occurs.
- **Example shape:** `=IfError(...)`

### IsBlank

- **Kind:** power-fx-function
- **Purpose:** True when the value is blank.
- **Example shape:** `=IsBlank(...)`

### IsBlankOrError

- **Kind:** power-fx-function
- **Purpose:** True when the value is blank or an error.
- **Example shape:** `=IsBlankOrError(...)`

### IsEmpty

- **Kind:** power-fx-function
- **Purpose:** True when a table has no records.
- **Example shape:** `=IsEmpty(...)`

### IsError

- **Kind:** power-fx-function
- **Purpose:** True when the value is an error.
- **Example shape:** `=IsError(...)`

### IsNumeric

- **Kind:** power-fx-function
- **Purpose:** True when the value is numeric.
- **Example shape:** `=IsNumeric(...)`

### Not

- **Kind:** power-fx-function
- **Purpose:** Boolean negation (`!`).
- **Example shape:** `=Not(...)`

### Or

- **Kind:** power-fx-function
- **Purpose:** True when any argument is true (`||`).
- **Example shape:** `=Or(...)`

### Switch

- **Kind:** power-fx-function
- **Purpose:** Match a value and evaluate the matching formula.
- **Example shape:** `=Switch(...)`


## Math

### Abs

- **Kind:** power-fx-function
- **Purpose:** Distance of a number from zero.
- **Example shape:** `=Abs(...)`

### Acos

- **Kind:** power-fx-function
- **Purpose:** Arccosine of a number, in radians.
- **Example shape:** `=Acos(...)`

### Acot

- **Kind:** power-fx-function
- **Purpose:** Arccotangent of a number, in radians.
- **Example shape:** `=Acot(...)`

### Asin

- **Kind:** power-fx-function
- **Purpose:** Arcsine of a number, in radians.
- **Example shape:** `=Asin(...)`

### Atan

- **Kind:** power-fx-function
- **Purpose:** Arctangent of a number, in radians.
- **Example shape:** `=Atan(...)`

### Atan2

- **Kind:** power-fx-function
- **Purpose:** Arctangent from an (x, y) pair, in radians.
- **Example shape:** `=Atan2(...)`

### Average

- **Kind:** power-fx-function
- **Purpose:** Mean of a table expression or argument list.
- **Example shape:** `=Average(...)`

### Cos

- **Kind:** power-fx-function
- **Purpose:** Cosine of an angle in radians.
- **Example shape:** `=Cos(...)`

### Cot

- **Kind:** power-fx-function
- **Purpose:** Cotangent of an angle in radians.
- **Example shape:** `=Cot(...)`

### Degrees

- **Kind:** power-fx-function
- **Purpose:** Radians to degrees.
- **Example shape:** `=Degrees(...)`

### Exp

- **Kind:** power-fx-function
- **Purpose:** e raised to a power.
- **Example shape:** `=Exp(...)`

### Int

- **Kind:** power-fx-function
- **Purpose:** Round down to the nearest integer.
- **Example shape:** `=Int(...)`

### Ln

- **Kind:** power-fx-function
- **Purpose:** Natural logarithm.
- **Example shape:** `=Ln(...)`

### Log

- **Kind:** power-fx-function
- **Purpose:** Logarithm in a chosen base.
- **Example shape:** `=Log(...)`

### Max

- **Kind:** power-fx-function
- **Purpose:** Largest value in a set or table.
- **Example shape:** `=Max(...)`

### Min

- **Kind:** power-fx-function
- **Purpose:** Smallest value in a set or table.
- **Example shape:** `=Min(...)`

### Mod

- **Kind:** power-fx-function
- **Purpose:** Remainder after division.
- **Example shape:** `=Mod(...)`

### Pi

- **Kind:** power-fx-function
- **Purpose:** The constant π.
- **Example shape:** `=Pi(...)`

### Power

- **Kind:** power-fx-function
- **Purpose:** Base raised to an exponent (`^`).
- **Example shape:** `=Power(...)`

### Radians

- **Kind:** power-fx-function
- **Purpose:** Degrees to radians.
- **Example shape:** `=Radians(...)`

### Rand

- **Kind:** power-fx-function
- **Purpose:** Pseudo-random number between 0 and 1.
- **Example shape:** `=Rand(...)`

### RandBetween

- **Kind:** power-fx-function
- **Purpose:** Pseudo-random integer in a range.
- **Example shape:** `=RandBetween(...)`

### Round

- **Kind:** power-fx-function
- **Purpose:** Nearest value at a given precision.
- **Example shape:** `=Round(...)`

### RoundDown

- **Kind:** power-fx-function
- **Purpose:** Round toward zero/down.
- **Example shape:** `=RoundDown(...)`

### RoundUp

- **Kind:** power-fx-function
- **Purpose:** Round away from zero/up.
- **Example shape:** `=RoundUp(...)`

### Sin

- **Kind:** power-fx-function
- **Purpose:** Sine of an angle in radians.
- **Example shape:** `=Sin(...)`

### Sqrt

- **Kind:** power-fx-function
- **Purpose:** Square root.
- **Example shape:** `=Sqrt(...)`

### StdevP

- **Kind:** power-fx-function
- **Purpose:** Population standard deviation.
- **Example shape:** `=StdevP(...)`

### Sum

- **Kind:** power-fx-function
- **Purpose:** Total of a table expression or argument list.
- **Example shape:** `=Sum(...)`

### Tan

- **Kind:** power-fx-function
- **Purpose:** Tangent of an angle in radians.
- **Example shape:** `=Tan(...)`

### Trunc

- **Kind:** power-fx-function
- **Purpose:** Drop the fractional part of a number.
- **Example shape:** `=Trunc(...)`

### VarP

- **Kind:** power-fx-function
- **Purpose:** Population variance.
- **Example shape:** `=VarP(...)`


## Table

### AddColumns

- **Kind:** power-fx-function
- **Purpose:** Returns a table with extra calculated columns.
- **Example shape:** `=AddColumns(...)`

### Count

- **Kind:** power-fx-function
- **Purpose:** Count records that hold numbers.
- **Example shape:** `=Count(...)`

### CountA

- **Kind:** power-fx-function
- **Purpose:** Count records that are not empty.
- **Example shape:** `=CountA(...)`

### CountIf

- **Kind:** power-fx-function
- **Purpose:** Count records that match a condition.
- **Example shape:** `=CountIf(...)`

### CountRows

- **Kind:** power-fx-function
- **Purpose:** Count all records.
- **Example shape:** `=CountRows(...)`

### Distinct

- **Kind:** power-fx-function
- **Purpose:** Unique records from a table.
- **Example shape:** `=Distinct(...)`

### DropColumns

- **Kind:** power-fx-function
- **Purpose:** Table without the named columns.
- **Example shape:** `=DropColumns(...)`

### Filter

- **Kind:** power-fx-function
- **Purpose:** Rows that match one or more conditions.
- **Example shape:** `=Filter(...)`

### First

- **Kind:** power-fx-function
- **Purpose:** First record.
- **Example shape:** `=First(...)`

### FirstN

- **Kind:** power-fx-function
- **Purpose:** First N records.
- **Example shape:** `=FirstN(...)`

### ForAll

- **Kind:** power-fx-function
- **Purpose:** Evaluate a formula for every record.
- **Example shape:** `=ForAll(...)`

### Index

- **Kind:** power-fx-function
- **Purpose:** Record at a 1-based position.
- **Example shape:** `=Index(...)`

### Last

- **Kind:** power-fx-function
- **Purpose:** Last record.
- **Example shape:** `=Last(...)`

### LastN

- **Kind:** power-fx-function
- **Purpose:** Last N records.
- **Example shape:** `=LastN(...)`

### LookUp

- **Kind:** power-fx-function
- **Purpose:** First record that matches a condition.
- **Example shape:** `=LookUp(...)`

### Patch

- **Kind:** power-fx-function
- **Purpose:** Create or merge records.
- **Example shape:** `=Patch(...)`

### Remove

- **Kind:** power-fx-function
- **Purpose:** Delete specific records from a source.
- **Example shape:** `=Remove(...)`

### RenameColumns

- **Kind:** power-fx-function
- **Purpose:** Rename one or more columns.
- **Example shape:** `=RenameColumns(...)`

### Search

- **Kind:** power-fx-function
- **Purpose:** Rows whose selected columns contain a string.
- **Example shape:** `=Search(...)`

### Sequence

- **Kind:** power-fx-function
- **Purpose:** Table of sequential numbers.
- **Example shape:** `=Sequence(...)`

### ShowColumns

- **Kind:** power-fx-function
- **Purpose:** Keep only the named columns.
- **Example shape:** `=ShowColumns(...)`

### Shuffle

- **Kind:** power-fx-function
- **Purpose:** Randomize record order.
- **Example shape:** `=Shuffle(...)`

### Sort

- **Kind:** power-fx-function
- **Purpose:** Sort records by a formula.
- **Example shape:** `=Sort(...)`

### SortByColumns

- **Kind:** power-fx-function
- **Purpose:** Sort records by column names.
- **Example shape:** `=SortByColumns(...)`

### Summarize

- **Kind:** power-fx-function
- **Purpose:** Group rows and aggregate the rest.
- **Example shape:** `=Summarize(...)`

### Table

- **Kind:** power-fx-function
- **Purpose:** Build a temporary table from records.
- **Example shape:** `=Table(...)`


## Text

### Char

- **Kind:** power-fx-function
- **Purpose:** Character for a numeric code.
- **Example shape:** `=Char(...)`

### Concat

- **Kind:** power-fx-function
- **Purpose:** Join strings produced from a table.
- **Example shape:** `=Concat(...)`

### Concatenate

- **Kind:** power-fx-function
- **Purpose:** Join two or more strings.
- **Example shape:** `=Concatenate(...)`

### EncodeHTML

- **Kind:** power-fx-function
- **Purpose:** Escape characters for HTML.
- **Example shape:** `=EncodeHTML(...)`

### EncodeUrl

- **Kind:** power-fx-function
- **Purpose:** Percent-encode a URL fragment.
- **Example shape:** `=EncodeUrl(...)`

### EndsWith

- **Kind:** power-fx-function
- **Purpose:** True when a string ends with another string.
- **Example shape:** `=EndsWith(...)`

### Find

- **Kind:** power-fx-function
- **Purpose:** Start position of one string inside another.
- **Example shape:** `=Find(...)`

### Left

- **Kind:** power-fx-function
- **Purpose:** Leftmost characters of a string.
- **Example shape:** `=Left(...)`

### Len

- **Kind:** power-fx-function
- **Purpose:** Character length.
- **Example shape:** `=Len(...)`

### Lower

- **Kind:** power-fx-function
- **Purpose:** Lowercase letters.
- **Example shape:** `=Lower(...)`

### Mid

- **Kind:** power-fx-function
- **Purpose:** Substring from a start position.
- **Example shape:** `=Mid(...)`

### PlainText

- **Kind:** power-fx-function
- **Purpose:** Strip HTML/XML tags.
- **Example shape:** `=PlainText(...)`

### Proper

- **Kind:** power-fx-function
- **Purpose:** Capitalize the first letter of each word.
- **Example shape:** `=Proper(...)`

### Replace

- **Kind:** power-fx-function
- **Purpose:** Overwrite characters by start position.
- **Example shape:** `=Replace(...)`

### Right

- **Kind:** power-fx-function
- **Purpose:** Rightmost characters of a string.
- **Example shape:** `=Right(...)`

### Split

- **Kind:** power-fx-function
- **Purpose:** Break a string into a table of pieces.
- **Example shape:** `=Split(...)`

### StartsWith

- **Kind:** power-fx-function
- **Purpose:** True when a string begins with another string.
- **Example shape:** `=StartsWith(...)`

### Substitute

- **Kind:** power-fx-function
- **Purpose:** Replace matching substrings.
- **Example shape:** `=Substitute(...)`

### Trim

- **Kind:** power-fx-function
- **Purpose:** Collapse extra interior and edge spaces.
- **Example shape:** `=Trim(...)`

### TrimEnds

- **Kind:** power-fx-function
- **Purpose:** Strip leading and trailing spaces only.
- **Example shape:** `=TrimEnds(...)`

### UniChar

- **Kind:** power-fx-function
- **Purpose:** Character for a Unicode code point.
- **Example shape:** `=UniChar(...)`

### Upper

- **Kind:** power-fx-function
- **Purpose:** Uppercase letters.
- **Example shape:** `=Upper(...)`


## Utility

### Blank

- **Kind:** power-fx-function
- **Purpose:** A blank/null value for data sources.
- **Example shape:** `=Blank(...)`

### Coalesce

- **Kind:** power-fx-function
- **Purpose:** First non-blank argument.
- **Example shape:** `=Coalesce(...)`

### GUID

- **Kind:** power-fx-function
- **Purpose:** Parse or create a GUID.
- **Example shape:** `=GUID(...)`

### Language

- **Kind:** power-fx-function
- **Purpose:** Language tag of the current user.
- **Example shape:** `=Language(...)`

### Set

- **Kind:** power-fx-function
- **Purpose:** Assign a global; limited support in PAD.
- **Example shape:** `=Set(...)`

### With

- **Kind:** power-fx-function
- **Purpose:** Evaluate a formula against a named record.
- **Example shape:** `=With(...)`

