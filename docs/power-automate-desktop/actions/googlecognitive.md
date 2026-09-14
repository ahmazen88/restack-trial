# Google Cognitive

Call Google Cloud Vision and Natural Language APIs.

- Actions in this module: **9**
- Official docs: [Google Cognitive actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/googlecognitive)

## Actions

### Analyze sentiment

Invokes the Google Cloud Natural Language service named 'Analyze Sentiment'.

Designer name: **Analyze sentiment**. Official reference: [Google Cognitive / Analyze sentiment](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/googlecognitive#analyzesentimentgoogle).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| API key | Required | Text value | — |
| Document type | Choice | Plain text, HTML | Plain text |
| Provide document | Choice | From file, From GCS | From file |
| File path | Required | File | — |
| GCS Content URI | Required | Text value | — |
| Language | Optional | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Failed to Invoke cognitive services`, `Request timeout expired`.

---

### Analyze entities

Invokes the Google Cloud Natural Language service named 'Analyze Entities'.

Designer name: **Analyze entities**. Official reference: [Google Cognitive / Analyze entities](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/googlecognitive#analyzeentitiesgoogle).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| API key | Required | Text value | — |
| Document type | Choice | Plain text, HTML | Plain text |
| Provide file | Choice | From file, From GCS | From file |
| File path | Required | File | — |
| GCS URL | Required | Text value | — |
| Language | Optional | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Failed to Invoke cognitive services`, `Request timeout expired`.

---

### Analyze syntax

Invokes the Google Cloud Natural Language service named 'Analyze Syntax'.

Designer name: **Analyze syntax**. Official reference: [Google Cognitive / Analyze syntax](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/googlecognitive#analyzesyntaxgoogle).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| API key | Required | Text value | — |
| Document type | Choice | Plain text, HTML | Plain text |
| Provide document | Choice | From file, From GCS | From file |
| File path | Required | File | — |
| GCS Content URI | Required | Text value | — |
| Language | Optional | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Failed to Invoke cognitive services`, `Request timeout expired`.

---

### Label detection

Invokes the Google Cloud Vision service named 'Label Detection'.

Designer name: **Label detection**. Official reference: [Google Cognitive / Label detection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/googlecognitive#labeldetectiongoogle).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| API key | Required | Text value | — |
| Provide image | Choice | From file, From GCS | From file |
| Image file | Required | File | — |
| GCS Image URI | Required | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Failed to Invoke cognitive services`, `Request timeout expired`.

---

### Landmark detection

Invokes the Google Cloud Vision service named 'Landmark Detection'.

Designer name: **Landmark detection**. Official reference: [Google Cognitive / Landmark detection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/googlecognitive#landmarkdetectiongoogle).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| API key | Required | Text value | — |
| Provide image | Choice | From file, From GCS | From file |
| Image file path | Required | File | — |
| GCS Image URI | Required | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Failed to Invoke cognitive services`, `Request timeout expired`.

---

### Text Detection

Invokes the Google Cloud Vision service named 'Text Detection'.

Designer name: **Text Detection**. Official reference: [Google Cognitive / Text Detection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/googlecognitive#textdetectiongoogle).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| API key | Required | Text value | — |
| Provide image | Choice | From file, From GCS | From file |
| Image file | Required | File | — |
| GCS Image URI | Required | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Failed to Invoke cognitive services`, `Request timeout expired`.

---

### Logo detection

Invokes the Google Cloud Vision service named 'Logo Detection'.

Designer name: **Logo detection**. Official reference: [Google Cognitive / Logo detection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/googlecognitive#logodetectiongoogle).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| API key | Required | Text value | — |
| Provide image | Choice | From file, From GCS | From file |
| Image file | Required | File | — |
| GCS Image URI | Required | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Failed to Invoke cognitive services`, `Request timeout expired`.

---

### Image properties detection

Invokes the Google Cloud Vision service named 'Image Properties Detection'.

Designer name: **Image properties detection**. Official reference: [Google Cognitive / Image properties detection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/googlecognitive#imagepropertiesdetectiongoogle).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| API key | Required | Text value | — |
| Provide image | Choice | From file, From GCS | From file |
| Image file | Required | File | — |
| GCS Image URI | Required | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Failed to Invoke cognitive services`, `Request timeout expired`.

---

### Safe search detection

Invokes the Google Cloud Vision service named 'Safe Search Detection'.

Designer name: **Safe search detection**. Official reference: [Google Cognitive / Safe search detection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/googlecognitive#safesearchdetectiongoogle).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| API key | Required | Text value | — |
| Provide image | Choice | From file, From GCS | From file |
| Image file | Required | File | — |
| GCS Image URI | Required | Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| StatusCode | Numeric value |

**On error:** `Failed to Invoke cognitive services`, `Request timeout expired`.

---
