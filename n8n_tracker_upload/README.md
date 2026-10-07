# Production Tracker – upload from SharePoint (option 1)

Your company's n8n has no SharePoint connector, so the tracker is **brought to n8n** through an n8n upload form.
Uploading refreshes the Data Table, then runs the *Report copy* workflow, which emails the Production
Intelligence Report.

```
Form: upload tracker.xlsx ─► Read sheet ─► Clean rows ─► Data Table: upsert on Invoice ─► Run "Report copy" ─► "Done" page
```

## One-time setup (≈15 min)

### A. Import the upload workflow
1. n8n → **Create workflow** → **⋯ → Import from File** → `tracker_upload_workflow.json`.
2. **Upsert into Data Table**: pick the same Data Table that *Report copy* reads from.
3. **Clean Rows**: check the settings at the top:
   - `COLUMNS`: the Data Table's column names, **spelled exactly** as in the table.
   - `ALIASES`: the tracker's Excel headings for each column, if they differ (e.g. *Invoice No* → `Invoice`).
   - `TYPES`: leave empty if the Data Table columns are text. Set `'number'` / `'date'` for number/date columns.
   - `KEY`: the column that uniquely identifies a row (default `Invoice`). If one invoice can have several rows,
     tell us – you'll need a different key.
4. **Read Tracker Sheet**: if the data isn't on the first tab, open *Add option → Sheet Name* and type the tab name.
   If there are title rows above the headings, add *Range* (e.g. `A3:Z5000`).

### B. Let *Report copy* be started by the upload
1. Open **Report copy**, add a **When Executed by Another Workflow** trigger (*Input data mode: Accept all data*),
   and connect it to **Get row(s)**. Keep the manual trigger too, if you like.
2. In **Get row(s)**, switch **Return All** on, so new rows are never cut off at 5,000.
3. Save / publish *Report copy*.

### C. Connect the two
1. Back in the upload workflow, **Refresh Report** → select **Report copy**.
2. **Publish** the upload workflow.
3. Open **Upload Tracker** → copy the **Production URL** (ends in `/form/production-tracker-upload`).
   Bookmark it or pin it in your Teams channel – that's the page your team uses.

## Every time the tracker changes
1. In SharePoint: open the tracker → **File → Create a Copy → Download a Copy** (gets an `.xlsx`).
2. Open the form link → choose the file → **Upload & refresh report**.
3. The confirmation shows how many rows were saved. The report email follows a few minutes later.

## How the data is handled
- **Upsert**: rows whose `Invoice` already exists are **updated**, new invoices are **added** – no duplicates.
- Blank rows and *Total* rows (no invoice number) are skipped. If an invoice appears twice in the file, the
  **last** row wins.
- The tracker is treated as the source of truth: if a column is empty in the tracker, it becomes empty in the
  Data Table too.
- Rows **deleted** from the tracker are *not* removed from the Data Table. If you need that, use a full refresh
  instead: put a *Data Table → Table → Clear* step before the upsert (note this briefly empties the table).

## Notes
- Only people with the form link can upload. For extra control, set *Authentication* on the **Upload Tracker**
  node (Basic Auth, or n8n user login on newer versions).
- If something fails (wrong column names, wrong tab), the form shows an error and the run appears under
  **Executions** with the exact step that failed. The Data Table is left as it was for any rows not reached.

## Editing
Edit `src/*.js`, run `python3 build.py` to regenerate the JSON, and `node test/run.js` to re-test.
