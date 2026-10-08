# Where we are and what to do next

## Paused (2026-10-08): work with what we have
Findings from the company n8n:
- **Microsoft credentials need IT:** *Microsoft Drive OAuth2 API* asks for a Client ID and Client Secret, so an
  app registration in the company Microsoft account is needed. Redirect URL to give IT:
  `https://ampworkflow.gevernova.net/rest/oauth2-credential/callback`
- **Outbound network is restricted:** a Datadog credential test failed with `ECONNREFUSED`, so the server only
  reaches approved destinations. Whether Microsoft (login.microsoftonline.com, graph.microsoft.com) is reachable
  is untested; the user chose not to test for now.
- **Approved email exists:** the *GEV SMTP* credential (used in *Report copy*'s "Send an Email" node).

- **Nodes confirmed installed** (node panel, 2026-10-08):
  - Core: Code, Data table, **HTTP Request**, **Webhook**, Execute Sub-workflow, n8n Form
  - Data transformation: Date & Time, Edit Fields (Set), Filter, Limit, Remove Duplicates, Split Out, combine-items group
  - Flow: If, Switch, Merge, Loop Over Items, Compare Datasets, Wait
  - AI: AI Agent, Guardrails, Basic LLM Chain, Information Extractor, Q&A Chain, Sentiment Analysis,
    Summarization Chain, Text Classifier
  - Triggers: schedule, webhook, form, called by another workflow, chat message, evaluation, app events
  - Apps: mostly HTTP-based security tools, plus the company **AMP Agent** node
  - The OneDrive and Outlook nodes are *not* available. Because HTTP Request is installed, the Graph-based nodes in
    `tracker_onedrive_workflow.json` will load, but they still need the IT app registration and network access
    to Microsoft.

- **Company mail node** ("Send an Email" in *Report copy*): **GEV Send Email node, version 1**.
  - Credential: GEV SMTP account 1539. Operation: Send. From Email: noreply@gevernova.com (dropdown).
  - To Email: text. Subject: text. Email Format: HTML. HTML: field (currently `{{ $json.output }}`).
    Options: Attachments.
  - Settings: On Error = Stop Workflow.
  - To map from Build Report: To `{{ $json.to }}`, Subject `{{ $json.subject }}`, HTML `{{ $json.html }}`.
  - Exact internal node type not known yet. Copying the node (Ctrl+C) and pasting the JSON would let it be
    embedded directly in the workflow file.

- **Data Table "datatable"** columns: Received_Date, Allocated_Date, Invoice_Date (text, `YYYY-MM-DD`),
  Project_Manager (text), Customer (text), Name_the_PortalEmail_ID (text), **Invoice (number)**,
  **Value (text, e.g. `1157.44`)**, Company_Code (text, e.g. `3060`), plus system id/createdAt.
  Clean Rows now matches this exactly.
  - Open question: the table has repeated invoice numbers (e.g. 7001212645 twice, same value). Are these accidental
    duplicates, or can one invoice really have several rows? Upsert on Invoice keeps one row per invoice.

Decision: **stay with what already works.** That's the upload form (confirmed working up to the Data Table),
plus the rule-based report sent through the company GEV SMTP mail node. No Microsoft connectors for now.

When resuming, build: Upload form → Read Tracker Sheet → Clean Rows → (Upsert) → Summarise → Build Report →
company "Send an Email" node (To `{{ $json.to }}`, Subject `{{ $json.subject }}`, HTML `{{ $json.html }}`).

## Update (2026-10-08 later)
- "Spinning" upload fixed: compare first, save only changed rows; clear + bulk add for big changes; forms answer
  immediately in the reports workflow.
- Reports workflow now has **AI Commentary** (Basic LLM Chain + GEV LLM Model) on top of the rule-based report.
- Invoice drafts workflow in `../n8n_invoice_drafts/`.

## Status
| Piece | State |
|---|---|
| Upload form workflow (`tracker_upload_workflow.json`) | **Works on the company n8n** up to the Data Table step (4,095 rows read and cleaned). Code nodes pass the SQL-keyword scanner. |
| Single flow from OneDrive (`tracker_onedrive_workflow.json`) | Built and tested offline. Not yet run: it depends on connectors and Microsoft sign-in that aren't confirmed yet. |
| Report | Rule-based HTML report (`src/report.js`): monthly, top customers, company codes, daily, data quality. |

## The two unknowns that decide the design
1. **Which nodes are installed.** Confirmed: Code, Extract From File, Data Table, Schedule. Missing: OneDrive and
   Outlook nodes. Unknown: HTTP Request, Microsoft SharePoint, Microsoft Excel 365, Send Email, and the company
   mail node used in *Report copy*.
2. **Whether Microsoft sign-in works without IT.** Open *Credentials → Add → Microsoft Drive OAuth2 API*:
   a plain **Sign in** button means yes; **Client ID / Secret** fields mean an IT request is needed.

## Decision tree
**Reading the tracker** (first one available wins):
1. Microsoft Excel 365 node: reads rows directly, no file download or parsing
2. Microsoft SharePoint node: download the file (the personal OneDrive is a SharePoint site)
3. HTTP Request + Microsoft Graph (current build)
4. Upload form (works today, no Microsoft connector needed)

**Sending the report** (first one available wins):
1. The company mail node from *Report copy*: approved, already in use
2. Send Email (SMTP)
3. HTTP Request + Graph `sendMail` (current build)

## Option that works today with zero new access
Upload form → Read Tracker Sheet → Clean Rows → Summarise → Build Report → **company mail node**.
That's one flow and uses only nodes already confirmed, plus the mail node from *Report copy*. The only manual
step is uploading the file. If the Microsoft connectors turn out to be blocked, build this one.

## Other points to decide
- **Data Table step:** the upsert makes about 4,000 calls per run, which is slow, and the report doesn't need it.
  Keep it only if something else reads the Data Table.
- **Personal OneDrive:** the automation depends on one person's account. Moving the tracker to a team SharePoint
  site is safer long term.
- **AI vs rules:** the rule-based report has deterministic numbers. If narrative commentary is wanted later,
  it can be added on top of the fixed figures, so the numbers never come from the AI.

## To bring tomorrow
1. Which of these appear when searching the node panel: HTTP Request, Microsoft SharePoint, Microsoft Excel 365,
   Send Email
2. The exact name of the email node in *Report copy*
3. What the *Microsoft Drive OAuth2 API* credential screen asks for
4. Data Table column types (e.g. Value: number or string)

## Later additions (agreed)
- **Past due by payment terms**: Tableau has payment-terms days (30 / 60 / 90) and a Net Due Date column; use them per
  invoice (or per customer) instead of a fixed number of days.
- Business type (Nature of Activities PL / PC) and Customer Type (TP / OOB / WOB): skipped until their meaning is confirmed.
