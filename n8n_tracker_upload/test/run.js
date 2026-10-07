// Offline test of the Code-node scripts with a stand-in for n8n's $ / $input.
const fs = require('fs');
const path = require('path');
const src = (f) => fs.readFileSync(path.join(__dirname, '..', 'src', f), 'utf8');
const run = (code, input, nodes = {}) =>
  new Function('$', '$input', code)((n) => ({ all: () => nodes[n], first: () => nodes[n][0] }), { all: () => input });
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
assert(s.rowsRead === 5 && s.rowsSaved === 3 && s.blankRows === 1, 'counts');
assert(s.duplicateInvoices.length === 1 && s.duplicateInvoices[0] === '7001211479', 'lists repeated invoice');
assert(s.issues['zero or negative value'].count === 1 && s.issues['missing customer'].count === 1, 'value / customer checks');
assert(s.issues['missing company code'].count === 1, 'company code check');
assert(s.issues['date before 2020-01-01'].examples[0] === '7001211481', 'early date check');
assert(s.issues['allocated before received'].examples[0] === '7001211480', 'allocated-before-received check');
assert(!s.issues['missing value'] && !s.issues['no readable date'], 'no false flags');
assert(JSON.stringify(run(src('summary.js'), [], nodes)) === JSON.stringify(run(src('summary.js'), [], nodes)), 'deterministic: same input, same output');
console.log('\nDone page would show:\n' + s.message);
