// Clean Rows
// 1. COLUMNS = the exact column names in your n8n Data Table (only these are sent).
// 2. ALIASES = other headings the SharePoint tracker might use for the same column.
// 3. TYPES   = 'string' (default), 'number', 'numberText' (plain number stored as text, e.g. 1157.44)
//             or 'date' – match your Data Table column types
//             (the Column list in the Data Table node shows each type, e.g. "Invoice (number)").
//             'date' also turns Excel serial dates (e.g. 46118) into 2026-04-06.
// 4. KEY     = the column that identifies a row (matches existing rows so they are not duplicated).
const COLUMNS = ['Invoice', 'Value', 'Customer', 'Company_Code', 'Project_Manager', 'Name_the_PortalEmail_ID',
  'Received_Date', 'Allocated_Date', 'Invoice_Date',
  'Status', 'Upload_Date', 'Tracker_TAT', 'Uploaded_By', 'Pending_Category', 'Pending_Reason'];
const ALIASES = {
  Invoice: ['invoice', 'invoice no', 'invoice number', 'invoice #', 'inv no'],
  Value: ['value', 'amount', 'invoice value'],
  Customer: ['customer', 'customer name', 'client'],
  Company_Code: ['company code', 'coco', 'co code', 'company_code'],
  Project_Manager: ['project manager', 'pm', 'manager'],
  Name_the_PortalEmail_ID: ['name the portal email id', 'portal email id', 'portal email', 'portal', 'email id',
    'submission portal'],
  Received_Date: ['received date', 'date received', 'received'],
  Allocated_Date: ['allocated date', 'date allocated', 'allocated'],
  Invoice_Date: ['invoice date', 'inv date'],
  Status: ['status', 'invoice status'],
  Upload_Date: ['invoice upload date', 'upload date', 'uploaded date', 'invoice upload dt', 'date uploaded'],
  Tracker_TAT: ['tat', 'turn around time', 'turnaround time', 'tat days'],
  Uploaded_By: ['uploaded by', 'processed by', 'owner', 'done by'],
  Pending_Category: ['category', 'pending category', 'blocker category'],
  Pending_Reason: ['reason for pending', 'pending reason', 'reason', 'comments', 'remarks'],
};
const TYPES = { Invoice: 'number', Value: 'numberText', Received_Date: 'date', Allocated_Date: 'date', Invoice_Date: 'date',
  Upload_Date: 'date', Tracker_TAT: 'numberText' }; // "NA" in a date or TAT cell becomes empty
const KEY = 'Invoice';
const UPPER = ['Customer', 'Company_Code']; // made upper case so spelling variants group together
// The tracker sometimes holds the sales org instead of the company code. Left = sales org, right = real company code.
const COMPANY_CODE_FIX = { G36C: 'G367', GS5C: 'G367' };

// Status in one standard wording (first matching rule wins); anything else is kept as written
const STATUS_RULES = [
  [/hold/i, 'On hold'],
  [/cancel|do not distribute/i, 'Cancelled'],
  [/pend|open|progress|query|block|wip/i, 'Pending'],
  [/complet|done|upload|submit|sent|distribut|closed|invoiced|posted/i, 'Completed'],
];
const standardStatus = (t) => (t ? (STATUS_RULES.find(([re]) => re.test(t)) || [null, t])[1] : null);
const norm = (s) => String(s ?? '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
const lookup = new Map();
for (const col of COLUMNS) {
  lookup.set(norm(col), col);
  for (const a of ALIASES[col] || []) lookup.set(norm(a), col);
}
// Excel serial day numbers (e.g. 46118 = 2026-04-06); the time of day is ignored
const fromSerial = (n) => (n >= 20000 && n <= 80000
  ? new Date(Date.UTC(1899, 11, 30) + Math.floor(n) * 86400000).toISOString().slice(0, 10) : null);
const pad = (n) => String(n).padStart(2, '0');
const convert = (col, v) => {
  if (v === '' || v == null) return null;
  if (TYPES[col] === 'number' || TYPES[col] === 'numberText') {
    if (typeof v === 'number') return Number.isFinite(v) ? (TYPES[col] === 'number' ? v : String(v)) : null;
    let t = String(v).trim().replace(/[\s,$€£]/g, '');
    const negative = /^\(.*\)$/.test(t) || t.startsWith('-'); // (1157.44) and -1157.44 are negative amounts
    t = t.replace(/^\((.*)\)$/, '$1').replace(/^-/, '');
    if (TYPES[col] === 'number') t = t.replace(/\.0+$/, '');
    // whole value must be a plain number: "7001 / 7002" or "INV-12" are not guessed
    if (!(TYPES[col] === 'number' ? /^\d+$/ : /^\d*\.?\d+$/).test(t)) return null;
    const n = Number(t) * (negative ? -1 : 1);
    return TYPES[col] === 'number' ? n : String(n);
  }
  if (TYPES[col] === 'date') {
    if (typeof v === 'number') return fromSerial(v);
    const t = String(v).trim();
    if (/^\d{5}(\.\d+)?$/.test(t)) return fromSerial(Number(t));
    const iso = t.match(/^(\d{4})-(\d{2})-(\d{2})/);
    if (iso) return `${iso[1]}-${iso[2]}-${iso[3]}`;
    const d = new Date(t); // e.g. 4/6/2026 (US order) or "Apr 6, 2026"
    return isNaN(d) ? null : `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
  }
  const text = String(v).replace(/\s+/g, ' ').trim();
  if (col === 'Status') return standardStatus(text);
  if (col === 'Uploaded_By') return text.toLowerCase().replace(/\b[a-z]/g, (c) => c.toUpperCase()); // "TUSHAR" / "tushar" → "Tushar"
  const out = UPPER.includes(col) ? text.toUpperCase() : text;
  return col === 'Company_Code' && COMPANY_CODE_FIX[out] ? COMPANY_CODE_FIX[out] : out;
};

// Stop early on the wrong file / wrong tab instead of saving nothing
const input = $input.all().filter((i) => Object.keys(i.json || {}).length);
if (!input.length) throw new Error('The uploaded sheet is empty. Check the file and the Sheet Name option on "Read Tracker Sheet". Nothing was changed.');
// Excel leaves empty cells out of a row, so collect the headings from every row
const headings = [...new Set(input.flatMap((i) => Object.keys(i.json)))];
if (!headings.some((h) => lookup.get(norm(h)) === KEY)) {
  throw new Error(`No "${KEY}" column found. Headings in the sheet: ${headings.join(', ')}. ` +
    'Check the file, the Sheet Name option on "Read Tracker Sheet", or add the heading to ALIASES. Nothing was changed.');
}

const rows = new Map();
for (const { json: raw } of input) {
  const row = {};
  for (const [header, value] of Object.entries(raw)) {
    const col = lookup.get(norm(header));
    if (col && row[col] == null) row[col] = convert(col, value);
  }
  if (row[KEY] == null || row[KEY] === '') continue; // blank / totals rows
  for (const col of COLUMNS) if (!(col in row)) row[col] = null;
  rows.set(String(row[KEY]), row); // a repeated key keeps the last row
}
return [...rows.values()].map((json) => ({ json }));
