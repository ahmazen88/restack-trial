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
  Sales_Org: null, SAP_Customer_Code: null, Profit_Center: null, Product_Line: null,
  Status: null, Upload_Date: null, Tracker_TAT: null, Uploaded_By: null, Pending_Category: null, Pending_Reason: null, Standard_Category: null, Business_Type: null };
const withMail = code('Build Report').replace("const RECIPIENTS = [''];", "const RECIPIENTS = ['me@example.com'];")
  .replace('const TODAY = new Date().toISOString().slice(0, 10);', "const TODAY = '2026-10-08';");
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
  run(out, 'Standard Blockers', out['Check Table']);
  out['AI Blocker Classifier'] = files.blockerAi ? files.blockerAi(JSON.parse(out['Standard Blockers'][0].json.items)) : [{ json: { error: 'model unavailable' } }];
  run(out, 'Add Lookups', out['AI Blocker Classifier']);
  run(out, 'Safety Check', out['Add Lookups']);
  out['Clear Table'] = [{ json: { success: true, deletedCount: 4000 } }];
  run(out, 'Rows to Save', out['Clear Table']);
  out['Save All Rows'] = [{ json: { count: out['Rows to Save'].length } }];
  run(out, 'Summarise Upload', out['Save All Rows']);
  run(out, 'Build Report', out['Summarise Upload'], withMail);
  out['AI Commentary'] = aiOut;
  run(out, 'Add AI Commentary', out['AI Commentary']);
  out['AI Chart Designer'] = files.chartsAi || [{ json: { error: 'model unavailable' } }];
  run(out, 'Add AI Charts', out['AI Chart Designer']);
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
const sent = big['Add AI Charts'][0];
assert(/AI commentary/.test(sent.json.html) && sent.binary.dashboard && sent.json.to === 'me@example.com' && sent.json.subject,
  'email item has to, subject, html with AI commentary, and the attachment');
assert(/4,100 invoices saved/.test(rep.json.doneMessage) && /me@example\.com/.test(rep.json.doneMessage), 'Done page: ' + rep.json.doneMessage.slice(0, 140) + '…');

// 3b. First upload into an empty table
const first = fullRun(makeSheet(50), {}, [{ json: { text: 'x' } }]);
assert(first['Safety Check'][0].json.tableHadRows === false && first['Rows to Save'].length === 50, 'empty table (first upload) is fine');
assert(!/AI commentary/.test(first['Add AI Commentary'][0].json.html), 'too-short AI answer → report sent without commentary');

// 3c. AI step failed (node continues with an error item)
const aiFail = fullRun(makeSheet(50), TABLE_ROW, [{ json: { error: 'model unavailable' } }]);
assert(aiFail['Add AI Commentary'][0].json.html === aiFail['Build Report'][0].json.html && aiFail['Add AI Charts'][0].binary.dashboard,
  'AI unavailable → the normal report still goes out with the attachment');

// 3d. AI answer with junk is cleaned
const junk = fullRun(makeSheet(50), TABLE_ROW, [{ json: { text: '```html\n<h3 style="color:red">Summary</h3><script>alert(1)</script><p onclick="x()">Fifty invoices arrived, all within normal range for the period.</p>\n```' } }]);
const jh = junk['Add AI Commentary'][0].json.html;
const aiPart = jh.slice(jh.indexOf('Check before acting.</div>') + 26, jh.indexOf('</div>', jh.indexOf('Check before acting.</div>') + 26));
assert(aiPart === '<h3>Summary</h3><p>Fifty invoices arrived, all within normal range for the period.</p>\n', 'AI answer: code fences, scripts and attributes removed');

// 3e. AI chart designer
const chartAi = [{ json: { text: '```json\n[{"title":"Weekly incoming","dataset":"weeklyIncoming","metric":"invoices","chart":"line","why":"Volume rose 25% in the last week"},' +
  '{"title":"Work by area","dataset":"receivedByArea","metric":"invoices","chart":"bar","why":"La Prairie receives most of the invoices"},' +
  '{"title":"Made up","dataset":"secretNumbers","metric":"value","chart":"bar"},' +
  '{"title":"Donut of a percentage","dataset":"within24hByCompanyCode","metric":"percent","chart":"donut"},' +
  '{"title":"Who acts","dataset":"whoActs","metric":"invoices","chart":"donut"},' +
  '{"title":"Line on a split","dataset":"receivedByArea","metric":"invoices","chart":"line"}]\n```' } }];
const chartSheet = makeSheet(400).map((x, i) => ({ json: { ...x.json, Status: i % 5 ? 'Completed' : 'Pending', 'Invoice upload Date': i % 5 ? (i % 3 ? x.json.Received_Date : x.json.Invoice_Date) : '',
  Category: i % 3 === 0 ? 'No Portal Access' : i % 2 ? 'Quantity Mismatch' : 'PO unavailable on portal', 'Reason for Pending': i % 5 ? '' : 'Email sent on 1 Oct' } }));
