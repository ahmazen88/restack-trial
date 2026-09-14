# FTP — how each function works

Native Actions pane module **FTP**.

15 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Change working directory

- **Id:** `ftp/change-working-directory`
- **Kind:** native-action
- **Purpose:** This action sets the current working directory for an FTP connection.

**Use case.** In a vendor SFTP drop that still has no API, drop **Change working directory** on the canvas. This action sets the current working directory for an FTP connection.

**Demonstration.**

```text
**Change working directory**
- Connection: `%FTPConnection%`
- Set working directory to: `C:\RPA\Invoices`
```

**Analogy.** One tool in that kit: a loading dock: open the gate, drop pallets, close the gate.

**In combination.** Open FTP or secure FTP connection, transfer, Close connection.

### Close connection

- **Id:** `ftp/close-connection`
- **Kind:** native-action
- **Purpose:** Closes connection.

**Use case.** In a vendor SFTP drop that still has no API, drop **Close connection** on the canvas. Closes connection.

**Demonstration.**

```text
**Close connection**
- Connection: `%FTPConnection%`
```

**Analogy.** Turning out the lights when the work in that room is done.

**In combination.** Open FTP or secure FTP connection, transfer, Close connection. Call this only after the last use of the instance so you do not break later steps.

### Create FTP directory

- **Id:** `ftp/create-ftp-directory`
- **Kind:** native-action
- **Purpose:** Creates FTP directory.

**Use case.** In a vendor SFTP drop that still has no API, drop **Create FTP directory** on the canvas. Creates FTP directory.

**Demonstration.**

```text
**Create FTP directory**
- FTP connection: `%FTPConnection%`
- New directory: `C:\RPA\Invoices`
```

**Analogy.** One tool in that kit: a loading dock: open the gate, drop pallets, close the gate.

**In combination.** Open FTP or secure FTP connection, transfer, Close connection.

### Delete FTP directory

- **Id:** `ftp/delete-ftp-directory`
- **Kind:** native-action
- **Purpose:** Deletes FTP directory.

**Use case.** In a vendor SFTP drop that still has no API, drop **Delete FTP directory** on the canvas. Deletes FTP directory.

**Demonstration.**

```text
**Delete FTP directory**
- FTP connection: `%FTPConnection%`
- Directory to delete: `C:\RPA\Invoices`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Open FTP or secure FTP connection, transfer, Close connection.

### Delete FTP file

- **Id:** `ftp/delete-ftp-file`
- **Kind:** native-action
- **Purpose:** Deletes FTP file.

**Use case.** In a vendor SFTP drop that still has no API, drop **Delete FTP file** on the canvas. Deletes FTP file.

**Demonstration.**

```text
**Delete FTP file**
- FTP connection: `%FTPConnection%`
- Files to delete: `%Files%`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Open FTP or secure FTP connection, transfer, Close connection.

### Download file(s) from FTP

- **Id:** `ftp/download-file-s-from-ftp`
- **Kind:** native-action
- **Purpose:** Downloads file(s) from FTP.

**Use case.** In a vendor SFTP drop that still has no API, drop **Download file(s) from FTP** on the canvas. Downloads file(s) from FTP.

**Demonstration.**

```text
**Download file(s) from FTP**
- FTP connection: `%FTPConnection%`
- Download into folder: `C:\RPA\Invoices`
- File(s) to download: `%Files%`
- Transfer type: `Auto`
- If file exists: `C:\RPA\Invoices\INV-1042.pdf`
```

**Analogy.** One tool in that kit: a loading dock: open the gate, drop pallets, close the gate.

**In combination.** Open FTP or secure FTP connection, transfer, Close connection.

### Download folder(s) from FTP

- **Id:** `ftp/download-folder-s-from-ftp`
- **Kind:** native-action
- **Purpose:** Downloads folder(s) from FTP.

**Use case.** In a vendor SFTP drop that still has no API, drop **Download folder(s) from FTP** on the canvas. Downloads folder(s) from FTP.

**Demonstration.**

```text
**Download folder(s) from FTP**
- FTP connection: `%FTPConnection%`
- Folder(s) to download: `%Files%`
- Download into local folder: `C:\RPA\Invoices`
```

**Analogy.** One tool in that kit: a loading dock: open the gate, drop pallets, close the gate.

**In combination.** Open FTP or secure FTP connection, transfer, Close connection.

### Invoke FTP command

- **Id:** `ftp/invoke-ftp-command`
- **Kind:** native-action
- **Purpose:** Calls FTP command.

**Use case.** In a vendor SFTP drop that still has no API, drop **Invoke FTP command** on the canvas. Calls FTP command.

**Demonstration.**

```text
**Invoke FTP command**
- FTP connection: `%FTPConnection%`
- FTP command: `INV-1042`
- Valid reply code(s): `INV-1042`
Produces:
- `%ReplyCode%` (Text value)
- `%ReplyText%` (Text value)
```

**Analogy.** One tool in that kit: a loading dock: open the gate, drop pallets, close the gate.

**In combination.** Open FTP or secure FTP connection, transfer, Close connection.

### List FTP directory

- **Id:** `ftp/list-ftp-directory`
- **Kind:** native-action
- **Purpose:** Lists FTP directory.

**Use case.** In a vendor SFTP drop that still has no API, drop **List FTP directory** on the canvas. Lists FTP directory.

**Demonstration.**

```text
**List FTP directory**
- Connection: `%FTPConnection%`
- Path: `C:\RPA\Invoices\INV-1042.pdf`
Produces:
- `%Directories%` (List of FTP directories)
- `%Files%` (List of FTP files)
```

