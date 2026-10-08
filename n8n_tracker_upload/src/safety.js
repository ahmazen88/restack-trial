// Safety Check – runs BEFORE the table is emptied.
// If anything is wrong it stops here with a clear message, and the Data Table is left exactly as it was.
const rows = $('Clean Rows').all();
if (!rows.length) {
  throw new Error('No rows with an invoice number were found in the file. Nothing was changed.');
}
const columns = Object.keys(rows[0].json); // the columns Clean Rows will save
const sample = $input.first().json || {}; // one existing row of the Data Table (empty if the table is empty)
const tableColumns = Object.keys(sample);
if (tableColumns.length) {
  const missing = columns.filter((c) => !tableColumns.includes(c));
  if (missing.length) {
    throw new Error(`The Data Table has no column called: ${missing.join(', ')}. ` +
      'Check that "Check Table", "Clear Table" and "Save All Rows" all point to the right Data Table, ' +
      'or fix the names in COLUMNS on "Clean Rows". Nothing was changed.');
  }
}
return [{ json: { rowsToSave: rows.length, tableHadRows: tableColumns.length > 0 } }];
