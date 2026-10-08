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

## Checks on every upload (deterministic: the same file always gives the same result)
- **Wrong file / wrong tab:** stops with a clear message if no Invoice column is found.
- **Text cleanup:** extra spaces removed; Customer and Company_Code upper-cased so variants group together.
- **Data quality** (shown on the Done page, rows are still saved): missing or zero/negative value, missing
  customer or company code, no readable date, dates before 2020-01-01, allocated before received, and the
  invoice numbers that appear more than once.

## Notes
- Only people with the form link can upload. For extra control, set *Authentication* on the **Upload Tracker**
  node (Basic Auth, or n8n user login on newer versions).
- If something fails (wrong column names, wrong tab), the form shows an error and the run appears under
  **Executions** with the exact step that failed. The Data Table is left as it was for any rows not reached.

## One flow: OneDrive tracker → Data Table → report email (`tracker_onedrive_workflow.json`)
Everything in a single workflow. It doesn't call *Report copy*; it builds and emails its own report.
The tracker lives in your own OneDrive (`spo-mydrive.ge.com/personal/<your SSO>`), so n8n reads it with your
own Microsoft login.

```
Weekdays 07:00 (or Test Run) ─► Find Tracker ─► Pick Tracker File ─► Download Tracker ─► Read Tracker Sheet
   ─► Clean Rows ─► Upsert into Data Table ─► Summarise Upload ─► Build Report ─► Send Report ─► Remember Version
```

Setup:
1. Import `tracker_onedrive_workflow.json`.
2. **Find Tracker** and **Download Tracker** are *HTTP Request* nodes calling Microsoft Graph (they work even
   where the OneDrive/Outlook nodes are not installed). Select a **Microsoft Drive OAuth2 API** credential
   (sign in with your company account).
3. **Pick Tracker File**: `TRACKER_NAME` must match the file name exactly (`Trackers - NAM Distribution.xlsx`).
4. **Upsert into Data Table** → your Data Table. Optional: delete this step and connect Clean Rows straight to
   Summarise Upload if you don't need the Data Table.
5. **Build Report**: put the email addresses in `RECIPIENTS` at the top (the run stops with a message if it's
   empty). **Send Report** (HTTP Request → Graph `sendMail`): select a **Microsoft Outlook OAuth2 API**
   credential. **Or use the company mail node** (the GEV SMTP "Send an Email" node from *Report copy*): copy it in,
   connect Build Report → it → Remember Version, and set To `{{ $json.to }}`, Subject `{{ $json.subject }}`,
   HTML body `{{ $json.html }}`.
6. Click **Test Run**, check the email, then **Publish**. Set the timezone under *Workflow settings*.

The report (rule-based, no AI: the same file always gives the same email):
- Headline figures: invoices, total value, customers, company codes
- Monthly summary (last 12 months), top 10 customers by value with share, company codes with share,
  daily activity (last 14 active days)
- Data quality: blank rows, repeated invoices, missing/zero values, missing customer or company code,
  unreadable or pre-2020 dates, allocated-before-received
- The "as of" date is the latest date in the data, not the clock. Dates use Received → Allocated → Invoice
  date (first filled), the same order as *Report copy*.

Behaviour:
- If the file hasn't changed since the last scheduled run (same version/eTag), the run stops early: no
  upsert, no email. Manual test runs always process the file.
- Stops with a clear error if the file is missing or two files share the name.
- The file is in a personal OneDrive. If it moves to a team SharePoint site, swap the two OneDrive nodes for
  SharePoint nodes; everything else stays the same.

## Upload, reports & dashboard: one workflow (`tracker_reports_workflow.json`)
Four ways in, one report engine:
```
Upload Tracker (form) ─► Read ─► Clean Rows ─► Upsert ─► Summarise ─┐
Request a Report (form: type, From/To, company code, customer, send to) ──┤
Every Monday 07:00 (weekly) ──────────────────────────────────────────────┼─► Get All Rows ─► Report Settings ─► Build Report
1st of month 07:00 (monthly) ─────────────────────────────────────────────┘        ─► [GEV Send Email] ─► Done Page (forms only)
```
The report covers headlines with change vs the previous period and a forecast, **customers to look out for**
(volume spike / sharp fall / gone quiet / new / high value share / slow turnaround / portal / data issues),
incoming volume by month and week, the **workload heatmap** (day of month × month), busiest weekdays,
the **forecast** (next 4 weeks and next month, with range), the company code split with top customers,
customer details with a 6-month trend, channels, project managers and data quality.
All rules are fixed and listed at the top of **Build Report** (`RULES`). The same data always gives the same report.

The email has the report; the attached **dashboard.html** has the same report with its own filters (period,
company code, customer). It opens in any browser. If the company blocks .html attachments, use the request form.

