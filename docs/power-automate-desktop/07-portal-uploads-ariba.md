# Portal uploads like Ariba

**Power Automate cloud flow (import):** [AribaFolderUpload-package.zip](flows/ariba-folder-upload/cloud/AribaFolderUpload-package.zip) — [import steps](flows/ariba-folder-upload/cloud/README.md)  
**Desktop flow (paste):** [AribaFolderUpload.robin](flows/ariba-folder-upload/AribaFolderUpload.robin) — [how to run](flows/ariba-folder-upload/README.md)  
**SAP documents used:** [ariba-sources.md](flows/ariba-folder-upload/ariba-sources.md)

You **put PDFs in a folder** and **Run** the [cloud package](flows/ariba-folder-upload/cloud/AribaFolderUpload-package.zip) (or **Play** in PAD). No PAD trigger, no mail, no queue, no notification.

The robin follows SAP Business Network (Ariba) public steps: **Workbench** → **Orders** → open PO → **Create Invoice** → **Standard Invoice** → **Summary** → **Add to Header** → **Attachment** → **Choose File** → **Add Attachment** → **Next** → **Submit**.

**Analogy.** A tray on the clerk’s desk. You drop envelopes in. When you say “go,” the clerk badges in, waits for the lift (**Loading**), finds the purchase order on the workbench, fills the starred Summary fields, hands the envelope to **Add Attachment**, and leaves when the stamp says submitted.

## Drop folder

| Path | Role |
| --- | --- |
| `C:\RPA\Ariba\Inbox` | PDFs. Prefer `PO_Invoice.pdf` (mock PO `4500123456`) |
| `C:\RPA\Ariba\Done` | Submitted |
| `C:\RPA\Ariba\Failed` | Failed + screenshot |
| `C:\RPA\Ariba\Proof` | Success screenshot |
| `C:\RPA\Ariba\run-log.csv` | Status and seconds |

Practice mock: `demo` / `demo`. Production: `https://supplier.ariba.com`.

## Waits

Wait for **Loading** to vanish (90s) or the next SAP label to appear (60s). Open dialog 15s. File listed after **Add Attachment** 90s. Submit 120s. OCR fallback 20s, **Tolerance 10**. **On block error** 3 × 5s. Invoice date = today `MM/dd/yyyy`.

## Attach doors (KB0399884)

| Door | PAD |
| --- | --- |
| A — `input type=file` | **Populate text field on web page**, emulate typing off |
| B — **Choose File** / Browse | **Wait for window** `Open` (15s) → **Send keys** path |
| Then always | **Add Attachment**, wait for the file name under Attachments |

Default attachment cap **10 MB**; total **100 MB** (KB0393164 / KB0399884). Buyer rules can forbid attachments.

## Where it goes wrong

Empty inbox → success stop. **Approve sign-in** → exit. Duplicate invoice numbers blocked by default on the Network. **Create Invoice** missing → OC/ASN/SES rule. No **Invoice submitted** → Failed folder, next PDF.

**Not in this flow:** PAD triggers, Outlook, SharePoint, work queues, Teams, **Display select file dialog**, Internet Explorer, SAP GUI ([playbook 12](06-combination-playbooks.md#12-sap-posting-from-excel)).
