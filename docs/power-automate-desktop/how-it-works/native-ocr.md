# OCR — how each function works

Native Actions pane module **OCR**.

3 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Extract text with OCR

- **Id:** `ocr/extract-text-with-ocr`
- **Kind:** native-action
- **Purpose:** Extracts text with OCR.

**Use case.** In text painted on a screen the UI tree cannot see, drop **Extract text with OCR** on the canvas. Extracts text with OCR.

**Demonstration.**

```text
**Extract text with OCR**
- OCR engine: `%OCREngine%`
- OCR engine variable: `%OCREngine%`
- OCR source: `Screen`
- Image file path: `C:\RPA\Invoices\INV-1042.pdf`
- Search mode: `Whole of specified source`
- Image: `%Files%`
- Tolerance: `10`
- X1: `1`
- … 13 more parameter(s) in the action modal
Produces:
- `%OcrText%` (Text value)
```

**Analogy.** One tool in that kit: reading a shop window with your eyes instead of asking the cashier.

**In combination.** If text on screen (OCR) or Extract text with OCR after an image or window is visible.

### If text on screen (OCR)

- **Id:** `ocr/if-text-on-screen-ocr`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when text on screen (OCR).

**Use case.** In text painted on a screen the UI tree cannot see, drop **If text on screen (OCR)** on the canvas. Opens a conditional branch that runs when text on screen (OCR).

**Demonstration.**

```text
**If text on screen (OCR)**
- If text: `Exists`
- OCR engine type: `%OCREngine%`
- OCR engine variable: `%OCREngine%`
- Text to find: `INV-1042`
- Is regular expression: `False`
- Search for text on: `Entire screen`
- Search mode: `Whole of specified source`
- Image(s): `%Files%`
- … 17 more parameter(s) in the action modal
Produces:
- `%LocationOfTextFoundX%` (Numeric value)
- `%LocationOfTextFoundY%` (Numeric value)
Place the actions that should run inside this block, then End.
```

**Analogy.** Checking a condition on a clipboard before you choose a door.

**In combination.** If text on screen (OCR) or Extract text with OCR after an image or window is visible. Combine with Else / Else if and End. Put Wait or If file exists before brittle UI/browser steps.

### Wait for text on screen (OCR)

- **Id:** `ocr/wait-for-text-on-screen-ocr`
- **Kind:** native-action
- **Purpose:** Pauses the flow until text on screen (OCR).

**Use case.** In text painted on a screen the UI tree cannot see, drop **Wait for text on screen (OCR)** on the canvas. Pauses the flow until text on screen (OCR).

**Demonstration.**

```text
**Wait for text on screen (OCR)**
- Wait for text to: `Appear`
- OCR engine type: `%OCREngine%`
- OCR engine variable: `%OCREngine%`
- Text to find: `INV-1042`
- Is regular expression: `False`
- Search for text on: `Entire screen`
- Search mode: `Whole of specified source`
- Image(s): `%Files%`
- … 18 more parameter(s) in the action modal
Produces:
- `%LocationOfTextFoundX%` (Numeric value)
- `%LocationOfTextFoundY%` (Numeric value)
```

**Analogy.** Standing at the microwave until it beeps, so you do not grab a cold plate.

**In combination.** If text on screen (OCR) or Extract text with OCR after an image or window is visible.
