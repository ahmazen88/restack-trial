"""Builds production_tracker_workflow.json from the Code-node scripts in src/."""
import json
import uuid
from pathlib import Path

HERE = Path(__file__).parent
TRACKER_COLUMNS = ['Item ID', 'Description', 'Category', 'Location / Line', 'Unit', 'Planned Qty', 'Actual Qty',
                   'Rejected Qty', 'Remaining Qty', '% Complete', 'Planned Finish', 'Status', 'Remarks',
                   'Last Updated', 'Source File']
LOG_COLUMNS = ['Timestamp', 'Source File', 'File ID', 'Rows Read', 'Items Updated', 'Items Added',
               'Rows Skipped', 'Result']


def js(name):
    return (HERE / 'src' / name).read_text()


def rl(value='', mode='list', **extra):
    return {'__rl': True, 'value': value, 'mode': mode, **extra}


def schema(cols):
    return [{'id': c, 'displayName': c, 'required': False, 'defaultMatch': False, 'display': True,
             'type': 'string', 'canBeUsedToMatch': True} for c in cols]


def node(name, type_, version, pos, params, **extra):
    return {'parameters': params, 'id': str(uuid.uuid5(uuid.NAMESPACE_URL, name)), 'name': name,
            'type': f'n8n-nodes-base.{type_}', 'typeVersion': version, 'position': pos, **extra}


SHEET = rl()  # pick the "Production Tracker" spreadsheet after import


def sheets(name, pos, operation, tab, cols, matching=None, **extra):
    columns = {'mappingMode': 'autoMapInputData', 'value': {}, 'matchingColumns': matching or [],
               'schema': schema(cols)}
    return node(name, 'googleSheets', 4.5, pos, {
        'operation': operation, 'documentId': SHEET, 'sheetName': rl(tab, 'name'),
        'columns': columns, 'options': {}}, **extra)


def move(name, pos, file_id_expr):
    return node(name, 'googleDrive', 3, pos, {
        'operation': 'move', 'fileId': rl(file_id_expr, 'id'),
        'driveId': rl('My Drive', 'list', cachedResultName='My Drive'),
        'folderId': rl()})


def ext_rule(key, *exts):
    return {
        'conditions': {
            'options': {'caseSensitive': False, 'leftValue': '', 'typeValidation': 'loose', 'version': 2},
            'conditions': [{
                'id': str(uuid.uuid5(uuid.NAMESPACE_URL, key + e)),
                'leftValue': "={{ ($binary.data.fileName || '').toLowerCase().split('.').pop() }}",
                'rightValue': e, 'operator': {'type': 'string', 'operation': 'equals'}} for e in exts],
            'combinator': 'or'},
        'renameOutput': True, 'outputKey': key}


