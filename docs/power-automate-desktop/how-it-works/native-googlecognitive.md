# Google Cognitive — how each function works

Native Actions pane module **Google Cognitive**.

9 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Analyze entities

- **Id:** `googlecognitive/analyze-entities`
- **Kind:** native-action
- **Purpose:** Invokes the Google Cloud Natural Language service named 'Analyze Entities'.

**Use case.** In classifying a scanned image the UI cannot read, drop **Analyze entities** on the canvas. Invokes the Google Cloud Natural Language service named 'Analyze Entities'.

**Demonstration.**

```text
**Analyze entities**
- API key: `INV-1042`
- Document type: `Plain text`
- Provide file: `C:\RPA\Invoices\INV-1042.pdf`
- File path: `C:\RPA\Invoices\INV-1042.pdf`
- GCS URL: `https://api.contoso.example/v1/invoices`
- Language: `INV-1042`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: asking an outside specialist to look at a photo.

**In combination.** Call the vision or language action, then branch on the returned JSON/text.

### Analyze sentiment

- **Id:** `googlecognitive/analyze-sentiment`
- **Kind:** native-action
- **Purpose:** Invokes the Google Cloud Natural Language service named 'Analyze Sentiment'.

**Use case.** In classifying a scanned image the UI cannot read, drop **Analyze sentiment** on the canvas. Invokes the Google Cloud Natural Language service named 'Analyze Sentiment'.

**Demonstration.**

```text
**Analyze sentiment**
- API key: `INV-1042`
- Document type: `Plain text`
- Provide document: `From file`
- File path: `C:\RPA\Invoices\INV-1042.pdf`
- GCS Content URI: `INV-1042`
- Language: `INV-1042`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: asking an outside specialist to look at a photo.

**In combination.** Call the vision or language action, then branch on the returned JSON/text.

### Analyze syntax

- **Id:** `googlecognitive/analyze-syntax`
- **Kind:** native-action
- **Purpose:** Invokes the Google Cloud Natural Language service named 'Analyze Syntax'.

**Use case.** In classifying a scanned image the UI cannot read, drop **Analyze syntax** on the canvas. Invokes the Google Cloud Natural Language service named 'Analyze Syntax'.

**Demonstration.**

```text
**Analyze syntax**
- API key: `INV-1042`
- Document type: `Plain text`
- Provide document: `From file`
- File path: `C:\RPA\Invoices\INV-1042.pdf`
- GCS Content URI: `INV-1042`
- Language: `INV-1042`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: asking an outside specialist to look at a photo.

**In combination.** Call the vision or language action, then branch on the returned JSON/text.

### Image properties detection

- **Id:** `googlecognitive/image-properties-detection`
- **Kind:** native-action
- **Purpose:** Invokes the Google Cloud Vision service named 'Image Properties Detection'.

**Use case.** In classifying a scanned image the UI cannot read, drop **Image properties detection** on the canvas. Invokes the Google Cloud Vision service named 'Image Properties Detection'.

**Demonstration.**

```text
**Image properties detection**
- API key: `INV-1042`
- Provide image: `From file`
- Image file: `C:\RPA\Invoices\INV-1042.pdf`
- GCS Image URI: `INV-1042`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: asking an outside specialist to look at a photo.

**In combination.** Call the vision or language action, then branch on the returned JSON/text.

### Label detection

- **Id:** `googlecognitive/label-detection`
- **Kind:** native-action
- **Purpose:** Invokes the Google Cloud Vision service named 'Label Detection'.

**Use case.** In classifying a scanned image the UI cannot read, drop **Label detection** on the canvas. Invokes the Google Cloud Vision service named 'Label Detection'.

**Demonstration.**

```text
**Label detection**
- API key: `INV-1042`
- Provide image: `From file`
- Image file: `C:\RPA\Invoices\INV-1042.pdf`
- GCS Image URI: `INV-1042`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: asking an outside specialist to look at a photo.

**In combination.** Call the vision or language action, then branch on the returned JSON/text.

### Landmark detection

- **Id:** `googlecognitive/landmark-detection`
- **Kind:** native-action
- **Purpose:** Invokes the Google Cloud Vision service named 'Landmark Detection'.

**Use case.** In classifying a scanned image the UI cannot read, drop **Landmark detection** on the canvas. Invokes the Google Cloud Vision service named 'Landmark Detection'.

**Demonstration.**

```text
**Landmark detection**
- API key: `INV-1042`
- Provide image: `From file`
- Image file path: `C:\RPA\Invoices\INV-1042.pdf`
- GCS Image URI: `INV-1042`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: asking an outside specialist to look at a photo.

**In combination.** Call the vision or language action, then branch on the returned JSON/text.

### Logo detection

- **Id:** `googlecognitive/logo-detection`
- **Kind:** native-action
- **Purpose:** Invokes the Google Cloud Vision service named 'Logo Detection'.

**Use case.** In classifying a scanned image the UI cannot read, drop **Logo detection** on the canvas. Invokes the Google Cloud Vision service named 'Logo Detection'.

**Demonstration.**

```text
**Logo detection**
- API key: `INV-1042`
- Provide image: `From file`
- Image file: `C:\RPA\Invoices\INV-1042.pdf`
- GCS Image URI: `INV-1042`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: asking an outside specialist to look at a photo.

**In combination.** Call the vision or language action, then branch on the returned JSON/text.

### Safe search detection

- **Id:** `googlecognitive/safe-search-detection`
- **Kind:** native-action
- **Purpose:** Invokes the Google Cloud Vision service named 'Safe Search Detection'.

**Use case.** In classifying a scanned image the UI cannot read, drop **Safe search detection** on the canvas. Invokes the Google Cloud Vision service named 'Safe Search Detection'.

**Demonstration.**

```text
**Safe search detection**
- API key: `INV-1042`
- Provide image: `From file`
- Image file: `C:\RPA\Invoices\INV-1042.pdf`
- GCS Image URI: `INV-1042`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: asking an outside specialist to look at a photo.

**In combination.** Call the vision or language action, then branch on the returned JSON/text.

### Text Detection

- **Id:** `googlecognitive/text-detection`
- **Kind:** native-action
- **Purpose:** Invokes the Google Cloud Vision service named 'Text Detection'.

**Use case.** In classifying a scanned image the UI cannot read, drop **Text Detection** on the canvas. Invokes the Google Cloud Vision service named 'Text Detection'.

**Demonstration.**

```text
**Text Detection**
- API key: `INV-1042`
- Provide image: `From file`
- Image file: `C:\RPA\Invoices\INV-1042.pdf`
- GCS Image URI: `INV-1042`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: asking an outside specialist to look at a photo.

**In combination.** Call the vision or language action, then branch on the returned JSON/text.
