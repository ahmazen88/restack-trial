// Build Log Entry — one row per processed file
const before = new Set(
  $('Read Tracker').all().map((i) => String(i.json['Item ID'] ?? '').trim()).filter(Boolean),
);
const files = {};
for (const { json: r } of $('Normalize Report Rows').all()) {
  const f = (files[r._fileId] ??= { name: r._sourceFile, rows: 0, skipped: 0, ids: new Set() });
  f.rows++;
  if (r._skip) f.skipped++;
  else f.ids.add(String(r['Item ID']).trim());
}
const now = new Date().toISOString().replace('T', ' ').slice(0, 16);
return Object.entries(files).map(([fileId, f]) => {
  const ids = [...f.ids];
  const added = ids.filter((id) => !before.has(id)).length;
  return {
    json: {
      Timestamp: now,
      'Source File': f.name,
      'File ID': fileId,
      'Rows Read': f.rows,
      'Items Updated': ids.length - added,
      'Items Added': added,
      'Rows Skipped': f.skipped,
      Result: f.skipped === f.rows ? 'No rows matched – check column names' : 'Processed',
    },
  };
});
