# Folder

Create, copy, move, list, and empty folders.

This page documents every **native action** in this group (10 items).

## Actions

### Copy folder

- **Inventory id:** `folder/copy-folder`
- **Kind:** native-action
- **Purpose:** Copies folder.
- **Key inputs:** `Folder to copy` (Folder); `Destination folder` (Folder); `If folder exists` (Do nothing, Overwrite)
- **Produces:** `CopiedFolder` (Folder)
- **Exceptions:** `Folder doesn't exist`; `Destination folder doesn't exist`; `Can't copy folder`
- **Microsoft Learn:** [Copy folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#copy)

### Create folder

- **Inventory id:** `folder/create-folder`
- **Kind:** native-action
- **Purpose:** Creates folder.
- **Key inputs:** `Create new folder into` (Folder); `New folder name` (Text value)
- **Produces:** `NewFolder` (Folder)
- **Exceptions:** `Folder doesn't exist`; `Can't create folder`; `New folder path and name are empty`
- **Microsoft Learn:** [Create folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#create)

### Delete folder

- **Inventory id:** `folder/delete-folder`
- **Kind:** native-action
- **Purpose:** Deletes folder.
- **Key inputs:** `Folder to delete` (Folder)
- **Produces:** None listed
- **Exceptions:** `Folder doesn't exist`; `Can't delete folder`
- **Microsoft Learn:** [Delete folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#delete)

### Empty folder

- **Inventory id:** `folder/empty-folder`
- **Kind:** native-action
- **Purpose:** Delete all the contents of a folder (files and subfolders) without deleting the folder itself.
- **Key inputs:** `Folder to empty` (Folder)
- **Produces:** None listed
- **Exceptions:** `Folder doesn't exist`; `Can't delete folder's contents`
- **Microsoft Learn:** [Empty folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#empty)

### Get files in folder

- **Inventory id:** `folder/get-files-in-folder`
- **Kind:** native-action
- **Purpose:** Reads files in folder into a flow variable.
- **Key inputs:** `Folder` (Folder); `File filter` (Text value); `Include subfolders` (Boolean value); `Fail upon denied access to any subfolder` (Boolean value); `Sort by` (No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists); `Descending` (Boolean value); `Then by` (No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists); `Descending` (Boolean value); `Then by` (No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists); `Descending` (Boolean value)
- **Produces:** `Files` (List of Files)
- **Exceptions:** `Folder doesn't exist`; `Can't retrieve list of files`
- **Microsoft Learn:** [Get files in folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#getfiles)

### Get special folder

- **Inventory id:** `folder/get-special-folder`
- **Kind:** native-action
- **Purpose:** Reads special folder into a flow variable.
- **Key inputs:** `Special folder name` (Programs, Personal, Favorites, Startup, Recent, Send To, Start Menu, Music, Desktop, Templates, Application Data, Local Application Data, Internet Cache, Cookies, History, Common Application Data, System, Program Files, Pictures, Common Program Files)
- **Produces:** `SpecialFolderPath` (Folder)
- **Exceptions:** none listed
- **Microsoft Learn:** [Get special folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#getspecialfolder)

### Get subfolders in folder

- **Inventory id:** `folder/get-subfolders-in-folder`
- **Kind:** native-action
- **Purpose:** Reads subfolders in folder into a flow variable.
- **Key inputs:** `Folder` (Folder); `Folder filter` (Text value); `Include subfolders` (Boolean value); `Fail upon denied access to any subfolder` (Boolean value); `Sort by` (No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists); `Descending` (Boolean value); `Then by` (No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists); `Descending` (Boolean value); `Then by` (No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists); `Descending` (Boolean value)
- **Produces:** `Folders` (List of Folders)
- **Exceptions:** `Folder doesn't exist`; `Can't retrieve list of subfolders`
- **Microsoft Learn:** [Get subfolders in folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#getsubfolders)

### If folder exists

- **Inventory id:** `folder/if-folder-exists`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when folder exists.
- **Key inputs:** `If folder` (Exists, Doesn't exist); `Folder path` (Folder)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [If folder exists](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#iffolderexistsaction)

### Move folder

- **Inventory id:** `folder/move-folder`
- **Kind:** native-action
- **Purpose:** Moves folder.
- **Key inputs:** `Folder to move` (Folder); `Destination folder` (Folder)
- **Produces:** `MovedFolder` (Folder)
- **Exceptions:** `Folder doesn't exist`; `Destination folder doesn't exist`; `Can't move folder`
- **Microsoft Learn:** [Move folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#move)

### Rename folder

- **Inventory id:** `folder/rename-folder`
- **Kind:** native-action
- **Purpose:** Renames folder.
- **Key inputs:** `Folder to rename` (Folder); `New folder name` (Text value)
- **Produces:** `RenamedFolder` (Folder)
- **Exceptions:** `Folder doesn't exist`; `Can't rename folder`
- **Microsoft Learn:** [Rename folder](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/folder#rename)
