# Text — how each function works

Native Actions pane module **Text**.

19 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Append line to text

- **Id:** `text/append-line-to-text`
- **Kind:** native-action
- **Purpose:** Appends a new line of text to a text value.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Append line to text** on the canvas. Appends a new line of text to a text value.

**Demonstration.**

```text
**Append line to text**
- Original text: `INV-1042`
- Line to append: `INV-1042`
Produces:
- `%Result%` (Text value)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Change text case

- **Id:** `text/change-text-case`
- **Kind:** native-action
- **Purpose:** Changes the casing of a text to uppercase, lowercase, title case or sentence case.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Change text case** on the canvas. Changes the casing of a text to uppercase, lowercase, title case or sentence case.

**Demonstration.**

```text
**Change text case**
- Text to convert: `INV-1042`
- Convert to: `Upper case`
Produces:
- `%TextWithNewCase%` (Text value)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Convert datetime to text

- **Id:** `text/convert-datetime-to-text`
- **Kind:** native-action
- **Purpose:** Converts datetime to text.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Convert datetime to text** on the canvas. Converts datetime to text.

**Demonstration.**

```text
**Convert datetime to text**
- Datetime to convert: `(set in designer)`
- Format to use: `Standard`
- Custom Format: `INV-1042`
- Standard format: `Short date`
Produces:
- `%FormattedDateTime%` (Text value)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Convert number to text

- **Id:** `text/convert-number-to-text`
- **Kind:** native-action
- **Purpose:** Converts number to text.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Convert number to text** on the canvas. Converts number to text.

**Demonstration.**

```text
**Convert number to text**
- Number to convert: `1`
- Decimal places: `2`
- Use thousands separator: `True`
Produces:
- `%FormattedNumber%` (Text value)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Convert text to datetime

- **Id:** `text/convert-text-to-datetime`
- **Kind:** native-action
- **Purpose:** Converts text to datetime.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Convert text to datetime** on the canvas. Converts text to datetime.

**Demonstration.**

```text
**Convert text to datetime**
- Text to convert: `INV-1042`
- Date is represented in custom format: `False`
- Custom format: `INV-1042`
Produces:
- `%TextAsDateTime%` (Datetime)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Convert text to number

- **Id:** `text/convert-text-to-number`
- **Kind:** native-action
- **Purpose:** Converts text to number.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Convert text to number** on the canvas. Converts text to number.

**Demonstration.**

```text
**Convert text to number**
- Text to convert: `INV-1042`
Produces:
- `%TextAsNumber%` (Numeric value)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Create HTML content

- **Id:** `text/create-html-content`
- **Kind:** native-action
- **Purpose:** Creates HTML content.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Create HTML content** on the canvas. Creates HTML content.

**Demonstration.**

