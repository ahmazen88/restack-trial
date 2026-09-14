# SharePoint

SharePoint operations inside a desktop flow. This is the **SharePoint cloud connector**, not a small fixed action list. Search the pane for the operation name; parameters match the cloud connector.

Official docs: [SharePoint in desktop flows](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/sharepoint).

Requires an Attended RPA license. Admins can disable the group with DLP or a machine registry policy.

## Operations you will use first

These names are the usual SharePoint connector operations that appear in PAD. Version suffixes (`V2`) may show depending on tenant.

### Files and folders

| Operation | Purpose |
|---|---|
| Get folder metadata using path | Resolve a folder path to metadata, including `Id`. |
| Get file metadata using path | Resolve a file path to metadata. |
| List folder | Children of a folder (files and subfolders as custom objects). |
| Get file content / Get file content using path | File body as binary. Follow with **Convert binary data to file**. |
| Create file | Upload binary to a library path. |
| Update file | Overwrite file content. |
| Delete file | Remove a file. |
| Copy file | Copy within SharePoint. |
| Move file | Move within SharePoint. |
| Create sharing link for a file or folder | Sharing URL. |
| Extract folder | Not every tenant shows the same set — search “folder”. |

### Lists

| Operation | Purpose |
|---|---|
| Get items | Filter/list rows. |
| Get item | One row by id. |
| Create item | New list item. |
| Update item | Patch fields. |
| Delete item | Remove a row. |

Each list item is a **custom object**. Folder items expose `IsFolder`, `Name`, `Path`, `Id`.

## Pattern: download every file in a folder

1. **Get folder metadata using path** → `Id`.
2. **List folder** with that id → list of custom objects.
3. **For each** object.
4. **If** `IsFolder` is false.
5. **Get file content using path** using the item `Path`.
6. **Convert binary data to file** using the item `Name`.

Nested folders: inside `IsFolder` = true, take `Name`, get metadata for `originalPath/Name`, **List folder** again, inner **For each**.

## Files as binary

Same rule as other cloud connectors: PAD file actions speak paths; SharePoint operations speak binary / identifiers.
