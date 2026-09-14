# Compression — how each function works

Native Actions pane module **Compression**.

2 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Unzip files

- **Id:** `compression/unzip-files`
- **Kind:** native-action
- **Purpose:** Extracts files from a ZIP archive.

**Use case.** In packing a day's invoices to email or archive, drop **Unzip files** on the canvas. Extracts files from a ZIP archive.

**Demonstration.**

```text
**Unzip files**
- Archive path: `C:\RPA\Invoices\INV-1042.pdf`
- Destination folder: `C:\RPA\Invoices`
- Password: `%Credential.Password%  (sensitive)`
- Include mask: `INV-1042`
- Exclude mask: `INV-1042`
```

**Analogy.** One tool in that kit: a packing box and a box cutter.

**In combination.** ZIP files before send; Unzip files after download.

### ZIP files

- **Id:** `compression/zip-files`
- **Kind:** native-action
- **Purpose:** Compresses files or folders into a ZIP archive.

**Use case.** In packing a day's invoices to email or archive, drop **ZIP files** on the canvas. Compresses files or folders into a ZIP archive.

**Demonstration.**

```text
**ZIP files**
- Archive path: `C:\RPA\Invoices\INV-1042.pdf`
- File(s) to zip: `%Files%`
- Compression level: `Best balance of speed and compression`
- Password: `%Credential.Password%  (sensitive)`
- Archive comment: `Processed by desktop flow Close-P9`
Produces:
- `%ZipFile%` (File)
```

**Analogy.** One tool in that kit: a packing box and a box cutter.

**In combination.** ZIP files before send; Unzip files after download.
