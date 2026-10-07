// Summarise Upload — one item for the confirmation page
const read = $('Read Tracker Sheet').all().length;
const saved = $('Clean Rows').all().length;
return [{
  json: {
    file: $('Upload Tracker').first().binary?.Tracker_File?.fileName ?? 'tracker',
    rowsRead: read,
    rowsSaved: saved,
    rowsSkipped: read - saved,
    uploadedAt: new Date().toISOString().replace('T', ' ').slice(0, 16),
  },
}];
