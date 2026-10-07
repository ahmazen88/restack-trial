"""Builds both tracker workflows from the Code-node scripts in src/.

- tracker_upload_workflow.json   : manual upload through an n8n form
- tracker_onedrive_workflow.json : scheduled, reads the tracker straight from OneDrive
"""
import json
import uuid
from pathlib import Path

HERE = Path(__file__).parent
UPLOAD_FILE_NAME = "const FILE_NAME = $('Upload Tracker').first().binary?.Tracker_File?.fileName ?? 'tracker';"
ONEDRIVE_FILE_NAME = "const FILE_NAME = $('Pick Tracker File').first().json.name;"


def js(name):
    return (HERE / 'src' / name).read_text()


def node(prefix, name, type_, version, pos, params, **extra):
    return {'parameters': params, 'id': str(uuid.uuid5(uuid.NAMESPACE_URL, prefix + name)), 'name': name,
            'type': f'n8n-nodes-base.{type_}', 'typeVersion': version, 'position': pos, **extra}


def sticky(prefix, content, pos, height=300):
    return {'parameters': {'width': 560, 'height': height, 'content': content},
            'id': str(uuid.uuid5(uuid.NAMESPACE_URL, prefix + 'sticky')), 'name': 'Setup Notes',
            'type': 'n8n-nodes-base.stickyNote', 'typeVersion': 1, 'position': pos}


def processing_nodes(prefix, x, binary_property, summary_js):
    """Read sheet → clean → upsert → summarise: identical in both workflows."""
    return [
        node(prefix, 'Read Tracker Sheet', 'extractFromFile', 1, [x, 300], {
            'operation': 'xlsx', 'binaryPropertyName': binary_property, 'options': {}}),
        node(prefix, 'Clean Rows', 'code', 2, [x + 220, 300], {'jsCode': js('clean.js')}),
        node(prefix, 'Upsert into Data Table', 'dataTable', 1, [x + 440, 300], {
            'resource': 'row', 'operation': 'upsert',
            'dataTableId': {'__rl': True, 'mode': 'list', 'value': ''},
            'matchType': 'allConditions',
            'filters': {'conditions': [{'keyName': 'Invoice', 'condition': 'eq',
                                        'keyValue': '={{ $json.Invoice }}'}]},
            'columns': {'mappingMode': 'autoMapInputData', 'value': {}, 'matchingColumns': [], 'schema': []},
            'options': {}}),
        node(prefix, 'Summarise Upload', 'code', 2, [x + 660, 300], {'jsCode': summary_js}),
    ]


def refresh_report(prefix, x):
    return node(prefix, 'Refresh Report', 'executeWorkflow', 1.2, [x, 300], {
        'source': 'database',
        'workflowId': {'__rl': True, 'mode': 'list', 'value': ''},
        'workflowInputs': {'mappingMode': 'defineBelow', 'value': {}, 'matchingColumns': [], 'schema': [],
                           'attemptToConvertTypes': False, 'convertFieldsToString': True},
        'mode': 'once',
        'options': {'waitForSubWorkflow': False}})


def chain(*names):
    return {a: {'main': [[{'node': b, 'type': 'main', 'index': 0}]]} for a, b in zip(names, names[1:])}


