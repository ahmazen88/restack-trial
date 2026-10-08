// Full offline check of production_tracker.json (the single-line "Production Tracker" workflow).
// Runs every Code node in order with realistic data, plus the failure cases.
const fs = require('fs');
const path = require('path');
const wf = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'production_tracker.json'), 'utf8'));
const byName = Object.fromEntries(wf.nodes.map((n) => [n.name, n]));
const code = (n) => byName[n].parameters.jsCode;
let okCount = 0;
const assert = (c, m) => { if (!c) { console.error('FAIL:', m); process.exit(1); } okCount++; console.log('ok -', m); };
const throws = (f) => { try { f(); return ''; } catch (e) { return e.message; } };

// ---------- 1. Shape: one start, one end, a single straight line ----------
const flow = wf.nodes.filter((n) => n.type !== 'n8n-nodes-base.stickyNote');
const targets = new Set(Object.values(wf.connections).flatMap((c) => c.main.flat().map((x) => x.node)));
const starts = flow.filter((n) => !targets.has(n.name));
const ends = flow.filter((n) => !wf.connections[n.name]);
assert(starts.length === 1 && starts[0].name === 'Upload Tracker', 'exactly one starting point: Upload Tracker');
assert(ends.length === 1 && ends[0].name === 'Done Page', 'exactly one ending point: Done Page');
const order = ['Upload Tracker'];
while (wf.connections[order.at(-1)]) {
  const next = wf.connections[order.at(-1)].main.flat();
  assert(next.length === 1, `"${order.at(-1)}" has exactly one next step`);
  order.push(next[0].node);
}
assert(order.length === flow.length, `all ${flow.length} steps are on the line: ${order.join(' → ')}`);

// ---------- 2. Every reference to another step points to an earlier step ----------
for (const n of flow) {
  const text = JSON.stringify(n.parameters);
  for (const [, ref] of text.matchAll(/\$\(\\?['"]([^'"\\]+)\\?['"]\)/g)) {
    if (ref === 'Compare with Table') continue; // only read inside try/catch, for the other workflows
    assert(order.indexOf(ref) > -1 && order.indexOf(ref) < order.indexOf(n.name), `"${n.name}" reads "${ref}", which runs earlier`);
  }
}
const sql = /(update|delete|insert|drop|alter|truncate|create|merge|grant)/i;
assert(flow.filter((n) => n.parameters.jsCode && sql.test(n.parameters.jsCode)).length === 0, 'no Code node contains words the company scanner blocks');
assert(byName['Clear Table'].executeOnce && byName['Check Table'].executeOnce && byName['Check Table'].parameters.returnAll, 'Clear Table and Check Table run once, not once per row');
assert(byName['Save All Rows'].parameters.options.optimizeBulk === true, 'all rows are saved in one bulk call');
assert(byName['Read Tracker Sheet'].alwaysOutputData && byName['Check Table'].alwaysOutputData, 'an empty sheet or an empty table cannot stop the flow silently');
assert(order.indexOf('Safety Check') < order.indexOf('Clear Table'), 'the Safety Check runs before the table is emptied');

// ---------- 3. Run the Code nodes ----------
const run = (out, name, input, src = code(name)) => {
  const $ = (n) => { if (!(n in out)) throw new Error(`Referenced node doesn't exist: ${n}`); return { all: () => out[n], first: () => out[n][0], itemMatching: (i) => out[n][i] }; };
  out[name] = new Function('$', '$input', src)($, { all: () => input, first: () => input[0] });
  return out[name];
};
const customers = ['Rio Tinto Alcan Inc', 'SALT RIVER PROJECT', 'EXELON ACCOUNTS PAYABLE', 'Duke  Energy ', 'PG&E'];
const makeSheet = (count) => {
  const sheet = [];
  for (let i = 0; i < count; i++) {
    const serial = 45658 + (i % 600) + 0.4; // Excel dates (number with a time part) 2025-01-01 …
    const row = { 'Invoice ': 7001200000 + i, Value: (i * 37) % 900 + 100.5, Customer: customers[i % 5],
      'Company Code': ['3060', '3485', '3487', '3110'][i % 4], 'Project Manager': 'LOMBARD Axel',
      'Name the Portal/Email ID': i % 2 ? 'Ariba' : 'invoices@riotinto.com', Received_Date: serial,
      Allocated_Date: serial + 1, Invoice_Date: serial + 2 };
    sheet.push({ json: row });
  }
  return sheet;
};
const TABLE_ROW = { id: 1, Invoice: 1, Value: '1', Customer: 'X', Company_Code: '1', Project_Manager: 'X',
  Name_the_PortalEmail_ID: 'X', Received_Date: '2026-01-01', Allocated_Date: null, Invoice_Date: null,
  SAP_Customer_Code: null, Profit_Center: null };
