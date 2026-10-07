// Clean Rows
// 1. COLUMNS = the exact column names in your n8n Data Table (only these are sent).
// 2. ALIASES = other headings the SharePoint tracker might use for the same column.
// 3. TYPES   = 'string' (default), 'number' or 'date' – match your Data Table column types.
// 4. KEY     = the column that identifies a row (matches existing rows so they are not duplicated).
const COLUMNS = ['Invoice', 'Value', 'Customer', 'Company_Code', 'Received_Date', 'Allocated_Date', 'Invoice_Date'];
const ALIASES = {
  Invoice: ['invoice', 'invoice no', 'invoice number', 'invoice #', 'inv no'],
  Value: ['value', 'amount', 'invoice value', 'total'],
  Customer: ['customer', 'customer name', 'client'],
  Company_Code: ['company code', 'coco', 'co code', 'company_code'],
  Received_Date: ['received date', 'date received', 'received'],
  Allocated_Date: ['allocated date', 'date allocated', 'allocated'],
  Invoice_Date: ['invoice date', 'inv date'],
};
const TYPES = {};
const KEY = 'Invoice';

const norm = (s) => String(s ?? '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
const lookup = new Map();
for (const col of COLUMNS) {
  lookup.set(norm(col), col);
  for (const a of ALIASES[col] || []) lookup.set(norm(a), col);
}
const convert = (col, v) => {
  if (v === '' || v == null) return null;
  if (TYPES[col] === 'number') {
    const n = parseFloat(String(v).replace(/[^0-9.\-]/g, ''));
    return Number.isFinite(n) ? n : null;
  }
  if (TYPES[col] === 'date') {
    const d = typeof v === 'number' ? new Date(Date.UTC(1899, 11, 30) + v * 86400000) : new Date(v);
    return isNaN(d) ? null : d.toISOString();
  }
  return String(v).trim();
};

const rows = new Map();
for (const { json: raw } of $input.all()) {
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