def upload_workflow():
    p = 'upload-'
    summary_js = js('summary.js')
    assert UPLOAD_FILE_NAME in summary_js
    nodes = [
        node(p, 'Upload Tracker', 'formTrigger', 2.2, [0, 300], {
            'formTitle': 'Upload Production Tracker',
            'formDescription': 'Download the latest tracker from SharePoint (File → Create a Copy → Download a Copy) '
                               'and upload it here. The Production Intelligence Report refreshes automatically.',
            'formFields': {'values': [{'fieldLabel': 'Tracker File', 'fieldType': 'file', 'multipleFiles': False,
                                       'acceptFileTypes': '.xlsx,.xlsm', 'requiredField': True}]},
            'responseMode': 'lastNode',
            'options': {'path': 'production-tracker-upload', 'buttonLabel': 'Upload & refresh report'}}),
        *processing_nodes(p, 220, 'Tracker_File', summary_js),
        refresh_report(p, 1100),
        node(p, 'Done Page', 'form', 1, [1320, 300], {
            'operation': 'completion', 'respondWith': 'text',
            'completionTitle': 'Tracker uploaded ✔',
            'completionMessage': "={{ $('Summarise Upload').first().json.message }}. "
                                 "The report is being generated and will arrive by email shortly.",
            'options': {}}),
        sticky(p, '## Tracker upload – setup\n'
                  '1. **Upsert into Data Table** → pick your Data Table\n'
                  '2. **Clean Rows** → check `COLUMNS` matches the Data Table columns exactly; '
                  'add tracker headings to `ALIASES`\n'
                  '3. **Read Tracker Sheet** → *Options → Sheet Name* if the data is not on the first tab\n'
                  '4. **Refresh Report** → pick *Report copy* (it needs a *When Executed by Another Workflow* '
                  'trigger)\n'
                  '5. Publish, then share the form URL from **Upload Tracker** (Production URL)', [-40, -40]),
    ]
    connections = chain('Upload Tracker', 'Read Tracker Sheet', 'Clean Rows', 'Upsert into Data Table',
                        'Summarise Upload', 'Refresh Report', 'Done Page')
    return 'Production Tracker – Upload from SharePoint', nodes, connections


def onedrive_workflow():
    p = 'onedrive-'
    summary_js = js('summary.js').replace(UPLOAD_FILE_NAME, ONEDRIVE_FILE_NAME)
    nodes = [
        node(p, 'Weekdays 7am', 'scheduleTrigger', 1.2, [0, 200], {
            'rule': {'interval': [{'field': 'cronExpression', 'expression': '0 7 * * 1-5'}]}}),
        node(p, 'Test Run', 'manualTrigger', 1, [0, 400], {}),
        node(p, 'Find Tracker', 'microsoftOneDrive', 1.1, [220, 300], {
            'resource': 'file', 'operation': 'search', 'query': 'NAM Distribution'}),
        node(p, 'Pick Tracker File', 'code', 2, [440, 300], {'jsCode': js('pick.js')}),
        node(p, 'Download Tracker', 'microsoftOneDrive', 1.1, [660, 300], {
            'resource': 'file', 'operation': 'download', 'fileId': '={{ $json.id }}',
            'binaryPropertyName': 'data'}),
        *processing_nodes(p, 880, 'data', summary_js),
        node(p, 'Remember Version', 'code', 2, [1760, 300], {'jsCode': js('remember.js')}),
        refresh_report(p, 1980),
        sticky(p, '## Tracker from OneDrive – setup\n'
                  '1. **Find Tracker** & **Download Tracker** → credential *Microsoft Drive OAuth2 API* '
                  '(sign in with your GE account)\n'
                  '2. **Pick Tracker File** → `TRACKER_NAME` must match the file name exactly\n'
                  '3. **Upsert into Data Table** → pick your Data Table\n'
                  '4. **Refresh Report** → pick *Report copy*\n'
                  '5. Click **Test Run** once, then **Publish** – it then runs weekdays at 07:00 '
                  '(timezone: Workflow settings) and skips days when the file has not changed', [-40, -120]),
    ]
    connections = {
        'Weekdays 7am': {'main': [[{'node': 'Find Tracker', 'type': 'main', 'index': 0}]]},
        'Test Run': {'main': [[{'node': 'Find Tracker', 'type': 'main', 'index': 0}]]},
        **chain('Find Tracker', 'Pick Tracker File', 'Download Tracker', 'Read Tracker Sheet', 'Clean Rows',
                'Upsert into Data Table', 'Summarise Upload', 'Remember Version', 'Refresh Report'),
    }
    return 'Production Tracker – Scheduled from OneDrive', nodes, connections


if __name__ == '__main__':
    for filename, (name, nodes, connections) in [('tracker_upload_workflow.json', upload_workflow()),
                                                 ('tracker_onedrive_workflow.json', onedrive_workflow())]:
        workflow = {'name': name, 'nodes': nodes, 'connections': connections, 'pinData': {},
                    'settings': {'executionOrder': 'v1'}, 'active': False, 'tags': []}
        (HERE / filename).write_text(json.dumps(workflow, indent=2, ensure_ascii=False) + '\n')
        print('wrote', filename, 'with', len(nodes), 'nodes')
