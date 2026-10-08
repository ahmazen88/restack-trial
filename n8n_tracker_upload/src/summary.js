// Summarise Upload — counts and data quality checks for the confirmation page.
// Fixed rules only (no clock, no randomness): the same file always gives the same result.
const KEY = 'Invoice';
const KEY_ALIASES = ['invoice', 'invoice no', 'invoice number', 'invoice #', 'inv no']; // keep in step with Clean Rows
const EARLIEST_DATE = '2020-01-01';
const DATE_COLUMNS = ['Received_Date', 'Allocated_Date', 'Invoice_Date'];
const LIST_LIMIT = 10;
const FILE_NAME = $('Upload Tracker').first().binary?.Tracker_File?.fileName ?? 'tracker';

const norm = (s) => String(s ?? '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
const keyNames = new Set([KEY, ...KEY_ALIASES].map(norm));
const num = (v) => {
  const n = parseFloat(String(v ?? '').replace(/[^0-9.\-]/g, ''));
  return Number.isFinite(n) ? n : null;
};

// Raw sheet: blank-key rows and repeated invoices
const raw = $('Read Tracker Sheet').all().map((i) => i.json);
const seen = new Map();
let blank = 0;
for (const r of raw) {
  const h = Object.keys(r).find((k) => keyNames.has(norm(k)));
  const id = h == null ? '' : String(r[h] ?? '').trim();
  if (!id) { blank++; continue; }
  seen.set(id, (seen.get(id) || 0) + 1);
}
const duplicates = [...seen].filter(([, n]) => n > 1).map(([id]) => id).sort();

// Cleaned rows: quality checks
const rows = $('Clean Rows').all().map((i) => i.json);
const checks = {
  'missing value': (r) => num(r.Value) === null,
  'zero or negative value': (r) => num(r.Value) !== null && num(r.Value) <= 0,
  'missing customer': (r) => !r.Customer,
  'missing company code': (r) => !r.Company_Code,
  'no readable date': (r) => DATE_COLUMNS.every((c) => !r[c]),
  [`date before ${EARLIEST_DATE}`]: (r) => DATE_COLUMNS.some((c) => r[c] && r[c] < EARLIEST_DATE),
  'allocated before received': (r) => r.Allocated_Date && r.Received_Date && r.Allocated_Date < r.Received_Date,
};
const issues = {};
for (const [label, test] of Object.entries(checks)) {
  const ids = rows.filter(test).map((r) => String(r[KEY]));
  if (ids.length) issues[label] = { count: ids.length, examples: ids.slice(0, LIST_LIMIT) };
}

const fmt = (n) => n.toLocaleString('en-US');
// how many rows were actually written (only present when the "Compare with Table" step is used)
const written = (() => {
  try { return $('Compare with Table').all().filter((i) => i.json.Invoice !== undefined && i.json.Invoice !== null && i.json.Invoice !== '').length; }
  catch (e) { return null; }
})();
const parts = written === null
  ? [`${fmt(rows.length)} invoices saved from ${fmt(raw.length)} rows`]
  : [`${fmt(rows.length)} invoices in the file (${fmt(raw.length)} rows) · ${fmt(written)} new or changed rows saved, the rest were already up to date`];
if (blank) parts.push(`${fmt(blank)} blank rows skipped`);
if (duplicates.length) {
  parts.push(`${fmt(duplicates.length)} invoices appear more than once (last row kept): ` +
    duplicates.slice(0, LIST_LIMIT).join(', ') + (duplicates.length > LIST_LIMIT ? ', …' : ''));
}
for (const [label, { count, examples }] of Object.entries(issues)) {
  parts.push(`${fmt(count)} with ${label} (e.g. ${examples.slice(0, 3).join(', ')})`);
}
if (!duplicates.length && !Object.keys(issues).length) parts.push('no data quality issues found');

return [{
  json: {
    file: FILE_NAME,
    rowsRead: raw.length,
    rowsSaved: rows.length,
    blankRows: blank,
    duplicateInvoices: duplicates,
    issues,
    message: parts.join(' · '),
  },
}];
