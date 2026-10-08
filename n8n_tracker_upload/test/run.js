// Offline test of the Code-node scripts with a stand-in for n8n's $ / $input.
const fs = require('fs');
const path = require('path');
const src = (f) => fs.readFileSync(path.join(__dirname, '..', 'src', f), 'utf8');
const run = (code, input, nodes = {}, memory = {}) =>
  new Function('$', '$input', '$getWorkflowStaticData', code)(
    (n) => ({ all: () => nodes[n], first: () => nodes[n][0] }), { all: () => input }, () => memory);
const assert = (c, m) => { if (!c) { console.error('FAIL:', m); process.exit(1); } console.log('ok -', m); };
const throws = (fn) => { try { fn(); return null; } catch (e) { return e.message; } };

// Shaped like the real tracker: numeric invoice numbers, Excel serial dates
const sheet = [
  { Invoice: 7001211479, Value: '1,250.00', Customer: ' Rio  Tinto Alcan Inc ', 'Company Code': 'cc10', Received_Date: 46118, Allocated_Date: '46118', Invoice_Date: 46107 },
  { 'Invoice': '7001211480', Value: 300, Customer: 'SALT RIVER PROJECT', 'Company Code': 'CC20', Received_Date: '10/7/2026', Allocated_Date: '10/5/2026' },
  { Invoice: '', Value: '1550', Customer: 'TOTAL' },
  { Invoice: 7001211479, Value: '1,300.00', Customer: 'RIO TINTO ALCAN INC', 'Company Code': 'CC10', Received_Date: 46119 },
  { Invoice: 7001211481, Value: '0', Customer: '', Received_Date: 43000 },
].map((json) => ({ json }));

// --- Clean Rows
const out = run(src('clean.js'), sheet).map((i) => i.json);
const byId = Object.fromEntries(out.map((r) => [r.Invoice, r]));
assert(out.length === 3, 'drops blank-key row and keeps one row per invoice');
assert(Object.keys(byId).every((k) => typeof byId[k].Invoice === 'number'), 'Invoice sent as a number');
assert(byId[7001211479].Value === '1,300.00' && byId[7001211479].Received_Date === '2026-04-07', 'last duplicate wins');
assert(byId[7001211480].Customer === 'SALT RIVER PROJECT', 'text kept');
const first = run(src('clean.js'), [sheet[0]]).map((i) => i.json)[0];
assert(first.Customer === 'RIO TINTO ALCAN INC' && first.Company_Code === 'CC10', 'spaces collapsed, Customer/Company_Code upper-cased');
assert(first.Received_Date === '2026-04-06' && first.Allocated_Date === '2026-04-06' && first.Invoice_Date === '2026-03-26',
  'Excel serial dates (number or text) become YYYY-MM-DD');
assert(/No "Invoice" column found/.test(throws(() => run(src('clean.js'), [{ json: { Foo: 1, Bar: 2 } }]))), 'wrong-file guard');
assert(/no rows/.test(throws(() => run(src('clean.js'), []))), 'empty-sheet guard');

// --- Summarise Upload
const nodes = {
  'Read Tracker Sheet': sheet, 'Clean Rows': out.map((json) => ({ json })),
  'Upload Tracker': [{ json: {}, binary: { Tracker_File: { fileName: 'Tracker.xlsx' } } }],
};
const s = run(src('summary.js'), [], nodes)[0].json;
assert(s.file === 'Tracker.xlsx', 'upload: file name from the form');
assert(s.rowsRead === 5 && s.rowsSaved === 3 && s.blankRows === 1, 'counts');
assert(s.duplicateInvoices.length === 1 && s.duplicateInvoices[0] === '7001211479', 'lists repeated invoice');
assert(s.issues['zero or negative value'].count === 1 && s.issues['missing customer'].count === 1, 'value / customer checks');
assert(s.issues['missing company code'].count === 1, 'company code check');
assert(s.issues['date before 2020-01-01'].examples[0] === '7001211481', 'early date check');
assert(s.issues['allocated before received'].examples[0] === '7001211480', 'allocated-before-received check');
assert(!s.issues['missing value'] && !s.issues['no readable date'], 'no false flags');
assert(JSON.stringify(run(src('summary.js'), [], nodes)) === JSON.stringify(run(src('summary.js'), [], nodes)), 'deterministic: same input, same output');
console.log('\nDone page would show:\n' + s.message);

