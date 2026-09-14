# Compression

Zip and unzip files and folders.

- Actions in this module: **2**
- Official docs: [Compression actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/compression)

## Actions

### ZIP files

Compress one or more files or folders into a ZIP archive.

Designer name: **ZIP files**. Official reference: [Compression / ZIP files](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/compression#zipfiles).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Archive path | Required | File | — |
| File(s) to zip | Required | List of FileSystemObject | — |
| Compression level | Choice | None, Best speed, Best balance of speed and compression, Best compression | Best balance of speed and compression |
| Password | Optional | Direct encrypted input or Text value | — |
| Archive comment | Optional | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| ZipFile | File |

**On error:** `File or folder doesn't exist`, `File or folder name is invalid`, `Archive already exists but it isn't a valid ZIP archive`, `Failed to zip files`.

---

### Unzip files

Uncompress one or more files or folders contained in a ZIP archive.

Designer name: **Unzip files**. Official reference: [Compression / Unzip files](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/compression#unzipfiles).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Archive path | Required | File | — |
| Destination folder | Required | Folder | — |
| Password | Optional | Direct encrypted input or Text value | — |
| Include mask | Optional | Text value | — |
| Exclude mask | Optional | Text value | — |

Produces no variables.

**On error:** `Can't create destination folder`, `Archive not found`, `Archive isn't a valid ZIP file`, `Failed to unzip files`.

---