const C1 = fullRun(chartSheet, TABLE_ROW, [{ json: {} }], { chartsAi: chartAi });
const c1 = C1['Add AI Charts'][0];
assert(c1.json.aiCharts === true && c1.json.chartsUsed.join() === 'weeklyIncoming/invoices/line,receivedByArea/invoices/bar,within24hByCompanyCode/percent/bar,whoActs/invoices/donut',
  'AI chart choices used (max 4); unknown dataset dropped; a donut of percentages drawn as bar: ' + c1.json.chartsUsed.join(', '));
assert(/La Prairie receives most of the invoices/.test(c1.json.html) && !/Volume rose/.test(c1.json.html), 'AI "why" shown, but a "why" containing numbers is dropped');
const facts1 = JSON.parse(C1['Build Report'][0].json.facts);
const m0 = facts1.charts.weeklyIncoming.at(-2);
assert(c1.json.html.includes(m0.received.toLocaleString('en-US')), 'chart figures come from the report facts');
const dash1 = Buffer.from(c1.binary.dashboard.data, 'base64').toString();
assert(!c1.json.html.includes('<!--charts-->') && !dash1.includes('<!--charts-->') && /<svg/.test(dash1) && /<polyline/.test(dash1) && /<path d="M /.test(dash1),
  'charts placed in the email (tables) and in dashboard.html (SVG: line for the trend, donut)');
assert(!/<svg/.test(c1.json.html), 'no SVG in the email (Outlook cannot show it) – email charts are tables');
assert(c1.json.to === 'me@example.com' && c1.json.subject && c1.binary.dashboard.fileName === 'dashboard.html', 'email item still has to, subject and attachment');
const C0 = fullRun(makeSheet(400), TABLE_ROW, [{ json: {} }], { chartsAi: [{ json: { text: '[{"title":"Open by area","dataset":"openByArea","metric":"invoices","chart":"bar"}]' } }] });
assert(C0['Add AI Charts'][0].json.aiCharts === false, 'a chart with only zeros (nothing open) is not drawn');
const C2 = fullRun(chartSheet, TABLE_ROW, [{ json: {} }], { chartsAi: [{ json: { text: 'Sure! Here are some ideas for charts.' } }] });
assert(C2['Add AI Charts'][0].json.aiCharts === false && C2['Add AI Charts'][0].json.chartsUsed.length >= 2 && /Standard highlight charts/.test(C2['Add AI Charts'][0].json.html),
  'unusable AI answer → standard charts: ' + C2['Add AI Charts'][0].json.chartsUsed.join(', '));
const C3 = fullRun(chartSheet, TABLE_ROW, [{ json: {} }]);
assert(C3['Add AI Charts'][0].json.aiCharts === false && /Standard highlight charts/.test(C3['Add AI Charts'][0].json.html), 'AI chart step failed → standard charts, email still goes out');
if (process.env.CHART_OUT) { fs.writeFileSync(process.env.CHART_OUT + '_email.html', c1.json.html); fs.writeFileSync(process.env.CHART_OUT + '_dash.html', dash1); }

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
  { json: { Code: 'GWJ1', 'Company Code': '3060', 'Profit Center': 'GPJ908', Product: 'X', 'Product Line': 'PTI', 'Nature of Activities PL': 'Manufacturing', 'Customer Number': 106685, 'Key Customer': 'SIEMENS', 'Customer Name': 'SIEMENS AG', 'Billing Document': 9001400001, 'Accounting Document': 2000000001 } },
  { json: { Code: 'GWJ1', 'Company Code': '3485', 'Profit Center': ' gpj777 ', 'Product Line': 'AIS', 'Customer Number': 80950, 'Key Customer': 'EATON', 'Customer Name': 'EATON', 'Billing Document': ' 9,001,400,002 ' } },
  { json: { Code: 'GWJ1', 'Company Code': '3487', 'Profit Center': '', 'Customer Number': 22806, 'Customer Name': 'ABB', 'Billing Document': '9001400003.0' } },
  { json: { 'Company Code': 'G367', 'Profit Center': 'GPIM0D', 'Product Line': 'PQP', 'Customer Number': 99999, 'Billing Document': 7001300001 } }, // G367 is in Tableau too
  { json: { 'Company Code': 'GWJ1', 'Profit Center': 'GPXXXX', 'Product Line': 'XXX', 'Customer Number': 12345, 'Billing Document': 7001300002 } }, // other company code: ignored
];
const earlier = [ // the Data Table before this upload: 9001400004 was matched last time, is not in today's Tableau file
  { ...TABLE_ROW, id: 7, Invoice: 9001400004, Company_Code: '3060', SAP_Customer_Code: '45454', Profit_Center: 'GPJ123', Product_Line: 'GIS' },
];
const L = fullRun(lookSheet, earlier, [{ json: {} }], { zsd: zsd.concat(NOFILE.slice(0, 0)), zsd2025, tableau });
const by = Object.fromEntries(L['Rows to Save'].map((i) => [i.json.Invoice, i.json]));
assert(by[7001300001].Company_Code === 'G367' && by[7001300002].Company_Code === 'G367', 'tracker sales org G36C / GS5C → company code G367');
assert(by[7001300001].SAP_Customer_Code === '89598' && by[7001300002].SAP_Customer_Code === '170940', 'G367: SAP customer code from the ZSD log (2026 and 2025 sheets)');
assert(by[7001300001].Profit_Center === 'GPIM0D' && by[7001300001].SAP_Customer_Code === '89598', 'G367 looked up in Tableau too: profit centre from Tableau, SAP code from ZSD first');
assert(by[7001300002].Profit_Center === null && by[7001300002].Product_Line === 'PQP', 'Tableau rows of other company codes (GWJ1, GS52) are ignored; G367 without Tableau product line = PQP');
assert(by[9001400001].SAP_Customer_Code === '106685' && by[9001400001].Profit_Center === 'GPJ908', '3060: SAP customer code and profit centre from Tableau ("Customer Number", not "Key Customer"/"Customer Name")');
assert(by[9001400002].Profit_Center === 'GPJ777' && by[9001400003].SAP_Customer_Code === '22806' && by[9001400003].Profit_Center === null,
  'cleaned before matching: leading zeros, spaces, commas, "9001400003.0"; profit centre tidied to GPJ777; empty stays empty');
