# n8n workflow pack: sales, inbox and AI agents

There are 12 workflows here. Each one is a JSON file that you import into n8n (**Workflows → Import from file**, or paste the JSON onto the canvas). They are built to work together and share one Google Sheet that acts as the CRM.

| # | Workflow | Trigger | What it does for you |
|---|---|---|---|
| 01 | Lead intake → qualify → reply → CRM | Webhook `/lead-intake` | Reads the lead's website. Claude scores the lead 0–100 and writes a personalised reply in under a minute (sent or saved as a draft). Adds or updates the row in **Leads** and alerts you about hot leads. |
| 02 | Smart follow-up sequence | Weekdays 09:10 | Sends touches 2 to 4, each from a different angle (value, then proof, then break-up). Before sending, it checks Gmail and **stops for anyone who replied**. |
| 03 | Invoice reminders and dunning | Daily 08:40 | Works through a ladder: 3 days before due, due date, +7, +14, then a final notice at +30. Each stage is sent only once, from fixed templates with no AI. You get a daily summary. |
| 04 | Meeting booked → pre-call brief | Calendly, Cal.com or JSON webhook `/meeting-booked` | Reads the booker's website and your CRM, then emails you a one-page brief with discovery questions, objections to expect and a price anchor. |
| 05 | Project done → feedback → reviews | Webhook `/project-complete` | Emails the client a 2-question form. A 4–5★ answer gets your review link and a referral ask. A score of 3★ or lower puts a recovery draft in your Gmail and alerts you. |
| 06 | AI inbox triage | Every new email | Assigns a category, urgency and labels. Saves a **reply draft in the thread** when one is needed. New leads go to 01, known leads are marked `replied`, and noise is marked read. |
| 07 | Morning brief | Weekdays 07:30 | One email covering your top 3 for the day, who to reply to, the pipeline, overdue money and what you can ignore. |
| 08 | Invoice and receipt extractor | Email with a PDF attached | Pulls out vendor, dates, tax, total and category, then adds a row to **Ledger**. Reminds you about bills due within 7 days. |
| 09 | **JSON-by-email command center** | Email with subject `[n8n]` | Email JSON to run any workflow in this pack. It handles batches and replies with the results. |
| 10 | Research agent | Webhook `/research` (or 09) | A Claude agent searches the web, reads pages, checks the numbers and emails you a cited HTML report. |
| 11 | Draft → your approval → send | Support inbox or webhook `/draft-with-approval` | Claude drafts a reply from your knowledge base and sends you **Approve / Request changes** buttons by email. If you ask for changes, it revises and asks again. |
| 12 | Error alerts | Any workflow failure | Emails you the workflow, the node, the error and a link to the execution. |

---

## Setup (about 15 minutes)

1. **Credentials** (n8n → Credentials): **Gmail OAuth2**, **Google Sheets OAuth2** and **Anthropic**. Workflow 10 also needs a **SerpAPI** key. After importing, open each red-flagged node and pick the credential.
2. **Create one Google Sheet** with the tabs and header rows below. Copy its ID from the URL (`docs.google.com/spreadsheets/d/<THIS_PART>/edit`).
3. **Fill in the `Config` node** at the start of each workflow. Every value you need to edit is in that node: your email, sheet ID, booking link, offer description, label IDs and webhook URLs.
4. **Workflow 12 first.** Activate it, then in every other workflow go to **Settings → Error workflow → "12 · Error Alerts"**.
5. Activate the workflows. Webhook URLs look like `https://YOUR-N8N/webhook/lead-intake`. Put those URLs into the Config of 06 and 09 so the workflows can call each other.

Model: all AI nodes use `claude-sonnet-5-5`. You can change it in any "Claude (…)" node. A cheaper model such as `claude-haiku-5-5` works fine for 06 and 08.

### Google Sheet tabs and headers (row 1)

```
Leads      email | name | company | website | phone | source | budget | timeline | message | score | tier | intent | summary | next_step | stage | touches | last_contacted | next_follow_up | thread_id | created_at | notes
Invoices   invoice_id | client_name | client_email | amount | currency | issue_date | due_date | status | pay_link | last_reminder_stage | last_reminder_at | notes
Ledger     logged_at | doc_type | vendor | invoice_number | issue_date | due_date | currency | subtotal | tax | total | category | description | status | confidence | needs_review | from | file | email_link
Feedback   at | client_name | client_email | project | rating | comment | responded
InboxLog   received | from | subject | category | urgency | summary | needs_reply | known_lead | thread
```

