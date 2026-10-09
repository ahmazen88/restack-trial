"""Builds the tracker workflows from the Code-node scripts in src/.

- tracker_upload_workflow.json   : upload the tracker through a form → Data Table (fast: only changed rows)
- tracker_onedrive_workflow.json : OneDrive tracker → Data Table → report email (needs Microsoft access)
- tracker_reports_workflow.json  : upload / request / weekly / monthly → Data Table → report + AI commentary
"""
import json
import uuid
from pathlib import Path

HERE = Path(__file__).parent
UPLOAD_FILE_NAME = "const FILE_NAME = $('Upload Tracker').first().binary?.Tracker_File?.fileName ?? 'tracker';"
ONEDRIVE_FILE_NAME = "const FILE_NAME = $('Pick Tracker File').first().json.name;"
BULK_LIMIT = 300  # same value as in src/compare.js
DATA_TABLE = {'__rl': True, 'mode': 'list', 'value': ''}  # pick "datatable" after import


def js(name):
    return (HERE / 'src' / name).read_text()


def node(prefix, name, type_, version, pos, params, **extra):
    full_type = type_ if '.' in type_ else f'n8n-nodes-base.{type_}'
    return {'parameters': params, 'id': str(uuid.uuid5(uuid.NAMESPACE_URL, prefix + name)), 'name': name,
            'type': full_type, 'typeVersion': version, 'position': pos, **extra}


def sticky(prefix, content, pos, height=300, width=560, name='Setup Notes'):
    return {'parameters': {'width': width, 'height': height, 'content': content},
            'id': str(uuid.uuid5(uuid.NAMESPACE_URL, prefix + name)), 'name': name,
            'type': 'n8n-nodes-base.stickyNote', 'typeVersion': 1, 'position': pos}


def link(a, *targets):
    """a → targets, one output per target list (e.g. If true/false)."""
    return {a: {'main': [[{'node': t, 'type': 'main', 'index': 0} for t in out] for out in targets]}}


def chain(*names):
    out = {}
    for a, b in zip(names, names[1:]):
        out.update(link(a, [b]))
    return out


def if_node(prefix, name, pos, expression):
    return node(prefix, name, 'if', 2.2, pos, {
        'conditions': {
            'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'loose', 'version': 2},
            'conditions': [{'id': str(uuid.uuid5(uuid.NAMESPACE_URL, prefix + name + 'cond')),
                            'leftValue': expression, 'rightValue': '',
                            'operator': {'type': 'boolean', 'operation': 'true', 'singleValue': True}}],
            'combinator': 'and'},
        'options': {}})


