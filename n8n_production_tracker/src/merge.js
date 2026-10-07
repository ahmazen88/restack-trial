// Merge Into Tracker
// 'cumulative' = report quantities are totals to date (overwrite).
// 'incremental' = report quantities are today's output (added to the tracker).
const QTY_MODE = 'cumulative';
const COLUMNS = ['Item ID', 'Description', 'Category', 'Location / Line', 'Unit', 'Planned Qty', 'Actual Qty', 'Rejected Qty', 'Remaining Qty', '% Complete', 'Planned Finish', 'Status', 'Remarks', 'Last Updated', 'Source File'];
const DERIVED = new Set(['Item ID', 'Remaining Qty', '% Complete', 'Status', 'Last Updated', 'Source File']);
const MANUAL_STATUSES = ['On Hold', 'Cancelled'];

const num = (v) => {
  const n = parseFloat(String(v ?? '').replace(/[,%\s]/g, ''));
  return Number.isFinite(n) ? n : 0;
};
const today = new Date().toISOString().slice(0, 10);

const tracker = new Map();
for (const { json } of $('Read Tracker').all()) {
  const id = String(json['Item ID'] ?? '').trim();
  if (id) tracker.set(id, json);
}

const changed = new Map();
for (const { json: r } of $('Normalize Report Rows').all()) {
  if (r._skip) continue;
  const id = String(r['Item ID']).trim();
  const row = { ...(changed.get(id) || tracker.get(id) || {}) };
  row['Item ID'] = id;

  for (const col of COLUMNS) {
    if (DERIVED.has(col) || r[col] === undefined) continue;
    const additive = QTY_MODE === 'incremental' && (col === 'Actual Qty' || col === 'Rejected Qty');
    row[col] = additive ? num(row[col]) + r[col] : r[col];
  }

  const planned = num(row['Planned Qty']);
  const actual = num(row['Actual Qty']);
  const pct = planned > 0 ? Math.min(actual / planned, 1) : 0;
  row['Remaining Qty'] = planned > 0 ? Math.max(planned - actual, 0) : '';
  row['% Complete'] = planned > 0 ? Math.round(pct * 1000) / 1000 : '';

  if (r.Status) {
    row.Status = r.Status;
  } else if (!MANUAL_STATUSES.includes(row.Status)) {
    const finish = row['Planned Finish'] ? new Date(row['Planned Finish']) : null;
    if (planned > 0 && actual >= planned) row.Status = 'Complete';
    else if (finish && !isNaN(finish) && finish.toISOString().slice(0, 10) < today) row.Status = 'Behind Schedule';
    else if (actual > 0) row.Status = 'In Progress';
    else row.Status = 'Not Started';
  }

  row['Last Updated'] = new Date().toISOString().replace('T', ' ').slice(0, 16);
  row['Source File'] = r._sourceFile;
  changed.set(id, row);
}

// Always emit at least one item so the log step still runs when nothing matched
if (!changed.size) return [{ json: {} }];
return [...changed.values()].map((row) => ({
  json: Object.fromEntries(COLUMNS.map((c) => [c, row[c] ?? ''])),
}));
