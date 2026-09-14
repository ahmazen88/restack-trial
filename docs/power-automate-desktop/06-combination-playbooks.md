# Combination playbooks

Single actions rarely finish a business job. These playbooks show **how functions work together**: the use case, the analogy for the whole flow, and a demonstration built from real PAD modules.

Replace Contoso paths, UI elements, and mailboxes with yours. Keep Launch/Close pairs and convert file ↔ binary around cloud connectors.

## 1. Invoice PDF in Outlook → Excel log → archive folder

**Use case.** AP receives vendor PDFs in Outlook. The bot logs invoice numbers and stores the file.

**Analogy.** A mail clerk opens envelopes, writes a line in a ledger, and drops the paper in a dated drawer.

**Demonstration.**

1. **Launch Outlook** → `%OutlookInstance%`
2. **Retrieve email messages from Outlook** (unread, has attachment, folder Inbox)
3. **For each** `%RetrievedEmails%`
4. **Save Outlook email messages** attachments to `C:\RPA\Invoices\Inbox`
5. **Get files in folder** `*.pdf`
6. **For each** file:
   - **Extract text from PDF**
   - **Parse text** for `INV-\d+`
   - **Launch Excel** `C:\RPA\Close\InvoiceLog.xlsx`
   - **Get first free column/row from Excel worksheet**
   - **Write to Excel worksheet** (number, date, file name)
   - **Save Excel** / **Close Excel**
   - **Move file(s)** to `C:\RPA\Invoices\Done\%CurrentDate%\`
7. **Process email messages in Outlook** (mark read / move to Processed)
8. **Close Outlook**

**Functions in combination.** Outlook + File/Folder + PDF + Text + Excel + Loops + Date time.

---

## 2. Watch folder of CSVs → data table → filtered Excel

**Use case.** Stores drop daily sales CSVs. Finance wants only rows where Amount > 0.

**Analogy.** Emptying an inbox tray, copying good lines into a clean notebook, throwing out blanks.

**Demonstration.**

1. **Get current date and time**
2. **If folder exists** `C:\RPA\Drop\Sales` (else **Create folder**)
3. **Get files in folder** `*.csv`
4. **If** `%Files.Count% = 0` → **Stop flow** (success)
5. **Create new data table** (headers Date, Store, Amount)
6. **For each** `%Files%`
   - **Read from CSV file** → `%CsvData%`
   - **Join data tables** or **For each** row + **If** `%CurrentRow['Amount']% > 0` + **Insert row into data table**
7. **Launch Excel** (new document)
8. **Write to Excel worksheet** `%CombinedTable%`
9. **Save Excel** as `C:\RPA\Out\sales-%Date%.xlsx`
10. **Close Excel**
11. **Move file(s)** originals to `C:\RPA\Drop\Sales\Archive`

**Functions in combination.** Folder + File + Variables (data table) + Conditionals + Loops + Excel.

---

## 3. Web portal extract → CSV → close browser

**Use case.** A vendor portal has no API. The bot logs in, pulls a table, and leaves.

**Analogy.** A clerk sits at Chrome, waits for the page, copies the printed table, logs off.

**Demonstration.**

1. **Get credential** (`VendorPortal`)
2. **Launch new Chrome** `https://vendor.example/login` → `%Browser%`
3. **Wait for web page content** (login button UI element)
4. **Populate text field on web page** (user / password from credential)
5. **Press button on web page** (Sign in)
6. **Wait for web page content** (Orders heading)
7. **Extract data from web page** (table → `%Orders%`)
8. **Write to CSV file** `C:\RPA\Out\orders.csv`
9. **Close web browser**

**On error** (block around 2–8): **Take screenshot**, **Log message** Error, **Display message** if attended.

**Functions in combination.** Secret variables + Browser automation + File + Workstation + Logging + Flow control.

---

## 4. Desktop ERP form fill (UI automation)

**Use case.** Line-of-business Windows app with no API. Post a batch of rows from Excel.

**Analogy.** A trained operator reading a spreadsheet and typing into the same screens as always.

**Demonstration.**

1. **Launch Excel** / **Read from Excel worksheet** → `%Batch%`
2. **Run application** `C:\Apps\ERP.exe`
3. **Wait for window** (title contains ERP)
4. **Get window** → `%ERPWindow%`
5. **For each** `%Batch%`
   - **Focus window**
   - **Populate text field in window** (Account, Amount, Date from `%CurrentRow%`)
   - **Click UI element in window** (Post)
   - **Wait for window content** (success status)
6. **Close window**
7. **Close Excel**

If a control has no selector: **Send keys** / **Move mouse to image** as a fallback, still inside **Block Input** for unattended runs.

**Functions in combination.** Excel + System + UI automation + Loops + Mouse and keyboard.

---

## 5. Work queue producer and consumer

**Use case.** Hundreds of cases. Several unattended machines should share the pile.

