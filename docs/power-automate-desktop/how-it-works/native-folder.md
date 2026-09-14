# Folder — how each function works

Native Actions pane module **Folder**.

10 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Copy folder

- **Id:** `folder/copy-folder`
- **Kind:** native-action
- **Purpose:** Copies folder.

**Use case.** In today's drop folder under C:\Input, drop **Copy folder** on the canvas. Copies folder.

**Demonstration.**

```text
**Copy folder**
- Folder to copy: `C:\RPA\Invoices`
- Destination folder: `C:\RPA\Invoices`
- If folder exists: `C:\RPA\Invoices`
Produces:
- `%CopiedFolder%` (Folder)
```

**Analogy.** One tool in that kit: a desk inbox tray and the drawers under it.

**In combination.** Get files in folder, then loop; Create/Empty/Move folder around the batch.

### Create folder

- **Id:** `folder/create-folder`
- **Kind:** native-action
- **Purpose:** Creates folder.

**Use case.** In today's drop folder under C:\Input, drop **Create folder** on the canvas. Creates folder.

**Demonstration.**

```text
**Create folder**
- Create new folder into: `C:\RPA\Invoices`
- New folder name: `C:\RPA\Invoices`
Produces:
- `%NewFolder%` (Folder)
```

**Analogy.** One tool in that kit: a desk inbox tray and the drawers under it.

**In combination.** Get files in folder, then loop; Create/Empty/Move folder around the batch.

### Delete folder

- **Id:** `folder/delete-folder`
- **Kind:** native-action
- **Purpose:** Deletes folder.

**Use case.** In today's drop folder under C:\Input, drop **Delete folder** on the canvas. Deletes folder.

**Demonstration.**

```text
**Delete folder**
- Folder to delete: `C:\RPA\Invoices`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Get files in folder, then loop; Create/Empty/Move folder around the batch.

### Empty folder

- **Id:** `folder/empty-folder`
- **Kind:** native-action
- **Purpose:** Delete all the contents of a folder (files and subfolders) without deleting the folder itself.

**Use case.** In today's drop folder under C:\Input, drop **Empty folder** on the canvas. Delete all the contents of a folder (files and subfolders) without deleting the folder itself.

**Demonstration.**

```text
**Empty folder**
- Folder to empty: `C:\RPA\Invoices`
```

**Analogy.** One tool in that kit: a desk inbox tray and the drawers under it.

**In combination.** Get files in folder, then loop; Create/Empty/Move folder around the batch.

### Get files in folder

- **Id:** `folder/get-files-in-folder`
- **Kind:** native-action
- **Purpose:** Reads files in folder into a flow variable.

**Use case.** In today's drop folder under C:\Input, drop **Get files in folder** on the canvas. Reads files in folder into a flow variable.

**Demonstration.**

```text
**Get files in folder**
- Folder: `C:\RPA\Invoices`
- File filter: `*.pdf`
- Include subfolders: `False`
- Fail upon denied access to any subfolder: `True`
- Sort by: `No sort`
- Descending: `False`
- Then by: `No sort`
- Descending: `False`
- … 2 more parameter(s) in the action modal
Produces:
- `%Files%` (List of Files)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Get files in folder, then loop; Create/Empty/Move folder around the batch.

### Get special folder

- **Id:** `folder/get-special-folder`
- **Kind:** native-action
- **Purpose:** Reads special folder into a flow variable.

**Use case.** In today's drop folder under C:\Input, drop **Get special folder** on the canvas. Reads special folder into a flow variable.

**Demonstration.**

```text
**Get special folder**
- Special folder name: `C:\RPA\Invoices`
Produces:
- `%SpecialFolderPath%` (Folder)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Get files in folder, then loop; Create/Empty/Move folder around the batch.

### Get subfolders in folder

- **Id:** `folder/get-subfolders-in-folder`
- **Kind:** native-action
- **Purpose:** Reads subfolders in folder into a flow variable.

**Use case.** In today's drop folder under C:\Input, drop **Get subfolders in folder** on the canvas. Reads subfolders in folder into a flow variable.

**Demonstration.**

```text
**Get subfolders in folder**
- Folder: `C:\RPA\Invoices`
- Folder filter: `C:\RPA\Invoices`
- Include subfolders: `False`
- Fail upon denied access to any subfolder: `True`
- Sort by: `No sort`
- Descending: `False`
- Then by: `No sort`
- Descending: `False`
- … 2 more parameter(s) in the action modal
Produces:
- `%Folders%` (List of Folders)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Get files in folder, then loop; Create/Empty/Move folder around the batch.

### If folder exists

- **Id:** `folder/if-folder-exists`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when folder exists.

**Use case.** In today's drop folder under C:\Input, drop **If folder exists** on the canvas. Opens a conditional branch that runs when folder exists.

**Demonstration.**

```text
**If folder exists**
- If folder: `C:\RPA\Invoices`
- Folder path: `C:\RPA\Invoices`
Place the actions that should run inside this block, then End.
```

**Analogy.** Checking a condition on a clipboard before you choose a door.

**In combination.** Get files in folder, then loop; Create/Empty/Move folder around the batch. Combine with Else / Else if and End. Put Wait or If file exists before brittle UI/browser steps.

### Move folder

- **Id:** `folder/move-folder`
- **Kind:** native-action
- **Purpose:** Moves folder.

**Use case.** In today's drop folder under C:\Input, drop **Move folder** on the canvas. Moves folder.

**Demonstration.**

```text
**Move folder**
- Folder to move: `C:\RPA\Invoices`
- Destination folder: `C:\RPA\Invoices`
Produces:
- `%MovedFolder%` (Folder)
```

**Analogy.** One tool in that kit: a desk inbox tray and the drawers under it.

**In combination.** Get files in folder, then loop; Create/Empty/Move folder around the batch.

### Rename folder

- **Id:** `folder/rename-folder`
- **Kind:** native-action
- **Purpose:** Renames folder.

**Use case.** In today's drop folder under C:\Input, drop **Rename folder** on the canvas. Renames folder.

**Demonstration.**

```text
**Rename folder**
- Folder to rename: `C:\RPA\Invoices`
- New folder name: `C:\RPA\Invoices`
Produces:
- `%RenamedFolder%` (Folder)
```

**Analogy.** One tool in that kit: a desk inbox tray and the drawers under it.

**In combination.** Get files in folder, then loop; Create/Empty/Move folder around the batch.
