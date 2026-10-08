// Report Settings — which report to build, depending on what started the run
const ran = (name) => { try { return $(name).isExecuted; } catch (e) { return false; } };
let s;
if (ran('Request a Report')) {
  const f = $('Request a Report').first().json;
  s = {
    source: 'form', type: f['Report type'] || 'Overview', from: f['From'] || '', to: f['To'] || '',
    companyCode: f['Company code (optional)'] || '', customer: f['Customer contains (optional)'] || '',
    sendTo: f['Send to (optional)'] || '',
  };
} else if (ran('Upload Tracker')) {
  s = { source: 'form', type: 'Overview' };
} else if (ran('Every Monday 7am')) {
  s = { source: 'schedule', type: 'Weekly' };
} else if (ran('1st of Month 7am')) {
  s = { source: 'schedule', type: 'Monthly' };
} else {
  s = { source: 'manual', type: 'Overview' };
}
return [{ json: s }];