**Analogy.** A ticket dispenser at a bakery: one machine takes the next ticket, bakes, marks the ticket done or hands it back.

**Producer (Main on a scheduler):**

1. **Read from CSV file** or **List rows from selected environment**
2. **Add multiple work queue items** (data table of case ids)

**Consumer (machine group):**

1. **Process work queue items**
2. Nested: do the business steps (Excel, UI, HTTP)
3. **Update work queue item** (Processed / generic exception)
4. On failure: **Requeue item with delay** or set business exception notes

**Functions in combination.** Work queues + whatever native module does the real work + Logging.

---

## 6. HTTP JSON → custom object → Excel

**Use case.** The system of record is an API. No UI.

**Analogy.** Phoning the warehouse instead of walking the aisles, then copying the answer into the ledger.

**Demonstration.**

1. **Get credential** or **Retrieve environment variable** (base URL)
2. **Invoke web service** `GET https://api.contoso.example/v1/invoices`
3. **Convert JSON to custom object** `%WebServiceResponse%` → `%Payload%`
4. **Set variable** / data table from `%Payload['items']%` (or **Run Power Fx expression** `=Table(...)`)
5. **Launch Excel** / **Write to Excel worksheet**
6. **Save Excel** / **Close Excel**

**Functions in combination.** HTTP + Variables (JSON) + Excel + Environment / credentials.

---

## 7. SharePoint download → local Excel → upload result

**Use case.** Source file lives in a library. Excel.exe still does the heavy reshape.

**Analogy.** Borrow a binder from the library, work at your desk, return a new copy.

**Demonstration.**

1. **Get file content using path** (SharePoint) → binary
2. **Convert binary data to file** `C:\RPA\Temp\source.xlsx`
3. **Launch Excel** that local path
4. Native Excel reshape (**Filter cells**, **Get first free column/row**, **Write to Excel worksheet**)
5. **Save Excel** / **Close Excel**
6. **Convert file to binary data**
7. **Create file** or **Update file** on SharePoint

**Functions in combination.** SharePoint cloud + File binary converters + Excel.

---

## 8. Controlled failure: On block error + email + screenshot

**Use case.** Unattended close must not die silently, and must not leave Excel locked.

**Analogy.** A safety net, a photo of the accident, and a call to the supervisor.

**Demonstration.**

1. **On block error** (continue / go to label `Cleanup`)
2. Nested:
   - **Launch Excel**
   - (business actions)
3. **End**
4. Label `Cleanup`:
   - **Get last error**
   - **Take screenshot**
   - **Log message** Error `%LastError%`
   - **Send email through Outlook** or **Send an email (V2)** to AP
   - **Close Excel** if instance exists
5. **Stop flow** (error) or continue

**Functions in combination.** Flow control + Workstation + Logging + Outlook or Office 365 Outlook + Excel.

---

## 9. Subflows: Extract / Transform / Load

**Use case.** One flow is too long to debug as a single Main tab.

**Analogy.** Three rooms in a workshop. Main only walks you from room to room.

**Demonstration.**

- **Main:** **Run subflow** `Extract` → **Run subflow** `Transform` → **Run subflow** `Load`
- **Extract:** Outlook/File/HTTP, produces `%RawTable%` (output variable)
- **Transform:** Variables data table + Text + Date time
- **Load:** Excel or Dataverse **Add a new row to selected environment**

Pass values as **input/output variables** or flow variables. Use **Exit subflow** for an early return.

**Functions in combination.** Flow control (Run subflow) + any modules inside the rooms.

---

## 10. Attended exception: person picks the file

**Use case.** The path changes every run and a human is at the PC.

**Analogy.** Tapping a coworker and asking “which pack is today’s?”

**Demonstration.**

1. **Display select file dialog** filter `*.xlsx`
2. **If** `%SelectedFile%` is empty → **Stop flow**
3. **Launch Excel** `%SelectedFile%`
4. (process)
5. **Display message** “Posted %RowCount% rows.” Yes/No to open the log folder
6. **If** Yes → **Open** folder with **Run application** `explorer.exe`

**Functions in combination.** Message boxes + Conditionals + Excel + System.

---

## 11. UI first, OCR fallback

**Use case.** Most days the status label is in the UI tree. On theme changes it is only pixels.

**Analogy.** Ask the cashier the price; if they do not answer, read the window sign with your eyes.

**Demonstration.**

1. **If window contains** UI element StatusLabel
   - **Get details of a UI element in window**
2. **Else**
   - **If text on screen (OCR)** `Posted`
   - **Extract text with OCR**
3. **If** neither → **Throw custom error** `Status not found`

**Functions in combination.** UI automation + OCR + Conditionals + Flow control.

---

## 12. SAP posting from Excel

**Use case.** Journal lines in Excel must become an SAP document.

**Analogy.** Reading a paper journal and typing it into the green-screen transaction the accountant always uses.

**Demonstration.**