```text
**Create HTML content**
- (no inputs)
Produces:
- `%`HtmlContent`%` (Text value)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Create random text

- **Id:** `text/create-random-text`
- **Kind:** native-action
- **Purpose:** Creates random text.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Create random text** on the canvas. Creates random text.

**Demonstration.**

```text
**Create random text**
- Use uppercase letters (A-Z): `True`
- Use lowercase letters (a-z): `True`
- Use digits (0-9): `True`
- Use symbols ( , . ? ! + - _ # $ ^ ): `True`
- Minimum length: `6`
- Maximum length: `10`
Produces:
- `%RandomText%` (Text value)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Crop text

- **Id:** `text/crop-text`
- **Kind:** native-action
- **Purpose:** Retrieves a text value that occurs before, after or between the specified text flag(s) in a given text.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Crop text** on the canvas. Retrieves a text value that occurs before, after or between the specified text flag(s) in a given text.

**Demonstration.**

```text
**Crop text**
- Original text: `INV-1042`
- Mode: `Get text before the specified flag`
- Start flag: `INV-1042`
- End flag: `INV-1042`
- Ignore case: `False`
Produces:
- `%CroppedText%` (Text value)
- `%IsFlagFound%` (Boolean value)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Escape text for regular expression

- **Id:** `text/escape-text-for-regular-expression`
- **Kind:** native-action
- **Purpose:** Escapes a minimal set of characters (\, *, +, ?, |, {, , (,), ^, $,., #, and white space) by replacing them with their escape codes.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Escape text for regular expression** on the canvas. Escapes a minimal set of characters (\, *, +, ?, |, {, , (,), ^, $,., #, and white space) by replacing them with their escape codes.

**Demonstration.**

```text
**Escape text for regular expression**
- Text to escape: `INV-1042`
Produces:
- `%EscapedText%` (Text value)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Get subtext

- **Id:** `text/get-subtext`
- **Kind:** native-action
- **Purpose:** Reads subtext into a flow variable.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Get subtext** on the canvas. Reads subtext into a flow variable.

**Demonstration.**

```text
**Get subtext**
- Original text: `INV-1042`
- Start index: `Character position`
- Character position: `1`
- Length: `Number of chars`
- Number of chars: `1`
Produces:
- `%Subtext%` (Text value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Join text

- **Id:** `text/join-text`
- **Kind:** native-action
- **Purpose:** Joins text.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Join text** on the canvas. Joins text.

**Demonstration.**

```text
**Join text**
- Specify the list to join: `%Files%`
- Delimiter to separate list items: `None`
- Custom delimiter: `INV-1042`
- Standard delimiter: `Space`
- Times: `1`
Produces:
- `%JoinedText%` (Text value)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Pad text

- **Id:** `text/pad-text`
- **Kind:** native-action
- **Purpose:** Pads text.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Pad text** on the canvas. Pads text.

**Demonstration.**

```text
**Pad text**
- Text to pad: `INV-1042`
- Pad: `Left`
- Text for padding: `INV-1042`
- Total length: `10`
Produces:
- `%PaddedText%` (Text value)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Parse text

- **Id:** `text/parse-text`
- **Kind:** native-action
- **Purpose:** Parses text.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Parse text** on the canvas. Parses text.

**Demonstration.**

```text
**Parse text**
- Text to Parse: `INV-1042`
- Text to Find: `INV-1042`
- Is regular expression: `False`
- Start Parsing at Position: `1`
- First occurrence only: `True`
- Ignore case: `False`
Produces:
- `%Position%` (Numeric value)
- `%Positions%` (List of Numeric values)
- `%Match%` (Text value)
- `%Matches%` (List of Text values)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Recognize entities in text

- **Id:** `text/recognize-entities-in-text`
- **Kind:** native-action
- **Purpose:** Recognizes entities in text, such as numbers, units, data/time and others expressed in natural language across multiple languages.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Recognize entities in text** on the canvas. Recognizes entities in text, such as numbers, units, data/time and others expressed in natural language across multiple languages.

**Demonstration.**

```text
**Recognize entities in text**
- Text to recognize from: `INV-1042`
- Entity type: `Date time`
- Language: `English`
Produces:
- `%RecognizedEntities%` (Datatable)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Replace text

- **Id:** `text/replace-text`
- **Kind:** native-action
- **Purpose:** Replaces text.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Replace text** on the canvas. Replaces text.

**Demonstration.**

```text
**Replace text**
- Text to parse: `INV-1042`
- Text to find: `INV-1042`
- Use regular expressions for find and replace: `False`
- Ignore case: `False`
- Replace with: `INV-1042`
- Activate escape sequences: `False`
Produces:
- `%Replaced%` (Text value)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Reverse text

- **Id:** `text/reverse-text`
- **Kind:** native-action
- **Purpose:** Reverses the order of letters in a text string.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Reverse text** on the canvas. Reverses the order of letters in a text string.

**Demonstration.**

```text
**Reverse text**
- Text to reverse: `INV-1042`
Produces:
- `%ReversedText%` (Text value)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Split text

- **Id:** `text/split-text`
- **Kind:** native-action
- **Purpose:** Splits text.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Split text** on the canvas. Splits text.

**Demonstration.**

```text
**Split text**
- The text to split: `INV-1042`
- Delimiter type: `Standard`
- Custom delimiter: `INV-1042`
- Standard delimiter: `Space`
- Times: `1`
- Is regular expression: `False`
Produces:
- `%TextList%` (List of Text values)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.

### Trim text

- **Id:** `text/trim-text`
- **Kind:** native-action
- **Purpose:** Trims text.

**Use case.** In cleaning a filename, invoice number, or CSV line, drop **Trim text** on the canvas. Trims text.

**Demonstration.**

```text
**Trim text**
- Text to trim: `INV-1042`
- What to trim: `whitespace characters from the beginning and end`
Produces:
- `%TrimmedText%` (Text value)
```

**Analogy.** One tool in that kit: scissors, tape, and a stamp for words.

**In combination.** Parse/Replace/Split/Join text before writing to Excel or a file.
