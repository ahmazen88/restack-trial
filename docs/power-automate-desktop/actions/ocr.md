# OCR

Extract or wait for on-screen text with Windows or Tesseract OCR.

- Actions in this module: **2**
- Official docs: [OCR actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)

## Actions

### Wait for text on screen (OCR)

Wait until a specific text appears/disappears on the screen, on the foreground window, or relative to an image on the screen or foreground window using OCR.

Designer name: **Wait for text on screen (OCR)**. Official reference: [OCR / Wait for text on screen (OCR)](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr#waittextonscreenaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Wait for text to | Choice | Appear, Disappear | Appear |
| OCR engine type | Required | Windows OCR engine, Tesseract engine, OCR engine variable | OCR engine variable |
| OCR engine variable | Required | OCREngineObject | — |
| Text to find | Required | Text value | — |
| Is regular expression | Choice | Boolean value | False |
| Search for text on | Choice | Entire screen, Foreground window | Entire screen |
| Search mode | Choice | Whole of specified source, Specific subregion only, Subregion relative to image | Whole of specified source |
| Image(s) | Required | List of Images | — |
| X1 | Optional | Numeric value | — |
| Tolerance | Optional | Numeric value | 10 |
| Y1 | Optional | Numeric value | — |
| X1 | Optional | Numeric value | — |
| X2 | Optional | Numeric value | — |
| Y1 | Optional | Numeric value | — |
| Y2 | Optional | Numeric value | — |
| X2 | Optional | Numeric value | — |
| Y2 | Optional | Numeric value | — |
| Windows OCR language | Choice | Chinese (Simplified), Chinese (Traditional), Czech, Danish, Dutch, English, Finnish, French, German, Greek, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Romanian, Russian, Serbian (Cyrillic), Serbian (Latin), Slovak, Spanish, Swedish, Turkish | English |
| Use other language | Choice | Boolean value | False |
| Tesseract language | Choice | English, German, Spanish, French, Italian | English |
| Language abbreviation | Required | Text value | — |
| Language data path | Required | Text value | — |
| Image width multiplier | Required | Numeric value | 1 |
| Image height multiplier | Required | Numeric value | 1 |
| Image matching algorithm | Choice | Basic, Advanced | Basic |
| Fail with timeout error | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| LocationOfTextFoundX | Numeric value |
| LocationOfTextFoundY | Numeric value |

**On error:** `Can't check if text exists in non-interactive mode`, `Invalid subregion coordinates`, `Failed to analyze text with OCR`, `Failed to create the OCR engine`, `Data path folder doesn't exist`, `The selected Windows language pack isn't installed on the machine`, `OCR engine not alive`, `Timeout error`.

---

### Extract text with OCR

Extract text from a given source using the given OCR engine.

Designer name: **Extract text with OCR**. Official reference: [OCR / Extract text with OCR](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr#extracttextwithocr).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| OCR engine | Required | Windows OCR engine, Tesseract engine, OCR engine variable | OCR engine variable |
| OCR engine variable | Required | OCREngineObject | — |
| OCR source | Choice | Screen, Foreground window, Image on disk | Screen |
| Image file path | Required | File | — |
| Search mode | Choice | Whole of specified source, Specific subregion only, Subregion relative to image | Whole of specified source |
| Image | Required | List of Images | — |
| Tolerance | Optional | Numeric value | 10 |
| X1 | Optional | Numeric value | — |
| X2 | Optional | Numeric value | — |
| Y1 | Optional | Numeric value | — |
| Y2 | Optional | Numeric value | — |
| Windows OCR language | Choice | Chinese (Simplified), Chinese (Traditional), Czech, Danish, Dutch, English, Finnish, French, German, Greek, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Romanian, Russian, Serbian (Cyrillic), Serbian (Latin), Slovak, Spanish, Swedish, Turkish | English |
| Use other language | Choice | Boolean value | False |
| Tesseract language | Choice | English, German, Spanish, French, Italian | English |
| Language abbreviation | Required | Text value | — |
| Language data path | Required | Text value | — |
| Image width multiplier | Required | Numeric value | 1 |
| Image height multiplier | Required | Numeric value | 1 |
| Wait for image to appear | Choice | Boolean value | True |
| Timeout | Required | Numeric value | 5 |
| Image matching algorithm | Choice | Basic, Advanced | Basic |

**Outputs**

| Variable | Type |
|---|---|
| OcrText | Text value |

**On error:** `Failed to extract text with OCR`, `Image file not found`, `Landmark image not found`, `Can't get text from screen in non-interactive mode`, `Failed to create the OCR engine`, `Data path folder doesn't exist`, `The selected Windows language pack isn't installed on the machine`, `OCR engine not alive`.

---
