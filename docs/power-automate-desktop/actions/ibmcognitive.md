# IBM Cognitive

Call IBM Watson language and visual recognition APIs.

- Actions in this module: **5**
- Official docs: [IBM Cognitive actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ibmcognitive)

## Actions

### Convert document

Invokes the IBM service named 'Convert Document'.

Designer name: **Convert document**. Official reference: [IBM Cognitive / Convert document](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ibmcognitive#convertdocumentibm).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Username | Required | Text value | — |
| Password | Required | Direct encrypted input or Text value | — |
| Version date | Required | Text value | — |
| File path | Required | File | — |
| Mime type | Choice | text/html, text/xhtml+xml, application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document | text/html |
| Conversion target | Choice | Answer units, Normalized HTML, Normalized text | Answer units |
| Answer units | Optional | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Request timeout expired`, `Failed to Invoke cognitive services`.

---

### Translate

Invokes the IBM service named 'Translate'.

Designer name: **Translate**. Official reference: [IBM Cognitive / Translate](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ibmcognitive#translateibm).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| API key | Required | Text value | — |
| Version date | Required | Text value | — |
| Service endpoint location | Choice | US South, US East, Europe, Australia, Japan, UK, Korea | US East |
| Instance ID | Required | Text value | — |
| Translate mode | Choice | Model ID, Source and target | Model ID |
| Model ID | Required | Text value | — |
| Source | Required | Text value | — |
| Target | Required | Text value | — |
| Text | Required | List of Text values | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Request timeout expired`, `Failed to Invoke cognitive services`.

---

### Identify language

Invokes the IBM service named 'Identify Language'.

Designer name: **Identify language**. Official reference: [IBM Cognitive / Identify language](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ibmcognitive#identifylanguage).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| API key | Required | Text value | — |
| Version date | Required | Text value | — |
| Service endpoint location | Choice | US South, US East, Europe, Australia, Japan, UK, Korea | US East |
| Instance ID | Required | Text value | — |
| Text | Required | Text value | — |
| Content type | Optional | Text value | text/plain |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Request timeout expired`, `Failed to Invoke cognitive services`.

---

### Analyze tone

Invokes the IBM service named 'Analyze Tone'.

Designer name: **Analyze tone**. Official reference: [IBM Cognitive / Analyze tone](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ibmcognitive#analyzetoneibm).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| API key | Required | Text value | — |
| Version date | Required | Text value | — |
| Service endpoint location | Choice | US South, US East, Europe, Australia, Japan, UK, Korea | US East |
| Instance ID | Required | Text value | — |
| Provide text | Choice | From text, From file | From text |
| Text | Required | Text value | — |
| File path | Required | File | — |
| Content type | Choice | text/plain, text/html, application/json | text/plain |
| Tones | Optional | Text value | — |
| Sentences | Optional | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Request timeout expired`, `Failed to Invoke cognitive services`.

---

### Classify Image

Invokes the IBM service named 'Classify Image'.

Designer name: **Classify Image**. Official reference: [IBM Cognitive / Classify Image](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ibmcognitive#classifyimageibm).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| API key | Required | Text value | — |
| Version date | Required | Text value | — |
| Service endpoint location | Choice | US South, Europe, Korea | US South |
| Instance ID | Required | Text value | — |
| Provide image | Choice | From file, From GCS | From file |
| Image file path | Required | File | — |
| Image URL | Required | Text value | — |
| Owners | Optional | Text value | me |
| Classifier IDs | Optional | Text value | default |
| Threshold | Optional | Text value | — |
| Language | Optional | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Request timeout expired`, `Failed to Invoke cognitive services`.

---
