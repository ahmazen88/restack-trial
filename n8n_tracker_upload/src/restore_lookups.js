// Rows to Save — after the table is cleared, pass all rows (with the looked-up codes) to the bulk save.
// Helper fields starting with "_" are not saved.
return $('Add Lookups').all().map((i) => ({
  json: Object.fromEntries(Object.entries(i.json).filter(([k]) => !k.startsWith('_'))),
}));