const withMail = code('Build Report').replace("const RECIPIENTS = [''];", "const RECIPIENTS = ['me@example.com'];");
const NOFILE = [{ json: { error: 'This operation expects the node\'s input data to contain a binary file' } }];
const fullRun = (sheet, tableRow, aiOut, files = {}) => {
  const out = { 'Upload Tracker': [{ json: {}, binary: { Tracker_File: { fileName: 'Trackers - NAM Distribution.xlsx' } } }] };
  out['Read Tracker Sheet'] = sheet;
  run(out, 'Clean Rows', sheet);
  for (const step of ['Pick ZSD File', 'Pick ZSD File Again', 'Pick Tableau File']) run(out, step, []);
  out['Read ZSD Log'] = files.zsd || NOFILE;
  out['Read ZSD 2025 Sheet'] = files.zsd2025 || NOFILE;
  out['Read Tableau Extract'] = files.tableau || NOFILE;
  out['Check Table'] = Array.isArray(tableRow) ? tableRow.map((json) => ({ json })) : [{ json: tableRow }];
  run(out, 'Add Lookups', out['Check Table']);
  run(out, 'Safety Check', out['Add Lookups']);
  out['Clear Table'] = [{ json: { success: true, deletedCount: 4000 } }];
  run(out, 'Rows to Save', out['Clear Table']);
  out['Save All Rows'] = [{ json: { count: out['Rows to Save'].length } }];
  run(out, 'Summarise Upload', out['Save All Rows']);
  run(out, 'Build Report', out['Summarise Upload'], withMail);
  out['AI Commentary'] = aiOut;
  run(out, 'Add AI Commentary', out['AI Commentary']);
  return out;
};

// 3a. Realistic size: 4,100 rows, existing table
const t0 = Date.now();
const big = fullRun(makeSheet(4100), TABLE_ROW, [{ json: { text: '<h3>Summary</h3><p>4,100 invoices were received across four company codes; volume is steady.</p>' } }]);
const ms = Date.now() - t0;
assert(big['Rows to Save'].length === 4100, '4,100 rows cleaned and passed to the single bulk save');
const r0 = big['Rows to Save'][0].json;
assert(Object.keys(r0).sort().join() === Object.keys(TABLE_ROW).filter((k) => k !== 'id').sort().join(), 'rows have exactly the Data Table columns (incl. SAP_Customer_Code, Profit_Center)');
assert(big['Rows to Save'].every((i) => i.json.SAP_Customer_Code === null), 'no ZSD / Tableau file uploaded → codes stay empty, nothing breaks');
assert(r0.Invoice === 7001200000 && typeof r0.Invoice === 'number' && r0.Value === '100.5' && r0.Customer === 'RIO TINTO ALCAN INC',
  'Invoice is a number, Value is text, customer upper-cased (heading "Invoice " with a space still found)');
assert(r0.Received_Date === '2025-01-01' && r0.Allocated_Date === '2025-01-02' && r0.Invoice_Date === '2025-01-03',
  'Excel dates with a time part become the right day (not rounded to the next day)');
