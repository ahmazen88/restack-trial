# Portal uploads like Ariba

Procurement portals (SAP Business Network / Ariba, Coupa, Jaggaer, Ivalua, Oracle Supplier Portal, Fieldglass) almost never give AP a clean API for “attach this PDF and submit.” The bot has to **log in, walk a wizard, put a file on the page, wait until the portal admits it has the file, then submit**.

This note is the working pattern for that job. Playbook [19 in the combination set](06-combination-playbooks.md#19-ariba-style-portal-upload-invoice-pdf--submit--confirmation) is the short version. Use this page when you are actually building the flow.

**Analogy for the whole job.** A courier with a sealed envelope. They show a badge at the lobby (login), take the elevator to Accounts Payable (navigate), hand the envelope to the clerk (upload), wait until the clerk stamps a receipt number (confirmation), and only then leave the building (close browser). The hard part is not walking — it is **how that clerk accepts the envelope**.

## The two doors for a file

Every Ariba-like page uses one of two doors. Capture **both** as subflows. Detect which door you are on with **If web page contains** (hidden `input type=file`) versus **If window** (OS Open dialog after Attach).

| Door | What you see | PAD move | Unattended? |
| --- | --- | --- | --- |
| **A — HTML file input** | A real `<input type="file">` in the DOM (often hidden, styled as “Browse”) | **Populate text field on web page** with the **full local path** (`C:\RPA\Ariba\Inbox\INV-1001.pdf`). Do **not** emulate typing. | Yes |
| **B — Windows Open dialog** | Attach / paperclip / “Add attachment” opens the OS picker (`Open`, `File Upload`, locale titles like `Öffnen`) | **Press button on web page** (Attach) → **Wait for window** → **Populate text field in window** (File name) → **Press button in window** (Open) | Yes, if the unattended session has a desktop |
| **Attended pick (not a portal door)** | Human must choose which PDF | **Display select file dialog** | **No** — that action cannot run non-interactively |

Door A is quieter and faster. Door B is what Ariba, Coupa, and most “pretty” dropzones actually do: the visible control is a `<div>` or `<button>`, and the OS dialog is a **Windows** window, not a web element. After you click Attach, **leave Browser automation** and use **UI automation** on that dialog.

Do not use **Run JavaScript function on web page** to set `input.files`. Browsers block that for security. PAD’s own populate-on-file-input works because the browser extension sets the value; injected script does not.

```text
                     ┌─ input[type=file] in DOM? ──► Door A: Populate text field on web page
Click Attach / Browse ─┤
                     └─ OS picker appears? ────────► Door B: Wait for window → File name → Open
```

## Use case (Ariba invoice image)

AP has a PO-backed invoice PDF (from Outlook, a watch folder, or SharePoint). A supplier or shared-services clerk must create the invoice on **SAP Business Network** (classic Ariba Network / Invoice Collaboration), attach the legal image, and keep the confirmation (IR / invoice request id) in Excel.

Same skeleton covers:

- Catalog / CIF / price-file upload
- ASN / ship-notice attachments
- RFP response documents
- Supplier certificates (insurance, tax forms)

Only the navigation and field names change.

## Demonstration: one invoice, start to stamp

Replace realm URL, UI elements, and folders with yours. Keep Launch/Close pairs. File path must exist **on the machine that runs PAD** before Attach.

### 0. Inputs (flow variables)

| Variable | Example | Source |
| --- | --- | --- |
| `%PortalUrl%` | `https://contoso.procurement.ariba.com` | **Retrieve environment variable** (DEV vs PROD realm) |
| `%PortalCred%` | username + password | **Get credential** (`AribaSupplier`) — never plain text |
| `%InvoicePath%` | `C:\RPA\Ariba\Inbox\INV-1001.pdf` | Work queue, Outlook save, or SharePoint download |
| `%PONumber%` | `4500123456` | Excel / queue payload |
| `%InvoiceNumber%` | `INV-1001` | Same |
| `%InvoiceDate%` | `2026-09-14` | Same |
| `%Amount%` | `1250.00` | Same |

If the PDF still lives in SharePoint or Outlook, **get it onto disk first**. Cloud connectors produce binary; **Convert binary data to file** (or **Save Outlook email messages**) before any upload. Portals cannot read `%BinaryData%`.

### 1. Guard the file

1. **If file exists** `%InvoicePath%` — else **Throw custom error** `Invoice image missing`
2. **Get file path part** → `%FileName%`, `%FileExtension%` — extension in `pdf,tif,tiff,jpg,png,xlsx,zip` (match the portal allow-list)
3. Skip empty-looking names. Ariba attachments are often capped (commonly 10–100 MB per file, sometimes a count cap). Fail **before** login if the file is impossible.

Optional: **Extract text from PDF** + **Parse text** to confirm the invoice number in the image matches `%InvoiceNumber%` so you do not attach the wrong envelope.

### 2. Open a real browser (not IE)

1. **Launch new Microsoft Edge** or **Launch new Chrome**
   - Initial URL: `%PortalUrl%`
   - Attach to running browser **only** when you must reuse an SSO cookie / MFA session (attended). Unattended: launch clean, then **Get credential**.
2. **Wait for web page content** (Sign in, or the post-SSO home tile). Timeouts of 60–120 seconds are normal on Ariba.
3. If login fields are present:
   - **Populate text field on web page** (user)
   - **Populate text field on web page** (password from `%PortalCred%`, sensitive)
   - **Press button on web page** (Sign in)
4. MFA / SSO interstitial: **If web page contains** “Approve sign-in” → attended **Display message** “Complete MFA, then OK” or fail unattended with a clear error. Do not spin on a 6-digit box.

**Analogy.** Badge at the lobby. If the guard asks for a second factor, a person has to wave; the courier robot cannot.

### 3. Walk to “create invoice”

Ariba shells change by realm (classic frameset vs Guided Buying vs new Network UI). Record **your** tiles. A typical supplier path:

1. **Wait for web page content** (Inbox / Orders / Invoices tile)
2. **Click link on web page** or **Press button on web page** (Create Invoice / PO-Flip / Non-PO Invoice)
3. **Wait for web page content** (PO number field or invoice header)
4. **Populate text field on web page** `%PONumber%` → search → open the PO
5. Fill header: invoice number, date, amount, tax as required
   - **Set drop-down list value on web page** for currency / tax
   - **Set check box state on web page** for “This is a credit memo” only when it is

**Iframes.** Classic Ariba nests the form in one or more frames. Capture the UI element **from the inner page** (recorder includes the frame in the selector). If Click hits the chrome and does nothing:

- Re-capture inside the frame after the frame has loaded (**Wait for web page content** on an inner label)
- Turn on **Send physical click** on **Click link on web page**
- Last resort: **UI automation** against the browser window (weaker selectors)

There is no separate “switch iframe” action in PAD. The selector is the switch.

### 4. Put the file on the page (the actual upload)

**Door A — file input in the DOM**

1. **Wait for web page content** (Attach / Browse / paperclip)
2. If the input is hidden, you can still target it if the recorder sees `input[type=file]`
3. **Populate text field on web page**
   - UI element: the file input
   - Text: `%InvoicePath%` (absolute path)
   - Populate using physical keystrokes: **Off**
   - Emulate typing: **Off**
4. **Wait for web page content** until the file **name** appears next to Attach (or a progress control disappears)

**Door B — OS Open dialog (most Ariba Attach buttons)**

1. **Press button on web page** (Add attachment / Browse / paperclip)
2. **Wait for window** title contains `Open` (also record `File Upload`, `Choose File`, and the OS language title)
3. **Focus window** (the dialog)
4. **Focus text field in window** (File name)
5. **Populate text field in window** `%InvoicePath%`
6. **Press button in window** (Open) — or **Send keys** `{Enter}` only if the Open button selector is flaky
7. **Wait for window** to **close** (dialog gone) so you do not type into the next invoice
8. Back in the browser: **Wait for web page content** (file name on the attachment list)

Multiple files: **For each** path in `%AttachmentList%`, repeat Door A or B. Some realms allow one “invoice image” plus extra supporting docs — use the correct paperclip for each.

Dropzones that only accept drag-and-drop: look for a hidden file input first (Door A). **Drag and drop UI element in window** onto a browser dropzone is brittle; prefer Browse.

**Analogy.** Door A is sliding the envelope under a slot that already has the right width. Door B is ringing the bell, waiting for the clerk to open the hatch, and placing the envelope in their hands.

### 5. Submit and keep the stamp

1. **Press button on web page** (Next / Review / Submit) — wizards often have **two** submits (validate, then confirm)
2. **Wait for web page content** (“successfully submitted”, IR number, or error banner)
3. **If web page contains** an error banner → **Get details of element on web page** → **Throw custom error** with that text
4. **Extract data from web page** or **Get details of element on web page** → `%ConfirmationId%`
5. **Take screenshot of web page** to `C:\RPA\Ariba\Proof\%InvoiceNumber%.png` (audit)
6. **Launch Excel** log → **Get first free column/row** → **Write to Excel worksheet** (PO, invoice, confirmation, timestamp, file name) → **Save Excel** / **Close Excel**
7. **Move file(s)** PDF to `C:\RPA\Ariba\Done\%CurrentDate%\`
8. **Close web browser**

Parse the confirmation with **Parse text** (`IR\d+`, `INV\d+`, or whatever your realm prints). Do not leave the page until `%ConfirmationId%` is non-empty.

## Reusable subflow: `UploadAttachment`

Put this in every portal project. Main only passes `%Browser%` and `%InvoicePath%`.

**Subflow `UploadAttachment`**

1. **If web page contains** UI element `FileInput` (hidden or visible)
   - **Populate text field on web page** `%InvoicePath%` (no emulate typing)
2. **Else**
   - **Press button on web page** `AttachButton`
   - **Wait for window** `OpenDialog` (timeout 15s)
   - **If window** not found → **Throw custom error** `Attachment picker did not open`
   - **Populate text field in window** File name = `%InvoicePath%`
   - **Press button in window** Open
   - **Wait for window** `OpenDialog` closes
3. **Wait for web page content** `AttachedFileName` (use **Get file path part** name as the text to wait for)
4. **If web page contains** “failed to upload” / virus / file type → **Throw custom error**

Call it from invoice, catalog, ASN, and RFP flows. Only the button UI element changes (input variable `%AttachButton%`).

## Combination with mail, queues, and Excel

**Inbound PDF → portal** (AP factory)

1. **Launch Outlook** → **Retrieve email messages from Outlook** (unread, has attachment)
2. **Save Outlook email messages** to `C:\RPA\Ariba\Inbox`
3. **Process a work queue item** (or **For each** file)
4. Run the demonstration above
5. **Update work queue item** processed / generic exception
6. **Process email messages in Outlook** (mark read)

**SharePoint drop → portal**

1. **List folder** / **Get file content**
2. **Convert binary data to file** `C:\RPA\Ariba\Inbox\%Name%`
3. Same upload
4. **Move file** on SharePoint to `/Submitted`

**Many invoices, one login**

Login is expensive (SSO, MFA, Ariba slowness). **Get credential** + launch **once**, then **For each** queue item: navigate → upload → submit → log. On session timeout (**If web page contains** Sign in), call `Login` again and retry the **same** item. **On block error** around one item so a bad PDF does not kill the batch.

## Ariba-shaped gotchas

| Symptom | What is going on | What to do |
| --- | --- | --- |
| Attach click does nothing | Overlay, iframe, or the real button is a child span | Re-capture; physical click; wait for overlay |
| Populate file input “succeeds” but no file | You populated a visible text box, not `type=file`, or emulate-typing was on | Door A only on the file input; keystrokes off |
| Open dialog not found | Locale title, or the picker is a Chrome window not “Open” | Capture the window with the recorder; use **If window contains** File name |
| Dialog found, path typed into the **page** | Focus never moved to the dialog | **Focus window** on the dialog before populate |
| Works attended, fails unattended | MFA, **Display select file dialog**, or no desktop for Door B | Credential + Door A/B; no message-box picker |
| Timeout after 10 minutes | Ariba idle logout | Shorter items; heartbeat click; re-login |
| Duplicate invoice | Realm rejects same supplier+invoice number | **If web page contains** duplicate → mark queue item failed, do not retry forever |
| DEV uploaded to PROD | Hard-coded URL | `%PortalUrl%` from environment |
| Selector broke after a Network UI refresh | Dynamic ids | Prefer name/text/role in the UI element; repair in the designer |
| File on a share path | Portal picker runs as the bot user and may not see `\\fileserver\...` | Copy to `C:\RPA\...` first (**Copy file(s)**) |

**SAP GUI is a different playbook.** Posting in SAP ERP (`FB60`, MIRO) uses **SAP automation** ([playbook 12](06-combination-playbooks.md#12-sap-posting-from-excel)). Ariba Network is a **website**. Do not mix SAP GUI actions with the browser upload.

## Same doors, other portals

| Portal | Typical upload | Notes |
| --- | --- | --- |
| SAP Business Network / Ariba | Invoice image, catalog, ASN, RFP | Iframes, slow waits, realm URLs |
| Coupa | Invoice / expense attachments | Often Door B; watch for multiple nested modals |
| Jaggaer / Bravo | Bid envelopes, catalogs | Wizard + mandatory attachment types |
| Ivalua | Supplier docs | Dropzone + hidden file input (try Door A first) |
| Oracle Supplier Portal | Invoice attachments | ADF iframes; physical click |
| Fieldglass | Timesheet / SOW docs | Similar Door B |
| “Any” vendor portal | Proof of delivery, claims | This same `UploadAttachment` subflow |

## Functions in combination

Browser automation (Launch, Wait, Populate, Press, Extract, Screenshot, Close) + UI automation (Wait for window, Focus, Populate, Press) + File/Folder + **Get credential** + Excel or work queues + Outlook or SharePoint for the inbound file + **On block error** + optional PDF text check.

**Not in this combination:** **Display select file dialog** (human picker), **Run JavaScript** to stuff `input.files`, **Launch new Internet Explorer**.
