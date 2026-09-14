# Data-type properties

Properties are fields you read with dot notation. They do not change the original value.

Classic:

```text
%Files.Count%
%InvoiceDate.Year%
%Attachment.NameWithoutExtension%
```

Power Fx uses the same names where the type exists, with record/table syntax instead of `%`.

Official reference: [Variable data type properties](https://learn.microsoft.com/en-us/power-automate/desktop-flows/datatype-properties).

## Text

| Property | Type | Meaning |
|---|---|---|
| `Length` | Number | Character count. |
| `isEmpty` | Boolean | True when the string has no characters. |
| `ToUpper` | Text | Uppercase copy. |
| `ToLower` | Text | Lowercase copy. |
| `Trimmed` | Text | Copy without leading/trailing whitespace. |

```text
%CustomerName.ToUpper%
```

## Datetime

| Property | Type | Meaning |
|---|---|---|
| `Year` | Number | Year part. |
| `Month` | Number | Month 1–12. |
| `Day` | Number | Day of month. |
| `DayOfWeek` | Text | Weekday name. |
| `DayOfYear` | Number | 1–365/366. |
| `Hour` | Number | 0–23. |
| `Minute` | Number | 0–59. |
| `Second` | Number | 0–59. |

```text
%CurrentDateTime.Month%
```

## List

| Property | Type | Meaning |
|---|---|---|
| `Count` | Number | Number of items. |

## File

| Property | Type | Meaning |
|---|---|---|
| `FullName` | Text | Full path. |
| `RootPath` | Text | Drive root (`C:\`). |
| `Directory` | Text | Parent folder path. |
| `Name` | Text | File name with extension. |
| `NameWithoutExtension` | Text | File name without extension. |
| `Extension` | Text | Extension including dot in most cases. |
| `Size` | Number | Size in bytes. |
| `CreationTime` | Datetime | Created. |
| `LastAccessed` | Datetime | Last access. |
| `LastModified` | Datetime | Last write. |
| `IsHidden` | Boolean | Hidden attribute. |
| `IsSystem` | Boolean | System attribute. |
| `IsReadOnly` | Boolean | Read-only attribute. |
| `IsArchive` | Boolean | Archive attribute. |
| `Exists` | Boolean | File is present on disk. |
| `isEmpty` | Boolean | Zero-byte file. |

```text
%DownloadedFile.NameWithoutExtension% + '_' + TextId + DownloadedFile.Extension
```

(In classic mode concatenate with `%DownloadedFile.NameWithoutExtension + '_' + TextId + DownloadedFile.Extension%`.)

## Folder

| Property | Type | Meaning |
|---|---|---|
| `FullName` | Text | Full path. |
| `RootPath` | Text | Drive root. |
| `Parent` | Text | Parent directory. |
| `Name` | Text | Folder name. |
| `CreationTime` | Datetime | Created. |
| `LastModified` | Datetime | Last write. |
| `IsHidden` | Boolean | Hidden attribute. |
| `Exists` | Boolean | Folder is present. |
| `isEmpty` | Boolean | No files or subfolders. |
| `FilesCount` | Number | Files in the folder (not recursive). |
| `FoldersCount` | Number | Immediate subfolders. |

## Mail message (IMAP / POP)

| Property | Meaning |
|---|---|
| `MailFolder` | Source folder name. |
| `Uid` | Unique id. |
| `From` | Sender. |
| `To` | Recipient list. |
| `Cc` | Cc list. |
| `Date` | Sent datetime. |
| `Subject` | Subject. |
| `Body` | Body (HTML or text). |
| `BodyText` | Plain-text body. |
| `Attachments` | List of saved attachment files. |

## Exchange connection / Exchange mail

Connection: `ServerAddress`.

Mail adds `ItemId` instead of `Uid`. Other fields match IMAP mail (`From`, `To`, `Cc`, `Date`, `Subject`, `Body`, `BodyText`, `Attachments`, `MailFolder`).

## Outlook mail message

Same shape as Exchange mail, with `EntryId` as the unique id and an extra `Bcc` list.

## FTP file / folder / connection

FTP file: `FullName`, `Directory`, `Name`, `NameWithoutExtension`, `Extension`, `Size`, `LastModified`.

FTP folder: `FullName`, `Parent`, `Name`, `LastModified`.

FTP connection: `Host`, `SecurityProtocol`.

## Datatable

| Property | Meaning |
|---|---|
| `RowsCount` | Number of rows. |
| `Columns` | List of column names. |
| `IsEmpty` | No rows. |
| `ColumnHeadersRow` | Header row as a datarow. |

## Datarow

| Property | Meaning |
|---|---|
| `ColumnsCount` | Number of columns. |
| `ColumnsNames` | Header list. |

## Browser instance

| Property | Meaning |
|---|---|
| `DisplayRectangleX` / `DisplayRectangleY` | Top-left of the window. |
| `Handle` | Window handle. |
| `HtmlDialogs` | Page dialogs, if any. |
| `IsAlive` | Browser process still running. |

## Window / Excel instances

`Handle` on both. Excel instance is the workbook/application handle you pass into every later Excel action.

## SQL connection

| Property | Meaning |
|---|---|
| `ConnectionString` | String used to open the connection. |
| `IsClosed` | Connection no longer open. |

## PDF table info

| Property | Meaning |
|---|---|
| `DataTable` | Extracted table. |
| `TableStartingPage` | First page of the table. |
| `TableEndingPage` | Last page of the table. |
| `TableOrderInPage` | Order of this table on the page. |

## CMD session

`IsAlive`, `ProcessId`.

## Credential

`Username`, `Password` (sensitive).

## Terminal session

`IsTerminated`.

## XML node

| Property | Meaning |
|---|---|
| `Children` | Child nodes. |
| `InnerText` | Concatenated text. |
| `InnerXML` | Inner markup. |
| `Name` | Node name. |
| `OuterXML` | Node including its own tags. |
| `Parent` | Parent node. |
| `Value` | Node value. |

## Active Directory

Entry: `LdapPath`.

Group info: `Description`, `DisplayName`, `Members`, `Name`.

User info: `City`, `Company`, `Country`, `Department`, `Email`, `Extension`, `FirstName`, `Initials`, `LastName`, `PostalCode`, `State`, `StreetAddress`, `TelephoneNumber`, `Title`.

## AWS EBS snapshot

`DataEncryptionKeyId`, `Description`, `Encrypted`, `KmsKeyId`, `OwnerAlias`, `OwnerId`, `Progress`, `SnapshotId`, `StartTime`, `State`, `StateMessage`, `Tags`, `VolumeId`, `VolumeSize`.

## AWS EBS volume

`Attachments`, `AvailabilityZone`, `CreateTime`, `Encrypted`, `FastRestored`, `Iops`, `KmsKeyId`, `MultiAttachEnabled`, `OutpostArn`, `Size`, `SnapshotId`, `State`, `Tags`, `VolumeId`, `VolumeType`.

## Azure managed disk

`AvailabilityZones`, `Configuration`, `Encrypted`, `IopsSLimit`, `IsAttachedToVirtualMachine`, `OperationSystem`, `SizeInGB`, `State`, `ThroughputLimit`, `TimeCreated`, `Type`, `VirtualMachine`, `ResourceGroup`, `Id`, `Location`, `Name`, `SubscriptionId`, `Tags`.

## Azure resource group

`ProvisioningState`, `Id`, `Location`, `Name`, `SubscriptionId`, `Tags`.

## Azure snapshot

`CreationSourceId`, `CreationSourceType`, `OperationSystem`, `SizeInGB`, `StorageAccountType`, `TimeCreated`, `ResourceGroup`, `id`, `Location`, `Name`, `SubscriptionId`, `Tags`.

## Error

| Property | Meaning |
|---|---|
| `ActionIndex` | 0-based action index that failed. |
| `ActionName` | Action display name. |
| `ErrorDetails` | Detail payload. |
| `Location` | Subflow + action location text. |
| `Message` | Error message. |
| `SubflowName` | Subflow that failed. |

```text
%LastError.Message%
%LastError.ActionName%
```
