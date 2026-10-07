// Build Rejected Log — files that are not CSV / Excel
const now = new Date().toISOString().replace('T', ' ').slice(0, 16);
return $input.all().map((_, i) => {
  const f = $('New File in Inbox').itemMatching(i).json;
  return {
    json: {
      Timestamp: now,
      'Source File': f.name,
      'File ID': f.id,
      'Rows Read': 0,
      'Items Updated': 0,
      'Items Added': 0,
      'Rows Skipped': 0,
      Result: 'Rejected – unsupported file type (use .csv, .xlsx or .xls)',
    },
  };
});
