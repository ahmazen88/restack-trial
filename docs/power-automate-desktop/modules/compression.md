# Compression

Zip and unzip files and folders.

This page documents every **native action** in this group (2 items).

## Actions

### Unzip files

- **Inventory id:** `compression/unzip-files`
- **Kind:** native-action
- **Purpose:** Extracts files from a ZIP archive.
- **Key inputs:** `Archive path` (File); `Destination folder` (Folder); `Password` (Direct encrypted input or Text value; optional); `Include mask` (Text value; optional); `Exclude mask` (Text value; optional)
- **Produces:** None listed
- **Exceptions:** `Can't create destination folder`; `Archive not found`; `Archive isn't a valid ZIP file`; `Failed to unzip files`
- **Microsoft Learn:** [Unzip files](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/compression#unzipfiles)

### ZIP files

- **Inventory id:** `compression/zip-files`
- **Kind:** native-action
- **Purpose:** Compresses files or folders into a ZIP archive.
- **Key inputs:** `Archive path` (File); `File(s) to zip` (List of FileSystemObject); `Compression level` (None, Best speed, Best balance of speed and compression, Best compression); `Password` (Direct encrypted input or Text value; optional); `Archive comment` (Text value; optional)
- **Produces:** `ZipFile` (File)
- **Exceptions:** `File or folder doesn't exist`; `File or folder name is invalid`; `Archive already exists but it isn't a valid ZIP archive`; `Failed to zip files`
- **Microsoft Learn:** [ZIP files](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/compression#zipfiles)
