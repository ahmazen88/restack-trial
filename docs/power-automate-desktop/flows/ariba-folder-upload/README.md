# Connected flow: folder drop → SAP Business Network invoice

Paste `AribaFolderUpload.robin` into Power Automate for desktop. The click path matches SAP’s public Ariba / Business Network docs in [ariba-sources.md](ariba-sources.md), not a generic four-question wizard.

Drop `4500123456_INV-1001.pdf` (or `INV-1001.pdf` against the mock PO) in `C:\RPA\Ariba\Inbox` and press **Play**. No PAD trigger.

## What you run

1. Capture **AribaPortal** controls ([ui-elements.md](ui-elements.md)).
2. Paste the robin into **Main**.
3. **On block error**: Fixed, 3 × 5 seconds, continue from **end of the block**.
4. Mark Input/Output variables (cloud **Run a desktop flow** interface later).
5. Practice on the mock, then set `PortalUrl` to `https://supplier.ariba.com`.

```bash
python3 -m http.server 8765 --directory docs/power-automate-desktop/flows/ariba-folder-upload/mock-portal
```

Mock sign-in: `demo` / `demo`. User `mfa` → **Approve sign-in**. Mock PO **4500123456**. Each navigation shows **Loading** for 1.8s.

## Official click path (wired in the robin)

1. **Workbench**
2. **Orders** tile → **Order numbers** filter → **Apply** → open PO
3. **Create Invoice** → **Standard Invoice**
4. **Summary**: Invoice Number `*`, Invoice Date `*` (today `MM/dd/yyyy`)
5. **Add to Header** → **Attachment**
6. **Choose File** (Door A populate `input type=file`, or Door B OS **Open** 15s) then **Add Attachment**
7. Wait until the file name is listed under Attachments (90s)
8. **Next** → **Review** → **Submit**
9. Wait for **Invoice submitted** (120s)

## Timeouts

| Moment | Seconds |
| --- | ---: |
| Browser process | 60 |
| Page / SSO / Workbench | 120 |
| Loading overlay gone | 90 |
| Each screen label | 60 |
| OS Open dialog | 15 |
| File name after **Add Attachment** | 90 |
| Submit | 120 |
| OCR fallback | 20 |

Do not sleep 10–30s through loading. Image/OCR **Tolerance is 10**, multiplier **1**.

## Where it goes wrong

Empty inbox → `CleanExit`. MFA text → stop. Duplicate invoice numbers are rejected by default on the Network. Missing **Add Attachment** after Choose File leaves an empty Attachments list. Create Invoice greyed out → buyer rules (OC / ASN / SES). Attachment default **10 MB**, total **100 MB** (SAP KBA 0393164 / 0399884). One PDF failure does not stop the batch.