assert(big['Rows to Save'][3].json.Customer === 'DUKE ENERGY', 'extra spaces removed');
assert(ms < 5000, `all Code steps together take ${ms} ms for 4,100 rows (no spinning)`);
const rep = big['Build Report'][0];
assert(rep.json.to === 'me@example.com' && rep.binary.dashboard && rep.binary.dashboard.fileName === 'dashboard.html', 'report built and dashboard.html attached');
assert(typeof rep.json.facts === 'string' && rep.json.facts.length < 20000, `AI receives compact facts (${rep.json.facts.length} characters)`);
const sent = big['Add AI Commentary'][0];
assert(/AI commentary/.test(sent.json.html) && sent.binary.dashboard && sent.json.to === 'me@example.com' && sent.json.subject,
  'email item has to, subject, html with AI commentary, and the attachment');
assert(/4,100 invoices saved/.test(rep.json.doneMessage) && /me@example\.com/.test(rep.json.doneMessage), 'Done page: ' + rep.json.doneMessage.slice(0, 140) + '…');

// 3b. First upload into an empty table
const first = fullRun(makeSheet(50), {}, [{ json: { text: 'x' } }]);
assert(first['Safety Check'][0].json.tableHadRows === false && first['Rows to Save'].length === 50, 'empty table (first upload) is fine');
assert(!/AI commentary/.test(first['Add AI Commentary'][0].json.html), 'too-short AI answer → report sent without commentary');

// 3c. AI step failed (node continues with an error item)
const aiFail = fullRun(makeSheet(50), TABLE_ROW, [{ json: { error: 'model unavailable' } }]);
assert(aiFail['Add AI Commentary'][0].json.html === aiFail['Build Report'][0].json.html && aiFail['Add AI Commentary'][0].binary.dashboard,
  'AI unavailable → the normal report still goes out with the attachment');

// 3d. AI answer with junk is cleaned
const junk = fullRun(makeSheet(50), TABLE_ROW, [{ json: { text: '```html\n<h3 style="color:red">Summary</h3><script>alert(1)</script><p onclick="x()">Fifty invoices arrived, all within normal range for the period.</p>\n```' } }]);
const jh = junk['Add AI Commentary'][0].json.html;
const aiPart = jh.slice(jh.indexOf('Check before acting.</div>') + 26, jh.indexOf('</div>', jh.indexOf('Check before acting.</div>') + 26));
assert(aiPart === '<h3>Summary</h3><p>Fifty invoices arrived, all within normal range for the period.</p>\n', 'AI answer: code fences, scripts and attributes removed');

// ---------- 4. Messy tracker values ----------
const messy = [
  { json: { Customer: 'NO INVOICE CELL IN FIRST ROW', Value: 5 } },
  { json: { Invoice: '7001212645', Value: '$1,157.44', Customer: 'a', 'Company Code': 3060, Received_Date: '4/6/2026' } },
  { json: { Invoice: 7001212646, Value: '(1,157.44)', Customer: 'b', Received_Date: '2026-04-07T00:00:00.000Z' } },
  { json: { Invoice: '7001212647 / 7001212648', Value: '10', Customer: 'c' } },
  { json: { Invoice: '7001-1', Value: '10', Customer: 'd' } },
  { json: { Invoice: 'Total', Value: 999999 } },
  { json: { Invoice: '7001212649.0', Value: 'n/a', Customer: 'e', Received_Date: 'pending', Allocated_Date: '46118' } },
  { json: { Invoice: 7001212645, Value: '1200', Customer: 'a2' } },
];
const m = {};
run(m, 'Clean Rows', messy);
const rows = Object.fromEntries(m['Clean Rows'].map((i) => [i.json.Invoice, i.json]));
assert(Object.keys(rows).sort().join() === '7001212645,7001212646,7001212649', 'first row without an invoice cell does not trip the column check; unclear invoice numbers are skipped, not guessed');
assert(rows[7001212645].Value === '1200' && rows[7001212645].Customer === 'A2', 'repeated invoice: last row wins');
assert(rows[7001212646].Value === '-1157.44' && rows[7001212646].Received_Date === '2026-04-07', '(1,157.44) → -1157.44; ISO date with time → that day');
assert(rows[7001212649].Value === null && rows[7001212649].Received_Date === null && rows[7001212649].Allocated_Date === '2026-04-06', '"n/a" and "pending" become empty; text serial 46118 → 2026-04-06');
m['Upload Tracker'] = [{ json: {}, binary: { Tracker_File: { fileName: 'x.xlsx' } } }];
m['Read Tracker Sheet'] = messy;
run(m, 'Summarise Upload', []);
const msg = m['Summarise Upload'][0].json.message;
assert(/2 rows skipped because the invoice number is not a plain number: 7001212647 \/ 7001212648, 7001-1/.test(msg) && /2 blank or total rows skipped/.test(msg) && !/Total/.test(msg)
  && /appear more than once/.test(msg), 'Done page lists skipped, blank and repeated invoices: ' + msg.slice(0, 160) + '…');