nodes = [
    node('New File in Inbox', 'googleDriveTrigger', 1, [0, 300], {
        'pollTimes': {'item': [{'mode': 'everyMinute'}]}, 'triggerOn': 'specificFolder',
        'folderToWatch': rl(), 'event': 'fileCreated', 'options': {}}),
    node('Download File', 'googleDrive', 3, [220, 300], {
        'operation': 'download', 'fileId': rl('={{ $json.id }}', 'id'), 'options': {}}),
    node('File Type', 'switch', 3.2, [440, 300], {
        'rules': {'values': [ext_rule('CSV', 'csv'), ext_rule('XLSX', 'xlsx', 'xlsm'), ext_rule('XLS', 'xls')]},
        'options': {'fallbackOutput': 'extra', 'renameFallbackOutput': 'Unsupported'}}),
    node('Read CSV', 'extractFromFile', 1, [680, 100], {'operation': 'csv', 'options': {}}),
    node('Read XLSX', 'extractFromFile', 1, [680, 260], {'operation': 'xlsx', 'options': {}}),
    node('Read XLS', 'extractFromFile', 1, [680, 420], {'operation': 'xls', 'options': {}}),
    node('Normalize Report Rows', 'code', 2, [900, 260], {'jsCode': js('normalize.js')}),
    node('Read Tracker', 'googleSheets', 4.5, [1120, 260], {
        'operation': 'read', 'documentId': SHEET, 'sheetName': rl('Tracker', 'name'), 'options': {}},
        executeOnce=True, alwaysOutputData=True),
    node('Merge Into Tracker', 'code', 2, [1340, 260], {'jsCode': js('merge.js')}),
    node('Has Changes?', 'if', 2.2, [1560, 260], {
        'conditions': {
            'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'loose', 'version': 2},
            'conditions': [{'id': str(uuid.uuid5(uuid.NAMESPACE_URL, 'has-changes')),
                            'leftValue': "={{ $json['Item ID'] }}", 'rightValue': '',
                            'operator': {'type': 'string', 'operation': 'notEmpty', 'singleValue': True}}],
            'combinator': 'and'},
        'options': {}}),
    sheets('Update Tracker', [1780, 160], 'appendOrUpdate', 'Tracker', TRACKER_COLUMNS, ['Item ID']),
    node('Build Log Entry', 'code', 2, [2000, 260], {'jsCode': js('log.js')}),
    sheets('Write Update Log', [2220, 260], 'append', 'Update Log', LOG_COLUMNS),
    move('Move to Processed', [2440, 260], "={{ $('Build Log Entry').item.json['File ID'] }}"),
    node('Build Rejected Log', 'code', 2, [680, 620], {'jsCode': js('rejected.js')}),
    sheets('Log Rejected File', [900, 620], 'append', 'Update Log', LOG_COLUMNS),
    move('Move to Rejected', [1120, 620], "={{ $('Build Rejected Log').item.json['File ID'] }}"),
    {
        'parameters': {'width': 520, 'height': 340, 'content': (
            '## Production Tracker – setup\n'
            '1. **New File in Inbox** → pick your `Inbox` folder\n'
            '2. **Read Tracker / Update Tracker / Write Update Log / Log Rejected File** '
            '→ pick the *Production Tracker* spreadsheet\n'
            '3. **Move to Processed** / **Move to Rejected** → pick those folders\n'
            '4. Report column names → add aliases in **Normalize Report Rows**\n'
            '5. Daily (not cumulative) quantities → set `QTY_MODE` in **Merge Into Tracker**\n\n'
            'Drop .csv / .xlsx / .xls files (header in row 1) into Inbox. Checked every minute.')},
        'id': str(uuid.uuid5(uuid.NAMESPACE_URL, 'sticky')), 'name': 'Setup Notes',
        'type': 'n8n-nodes-base.stickyNote', 'typeVersion': 1, 'position': [-40, -120]},
]


def link(*targets):
    return [[{'node': t, 'type': 'main', 'index': 0} for t in out] for out in targets]


connections = {
    'New File in Inbox': {'main': link(['Download File'])},
    'Download File': {'main': link(['File Type'])},
    'File Type': {'main': link(['Read CSV'], ['Read XLSX'], ['Read XLS'], ['Build Rejected Log'])},
    'Read CSV': {'main': link(['Normalize Report Rows'])},
    'Read XLSX': {'main': link(['Normalize Report Rows'])},
    'Read XLS': {'main': link(['Normalize Report Rows'])},
    'Normalize Report Rows': {'main': link(['Read Tracker'])},
    'Read Tracker': {'main': link(['Merge Into Tracker'])},
    'Merge Into Tracker': {'main': link(['Has Changes?'])},
    'Has Changes?': {'main': link(['Update Tracker'], ['Build Log Entry'])},
    'Update Tracker': {'main': link(['Build Log Entry'])},
    'Build Log Entry': {'main': link(['Write Update Log'])},
    'Write Update Log': {'main': link(['Move to Processed'])},
    'Build Rejected Log': {'main': link(['Log Rejected File'])},
    'Log Rejected File': {'main': link(['Move to Rejected'])},
}

if __name__ == '__main__':
    workflow = {'name': 'Production Tracker – Auto Refresh from Drive', 'nodes': nodes, 'connections': connections,
                'pinData': {}, 'settings': {'executionOrder': 'v1'}, 'active': False, 'tags': []}
    (HERE / 'production_tracker_workflow.json').write_text(json.dumps(workflow, indent=2, ensure_ascii=False) + '\n')
    print('wrote production_tracker_workflow.json with', len(nodes), 'nodes')
