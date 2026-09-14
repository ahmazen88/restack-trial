# Variable data types

PAD assigns a type from the value you store. Some types appear everywhere (text, number). Others exist only after a specific action (Excel instance, OCR engine).

Use this page with [Variables actions](modules/variables.md).

## Simple types

### Text value

Any string: paths, HTML, JSON text, file contents. Create with **Set variable** and a literal, or consume an action output.

### Numeric value

The only type that participates in math (`%Counter + 1%`). Create with a bare number in **Set variable**.

### Boolean value

`True` or `False`. In classic syntax write `%True%` and `%False%`. Combine with `and`, `or`, `not`.

## Structured types

### List

A zero-based collection. Create with **Create new list**, or receive one from **Get files in folder**, **Split text**, and similar. Index: `%Names[0]%`. Slice: `%Names[1:3]%` (stop index is exclusive).

### Datatable

Rows and columns. Create with **Create new data table**, **Read from Excel worksheet**, **Execute SQL statement**, or **Extract data from web page**. Cell: `%Table[0][1]%` or `%Table[0]['Amount']%`. A **For each** over a table yields a **datarow**.

### Datarow

One table row. Column by index or header name: `%Row['Amount']%`.

### Custom object

Property map, JSON-friendly. Empty: `%{{ }}%`. Literal: `%{ 'Name': 'Ada', 'Id': 1 }%`. Reserved keywords cannot be property names.

### Connector object

Structured payload from a **cloud connector** operation. Nested properties often hold lists of other connector objects.

### General value

Design-time placeholder when PAD cannot yet prove a type. At runtime it becomes a concrete type.

## Files, dates, secrets

### File / Folder / FileSystemObject

Disk items. `FileSystemObject` is the union type used when an input accepts either.

### Datetime

Date and time. Classic literal: `%d"2026-03-25 14:30:00"%`. Format tokens: `yyyy MM dd HH mm ss ff zzz`.

### SensitiveValue

Masked text (passwords, secret environment variables). Logs and the variables viewer hide the value.

### Credential

Object from **Get credential** (username, password, and related fields).

## Application instances

These exist only after a launch/attach/open action. Pass the same instance into later actions in the group.

| Type | Created by |
| --- | --- |
| Web browser instance | Launch new Chrome / Edge / Firefox / Internet Explorer |
| Window instance | Get window |
| Excel instance | Launch Excel / Attach to running Excel |
| Word instance | Launch Word / Attach to running Word |
| Outlook instance | Launch Outlook |
| Access instance | Launch Access |
| SQL connection | Open SQL connection |
| Exchange connection | Connect to Exchange server |
| FTP connection | Open FTP connection / Open secure FTP connection |
| CMD session | Open CMD session |
| Terminal session | Open terminal session |
| OCR Engine | OCR actions (Windows OCR or Tesseract settings) |
| XML node | Read XML from file |

## Messages and errors

| Type | Created by |
| --- | --- |
| Mail message | Retrieve email messages (IMAP) |
| Outlook mail message | Retrieve email messages from Outlook |
| Exchange mail message | Retrieve Exchange email messages |
| Error | Get last error |
| List of PDF table info | Extract tables from PDF |
| TriggerEventInstanceHandle | UI element event trigger |

## Directory, cloud, and vendor objects

| Type | Module |
| --- | --- |
| Active Directory entry, Group info, Group member, User info | Active Directory |
| EC2 client, instance, volume, snapshot, instance info | AWS |
| Azure client, VM, disk, snapshot, subscription, resource group | Azure |
| FTP file, FTP directory | FTP |

## Indexing rules

| Language | First item |
| --- | --- |
| Classic `%List[0]%` | **0-based** |
| Power Fx `Index(List, 1)` | **1-based** |

## Reserved names

Do not use engine keywords as variable names or custom-object properties (case-insensitive), including: `if`, `else`, `loop`, `for`, `foreach`, `while`, `switch`, `case`, `default`, `set`, `label`, `goto`, `true`, `false`, `not`, `and`, `or`, `input`, `output`, `main`, `function`, `error`, `wait`, `next`, `end`, `mod`, `block`, `call`, `global`.

Full list: [Reserved keywords in desktop flows](https://learn.microsoft.com/en-us/power-automate/desktop-flows/reserved-keywords).
