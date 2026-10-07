# Production Tracker – n8n auto-refresh

Drop a production report (CSV or Excel) into a Google Drive folder. Within a minute, n8n merges it into the
**Production Tracker** Google Sheet, recalculates progress and status, logs what changed, and files the report away.

```
Drive "Inbox" folder ──► Download ──► CSV / XLSX / XLS? ──► Read rows ──► Normalize columns
                                            │ other                                      │
                                            ▼                                            ▼
                               Log "Rejected" + move to Rejected     Read Tracker ──► Merge (by Item ID)
                                                                                         │
                                         Move to Processed ◄── Write Update Log ◄── Upsert Tracker rows
```

## Files

| File | What it is |
|---|---|
| `production_tracker_workflow.json` | The n8n workflow – import this |
| `Production_Tracker_Template.xlsx` | Tracker sheet (`Tracker` + `Update Log` tabs, status colours, % formatting) |
| `sample_report.csv` | Example report to test with |
| `src/*.js` | Source of the Code nodes (built into the JSON by `build.py`) |
| `test/run.js` | Offline test of the merge logic: `node test/run.js` |

## Setup (≈10 minutes)

1. **Create the tracker.** Upload `Production_Tracker_Template.xlsx` to Google Drive, then
   *File → Save as Google Sheets*. Name it `Production Tracker`. Keep the tab names `Tracker` and `Update Log`.
2. **Create three Drive folders**: `Production Reports – Inbox`, `… – Processed`, `… – Rejected`.
3. **Import the workflow.** In n8n: *Workflows → Import from File* → `production_tracker_workflow.json`.
4. **Connect Google.** Open any Google node and create/select a *Google Drive OAuth2* and a
   *Google Sheets OAuth2* credential (same Google account that owns the files).
5. **Point the nodes at your files** (each is a dropdown):
   - `New File in Inbox` → Inbox folder
   - `Read Tracker`, `Update Tracker`, `Write Update Log`, `Log Rejected File` → `Production Tracker` spreadsheet
   - `Move to Processed` / `Move to Rejected` → those folders
6. **Test.** Upload `sample_report.csv` to the Inbox, click *Test workflow* (or *Fetch Test Event* on the trigger).
   You should see 4 rows in `Tracker` and one line in `Update Log`. Then toggle the workflow **Active**.

## How the data is merged

- **Matching key:** `Item ID`. Report rows with an ID already in the tracker update that row; new IDs are appended.
  Rows with no ID (e.g. a "Totals" line) are skipped and counted in the log.
- **Column names are flexible.** `Job No`, `WO`, `Activity ID`, `BOQ Ref` all map to `Item ID`; `Installed`,
  `Produced`, `Completed Qty` all map to `Actual Qty`, and so on. Add your own headings to the `ALIASES` list at
  the top of the **Normalize Report Rows** node.
- **Only fields present in the report are overwritten.** Remarks or dates you typed into the tracker by hand stay,
  unless the report has a value for that column.
- **Cumulative vs daily quantities.** By default report quantities are treated as *totals to date* and overwrite the
  tracker. If your reports contain *today's output only*, set `QTY_MODE = 'incremental'` in **Merge Into Tracker**
  and the quantities get added instead (then don't drop the same report twice).
- **Calculated columns:** `Remaining Qty`, `% Complete`, `Last Updated`, `Source File` and `Status`:
  - `Complete` when Actual ≥ Planned
  - `Behind Schedule` when past `Planned Finish` and not complete
  - `In Progress` / `Not Started` otherwise
  - A `Status` column in the report always wins, and `On Hold` / `Cancelled` set manually in the tracker are kept.

## Limitations / notes

- Report headers must be in **row 1** of the first sheet. If your Excel report has title rows above the header,
  set *Options → Range* on the `Read XLSX` node (e.g. `A5:Z500`).
- Drop **.csv / .xlsx / .xls** files. Native Google Sheets, PDFs etc. are moved to *Rejected* with a log entry.
  (PDF reports can be added later with an AI extraction step.)
- The Drive trigger polls every minute and fires on **newly created/uploaded** files. Moving an old file into
  the folder may not trigger it – upload or copy it instead.
- If a Google step fails (e.g. permissions), the report stays in the Inbox and the failed run shows in
  n8n's *Executions* list. Add an Error Workflow under *Workflow settings* if you want email alerts.

## Editing the logic

Edit the scripts in `src/`, then run `python3 build.py` to regenerate the workflow JSON, and
`node test/run.js` to re-test. `python3 make_template.py` regenerates the template.
