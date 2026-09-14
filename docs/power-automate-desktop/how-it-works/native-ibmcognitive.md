# IBM Cognitive — how each function works

Native Actions pane module **IBM Cognitive**.

5 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Analyze tone

- **Id:** `ibmcognitive/analyze-tone`
- **Kind:** native-action
- **Purpose:** Invokes the IBM service named 'Analyze Tone'.

**Use case.** In translating a vendor PDF extract, drop **Analyze tone** on the canvas. Invokes the IBM service named 'Analyze Tone'.

**Demonstration.**

```text
**Analyze tone**
- API key: `INV-1042`
- Version date: `INV-1042`
- Service endpoint location: `https://api.contoso.example/v1/invoices`
- Instance ID: `INV-1042`
- Provide text: `From text`
- Text: `INV-1042`
- File path: `C:\RPA\Invoices\INV-1042.pdf`
- Content type: `text/plain`
- … 3 more parameter(s) in the action modal
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: sending a paragraph to a translation desk and getting it back.

**In combination.** Run Identify language or Translate, then write the result to Excel or a file.

### Classify Image

- **Id:** `ibmcognitive/classify-image`
- **Kind:** native-action
- **Purpose:** Invokes the IBM service named 'Classify Image'.

**Use case.** In translating a vendor PDF extract, drop **Classify Image** on the canvas. Invokes the IBM service named 'Classify Image'.

**Demonstration.**

```text
**Classify Image**
- API key: `INV-1042`
- Version date: `INV-1042`
- Service endpoint location: `https://api.contoso.example/v1/invoices`
- Instance ID: `INV-1042`
- Provide image: `From file`
- Image file path: `C:\RPA\Invoices\INV-1042.pdf`
- Image URL: `https://api.contoso.example/v1/invoices`
- Owners: `me`
- … 4 more parameter(s) in the action modal
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: sending a paragraph to a translation desk and getting it back.

**In combination.** Run Identify language or Translate, then write the result to Excel or a file.

### Convert document

- **Id:** `ibmcognitive/convert-document`
- **Kind:** native-action
- **Purpose:** Converts document.

**Use case.** In translating a vendor PDF extract, drop **Convert document** on the canvas. Converts document.

**Demonstration.**

```text
**Convert document**
- Username: `CONTOSO\rpa.bot`
- Password: `%Credential.Password%  (sensitive)`
- Version date: `INV-1042`
- File path: `C:\RPA\Invoices\INV-1042.pdf`
- Mime type: `%XmlDoc%`
- Conversion target: `Answer units`
- Answer units: `INV-1042`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: sending a paragraph to a translation desk and getting it back.

**In combination.** Run Identify language or Translate, then write the result to Excel or a file.

### Identify language

- **Id:** `ibmcognitive/identify-language`
- **Kind:** native-action
- **Purpose:** Invokes the IBM service named 'Identify Language'.

**Use case.** In translating a vendor PDF extract, drop **Identify language** on the canvas. Invokes the IBM service named 'Identify Language'.

**Demonstration.**

```text
**Identify language**
- API key: `INV-1042`
- Version date: `INV-1042`
- Service endpoint location: `https://api.contoso.example/v1/invoices`
- Instance ID: `INV-1042`
- Text: `INV-1042`
- Content type: `text/plain`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: sending a paragraph to a translation desk and getting it back.

**In combination.** Run Identify language or Translate, then write the result to Excel or a file.

### Translate

- **Id:** `ibmcognitive/translate`
- **Kind:** native-action
- **Purpose:** Invokes the IBM service named 'Translate'.

**Use case.** In translating a vendor PDF extract, drop **Translate** on the canvas. Invokes the IBM service named 'Translate'.

**Demonstration.**

```text
**Translate**
- API key: `INV-1042`
- Version date: `INV-1042`
- Service endpoint location: `https://api.contoso.example/v1/invoices`
- Instance ID: `INV-1042`
- Translate mode: `Model ID`
- Model ID: `INV-1042`
- Source: `INV-1042`
- Target: `INV-1042`
- … 2 more parameter(s) in the action modal
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: sending a paragraph to a translation desk and getting it back.

**In combination.** Run Identify language or Translate, then write the result to Excel or a file.
