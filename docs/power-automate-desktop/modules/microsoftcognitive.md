# Microsoft Cognitive

Call Azure Cognitive Services for vision, OCR, language, and sentiment.

This page documents every **native action** in this group (8 items).

## Actions

### Analyze image

- **Inventory id:** `microsoftcognitive/analyze-image`
- **Kind:** native-action
- **Purpose:** Runs **Analyze image** from the actions pane.
- **Key inputs:** `Server location` (West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East); `Subscription key` (Text value); `Provide image` (From file, From GCS); `Image file` (File); `Image URL` (Text value); `Visual features` (Text value; optional); `Details` (Text value; optional); `Language` (Text value; optional); `Timeout` (Numeric value; optional)
- **Produces:** `JSONResponse` (Custom object); `StatusCode` (Numeric value)
- **Exceptions:** `Request timeout expired`; `Failed to Invoke cognitive services`
- **Microsoft Learn:** [Analyze image](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/microsoftcognitive#analyzeimagemicrosoft)

### Describe image

- **Inventory id:** `microsoftcognitive/describe-image`
- **Kind:** native-action
- **Purpose:** Runs **Describe image** from the actions pane.
- **Key inputs:** `Server location` (West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East); `Subscription key` (Text value); `Provide image` (From file, From GCS); `Image file` (File); `Image URL` (Text value); `Max candidates` (Text value; optional); `Timeout` (Numeric value; optional)
- **Produces:** `JSONResponse` (Custom object); `StatusCode` (Numeric value)
- **Exceptions:** `Request timeout expired`; `Failed to Invoke cognitive services`
- **Microsoft Learn:** [Describe image](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/microsoftcognitive#describeimagemicrosoft)

### Detect language

- **Inventory id:** `microsoftcognitive/detect-language`
- **Kind:** native-action
- **Purpose:** Runs **Detect language** from the actions pane.
- **Key inputs:** `Server location` (West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East); `Subscription key` (Text value); `Text` (Text value); `Timeout` (Numeric value; optional)
- **Produces:** `JSONResponse` (Custom object); `StatusCode` (Numeric value)
- **Exceptions:** `Request timeout expired`; `Failed to Invoke cognitive services`
- **Microsoft Learn:** [Detect language](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/microsoftcognitive#detectlanguage)

### Key phrases

- **Inventory id:** `microsoftcognitive/key-phrases`
- **Kind:** native-action
- **Purpose:** Runs **Key phrases** from the actions pane.
- **Key inputs:** `Server location` (West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East); `Subscription key` (Text value); `Text` (List of Text values); `Language` (Text value; optional); `Timeout` (Numeric value; optional)
- **Produces:** `JSONResponse` (Custom object); `StatusCode` (Numeric value)
- **Exceptions:** `Request timeout expired`; `Failed to Invoke cognitive services`
- **Microsoft Learn:** [Key phrases](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/microsoftcognitive#keyphrases)

### OCR

- **Inventory id:** `microsoftcognitive/ocr`
- **Kind:** native-action
- **Purpose:** Runs **OCR** from the actions pane.
- **Key inputs:** `Server location` (West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East); `Subscription key` (Text value); `Provide image` (From file, From GCS); `Image file` (File); `Image URL` (Text value); `Language` (Text value; optional); `Detect orientation` (Text value; optional); `Timeout` (Numeric value; optional)
- **Produces:** `JSONResponse` (Custom object); `StatusCode` (Numeric value)
- **Exceptions:** `Request timeout expired`; `Failed to Invoke cognitive services`
- **Microsoft Learn:** [OCR](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/microsoftcognitive#ocrmicrosoft)

### Sentiment

- **Inventory id:** `microsoftcognitive/sentiment`
- **Kind:** native-action
- **Purpose:** Runs **Sentiment** from the actions pane.
- **Key inputs:** `Server location` (West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East); `Subscription key` (Text value); `Text` (List of Text values); `Language` (Text value; optional); `Timeout` (Numeric value; optional)
- **Produces:** `JSONResponse` (Custom object); `StatusCode` (Numeric value)
- **Exceptions:** `Request timeout expired`; `Failed to Invoke cognitive services`
- **Microsoft Learn:** [Sentiment](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/microsoftcognitive#sentiment)

### Spell check

- **Inventory id:** `microsoftcognitive/spell-check`
- **Kind:** native-action
- **Purpose:** Runs **Spell check** from the actions pane.
- **Key inputs:** `Subscription key` (Text value); `Text` (List of Text values); `Mode` (Text value; optional); `Mkt` (Text value; optional); `Timeout` (Numeric value; optional)
- **Produces:** `JSONResponse` (Custom object); `StatusCode` (Numeric value)
- **Exceptions:** `Request timeout expired`; `Failed to Invoke cognitive services`
- **Microsoft Learn:** [Spell check](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/microsoftcognitive#spellcheck)

### Tag image

- **Inventory id:** `microsoftcognitive/tag-image`
- **Kind:** native-action
- **Purpose:** Runs **Tag image** from the actions pane.
- **Key inputs:** `Server location` (West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East); `Subscription key` (Text value); `Provide image` (From file, From GCS); `Image file` (File); `Image URL` (Text value); `Timeout` (Numeric value; optional)
- **Produces:** `JSONResponse` (Custom object); `StatusCode` (Numeric value)
- **Exceptions:** `Request timeout expired`; `Failed to Invoke cognitive services`
- **Microsoft Learn:** [Tag image](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/microsoftcognitive#tagimagemicrosoft)
