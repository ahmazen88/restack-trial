// End-to-end offline run of the single-line "Production Tracker" workflow (all Code nodes, in order)
const fs = require('fs');
const path = require('path');
const wf = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'production_tracker.json'), 'utf8'));
const code = (n) => wf.nodes.find((x) => x.name === n).parameters.jsCode;
const assert = (c, m) => { if (!c) { console.error('FAIL:', m); process.exit(1); } console.log('ok -', m); };
const out = {};
const $ = (n) => { if (!(n in out)) throw new Error('no node ' + n); return { all: () => out[n], first: () => out[n][0], itemMatching: (i) => out[n][i] }; };
const step = (name, input, src = code(name)) => (out[name] = new Function('$', '$input', src)($, { all: () => input, first: () => input[0] }));

const sheet = [];
for (let i = 0; i < 400; i++) {
  const d = new Date(Date.UTC(2026, 0, 2) + (i % 270) * 86400000).toISOString().slice(0, 10);
  sheet.push({ json: { Invoice: 7001200000 + i, Value: `${(i * 37) % 900 + 100}.50`, Customer: ['Rio Tinto Alcan Inc', 'SALT RIVER PROJECT', 'EXELON ACCOUNTS PAYABLE'][i % 3],
    'Company Code': ['3060', '3485', '3487'][i % 3], 'Project Manager': 'LOMBARD Axel', 'Name the Portal/Email ID': 'invoices@riotinto.com',
    Received_Date: d, Allocated_Date: d, Invoice_Date: d } });
}
out['Upload Tracker'] = [{ json: {}, binary: { Tracker_File: { fileName: 'Trackers - NAM Distribution.xlsx' } } }];
out['Read Tracker Sheet'] = sheet;
step('Clean Rows', sheet);
out['Clear Table'] = [{ json: { success: true } }];
step('Rows to Save', out['Clear Table']);
assert(out['Rows to Save'].length === 400 && out['Rows to Save'][0].json.Customer === 'RIO TINTO ALCAN INC', 'all 400 cleaned rows go to the bulk save');
out['Save All Rows'] = [{ json: { count: 400 } }];
step('Summarise Upload', out['Save All Rows']);
const noMail = code('Build Report');
assert(/Add at least one email address/.test((() => { try { step('Build Report', [], noMail); } catch (e) { return e.message; } })()), 'stops with a clear message until your email is filled in');
step('Build Report', out['Summarise Upload'], noMail.replace("const RECIPIENTS = [''];", "const RECIPIENTS = ['me@example.com'];"));
const rep = out['Build Report'][0];
assert(rep.json.to === 'me@example.com' && /Upload result/.test(rep.json.html) && rep.binary.dashboard, 'report built from the uploaded rows, dashboard attached');
out['AI Commentary'] = [{ json: { text: '<h3>Summary</h3><p>Incoming invoices were 400 this period across three company codes.</p>' } }];
step('Add AI Commentary', out['AI Commentary']);
assert(/AI commentary/.test(out['Add AI Commentary'][0].json.html) && out['Add AI Commentary'][0].binary.dashboard, 'AI commentary on top, attachment kept');
const done = wf.nodes.find((x) => x.name === 'Done Page').parameters.completionMessage;
assert(/doneMessage/.test(done) && /Report "/.test(rep.json.doneMessage), 'Done page shows the result: ' + rep.json.doneMessage.slice(0, 120) + '…');