const d = {};
run(d, 'Clean Rows', [{ json: { Invoice: 1, Received_Date: '4/6/2026' } }]);
assert(d['Clean Rows'][0].json.Received_Date === '2026-04-06', 'US date 4/6/2026 → 2026-04-06');

// ---------- 5a. SAP customer code / profit centre lookups ----------
const lookSheet = [
  { json: { Invoice: 7001300001, Value: 10, Customer: 'IDAHO POWER COMPANY', 'Company Code': 'G36C', Received_Date: '2026-04-01' } },
  { json: { Invoice: 7001300002, Value: 20, Customer: 'EKU POWER DRIVES', 'Company Code': 'GS5C', Received_Date: '2026-04-01' } },
  { json: { Invoice: 9001400001, Value: 30, Customer: 'SIEMENS', 'Company Code': '3060', Received_Date: '2026-04-02' } },
  { json: { Invoice: 9001400002, Value: 40, Customer: 'EATON', 'Company Code': '3485', Received_Date: '2026-04-02' } },
  { json: { Invoice: 9001400003, Value: 50, Customer: 'ABB', 'Company Code': '3487', Received_Date: '2026-04-03' } },
  { json: { Invoice: 9001400004, Value: 60, Customer: 'OLD ONE', 'Company Code': '3060', Received_Date: '2026-04-03' } },
];
const zsd = [ // ZSD log: invoice in an unnamed-looking column, customer code in "Customer", name in "Name"
  { json: { 'Billing Doc.': '0007001300001', 'Billing Date': 46000, 'Company Code': 'G367', Customer: '0000089598', Name: 'IDAHO POWER COMPANY', Text: 'Successfully Processed', 'Net Value': 10 } },
  { json: { 'Billing Doc.': 5555555555, 'Company Code': 'G367', Customer: 11111, Name: 'NOT IN TRACKER' } },
];
const zsd2025 = [{ json: { 'Billing Doc.': '7001300002', 'Company Code': 'G367', Customer: '170940', Name: 'EKU Power Drives Inc.' } }];
const tableau = [ // Tableau: several "customer" columns, profit centre, invoice in "Billing Document" (Excel number)
  { json: { Code: 'GWJ1', 'Company Code': '3060', 'Profit Center': 'GPJ908', 'Customer Number': 106685, 'Key Customer': 'SIEMENS', 'Customer Name': 'SIEMENS AG', 'Billing Document': 9001400001, 'Accounting Document': 2000000001 } },
  { json: { Code: 'GWJ1', 'Company Code': '3485', 'Profit Center': ' gpj777 ', 'Customer Number': 80950, 'Key Customer': 'EATON', 'Customer Name': 'EATON', 'Billing Document': ' 9,001,400,002 ' } },
  { json: { Code: 'GWJ1', 'Company Code': '3487', 'Profit Center': '', 'Customer Number': 22806, 'Customer Name': 'ABB', 'Billing Document': '9001400003.0' } },
  { json: { 'Profit Center': 'GPJ999', 'Customer Number': 99999, 'Billing Document': 7001300001 } }, // G367 invoice: no profit centre
];
const earlier = [ // the Data Table before this upload: 9001400004 was matched last time, is not in today's Tableau file
  { ...TABLE_ROW, id: 7, Invoice: 9001400004, Company_Code: '3060', SAP_Customer_Code: '45454', Profit_Center: 'GPJ123' },
];
const L = fullRun(lookSheet, earlier, [{ json: {} }], { zsd: zsd.concat(NOFILE.slice(0, 0)), zsd2025, tableau });
const by = Object.fromEntries(L['Rows to Save'].map((i) => [i.json.Invoice, i.json]));
assert(by[7001300001].Company_Code === 'G367' && by[7001300002].Company_Code === 'G367', 'tracker sales org G36C / GS5C → company code G367');
assert(by[7001300001].SAP_Customer_Code === '89598' && by[7001300002].SAP_Customer_Code === '170940', 'G367: SAP customer code from the ZSD log (2026 and 2025 sheets)');
assert(by[7001300001].Profit_Center === null && by[7001300002].Profit_Center === null, 'G367: no profit centre (even if Tableau has one)');
assert(by[9001400001].SAP_Customer_Code === '106685' && by[9001400001].Profit_Center === 'GPJ908', '3060: SAP customer code and profit centre from Tableau ("Customer Number", not "Key Customer"/"Customer Name")');
assert(by[9001400002].Profit_Center === 'GPJ777' && by[9001400003].SAP_Customer_Code === '22806' && by[9001400003].Profit_Center === null,
  'cleaned before matching: leading zeros, spaces, commas, "9001400003.0"; profit centre tidied to GPJ777; empty stays empty');