Setup: Data Table in **Upsert** and **Get All Rows**; `RECIPIENTS` in **Build Report**; swap the placeholder
**Send Report** for the GEV *Send an Email* node (To `{{ $json.to }}`, Subject `{{ $json.subject }}`, HTML
`{{ $json.html }}`, Attachments `dashboard`); publish and share the two form links.

## Fast saving (fix for the "spinning" upload)
The first versions saved every row one by one (about 8,000 calls for 4,100 rows) while the form waited. Now:
```
Clean Rows → Get Table Rows → Compare with Table → Anything to save? ─no──────────────────────────────► Summarise
                                                        │yes
                                                        └► Few changes? ─yes► Save Changed Rows ─────────► Summarise
                                                                         └no─► Clear Table → Restore Rows → Bulk Add All Rows ─► Summarise
```
- Normal upload: only new or changed invoices are written, usually a handful.
- Empty table, or more than 300 changes (e.g. the first upload): the table is cleared and all rows are added in one
  bulk call. Rows that are no longer in the tracker disappear then; the tracker is the source of truth.
- In the reports workflow, both forms answer immediately ("received – the report arrives by email").

## AI commentary (reports workflow)
**AI Commentary** (Basic LLM Chain) gets the compact `facts` from **Build Report** and writes four sections:
Summary, What needs attention, Workload outlook and Suggested actions. The system prompt forbids inventing or
recalculating numbers and fixes the HTML format. **Add AI Commentary** cleans the HTML (allowed tags only) and puts
it above the rule-based report. If the AI fails, the report goes out without it (retry once, then continue).
Connect a **GEV LLM Model** to its *Model* input and set the temperature to 0.1–0.2.

## Editing
Edit `src/*.js`, run `python3 build.py` to regenerate both workflow JSON files, and `node test/run.js` to re-test.

## The one to use: `production_tracker.json` (one start, one end)
```
Upload Tracker (form) → Read Tracker Sheet → Clean Rows → Check Table → Safety Check → Clear Table → Rows to Save
  → Save All Rows → Summarise Upload → Build Report → AI Commentary → Add AI Commentary → Send an Email → Done Page
```
A straight line: no branches and no choices. On every upload the table is emptied and refilled in one bulk call,
so it doesn't spin, and the tracker is always the source of truth. Setup is the 5 steps in the yellow note
inside the workflow. Test: `node test/simple.js` (57 checks).

Safety: **Safety Check** runs before **Clear Table**. An empty sheet, the wrong file or tab, no usable invoice
numbers, or a Data Table missing one of the columns all stop the run with a clear message, and the table is left
as it was. Invoice numbers that are not a plain number (e.g. `7001 / 7002`) are skipped and listed on the Done page,
never guessed. Amounts like `$1,157.44` and `(1,157.44)` are read correctly; Excel dates with a time part keep their day.

### SAP customer code and profit centre (lookups)
The upload form has two optional boxes: **ZSD Log** and **Tableau Extract**.
- G367 (tracker sales org G36C / GS5C is changed to G367): SAP customer code from the ZSD log (first sheet and
  `2025 Inv Processed`). No profit centre.
- 3060 / 3487 / 3485: SAP customer code and profit centre from the Tableau extract.
- Matching is on invoice number only. The invoice column is the one whose values match the tracker's invoice numbers,
  so the heading spelling does not matter. No match = empty (never guessed).
- Codes found on an earlier upload are kept (read from the Data Table before it is cleared), so invoices that are no
  longer in a later Tableau extract keep their codes.
- The Data Table needs two extra string columns: `SAP_Customer_Code`, `Profit_Center`. The Safety Check stops with a
  clear message until they exist.

### AI Chart Designer
A second Basic LLM Chain reads the same facts and returns a JSON list of 3–4 charts (dataset, metric, chart type,
title, a short "why"). **Add AI Charts** draws them from the facts only: unknown datasets, splits with one entry and
any "why" containing numbers are dropped; if nothing usable comes back, standard charts are drawn. Email: table-based
charts (work in Outlook). dashboard.html: SVG charts. An unfinished month is marked `*` and drawn lighter / dashed.

### Breakdown tree
One table instead of separate splits: Entity (La Prairie Canada = 3060 + 3487, Charleroi = 3485, Clearwater = G367)
→ Company code → Sales org (G36C / GS5C, G367 only) → profit centre / product line. The order of the last two is
checked against the data (fewest values under more than one parent; a tie keeps profit centre → product line). Empty levels are skipped and single groups are merged onto one line. A profit centre (or other
value) under more than one company code is pointed out. Needs the `Sales_Org` column in the Data Table.

### Lookup rules (latest)
- Tableau rows are used only for company codes 3060, 3485, 3487 and G367 (GS52, GWJ1 and others are ignored).
- G367 is looked up in Tableau too: SAP customer code from the ZSD log first, then Tableau; profit centre and product line
  from Tableau; product line PQP when Tableau has none.
- Business type (Nature of Activities PL / PC) and Customer Type are not used for now.