assert(by[9001400004].SAP_Customer_Code === '45454' && by[9001400004].Profit_Center === 'GPJ123' && by[9001400004].Product_Line === 'GIS', 'invoice no longer in the Tableau file keeps the codes found on an earlier upload');
assert(/SAP customer code found for 6 of 6 invoices · profit centre found for 4 of 6/.test(L['Summarise Upload'][0].json.message), 'Done page: ' + L['Summarise Upload'][0].json.message.match(/SAP customer code.*?\)/)[0]);
assert(by[9001400001].Product_Line === 'PTI' && by[9001400002].Product_Line === 'AIS' && by[9001400001].Business_Type === 'MANUFACTURING' && by[9001400002].Business_Type === null,
  'product line ("Product Line" chosen over "Product") and activity ("Nature of Activities PL") from Tableau');
assert(by[7001300001].Business_Type === 'MANUFACTURING' && by[7001300002].Business_Type === 'MANUFACTURING', 'Clearwater (G367): activity Manufacturing');
assert(L['Rows to Save'].every((i) => !('_lookupNotes' in i.json)), 'helper notes are not saved to the Data Table');
const doneMsg = L['Summarise Upload'][0].json.message;
assert(/Columns used – Read ZSD Log: 1 matching rows \(invoice column "Billing Doc\.", customer code "Customer"\)/.test(doneMsg) && /product line "Product Line"/.test(doneMsg),
  'Done page lists the columns used from each file');
const lh = L['Build Report'][0].json.html;
assert(by[7001300001].Sales_Org === 'G36C' && by[7001300002].Sales_Org === 'GS5C' && by[9001400001].Sales_Org === null, 'sales org kept for G367 (G36C / GS5C), empty for the others');
const sectionOf = (html, n) => html.slice(html.indexOf(`>${n}. `), html.indexOf(`>${n + 1}. `) > 0 ? html.indexOf(`>${n + 1}. `) : undefined);
const pcPart = sectionOf(lh, 5); const ccPart = sectionOf(lh, 6);
assert(/Profit centre analysis/.test(pcPart) && /GPJ908/.test(pcPart) && /GPJ777/.test(pcPart) && /NOT FOUND/.test(pcPart) && /GPIM0D/.test(pcPart),
  'profit centre section: every profit centre (incl. G367 from Tableau) and NOT FOUND as a gap');
const block3060 = ccPart.slice(ccPart.indexOf('3060 – LA PRAIRIE'), ccPart.indexOf('3485 – CHARLEROI'));
assert(/SIEMENS \(SAP 106685\)/.test(block3060) && !/EATON/.test(block3060) && /EATON \(SAP 80950\)/.test(ccPart) && /IDAHO POWER COMPANY \(SAP 89598\)/.test(ccPart.slice(ccPart.indexOf('G367 – CLEARWATER'))),
  'company code section: each company code lists only its own customers, always with the SAP customer code');
const lf = JSON.parse(L['Build Report'][0].json.facts);
assert(lf.focus === 'invoice distribution' && lf.profitCentres.some((x) => x.profitCentre === 'GPJ908') && lf.companyCodes.find((x) => x.companyCode === '3060').topCustomers.some((c) => c.customer === 'SIEMENS (SAP 106685)'),
  'AI facts: profit centres, and customers inside their company code with SAP code');