def processing(prefix, x, y, binary_property, summary_js):
    """Read sheet → clean → save only what changed → summarise.

    Returns (nodes, connections, first node name, last node name)."""
    n = [
        node(prefix, 'Read Tracker Sheet', 'extractFromFile', 1, [x, y], {
            'operation': 'xlsx', 'binaryPropertyName': binary_property, 'options': {}}),
        node(prefix, 'Clean Rows', 'code', 2, [x + 220, y], {'jsCode': js('clean.js')}),
        node(prefix, 'Get Table Rows', 'dataTable', 1, [x + 440, y], {
            'resource': 'row', 'operation': 'get', 'dataTableId': DATA_TABLE,
            'matchType': 'anyCondition', 'filters': {}, 'returnAll': True}, executeOnce=True, alwaysOutputData=True),
        node(prefix, 'Compare with Table', 'code', 2, [x + 660, y], {'jsCode': js('compare.js')},
             alwaysOutputData=True),
        if_node(prefix, 'Anything to save?', [x + 880, y],
                "={{ $json.Invoice !== undefined && $json.Invoice !== null && $json.Invoice !== '' }}"),
        if_node(prefix, 'Few changes?', [x + 1100, y - 100],
                "={{ $('Get Table Rows').all().some(i => i.json.Invoice !== undefined && i.json.Invoice !== null)"
                f" && $('Compare with Table').all().length <= {BULK_LIMIT} }}}}"),
        node(prefix, 'Save Changed Rows', 'dataTable', 1, [x + 1320, y - 200], {
            'resource': 'row', 'operation': 'upsert', 'dataTableId': DATA_TABLE, 'matchType': 'allConditions',
            'filters': {'conditions': [{'keyName': 'Invoice', 'condition': 'eq', 'keyValue': '={{ $json.Invoice }}'}]},
            'columns': {'mappingMode': 'autoMapInputData', 'value': {}, 'matchingColumns': [], 'schema': []},
            'options': {}}),
        node(prefix, 'Clear Table', 'dataTable', 1, [x + 1320, y], {
            'resource': 'table', 'operation': 'clear', 'dataTableId': DATA_TABLE}, executeOnce=True),
        node(prefix, 'Restore Rows', 'code', 2, [x + 1540, y], {'jsCode': js('restore.js')}),
        node(prefix, 'Bulk Add All Rows', 'dataTable', 1, [x + 1760, y], {
            'resource': 'row', 'operation': 'insert', 'dataTableId': DATA_TABLE,
            'columns': {'mappingMode': 'autoMapInputData', 'value': {}, 'matchingColumns': [], 'schema': []},
            'options': {'optimizeBulk': True}}),
        node(prefix, 'Summarise Upload', 'code', 2, [x + 1980, y - 100], {'jsCode': summary_js}, executeOnce=True),
    ]
    c = {
        **chain('Read Tracker Sheet', 'Clean Rows', 'Get Table Rows', 'Compare with Table', 'Anything to save?'),
        **link('Anything to save?', ['Few changes?'], ['Summarise Upload']),
        **link('Few changes?', ['Save Changed Rows'], ['Clear Table']),
        **chain('Clear Table', 'Restore Rows', 'Bulk Add All Rows', 'Summarise Upload'),
        **link('Save Changed Rows', ['Summarise Upload']),
    }
    return n, c, 'Read Tracker Sheet', 'Summarise Upload'


SAVE_NOTE = ('**Data Table:** pick `datatable` in **Get Table Rows**, **Save Changed Rows**, **Clear Table** and '
             '**Bulk Add All Rows**. Only new or changed invoices are saved (seconds). If the table is empty or more '
             f'than {BULK_LIMIT} rows changed, the table is cleared and all rows are added in one bulk call.')


def upload_workflow():
    p = 'upload-'
    summary_js = js('summary.js')
    assert UPLOAD_FILE_NAME in summary_js
    proc, proc_c, first, last = processing(p, 220, 300, 'Tracker_File', summary_js)
    nodes = [
        node(p, 'Upload Tracker', 'formTrigger', 2.2, [0, 300], {
            'formTitle': 'Upload Production Tracker',
            'formDescription': 'Download the latest tracker (File → Create a Copy → Download a Copy) and upload '
                               'it here. Only new or changed invoices are saved to the Data Table.',
            'formFields': {'values': [{'fieldLabel': 'Tracker File', 'fieldType': 'file', 'multipleFiles': False,
                                       'acceptFileTypes': '.xlsx,.xlsm', 'requiredField': True}]},
            'responseMode': 'lastNode',
            'options': {'path': 'production-tracker-upload', 'buttonLabel': 'Upload'}}),
        *proc,
        node(p, 'Done Page', 'form', 1, [2420, 200], {
            'operation': 'completion', 'respondWith': 'text', 'completionTitle': 'Tracker saved ✔',
            'completionMessage': "={{ $('Summarise Upload').first().json.message }}", 'options': {}}),
        sticky(p, '## Tracker upload → Data Table\n'
                  f'1. {SAVE_NOTE}\n'
                  '2. **Clean Rows** → `COLUMNS` must match the Data Table columns; add tracker headings to `ALIASES`\n'
                  '3. **Read Tracker Sheet** → *Options → Sheet Name* if the data is not on the first tab\n'
                  '4. Publish, then share the form URL from **Upload Tracker** (Production URL)',
               [-40, -140], height=320, width=640),
    ]
    connections = {**link('Upload Tracker', [first]), **proc_c, **link(last, ['Done Page'])}
    return 'Production Tracker – Upload to Data Table', nodes, connections


GRAPH = 'https://graph.microsoft.com/v1.0'


