# XML

Read XML, run XPath, and edit elements and attributes.

This page documents every **native action** in this group (10 items).

## Actions

### Execute XPath expression

- **Inventory id:** `xml/execute-xpath-expression`
- **Kind:** native-action
- **Purpose:** Extract values from an XML document based on the provided XPath query.
- **Key inputs:** `XML document to parse` (Text value); `XPath query` (Text value); `Get first value only` (Boolean value)
- **Produces:** `XPathResult` (XML node); `XPathResults` (List of XML nodes)
- **Exceptions:** `Invalid XML document provided`; `Invalid XPath expression provided`
- **Microsoft Learn:** [Execute XPath expression](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#executexpathquery)

### Get XML element attribute

- **Inventory id:** `xml/get-xml-element-attribute`
- **Kind:** native-action
- **Purpose:** Reads XML element attribute into a flow variable.
- **Key inputs:** `XML document` (XML node); `XPath query` (Text value; optional); `Attribute name` (Text value); `Get value as` (Text value, Numeric value, Datetime value, Boolean value)
- **Produces:** `XmlAttributeValue` (Boolean value); `XmlAttributeValue` (Datetime); `XmlAttributeValue` (Numeric value); `XmlAttributeValue` (Text value)
- **Exceptions:** `Invalid XPath expression provided`; `XPath expression returns no element`; `Attribute not found in element`; `Failed to convert attribute value to the requested data type`
- **Microsoft Learn:** [Get XML element attribute](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#getxmlelementattribute)

### Get XML element value

- **Inventory id:** `xml/get-xml-element-value`
- **Kind:** native-action
- **Purpose:** Reads XML element value into a flow variable.
- **Key inputs:** `XML document` (XML node); `XPath query` (Text value; optional); `Get value as` (Text value, Numeric value, Datetime value, Boolean value)
- **Produces:** `XmlElementValue` (Boolean value); `XmlElementValue` (Datetime); `XmlElementValue` (Numeric value); `XmlElementValue` (Text value)
- **Exceptions:** `Invalid XPath expression provided`; `XPath expression returns no element`; `Failed to convert element value to the requested data type`
- **Microsoft Learn:** [Get XML element value](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#getxmlelementvalue)

### Insert XML element

- **Inventory id:** `xml/insert-xml-element`
- **Kind:** native-action
- **Purpose:** Inserts XML element.
- **Key inputs:** `XML document` (XML node); `XPath query` (Text value); `XML element to insert` (XML node)
- **Produces:** None listed
- **Exceptions:** `Invalid XPath expression provided`; `XPath expression returns no element`; `Failed to insert XML element`
- **Microsoft Learn:** [Insert XML element](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#insertelement)

### Read XML from file

- **Inventory id:** `xml/read-xml-from-file`
- **Kind:** native-action
- **Purpose:** Reads XML from file.
- **Key inputs:** `File path` (File); `Encoding` (System default, ASCII, Unicode, Unicode big endian, UTF-8)
- **Produces:** `XmlDocument` (XML node)
- **Exceptions:** `Directory not found`; `File not found`; `Failed to read from file`; `File doesn't contain a valid XML document`
- **Microsoft Learn:** [Read XML from file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#readfromfile)

### Remove XML element

- **Inventory id:** `xml/remove-xml-element`
- **Kind:** native-action
- **Purpose:** Removes XML element.
- **Key inputs:** `XML document` (XML node); `XPath query` (Text value)
- **Produces:** None listed
- **Exceptions:** `Invalid XPath expression provided`; `Failed to remove XML element`
- **Microsoft Learn:** [Remove XML element](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#removeelement)

### Remove XML element attribute

- **Inventory id:** `xml/remove-xml-element-attribute`
- **Kind:** native-action
- **Purpose:** Removes XML element attribute.
- **Key inputs:** `XML document` (XML node); `XPath query` (Text value; optional); `Attribute name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Invalid XPath expression provided`; `XPath expression returns no element`; `Attribute not found in element`; `Failed to remove XML attribute`
- **Microsoft Learn:** [Remove XML element attribute](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#removeelementattribute)

### Set XML element attribute

- **Inventory id:** `xml/set-xml-element-attribute`
- **Kind:** native-action
- **Purpose:** Writes XML element attribute.
- **Key inputs:** `XML document` (XML node); `XPath query` (Text value; optional); `Attribute name` (Text value); `Attribute value` (Text value)
- **Produces:** None listed
- **Exceptions:** `Invalid XPath expression provided`; `XPath expression returns no element`; `Failed to set XML attribute`
- **Microsoft Learn:** [Set XML element attribute](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#setelementattribute)

### Set XML element value

- **Inventory id:** `xml/set-xml-element-value`
- **Kind:** native-action
- **Purpose:** Writes XML element value.
- **Key inputs:** `XML document` (XML node); `XPath query` (Text value; optional); `XML element value` (Text value)
- **Produces:** None listed
- **Exceptions:** `Invalid XPath expression provided`; `XPath expression returns no element`; `Failed to set element value`
- **Microsoft Learn:** [Set XML element value](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#setelementvalue)

### Write XML to file

- **Inventory id:** `xml/write-xml-to-file`
- **Kind:** native-action
- **Purpose:** Writes XML to file.
- **Key inputs:** `File path` (File); `XML to write` (Text value); `Encoding` (System default, ASCII, Unicode, Unicode big endian, UTF-8); `Format XML` (Boolean value); `Indentation per level` (Numeric value; optional)
- **Produces:** None listed
- **Exceptions:** `Invalid directory specified`; `Failed to write XML to file`
- **Microsoft Learn:** [Write XML to file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/xml#writexmltofile)