const dash = Buffer.from(L['Build Report'][0].binary.dashboard.data, 'base64').toString();
if (process.env.DASH_OUT) fs.writeFileSync(process.env.DASH_OUT, dash);
assert(/id="pc"/.test(dash) && /<option>GPJ908<\/option>/.test(dash) && /id="pl"/.test(dash), 'dashboard has profit centre and product line filters');
const wrongZsd = fullRun(lookSheet, {}, [{ json: {} }], { zsd: [{ json: { A: 1, B: 'x' } }] });
assert(wrongZsd['Rows to Save'].every((i) => i.json.SAP_Customer_Code === null), 'a file with no matching invoice numbers fills nothing (no guessing)');

// ---------- 5b. structure check: a profit centre under two company codes is a data problem ----------
const treeOf = (rowsIn) => {
  const out = { 'Add Lookups': rowsIn.map((json) => ({ json })), 'Summarise Upload': [{ json: { message: '' } }] };
  run(out, 'Build Report', [], withMail);
  return out['Build Report'][0];
};
const mk = (i, cc, pc, bt, pl) => ({ Invoice: 8000000000 + i, Value: '100', Customer: 'C' + (i % 4), Company_Code: cc, Received_Date: '2026-03-' + String(1 + (i % 20)).padStart(2, '0'),
  Profit_Center: pc, Business_Type: bt, Product_Line: pl, Sales_Org: null });
const clean = [];
for (let i = 0; i < 40; i++) clean.push(mk(i, ['3060', '3485'][i % 2], i % 2 ? 'PC-B' : (i % 4 < 2 ? 'PC-A1' : 'PC-A2'), i % 3 ? 'MANUFACTURING' : 'SERVICES', i % 3 ? 'PTI' : 'AIS'));
assert(!/Check the data/.test(treeOf(clean).json.html), 'one product line under several profit centres is normal, no warning');
const messyTree = clean.map((r, i) => (i === 0 ? { ...r, Company_Code: '3485', Profit_Center: 'PC-A1' } : r));
assert(/Check the data: 1 profit centre\(s\) appear under more than one company code \(PC-A1\)/.test(treeOf(messyTree).json.html), 'a profit centre under two company codes is pointed out');

// ---------- 5c. pending invoices, ageing and follow-ups ----------
const pend = [ // like the tracker screenshot; "today" = 2026-10-08
  { json: { 'Invoice#': 7001238182, '$ Value': '$411', 'Company Code': 'G367', Status: 'Pending', 'Invoice upload Date': 'NA', TAT: 'NA', 'Uploaded by': 'Tushar',
    Category: 'PO Lines not available on Portal', 'Reason for Pending': 'PO lines not available on portal. Email sent to Romero Walter on 23 June. Follow up email sent on 3 July.', Received_Date: '2026-06-20', Customer: 'IDAHO POWER' } },
  { json: { 'Invoice#': 7001264821, '$ Value': '$28,687', 'Company Code': 'G367', Status: 'Pending', 'Uploaded by': 'Tushar', Category: 'Quantity Mismatch',
    'Reason for Pending': 'Quantity Mismatch. Email sent to Stacy on 10 Sep', Received_Date: '2026-09-08', Customer: 'SALT RIVER' } },
  { json: { 'Invoice#': 7001265146, '$ Value': '$158,466', 'Company Code': '3485', Status: 'Pending', 'Uploaded by': 'Tushar', Category: 'PO unavailable on portal',
    'Reason for Pending': 'PO unavailable on portal. Email sent to Michael Gralewski on 10 Sep and mail sent on 19th september for follow up. Follow up email sent to Gavin on 6 Oct', Received_Date: '2026-09-09', Customer: 'EXELON' } },
  { json: { 'Invoice#': 7001247206, '$ Value': '$1,682', 'Company Code': 'G367', Status: 'Pending', 'Uploaded by': 'Abdul', Category: 'Unable to create invoice',
    'Reason for Pending': 'PO lines unavailable on portal. Escalated to Dispute Team (Yogita) for review.', Received_Date: '2026-07-15', Customer: 'EKU' } },
  { json: { 'Invoice#': 7001156057, '$ Value': '$19,589', 'Company Code': '3060', Status: 'Pending', 'Uploaded by': 'Tushar', Category: 'No Portal Access',
    'Reason for Pending': 'No Portal Access. Email sent to Bruno on 28 Aug', Received_Date: '2026-08-25', Customer: 'HYDRO' } },
  { json: { 'Invoice#': 7001100001, '$ Value': '$5,000', 'Company Code': '3060', Status: 'Completed', 'Invoice upload Date': '2026-10-02', 'Uploaded by': 'Lynette', Received_Date: '2026-09-28', Customer: 'HYDRO',
    'Reason for Pending': 'old note 1 Jan' } },
  { json: { 'Invoice#': 7001100002, '$ Value': '$7,000', 'Company Code': '3060', Status: 'Uploaded', TAT: '3', 'Uploaded by': 'Lynette', Received_Date: '2026-10-01', Customer: 'HYDRO' } },
];
const P = fullRun(pend, TABLE_ROW, [{ json: {} }]);
const saved = Object.fromEntries(P['Rows to Save'].map((i) => [i.json.Invoice, i.json]));
assert(saved[7001238182].Status === 'Pending' && saved[7001238182].Upload_Date === null && saved[7001238182].Tracker_TAT === null && saved[7001238182].Uploaded_By === 'Tushar'
  && saved[7001238182].Pending_Category === 'PO Lines not available on Portal' && /Romero Walter/.test(saved[7001238182].Pending_Reason), 'tracker Status / upload date / TAT / uploaded by / category / reason saved ("NA" → empty)');
