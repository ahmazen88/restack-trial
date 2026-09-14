# SAP Ariba / Business Network documents (looked up)

These are the public pages used to wire the folder-upload flow. SAP renamed **Ariba Network** to **SAP Business Network**. Supplier UI: `https://supplier.ariba.com`. Official invoicing PDF: [SAP Business Network Guide to Invoicing (2605)](https://help.sap.com/doc/f7c0cc0c04ec41dab2828da0f3766dfc/2605/en-US/ANInvoicingGuide_2.pdf).

## PO-flip (create invoice from a purchase order)

SAP KBA [KB0397437 — How do I create a purchase order-based invoice?](https://support.ariba.com/item/view/KB0397437) and [How do I submit an invoice from a Standard account?](https://support.ariba.com/item/view/180034):

1. **Workbench** tab (top of home).
2. **Orders** tile (or an orders-related tile).
3. Optional: **Edit filter** → **Order numbers** → **Exact match** → **Apply**.
4. Open the PO (click the PO number).
5. **Create Invoice** → **Standard Invoice**.
6. **Summary**: Invoice Number, Invoice Date, and every field with `*` (required). Invoice date is often auto-filled with today.
7. Optional: header tax, shipping, special handling, **View/Edit Addresses**, Additional Fields.
8. Attachments (below).
9. Line items: Quantity / Include toggle; **Update** if amounts change.
10. **Next** to review. **Previous** to go back.
11. **Submit**. The invoice is a related document on the PO.

Older buyer-branded PDFs still say **Inbox** instead of Workbench. Same Create Invoice → Standard Invoice path after you open the order.

If **Create Invoice** is missing, the buyer’s transaction rules may require an order confirmation, ship notice, receipt, or service sheet first ([supplier FAQ pattern](https://www.gov.je/SiteCollectionDocuments/Government%20and%20administration/Supplier%20frequently%20asked%20questions.pdf)).

Permissions: **Inbox Access** + **Outbox Access** + **Invoice Generation** ([Guide to Invoicing](https://help.sap.com/doc/f7c0cc0c04ec41dab2828da0f3766dfc/2605/en-US/ANInvoicingGuide_2.pdf) — SAP Business Network User Permissions).

## Attach a file to an invoice

SAP KBA [KB0399884 — How do I attach a file to my invoice?](https://support.ariba.com/item/view/KB0399884):

1. Above Line Items: **Add to Header** → **Attachment**.
2. **Choose File** (some buyer PDFs say **Browse**) and pick the document (OS Open dialog).
3. **Add Attachment**. The file line appears under **Attachments** only after this click.
4. Delete: check the row → **Delete**.

After submit, attachments can be edited only in **Canceled**, **Failed**, or **Rejected**. Otherwise the buyer must reject first.

Buyer invoice rules can **forbid attachments** or limit file types. Online submit without a required attachment shows an error ([Guide to Invoicing](https://help.sap.com/doc/f7c0cc0c04ec41dab2828da0f3766dfc/2605/en-US/ANInvoicingGuide_2.pdf) — invoice rules). Line-level attachments exist via **Line Item Actions** → **Attachment** when the customer allows them.

Attachments are supporting files routed with the invoice; they are **not** digitally signed with the cXML ([Guide to Invoicing](https://help.sap.com/doc/f7c0cc0c04ec41dab2828da0f3766dfc/2605/en-US/ANInvoicingGuide_2.pdf) — Invoices with File Attachments).

## Size limits

SAP KBA [KB0393164 — maximum cXML document and attachment size](https://support.ariba.com/item/view/KB0393164):

| Limit | Figure |
| --- | --- |
| cXML invoice / PO / ASN / OC | 40 MB or 10,000 lines (attachments **not** counted) |
| Other cXML | 4 MB or 1,000 lines |
| Attachment default | **10 MB** |
| Attachment highest usual setting | **100 MB** (KBA 0399884: total attachments cannot exceed 100 MB) |
| Quality review attachments | default 100 MB, up to 200 MB |

Some customer PDFs still print 10 MB as a house rule. Fail a PDF before login if it is larger than the buyer’s cap.

## Duplicate invoice numbers

By default SAP Business Network **does not allow duplicate invoice numbers**. Reuse of numbers on Canceled/Rejected/Failed invoices is a buyer rule: **Allow suppliers to reuse invoice numbers** ([Guide to Invoicing](https://help.sap.com/doc/f7c0cc0c04ec41dab2828da0f3766dfc/2605/en-US/ANInvoicingGuide_2.pdf)).

## What this means for the PAD flow

| Doc step | PAD |
| --- | --- |
| Workbench → Orders → filter PO → open PO | Wait for those texts, then click captured controls |
| Create Invoice → Standard Invoice | Two clicks, wait for **Summary** / Invoice Number |
| Invoice # from the PDF name; date = today | **Get file path part**, **Get current date and time** `MM/dd/yyyy` |
| Add to Header → Attachment | Not a generic “question 3” |
| Choose File | Door A `input type=file` or Door B OS **Open** (15s) |
| **Add Attachment** | Required after the picker; wait until the file name is listed |
| Next → Submit | Review, then confirmation / status text |

Login URL for practice stays the mock. Production: `https://supplier.ariba.com`.
