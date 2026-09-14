# Folder

Create, copy, move, list, and delete folders.

- Actions in this module: **10**
- Official docs: [Folder actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder)

## Actions

### If folder exists

Mark the beginning of a conditional block of actions depending on whether a folder exists or not.

Designer name: **If folder exists**. Official reference: [Folder / If folder exists](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#iffolderexistsaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| If folder | Choice | Exists, Doesn't exist | Exists |
| Folder path | Required | Folder | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Get files in folder

Retrieve the list of files in a folder.

Designer name: **Get files in folder**. Official reference: [Folder / Get files in folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#getfiles).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Folder | Required | Folder | — |
| File filter | Required | Text value | * |
| Include subfolders | Choice | Boolean value | False |
| Fail upon denied access to any subfolder | Choice | Boolean value | True |
| Sort by | Choice | No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists | No sort |
| Descending | Choice | Boolean value | False |
| Then by | Choice | No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists | No sort |
| Descending | Choice | Boolean value | False |
| Then by | Choice | No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists | No sort |
| Descending | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| Files | List of Files |

**On error:** `Folder doesn't exist`, `Can't retrieve list of files`.

---

### Get subfolders in folder

Retrieve the list of subfolders in a folder.

Designer name: **Get subfolders in folder**. Official reference: [Folder / Get subfolders in folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#getsubfolders).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Folder | Required | Folder | — |
| Folder filter | Required | Text value | * |
| Include subfolders | Choice | Boolean value | False |
| Fail upon denied access to any subfolder | Choice | Boolean value | True |
| Sort by | Choice | No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists | No sort |
| Descending | Choice | Boolean value | False |
| Then by | Choice | No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists | No sort |
| Descending | Choice | Boolean value | False |
| Then by | Choice | No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists | No sort |
| Descending | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| Folders | List of Folders |

**On error:** `Folder doesn't exist`, `Can't retrieve list of subfolders`.

---

### Create folder

Create a new folder.

Designer name: **Create folder**. Official reference: [Folder / Create folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#create).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Create new folder into | Required | Folder | — |
| New folder name | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| NewFolder | Folder |

**On error:** `Folder doesn't exist`, `Can't create folder`, `New folder path and name are empty`.

---

### Delete folder

Delete an existing folder and its contents (files and subfolders).

Designer name: **Delete folder**. Official reference: [Folder / Delete folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#delete).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Folder to delete | Required | Folder | — |

Produces no variables.

**On error:** `Folder doesn't exist`, `Can't delete folder`.

---

### Empty folder

Delete all the contents of a folder (files and subfolders) without deleting the folder itself.

Designer name: **Empty folder**. Official reference: [Folder / Empty folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#empty).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Folder to empty | Required | Folder | — |

Produces no variables.

**On error:** `Folder doesn't exist`, `Can't delete folder's contents`.

---

### Copy folder

Copy a folder into a destination folder.

Designer name: **Copy folder**. Official reference: [Folder / Copy folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#copy).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Folder to copy | Required | Folder | — |
| Destination folder | Required | Folder | — |
| If folder exists | Choice | Do nothing, Overwrite | Do nothing |

**Outputs**

| Variable | Type |
|---|---|
| CopiedFolder | Folder |

**On error:** `Folder doesn't exist`, `Destination folder doesn't exist`, `Can't copy folder`.

---

### Move folder

Move an existing folder into a destination folder.

Designer name: **Move folder**. Official reference: [Folder / Move folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#move).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Folder to move | Required | Folder | — |
| Destination folder | Required | Folder | — |

**Outputs**

| Variable | Type |
|---|---|
| MovedFolder | Folder |

**On error:** `Folder doesn't exist`, `Destination folder doesn't exist`, `Can't move folder`.

---

### Rename folder

Change the name of a folder.

Designer name: **Rename folder**. Official reference: [Folder / Rename folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#rename).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Folder to rename | Required | Folder | — |
| New folder name | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| RenamedFolder | Folder |

**On error:** `Folder doesn't exist`, `Can't rename folder`.

---

### Get special folder

Retrieve the path of a Windows' special folder (such as Desktop, My Pictures, Internet Cache etc.).

Designer name: **Get special folder**. Official reference: [Folder / Get special folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#getspecialfolder).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Special folder name | Choice | Programs, Personal, Favorites, Startup, Recent, Send To, Start Menu, Music, Desktop, Templates, Application Data, Local Application Data, Internet Cache, Cookies, History, Common Application Data, System, Program Files, Pictures, Common Program Files | Desktop |

**Outputs**

| Variable | Type |
|---|---|
| SpecialFolderPath | Folder |

No module-specific exceptions are listed for this action.

---
