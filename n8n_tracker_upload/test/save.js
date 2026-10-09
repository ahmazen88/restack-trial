// Offline tests: Compare with Table / Restore Rows / Summarise counts / AI commentary step / Build Report facts
const fs = require('fs');
const path = require('path');
const src = (f) => fs.readFileSync(path.join(__dirname, '..', 'src', f), 'utf8');
const assert = (c, m) => { if (!c) { console.error('FAIL:', m); process.exit(1); } console.log('ok -', m); };
const run = (code, input, nodes = {}) => new Function('$', '$input', code)(
  (n) => { if (!(n in nodes)) throw new Error('no node ' + n); return { all: () => nodes[n], first: () => nodes[n][0] }; },
  { all: () => input, first: () => input[0] });

const row = (inv, v, c = 'RIO TINTO ALCAN INC') => ({ Invoice: inv, Value: v, Customer: c, Company_Code: '3060', Project_Manager: 'LOMBARD Axel',
  Name_the_PortalEmail_ID: 'invoices@riotinto.com', Received_Date: '2026-04-06', Allocated_Date: '2026-04-06', Invoice_Date: '2026-04-06' });
const cleaned = Array.from({ length: 1000 }, (_, i) => ({ json: row(7001200000 + i, String(100 + i)) }));
const table = cleaned.map((i) => ({ json: { id: i.json.Invoice - 7001199999, createdAt: 'x', ...i.json } }));

// normal day: 2 changed + 1 new -> only 3 rows saved
const tableDay = table.slice(0, 999).map((i) => ({ json: { ...i.json } }));
tableDay[5].json.Value = '1'; tableDay[7].json.Customer = 'OLD NAME';
const out = run(src('compare.js'), tableDay, { 'Clean Rows': cleaned });
assert(out.length === 3 && out.map((o) => o.json.Invoice).join() === '7001200005,7001200007,7001200999', 'only changed + new rows passed on');
assert(!('id' in out[0].json) && !('createdAt' in out[0].json), 'no table system fields passed on');
// number vs text in table is not a change
const typed = table.map((i) => ({ json: { ...i.json, Invoice: String(i.json.Invoice), Value: Number(i.json.Value) } }));
assert(run(src('compare.js'), typed, { 'Clean Rows': cleaned }).length === 0, 'same values with different types = unchanged');
// empty table -> all rows (bulk add)
assert(run(src('compare.js'), [{ json: {} }], { 'Clean Rows': cleaned }).length === 1000, 'empty table: all rows for bulk add');
// many changes (> 300) -> all rows (clear + bulk add)
const tableMany = table.map((i, k) => ({ json: { ...i.json, Customer: k < 400 ? 'Rio Tinto' : i.json.Customer } }));
assert(run(src('compare.js'), tableMany, { 'Clean Rows': cleaned }).length === 1000, '400 changes: all rows for clear + bulk add');
// nothing changed -> no rows (n8n then passes one empty item to "Anything to save?" = false)
assert(run(src('compare.js'), table, { 'Clean Rows': cleaned }).length === 0, 'nothing changed: nothing saved');
// restore
assert(run(src('restore.js'), [{ json: {} }], { 'Compare with Table': out }).length === 3, 'restore rows after clear');

// "Few changes?" decision (same expression as the If node)
const wf = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'tracker_reports_workflow.json'), 'utf8'));
const expr = wf.nodes.find((n) => n.name === 'Few changes?').parameters.conditions.conditions[0].leftValue.replace(/^=\{\{|\}\}$/g, '');
const few = (tableItems, compareItems) => new Function('$', `return (${expr});`)((n) => ({ all: () => (n === 'Get Table Rows' ? tableItems : compareItems) }));
assert(few(tableDay, out) === true, 'If: few changes -> save changed rows');
assert(few([{ json: {} }], cleaned) === false, 'If: empty table -> clear + bulk add');
assert(few(tableMany, cleaned) === false, 'If: many changes -> clear + bulk add');

// Summarise shows how many rows were written
const sumNodes = { 'Read Tracker Sheet': cleaned, 'Clean Rows': cleaned, 'Compare with Table': out, 'Upload Tracker': [{ json: {}, binary: { Tracker_File: { fileName: 't.xlsx' } } }] };
const msg = run(src('summary.js'), [], sumNodes)[0].json.message;
assert(/1,000 invoices in the file .* 3 new or changed rows saved/.test(msg), 'summary: rows written reported');

// AI commentary step
const base = [{ json: { html: '<div>REPORT</div>', subject: 's', to: 'a@x' }, binary: { dashboard: { fileName: 'dashboard.html' } } }];
const good = run(src('commentary.js'), [{ json: { text: '```html\n<h3 class="x">Summary</h3><p onclick="evil()">Incoming invoices rose 12% to 1,020.</p><script>alert(1)</script><a href="http://x">link</a><ul><li><b>SALT RIVER PROJECT</b> – volume spike</li></ul>```' } }], { 'Build Report': base })[0];
assert(good.json.aiUsed && good.json.html.endsWith('<div>REPORT</div>') && /AI commentary/.test(good.json.html), 'AI text placed above the report');
assert(!/script|onclick|href|class=|```/.test(good.json.html.split('<div>REPORT')[0]), 'AI HTML cleaned (no scripts, links, attributes)');
assert(good.binary.dashboard.fileName === 'dashboard.html', 'dashboard attachment kept');
const failed = run(src('commentary.js'), [{ json: { error: 'model unavailable' } }], { 'Build Report': base })[0];
assert(!failed.json.aiUsed && failed.json.html === '<div>REPORT</div>', 'AI failure: report sent without commentary');
const plain = run(src('commentary.js'), [{ json: { text: 'Summary: volume steady at 1,020 invoices this month.\n\nWatch SALT RIVER PROJECT closely this week.' } }], { 'Build Report': base })[0];
assert(/<p>Summary: volume steady/.test(plain.json.html), 'plain-text AI answer wrapped in paragraphs');

// Build Report facts for the AI
const build = wf.nodes.find((n) => n.name === 'Build Report').parameters.jsCode.replace("const RECIPIENTS = [''];", "const RECIPIENTS = ['a@x'];");
const rep = new Function('$', build)((n) => ({ all: () => (n === 'Get All Rows' ? table : []), first: () => (n === 'Report Settings' ? { json: { type: 'Overview' } } : { json: { message: 'Upload ok' } }) }))[0];
const facts = JSON.parse(rep.json.facts);
assert(facts.focus === 'invoice distribution' && facts.totals.received > 0 && Array.isArray(facts.pending.rootCauses) && Array.isArray(facts.byArea) && Array.isArray(facts.companyCodes) && facts.volume.last12Months > 0 && !('watchlist' in facts), 'facts for AI built (distribution focus, no customer watchlist)');
assert(/Upload result:/.test(rep.json.html), 'upload result shown in the email');
assert(JSON.stringify(facts).length < 12000, `facts are compact (${JSON.stringify(facts).length} chars)`);
