# Text

Join, split, parse, replace, convert, and generate text values.

This page documents every **native action** in this group (19 items).

## Actions

### Append line to text

- **Inventory id:** `text/append-line-to-text`
- **Kind:** native-action
- **Purpose:** Appends a new line of text to a text value.
- **Key inputs:** `Original text` (Text value); `Line to append` (Text value; optional)
- **Produces:** `Result` (Text value)
- **Exceptions:** none listed
- **Microsoft Learn:** [Append line to text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#appendline)

### Change text case

- **Inventory id:** `text/change-text-case`
- **Kind:** native-action
- **Purpose:** Changes the casing of a text to uppercase, lowercase, title case or sentence case.
- **Key inputs:** `Text to convert` (Text value; optional); `Convert to` (Upper case, Lower case, Title case, Sentence case)
- **Produces:** `TextWithNewCase` (Text value)
- **Exceptions:** none listed
- **Microsoft Learn:** [Change text case](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#changecase)

### Convert datetime to text

- **Inventory id:** `text/convert-datetime-to-text`
- **Kind:** native-action
- **Purpose:** Converts datetime to text.
- **Key inputs:** `Datetime to convert` (Datetime); `Format to use` (Standard, Custom); `Custom Format` (Text value); `Standard format` (Short date, Long date, Short time, Long time, Full datetime (short time), Full datetime (long time), General datetime (short time), General datetime (long time), Sortable datetime)
- **Produces:** `FormattedDateTime` (Text value)
- **Exceptions:** none listed
- **Microsoft Learn:** [Convert datetime to text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#convertdatetimetotext)

### Convert number to text

- **Inventory id:** `text/convert-number-to-text`
- **Kind:** native-action
- **Purpose:** Converts number to text.
- **Key inputs:** `Number to convert` (Numeric value); `Decimal places` (Numeric value; optional); `Use thousands separator` (Boolean value)
- **Produces:** `FormattedNumber` (Text value)
- **Exceptions:** none listed
- **Microsoft Learn:** [Convert number to text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#fromnumber)

### Convert text to datetime

- **Inventory id:** `text/convert-text-to-datetime`
- **Kind:** native-action
- **Purpose:** Converts text to datetime.
- **Key inputs:** `Text to convert` (Text value); `Date is represented in custom format` (Boolean value); `Custom format` (Text value)
- **Produces:** `TextAsDateTime` (Datetime)
- **Exceptions:** `Provided text value can't be converted into a valid datetime`
- **Microsoft Learn:** [Convert text to datetime](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#converttexttodatetime)

### Convert text to number

- **Inventory id:** `text/convert-text-to-number`
- **Kind:** native-action
- **Purpose:** Converts text to number.
- **Key inputs:** `Text to convert` (Text value)
- **Produces:** `TextAsNumber` (Numeric value)
- **Exceptions:** `Provided text value can't be converted into a valid number`
- **Microsoft Learn:** [Convert text to number](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#tonumber)

### Create HTML content

- **Inventory id:** `text/create-html-content`
- **Kind:** native-action
- **Purpose:** Creates HTML content.
- **Key inputs:** None
- **Produces:** ``HtmlContent`` (Text value)
- **Exceptions:** none listed
- **Microsoft Learn:** [Create HTML content](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#createhtmlcontentaction)

### Create random text

- **Inventory id:** `text/create-random-text`
- **Kind:** native-action
- **Purpose:** Creates random text.
- **Key inputs:** `Use uppercase letters (A-Z)` (Boolean value); `Use lowercase letters (a-z)` (Boolean value); `Use digits (0-9)` (Boolean value); `Use symbols ( , . ? ! + - _ # $ ^ )` (Boolean value); `Minimum length` (Numeric value; optional); `Maximum length` (Numeric value; optional)
- **Produces:** `RandomText` (Text value)
- **Exceptions:** none listed
- **Microsoft Learn:** [Create random text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#random)

### Crop text

- **Inventory id:** `text/crop-text`
- **Kind:** native-action
- **Purpose:** Retrieves a text value that occurs before, after or between the specified text flag(s) in a given text.
- **Key inputs:** `Original text` (Text value); `Mode` (Get text before the specified flag, Get text after the specified flag, Get text between the two specified flags); `Start flag` (Text value); `End flag` (Text value); `Ignore case` (Boolean value)
- **Produces:** `CroppedText` (Text value); `IsFlagFound` (Boolean value)
- **Exceptions:** none listed
- **Microsoft Learn:** [Crop text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#croptextaction)

### Escape text for regular expression

- **Inventory id:** `text/escape-text-for-regular-expression`
- **Kind:** native-action
- **Purpose:** Escapes a minimal set of characters (\, *, +, ?, |, {, , (,), ^, $,., #, and white space) by replacing them with their escape codes.
- **Key inputs:** `Text to escape` (Text value)
- **Produces:** `EscapedText` (Text value)
- **Exceptions:** none listed
- **Microsoft Learn:** [Escape text for regular expression](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#escapeforregularexpression)

### Get subtext

- **Inventory id:** `text/get-subtext`
- **Kind:** native-action
- **Purpose:** Reads subtext into a flow variable.
- **Key inputs:** `Original text` (Text value); `Start index` (Start of text, Character position); `Character position` (Numeric value); `Length` (End of text, Number of chars); `Number of chars` (Numeric value)
- **Produces:** `Subtext` (Text value)
- **Exceptions:** `Start index or length are out of range`
- **Microsoft Learn:** [Get subtext](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#getsubtextbase)

### Join text

- **Inventory id:** `text/join-text`
- **Kind:** native-action
- **Purpose:** Joins text.
- **Key inputs:** `Specify the list to join` (List of Text values); `Delimiter to separate list items` (None, Standard, Custom); `Custom delimiter` (Text value); `Standard delimiter` (Space, Tab, New line); `Times` (Numeric value; optional)
- **Produces:** `JoinedText` (Text value)
- **Exceptions:** none listed
- **Microsoft Learn:** [Join text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#jointext)

### Pad text

- **Inventory id:** `text/pad-text`
- **Kind:** native-action
- **Purpose:** Pads text.
- **Key inputs:** `Text to pad` (Text value; optional); `Pad` (Left, Right); `Text for padding` (Text value; optional); `Total length` (Numeric value; optional)
- **Produces:** `PaddedText` (Text value)
- **Exceptions:** none listed
- **Microsoft Learn:** [Pad text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#pad)

### Parse text

- **Inventory id:** `text/parse-text`
- **Kind:** native-action
- **Purpose:** Parses text.
- **Key inputs:** `Text to Parse` (Text value); `Text to Find` (Text value); `Is regular expression` (Boolean value); `Start Parsing at Position` (Numeric value); `First occurrence only` (Boolean value); `Ignore case` (Boolean value)
- **Produces:** `Position` (Numeric value); `Positions` (List of Numeric values); `Match` (Text value); `Matches` (List of Text values)
- **Exceptions:** `Provided regular expression is invalid`
- **Microsoft Learn:** [Parse text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#parsetext)

### Recognize entities in text

- **Inventory id:** `text/recognize-entities-in-text`
- **Kind:** native-action
- **Purpose:** Recognizes entities in text, such as numbers, units, data/time and others expressed in natural language across multiple languages.
- **Key inputs:** `Text to recognize from` (Text value); `Entity type` (Date time, Dimension, Temperature, Currency, Number range, Number, Ordinal, Percentage, Phone number, Email, IP address, Mention, Hashtag, URL, GUID, Quoted text); `Language` (English, Chinese (Simplified), Spanish, Spanish (Mexico), Portuguese, French, German, Italian, Japanese, Dutch, Korean, Swedish, Turkish, Hindi)
- **Produces:** `RecognizedEntities` (Datatable)
- **Exceptions:** none listed
- **Microsoft Learn:** [Recognize entities in text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#recognizeentitiesintext)

### Replace text

- **Inventory id:** `text/replace-text`
- **Kind:** native-action
- **Purpose:** Replaces text.
- **Key inputs:** `Text to parse` (Text value); `Text to find` (Text value); `Use regular expressions for find and replace` (Boolean value); `Ignore case` (Boolean value); `Replace with` (Text value); `Activate escape sequences` (Boolean value)
- **Produces:** `Replaced` (Text value)
- **Exceptions:** none listed
- **Microsoft Learn:** [Replace text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#replace)

### Reverse text

- **Inventory id:** `text/reverse-text`
- **Kind:** native-action
- **Purpose:** Reverses the order of letters in a text string.
- **Key inputs:** `Text to reverse` (Text value)
- **Produces:** `ReversedText` (Text value)
- **Exceptions:** none listed
- **Microsoft Learn:** [Reverse text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#reverse)

### Split text

- **Inventory id:** `text/split-text`
- **Kind:** native-action
- **Purpose:** Splits text.
- **Key inputs:** `The text to split` (Text value); `Delimiter type` (Standard, Custom); `Custom delimiter` (Text value); `Standard delimiter` (Space, Tab, New line); `Times` (Numeric value; optional); `Is regular expression` (Boolean value)
- **Produces:** `TextList` (List of Text values)
- **Exceptions:** `Provided regular expression is invalid`
- **Microsoft Learn:** [Split text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#splittext)

### Trim text

- **Inventory id:** `text/trim-text`
- **Kind:** native-action
- **Purpose:** Trims text.
- **Key inputs:** `Text to trim` (Text value; optional); `What to trim` (whitespace characters from the beginning, whitespace characters from the end, whitespace characters from the beginning and end)
- **Produces:** `TrimmedText` (Text value)
- **Exceptions:** none listed
- **Microsoft Learn:** [Trim text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/text#trim)
