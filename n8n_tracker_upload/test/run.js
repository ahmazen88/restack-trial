// Offline test of the Code-node scripts with a stand-in for n8n's $ / $input.
const fs = require('fs');
const path = require('path');
const src = (f) => fs.readFileSync(path.join(__dirname, '..', 'src', f), 'utf8');
const run = (code, input, nodes = {}) =>
  new Function('$', '$input', code)((n) => ({ all: () => nodes[n], first: () => nodes[n][0] }), { all: () => input });
const assert = (c, m) => { if (!c) { console.error('FAIL:', m); process.exit(1); } console.log('ok -', m); };

// Shaped like the real tracker: numeric invoice numbers, Excel serial dates
const sheet = [
  { 'Invoice': 7001211479, Value: '1,250.00', Customer: ' RIO TINTO ALCAN INC ', 'Company Code': 'CC10', Received_Date: 46118, Allocated_Date: '46118', Invoice_Date: 46107 },
  { 'Invoice No': '7001211480', Value: 300, Customer: 'SALT RIVER PROJECT', 'Company Code': 'CC20', Received_Date: '10/7/2026' },
  { 'Invoice': '', Value: '1550', Customer: 'TOTAL' },
  { 'Invoice': 7001211479, Value: '1,300.00', Customer: 'RIO TINTO ALCAN INC', 'Company Code': 'CC10', Received_Date: 46119 },
].map((json) => ({ json }));

const out = run(src('clean.js'), sheet).map((i) => i.json);
const a = out.find((r) => r.Invoice === 7001211479);
const b = out.find((r) => r.Invoice === 7001211480);
assert(out.length === 2, 'drops blank-key row and de-duplicates the repeated invoice');
assert(typeof a.Invoice === 'number' && typeof b.Invoice === 'number', 'Invoice sent as a number');
assert(a.Value === '1,300.00' && a.Received_Date === '2026-04-07', 'last duplicate wins');
assert(a.Customer === 'RIO TINTO ALCAN INC', 'trims text');
assert(b.Received_Date.startsWith('2026-10-0'), 'normal date text converted');
const first = run(src('clean.js'), [sheet[0]]).map((i) => i.json)[0];
assert(first.Received_Date === '2026-04-06' && first.Allocated_Date === '2026-04-06' && first.Invoice_Date === '2026-03-26',
  'Excel serial dates (number or text) become YYYY-MM-DD');
assert(b.Allocated_Date === null, 'missing columns sent as null');

const s = run(src('summary.js'), [], {
  'Read Tracker Sheet': sheet, 'Clean Rows': out.map((json) => ({ json })),
  'Upload Tracker': [{ json: {}, binary: { Tracker_File: { fileName: 'Tracker.xlsx' } } }],
})[0].json;
assert(s.rowsRead === 4 && s.rowsSaved === 2 && s.rowsSkipped === 2 && s.file === 'Tracker.xlsx', 'summary counts');