// --- OneDrive: Pick Tracker File / Remember Version
const NAME = 'Trackers - NAM Distribution.xlsx';
const found = [
  { id: 'A1', name: NAME, eTag: '"v7"', lastModifiedDateTime: '2026-10-07T10:00:00Z', file: {} },
  { id: 'B2', name: 'Trackers - NAM Distribution (old).xlsx', eTag: '"v1"', file: {} },
  { id: 'F3', name: NAME, folder: {} }, // a folder with the same name is ignored
].map((json) => ({ json }));
const graphShape = [{ json: { value: found.map((i) => i.json) } }];
assert(run(src('pick.js'), graphShape, {}, {})[0].json.id === 'A1', 'reads Microsoft Graph search results ({ value: [...] })');
const memory = {};
const picked = run(src('pick.js'), found, {}, memory);
assert(picked.length === 1 && picked[0].json.id === 'A1', 'picks the exact file name only');
assert(/was not found/.test(throws(() => run(src('pick.js'), [found[1]], {}, {}))), 'missing-file guard');
assert(/2 files are named/.test(throws(() => run(src('pick.js'), [found[0], found[0]], {}, {}))), 'duplicate-name guard');
run(src('remember.js'), [{ json: { ok: 1 } }], { 'Pick Tracker File': picked }, memory);
assert(memory.lastETag === '"v7"', 'remembers the processed version');
assert(run(src('pick.js'), found, {}, memory).length === 0, 'skips an unchanged file');
const changed = [{ json: { ...found[0].json, eTag: '"v8"' } }];
assert(run(src('pick.js'), changed, {}, memory).length === 1, 'processes a changed file');

const fs2 = require('fs');
const wf = JSON.parse(fs2.readFileSync(path.join(__dirname, '..', 'tracker_onedrive_workflow.json'), 'utf8'));
const odSummary = wf.nodes.find((n) => n.name === 'Summarise Upload').parameters.jsCode;
const s2 = run(odSummary, [], { ...nodes, 'Pick Tracker File': picked })[0].json;
assert(s2.file === NAME && s2.rowsSaved === s.rowsSaved, 'onedrive: same checks, file name from OneDrive');

// --- One-flow report
const odWf = JSON.parse(fs2.readFileSync(path.join(__dirname, '..', 'tracker_onedrive_workflow.json'), 'utf8'));
const reportJsRaw = odWf.nodes.find((n) => n.name === 'Build Report').parameters.jsCode;
assert(/Add at least one email address/.test(throws(() => run(reportJsRaw, [], {}))), 'stops when RECIPIENTS is empty');
const reportJs = reportJsRaw.replace('const RECIPIENTS = [];', "const RECIPIENTS = ['a@example.com', 'b@example.com'];");
const custs = ['RIO TINTO ALCAN INC', 'SALT RIVER PROJECT', 'EXELON ACCOUNTS PAYABLE', 'OGLETHORPE POWER CORPORATION', 'POWER LINE SUPPLY'];
const sample = Array.from({ length: 240 }, (_, i) => ({
  Invoice: 7001211000 + i,
  Value: String(((i * 7919) % 50000) + 250),
  Customer: custs[i % custs.length],
  Company_Code: ['CC10', 'CC20', 'CC30'][i % 3],
  Received_Date: new Date(Date.UTC(2026, 0, 1) + (i % 270) * 86400000).toISOString().slice(0, 10),
  Allocated_Date: null, Invoice_Date: null,
}));
const rnodes = {
  'Clean Rows': sample.map((json) => ({ json })),
  'Summarise Upload': [{ json: { blankRows: 3, duplicateInvoices: ['7001211005'], issues: { 'missing value': { count: 2, examples: ['7001211007', '7001211009'] } } } }],
  'Pick Tracker File': [{ json: { name: NAME, lastModified: '2026-10-07T10:15:00Z' } }],
};
const r1 = run(reportJs, [], rnodes)[0].json;
const r2 = run(reportJs, [], rnodes)[0].json;
assert(r1.html === r2.html && r1.subject === r2.subject, 'report is deterministic');
assert(r1.invoices === 240 && /Monthly summary/.test(r1.html) && /Top 10 customers/.test(r1.html), 'report sections present');
assert(/as of 2026-08-28/.test(r1.subject), 'as-of date comes from the data, not the clock');
assert(!/<script/i.test(r1.html), 'no scripts in email');
assert(r1.mail.message.toRecipients.length === 2 && r1.mail.message.body.contentType === 'HTML' &&
  r1.mail.message.body.content === r1.html, 'Graph sendMail body built');
assert(r1.to === 'a@example.com, b@example.com', 'plain "to" field for other mail nodes');
const send = odWf.nodes.find((n) => n.name === 'Send Report').parameters;
assert(send.url.endsWith('/me/sendMail') && send.nodeCredentialType === 'microsoftOutlookOAuth2Api', 'Send Report calls Graph sendMail');
const dl = odWf.nodes.find((n) => n.name === 'Download Tracker').parameters;
assert(dl.options.response.response.responseFormat === 'file' && dl.options.response.response.outputPropertyName === 'data', 'download saved as binary "data"');
assert(odWf.nodes.every((n) => !/microsoftOneDrive|microsoftOutlook/.test(n.type)), 'no OneDrive/Outlook nodes needed');
fs2.writeFileSync(path.join(__dirname, 'sample_report.html'), r1.html);
console.log('Subject:', r1.subject);
