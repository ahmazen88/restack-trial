# Capture these UI elements

Create a screen named **AribaPortal**. Rename each control **exactly**. Practice on the mock, then recapture on `https://supplier.ariba.com` (SAP Business Network). Click path: [ariba-sources.md](ariba-sources.md).

| PAD name | Mock selector | SAP / Ariba label |
| --- | --- | --- |
| `Txt_Username` | `#txt-username` | Sign-in user |
| `Txt_Password` | `#txt-password` | Sign-in password |
| `Btn_SignIn` | `#btn-signin` | Sign in |
| `Tab_Workbench` | `#tab-workbench` | **Workbench** tab |
| `Tile_Orders` | `#tile-orders` | **Orders** tile |
| `Txt_OrderNumbers` | `#txt-order-numbers` | Filter **Order numbers** |
| `Btn_Apply` | `#btn-apply` | **Apply** |
| `Lnk_PONumber` | `#lnk-po` | PO number link |
| `Btn_CreateInvoice` | `#btn-create-invoice` | **Create Invoice** |
| `Btn_StandardInvoice` | `#btn-standard-invoice` | **Standard Invoice** |
| `Txt_InvoiceNumber` | `#txt-invoice-number` | **Summary** → Invoice Number `*` |
| `Txt_InvoiceDate` | `#txt-invoice-date` | Invoice Date `*` (often pre-filled today) |
| `Btn_AddToHeader` | `#btn-add-to-header` | **Add to Header** |
| `Mnu_Attachment` | `#btn-menu-attachment` | **Attachment** |
| `Inp_File` | `#file-input` | File input (Door A) |
| `Btn_ChooseFile` | `#btn-choose-file` | **Choose File** / Browse (Door B, OS Open) |
| `Btn_AddAttachment` | `#btn-add-attachment` | **Add Attachment** (required after Choose File) |
| `Btn_Next` | `#btn-next` | **Next** (review) |
| `Btn_Submit` | `#btn-submit` | **Submit** |
| `Btn_BackToWorkbench` | `#btn-another` | Back to Workbench for the next PDF |

Capture **from the inner iframe** on the live Network. Do not use **Display select file dialog**. Door B: wait for window title `Open` (15s), send the full path, then **Add Attachment**.

Attachment total cap in SAP KBA 0399884 is **100 MB**; default per-file cap is often **10 MB** (KBA 0393164).
