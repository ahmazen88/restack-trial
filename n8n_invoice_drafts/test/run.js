// Offline test of the Code nodes with stand-ins for n8n's $ / $input.
const fs = require('fs');
const path = require('path');
const src = (f) => fs.readFileSync(path.join(__dirname, '..', 'src', f), 'utf8');
const assert = (c, m) => { if (!c) { console.error('FAIL:', m); process.exit(1); } console.log('ok -', m); };
const throws = (fn) => { try { fn(); return ''; } catch (e) { return e.message; } };
const run = (code, input, nodes = {}) => new Function('$', '$input', code)(
  (n) => { if (!(n in nodes)) throw new Error('no node ' + n); return { all: () => nodes[n], first: () => nodes[n][0], itemMatching: (i) => nodes[n][i] }; },
  { all: () => input, first: () => input[0] });

// Split
const split = run(src('split.js'), [{ json: { 'Invoice numbers': '7 001 206 102\n7001211479, 7001211479; 7009999999\n\nabc' } }]);
assert(split.map((i) => i.json.invoice).join() === '7001206102,7001211479,7009999999', 'split: spaces removed, duplicates and junk dropped');
assert(/at least one/.test(throws(() => run(src('split.js'), [{ json: { 'Invoice numbers': 'none' } }]))), 'split: empty input stops');

// Pick (Box search results, each paired to the requested number)
const search = [
  { json: { id: 'F1', type: 'file', name: '2026-04-01_7001206102_222123.pdf', path_collection: { entries: [{ name: 'All Files' }, { name: 'Invoices' }] } }, pairedItem: { item: 0 } },
  { json: { id: 'F9', type: 'file', name: 'Statement_March.pdf' }, pairedItem: { item: 0 } }, // content match, but name match wins
  { json: { id: 'F2', type: 'file', name: 'HAMEEDA PT10024010667_1.pdf' }, pairedItem: { item: 1 } }, // only result -> accepted, verified later
];
const picked = run(src('pick.js'), search, { 'Split Invoice Numbers': split });
assert(picked.length === 2 && picked[0].json.id === 'F1' && picked[1].json.id === 'F2', 'pick: name match preferred; single content match accepted');
assert(picked[0].json.folder === 'All Files / Invoices', 'pick: Box folder shown');
assert(/7009999999: no PDF found/.test(picked[0].json.problems.join()), 'pick: missing invoice reported');
const amb = [{ json: { id: 'A', type: 'file', name: 'x_7001206102.pdf' }, pairedItem: { item: 0 } }, { json: { id: 'B', type: 'file', name: 'y_7001206102.pdf' }, pairedItem: { item: 0 } }];
assert(/No invoice could be prepared.*2 possible files/.test(throws(() => run(src('pick.js'), amb, { 'Split Invoice Numbers': [split[0]] }))), 'pick: two files with the same number -> not guessed');

// Build Drafts (PDF text as Extract From File gives it)
const pdfText = `GE Vernova\nINVOICE\nInvoice Number: 7001206102\nInvoice Date: 04/01/2026\nBill To:\nRIO TINTO ALCAN INC\n1188 Sherbrooke St W\nPurchase Order No: 4500123456\nPayment Due: 05/01/2026\nTotal Amount Due USD 156,377.00`;
const items = [
  { json: { text: pdfText }, binary: { data: { fileName: '2026-04-01_7001206102_222123.pdf', mimeType: 'application/pdf' } } },
  { json: { text: 'Some other document without the number' }, binary: { data: { fileName: 'HAMEEDA PT10024010667_1.pdf' } } },
];
const nodes = { 'Pick Invoice Files': picked, 'Request Invoices': [{ json: { 'Send drafts to (optional)': '' } }] };
const code = src('drafts.js').replace("const SEND_DRAFTS_TO = '';", "const SEND_DRAFTS_TO = 'me@example.com';");
const d = run(code, items, nodes);
const h = d[0].json.html;
assert(d[0].json.to === 'me@example.com' && d[0].binary.data.fileName.includes('7001206102'), 'drafts go to me, PDF attached');
assert(/Invoice number found inside the PDF/.test(h) && d[0].json.verified, 'verified number inside PDF');
assert(/04\/01\/2026/.test(h) && /156,377\.00/.test(h) && /4500123456/.test(h) && /RIO TINTO ALCAN INC/.test(h) && /USD/.test(h), 'parsed date, amount, PO, customer, currency');
assert(/DRAFT – Invoice 7001206102 – RIO TINTO ALCAN INC/.test(d[0].json.subject), 'subject');
assert(!d[1].json.verified && /CHECK ATTACHMENT/.test(d[1].json.subject) && /NOT found inside the PDF/.test(d[1].json.html), 'unverified PDF clearly flagged');
assert(/Add your email address/.test(throws(() => run(src('drafts.js'), items, nodes))), 'stops without SEND_DRAFTS_TO');
const formOverride = run(src('drafts.js'), items, { ...nodes, 'Request Invoices': [{ json: { 'Send drafts to (optional)': 'other@example.com' } }] });
assert(formOverride[0].json.to === 'other@example.com', 'form address overrides');

// Summary
const s = run(src('summary.js'), [], { 'Build Drafts': d, 'Pick Invoice Files': picked })[0].json.message;
assert(/2 draft email\(s\) sent to me@example.com/.test(s) && /Check the attachment for: 7001211479/.test(s) && /7009999999: no PDF found/.test(s), 'done page summary');
fs.writeFileSync(path.join(__dirname, 'sample_draft.html'), h);
console.log('\nDone page:', s);
