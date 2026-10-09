// Pick Tracker File — choose the exact file from the OneDrive search results.
// Stops with a clear message if the file is missing or the name matches more than one file.
// ONLY_WHEN_CHANGED: skip the run (no upsert, no report) when the file's version (eTag) is the same as
// the last successful scheduled run. Manual test runs always process the file.
const TRACKER_NAME = 'Trackers - NAM Distribution.xlsx';
const ONLY_WHEN_CHANGED = true;

// Microsoft Graph returns the search results as { value: [...] }; accept a plain list too
const found = $input.all().flatMap((i) => (Array.isArray(i.json.value) ? i.json.value : [i.json]));
const matches = found.filter((f) => f.file && f.name === TRACKER_NAME);
if (matches.length === 0) {
  throw new Error(`"${TRACKER_NAME}" was not found in your OneDrive. Check the file name in TRACKER_NAME ` +
    'and the search text on "Find Tracker".');
}
if (matches.length > 1) {
  const where = matches.map((f) => f.parentReference?.path ?? f.webUrl ?? f.id).join(' | ');
  throw new Error(`${matches.length} files are named "${TRACKER_NAME}": ${where}. Rename or move the extra copies.`);
}
const file = matches[0];

const memory = $getWorkflowStaticData('global');
if (ONLY_WHEN_CHANGED && memory.lastETag && memory.lastETag === file.eTag) {
  return []; // unchanged since the last run – nothing to do
}
return [{
  json: { id: file.id, name: file.name, eTag: file.eTag, lastModified: file.lastModifiedDateTime },
}];
