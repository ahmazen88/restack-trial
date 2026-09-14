# FTP

Connect to FTP/FTPS servers and transfer files.

- Actions in this module: **15**
- Official docs: [FTP actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp)

## Actions

### Open FTP connection

This action establishes a specific connection to a remote FTP server, and stores that connection as a variable for later use.

Designer name: **Open FTP connection**. Official reference: [FTP / Open FTP connection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#openconnection).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Host | Required | Text value | — |
| Port | Optional | Numeric value | 21 |
| Active mode | Choice | Boolean value | False |
| Username | Required | Text value | — |
| Password | Optional | Direct encrypted input or Text value | — |
| Timeout | Optional | Numeric value | 10 |

**Outputs**

| Variable | Type |
|---|---|
| FTPConnection | FTP connection |

**On error:** `Login failure error`, `Connection error`.

---

### List FTP directory

This action returns the subdirectories and files contained in the current directory of an FTP connection.

Designer name: **List FTP directory**. Official reference: [FTP / List FTP directory](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#listdirectory).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Connection | Required | FTP connection | — |
| Path | Optional | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| Directories | List of FTP directories |
| Files | List of FTP files |

**On error:** `Listing error`, `Not connected error`, `Directory doesn't exist error`.

---

### Open secure FTP connection

This action establishes a specific secure connection to a remote FTP server, and stores that connection as a variable for later use.

Designer name: **Open secure FTP connection**. Official reference: [FTP / Open secure FTP connection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#opensecureconnection).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Host | Required | Text value | — |
| Port | Optional | Numeric value | 22 |
| Active mode | Choice | Boolean value | True |
| Secure FTP Protocol | Choice | SFTP, FTPS explicit, FTPS implicit | SFTP |
| Authentication method | Choice | Username and password, Private key, Private key and passphrase | Username and password |
| User name | Required | Text value | — |
| Password | Optional | Direct encrypted input or Text value | — |
| Path to private key | Required | Text value | — |
| Private key pass phrase | Optional | Direct encrypted input or Text value | — |
| Timeout | Optional | Numeric value | 10 |

**Outputs**

| Variable | Type |
|---|---|
| SftpConnection | FTP connection |

**On error:** `Login failure error`, `Connection error`.

---

### Close connection

This action closes an open FTP connection.

Designer name: **Close connection**. Official reference: [FTP / Close connection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#closeconnection).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Connection | Required | FTP connection | — |

Produces no variables.

**On error:** `Not connected error`.

---

### Change working directory

This action sets the current working directory for an FTP connection.

Designer name: **Change working directory**. Official reference: [FTP / Change working directory](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#changeworkingdirectory).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Connection | Required | FTP connection | — |
| Set working directory to | Required | Text value | — |

Produces no variables.

**On error:** `Not connected error`, `Directory doesn't exist error`, `Can't change working directory error`.

---

### Download file(s) from FTP

Downloads one or more files from an FTP server.

Designer name: **Download file(s) from FTP**. Official reference: [FTP / Download file(s) from FTP](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#downloadfiles).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| FTP connection | Required | FTP connection | — |
| Download into folder | Required | Folder | — |
| File(s) to download | Required | List of FTP files | — |
| Transfer type | Choice | Auto, Binary, ASCII | Auto |
| If file exists | Choice | Overwrite, Do not download, Download with unique name | Overwrite |

Produces no variables.

**On error:** `Not connected error`, `Remote file doesn't exist error`, `Directory doesn't exist error`, `FTP connection aborted error`, `Can't download file error`.

---

### Download folder(s) from FTP

Downloads one or more folders from an FTP server.

Designer name: **Download folder(s) from FTP**. Official reference: [FTP / Download folder(s) from FTP](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#downloadfolders).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| FTP connection | Required | FTP connection | — |
| Folder(s) to download | Required | List of FTP directories | — |
| Download into local folder | Required | Folder | — |

Produces no variables.

**On error:** `Not connected error`, `Remote directory doesn't exist error`, `Directory doesn't exist error`, `FTP connection aborted error`, `Can't download directory error`.

---

### Upload File(s) to FTP

Uploads one or more files to an FTP server.

Designer name: **Upload File(s) to FTP**. Official reference: [FTP / Upload File(s) to FTP](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#uploadfiles).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| FTP connection | Required | FTP connection | — |
| File(s) to upload | Required | List of Files | — |
| Remote location | Optional | Text value | — |
| Transfer type | Choice | Auto, Binary, ASCII | Auto |
| If file exists | Choice | Overwrite, Do not download, Download with unique name | Overwrite |

Produces no variables.

**On error:** `Not connected error`, `File not found error`, `FTP connection aborted error`, `Upload file error`.

---

### Upload folder(s) to FTP

Uploads one or more folders to an FTP server.

Designer name: **Upload folder(s) to FTP**. Official reference: [FTP / Upload folder(s) to FTP](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#uploadfolders).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| FTP connection | Required | FTP connection | — |
| Folder(s) to upload | Required | List of Folders | — |
| Remote location | Required | Text value | — |

Produces no variables.

**On error:** `Not connected error`, `Remote directory doesn't exist error`, `FTP connection aborted error`, `Upload directory error`.

---

### Delete FTP file

Deletes one or more files from an FTP server.

Designer name: **Delete FTP file**. Official reference: [FTP / Delete FTP file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#deletefiles).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| FTP connection | Required | FTP connection | — |
| Files to delete | Required | List of FTP files | — |

Produces no variables.

**On error:** `Not connected error`, `File not found error`, `Can't delete file error`.

---

### Rename FTP File

Renames a file that resides on an FTP server.

Designer name: **Rename FTP File**. Official reference: [FTP / Rename FTP File](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#renamefile).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| FTP connection | Required | FTP connection | — |
| File to rename | Required | FTP file | — |
| New file name | Required | Text value | — |

Produces no variables.

**On error:** `Not connected error`, `Can't rename file error`, `File not found error`.

---

### Create FTP directory

Creates a directory on an FTP server.

Designer name: **Create FTP directory**. Official reference: [FTP / Create FTP directory](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#createdirectory).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| FTP connection | Required | FTP connection | — |
| New directory | Required | FTP directory | — |

Produces no variables.

**On error:** `Access denied error`, `File exists error`, `Create directory error`, `Directory doesn't exist error`, `Not connected error`.

---

### Delete FTP directory

Deletes a directory from an FTP server.

Designer name: **Delete FTP directory**. Official reference: [FTP / Delete FTP directory](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#deletedirectory).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| FTP connection | Required | FTP connection | — |
| Directory to delete | Required | FTP directory | — |

Produces no variables.

**On error:** `Delete directory error`, `Remote directory doesn't exist error`, `Working directory change error`, `Not connected error`.

---

### Invoke FTP command

Invokes the given literal FTP command on the server.

Designer name: **Invoke FTP command**. Official reference: [FTP / Invoke FTP command](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#invokecommand).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| FTP connection | Required | FTP connection | — |
| FTP command | Required | Text value | — |
| Valid reply code(s) | Optional | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| ReplyCode | Text value |
| ReplyText | Text value |

**On error:** `Invoke command error`, `Not connected error`.

---

### Synchronize directories

Synchronize the files and subdirectories of a given Folder with a given remote FTP directory.

Designer name: **Synchronize directories**. Official reference: [FTP / Synchronize directories](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#synchronizedirectoryaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| FTP connection | Required | FTP connection | — |
| Synchronization direction | Choice | Remote -> local (Download), Local -> remote (Upload) | Remote -> local (Download) |
| Files to sync | Choice | All files, Only files matching the file filter, Only files not matching the file filter | All files |
| File filter | Required | Text value | * |
| Local folder | Required | Folder | — |
| FTP directory | Optional | FTP directory | / |
| Delete if source is absent | Choice | Boolean value | False |
| Include subdirectories | Choice | Boolean value | True |
| Time difference in hours | Optional | Numeric value | 0 |
| Time difference in minutes | Optional | Numeric value | 0 |
| Time difference ahead | Choice | Boolean value | True |

**Outputs**

| Variable | Type |
|---|---|
| FtpFilesAdded | List of FTP files |
| FtpFilesModified | List of FTP files |
| FtpFilesDeleted | List of FTP files |
| FilesAdded | List of Files |
| FilesModified | List of Files |
| FilesDeleted | List of Files |

**On error:** `Listing error`, `Not connected error`, `File not found error`, `FTP connection aborted error`, `Upload file error`, `Remote file doesn't exist error`, `Can't download file error`, `Delete directory error`, `Synchronization failed error`.

---
