# Text

Parse, split, join, convert, and transform text values.

- Actions in this module: **19**
- Official docs: [Text actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text)

## Actions

### Append line to text

Appends a new line of text to a text value.

Designer name: **Append line to text**. Official reference: [Text / Append line to text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#appendline).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Original text | Required | Text value | — |
| Line to append | Optional | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| Result | Text value |

No module-specific exceptions are listed for this action.

---

### Get subtext

Retrieve a subtext from a text value.

Designer name: **Get subtext**. Official reference: [Text / Get subtext](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#getsubtextbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Original text | Required | Text value | — |
| Start index | Choice | Start of text, Character position | Character position |
| Character position | Required | Numeric value | — |
| Length | Choice | End of text, Number of chars | Number of chars |
| Number of chars | Required | Numeric value | — |

**Outputs**

| Variable | Type |
|---|---|
| Subtext | Text value |

**On error:** `Start index or length are out of range`.

---

### Crop text

Returns a text value that occurs before, after or between the specified text flag(s) in a given text.

Designer name: **Crop text**. Official reference: [Text / Crop text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#croptextaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Original text | Required | Text value | — |
| Mode | Choice | Get text before the specified flag, Get text after the specified flag, Get text between the two specified flags | Get text before the specified flag |
| Start flag | Required | Text value | — |
| End flag | Required | Text value | — |
| Ignore case | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| CroppedText | Text value |
| IsFlagFound | Boolean value |

No module-specific exceptions are listed for this action.

---

### Pad text

Creates a fixed length text by adding characters to the left or to the right of an existing text.

Designer name: **Pad text**. Official reference: [Text / Pad text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#pad).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Text to pad | Optional | Text value | — |
| Pad | Choice | Left, Right | Left |
| Text for padding | Optional | Text value | — |
| Total length | Optional | Numeric value | 10 |

**Outputs**

| Variable | Type |
|---|---|
| PaddedText | Text value |

No module-specific exceptions are listed for this action.

---

### Trim text

Removes all occurrences of white space characters (such as space, tab, or new line) from the beginning and/or end of an existing text.

Designer name: **Trim text**. Official reference: [Text / Trim text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#trim).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Text to trim | Optional | Text value | — |
| What to trim | Choice | whitespace characters from the beginning, whitespace characters from the end, whitespace characters from the beginning and end | whitespace characters from the beginning and end |

**Outputs**

| Variable | Type |
|---|---|
| TrimmedText | Text value |

No module-specific exceptions are listed for this action.

---

### Reverse text

Reverses the order of letters in a text string.

Designer name: **Reverse text**. Official reference: [Text / Reverse text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#reverse).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Text to reverse | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| ReversedText | Text value |

No module-specific exceptions are listed for this action.

---

### Change text case

Changes the casing of a text to uppercase, lowercase, title case or sentence case.

Designer name: **Change text case**. Official reference: [Text / Change text case](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#changecase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Text to convert | Optional | Text value | — |
| Convert to | Choice | Upper case, Lower case, Title case, Sentence case | Upper case |

**Outputs**

| Variable | Type |
|---|---|
| TextWithNewCase | Text value |

No module-specific exceptions are listed for this action.

---

### Convert text to number

Converts a text representation of a number to a variable that contains a numeric value.

Designer name: **Convert text to number**. Official reference: [Text / Convert text to number](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#tonumber).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Text to convert | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| TextAsNumber | Numeric value |

**On error:** `Provided text value can't be converted into a valid number`.

---

### Convert number to text

Converts a number to text using a specified format.

Designer name: **Convert number to text**. Official reference: [Text / Convert number to text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#fromnumber).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Number to convert | Required | Numeric value | — |
| Decimal places | Optional | Numeric value | 2 |
| Use thousands separator | Choice | Boolean value | True |

**Outputs**

| Variable | Type |
|---|---|
| FormattedNumber | Text value |

No module-specific exceptions are listed for this action.

---

### Convert text to datetime

Converts a text representation of a date and/or time value to a datetime value.

Designer name: **Convert text to datetime**. Official reference: [Text / Convert text to datetime](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#converttexttodatetime).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Text to convert | Required | Text value | — |
| Date is represented in custom format | Choice | Boolean value | False |
| Custom format | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| TextAsDateTime | Datetime |

**On error:** `Provided text value can't be converted into a valid datetime`.

---

### Convert datetime to text

Converts a datetime value to text using a specified custom format.

Designer name: **Convert datetime to text**. Official reference: [Text / Convert datetime to text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#convertdatetimetotext).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Datetime to convert | Required | Datetime | — |
| Format to use | Choice | Standard, Custom | Standard |
| Custom Format | Required | Text value | — |
| Standard format | Choice | Short date, Long date, Short time, Long time, Full datetime (short time), Full datetime (long time), General datetime (short time), General datetime (long time), Sortable datetime | Short date |

**Outputs**

| Variable | Type |
|---|---|
| FormattedDateTime | Text value |

No module-specific exceptions are listed for this action.

---

### Create random text

Generates a text of specified length consisting of random characters.

Designer name: **Create random text**. Official reference: [Text / Create random text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#random).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Use uppercase letters (A-Z) | Choice | Boolean value | True |
| Use lowercase letters (a-z) | Choice | Boolean value | True |
| Use digits (0-9) | Choice | Boolean value | True |
| Use symbols ( , . ? ! + - _ # $ ^ ) | Choice | Boolean value | True |
| Minimum length | Optional | Numeric value | 6 |
| Maximum length | Optional | Numeric value | 10 |

**Outputs**

| Variable | Type |
|---|---|
| RandomText | Text value |

No module-specific exceptions are listed for this action.

---

### Join text

Converts a list into a text value by separating its items with a specified delimiter.

Designer name: **Join text**. Official reference: [Text / Join text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#jointext).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Specify the list to join | Required | List of Text values | — |
| Delimiter to separate list items | Choice | None, Standard, Custom | None |
| Custom delimiter | Required | Text value | — |
| Standard delimiter | Choice | Space, Tab, New line | Space |
| Times | Optional | Numeric value | 1 |

**Outputs**

| Variable | Type |
|---|---|
| JoinedText | Text value |

No module-specific exceptions are listed for this action.

---

### Split text

Creates a list containing the substrings of a text that are separated by a specified delimiter or a regular expression.

Designer name: **Split text**. Official reference: [Text / Split text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#splittext).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| The text to split | Required | Text value | — |
| Delimiter type | Choice | Standard, Custom | Standard |
| Custom delimiter | Required | Text value | — |
| Standard delimiter | Choice | Space, Tab, New line | Space |
| Times | Optional | Numeric value | 1 |
| Is regular expression | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| TextList | List of Text values |

**On error:** `Provided regular expression is invalid`.

---

### Parse text

Parses a text to find the first or all occurrences of a specified subtext or a regular expression pattern.

Designer name: **Parse text**. Official reference: [Text / Parse text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#parsetext).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Text to Parse | Required | Text value | — |
| Text to Find | Required | Text value | — |
| Is regular expression | Choice | Boolean value | False |
| Start Parsing at Position | Required | Numeric value | — |
| First occurrence only | Choice | Boolean value | True |
| Ignore case | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| Position | Numeric value |
| Positions | List of Numeric values |
| Match | Text value |
| Matches | List of Text values |

**On error:** `Provided regular expression is invalid`.

---

### Replace text

Replaces all occurrences of a specified subtext with another text.

Designer name: **Replace text**. Official reference: [Text / Replace text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#replace).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Text to parse | Required | Text value | — |
| Text to find | Required | Text value | — |
| Use regular expressions for find and replace | Choice | Boolean value | False |
| Ignore case | Choice | Boolean value | False |
| Replace with | Required | Text value | — |
| Activate escape sequences | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| Replaced | Text value |

No module-specific exceptions are listed for this action.

---

### Escape text for regular expression

Escapes a minimal set of characters (\, *, +, ?, |, {, [, (,), ^, $,., #, and white space) by replacing them with their escape codes.

Designer name: **Escape text for regular expression**. Official reference: [Text / Escape text for regular expression](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#escapeforregularexpression).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Text to escape | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| EscapedText | Text value |

No module-specific exceptions are listed for this action.

---

### Recognize entities in text

Recognizes entities in text, such as numbers, units, data/time and others expressed in natural language across multiple languages.

Designer name: **Recognize entities in text**. Official reference: [Text / Recognize entities in text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#recognizeentitiesintext).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Text to recognize from | Required | Text value | — |
| Entity type | Choice | Date time, Dimension, Temperature, Currency, Number range, Number, Ordinal, Percentage, Phone number, Email, IP address, Mention, Hashtag, URL, GUID, Quoted text | Date time |
| Language | Choice | English, Chinese (Simplified), Spanish, Spanish (Mexico), Portuguese, French, German, Italian, Japanese, Dutch, Korean, Swedish, Turkish, Hindi | English |

**Outputs**

| Variable | Type |
|---|---|
| RecognizedEntities | Datatable |

No module-specific exceptions are listed for this action.

---

### Create HTML content

Generates rich HTML content and stores it in a variable.

Designer name: **Create HTML content**. Official reference: [Text / Create HTML content](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#createhtmlcontentaction).

This action has no input parameters.

**Outputs**

| Variable | Type |
|---|---|
| HtmlContent | Text value |

No module-specific exceptions are listed for this action.

---