Lead `stage` values: `new`, `contacted`, `proposal_sent`, `replied`, `meeting_booked`, `nurture`, `won`, `lost`. Set `won` or `lost` yourself. The workflows set the rest.
Invoice `status`: set it to `paid`, `void`, `disputed` or `paused` to stop reminders.

### Gmail label IDs (workflows 06 and 08)

Create the labels in Gmail (for example `AI/Lead`, `AI/Client`, `AI/Billing`, `AI/Support`, `AI/Scheduling`, `AI/FYI`, `AI/Needs reply`, `AI/Processed`). To get their IDs, run any Gmail node with **Label → Get Many**, then paste the `Label_…` IDs into Config. Any label ID left as a placeholder is skipped, so nothing breaks.

---

## Sending JSON by email (workflow 09)

Send an email **from an address listed in `allowedSenders`** with a subject that starts with `[n8n]`. Put the JSON anywhere in the body; a ```` ```json ```` fence and your signature are fine. The `token` must match the token in Config, because the From address can be faked.

**Add a lead (runs 01: scored, replied to and saved to the CRM)**
```json
{"token":"YOUR_SECRET","action":"add_lead",
 "data":{"name":"Jane Doe","email":"jane@acme.com","company":"Acme","website":"acme.com",
         "message":"Met at the conference, wants a quote for Q1","budget":"20k","source":"event"}}
```

**Batch: several leads in one email**
```json
{"token":"YOUR_SECRET","action":"add_lead","data":[
  {"name":"Jane Doe","email":"jane@acme.com","message":"pricing"},
  {"name":"Raj Patel","email":"raj@globex.io","message":"demo next week"}]}
```

**Several different actions in one email**
```json
[{"token":"YOUR_SECRET","action":"research","data":{"question":"Top 5 competitors of Globex and their pricing","depth":"deep"}},
 {"token":"YOUR_SECRET","action":"project_complete","data":{"client_name":"Ann Lee","client_email":"ann@initech.com","project":"Brand refresh"}}]
```

**Pre-call brief for a call you booked by hand**
```json
{"token":"YOUR_SECRET","action":"meeting_brief",
 "data":{"name":"Raj Patel","email":"raj@globex.io","start_time":"2026-10-20T15:00:00Z","notes":"Wants to cut onboarding time"}}
```

**Get an AI draft to approve before it goes out (runs 11)**
```json
{"token":"YOUR_SECRET","action":"approve_reply",
 "data":{"from":"customer@client.com","name":"Chris","subject":"Refund?","body":"I was charged twice this month."}}
```

You'll get a reply such as `✅ add_lead {...}` or `❌ …` for each item. If the JSON is invalid or the action is unknown, the reply tells you what went wrong and shows the correct format. Emails from senders not on the list, or with the wrong token, are ignored silently.

To add your own action, add `"name": "https://YOUR-N8N/webhook/path"` to `routes` in Config.

---

## Calling the webhooks directly

```bash
curl -X POST https://YOUR-N8N/webhook/lead-intake -H 'Content-Type: application/json' \
  -d '{"name":"Jane","email":"jane@acme.com","company":"Acme","message":"Need a new website"}'
```

01 also understands common form-builder field names (`full_name`, `email_address`, `url`, `details`, `utm_source`, …). That lets you point Tally, Typeform, Webflow or Framer webhooks straight at it.
04 takes Calendly `invitee.created` and Cal.com `BOOKING_CREATED` payloads as they are.

## How they chain together

```
email in ─► 06 triage ─┬─ new lead ─────────► 01 qualify + reply ─► Leads ─► 02 follow-ups ─┐
                       ├─ lead replied ─────► Leads.stage = replied ─────────(02 stops)◄─────┘
                       └─ needs reply ──────► draft in thread
booking ─► 04 brief ─► Leads.stage = meeting_booked
PDF bill ─► 08 ─► Ledger            Invoices ─► 03 dunning
all of it ─► 07 morning brief       anything ─► 09 (JSON by email) ─► any webhook
```

## Safety defaults

- 01 has `replyMode`. Set it to `draft` until you trust the replies, then switch to `send`.
- 06 never sends anything. It only saves drafts.
- 03 never uses AI for money emails. It only sends on a stage it hasn't sent before, and never goes back down the ladder.
- 11 never sends without your click, and stops after `maxRounds` revisions.
- 09 needs both an allowed sender and a token.