**Analogy.** One tool in that kit: a loading dock: open the gate, drop pallets, close the gate.

**In combination.** Open FTP or secure FTP connection, transfer, Close connection.

### Open FTP connection

- **Id:** `ftp/open-ftp-connection`
- **Kind:** native-action
- **Purpose:** Opens FTP connection.

**Use case.** In a vendor SFTP drop that still has no API, drop **Open FTP connection** on the canvas. Opens FTP connection.

**Demonstration.**

```text
**Open FTP connection**
- Host: `INV-1042`
- Port: `21`
- Active mode: `False`
- Username: `CONTOSO\rpa.bot`
- Password: `%Credential.Password%  (sensitive)`
- Timeout: `30`
Produces:
- `%FTPConnection%` (FTP connection)
```

**Analogy.** Unlocking the room before you work. Same family as: a loading dock: open the gate, drop pallets, close the gate.

**In combination.** Open FTP or secure FTP connection, transfer, Close connection. Keep the produced instance/connection and pass it into every later action in this module.

### Open secure FTP connection

- **Id:** `ftp/open-secure-ftp-connection`
- **Kind:** native-action
- **Purpose:** Opens secure FTP connection.

**Use case.** In a vendor SFTP drop that still has no API, drop **Open secure FTP connection** on the canvas. Opens secure FTP connection.

**Demonstration.**

```text
**Open secure FTP connection**
- Host: `INV-1042`
- Port: `22`
- Active mode: `True`
- Secure FTP Protocol: `SFTP`
- Authentication method: `Username and password`
- User name: `CONTOSO\rpa.bot`
- Password: `%Credential.Password%  (sensitive)`
- Path to private key: `C:\RPA\Invoices\INV-1042.pdf`
- … 2 more parameter(s) in the action modal
Produces:
- `%SftpConnection%` (FTP connection)
```

**Analogy.** Unlocking the room before you work. Same family as: a loading dock: open the gate, drop pallets, close the gate.

**In combination.** Open FTP or secure FTP connection, transfer, Close connection. Keep the produced instance/connection and pass it into every later action in this module.

### Rename FTP File

- **Id:** `ftp/rename-ftp-file`
- **Kind:** native-action
- **Purpose:** Renames FTP File.

**Use case.** In a vendor SFTP drop that still has no API, drop **Rename FTP File** on the canvas. Renames FTP File.

**Demonstration.**

```text
**Rename FTP File**
- FTP connection: `%FTPConnection%`
- File to rename: `C:\RPA\Invoices\INV-1042.pdf`
- New file name: `C:\RPA\Invoices\INV-1042.pdf`
```

**Analogy.** One tool in that kit: a loading dock: open the gate, drop pallets, close the gate.

**In combination.** Open FTP or secure FTP connection, transfer, Close connection.

### Synchronize directories

- **Id:** `ftp/synchronize-directories`
- **Kind:** native-action
- **Purpose:** Synchronize the files and subdirectories of a given Folder with a given remote FTP directory.

**Use case.** In a vendor SFTP drop that still has no API, drop **Synchronize directories** on the canvas. Synchronize the files and subdirectories of a given Folder with a given remote FTP directory.

**Demonstration.**

```text
**Synchronize directories**
- FTP connection: `%FTPConnection%`
- Synchronization direction: `Remote -> local (Download)`
- Files to sync: `C:\RPA\Invoices\INV-1042.pdf`
- File filter: `*.pdf`
- Local folder: `C:\RPA\Invoices`
- FTP directory: `C:\RPA\Invoices`
- Delete if source is absent: `False`
- Include subdirectories: `True`
- … 3 more parameter(s) in the action modal
Produces:
- `%FtpFilesAdded%` (List of FTP files)
- `%FtpFilesModified%` (List of FTP files)
- `%FtpFilesDeleted%` (List of FTP files)
- `%FilesAdded%` (List of Files)
- `%FilesModified%` (List of Files)
- `%FilesDeleted%` (List of Files)
```

**Analogy.** One tool in that kit: a loading dock: open the gate, drop pallets, close the gate.

**In combination.** Open FTP or secure FTP connection, transfer, Close connection.

### Upload File(s) to FTP

- **Id:** `ftp/upload-file-s-to-ftp`
- **Kind:** native-action
- **Purpose:** Uploads file(s) to FTP.

**Use case.** In a vendor SFTP drop that still has no API, drop **Upload File(s) to FTP** on the canvas. Uploads file(s) to FTP.

**Demonstration.**

```text
**Upload File(s) to FTP**
- FTP connection: `%FTPConnection%`
- File(s) to upload: `%Files%`
- Remote location: `INV-1042`
- Transfer type: `Auto`
- If file exists: `C:\RPA\Invoices\INV-1042.pdf`
```

**Analogy.** One tool in that kit: a loading dock: open the gate, drop pallets, close the gate.

**In combination.** Open FTP or secure FTP connection, transfer, Close connection.

### Upload folder(s) to FTP

- **Id:** `ftp/upload-folder-s-to-ftp`
- **Kind:** native-action
- **Purpose:** Uploads folder(s) to FTP.

**Use case.** In a vendor SFTP drop that still has no API, drop **Upload folder(s) to FTP** on the canvas. Uploads folder(s) to FTP.

**Demonstration.**

```text
**Upload folder(s) to FTP**
- FTP connection: `%FTPConnection%`
- Folder(s) to upload: `%Files%`
- Remote location: `INV-1042`
```

**Analogy.** One tool in that kit: a loading dock: open the gate, drop pallets, close the gate.

**In combination.** Open FTP or secure FTP connection, transfer, Close connection.