const pendOf = (f) => ({ open: f.totals.open, countedTo: f.daysCountedTo, actNow: f.pending.oldestOpen, followUpDue: f.totals.followUpDue,
  blockers: f.pending.rootCauses.map((b) => ({ blocker: b.rootCause, invoices: b.open, who: b.whoActs })), pastDue: f.totals.pastDue, whoActs: f.pending.whoActs });
const pf = pendOf(JSON.parse(P['Build Report'][0].json.facts));
assert(pf.open === 5 && pf.countedTo === '2026-10-08', '5 open items (Completed / Uploaded are not pending), counted to today');
const act = Object.fromEntries(pf.actNow.map((x) => [x.invoice, x]));
assert(act['7001238182'].daysPending === 110 && act['7001238182'].lastAction === '2026-07-03' && act['7001238182'].followUps === 2 && act['7001238182'].daysSinceLastAction === 97,
  'dates read from the reason: 23 June + 3 July → 2 follow-ups, last action 3 July, 97 days ago; 110 days pending');
assert(act['7001265146'].followUps === 3 && act['7001265146'].lastAction === '2026-10-06' && act['7001265146'].daysSinceLastAction === 2, '"10 Sep", "19th september", "6 Oct" all read; followed up 2 days ago');
assert(act['7001247206'].lastAction === null && act['7001247206'].followUps === 0, 'no date in the reason → no follow-up logged');
assert(pf.pastDue === undefined && pf.followUpDue === 5, 'no "past due" yet (needs payment terms); follow-up due (nothing logged for 2+ days): 5');
const bl = Object.fromEntries(pf.blockers.map((b) => [b.blocker, b.invoices]));
assert(bl['PO issue on portal'] === 3 && bl['Invoice vs PO mismatch'] === 1 && bl['Portal access'] === 1, 'blocker groups: ' + JSON.stringify(bl));
const who = Object.fromEntries(pf.whoActs.map((x) => [x.who, x.open]));
assert(who['Ours (distribution team)'] === 1 && who['Customer / GE order team'] === 4 && pf.blockers.find((b) => b.blocker === 'Portal access').who === 'Ours (distribution team)',
  'portal access is ours to act on; PO issues and mismatches wait on the customer / GE order team: ' + JSON.stringify(who));
const sc = Object.fromEntries(P['Rows to Save'].map((i) => [i.json.Invoice, i.json.Standard_Category]));
assert(sc[7001238182] === 'PO lines not available on portal' && sc[7001264821] === 'Quantity mismatch' && sc[7001265146] === 'PO not available on portal'
  && sc[7001156057] === 'No portal access / portal migration' && sc[7001100001] === null,
  'standard categories by fixed rules; completed rows get none');
