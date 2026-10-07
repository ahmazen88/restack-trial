# Where we are and what to do next

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
