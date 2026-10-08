// Rows to Save — after the table is cleared, pass all rows (with SAP customer code and profit centre) to the bulk save
return $('Add Lookups').all().map((i) => ({ json: i.json }));