assert(sc[7001247206] === 'PO lines not available on portal', '"Unable to create invoice" with reason "PO lines unavailable" → the cause (PO lines) wins');
assert(pf.actNow.map((x) => x.invoice).join() === '7001238182,7001247206,7001156057,7001264821,7001265146', 'oldest open invoices first: ' + pf.actNow.map((x) => x.invoice).join(', '));
// TAT: one rule – received → submitted; open ones count to today; the tracker's own TAT column is not used
const tq = fullRun([
  { json: { 'Invoice#': 7003000001, '$ Value': '10', 'Company Code': '3060', Status: 'Completed', Received_Date: '2026-10-01', 'Invoice upload Date': '2026-10-01', TAT: '5', Customer: 'A' } },
  { json: { 'Invoice#': 7003000002, '$ Value': '10', 'Company Code': '3060', Status: 'Completed', Received_Date: '2026-10-01', 'Invoice upload Date': '2026-10-02', Customer: 'A' } },
  { json: { 'Invoice#': 7003000003, '$ Value': '10', 'Company Code': '3485', Status: 'Completed', Received_Date: '2026-10-01', 'Invoice upload Date': '2026-10-05', TAT: '1', Customer: 'B' } },
  { json: { 'Invoice#': 7003000004, '$ Value': '10', 'Company Code': '3485', Status: 'Pending', Category: 'No Portal Access', Received_Date: '2026-10-02', Customer: 'B' } },
  { json: { 'Invoice#': 7003000005, '$ Value': '10', 'Company Code': '3485', Status: 'Pending', Category: 'No Portal Access', Received_Date: '2026-10-08', Customer: 'B' } },
  { json: { 'Invoice#': 7003000006, '$ Value': '10', 'Company Code': '3485', Status: 'Completed', Received_Date: '2026-10-03', Customer: 'B' } },
], TABLE_ROW, [{ json: {} }]);
const tf = JSON.parse(tq['Build Report'][0].json.facts).totals;
assert(tf.within24h === 2 && tf.over24h === 2 && tf.stillWithin24hOpen === 1 && tf.tatUnknown === 1 && tf.within24hPercent === 50 && tf.avgTatDays === 1.67,
  'TAT = received → submitted (tracker TAT ignored): same day and next day within 24 h, 4 days over, open 6 days over, open today still within, no upload date unknown: ' + JSON.stringify({ a: tf.within24h, b: tf.over24h, c: tf.stillWithin24hOpen, d: tf.tatUnknown, e: tf.within24hPercent, f: tf.avgTatDays }));
assert(/Completed without an upload date \(TAT unknown\)/.test(tq['Build Report'][0].json.html) && /within 24 h/.test(tq['Build Report'][0].json.subject), 'TAT gaps listed in data quality; subject shows the 24-hour share: ' + tq['Build Report'][0].json.subject);
const ph = P['Build Report'][0].json.html;
assert(!/Past due/.test(ph) && /Pending invoices – full list \(5\)/.test(ph) && /Root causes holding invoices/.test(ph) && /Status by area and company code/.test(ph)
  && /Ageing of open invoices by area/.test(ph) && /90\+ days/.test(ph) && /Romero Walter/.test(ph) && !/Act now|Customers to look out for/.test(ph),
  'report: status by area, root causes, ageing by area, full pending list with reasons');
for (const [n, t] of [[1, 'Headline'], [2, 'Volume and scope of work'], [3, '24-hour TAT'], [4, 'Pending invoices'], [5, 'Profit centre analysis'], [6, 'Company code analysis'], [7, 'Customer names and SAP codes'], [8, 'Pending reasons'], [9, 'Data quality']]) {
  assert(ph.includes(`>${n}. ${t}`), `section ${n}: ${t}`);
}
assert(/Who has to act/.test(ph) && /Pareto/.test(ph) && /Root cause × company code/.test(ph) && /Swim lanes/.test(ph) && /Volume heatmap – company code × month/.test(ph) && /Workload heatmap by area/.test(ph) && /Within 24 hours by company code/.test(ph),
  'visuals: who acts, Pareto, root cause × company code heatmap, swim lanes, volume heatmap, day-of-month heatmap, 24-hour bars');
const pdash = Buffer.from(P['Build Report'][0].binary.dashboard.data, 'base64').toString();
const pd = {}; new Function('document', pdash.slice(pdash.indexOf('<script>') + 8, pdash.indexOf('</script>')))({ getElementById: (x) => (pd[x] = pd[x] || { value: '', set innerHTML(v) { pd.html = v; } }) });
assert(/<svg/.test(pd.html) && /hover a dot for the invoice/.test(pd.html) && /7001238182 · CLEARWATER G367/.test(pd.html) && /cumulative share/.test(pd.html),
  'dashboard runs in the browser: SVG swim lanes (a dot per invoice), Pareto, donuts');
const listPart = ph.slice(ph.indexOf('Pending invoices – full list'), ph.indexOf('>5. '));
const listOrder = ['7001156057', '7001238182', '7001247206', '7001265146', '7001264821'].map((x) => listPart.indexOf(x));
assert(listOrder.every((x, i) => x > 0 && (i === 0 || x > listOrder[i - 1])), 'full list: ours (portal access) first, then PO issues (PO lines, PO missing), then mismatches; oldest first within a category');
assert(/CLEARWATER \/ G367/.test(listPart) && /Days since/.test(listPart) && /Follow-ups/.test(listPart) && /Profit centre/.test(listPart) && /Activity/.test(listPart) && /IDAHO POWER \(no SAP code\)/.test(listPart),
  'each pending invoice shows area / company code, profit centre, product line, activity, customer with SAP code, days pending, root cause, last action, days since, follow-ups, owner');
