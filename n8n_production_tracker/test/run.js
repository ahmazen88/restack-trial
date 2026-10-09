// Simulates the n8n Code-node runtime to test the three scripts end to end.
const fs = require('fs');
const path = require('path');
const src = (f) => fs.readFileSync(path.join(__dirname, '..', 'src', f), 'utf8');
const run = (code, input, nodes) => {
  const $ = (name) => ({
    all: () => nodes[name],
    first: () => nodes[name][0],
    itemMatching: (i) => nodes[name][Math.min(i, nodes[name].length - 1)],
  });
  const $input = { all: () => input };
  return new Function('$', '$input', code)($, $input);
};
const assert = (c, m) => { if (!c) { console.error('FAIL:', m); process.exit(1); } console.log('ok -', m); };

const trigger = [{ json: { id: 'file123', name: 'daily_report_2026-10-07.csv' } }];
const report = [
  { 'Job No': 'WO-1001', 'Description': 'Duct fabrication L1', 'Area': 'Level 1', 'UOM': 'm2', 'Planned': '1,200', 'Installed Qty': 600, 'Due Date': '2026-12-01' },
  { 'Job No': 'WO-1002', 'Description': 'Chilled water pipe', 'Area': 'Level 2', 'UOM': 'm', 'Planned': 500, 'Installed Qty': 500 },
  { 'Job No': 'WO-1003', 'Planned': 100, 'Installed Qty': 10, 'Due Date': 45000 },
  { 'Job No': '', 'Description': 'Totals', 'Planned': 1800 },
].map((json) => ({ json }));
const tracker = [
  { row_number: 2, 'Item ID': 'WO-1001', 'Description': 'Duct fabrication L1', 'Planned Qty': 1200, 'Actual Qty': 300, 'Status': 'In Progress', 'Remarks': 'keep me' },
  { row_number: 3, 'Item ID': 'WO-0999', 'Status': 'On Hold' },
].map((json) => ({ json }));

const norm = run(src('normalize.js'), report, { 'New File in Inbox': trigger });
assert(norm.length === 4, 'normalize keeps every row');
assert(norm[0].json['Planned Qty'] === 1200, 'parses "1,200" as 1200');
assert(norm[0].json['Location / Line'] === 'Level 1', 'maps Area -> Location / Line');
assert(norm[2].json['Planned Finish'] === '2023-03-15', 'converts Excel serial date');
assert(norm[3].json._skip, 'row without ID flagged as skipped');

const nodes = { 'Read Tracker': tracker, 'Normalize Report Rows': norm, 'New File in Inbox': trigger };
const merged = run(src('merge.js'), [], nodes).map((i) => i.json);
const byId = Object.fromEntries(merged.map((r) => [r['Item ID'], r]));
assert(merged.length === 3, 'three items changed');
assert(byId['WO-1001']['Actual Qty'] === 600 && byId['WO-1001']['% Complete'] === 0.5, 'cumulative overwrite + % complete');
assert(byId['WO-1001'].Remarks === 'keep me', 'keeps tracker fields the report lacks');
assert(byId['WO-1002'].Status === 'Complete', 'complete status');
assert(byId['WO-1003'].Status === 'Behind Schedule', 'overdue -> Behind Schedule');
assert(!('row_number' in byId['WO-1001']), 'drops row_number');

const log = run(src('log.js'), [], nodes).map((i) => i.json);
assert(log.length === 1 && log[0]['Items Updated'] === 1 && log[0]['Items Added'] === 2 && log[0]['Rows Skipped'] === 1, 'log counts');

const incr = src('merge.js').replace("QTY_MODE = 'cumulative'", "QTY_MODE = 'incremental'");
const m2 = run(incr, [], nodes).map((i) => i.json);
assert(m2.find((r) => r['Item ID'] === 'WO-1001')['Actual Qty'] === 900, 'incremental mode adds to existing');

const empty = run(src('merge.js'), [], { ...nodes, 'Normalize Report Rows': [norm[3]] });
assert(empty.length === 1 && Object.keys(empty[0].json).length === 0, 'emits empty item when nothing matched');
console.log(JSON.stringify(log[0]));
