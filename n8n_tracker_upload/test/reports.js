// Offline test of Report Settings + Build Report with Data Table-shaped sample rows.
const fs = require('fs');
const path = require('path');
const wf = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'tracker_reports_workflow.json'), 'utf8'));
const code = (name) => wf.nodes.find((n) => n.name === name).parameters.jsCode;
const assert = (c, m) => { if (!c) { console.error('FAIL:', m); process.exit(1); } console.log('ok -', m); };
const run = (src, nodes, executed = []) => new Function('$', src)((n) => {
  if (!(n in nodes)) throw new Error(`no node ${n}`);
  return { all: () => nodes[n], first: () => nodes[n][0], isExecuted: executed.includes(n) };
});

// Deterministic sample: 2026-01-05 .. 2026-09-30, month-end peaks, a spiking customer, a new one, one gone quiet
const custs = ['RIO TINTO ALCAN INC', 'SALT RIVER PROJECT', 'EXELON ACCOUNTS PAYABLE', 'OGLETHORPE POWER CORPORATION', 'POWER LINE SUPPLY', 'BONNEVILLE POWER ADMINISTRATION'];
const portals = ['invoices@riotinto.com', 'apinv@srpnet.com', 'Taulia', 'OPCMXInvoices@opc.com', 'ap_pls@uscco.com', 'acctspay@bpa.gov'];
const pms = ['LOMBARD Axel', 'Martha Guerrero', 'Marlena Neufeld', 'SaintCilien Patricia'];
const rows = []; let inv = 7001200000;
for (let t = Date.UTC(2026, 0, 5); t <= Date.UTC(2026, 8, 30); t += 86400000) {
  const d = new Date(t); const day = d.getUTCDate(); const wd = d.getUTCDay();
  if (wd === 0 || wd === 6) continue;
  const n = 3 + (day >= 26 ? 4 : 0) + (wd === 1 ? 2 : 0);
  for (let k = 0; k < n; k++) {
    let ci = (inv + k) % 5;
    if (d.getUTCMonth() === 8 && k % 3 === 0) ci = 1; // SALT RIVER spikes in September
    const quietBpa = d.getUTCMonth() >= 8; // BPA active until August, then gone quiet
    const c = quietBpa ? custs[ci] : (k === 0 && day % 4 === 0 ? custs[5] : custs[ci]);
    const iso = d.toISOString().slice(0, 10);
    rows.push({ json: { id: rows.length + 1, Received_Date: iso, Allocated_Date: new Date(t + (c === custs[2] ? 5 : 1) * 86400000).toISOString().slice(0, 10),
      Invoice_Date: iso, Project_Manager: pms[k % 4], Customer: c, Name_the_PortalEmail_ID: portals[custs.indexOf(c)],
      Invoice: inv++, Value: String(((inv * 7919) % 60000) + 250), Company_Code: ['3060', '3485', '3487'][custs.indexOf(c) % 3] } });
  }
}
rows.push({ json: { ...rows[10].json, id: 99999, Customer: 'NEW CO LLC', Invoice: 7009999999, Received_Date: '2026-09-29', Value: '' } });

const triggers = ['Upload Tracker', 'Every Monday 7am', '1st of Month 7am'];
const settingsFor = (executed, form) => run(code('Report Settings'),
  { 'Request a Report': [{ json: form || {} }], ...Object.fromEntries(triggers.map((t) => [t, [{ json: {} }]])) }, executed)[0].json;
const build = (settings, recipients = "['a@example.com']") => {
  const src = code('Build Report').replace("const RECIPIENTS = [''];", `const RECIPIENTS = ${recipients};`);
  return run(src, { 'Report Settings': [{ json: settings }], 'Get All Rows': rows })[0];
};

assert(settingsFor(['Every Monday 7am']).type === 'Weekly', 'Monday schedule -> Weekly');
assert(settingsFor(['1st of Month 7am']).type === 'Monthly' && settingsFor(['1st of Month 7am']).source === 'schedule', '1st of month -> Monthly, no Done page');
assert(settingsFor(['Upload Tracker']).source === 'form', 'upload -> Overview with Done page');
const reqForm = { 'Report type': 'Custom period', From: '2026-06-01', To: '2026-08-31', 'Company code (optional)': '3485', 'Customer contains (optional)': '', 'Send to (optional)': 'boss@example.com' };
const req = settingsFor(['Request a Report'], reqForm);
assert(req.from === '2026-06-01' && req.companyCode === '3485' && req.sendTo === 'boss@example.com', 'request form choices read');

const monthly = build(settingsFor(['1st of Month 7am']));
assert(monthly.json.to === 'a@example.com', 'default recipients');
assert(/Distribution status by area/.test(monthly.json.html) && /Workload heatmap by area/.test(monthly.json.html) && /Pending invoices – full list/.test(monthly.json.html) && !/Customers to look out for|Customer details|Forecast/.test(monthly.json.html), 'distribution sections present, sales sections gone');
assert(JSON.stringify(build(settingsFor(['1st of Month 7am']))) === JSON.stringify(monthly), 'deterministic');
const custom = build(req);
assert(custom.json.to === 'boss@example.com' && /company code 3485/.test(custom.json.html) && /2026-06-01 to 2026-08-31/.test(custom.json.html), 'custom period + company code + recipient');
assert(!/rgb\(/.test(monthly.json.html), 'email-safe hex colours');
const weekly = build(settingsFor(['Every Monday 7am']));
assert(/Week of 2026-09-28/.test(weekly.json.subject), 'weekly report = latest week in data');
assert(/Add at least one email address/.test((() => { try { build(settingsFor(['Every Monday 7am']), '[]'); } catch (e) { return e.message; } })()), 'stops without recipients');

const dash = Buffer.from(monthly.binary.dashboard.data, 'base64').toString('utf8');
assert(monthly.binary.dashboard.fileName === 'dashboard.html' && /const ROWS = \[/.test(dash) && /function analyse/.test(dash), 'dashboard attachment built');
console.log('dashboard size KB:', Math.round(dash.length / 1024), '| rows:', rows.length, '| subject:', monthly.json.subject);
fs.writeFileSync(path.join(__dirname, 'sample_email.html'), monthly.json.html);
fs.writeFileSync(path.join(__dirname, 'sample_dashboard.html'), dash);