assert(by[9001400004].SAP_Customer_Code === '45454' && by[9001400004].Profit_Center === 'GPJ123', 'invoice no longer in the Tableau file keeps the codes found on an earlier upload');
assert(/SAP customer code found for 6 of 6 invoices · profit centre found for 3 of 4/.test(L['Summarise Upload'][0].json.message), 'Done page: ' + L['Summarise Upload'][0].json.message.match(/SAP customer code.*?\)/)[0]);
const wrongZsd = fullRun(lookSheet, {}, [{ json: {} }], { zsd: [{ json: { A: 1, B: 'x' } }] });
assert(wrongZsd['Rows to Save'].every((i) => i.json.SAP_Customer_Code === null), 'a file with no matching invoice numbers fills nothing (no guessing)');

// ---------- 5. Stops BEFORE emptying the table when something is wrong ----------
const stop = (sheet, tableRow) => throws(() => fullRun(sheet, tableRow, [{ json: {} }]));
assert(/sheet is empty.*Nothing was changed/.test(stop([{ json: {} }], TABLE_ROW)), 'empty sheet → clear message, table untouched');
assert(/No "Invoice" column found.*Nothing was changed/.test(stop([{ json: { Foo: 1 } }], TABLE_ROW)), 'wrong file/tab → clear message, table untouched');
assert(/No rows with an invoice number.*Nothing was changed/.test(stop([{ json: { Invoice: 'abc' } }], TABLE_ROW)), 'no usable invoice numbers → stops, table untouched');
const { SAP_Customer_Code, ...noSap } = TABLE_ROW;
assert(/no column called: SAP_Customer_Code.*add the missing column.*Nothing was changed/.test(stop(makeSheet(5), noSap)), 'new column not yet added to the Data Table → clear message, table untouched');
const { Company_Code, ...noCode } = TABLE_ROW;
assert(/no column called: Company_Code.*Nothing was changed/.test(stop(makeSheet(5), noCode)), 'table column missing → stops before Clear Table, table untouched');
assert(/Add at least one email address/.test(throws(() => { const o = fullRun(makeSheet(5), TABLE_ROW, [{ json: {} }]); run(o, 'Build Report', [], code('Build Report')); })),
  'email not filled in → clear message');

// ---------- 6. Expressions in the non-code steps ----------
assert(byName['Done Page'].parameters.completionMessage === "={{ $('Build Report').first().json.doneMessage }}", 'Done page shows the upload result');
assert(/\$json\.subject/.test(byName['AI Commentary'].parameters.text) && /\$json\.facts/.test(byName['AI Commentary'].parameters.text), 'AI prompt uses subject and facts from Build Report');
console.log(`\nall ${okCount} checks passed`);