1. **Launch Excel** / **Read from Excel worksheet**
2. **Launch SAP** / **Start SAP transaction** `FB50`
3. **For each** row:
   - **Populate SAP text field in element**
   - **Click SAP UI element** (Enter)
4. **End SAP transaction**
5. **Close SAP connection**
6. **Write to Excel worksheet** (document number) / **Close Excel**

**Functions in combination.** Excel + SAP automation + Loops.

---

## 13. HR joiner row → Active Directory user

**Use case.** A starter spreadsheet should create the AD account.

**Analogy.** Reading the new-hire form and cutting a building badge.

**Demonstration.**

1. **Read from Excel worksheet** (Joiners sheet)
2. **Connect to server** (AD)
3. **For each** row:
   - **If** `%CurrentRow['Status']% = 'Ready'`
   - **Create user** (name, UPN, OU from columns)
   - **Modify group** (add to App-Users)
   - **Write to Excel worksheet** Status = Created
4. **Close connection**
5. **Save Excel** / **Close Excel**

**Functions in combination.** Excel + Active Directory + Conditionals + Loops.

---

## 14. Test pack around a child flow

**Use case.** You changed Extract and want a red/green check.

**Analogy.** A fire drill with an answer key.

**Demonstration.**

1. **Set variable** expected count `12`
2. **Test a desktop flow** `AP-Extract-Invoices` with sample inputs
3. **Assert** `%OutputCount% = %Expected%` message `Extract count mismatch`

Run from the designer test tooling. Keep test data under `C:\RPA\Fixtures`.

**Functions in combination.** Testing + Variables + Run flow.

---

## 15. Power Fx reshape, then classic Excel write

**Use case.** Flow is Power Fx–enabled. You want Filter/Sum in formulas, then still use Excel.exe.

**Analogy.** A calculator tape (Power Fx) clipped to the ledger (Excel actions).

**Demonstration.**

1. **Run Power Fx expression** `=Filter(Orders, Amount > 0)`
2. **Run Power Fx expression** `=Sum(Filtered, Amount)`
3. **Launch Excel**
4. **Write to Excel worksheet** the filtered table and the total
5. **Close Excel**

Do not mix `%Orders[0]%` in this flow. Use `=Index(Orders, 1)`.

**Functions in combination.** Variables (Run Power Fx expression) + Power Fx Filter/Sum + Excel.

---

## 16. Teams alert when the close bot finishes

**Use case.** Nightly unattended run should ping Finance.

**Analogy.** Leaning into the team room and saying “the ledger is on the shelf.”

**Demonstration.**

1. (playbook 1 or 2 body)
2. **If** success → **Post message in a chat or channel** “Close P9 posted %RowCount% invoices.”
3. **Else** → **Post message** with `%LastError%` and screenshot path

**Functions in combination.** Native close steps + Microsoft Teams cloud + Flow control.

---

## 17. Merge daily PDFs and send through Office 365 Outlook

**Use case.** Five plant PDFs must go out as one attachment. No local Outlook.

**Analogy.** Stapling five photocopies and handing one pack to webmail.

**Demonstration.**

1. **Get files in folder** `C:\RPA\Plant\*.pdf`
2. **Merge PDF files** → `C:\RPA\Out\daily.pdf`
3. **Convert file to binary data**
4. **Send an email (V2)** To `plant-ops@contoso.example`, attachment Name `daily.pdf`, ContentBytes `%BinaryData%`

**Functions in combination.** Folder + PDF + File (binary) + Office 365 Outlook cloud.

---

## 18. Clipboard bridge between two stubborn apps

**Use case.** App A copies a reference; App B only accepts paste.

**Analogy.** A sticky note walked down the hall.

**Demonstration.**

1. **Get window** (App A) / **Click UI element** Copy
2. **Get clipboard text** → `%Ref%`
3. **Get window** (App B) / **Focus text field in window**
4. **Set clipboard Text** `%Ref%` (or **Populate text field** if paste is unsafe)
5. **Send keys** `Ctrl+V` only if the field cannot be populated
6. **Clear clipboard contents**

**Functions in combination.** UI automation + Clipboard + Mouse and keyboard.

---

## Combination cheat sheet

| Job | Core modules | Glue |
| --- | --- | --- |
| Mail to ledger | Outlook, PDF, Excel, Folder | For each, Parse text |
| API to ledger | HTTP, Variables, Excel | JSON custom object |
| Website to file | Browser, File | Wait for web page content |
| Windows app | UI automation, Excel | Wait for window, On block error |
| Cloud file + Excel.exe | SharePoint/OneDrive, File, Excel | Binary converters |
| Many machines | Work queues | Update work queue item |
| Human in the loop | Message boxes | If on button pressed |
| Secret | Get credential / CyberArk | Sensitive variables |
| Nightly notify | Teams or Outlook | Get last error, screenshot |

For per-function use case, demonstration, and analogy, open [how-it-works/README.md](how-it-works/README.md).