assert(P['Rows to Save'].every((i) => i.json.Invoice !== 7001100001 || i.json.Status === 'Completed'), 'completed rows saved too');
const yr = fullRun([
  { json: { 'Invoice#': 7002000001, '$ Value': '10', 'Company Code': '3060', Status: 'Pending', 'Uploaded by': 'Abdul', Category: 'Quantity Mismatch', Customer: 'OLD',
    'Reason for Pending': 'Email sent on 23 June. Follow up on 3 July. Escalated 3 Feb. Chased again 20 June', Received_Date: '2025-06-01' } },
  { json: { 'Invoice#': 7002000002, '$ Value': '20', 'Company Code': '3060', Status: 'Pending', 'Uploaded by': 'Abdul', Category: 'Quantity Mismatch', Customer: 'NODATE',
    'Reason for Pending': 'Email sent on 5 Oct' } },
  { json: { 'Invoice#': 7002000003, '$ Value': '30', 'Company Code': '3060', Status: 'Completed', Customer: 'X', Received_Date: '2026-10-01', 'Invoice upload Date': '2026-10-02' } },
], TABLE_ROW, [{ json: {} }]);
const yp = pendOf(JSON.parse(yr['Build Report'][0].json.facts));
const y1 = yp.actNow.find((x) => x.invoice === '7002000001');
assert(y1 && y1.followUps === 4 && y1.lastAction === '2026-06-20' && y1.daysPending === 494,
  'an item open since 2025: 23 June / 3 July read as 2025, 3 Feb and 20 June as 2026 (dates read in order)');
assert(yp.open === 2 && yp.actNow.some((x) => x.invoice === '7002000002' && x.daysPending === null && x.lastAction === '2026-10-05'), 'a pending item with no dates at all is still counted (days pending unknown)');
if (process.env.PEND_OUT) fs.writeFileSync(process.env.PEND_OUT, ph.replace('<!--charts-->', ''));

// ---------- 5d. AI only for wordings the rules cannot place; answers limited to the fixed list; remembered ----------
const odd = [
  { json: { 'Invoice#': 7009000001, '$ Value': '100', 'Company Code': '3060', Status: 'pending', 'Uploaded by': 'TUSHAR', Category: 'Customer awaiting GRN', 'Reason for Pending': 'Goods receipt not done by site', Received_Date: '2026-09-01', Customer: 'A' } },
  { json: { 'Invoice#': 7009000002, '$ Value': '100', 'Company Code': '3060', Status: 'In Progress', 'Uploaded by': 'tushar', Category: 'Weird thing', 'Reason for Pending': 'Something odd', Received_Date: '2026-09-01', Customer: 'A' } },
  { json: { 'Invoice#': 7009000003, '$ Value': '100', 'Company Code': '3060', Status: 'Pending', 'Uploaded by': 'Abdul', Category: 'Customer awaiting GRN', 'Reason for Pending': 'Goods receipt not done by site', Received_Date: '2026-09-02', Customer: 'B' } },
  { json: { 'Invoice#': 7009000004, '$ Value': '100', 'Company Code': '3060', Status: 'Pending', Received_Date: '2026-09-02', Customer: 'C' } },
  { json: { 'Invoice#': 7009000005, '$ Value': '100', 'Company Code': '3060', Status: '', 'Reason for Pending': 'email sent 2 Oct', Received_Date: '2026-09-02', Customer: 'C' } },
  { json: { 'Invoice#': 7009000006, '$ Value': '100', 'Company Code': '3060', Status: 'Done', Received_Date: '2026-09-02', Customer: 'C' } },
  { json: { 'Invoice#': 7009000007, '$ Value': '100', 'Company Code': '3060', Status: 'Pending', 'Uploaded by': 'Abdul', 'Invoice upload Date': '2026-09-20', Category: 'Quantity Mismatch', Received_Date: '2026-09-02', Customer: 'C' } },
];
let seenByAi = null;
const fakeAi = (items) => { seenByAi = items; return [{ json: { text: JSON.stringify(items.map((x) => ({ id: x.id, category: /grn|goods/i.test(x.text) ? 'PO not available on portal' : 'Totally new category' }))) } }]; };
const O = fullRun(odd, TABLE_ROW, [{ json: {} }], { blockerAi: fakeAi });
const os = Object.fromEntries(O['Rows to Save'].map((i) => [i.json.Invoice, i.json]));
assert(seenByAi.length === 2, 'AI sees only the 2 distinct wordings the rules cannot place (same wording asked once): ' + seenByAi.map((x) => x.text).join(' | '));
assert(os[7009000001].Standard_Category === 'PO not available on portal' && os[7009000003].Standard_Category === 'PO not available on portal', 'same wording → same AI category');
assert(os[7009000002].Standard_Category === 'Other', 'an AI answer outside the fixed list becomes "Other"');
assert(os[7009000001].Status === 'Pending' && os[7009000002].Status === 'Pending' && os[7009000006].Status === 'Completed' && os[7009000001].Uploaded_By === 'Tushar' && os[7009000002].Uploaded_By === 'Tushar',
  'status and owner names standardized ("pending"/"In Progress" → Pending, "Done" → Completed, "TUSHAR"/"tushar" → Tushar)');
