# PDF

Extract text, tables, and images from PDFs and merge or split files.

- Actions in this module: **5**
- Official docs: [PDF actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/pdf)

## Actions

### Extract text from PDF

You can extract text from a PDF file by using the "Extract text from PDF" action.

Designer name: **Extract text from PDF**. Official reference: [PDF / Extract text from PDF](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/pdf#extracttextfrompdfaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| PDF file | Required | File | — |
| Page(s) to extract | Choice | All, Single, Range | All |
| Single page number | Required | Numeric value | — |
| From page number | Required | Numeric value | — |
| To page number | Required | Numeric value | — |
| Password | Optional | Direct encrypted input or Text value | — |
| Optimize for structured data | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| ExtractedPDFText | Text value |

**On error:** `PDF file doesn't exist`, `Invalid password`, `Failed to extract text`.

---

### Extract tables from PDF

You can extract tables that are contained in a PDF file by using the **Extract tables from PDF** action.

Designer name: **Extract tables from PDF**. Official reference: [PDF / Extract tables from PDF](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/pdf#extracttablesfrompdfaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| PDF file | Required | File | — |
| Page(s) to extract | Choice | All, Single, Range | All |
| Single page number | Required | Numeric value | — |
| From page number | Required | Numeric value | — |
| To page number | Required | Numeric value | — |
| Password | Optional | Direct encrypted input or Text value | — |
| Merge tables that cross page margins | Choice | Boolean value | True |
| First line contains column names | Choice | Boolean value | True |

**Outputs**

| Variable | Type |
|---|---|
| ExtractedPDFTables | List of PDF table info |

**On error:** `PDF file doesn't exist`, `Invalid password`, `Failed to extract tables`.

---

### Extract images from PDF

To extract images from a PDF file you can use the **Extract images from PDF** action.

Designer name: **Extract images from PDF**. Official reference: [PDF / Extract images from PDF](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/pdf#extractimagesfrompdfaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| PDF file | Required | File | — |
| Password | Optional | Direct encrypted input or Text value | — |
| Page(s) to extract | Choice | All, Single, Range | All |
| Single page number | Required | Numeric value | — |
| From page number | Required | Numeric value | — |
| To page number | Required | Numeric value | — |
| Image(s) name | Required | Text value | — |
| Save image(s) to | Required | Folder | — |

Produces no variables.

**On error:** `Invalid password`, `Failed to extract images`, `Folder doesn't exist`, `PDF file doesn't exist`.

---

### Extract PDF file pages to new PDF file

You can create a new PDF file by extracting pages from an existing PDF file by using the **PDF file pages to a new PDF file** action.

Designer name: **Extract PDF file pages to new PDF file**. Official reference: [PDF / Extract PDF file pages to new PDF file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/pdf#extractpages).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| PDF file | Required | File | — |
| Password | Optional | Direct encrypted input or Text value | — |
| Page selection | Required | Text value | — |
| Extracted PDF path | Required | File | — |
| If file exists | Choice | Overwrite, Don't overwrite, Add sequential suffix | Add sequential suffix |

**Outputs**

| Variable | Type |
|---|---|
| ExtractedPDF | File |

**On error:** `Invalid password`, `PDF file doesn't exist`, `Page out of bounds`, `Invalid page selection`, `Failed to extract new PDF`.

---

### Merge PDF files

Merges multiple PDF files into a new one.

Designer name: **Merge PDF files**. Official reference: [PDF / Merge PDF files](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/pdf#mergefiles).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| PDF files | Required | List of Files | — |
| Merged PDF path | Required | File | — |
| If file exists | Choice | Overwrite, Don't overwrite, Add sequential suffix | Add sequential suffix |
| Passwords | Optional | Direct encrypted input or Text value | — |
| Delimiter | Required | Text value | , |

**Outputs**

| Variable | Type |
|---|---|
| MergedPDF | File |

**On error:** `PDF file doesn't exist`, `Invalid password`, `Failed to merge PDF files`.

---