def graph(prefix, name, pos, credential_type, method, url, body=None, options=None):
    """HTTP Request node calling Microsoft Graph with one of the built-in Microsoft credentials."""
    params = {'method': method, 'url': url, 'authentication': 'predefinedCredentialType',
              'nodeCredentialType': credential_type, 'options': options or {}}
    if body is not None:
        params.update({'sendBody': True, 'contentType': 'json', 'specifyBody': 'json', 'jsonBody': body})
    return node(prefix, name, 'httpRequest', 4.2, pos, params)


def onedrive_workflow():
    p = 'onedrive-'
    summary_js = js('summary.js').replace(UPLOAD_FILE_NAME, ONEDRIVE_FILE_NAME)
    proc, proc_c, first, last = processing(p, 880, 300, 'data', summary_js)
    nodes = [
        node(p, 'Weekdays 7am', 'scheduleTrigger', 1.2, [0, 200], {
            'rule': {'interval': [{'field': 'cronExpression', 'expression': '0 7 * * 1-5'}]}}),
        node(p, 'Test Run', 'manualTrigger', 1, [0, 400], {}),
        graph(p, 'Find Tracker', [220, 300], 'microsoftOneDriveOAuth2Api', 'GET',
              GRAPH + "/me/drive/root/search(q='NAM%20Distribution')"),
        node(p, 'Pick Tracker File', 'code', 2, [440, 300], {'jsCode': js('pick.js')}),
        graph(p, 'Download Tracker', [660, 300], 'microsoftOneDriveOAuth2Api', 'GET',
              '=' + GRAPH + '/me/drive/items/{{ $json.id }}/content',
              options={'response': {'response': {'responseFormat': 'file', 'outputPropertyName': 'data'}}}),
        *proc,
        node(p, 'Build Report', 'code', 2, [3080, 200], {'jsCode': js('report.js')}),
        graph(p, 'Send Report', [3300, 200], 'microsoftOutlookOAuth2Api', 'POST', GRAPH + '/me/sendMail',
              body='={{ JSON.stringify($json.mail) }}'),
        node(p, 'Remember Version', 'code', 2, [3520, 200], {'jsCode': js('remember.js')}),
        sticky(p, '## Production Tracker – OneDrive to report (needs Microsoft access from IT)\n'
                  '1. **Find Tracker** & **Download Tracker** → credential *Microsoft Drive OAuth2 API*\n'
                  '2. **Pick Tracker File** → `TRACKER_NAME` must match the file name exactly\n'
                  f'3. {SAVE_NOTE}\n'
                  '4. **Build Report** → `RECIPIENTS`; **Send Report** → *Microsoft Outlook OAuth2 API* '
                  '(or the GEV Send Email node)\n'
                  '5. **Test Run**, then **Publish**', [-40, -160], height=340, width=640),
    ]
    connections = {
        **link('Weekdays 7am', ['Find Tracker']), **link('Test Run', ['Find Tracker']),
        **chain('Find Tracker', 'Pick Tracker File', 'Download Tracker', first),
        **proc_c,
        **chain(last, 'Build Report', 'Send Report', 'Remember Version'),
    }
    return 'Production Tracker – OneDrive to Report', nodes, connections


SYSTEM_PROMPT = """You are a senior accounts-receivable operations analyst at GE Vernova. You write the commentary at the top of the automated INVOICE DISTRIBUTION report read by the billing team and their manager. The team's only job is to distribute invoices (upload them to customer portals or email them) and to clear whatever stops that. This is not a sales report.

RULES
1. Use ONLY the figures in the FACTS JSON. Never invent, estimate, round differently or recalculate numbers – quote them exactly as given.
2. If something is not in the facts, do not mention it. Do not speculate about causes you cannot see in the data.
3. Write the commentary itself. No preamble, no "Here is…", no questions, no offers of further help.
4. Plain business English, short sentences, no hype, no emojis.
5. Always say WHERE: area (La Prairie, Charleroi, Clearwater), company code and, when given, profit centre and product line. Name invoices, owners and categories exactly as in the facts.
6. Never comment on customers' business, volumes as an opportunity, growth or relationships. Never say "past due" (payment terms are not in the data).
7. "NOT FOUND" means the code is missing in the data – mention it only as a data gap.

OUTPUT FORMAT
Return an HTML fragment only – no <html>, <body>, <style>, scripts, images, links or markdown. Use only <h3>, <p>, <ul>, <li> and <b>. Exactly these four sections, in this order:
<h3>Distribution status</h3> 2–3 sentences: received, distributed and the distribution rate for the period; open invoices now, their value and how many need a follow-up; which area or company code holds the most.
<h3>What is holding invoices</h3> up to 5 bullets, biggest first, from rootCauses: the root cause and category, how many invoices and their value, where they sit (area / company code), and the oldest days pending.
<h3>Oldest and stalled items</h3> up to 5 bullets from oldestOpen: invoice number, area / company code, days pending, root cause, last action and days since it, and owner.
<h3>Actions for today</h3> up to 5 concrete bullets (e.g. chase a named owner's follow-ups, escalate a root cause in a company code, fill in the data gaps). Each must follow directly from a fact above.
Keep the whole commentary under 300 words. If the facts say "empty": true, write one <p> saying there is no data for this selection."""

