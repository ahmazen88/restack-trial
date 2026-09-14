# OCR

Find or extract on-screen text with Windows OCR or Tesseract.

This page documents every **native action** in this group (3 items).

## Actions

### Extract text with OCR

- **Inventory id:** `ocr/extract-text-with-ocr`
- **Kind:** native-action
- **Purpose:** Extracts text with OCR.
- **Key inputs:** `OCR engine` (Windows OCR engine, Tesseract engine, OCR engine variable); `OCR engine variable` (OCREngineObject); `OCR source` (Screen, Foreground window, Image on disk); `Image file path` (File); `Search mode` (Whole of specified source, Specific subregion only, Subregion relative to image); `Image` (List of Images); `Tolerance` (Numeric value; optional); `X1` (Numeric value; optional); `X2` (Numeric value; optional); `Y1` (Numeric value; optional); `Y2` (Numeric value; optional); `Windows OCR language` (Chinese (Simplified), Chinese (Traditional), Czech, Danish, Dutch, English, Finnish, French, German, Greek, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Romanian, Russian, Serbian (Cyrillic), Serbian (Latin), Slovak, Spanish, Swedish, Turkish); `Use other language` (Boolean value); `Tesseract language` (English, German, Spanish, French, Italian); `Language abbreviation` (Text value); `Language data path` (Text value); `Image width multiplier` (Numeric value); `Image height multiplier` (Numeric value); `Wait for image to appear` (Boolean value); `Timeout` (Numeric value); `Image matching algorithm` (Basic, Advanced)
- **Produces:** `OcrText` (Text value)
- **Exceptions:** `Failed to extract text with OCR`; `Image file not found`; `Landmark image not found`; `Can't get text from screen in non-interactive mode`; `Failed to create the OCR engine`; `Data path folder doesn't exist`; `The selected Windows language pack isn't installed on the machine`; `OCR engine not alive`
- **Microsoft Learn:** [Extract text with OCR](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr#extracttextwithocr)

### If text on screen (OCR)

- **Inventory id:** `ocr/if-text-on-screen-ocr`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when text on screen (OCR).
- **Key inputs:** `If text` (Exists, Doesn't exist); `OCR engine type` (Windows OCR engine, Tesseract engine, OCR engine variable); `OCR engine variable` (OCREngineObject); `Text to find` (Text value); `Is regular expression` (Boolean value); `Search for text on` (Entire screen, Foreground window); `Search mode` (Whole of specified source, Specific subregion only, Subregion relative to image); `Image(s)` (List of Images); `X1` (Numeric value; optional); `Tolerance` (Numeric value; optional); `Y1` (Numeric value; optional); `X1` (Numeric value; optional); `X2` (Numeric value; optional); `Y1` (Numeric value; optional); `Y2` (Numeric value; optional); `X2` (Numeric value; optional); `Y2` (Numeric value; optional); `Windows OCR language` (Chinese (Simplified), Chinese (Traditional), Czech, Danish, Dutch, English, Finnish, French, German, Greek, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Romanian, Russian, Serbian (Cyrillic), Serbian (Latin), Slovak, Spanish, Swedish, Turkish); `Use other language` (Boolean value); `Tesseract language` (English, German, Spanish, French, Italian); `Language abbreviation` (Text value); `Language data path` (Text value); `Image width multiplier` (Numeric value); `Image height multiplier` (Numeric value); `Image matching algorithm` (Basic, Advanced)
- **Produces:** `LocationOfTextFoundX` (Numeric value); `LocationOfTextFoundY` (Numeric value)
- **Exceptions:** `Can't check if text exists in non-interactive mode`; `Invalid subregion coordinates`; `Failed to analyze text with OCR`; `Failed to create the OCR engine`; `Data path folder doesn't exist`; `The selected Windows language pack isn't installed on the machine`; `OCR engine not alive`
- **Microsoft Learn:** [If text on screen (OCR)](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr#iftextonscreenaction)

### Wait for text on screen (OCR)

- **Inventory id:** `ocr/wait-for-text-on-screen-ocr`
- **Kind:** native-action
- **Purpose:** Pauses the flow until text on screen (OCR).
- **Key inputs:** `Wait for text to` (Appear, Disappear); `OCR engine type` (Windows OCR engine, Tesseract engine, OCR engine variable); `OCR engine variable` (OCREngineObject); `Text to find` (Text value); `Is regular expression` (Boolean value); `Search for text on` (Entire screen, Foreground window); `Search mode` (Whole of specified source, Specific subregion only, Subregion relative to image); `Image(s)` (List of Images); `X1` (Numeric value; optional); `Tolerance` (Numeric value; optional); `Y1` (Numeric value; optional); `X1` (Numeric value; optional); `X2` (Numeric value; optional); `Y1` (Numeric value; optional); `Y2` (Numeric value; optional); `X2` (Numeric value; optional); `Y2` (Numeric value; optional); `Windows OCR language` (Chinese (Simplified), Chinese (Traditional), Czech, Danish, Dutch, English, Finnish, French, German, Greek, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Romanian, Russian, Serbian (Cyrillic), Serbian (Latin), Slovak, Spanish, Swedish, Turkish); `Use other language` (Boolean value); `Tesseract language` (English, German, Spanish, French, Italian); `Language abbreviation` (Text value); `Language data path` (Text value); `Image width multiplier` (Numeric value); `Image height multiplier` (Numeric value); `Image matching algorithm` (Basic, Advanced); `Fail with timeout error` (Boolean value)
- **Produces:** `LocationOfTextFoundX` (Numeric value); `LocationOfTextFoundY` (Numeric value)
- **Exceptions:** `Can't check if text exists in non-interactive mode`; `Invalid subregion coordinates`; `Failed to analyze text with OCR`; `Failed to create the OCR engine`; `Data path folder doesn't exist`; `The selected Windows language pack isn't installed on the machine`; `OCR engine not alive`; `Timeout error`
- **Microsoft Learn:** [Wait for text on screen (OCR)](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr#waittextonscreenaction)
