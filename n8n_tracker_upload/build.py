"""Builds tracker_upload_workflow.json from the Code-node scripts in src/."""
import json
import uuid
from pathlib import Path

HERE = Path(__file__).parent


def js(name):
    return (HERE / 'src' / name).read_text()


def node(name, type_, version, pos, params, **extra):
    return {'parameters': params, 'id': str(uuid.uuid5(uuid.NAMESPACE_URL, 'upload-' + name)), 'name': name,
            'type': f'n8n-nodes-base.{type_}', 'typeVersion': version, 'position': pos, **extra}


nodes = [
    node('Upload Tracker', 'formTrigger', 2.2, [0, 300], {
        'formTitle': 'Upload Production Tracker',
        'formDescription': 'Download the latest tracker from SharePoint (File → Create a Copy → Download a Copy) '
                           'and upload it here. The Production Intelligence Report refreshes automatically.',
        'formFields': {'values': [{'fieldLabel': 'Tracker File', 'fieldType': 'file', 'multipleFiles': False,
                                   'acceptFileTypes': '.xlsx,.xlsm', 'requiredField': True}]},
        'responseMode': 'lastNode',
        'options': {'path': 'production-tracker-upload', 'buttonLabel': 'Upload & refresh report'}}),
    node('Read Tracker Sheet', 'extractFromFile', 1, [220, 300], {
        'operation': 'xlsx', 'binaryPropertyName': 'Tracker_File', 'options': {}}),
    node('Clean Rows', 'code', 2, [440, 300], {'jsCode': js('clean.js')}),
    node('Upsert into Data Table', 'dataTable', 1, [660, 300], {
        'resource': 'row', 'operation': 'upsert',
        'dataTableId': {'__rl': True, 'mode': 'list', 'value': ''},
        'matchType': 'allConditions',
        'filters': {'conditions': [{'keyName': 'Invoice', 'condition': 'eq', 'keyValue': '={{ $json.Invoice }}'}]},
        'columns': {'mappingMode': 'autoMapInputData', 'value': {}, 'matchingColumns': [], 'schema': []},
        'options': {}}),
    node('Summarise Upload', 'code', 2, [880, 300], {'jsCode': js('summary.js')}),
    node('Refresh Report', 'executeWorkflow', 1.2, [1100, 300], {
        'source': 'database',
        'workflowId': {'__rl': True, 'mode': 'list', 'value': ''},
        'workflowInputs': {'mappingMode': 'defineBelow', 'value': {}, 'matchingColumns': [], 'schema': [],
                           'attemptToConvertTypes': False, 'convertFieldsToString': True},
        'mode': 'once',
        'options': {'waitForSubWorkflow': False}}),
    node('Done Page', 'form', 1, [1320, 300], {
        'operation': 'completion', 'respondWith': 'text',
        'completionTitle': 'Tracker uploaded ✔',
        'completionMessage': "={{ $('Summarise Upload').first().json.message }}. "
                             "The report is being generated and will arrive by email shortly.",
        'options': {}}),
    {
        'parameters': {'width': 560, 'height': 300, 'content': (
            '## Tracker upload – setup\n'
            '1. **Upsert into Data Table** → pick your Data Table\n'
            '2. **Clean Rows** → check `COLUMNS` matches the Data Table columns exactly; '
            'add tracker headings to `ALIASES`\n'
            '3. **Read Tracker Sheet** → *Options → Sheet Name* if the data is not on the first tab\n'
            '4. **Refresh Report** → pick *Report copy* (it needs a *When Executed by Another Workflow* trigger)\n'
            '5. Publish, then share the form URL from **Upload Tracker** (Production URL)')},
        'id': str(uuid.uuid5(uuid.NAMESPACE_URL, 'upload-sticky')), 'name': 'Setup Notes',
        'type': 'n8n-nodes-base.stickyNote', 'typeVersion': 1, 'position': [-40, -40]},
]

order = ['Upload Tracker', 'Read Tracker Sheet', 'Clean Rows', 'Upsert into Data Table', 'Summarise Upload',
         'Refresh Report', 'Done Page']
connections = {a: {'main': [[{'node': b, 'type': 'main', 'index': 0}]]} for a, b in zip(order, order[1:])}

if __name__ == '__main__':
    workflow = {'name': 'Production Tracker – Upload from SharePoint', 'nodes': nodes, 'connections': connections,
                'pinData': {}, 'settings': {'executionOrder': 'v1'}, 'active': False, 'tags': []}
    (HERE / 'tracker_upload_workflow.json').write_text(json.dumps(workflow, indent=2, ensure_ascii=False) + '\n')
    print('wrote tracker_upload_workflow.json with', len(nodes), 'nodes')