USER_PROMPT = """=Report: {{ $json.subject }}

FACTS (JSON – the only source you may use):
{{ $json.facts }}

Write the commentary now, following the output format exactly."""

CHART_SYSTEM_PROMPT = """You are a data-visualisation designer for the INVOICE DISTRIBUTION report of a GE Vernova billing team. The team's only job is to get invoices distributed (uploaded to customer portals or emailed). You choose the charts that show, at a glance, what is stuck, why, where and for how long.

You do NOT draw charts and you do NOT write numbers. A program draws each chart you choose from the real data.

AVAILABLE DATASETS (only these; each must exist in FACTS.charts with at least 2 entries)
openByArea, openByCompanyCode, openByProfitCentre, openByProductLine (open invoices by where they sit) · rootCauses (open invoices by root cause) · ageing (open invoices by days pending, keep its order) · weeklyIncoming (invoices received per week, time series) · distributedByArea (metric "invoices" only)
METRICS: "invoices" (count) or "value"
CHART TYPES: "bar" (rankings and splits), "column" (ageing, weeks), "line" (weeklyIncoming only)

HOW TO CHOOSE
1. Pick 3 or 4 charts, most useful first, for someone deciding today which invoices to chase: the root causes, where the open invoices sit (area / company code / profit centre), how old they are, and incoming workload.
2. Do not pick two charts that show the same thing. Skip a split where one entry is almost everything or where "NOT FOUND" dominates.
3. This is not a sales report: never talk about customers' business, growth or opportunities. Never call anything "past due" (payment terms are not in the data).
4. For each chart write a short title and a "why" of at most 20 words, with NO digits or numbers.

OUTPUT
Return ONLY a JSON array, no other text, no code fences. Example:
[{"title":"What is holding invoices","dataset":"rootCauses","metric":"invoices","chart":"bar","why":"PO issues on the portal hold most of the open invoices"}]"""

CHART_USER_PROMPT = """=Report: {{ $json.subject }}

FACTS (JSON):
{{ $json.facts }}

Choose the charts now. Return only the JSON array."""

BLOCKER_SYSTEM_PROMPT = """You classify why an invoice is still pending, for an accounts-receivable billing team at GE Vernova. Each item is the tracker's Category and Reason for Pending text.

Choose exactly ONE category per item from this list, copied exactly:
- PO not available on portal (PO missing, not created, not visible or not yet released on the customer portal)
- PO lines not available on portal (the PO exists but the needed lines or line items are missing)
- PO cancelled or closed
- PO line and invoice line mismatch
- Price and quantity mismatch
- Quantity mismatch
- Price mismatch
- Amount, tax or freight mismatch (totals, tax, tariff, freight or other charges do not match or are missing on the PO)
- No portal access / portal migration (no login, access request, customer moved to another portal)
- Unable to submit invoice on portal (the portal rejects or will not let the invoice be submitted, cause not stated)
- Other (none of the above clearly fits)

RULES
1. Decide from the words given only. Do not guess a cause that is not written.
2. When the text names a cause and a symptom, choose the cause.
3. Return ONLY a JSON array, no other text, no code fences: [{"id":1,"category":"Quantity mismatch"}]
4. Include every id exactly once. If the list is empty, return []."""

