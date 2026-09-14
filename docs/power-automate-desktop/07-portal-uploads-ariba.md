# Portal uploads like Ariba

You **put invoice PDFs in a folder** and **run the desktop flow**. No mail pull, no SharePoint, no work queue, no PAD trigger, no notification. The folder is the inbox.

The bot then **logs in** to the procurement portal (SAP Business Network / Ariba, or Coupa, Jaggaer, and the like), **attaches each PDF**, **submits**, and **moves the file** to Done.

**Analogy.** A tray on the clerk’s desk. You drop envelopes in the tray. When you say “go,” the clerk badges in, hands each envelope to Accounts Payable, waits for a receipt stamp, and moves the envelope to the done drawer.

Playbook [19](06-combination-playbooks.md#19-ariba-style-portal-upload-drop-pdf-in-a-folder--submit) is the short version.

## Start: the drop folder

| Folder | Role |
| --- | --- |
| `C:\RPA\Ariba\Inbox` | You place `*.pdf` here, then run the flow |
| `C:\RPA\Ariba\Done` | Successful uploads |
| `C:\RPA\Ariba\Failed` | Files that did not submit |

How you start it: **Play** in the PAD console (or Run from the flow designer). The first actions are **Get files in folder**, not a trigger.

1. **If folder exists** `C:\RPA\Ariba\Inbox` (else **Create folder**)
2. **Get files in folder** `C:\RPA\Ariba\Inbox\*.pdf` → `%Pdfs%`
3. **If** `%Pdfs.Count% = 0` → **Stop flow** (nothing to upload)
4. Then login once and **For each** `%CurrentPdf%` in `%Pdfs%`

Name the PDF so the invoice number is obvious, for example `INV-1001.pdf`. **Get file path part** on `%CurrentPdf%` gives `%FileNameNoExtension%` → use that as `%InvoiceNumber%` on the portal. Add PO / date / amount on the page by hand in the recorded fields, or **Extract text from PDF** if those values are printed on the image.

## The two doors for a file

Every Ariba-like Attach control uses one of two doors. After you click Attach, find out which:

| Door | What you see | PAD move |
| --- | --- | --- |
| **A — HTML file input** | A real `<input type="file">` (often hidden behind Browse) | **Populate text field on web page** with the **full path** of `%CurrentPdf%`. Do **not** emulate typing. |
| **B — Windows Open dialog** | Attach / paperclip opens the OS picker (`Open`, `File Upload`, locale titles like `Öffnen`) | **Press button on web page** (Attach) → **Wait for window** → **Populate text field in window** (File name) → **Press button in window** (Open) |

Door B is what most Ariba Attach buttons do. The picker is a **Windows** window. Leave Browser automation and use **UI automation** on that dialog.

Do not use **Display select file dialog** (that asks a person to pick a file — you already dropped it in the folder). Do not use **Run JavaScript function on web page** to set `input.files` (browsers block it).

```text
Place PDFs in Inbox → Run flow → Get files in folder
        │
        ▼
  Click Attach / Browse
        ├─ input[type=file] in DOM?  → Door A: Populate text field on web page
        └─ OS picker appears?        → Door B: Wait for window → File name → Open
```

## Demonstration: folder → stamp

Replace realm URL, UI elements, and folders with yours. Keep Launch/Close pairs.

### 0. Values you set in the flow

| Variable | Example | How |
| --- | --- | --- |
| `%DropFolder%` | `C:\RPA\Ariba\Inbox` | **Set variable** |
| `%PortalUrl%` | `https://contoso.procurement.ariba.com` | **Set variable** (your realm) |
| `%PortalCred%` | username + password | **Get credential** (`AribaSupplier`) |

### 1. Take the PDFs from the tray

1. **Get files in folder** `%DropFolder%` filter `*.pdf`
2. **If** `%Pdfs.Count% = 0` → **Stop flow**
3. **For each** later uses `%CurrentPdf%`. Guard: **Get file path part** → `%FileExtension%` should be `pdf`

### 2. Open the browser once

1. **Launch new Microsoft Edge** or **Launch new Chrome** → `%PortalUrl%`
2. **Wait for web page content** (Sign in, or the home tile)
3. **Populate text field on web page** (user / password from `%PortalCred%`)
4. **Press button on web page** (Sign in)

If MFA appears, complete it yourself on an attended run, then continue. Do not add a notification or a second flow for that.

**Analogy.** Badge at the lobby once. Then walk every envelope from the tray.

### 3. For each PDF: create invoice and attach

Inside **For each** `%Pdfs%`:

1. **Get file path part** → `%InvoiceNumber%` from `%FileNameNoExtension%`
2. Navigate Create Invoice / PO-flip (your tiles)
3. Fill the header fields the portal requires
4. Put the file on the page (Door A or Door B) using `%CurrentPdf%` as the path
5. **Wait for web page content** until the file **name** shows on the attachment list
6. **Press button on web page** Review / Submit
7. **Wait for web page content** (success or error banner)
8. On success: **Get details of element on web page** → `%ConfirmationId%` → **Move file(s)** `%CurrentPdf%` to `C:\RPA\Ariba\Done`
9. On error: **Take screenshot of web page** → **Move file(s)** to `C:\RPA\Ariba\Failed`

**On block error** around the per-file steps so one bad PDF does not stop the rest. Login stays open for the whole **For each**.

**Iframes.** Classic Ariba nests the form in frames. Capture the UI element **from the inner page**. There is no separate “switch iframe” action; the selector is the switch. If Click does nothing, wait for an inner label, then try **Send physical click**.

### 4. Close

After the loop: **Close web browser**.

## Door A and Door B (the attach step)

**Door A**

1. **Wait for web page content** (Attach / Browse)
2. **Populate text field on web page** on the file input, Text = `%CurrentPdf%`, emulate typing **Off**
3. **Wait for web page content** (file name visible)

**Door B** (typical Ariba)

1. **Press button on web page** (Add attachment)
2. **Wait for window** title contains `Open`
3. **Focus window** → **Focus text field in window** (File name)
4. **Populate text field in window** `%CurrentPdf%`
5. **Press button in window** (Open)
6. Wait until that dialog is gone
7. **Wait for web page content** (file name on the list)

Put Door A/B in a subflow `UploadAttachment` that takes `%Browser%` and `%CurrentPdf%` if you reuse it.

## Ariba-shaped gotchas

| Symptom | What to do |
| --- | --- |
| Inbox empty and the flow “does nothing” | That is correct — **Stop flow** when `%Pdfs.Count% = 0` |
| Populate “succeeds” but no file | You filled a visible text box, not `type=file`, or emulate-typing was on |
| Open dialog not found | Record the real window title (locale); **Focus window** before typing the path |
| Path typed into the **page** | Focus never moved to the Open dialog |
| Attach click does nothing | Iframe or overlay — re-capture inside the frame; physical click |
| Duplicate invoice | Move that PDF to Failed; go to the next file |
| DEV vs PROD | Change `%PortalUrl%` in **Set variable**, do not hard-code in ten places |

**SAP GUI is a different playbook.** Posting in SAP ERP (`FB60`, MIRO) uses **SAP automation** ([playbook 12](06-combination-playbooks.md#12-sap-posting-from-excel)). Ariba Network is a **website**.

## Functions in combination

Folder (**Get files in folder**, **Move file(s)**) + File (**Get file path part**) + Browser automation + UI automation (OS Open dialog) + **Get credential** + Loops (**For each**) + **On block error**.

**Not in this flow:** PAD **triggers**, Outlook, SharePoint, work queues, Teams/email notifications, **Display select file dialog**, **Launch new Internet Explorer**.