// next upload: the remembered category is reused, the AI is not asked again
const earlierTable = O['Rows to Save'].map((i) => ({ ...i.json, id: 1 }));
let asked = null;
const O2 = fullRun(odd, earlierTable, [{ json: {} }], { blockerAi: (items) => { asked = items; return [{ json: { text: '[]' } }]; } });
assert(asked.length === 0 && O2['Rows to Save'].find((i) => i.json.Invoice === 7009000001).json.Standard_Category === 'PO not available on portal', 'next upload: remembered categories reused, AI not asked again');
const O3 = fullRun(odd, TABLE_ROW, [{ json: {} }]); // AI unavailable
assert(O3['Rows to Save'].find((i) => i.json.Invoice === 7009000001).json.Standard_Category === 'Other' && /set to "Other" \(AI gave no answer\)/.test(O3['Summarise Upload'][0].json.message),
  'AI unavailable → "Other", and the Done page says so');
const dm = O['Summarise Upload'][0].json.message;
if (process.env.STD_OUT) fs.writeFileSync(process.env.STD_OUT, fullRun(pend.concat(odd), TABLE_ROW, [{ json: {} }], { blockerAi: fakeAi })['Build Report'][0].json.html.replace('<!--charts-->', ''));
assert(/1 with no status \(e\.g\. 7009000005\)/.test(dm) && /1 with pending status but no reason \(e\.g\. 7009000004\)/.test(dm) && /1 with pending status but no owner/.test(dm)
  && /1 with pending status but an upload date \(e\.g\. 7009000007\)/.test(dm) && /1 with completed status but no upload date or TAT \(e\.g\. 7009000006\)/.test(dm),
  'Done page flags blanks and contradictions: ' + dm.match(/\d+ with no status.*TAT[^·]*/)[0]);
const oq = JSON.parse(O['Build Report'][0].json.facts).dataGaps.map((x) => x.issue + ':' + x.count).join(', ');
assert(/No status:1/.test(oq) && /Pending without a reason:1/.test(oq) && /Pending but has an upload date:1/.test(oq) && /To fill in|Pending without a reason/.test(O['Build Report'][0].json.html), 'report data quality lists what to fill in: ' + oq);

// ---------- 5e. customer names and SAP codes ----------
const idRows = [
  ['ACME POWER INC', '111', '3060'], ['ACME POWER INC.', '111', '3060'], ['Acme Power, Inc', '111', '3060'],
  ['ZENITH STEEL WORKS', '111', '3060'], ['NORTH GRID', '222', '3485'], ['NORTH GRID', '333', '3485'],
  ['BLUEWATER UTILITIES', '', '3060'], ['BLUEWATR UTILITIES', '', '3060'], ['BLUEWATR UTILITIES', '', '3485'],
].map(([c, sap, cc], i) => ({ Invoice: 8100000000 + i, Value: '10', Customer: c.toUpperCase(), Company_Code: cc, Received_Date: '2026-10-01', SAP_Customer_Code: sap || null, Status: 'Completed', Upload_Date: '2026-10-01' }));
const idRep = treeOf(idRows);
const idPart = sectionOf(idRep.json.html, 7);
assert(/Same name, different SAP codes \(1\)/.test(idPart) && /NORTH GRID/.test(idPart) && /222 \(1 · 3485\); 333 \(1 · 3485\)/.test(idPart), 'same name with two SAP codes: kept apart and listed');
assert(/One SAP code, different spellings \(1\)/.test(idPart) && /ACME POWER INC/.test(idPart) && /ACME POWER INC\. \(1\)/.test(idPart) && /ACME POWER, INC \(1\)/.test(idPart), 'one SAP code with three spellings: counted once, other spellings listed explicitly');
assert(/ZENITH STEEL WORKS \(1\) <span[^>]*>– very different name, check the SAP code/.test(idPart) && !/ACME POWER INC\. \(1\) <span/.test(idPart), 'a completely different name under the same SAP code is flagged (a wrong code, not a typo)');
assert(/Look-alike names in the same company code \(1\)/.test(idPart) && /BLUEWATER UTILITIES \(no SAP code\)/.test(idPart) && /BLUEWATR UTILITIES \(no SAP code\)/.test(idPart) && /please check/.test(idPart),
  'typo without SAP code: flagged for checking inside its company code (3060 only), not joined');
const id6 = sectionOf(idRep.json.html, 6);
assert((id6.match(/ACME POWER INC \(SAP 111\)/g) || []).length === 1 && /NORTH GRID \(SAP 222\)/.test(id6) && /NORTH GRID \(SAP 333\)/.test(id6), 'company code section counts a customer by SAP code, not by spelling');

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