BLOCKER_USER_PROMPT = """=Items (JSON, each has an id and the text):
{{ $json.items }}

Return only the JSON array."""


def reports_workflow():
    """Upload the tracker, request a report, or get weekly/monthly reports – with AI commentary."""
    p = 'reports-'
    proc, proc_c, first, last = processing(p, 220, 0, 'Tracker_File', js('summary.js'))
    received = {'values': {'respondWith': 'text'}}
    send = 'Send Report – paste GEV Send Email here'
    nodes = [
        node(p, 'Upload Tracker', 'formTrigger', 2.2, [0, 0], {
            'formTitle': 'Upload Production Tracker',
            'formDescription': 'Download the latest tracker (File → Create a Copy → Download a Copy) and upload '
                               'it here. The data is saved and an overview report is emailed to you.',
            'formFields': {'values': [{'fieldLabel': 'Tracker File', 'fieldType': 'file', 'multipleFiles': False,
                                       'acceptFileTypes': '.xlsx,.xlsm', 'requiredField': True}]},
            'responseMode': 'onReceived',
            'options': {'path': 'production-tracker-upload', 'buttonLabel': 'Upload',
                        'respondWithOptions': {'values': {
                            'respondWith': 'text',
                            'formSubmittedText': 'Upload received ✔ The data is being saved now – the report with '
                                                 'the upload results arrives by email in a few minutes. You can '
                                                 'close this page.'}}}}),
        *proc,
        node(p, 'Request a Report', 'formTrigger', 2.2, [0, 420], {
            'formTitle': 'Production Tracker – Request a Report',
            'formDescription': 'Choose the period and filters. The report is emailed to you with an interactive '
                               'dashboard attached. Leave fields empty for everything.',
            'formFields': {'values': [
                {'fieldLabel': 'Report type', 'fieldType': 'dropdown', 'requiredField': True,
                 'fieldOptions': {'values': [{'option': o} for o in
                                             ['Overview', 'Weekly', 'Monthly', 'Custom period']]}},
                {'fieldLabel': 'From', 'fieldType': 'date'},
                {'fieldLabel': 'To', 'fieldType': 'date'},
                {'fieldLabel': 'Company code (optional)', 'placeholder': 'e.g. 3485'},
                {'fieldLabel': 'Customer contains (optional)', 'placeholder': 'e.g. SALT RIVER'},
                {'fieldLabel': 'Send to (optional)', 'fieldType': 'email', 'placeholder': 'name.surname@company.com'},
            ]},
            'responseMode': 'onReceived',
            'options': {'path': 'production-tracker-report', 'buttonLabel': 'Generate report',
                        'respondWithOptions': {'values': {
                            'respondWith': 'text',
                            'formSubmittedText': 'Request received ✔ Your report arrives by email in a few minutes. '
                                                 'You can close this page.'}}}}),
        node(p, 'Every Monday 7am', 'scheduleTrigger', 1.2, [0, 600], {
            'rule': {'interval': [{'field': 'cronExpression', 'expression': '0 7 * * 1'}]}}),
        node(p, '1st of Month 7am', 'scheduleTrigger', 1.2, [0, 780], {
            'rule': {'interval': [{'field': 'cronExpression', 'expression': '0 7 1 * *'}]}}),
        node(p, 'Get All Rows', 'dataTable', 1, [2420, 420], {
            'resource': 'row', 'operation': 'get', 'dataTableId': DATA_TABLE,
            'matchType': 'anyCondition', 'filters': {}, 'returnAll': True}, executeOnce=True, alwaysOutputData=True),
        node(p, 'Report Settings', 'code', 2, [2640, 420], {'jsCode': js('settings.js')}),
        node(p, 'Build Report', 'code', 2, [2860, 420], {'jsCode': js('analytics.js')}),
        node(p, 'AI Commentary', '@n8n/n8n-nodes-langchain.chainLlm', 1.7, [3080, 420], {
            'promptType': 'define', 'text': USER_PROMPT, 'hasOutputParser': False,
            'messages': {'messageValues': [{'type': 'SystemMessagePromptTemplate', 'message': SYSTEM_PROMPT}]},
            'batching': {}},
            retryOnFail=True, maxTries=2, waitBetweenTries=3000, onError='continueRegularOutput'),
        node(p, 'Add AI Commentary', 'code', 2, [3300, 420], {'jsCode': js('commentary.js')}),
        node(p, send, 'noOp', 1, [3520, 420], {}),
        sticky(p, '## Production Tracker – upload, reports, dashboard & AI commentary\n'
                  f'1. {SAVE_NOTE} Also pick it in **Get All Rows**.\n'
                  '2. **Build Report** → default recipients in `RECIPIENTS`\n'
                  '3. **AI Commentary** → connect a chat model to its *Model* input: copy a **GEV LLM Model** node '
                  'from *Report copy*. Set its temperature to 0.1–0.2 for steady, factual wording.\n'
                  f'4. Replace **{send}**: copy *Send an Email* from *Report copy*, connect Add AI Commentary → it, '
                  'set To `{{ $json.to }}`, Subject `{{ $json.subject }}`, Email Format HTML, HTML `{{ $json.html }}`, '
                  'Attachments `dashboard`\n'
                  '5. Publish. Share the two form links. Forms answer immediately; results arrive by email.\n\n'
                  '**Runs**: upload (overview) · request (your period & filters) · Mondays 07:00 (weekly) · '
                  '1st of month 07:00 (monthly)', [-40, -520], height=440, width=700),
        sticky(p, '### AI prompt settings\nThe AI writes **commentary only** (summary, what needs attention, '
                  'workload outlook, suggested actions) from the fixed figures in `facts`. All numbers in the '
                  'report itself are calculated by rules, not by the AI. If the AI fails, the report is still sent.',
               [3020, 620], height=200, width=420, name='AI Notes'),
    ]
    connections = {
        **link('Upload Tracker', [first]), **proc_c, **link(last, ['Get All Rows']),
        **link('Request a Report', ['Get All Rows']),
        **link('Every Monday 7am', ['Get All Rows']),
        **link('1st of Month 7am', ['Get All Rows']),
        **chain('Get All Rows', 'Report Settings', 'Build Report', 'AI Commentary', 'Add AI Commentary', send),
    }
    return 'Production Tracker – Upload, Reports & AI Commentary', nodes, connections


