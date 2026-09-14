# Microsoft Cognitive — how each function works

Native Actions pane module **Microsoft Cognitive**.

8 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Analyze image

- **Id:** `microsoftcognitive/analyze-image`
- **Kind:** native-action
- **Purpose:** Runs **Analyze image** from the actions pane.

**Use case.** In OCR or sentiment on a document image, drop **Analyze image** on the canvas. Runs **Analyze image** from the actions pane.

**Demonstration.**

```text
**Analyze image**
- Server location: `West US`
- Subscription key: `INV-1042`
- Provide image: `From file`
- Image file: `C:\RPA\Invoices\INV-1042.pdf`
- Image URL: `https://api.contoso.example/v1/invoices`
- Visual features: `INV-1042`
- Details: `INV-1042`
- Language: `INV-1042`
- … 1 more parameter(s) in the action modal
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: a specialist who reads a page and returns notes.

**In combination.** Call Analyze image / OCR / Sentiment, then store the text in a variable.

### Describe image

- **Id:** `microsoftcognitive/describe-image`
- **Kind:** native-action
- **Purpose:** Runs **Describe image** from the actions pane.

**Use case.** In OCR or sentiment on a document image, drop **Describe image** on the canvas. Runs **Describe image** from the actions pane.

**Demonstration.**

```text
**Describe image**
- Server location: `West US`
- Subscription key: `INV-1042`
- Provide image: `From file`
- Image file: `C:\RPA\Invoices\INV-1042.pdf`
- Image URL: `https://api.contoso.example/v1/invoices`
- Max candidates: `INV-1042`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: a specialist who reads a page and returns notes.

**In combination.** Call Analyze image / OCR / Sentiment, then store the text in a variable.

### Detect language

- **Id:** `microsoftcognitive/detect-language`
- **Kind:** native-action
- **Purpose:** Runs **Detect language** from the actions pane.

**Use case.** In OCR or sentiment on a document image, drop **Detect language** on the canvas. Runs **Detect language** from the actions pane.

**Demonstration.**

```text
**Detect language**
- Server location: `West US`
- Subscription key: `INV-1042`
- Text: `INV-1042`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: a specialist who reads a page and returns notes.

**In combination.** Call Analyze image / OCR / Sentiment, then store the text in a variable.

### Key phrases

- **Id:** `microsoftcognitive/key-phrases`
- **Kind:** native-action
- **Purpose:** Runs **Key phrases** from the actions pane.

**Use case.** In OCR or sentiment on a document image, drop **Key phrases** on the canvas. Runs **Key phrases** from the actions pane.

**Demonstration.**

```text
**Key phrases**
- Server location: `West US`
- Subscription key: `INV-1042`
- Text: `%Files%`
- Language: `INV-1042`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: a specialist who reads a page and returns notes.

**In combination.** Call Analyze image / OCR / Sentiment, then store the text in a variable.

### OCR

- **Id:** `microsoftcognitive/ocr`
- **Kind:** native-action
- **Purpose:** Runs **OCR** from the actions pane.

**Use case.** In OCR or sentiment on a document image, drop **OCR** on the canvas. Runs **OCR** from the actions pane.

**Demonstration.**

```text
**OCR**
- Server location: `West US`
- Subscription key: `INV-1042`
- Provide image: `From file`
- Image file: `C:\RPA\Invoices\INV-1042.pdf`
- Image URL: `https://api.contoso.example/v1/invoices`
- Language: `INV-1042`
- Detect orientation: `INV-1042`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: a specialist who reads a page and returns notes.

**In combination.** Call Analyze image / OCR / Sentiment, then store the text in a variable.

### Sentiment

- **Id:** `microsoftcognitive/sentiment`
- **Kind:** native-action
- **Purpose:** Runs **Sentiment** from the actions pane.

**Use case.** In OCR or sentiment on a document image, drop **Sentiment** on the canvas. Runs **Sentiment** from the actions pane.

**Demonstration.**

```text
**Sentiment**
- Server location: `West US`
- Subscription key: `INV-1042`
- Text: `%Files%`
- Language: `INV-1042`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: a specialist who reads a page and returns notes.

**In combination.** Call Analyze image / OCR / Sentiment, then store the text in a variable.

### Spell check

- **Id:** `microsoftcognitive/spell-check`
- **Kind:** native-action
- **Purpose:** Runs **Spell check** from the actions pane.

**Use case.** In OCR or sentiment on a document image, drop **Spell check** on the canvas. Runs **Spell check** from the actions pane.

**Demonstration.**

```text
**Spell check**
- Subscription key: `INV-1042`
- Text: `%Files%`
- Mode: `INV-1042`
- Mkt: `INV-1042`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: a specialist who reads a page and returns notes.

**In combination.** Call Analyze image / OCR / Sentiment, then store the text in a variable.

### Tag image

- **Id:** `microsoftcognitive/tag-image`
- **Kind:** native-action
- **Purpose:** Runs **Tag image** from the actions pane.

**Use case.** In OCR or sentiment on a document image, drop **Tag image** on the canvas. Runs **Tag image** from the actions pane.

**Demonstration.**

```text
**Tag image**
- Server location: `West US`
- Subscription key: `INV-1042`
- Provide image: `From file`
- Image file: `C:\RPA\Invoices\INV-1042.pdf`
- Image URL: `https://api.contoso.example/v1/invoices`
- Timeout: `30`
Produces:
- `%JSONResponse%` (Custom object)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: a specialist who reads a page and returns notes.

**In combination.** Call Analyze image / OCR / Sentiment, then store the text in a variable.
