// Compare with Table — keep only invoices that are new or changed, so saving takes seconds, not minutes.
// If the table is empty, or more than BULK_LIMIT rows changed (e.g. the very first upload), ALL rows are passed on
// for a fast "clear table + bulk add" instead. Keep BULK_LIMIT the same as in the "Few changes?" step.
const BULK_LIMIT = 300;

const cleaned = $('Clean Rows').all().map((i) => i.json);
const columns = Object.keys(cleaned[0] || {});
const existing = new Map();
for (const { json: r } of $input.all()) {
  if (r.Invoice === undefined || r.Invoice === null || r.Invoice === '') continue; // empty table gives one empty item
  existing.set(String(r.Invoice), r);
}
const same = (a, b) => String(a ?? '').trim() === String(b ?? '').trim();
const changed = cleaned.filter((r) => {
  const before = existing.get(String(r.Invoice));
  return !before || columns.some((c) => !same(r[c], before[c]));
});
const rows = !existing.size || changed.length > BULK_LIMIT ? cleaned : changed;
return rows.map((json) => ({ json }));
