# XML — how each function works

Native Actions pane module **XML**.

10 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Execute XPath expression

- **Id:** `xml/execute-xpath-expression`
- **Kind:** native-action
- **Purpose:** Extract values from an XML document based on the provided XPath query.

**Use case.** In a vendor XML invoice, drop **Execute XPath expression** on the canvas. Extract values from an XML document based on the provided XPath query.

**Demonstration.**

```text
**Execute XPath expression**
- XML document to parse: `INV-1042`
- XPath query: `C:\RPA\Invoices\INV-1042.pdf`
- Get first value only: `False`
Produces:
- `%XPathResult%` (XML node)
- `%XPathResults%` (List of XML nodes)
```

**Analogy.** One tool in that kit: a nested set of labeled folders you open with a map (XPath).

**In combination.** Read XML from file, Execute XPath expression, Write XML to file.

### Get XML element attribute

- **Id:** `xml/get-xml-element-attribute`
- **Kind:** native-action
- **Purpose:** Reads XML element attribute into a flow variable.

**Use case.** In a vendor XML invoice, drop **Get XML element attribute** on the canvas. Reads XML element attribute into a flow variable.

**Demonstration.**

```text
**Get XML element attribute**
- XML document: `%XmlDoc%`
- XPath query: `C:\RPA\Invoices\INV-1042.pdf`
- Attribute name: `INV-1042`
- Get value as: `Text value`
Produces:
- `%XmlAttributeValue%` (Boolean value)
- `%XmlAttributeValue%` (Datetime)
- `%XmlAttributeValue%` (Numeric value)
- `%XmlAttributeValue%` (Text value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Read XML from file, Execute XPath expression, Write XML to file.

### Get XML element value

- **Id:** `xml/get-xml-element-value`
- **Kind:** native-action
- **Purpose:** Reads XML element value into a flow variable.

**Use case.** In a vendor XML invoice, drop **Get XML element value** on the canvas. Reads XML element value into a flow variable.

**Demonstration.**

```text
**Get XML element value**
- XML document: `%XmlDoc%`
- XPath query: `C:\RPA\Invoices\INV-1042.pdf`
- Get value as: `Text value`
Produces:
- `%XmlElementValue%` (Boolean value)
- `%XmlElementValue%` (Datetime)
- `%XmlElementValue%` (Numeric value)
- `%XmlElementValue%` (Text value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Read XML from file, Execute XPath expression, Write XML to file.

### Insert XML element

- **Id:** `xml/insert-xml-element`
- **Kind:** native-action
- **Purpose:** Inserts XML element.

**Use case.** In a vendor XML invoice, drop **Insert XML element** on the canvas. Inserts XML element.

**Demonstration.**

```text
**Insert XML element**
- XML document: `%XmlDoc%`
- XPath query: `C:\RPA\Invoices\INV-1042.pdf`
- XML element to insert: `%XmlDoc%`
```

**Analogy.** One tool in that kit: a nested set of labeled folders you open with a map (XPath).

**In combination.** Read XML from file, Execute XPath expression, Write XML to file.

### Read XML from file

- **Id:** `xml/read-xml-from-file`
- **Kind:** native-action
- **Purpose:** Reads XML from file.

**Use case.** In a vendor XML invoice, drop **Read XML from file** on the canvas. Reads XML from file.

**Demonstration.**

```text
**Read XML from file**
- File path: `C:\RPA\Invoices\INV-1042.pdf`
- Encoding: `System default`
Produces:
- `%XmlDocument%` (XML node)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Read XML from file, Execute XPath expression, Write XML to file.

### Remove XML element

- **Id:** `xml/remove-xml-element`
- **Kind:** native-action
- **Purpose:** Removes XML element.

**Use case.** In a vendor XML invoice, drop **Remove XML element** on the canvas. Removes XML element.

**Demonstration.**

```text
**Remove XML element**
- XML document: `%XmlDoc%`
- XPath query: `C:\RPA\Invoices\INV-1042.pdf`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Read XML from file, Execute XPath expression, Write XML to file.

### Remove XML element attribute

- **Id:** `xml/remove-xml-element-attribute`
- **Kind:** native-action
- **Purpose:** Removes XML element attribute.

**Use case.** In a vendor XML invoice, drop **Remove XML element attribute** on the canvas. Removes XML element attribute.

**Demonstration.**

```text
**Remove XML element attribute**
- XML document: `%XmlDoc%`
- XPath query: `C:\RPA\Invoices\INV-1042.pdf`
- Attribute name: `INV-1042`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Read XML from file, Execute XPath expression, Write XML to file.

### Set XML element attribute

- **Id:** `xml/set-xml-element-attribute`
- **Kind:** native-action
- **Purpose:** Writes XML element attribute.

**Use case.** In a vendor XML invoice, drop **Set XML element attribute** on the canvas. Writes XML element attribute.

**Demonstration.**

```text
**Set XML element attribute**
- XML document: `%XmlDoc%`
- XPath query: `C:\RPA\Invoices\INV-1042.pdf`
- Attribute name: `INV-1042`
- Attribute value: `INV-1042`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Read XML from file, Execute XPath expression, Write XML to file.

### Set XML element value

- **Id:** `xml/set-xml-element-value`
- **Kind:** native-action
- **Purpose:** Writes XML element value.

**Use case.** In a vendor XML invoice, drop **Set XML element value** on the canvas. Writes XML element value.

**Demonstration.**

```text
**Set XML element value**
- XML document: `%XmlDoc%`
- XPath query: `C:\RPA\Invoices\INV-1042.pdf`
- XML element value: `INV-1042`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Read XML from file, Execute XPath expression, Write XML to file.

### Write XML to file

- **Id:** `xml/write-xml-to-file`
- **Kind:** native-action
- **Purpose:** Writes XML to file.

**Use case.** In a vendor XML invoice, drop **Write XML to file** on the canvas. Writes XML to file.

**Demonstration.**

```text
**Write XML to file**
- File path: `C:\RPA\Invoices\INV-1042.pdf`
- XML to write: `INV-1042`
- Encoding: `System default`
- Format XML: `True`
- Indentation per level: `2`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Read XML from file, Execute XPath expression, Write XML to file.
