# XML

Read, query, and edit XML documents and nodes.

- Actions in this module: **10**
- Official docs: [XML actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml)

## Actions

### Read XML from file

Read the contents of an XML file into a variable.

Designer name: **Read XML from file**. Official reference: [XML / Read XML from file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#readfromfile).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| File path | Required | File | — |
| Encoding | Choice | System default, ASCII, Unicode, Unicode big endian, UTF-8 | System default |

**Outputs**

| Variable | Type |
|---|---|
| XmlDocument | XML node |

**On error:** `Directory not found`, `File not found`, `Failed to read from file`, `File doesn't contain a valid XML document`.

---

### Write XML to file

Write the contents of an XML node variable into a file.

Designer name: **Write XML to file**. Official reference: [XML / Write XML to file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#writexmltofile).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| File path | Required | File | — |
| XML to write | Required | Text value | — |
| Encoding | Choice | System default, ASCII, Unicode, Unicode big endian, UTF-8 | System default |
| Format XML | Choice | Boolean value | True |
| Indentation per level | Optional | Numeric value | 2 |

Produces no variables.

**On error:** `Invalid directory specified`, `Failed to write XML to file`.

---

### Execute XPath expression

Extract values from an XML document based on the provided XPath query.

Designer name: **Execute XPath expression**. Official reference: [XML / Execute XPath expression](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#executexpathquery).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| XML document to parse | Required | Text value | — |
| XPath query | Required | Text value | — |
| Get first value only | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| XPathResult | XML node |
| XPathResults | List of XML nodes |

**On error:** `Invalid XML document provided`, `Invalid XPath expression provided`.

---

### Get XML element attribute

Reads the value of an attribute of an XML element.

Designer name: **Get XML element attribute**. Official reference: [XML / Get XML element attribute](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#getxmlelementattribute).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| XML document | Required | XML node | — |
| XPath query | Optional | Text value | — |
| Attribute name | Required | Text value | — |
| Get value as | Choice | Text value, Numeric value, Datetime value, Boolean value | Text value |

**Outputs**

| Variable | Type |
|---|---|
| XmlAttributeValue | Boolean value |
| XmlAttributeValue | Datetime |
| XmlAttributeValue | Numeric value |
| XmlAttributeValue | Text value |

**On error:** `Invalid XPath expression provided`, `XPath expression returns no element`, `Attribute not found in element`, `Failed to convert attribute value to the requested data type`.

---

### Set XML element attribute

Writes the value of an attribute of an XML element.

Designer name: **Set XML element attribute**. Official reference: [XML / Set XML element attribute](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#setelementattribute).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| XML document | Required | XML node | — |
| XPath query | Optional | Text value | — |
| Attribute name | Required | Text value | — |
| Attribute value | Required | Text value | — |

Produces no variables.

**On error:** `Invalid XPath expression provided`, `XPath expression returns no element`, `Failed to set XML attribute`.

---

### Remove XML element attribute

Remove an attribute from an XML element.

Designer name: **Remove XML element attribute**. Official reference: [XML / Remove XML element attribute](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#removeelementattribute).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| XML document | Required | XML node | — |
| XPath query | Optional | Text value | — |
| Attribute name | Required | Text value | — |

Produces no variables.

**On error:** `Invalid XPath expression provided`, `XPath expression returns no element`, `Attribute not found in element`, `Failed to remove XML attribute`.

---

### Get XML element value

Reads the value of an XML element.

Designer name: **Get XML element value**. Official reference: [XML / Get XML element value](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#getxmlelementvalue).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| XML document | Required | XML node | — |
| XPath query | Optional | Text value | — |
| Get value as | Choice | Text value, Numeric value, Datetime value, Boolean value | Text value |

**Outputs**

| Variable | Type |
|---|---|
| XmlElementValue | Boolean value |
| XmlElementValue | Datetime |
| XmlElementValue | Numeric value |
| XmlElementValue | Text value |

**On error:** `Invalid XPath expression provided`, `XPath expression returns no element`, `Failed to convert element value to the requested data type`.

---

### Set XML element value

Writes the value of an XML element.

Designer name: **Set XML element value**. Official reference: [XML / Set XML element value](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#setelementvalue).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| XML document | Required | XML node | — |
| XPath query | Optional | Text value | — |
| XML element value | Required | Text value | — |

Produces no variables.

**On error:** `Invalid XPath expression provided`, `XPath expression returns no element`, `Failed to set element value`.

---

### Insert XML element

Insert a new XML element into an XML document.

Designer name: **Insert XML element**. Official reference: [XML / Insert XML element](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#insertelement).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| XML document | Required | XML node | — |
| XPath query | Required | Text value | — |
| XML element to insert | Required | XML node | — |

Produces no variables.

**On error:** `Invalid XPath expression provided`, `XPath expression returns no element`, `Failed to insert XML element`.

---

### Remove XML element

Remove one or more XML elements from an XML document.

Designer name: **Remove XML element**. Official reference: [XML / Remove XML element](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#removeelement).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| XML document | Required | XML node | — |
| XPath query | Required | Text value | — |

Produces no variables.

**On error:** `Invalid XPath expression provided`, `Failed to remove XML element`.

---
