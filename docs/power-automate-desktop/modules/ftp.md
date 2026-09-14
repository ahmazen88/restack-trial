# FTP

Open FTP/SFTP sessions and transfer files and folders.

This page documents every **native action** in this group (15 items).

## Actions

### Change working directory

- **Inventory id:** `ftp/change-working-directory`
- **Kind:** native-action
- **Purpose:** This action sets the current working directory for an FTP connection.
- **Key inputs:** `Connection` (FTP connection); `Set working directory to` (Text value)
- **Produces:** None listed
- **Exceptions:** `Not connected error`; `Directory doesn't exist error`; `Can't change working directory error`
- **Microsoft Learn:** [Change working directory](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#changeworkingdirectory)

### Close connection

- **Inventory id:** `ftp/close-connection`
- **Kind:** native-action
- **Purpose:** Closes connection.
- **Key inputs:** `Connection` (FTP connection)
- **Produces:** None listed
- **Exceptions:** `Not connected error`
- **Microsoft Learn:** [Close connection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#closeconnection)

### Create FTP directory

- **Inventory id:** `ftp/create-ftp-directory`
- **Kind:** native-action
- **Purpose:** Creates FTP directory.
- **Key inputs:** `FTP connection` (FTP connection); `New directory` (FTP directory)
- **Produces:** None listed
- **Exceptions:** `Access denied error`; `File exists error`; `Create directory error`; `Directory doesn't exist error`; `Not connected error`
- **Microsoft Learn:** [Create FTP directory](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#createdirectory)

### Delete FTP directory

- **Inventory id:** `ftp/delete-ftp-directory`
- **Kind:** native-action
- **Purpose:** Deletes FTP directory.
- **Key inputs:** `FTP connection` (FTP connection); `Directory to delete` (FTP directory)
- **Produces:** None listed
- **Exceptions:** `Delete directory error`; `Remote directory doesn't exist error`; `Working directory change error`; `Not connected error`
- **Microsoft Learn:** [Delete FTP directory](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#deletedirectory)

### Delete FTP file

- **Inventory id:** `ftp/delete-ftp-file`
- **Kind:** native-action
- **Purpose:** Deletes FTP file.
- **Key inputs:** `FTP connection` (FTP connection); `Files to delete` (List of FTP files)
- **Produces:** None listed
- **Exceptions:** `Not connected error`; `File not found error`; `Can't delete file error`
- **Microsoft Learn:** [Delete FTP file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#deletefiles)

### Download file(s) from FTP

- **Inventory id:** `ftp/download-file-s-from-ftp`
- **Kind:** native-action
- **Purpose:** Downloads file(s) from FTP.
- **Key inputs:** `FTP connection` (FTP connection); `Download into folder` (Folder); `File(s) to download` (List of FTP files); `Transfer type` (Auto, Binary, ASCII); `If file exists` (Overwrite, Do not download, Download with unique name)
- **Produces:** None listed
- **Exceptions:** `Not connected error`; `Remote file doesn't exist error`; `Directory doesn't exist error`; `FTP connection aborted error`; `Can't download file error`
- **Microsoft Learn:** [Download file(s) from FTP](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#downloadfiles)

### Download folder(s) from FTP

- **Inventory id:** `ftp/download-folder-s-from-ftp`
- **Kind:** native-action
- **Purpose:** Downloads folder(s) from FTP.
- **Key inputs:** `FTP connection` (FTP connection); `Folder(s) to download` (List of FTP directories); `Download into local folder` (Folder)
- **Produces:** None listed
- **Exceptions:** `Not connected error`; `Remote directory doesn't exist error`; `Directory doesn't exist error`; `FTP connection aborted error`; `Can't download directory error`
- **Microsoft Learn:** [Download folder(s) from FTP](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#downloadfolders)

### Invoke FTP command

- **Inventory id:** `ftp/invoke-ftp-command`
- **Kind:** native-action
- **Purpose:** Calls FTP command.
- **Key inputs:** `FTP connection` (FTP connection); `FTP command` (Text value); `Valid reply code(s)` (Text value; optional)
- **Produces:** `ReplyCode` (Text value); `ReplyText` (Text value)
- **Exceptions:** `Invoke command error`; `Not connected error`
- **Microsoft Learn:** [Invoke FTP command](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#invokecommand)

### List FTP directory

- **Inventory id:** `ftp/list-ftp-directory`
- **Kind:** native-action
- **Purpose:** Lists FTP directory.
- **Key inputs:** `Connection` (FTP connection); `Path` (Text value; optional)
- **Produces:** `Directories` (List of FTP directories); `Files` (List of FTP files)
- **Exceptions:** `Listing error`; `Not connected error`; `Directory doesn't exist error`
- **Microsoft Learn:** [List FTP directory](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#listdirectory)

### Open FTP connection

- **Inventory id:** `ftp/open-ftp-connection`
- **Kind:** native-action
- **Purpose:** Opens FTP connection.
- **Key inputs:** `Host` (Text value); `Port` (Numeric value; optional); `Active mode` (Boolean value); `Username` (Text value); `Password` (Direct encrypted input or Text value; optional); `Timeout` (Numeric value; optional)
- **Produces:** `FTPConnection` (FTP connection)
- **Exceptions:** `Login failure error`; `Connection error`
- **Microsoft Learn:** [Open FTP connection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#openconnection)

### Open secure FTP connection

- **Inventory id:** `ftp/open-secure-ftp-connection`
- **Kind:** native-action
- **Purpose:** Opens secure FTP connection.
- **Key inputs:** `Host` (Text value); `Port` (Numeric value; optional); `Active mode` (Boolean value); `Secure FTP Protocol` (SFTP, FTPS explicit, FTPS implicit); `Authentication method` (Username and password, Private key, Private key and passphrase); `User name` (Text value); `Password` (Direct encrypted input or Text value; optional); `Path to private key` (Text value); `Private key pass phrase` (Direct encrypted input or Text value; optional); `Timeout` (Numeric value; optional)
- **Produces:** `SftpConnection` (FTP connection)
- **Exceptions:** `Login failure error`; `Connection error`
- **Microsoft Learn:** [Open secure FTP connection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#opensecureconnection)

### Rename FTP File

- **Inventory id:** `ftp/rename-ftp-file`
- **Kind:** native-action
- **Purpose:** Renames FTP File.
- **Key inputs:** `FTP connection` (FTP connection); `File to rename` (FTP file); `New file name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Not connected error`; `Can't rename file error`; `File not found error`
- **Microsoft Learn:** [Rename FTP File](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#renamefile)

### Synchronize directories

- **Inventory id:** `ftp/synchronize-directories`
- **Kind:** native-action
- **Purpose:** Synchronize the files and subdirectories of a given Folder with a given remote FTP directory.
- **Key inputs:** `FTP connection` (FTP connection); `Synchronization direction` (Remote -> local (Download), Local -> remote (Upload)); `Files to sync` (All files, Only files matching the file filter, Only files not matching the file filter); `File filter` (Text value); `Local folder` (Folder); `FTP directory` (FTP directory; optional); `Delete if source is absent` (Boolean value); `Include subdirectories` (Boolean value); `Time difference in hours` (Numeric value; optional); `Time difference in minutes` (Numeric value; optional); `Time difference ahead` (Boolean value)
- **Produces:** `FtpFilesAdded` (List of FTP files); `FtpFilesModified` (List of FTP files); `FtpFilesDeleted` (List of FTP files); `FilesAdded` (List of Files); `FilesModified` (List of Files); `FilesDeleted` (List of Files)
- **Exceptions:** `Listing error`; `Not connected error`; `File not found error`; `FTP connection aborted error`; `Upload file error`; `Remote file doesn't exist error`; `Can't download file error`; `Delete directory error`; `Synchronization failed error`
- **Microsoft Learn:** [Synchronize directories](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#synchronizedirectoryaction)

### Upload File(s) to FTP

- **Inventory id:** `ftp/upload-file-s-to-ftp`
- **Kind:** native-action
- **Purpose:** Uploads file(s) to FTP.
- **Key inputs:** `FTP connection` (FTP connection); `File(s) to upload` (List of Files); `Remote location` (Text value; optional); `Transfer type` (Auto, Binary, ASCII); `If file exists` (Overwrite, Do not download, Download with unique name)
- **Produces:** None listed
- **Exceptions:** `Not connected error`; `File not found error`; `FTP connection aborted error`; `Upload file error`
- **Microsoft Learn:** [Upload File(s) to FTP](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#uploadfiles)

### Upload folder(s) to FTP

- **Inventory id:** `ftp/upload-folder-s-to-ftp`
- **Kind:** native-action
- **Purpose:** Uploads folder(s) to FTP.
- **Key inputs:** `FTP connection` (FTP connection); `Folder(s) to upload` (List of Folders); `Remote location` (Text value)
- **Produces:** None listed
- **Exceptions:** `Not connected error`; `Remote directory doesn't exist error`; `FTP connection aborted error`; `Upload directory error`
- **Microsoft Learn:** [Upload folder(s) to FTP](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ftp#uploadfolders)
