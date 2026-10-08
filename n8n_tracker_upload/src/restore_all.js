// Rows to Save — after the table is cleared, pass all cleaned rows on to be saved in one bulk call
return $('Clean Rows').all().map((i) => ({ json: i.json }));
