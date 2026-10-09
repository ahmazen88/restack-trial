"""Builds invoice_drafts_workflow.json: invoice numbers → Box search → PDF → draft email to you."""
import json
import uuid
from pathlib import Path

HERE = Path(__file__).parent


def js(name):
    return (HERE / 'src' / name).read_text()


def node(name, type_, version, pos, params, **extra):
    return {'parameters': params, 'id': str(uuid.uuid5(uuid.NAMESPACE_URL, 'drafts-' + name)), 'name': name,
            'type': f'n8n-nodes-base.{type_}', 'typeVersion': version, 'position': pos, **extra}


SEND = 'Send Draft to Me – paste GEV Send Email here'
nodes = [
    node('Request Invoices', 'formTrigger', 2.2, [0, 300], {
        'formTitle': 'Invoice Drafts',
        'formDescription': 'Enter invoice numbers. Each invoice PDF is found in Box and a draft email with the PDF '
                           'attached is sent to you to check and forward. Nothing is sent to customers.',
        'formFields': {'values': [
            {'fieldLabel': 'Invoice numbers', 'fieldType': 'textarea', 'requiredField': True,
             'placeholder': 'One per line, e.g.\n7001206102\n7001211479'},
            {'fieldLabel': 'Send drafts to (optional)', 'fieldType': 'email', 'placeholder': 'your email'},
        ]},
        'responseMode': 'lastNode',
        'options': {'path': 'invoice-drafts', 'buttonLabel': 'Prepare drafts'}}),
    node('Split Invoice Numbers', 'code', 2, [220, 300], {'jsCode': js('split.js')}),
    node('Search Box', 'box', 1, [440, 300], {
        'resource': 'file', 'operation': 'search', 'query': '={{ $json.invoice }}', 'returnAll': False, 'limit': 20,
        'additionalFields': {'file_extensions': 'pdf'}}, alwaysOutputData=True),
    node('Pick Invoice Files', 'code', 2, [660, 300], {'jsCode': js('pick.js')}),
    node('Download Invoice', 'box', 1, [880, 300], {
        'resource': 'file', 'operation': 'download', 'fileId': '={{ $json.id }}', 'binaryPropertyName': 'data'}),
    node('Read Invoice PDF', 'extractFromFile', 1, [1100, 300], {
        'operation': 'pdf', 'binaryPropertyName': 'data', 'options': {'keepSource': 'both'}}),
    node('Build Drafts', 'code', 2, [1320, 300], {'jsCode': js('drafts.js')}),
    node(SEND, 'noOp', 1, [1540, 300], {}),
    node('Summary', 'code', 2, [1760, 300], {'jsCode': js('summary.js')}),
    node('Done Page', 'form', 1, [1980, 300], {
        'operation': 'completion', 'respondWith': 'text', 'completionTitle': 'Drafts prepared ✔',
        'completionMessage': '={{ $json.message }}', 'options': {}}),
    {'parameters': {'width': 600, 'height': 330, 'content': (
        '## Invoice drafts – setup (one time)\n'
        '1. **Search Box** & **Download Invoice** → credential *Box account* (the one that already works)\n'
        '2. **Build Drafts** → your address in `SEND_DRAFTS_TO`\n'
        f'3. Replace **{SEND}**: copy *Send an Email* from *Report copy*, paste, connect Build Drafts → it → '
        'Summary, delete the placeholder. Set To `{{ $json.to }}`, Subject `{{ $json.subject }}`, Email Format '
        'HTML, HTML `{{ $json.html }}`, Attachments `data`\n'
        '4. Publish, open the form (Request Invoices → Production URL)\n\n'
        'Safe by design: drafts go **only to you**; the invoice number is checked inside each PDF.')},
     'id': str(uuid.uuid5(uuid.NAMESPACE_URL, 'drafts-sticky')), 'name': 'Setup Notes',
     'type': 'n8n-nodes-base.stickyNote', 'typeVersion': 1, 'position': [-40, -80]},
]
order = ['Request Invoices', 'Split Invoice Numbers', 'Search Box', 'Pick Invoice Files', 'Download Invoice',
         'Read Invoice PDF', 'Build Drafts', SEND, 'Summary', 'Done Page']
connections = {a: {'main': [[{'node': b, 'type': 'main', 'index': 0}]]} for a, b in zip(order, order[1:])}

if __name__ == '__main__':
    wf = {'name': 'Invoice Drafts – Box to my inbox', 'nodes': nodes, 'connections': connections, 'pinData': {},
          'settings': {'executionOrder': 'v1'}, 'active': False, 'tags': []}
    (HERE / 'invoice_drafts_workflow.json').write_text(json.dumps(wf, indent=2, ensure_ascii=False) + '\n')
    print('wrote invoice_drafts_workflow.json with', len(nodes), 'nodes')
