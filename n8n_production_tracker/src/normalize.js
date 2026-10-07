// Normalize Report Rows
// Maps whatever column names the dropped report uses onto the tracker columns.
// Add your own report headings to ALIASES (any case / punctuation is fine).
const ALIASES = {
  'Item ID': ['item id', 'item no', 'item', 'id', 'job', 'job no', 'job id', 'work order', 'wo', 'wo no', 'order no', 'activity id', 'activity code', 'boq ref', 'tag', 'tag no', 'ref'],
  'Description': ['description', 'desc', 'activity', 'item description', 'product', 'task', 'scope'],
  'Category': ['category', 'discipline', 'trade', 'product type', 'type', 'system'],
  'Location / Line': ['location / line', 'location', 'line', 'area', 'zone', 'floor', 'level', 'work center', 'work centre', 'machine', 'station', 'building'],
  'Unit': ['unit', 'uom', 'units'],
  'Planned Qty': ['planned qty', 'planned', 'plan qty', 'target', 'target qty', 'scope qty', 'boq qty', 'total qty', 'order qty', 'qty planned', 'budget qty'],
  'Actual Qty': ['actual qty', 'actual', 'produced', 'produced qty', 'completed qty', 'qty completed', 'done', 'installed', 'installed qty', 'output', 'qty', 'quantity', 'to date'],
  'Rejected Qty': ['rejected qty', 'rejected', 'scrap', 'defects', 'ncr qty', 'rework', 'rejects'],
  'Planned Finish': ['planned finish', 'due', 'due date', 'finish', 'target date', 'planned end', 'end date', 'deadline'],
  'Remarks': ['remarks', 'comments', 'notes', 'comment', 'note'],
  'Status': ['status', 'state'],
};
const NUMERIC = new Set(['Planned Qty', 'Actual Qty', 'Rejected Qty']);

const key = (s) => String(s ?? '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
const lookup = new Map();
for (const [col, names] of Object.entries(ALIASES)) for (const n of names) lookup.set(key(n), col);

const toNumber = (v) => {
  if (typeof v === 'number') return v;
  const n = parseFloat(String(v ?? '').replace(/[,\s]/g, ''));
  return Number.isFinite(n) ? n : undefined;
};
const toDate = (v) => {
  if (v === '' || v == null) return undefined;
  // Excel serial dates come through as numbers
  if (typeof v === 'number' && v > 20000 && v < 80000) {
    return new Date(Date.UTC(1899, 11, 30) + v * 86400000).toISOString().slice(0, 10);
  }
  const d = new Date(v);
  return isNaN(d) ? String(v) : d.toISOString().slice(0, 10);
};

const out = [];
for (let i = 0; i < $input.all().length; i++) {
  const raw = $input.all()[i].json;
  const file = $('New File in Inbox').itemMatching(i).json;
  const row = { _sourceFile: file.name, _fileId: file.id };
  for (const [header, value] of Object.entries(raw)) {
    const col = lookup.get(key(header));
    if (!col || row[col] !== undefined || value === '' || value == null) continue;
    if (NUMERIC.has(col)) {
      const n = toNumber(value);
      if (n !== undefined) row[col] = n;
    } else if (col === 'Planned Finish') {
      row[col] = toDate(value);
    } else {
      row[col] = String(value).trim();
    }
  }
  if (!row['Item ID']) row._skip = true;
  out.push({ json: row, pairedItem: i });
}
return out;
