// Offline test of the Code-node scripts with a stand-in for n8n's $ / $input.
const fs = require('fs');
const path = require('path');
const src = (f) => fs.readFileSync(path.join(__dirname, '..', 'src', f), 'utf8');
const run = (code, input, nodes = {}) =>
  new Function('$', '$input', code)((n) => ({ all: () => nodes[n], first: () => nodes[n][0] }), { all: () => input });
const assert = (c, m) => { if (!c) { console.error('FAIL:', m); process.exit(1); } console.log('ok -', m); };

const sheet = [
  { 'Invoice No': 'INV-001', Amount: '1,250.00', 'Customer Name': ' ACME ', 'Company Code': 'CC10', 'Received Date': '10/1/26', Notes: 'x' },
  { 'Invoice No': 'INV-002', Amount: '300', 'Customer Name': 'Beta', 'Company Code': 'CC20' },
  { 'Invoice No': '', Amount: '1550', 'Customer Name': 'TOTAL' },
  { 'Invoice No': 'INV-001', Amount: '1,300.00', 'Customer Name': 'ACME', 'Company Code': 'CC10' },
].map((json) => ({ json }));

const out = run(src('clean.js'), sheet).map((i) => i.json);
assert(out.length === 2, 'drops blank-key row and de-duplicates INV-001');
assert(out[0].Value === '1,300.00', 'last duplicate wins, value kept as text by default');
assert(out[1].Customer === 'Beta' && out[0].Customer === 'ACME', 'maps Customer Name and trims');
assert(!('Notes' in out[0]), 'drops columns not in the Data Table');
assert(out[1].Received_Date === null, 'missing columns sent as null');

const typed = src('clean.js').replace('const TYPES = {};', "const TYPES = { Value: 'number', Received_Date: 'date' };");
const t = run(typed, sheet).map((i) => i.json);
assert(t[1].Value === 300, 'number type conversion');
const first = run(typed, [sheet[0]]).map((i) => i.json)[0];
assert(first.Value === 1250 && first.Received_Date.startsWith('2026-10-0'), 'date type conversion');

const s = run(src('summary.js'), [], {
  'Read Tracker Sheet': sheet, 'Clean Rows': out.map((json) => ({ json })),
  'Upload Tracker': [{ json: {}, binary: { Tracker_File: { fileName: 'Tracker.xlsx' } } }],
})[0].json;
assert(s.rowsRead === 4 && s.rowsSaved === 2 && s.rowsSkipped === 2 && s.file === 'Tracker.xlsx', 'summary counts');
