# Microsoft Cognitive

Call Azure Cognitive Services for text, vision, and language.

- Actions in this module: **8**
- Official docs: [Microsoft Cognitive actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/microsoftcognitive)

## Actions

### Spell check

Invokes the Microsoft Cognitive service named 'Bing Spell Check.'.

Designer name: **Spell check**. Official reference: [Microsoft Cognitive / Spell check](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/microsoftcognitive#spellcheck).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Subscription key | Required | Text value | — |
| Text | Required | List of Text values | — |
| Mode | Optional | Text value | — |
| Mkt | Optional | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Request timeout expired`, `Failed to Invoke cognitive services`.

---

### Analyze image

Invokes the Microsoft Cognitive service named 'Analyze Image.'.

Designer name: **Analyze image**. Official reference: [Microsoft Cognitive / Analyze image](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/microsoftcognitive#analyzeimagemicrosoft).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Server location | Choice | West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East | West US |
| Subscription key | Required | Text value | — |
| Provide image | Choice | From file, From GCS | From file |
| Image file | Required | File | — |
| Image URL | Required | Text value | — |
| Visual features | Optional | Text value | — |
| Details | Optional | Text value | — |
| Language | Optional | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Request timeout expired`, `Failed to Invoke cognitive services`.

---

### Describe image

Invokes the Microsoft Cognitive service named 'Describe Image.'.

Designer name: **Describe image**. Official reference: [Microsoft Cognitive / Describe image](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/microsoftcognitive#describeimagemicrosoft).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Server location | Choice | West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East | West US |
| Subscription key | Required | Text value | — |
| Provide image | Choice | From file, From GCS | From file |
| Image file | Required | File | — |
| Image URL | Required | Text value | — |
| Max candidates | Optional | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Request timeout expired`, `Failed to Invoke cognitive services`.

---

### OCR

Invokes the Microsoft Cognitive service named 'OCR.'.

Designer name: **OCR**. Official reference: [Microsoft Cognitive / OCR](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/microsoftcognitive#ocrmicrosoft).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Server location | Choice | West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East | West US |
| Subscription key | Required | Text value | — |
| Provide image | Choice | From file, From GCS | From file |
| Image file | Required | File | — |
| Image URL | Required | Text value | — |
| Language | Optional | Text value | — |
| Detect orientation | Optional | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Request timeout expired`, `Failed to Invoke cognitive services`.

---

### Tag image

Invokes the Microsoft Cognitive service named 'Tag Image.'.

Designer name: **Tag image**. Official reference: [Microsoft Cognitive / Tag image](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/microsoftcognitive#tagimagemicrosoft).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Server location | Choice | West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East | West US |
| Subscription key | Required | Text value | — |
| Provide image | Choice | From file, From GCS | From file |
| Image file | Required | File | — |
| Image URL | Required | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Request timeout expired`, `Failed to Invoke cognitive services`.

---

### Detect language

Invokes the Microsoft Cognitive service named 'Text Analytics - Detect Language.'.

Designer name: **Detect language**. Official reference: [Microsoft Cognitive / Detect language](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/microsoftcognitive#detectlanguage).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Server location | Choice | West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East | West US |
| Subscription key | Required | Text value | — |
| Text | Required | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Request timeout expired`, `Failed to Invoke cognitive services`.

---

### Key phrases

Invokes the Microsoft Cognitive service named 'Text Analytics - Key Phrases.'.

Designer name: **Key phrases**. Official reference: [Microsoft Cognitive / Key phrases](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/microsoftcognitive#keyphrases).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Server location | Choice | West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East | West US |
| Subscription key | Required | Text value | — |
| Text | Required | List of Text values | — |
| Language | Optional | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Request timeout expired`, `Failed to Invoke cognitive services`.

---

### Sentiment

Invokes the Microsoft Cognitive service named 'Text Analytics - Sentiment.'.

Designer name: **Sentiment**. Official reference: [Microsoft Cognitive / Sentiment](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/microsoftcognitive#sentiment).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Server location | Choice | West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East | West US |
| Subscription key | Required | Text value | — |
| Text | Required | List of Text values | — |
| Language | Optional | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Request timeout expired`, `Failed to Invoke cognitive services`.

---
