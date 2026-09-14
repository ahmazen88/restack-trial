# Capture these UI elements

In PAD, open the mock (`http://127.0.0.1:8765/index.html`) or your Ariba realm. Create a screen named **AribaPortal**. Capture each control and **rename it exactly** as below so `AribaFolderUpload.robin` binds.

| PAD name | Mock selector | What it is on Ariba |
| --- | --- | --- |
| `Txt_Username` | `#txt-username` | Sign-in user |
| `Txt_Password` | `#txt-password` | Sign-in password |
| `Btn_SignIn` | `#btn-signin` | Sign in |
| `Btn_CreateInvoice` | `#btn-create-invoice` | Create Invoice / PO-flip |
| `Txt_PONumber` | `#txt-po` | PO search / PO field |
| `Btn_NextPO` | `#btn-next-q1` | Next after PO (often the same Next on Ariba — capture that step’s Next) |
| `Txt_InvoiceNumber` | `#txt-invoice-number` | Invoice number |
| `Txt_InvoiceDate` | `#txt-invoice-date` | Invoice date |
| `Btn_NextHeader` | `#btn-next-q2` | Next after header |
| `Inp_File` | `#file-input` | Hidden or visible `input type=file` (Door A) |
| `Btn_Attach` | `#btn-attach` | Add attachment / paperclip (Door B) |
| `Btn_NextAttach` | `#btn-next-q3` | Next after attachments |
| `Btn_Submit` | `#btn-submit` | Submit |
| `Btn_CreateAnother` | `#btn-another` | Back to home for the next PDF (optional on Ariba) |

Capture **from the inner iframe** on real Ariba. The selector is the frame switch.

Do not capture **Display select file dialog**. Door B uses the OS window title `Open` (locale: `Öffnen`, `Ouvrir`) plus **Send keys** of the full PDF path.

Image/OCR fallback uses **Tolerance 10** (PAD default). Do not raise image width/height multipliers above 1 unless a capture is too small to read.
