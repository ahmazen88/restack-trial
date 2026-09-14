# PDF — how each function works

Native Actions pane module **PDF**.

5 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Extract images from PDF

- **Id:** `pdf/extract-images-from-pdf`
- **Kind:** native-action
- **Purpose:** Extracts images from PDF.

**Use case.** In vendor invoices that arrive as PDF only, drop **Extract images from PDF** on the canvas. Extracts images from PDF.

**Demonstration.**

```text
**Extract images from PDF**
- PDF file: `C:\RPA\Invoices\INV-1042.pdf`
- Password: `%Credential.Password%  (sensitive)`
- Page(s) to extract: `All`
- Single page number: `1`
- From page number: `1`
- To page number: `1`
- Image(s) name: `INV-1042`
- Save image(s) to: `(set in designer)`
```

**Analogy.** One tool in that kit: photocopying a contract, cutting out the table, stacking the pages.

**In combination.** Extract text or tables, then write Excel or a file; Merge PDF files at the end of the day.

### Extract PDF file pages to new PDF file

- **Id:** `pdf/extract-pdf-file-pages-to-new-pdf-file`
- **Kind:** native-action
- **Purpose:** Extracts PDF file pages to new PDF file.

**Use case.** In vendor invoices that arrive as PDF only, drop **Extract PDF file pages to new PDF file** on the canvas. Extracts PDF file pages to new PDF file.

**Demonstration.**

```text
**Extract PDF file pages to new PDF file**
- PDF file: `C:\RPA\Invoices\INV-1042.pdf`
- Password: `%Credential.Password%  (sensitive)`
- Page selection: `INV-1042`
- Extracted PDF path: `C:\RPA\Invoices\INV-1042.pdf`
- If file exists: `C:\RPA\Invoices\INV-1042.pdf`
Produces:
- `%ExtractedPDF%` (File)
```

**Analogy.** One tool in that kit: photocopying a contract, cutting out the table, stacking the pages.

**In combination.** Extract text or tables, then write Excel or a file; Merge PDF files at the end of the day.

### Extract tables from PDF

- **Id:** `pdf/extract-tables-from-pdf`
- **Kind:** native-action
- **Purpose:** Extracts tables from PDF.

**Use case.** In vendor invoices that arrive as PDF only, drop **Extract tables from PDF** on the canvas. Extracts tables from PDF.

**Demonstration.**

```text
**Extract tables from PDF**
- PDF file: `C:\RPA\Invoices\INV-1042.pdf`
- Page(s) to extract: `All`
- Single page number: `1`
- From page number: `1`
- To page number: `1`
- Password: `%Credential.Password%  (sensitive)`
- Merge tables that cross page margins: `True`
- First line contains column names: `True`
Produces:
- `%ExtractedPDFTables%` (List of PDF table info)
```

**Analogy.** One tool in that kit: photocopying a contract, cutting out the table, stacking the pages.

**In combination.** Extract text or tables, then write Excel or a file; Merge PDF files at the end of the day.

### Extract text from PDF

- **Id:** `pdf/extract-text-from-pdf`
- **Kind:** native-action
- **Purpose:** Extracts text from PDF.

**Use case.** Turn an invoice PDF into text you can Parse text and write to Excel.

**Demonstration.**

```text
**Extract text from PDF**
- PDF file: `C:\RPA\Invoices\INV-1042.pdf`
- Page(s) to extract: `All`
- Single page number: `1`
- From page number: `1`
- To page number: `1`
- Password: `%Credential.Password%  (sensitive)`
- Optimize for structured data: `False`
Produces:
- `%ExtractedPDFText%` (Text value)
```

**Analogy.** One tool in that kit: photocopying a contract, cutting out the table, stacking the pages.

**In combination.** Extract text or tables, then write Excel or a file; Merge PDF files at the end of the day.

### Merge PDF files

- **Id:** `pdf/merge-pdf-files`
- **Kind:** native-action
- **Purpose:** Merges PDF files.

**Use case.** In vendor invoices that arrive as PDF only, drop **Merge PDF files** on the canvas. Merges PDF files.

**Demonstration.**

```text
**Merge PDF files**
- PDF files: `%Files%`
- Merged PDF path: `C:\RPA\Invoices\INV-1042.pdf`
- If file exists: `C:\RPA\Invoices\INV-1042.pdf`
- Passwords: `%Credential.Password%  (sensitive)`
- Delimiter: `,`
Produces:
- `%MergedPDF%` (File)
```

**Analogy.** One tool in that kit: photocopying a contract, cutting out the table, stacking the pages.

**In combination.** Extract text or tables, then write Excel or a file; Merge PDF files at the end of the day.
