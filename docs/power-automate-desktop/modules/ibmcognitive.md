# IBM Cognitive

Call IBM Watson document, vision, translation, and tone APIs.

This page documents every **native action** in this group (5 items).

## Actions

### Analyze tone

- **Inventory id:** `ibmcognitive/analyze-tone`
- **Kind:** native-action
- **Purpose:** Invokes the IBM service named 'Analyze Tone'.
- **Key inputs:** `API key` (Text value); `Version date` (Text value); `Service endpoint location` (US South, US East, Europe, Australia, Japan, UK, Korea); `Instance ID` (Text value); `Provide text` (From text, From file); `Text` (Text value); `File path` (File); `Content type` (text/plain, text/html, application/json); `Tones` (Text value; optional); `Sentences` (Text value; optional); `Timeout` (Numeric value; optional)
- **Produces:** `JSONResponse` (Custom object); `StatusCode` (Numeric value)
- **Exceptions:** `Request timeout expired`; `Failed to Invoke cognitive services`
- **Microsoft Learn:** [Analyze tone](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ibmcognitive#analyzetoneibm)

### Classify Image

- **Inventory id:** `ibmcognitive/classify-image`
- **Kind:** native-action
- **Purpose:** Invokes the IBM service named 'Classify Image'.
- **Key inputs:** `API key` (Text value); `Version date` (Text value); `Service endpoint location` (US South, Europe, Korea); `Instance ID` (Text value); `Provide image` (From file, From GCS); `Image file path` (File); `Image URL` (Text value); `Owners` (Text value; optional); `Classifier IDs` (Text value; optional); `Threshold` (Text value; optional); `Language` (Text value; optional); `Timeout` (Numeric value; optional)
- **Produces:** `JSONResponse` (Custom object); `StatusCode` (Numeric value)
- **Exceptions:** `Request timeout expired`; `Failed to Invoke cognitive services`
- **Microsoft Learn:** [Classify Image](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ibmcognitive#classifyimageibm)

### Convert document

- **Inventory id:** `ibmcognitive/convert-document`
- **Kind:** native-action
- **Purpose:** Converts document.
- **Key inputs:** `Username` (Text value); `Password` (Direct encrypted input or Text value); `Version date` (Text value); `File path` (File); `Mime type` (text/html, text/xhtml+xml, application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document); `Conversion target` (Answer units, Normalized HTML, Normalized text); `Answer units` (Text value; optional); `Timeout` (Numeric value; optional)
- **Produces:** `JSONResponse` (Custom object); `StatusCode` (Numeric value)
- **Exceptions:** `Request timeout expired`; `Failed to Invoke cognitive services`
- **Microsoft Learn:** [Convert document](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ibmcognitive#convertdocumentibm)

### Identify language

- **Inventory id:** `ibmcognitive/identify-language`
- **Kind:** native-action
- **Purpose:** Invokes the IBM service named 'Identify Language'.
- **Key inputs:** `API key` (Text value); `Version date` (Text value); `Service endpoint location` (US South, US East, Europe, Australia, Japan, UK, Korea); `Instance ID` (Text value); `Text` (Text value); `Content type` (Text value; optional); `Timeout` (Numeric value; optional)
- **Produces:** `JSONResponse` (Custom object); `StatusCode` (Numeric value)
- **Exceptions:** `Request timeout expired`; `Failed to Invoke cognitive services`
- **Microsoft Learn:** [Identify language](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ibmcognitive#identifylanguage)

### Translate

- **Inventory id:** `ibmcognitive/translate`
- **Kind:** native-action
- **Purpose:** Invokes the IBM service named 'Translate'.
- **Key inputs:** `API key` (Text value); `Version date` (Text value); `Service endpoint location` (US South, US East, Europe, Australia, Japan, UK, Korea); `Instance ID` (Text value); `Translate mode` (Model ID, Source and target); `Model ID` (Text value); `Source` (Text value); `Target` (Text value); `Text` (List of Text values); `Timeout` (Numeric value; optional)
- **Produces:** `JSONResponse` (Custom object); `StatusCode` (Numeric value)
- **Exceptions:** `Request timeout expired`; `Failed to Invoke cognitive services`
- **Microsoft Learn:** [Translate](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ibmcognitive#translateibm)
