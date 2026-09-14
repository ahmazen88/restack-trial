# Connected flow: folder drop → portal upload

This is the **actual desktop flow**, not a sketch. Paste `AribaFolderUpload.robin` into Power Automate for desktop, capture the UI elements in `ui-elements.md`, drop a PDF in Inbox, press **Play**.

Playbook [19](../../06-combination-playbooks.md#19-ariba-style-portal-upload-drop-pdf-in-a-folder--submit) and [07](../../07-portal-uploads-ariba.md) point here.

## What you run

1. Create `C:\RPA\Ariba\Inbox` (the flow also creates it).
2. Put `INV-1001.pdf` in that folder. Invoice number is the file name.
3. In PAD: **New flow** → capture **AribaPortal** controls (see `ui-elements.md`).
4. Open **Main**, paste the robin file.
5. On the **On block error** card: Retry policy **Fixed**, 3 times, 5 seconds; continue from **end of the block**; handle unexpected logic errors.
6. Variables pane: mark `PortalUrl`, `DropFolder`, `Username`, `Password` as **Input**; `ProcessedCount`, `FailedCount`, `LastConfirmationId` as **Output**. That is the run interface a cloud **Run a flow built with Power Automate for desktop** action uses later. This flow itself has **no PAD trigger**.
7. Press **Play**.

Default `PortalUrl` is the **mock** so you can prove navigation before touching Ariba:

```bash
python3 -m http.server 8765 --directory docs/power-automate-desktop/flows/ariba-folder-upload/mock-portal
```

Mock sign-in: `demo` / `demo`. User `mfa` shows **Approve sign-in** (the MFA fail path). Each **Next** shows a **Loading** overlay for 1.8s so waits are exercised.

When the mock run is green, set `PortalUrl` to your realm and change the `Question*` / `HomeText` variables to the labels on that site.

## Timeouts (loading-screen reduction)

Do not use a 10–30 second **Wait**. Wait until the overlay text is **gone** or the next question text is **present**.

| Moment | Seconds | Action |
| --- | ---: | --- |
| Browser process | 60 | Launch Edge `Timeout` |
| First page / SSO | 120 | Launch `WaitForPageToLoadTimeout` and post-login home |
| Loading overlay | 90 | Wait for web page to **not contain** `Loading` |
| Sign-in fields | 60 | Wait for element `Txt_Username` |
| Each wizard question | 60 | Wait for that question’s text |
| OS Open dialog | 15 | Wait for window title `Open` |
| File name on page | 90 | Wait for `%FileName%` after attach |
| Submit confirmation | 120 | Wait for `IR` |
| OCR fallback | 20 | If DOM text is missing three times |
| Click settle | 1 | Only after opening the OS dialog |

**Get current date and time** stamps each PDF. **Subtract dates** writes duration seconds to `C:\RPA\Ariba\run-log.csv`. Invoice date on question 2 is **today** as `MM/dd/yyyy`.

## Image / OCR figure

PAD’s documented default **Tolerance is 10**. The flow uses **10**, image width/height multiplier **1** (Microsoft: values greater than 3 produce bad OCR). That is the figure for image matching and OCR fallback when the DOM does not expose the question text.

## Where it goes wrong (wired, not hypothetical)

| Failure | What the flow does |
| --- | --- |
| Inbox empty | Log `EmptyInbox`, **Go to** `CleanExit`, success (nothing to do) |
| MFA / `Approve sign-in` | Log and exit before looping PDFs |
| Session dropped mid-batch | If Sign in is back, login again inside the PDF block |
| Home label missing in DOM | Retry 3 × 5s, then **Wait for text on screen (OCR)** |
| Click hits chrome / iframe | Recapture inside the frame; physical click if needed |
| Door A file input present | **Populate text field on web page** with the full path, emulate typing off |
| Door A missing | Click Attach → wait Open → **Send keys** path + Enter → wait Open closed |
| `failed to upload` / `Duplicate invoice` | Screenshot, move PDF to Failed, next file |
| No `IR\d+` on the page | Treat as failed, do not move to Done |
| Any other action error | **On block error** (retry 3 × 5s), then Failed folder |

One bad PDF does not stop the rest. Browser stays open for the whole **For each**.

## Wizard questions the flow looks for

The mock headings are the defaults. Change the `SET Question*` lines for Ariba.

1. `Question 1 of 4 — Purchase order`
2. `Question 2 of 4 — Invoice header`
3. `Question 3 of 4 — Attachments`
4. `Question 4 of 4 — Review and submit`

Navigation is **wait for that text → fill → Next**. If the wait times out, that PDF goes to Failed with a screenshot.

## After a run

| Path | Meaning |
| --- | --- |
| `C:\RPA\Ariba\Done` | Submitted |
| `C:\RPA\Ariba\Failed` | PDF + `.png` |
| `C:\RPA\Ariba\Proof` | Success screenshot named with confirmation |
| `C:\RPA\Ariba\run-log.csv` | Started, file, status, confirmation, seconds, message |

Not in this flow: PAD **UI element event trigger**, Outlook, SharePoint, work queues, Teams, **Display select file dialog**, Internet Explorer, SAP GUI.