def simple_workflow():
    """ONE start (upload form) → one straight line → ONE end (Done page). No branches, no options."""
    p = 'simple-'
    send = '⬜ Send Report – paste "Send an Email" here'
    report_js = (js('analytics.js')
                 .replace("const settings = $('Report Settings').first().json;",
                          "const settings = { type: 'Overview', source: 'form' };")
                 .replace("$('Get All Rows').all()", "$('Add Lookups').all()"))
    y = 300
    names = ['Upload Tracker', 'Read Tracker Sheet', 'Clean Rows',
             'Pick ZSD File', 'Read ZSD Log', 'Pick ZSD File Again', 'Read ZSD 2025 Sheet',
             'Pick Tableau File', 'Read Tableau Extract', 'Check Table', 'Standard Blockers', 'AI Blocker Classifier', 'Add Lookups', 'Safety Check', 'Clear Table',
             'Rows to Save', 'Save All Rows',
             'Summarise Upload', 'Build Report', 'AI Commentary', 'Add AI Commentary',
             'AI Chart Designer', 'Add AI Charts', send, 'Done Page']
    pos = {n: [220 * i, y] for i, n in enumerate(names)}
    nodes = [
        node(p, 'Upload Tracker', 'formTrigger', 2.2, pos['Upload Tracker'], {
            'formTitle': 'Upload Production Tracker',
            'formDescription': 'Upload the latest tracker (.xlsx). It is saved to the Data Table and the report '
                               'is emailed to you. The ZSD log and the Tableau extract are optional: add them '
                               'to fill in SAP customer code and profit centre. Please wait on this page until it '
                               'says Done.',
            'formFields': {'values': [
                {'fieldLabel': 'Tracker File', 'fieldType': 'file', 'multipleFiles': False,
                 'acceptFileTypes': '.xlsx,.xlsm', 'requiredField': True},
                {'fieldLabel': 'ZSD Log', 'fieldType': 'file', 'multipleFiles': False,
                 'acceptFileTypes': '.xlsx,.xlsm', 'requiredField': False},
                {'fieldLabel': 'Tableau Extract', 'fieldType': 'file', 'multipleFiles': False,
                 'acceptFileTypes': '.xlsx,.xlsm', 'requiredField': False}]},
            'responseMode': 'lastNode',
            'options': {'path': 'production-tracker', 'buttonLabel': 'Upload'}}),
        node(p, 'Read Tracker Sheet', 'extractFromFile', 1, pos['Read Tracker Sheet'], {
            'operation': 'xlsx', 'binaryPropertyName': 'Tracker_File', 'options': {}},
             alwaysOutputData=True),  # an empty sheet still reaches Clean Rows, which explains the problem
        node(p, 'Clean Rows', 'code', 2, pos['Clean Rows'], {'jsCode': js('clean.js')}),
        # optional files: each read step gets the uploaded files again; a missing file or sheet is skipped
        node(p, 'Pick ZSD File', 'code', 2, pos['Pick ZSD File'], {'jsCode': js('pick_file.js')}, executeOnce=True),
        node(p, 'Read ZSD Log', 'extractFromFile', 1, pos['Read ZSD Log'], {
            'operation': 'xlsx', 'binaryPropertyName': 'ZSD_Log', 'options': {}},
             alwaysOutputData=True, onError='continueRegularOutput'),
        node(p, 'Pick ZSD File Again', 'code', 2, pos['Pick ZSD File Again'], {'jsCode': js('pick_file.js')},
             executeOnce=True),
        node(p, 'Read ZSD 2025 Sheet', 'extractFromFile', 1, pos['Read ZSD 2025 Sheet'], {
            'operation': 'xlsx', 'binaryPropertyName': 'ZSD_Log', 'options': {'sheetName': '2025 Inv Processed'}},
             alwaysOutputData=True, onError='continueRegularOutput'),
        node(p, 'Pick Tableau File', 'code', 2, pos['Pick Tableau File'], {'jsCode': js('pick_file.js')},
             executeOnce=True),
        node(p, 'Read Tableau Extract', 'extractFromFile', 1, pos['Read Tableau Extract'], {
            'operation': 'xlsx', 'binaryPropertyName': 'Tableau_Extract', 'options': {}},
             alwaysOutputData=True, onError='continueRegularOutput'),
        node(p, 'Check Table', 'dataTable', 1, pos['Check Table'], {
            'resource': 'row', 'operation': 'get', 'dataTableId': DATA_TABLE,
            'matchType': 'anyCondition', 'filters': {}, 'returnAll': True},
             executeOnce=True, alwaysOutputData=True),
        node(p, 'Standard Blockers', 'code', 2, pos['Standard Blockers'], {'jsCode': js('blockers.js')}, executeOnce=True),
        node(p, 'AI Blocker Classifier', '@n8n/n8n-nodes-langchain.chainLlm', 1.7, pos['AI Blocker Classifier'], {
            'promptType': 'define', 'text': BLOCKER_USER_PROMPT, 'hasOutputParser': False,
            'messages': {'messageValues': [{'type': 'SystemMessagePromptTemplate', 'message': BLOCKER_SYSTEM_PROMPT}]},
            'batching': {}},
            retryOnFail=True, maxTries=2, waitBetweenTries=3000, onError='continueRegularOutput'),
        node(p, 'Add Lookups', 'code', 2, pos['Add Lookups'], {'jsCode': js('lookups.js')}, executeOnce=True),
        node(p, 'Safety Check', 'code', 2, pos['Safety Check'], {'jsCode': js('safety.js')}),
        node(p, 'Clear Table', 'dataTable', 1, pos['Clear Table'], {
            'resource': 'table', 'operation': 'clear', 'dataTableId': DATA_TABLE}, executeOnce=True),
        node(p, 'Rows to Save', 'code', 2, pos['Rows to Save'], {'jsCode': js('restore_lookups.js')}),
        node(p, 'Save All Rows', 'dataTable', 1, pos['Save All Rows'], {
            'resource': 'row', 'operation': 'insert', 'dataTableId': DATA_TABLE,
            'columns': {'mappingMode': 'autoMapInputData', 'value': {}, 'matchingColumns': [], 'schema': []},
            'options': {'optimizeBulk': True}}),
        node(p, 'Summarise Upload', 'code', 2, pos['Summarise Upload'], {'jsCode': js('summary.js')},
             executeOnce=True),
        node(p, 'Build Report', 'code', 2, pos['Build Report'], {'jsCode': report_js}),
        node(p, 'AI Commentary', '@n8n/n8n-nodes-langchain.chainLlm', 1.7, pos['AI Commentary'], {
            'promptType': 'define', 'text': USER_PROMPT, 'hasOutputParser': False,
            'messages': {'messageValues': [{'type': 'SystemMessagePromptTemplate', 'message': SYSTEM_PROMPT}]},
            'batching': {}},
            retryOnFail=True, maxTries=2, waitBetweenTries=3000, onError='continueRegularOutput'),
        node(p, 'Add AI Commentary', 'code', 2, pos['Add AI Commentary'], {'jsCode': js('commentary.js')}),
        node(p, 'AI Chart Designer', '@n8n/n8n-nodes-langchain.chainLlm', 1.7, pos['AI Chart Designer'], {
            'promptType': 'define', 'text': CHART_USER_PROMPT, 'hasOutputParser': False,
            'messages': {'messageValues': [{'type': 'SystemMessagePromptTemplate', 'message': CHART_SYSTEM_PROMPT}]},
            'batching': {}},
            retryOnFail=True, maxTries=2, waitBetweenTries=3000, onError='continueRegularOutput'),
        node(p, 'Add AI Charts', 'code', 2, pos['Add AI Charts'], {'jsCode': js('charts.js')}),
        node(p, send, 'noOp', 1, pos[send], {}),
        node(p, 'Done Page', 'form', 1, pos['Done Page'], {
            'operation': 'completion', 'respondWith': 'text', 'completionTitle': 'Done ✔',
            'completionMessage': "={{ $('Build Report').first().json.doneMessage }}", 'options': {}}),
        sticky(p, '## Setup – 5 steps\n'
                  '0. In the Data Table `datatable` add these 12 columns, all type *string*: `Status`, `Upload_Date`, '
                  '`Tracker_TAT`, `Uploaded_By`, `Pending_Category`, `Pending_Reason`, `Standard_Category`, `Sales_Org`, '
                  '`SAP_Customer_Code`, `Profit_Center`, `Product_Line`, `Business_Type`\n'
                  '1. **Check Table**, **Clear Table** and **Save All Rows** → Data table: choose `datatable` (all three)\n'
                  '2. **Build Report** → in the `RECIPIENTS` line at the top, put your email between the quotes\n'
                  '3. From *Report copy* copy **GEV LLM Model** → paste it here **three times** → connect one to the *Model* '
                  'dot under each AI step: **AI Blocker Classifier**, **AI Commentary**, **AI Chart Designer** '
                  '(temperature 0 for the classifier, 0.1–0.2 for the others)\n'
                  '4. From *Report copy* copy **Send an Email** → paste here → put it in place of the grey box '
                  '(connect Add AI Charts → Send an Email → Done Page, delete the grey box) and fill in: '
                  'To `{{ $json.to }}` · Subject `{{ $json.subject }}` · Email Format `HTML` · '
                  'HTML `{{ $json.html }}` · Attachments `dashboard`\n'
                  '5. **Publish** → open **Upload Tracker** → copy the *Production URL* → open it and upload the tracker',
               [0, -160], height=400, width=900),
    ]
    return 'Production Tracker', nodes, chain(*names)


if __name__ == '__main__':
    for filename, (name, nodes, connections) in [('tracker_upload_workflow.json', upload_workflow()),
                                                 ('tracker_onedrive_workflow.json', onedrive_workflow()),
                                                 ('tracker_reports_workflow.json', reports_workflow()),
                                                 ('production_tracker.json', simple_workflow())]:
        workflow = {'name': name, 'nodes': nodes, 'connections': connections, 'pinData': {},
                    'settings': {'executionOrder': 'v1'}, 'active': False, 'tags': []}
        (HERE / filename).write_text(json.dumps(workflow, indent=2, ensure_ascii=False) + '\n')
        print('wrote', filename, 'with', len(nodes), 'nodes')
