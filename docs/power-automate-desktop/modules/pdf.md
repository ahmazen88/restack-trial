# PDF

Extract text, tables, images, and pages, or merge PDF files.

This page documents every **native action** in this group (5 items).

## Actions

### Extract images from PDF

- **Inventory id:** `pdf/extract-images-from-pdf`
- **Kind:** native-action
- **Purpose:** Extracts images from PDF.
- **Key inputs:** `PDF file` (File); `Password` (Direct encrypted input or Text value; optional); `Page(s) to extract` (All, Single, Range); `Single page number` (Numeric value); `From page number` (Numeric value); `To page number` (Numeric value); `Image(s) name` (Text value); `Save image(s) to` (Folder)
- **Produces:** None listed
- **Exceptions:** `Invalid password`; `Failed to extract images`; `Folder doesn't exist`; `PDF file doesn't exist`
- **Microsoft Learn:** [Extract images from PDF](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/pdf#extractimagesfrompdfaction)

### Extract PDF file pages to new PDF file

- **Inventory id:** `pdf/extract-pdf-file-pages-to-new-pdf-file`
- **Kind:** native-action
- **Purpose:** Extracts PDF file pages to new PDF file.
- **Key inputs:** `PDF file` (File); `Password` (Direct encrypted input or Text value; optional); `Page selection` (Text value); `Extracted PDF path` (File); `If file exists` (Overwrite, Don't overwrite, Add sequential suffix)
- **Produces:** `ExtractedPDF` (File)
- **Exceptions:** `Invalid password`; `PDF file doesn't exist`; `Page out of bounds`; `Invalid page selection`; `Failed to extract new PDF`
- **Microsoft Learn:** [Extract PDF file pages to new PDF file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/pdf#extractpages)

### Extract tables from PDF

- **Inventory id:** `pdf/extract-tables-from-pdf`
- **Kind:** native-action
- **Purpose:** Extracts tables from PDF.
- **Key inputs:** `PDF file` (File); `Page(s) to extract` (All, Single, Range); `Single page number` (Numeric value); `From page number` (Numeric value); `To page number` (Numeric value); `Password` (Direct encrypted input or Text value; optional); `Merge tables that cross page margins` (Boolean value); `First line contains column names` (Boolean value)
- **Produces:** `ExtractedPDFTables` (List of PDF table info)
- **Exceptions:** `PDF file doesn't exist`; `Invalid password`; `Failed to extract tables`
- **Microsoft Learn:** [Extract tables from PDF](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/pdf#extracttablesfrompdfaction)

### Extract text from PDF

- **Inventory id:** `pdf/extract-text-from-pdf`
- **Kind:** native-action
- **Purpose:** Extracts text from PDF.
- **Key inputs:** `PDF file` (File); `Page(s) to extract` (All, Single, Range); `Single page number` (Numeric value); `From page number` (Numeric value); `To page number` (Numeric value); `Password` (Direct encrypted input or Text value; optional); `Optimize for structured data` (Boolean value)
- **Produces:** `ExtractedPDFText` (Text value)
- **Exceptions:** `PDF file doesn't exist`; `Invalid password`; `Failed to extract text`
- **Microsoft Learn:** [Extract text from PDF](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/pdf#extracttextfrompdfaction)

### Merge PDF files

- **Inventory id:** `pdf/merge-pdf-files`
- **Kind:** native-action
- **Purpose:** Merges PDF files.
- **Key inputs:** `PDF files` (List of Files); `Merged PDF path` (File); `If file exists` (Overwrite, Don't overwrite, Add sequential suffix); `Passwords` (Direct encrypted input or Text value; optional); `Delimiter` (Text value)
- **Produces:** `MergedPDF` (File)
- **Exceptions:** `PDF file doesn't exist`; `Invalid password`; `Failed to merge PDF files`
- **Microsoft Learn:** [Merge PDF files](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/pdf#mergefiles)
