# Power Automate flow: Ariba folder upload

This is the importable **cloud** flow. It is instant: you drop PDFs in a folder, then **Run**. It does **not** watch the folder, mail, SharePoint, or a queue.

The RPA clicks live in [`../AribaFolderUpload.robin`](../AribaFolderUpload.robin). Microsoft stores desktop flows as Dataverse binaries, so a `.robin` file cannot be imported as a desktop flow. Paste it in Power Automate for desktop, then bind it here.

## Files

| File | What it is |
| --- | --- |
| [`AribaFolderUpload-package.zip`](AribaFolderUpload-package.zip) | Upload this in Power Automate |
| [`workflow-definition.json`](workflow-definition.json) | Same logic, for Code view |
| [`inputs.json`](inputs.json) | Input/output names the two flows share |
| [`pack.py`](pack.py) | Rebuilds the zip |

## Import (cloud)

1. Open [Power Automate](https://make.powerautomate.com) → **My flows**.
2. **Import** → **Import Package (Legacy)**.
3. Upload `AribaFolderUpload-package.zip`.
4. **Import setup** for the flow: **Create as new**.
5. Related resource **Desktop flows** / `shared_uiflow`: pick your **machine** connection (attended, this PC). Create one under **Data** → **Connections** → **Desktop flows** if none exists.
6. **Import**.

## Desktop flow (required before the cloud Run action works)

1. In Power Automate for desktop, **New flow** named `AribaFolderUpload`.
2. Capture screen **AribaPortal** ([`../ui-elements.md`](../ui-elements.md)).
3. Paste `AribaFolderUpload.robin` into **Main**.
4. **On block error**: Fixed, 3 × 5 seconds, continue from **end of the block**.
5. Variables pane — mark as **Input**: `PortalUrl`, `DropFolder`, `Username`, `Password` (Password = sensitive). Mark as **Output**: `ProcessedCount`, `FailedCount`, `LastConfirmationId`.
6. Save. Copy the desktop flow id from  
   `https://make.powerautomate.com/manage/environments/{env}/uiflows/{id}/details`.

## Bind and run

1. Open the imported cloud flow.
2. Action **Run a flow built with Power Automate for desktop**: choose `AribaFolderUpload` (replaces the placeholder `uiFlowId`).
3. Run mode **Attended**, session **Local**. Timeout in the package is **2 hours**.
4. Practice mock: `python3 -m http.server 8765 --directory ../mock-portal` then drop `4500123456_INV-1001.pdf` in `C:\RPA\Ariba\Inbox`.
5. Cloud **Run**. Leave Portal URL / folder / user / password blank for mock defaults (`demo` / `demo`). Production: `https://supplier.ariba.com` and the Network account.
6. PAD console must be signed in on that machine (attended).

If any PDF lands in Failed, the cloud run **Fails** and the summary shows counts. Empty inbox is success.

## Create from blank instead of the zip

1. **Create** → **Instant cloud flow** → **Manually trigger a flow**.
2. Add **Run a flow built with Power Automate for desktop** (`RunUIFlow_V2`).
3. Switch to **Code view** and replace the definition with [`workflow-definition.json`](workflow-definition.json), or map `item/PortalUrl`, `item/DropFolder`, `item/Username`, `item/Password` by hand.
4. Pick `AribaFolderUpload` and the machine connection.

Do not add a recurrence, folder trigger, Outlook, SharePoint, or a notification action.
