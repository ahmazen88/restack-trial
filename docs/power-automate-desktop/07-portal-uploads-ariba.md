# Portal uploads like Ariba

**The connected flow is in** [flows/ariba-folder-upload/](flows/ariba-folder-upload/README.md). Paste `AribaFolderUpload.robin` into PAD. This page is the map of that flow: drop folder, waits, questions, and the two attach doors.

You **put PDFs in a folder** and **press Play**. No PAD trigger, no mail, no SharePoint, no work queue, no notification.

**Analogy.** A tray on the clerk’s desk. You drop envelopes in. When you say “go,” the clerk badges in, waits for the lift doors (loading overlay), answers each window question, hands over the envelope, and files it when the receipt stamp appears.

## Start: the drop folder

| Folder | Role |
| --- | --- |
| `C:\RPA\Ariba\Inbox` | You place `*.pdf` here, then run the flow |
| `C:\RPA\Ariba\Done` | Successful uploads |
| `C:\RPA\Ariba\Failed` | Files that did not submit (plus a screenshot) |
| `C:\RPA\Ariba\Proof` | Success screenshots |
| `C:\RPA\Ariba\run-log.csv` | Started, file, status, confirmation, seconds |

Default practice URL is the **mock portal** in `flows/ariba-folder-upload/mock-portal/` (`demo` / `demo`). Point `PortalUrl` at your Ariba realm after selectors work.

## Waits (do not sleep through loading)

The robin file waits for **text to appear or Loading to vanish**. Fixed **Wait** is 1 second, and only after the OS Open dialog appears.

| Moment | Seconds |
| --- | ---: |
| Launch browser | 60 |
| Page load / SSO / home | 120 |
| Loading overlay gone | 90 |
| Each wizard question | 60 |
| Open dialog | 15 |
| File name after attach | 90 |
| Confirmation `IR` | 120 |
| OCR fallback | 20 |

Retries: **On block error** Fixed **3 × 5 seconds**, then that PDF goes to Failed and the loop continues. Invoice date is **Get current date and time** formatted `MM/dd/yyyy`. **Subtract dates** writes duration to the CSV.

Image/OCR **Tolerance 10** (PAD default). Multiplier **1**.

## Wizard questions the flow finds on screen

Wait for the heading, then fill, then Next. Defaults match the mock. Change the `SET Question*` lines for Ariba. The robin file runs **Get files in folder** on Inbox, then this wizard.

1. Purchase order
2. Invoice header (number from file name, date = today)
3. Attachments
4. Review and submit

If the DOM does not show the home label after three tries, **Wait for text on screen (OCR)** on the foreground window.

## The two doors for a file

| Door | PAD move |
| --- | --- |
| **A —** `input type=file` in the DOM | **Populate text field on web page** with the full path of `%CurrentPdf%`. Emulate typing **off**. |
| **B —** Attach opens OS `Open` | Click Attach → **Wait for window** (15s) → **Send keys** path + Enter → wait for `Open` to close |

Then wait until the **file name** is on the page (90s).

## Where it goes wrong

Empty inbox → stop successfully. MFA text `Approve sign-in` → log and exit. Duplicate / upload fail / missing `IR\d+` → screenshot, Failed folder, next PDF. Session back on Sign in → login again inside the loop.

**SAP GUI is a different playbook** ([12](06-combination-playbooks.md#12-sap-posting-from-excel)).

**Not in this flow:** PAD triggers, Outlook, SharePoint, work queues, Teams, **Display select file dialog**, Internet Explorer.
