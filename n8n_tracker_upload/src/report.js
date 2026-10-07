// Build Report — a simple, rule-based Production Tracker report as an HTML email.
// Fixed rules only: the same tracker file always produces the same report.
const MONTHS_SHOWN = 12;
const TOP_CUSTOMERS = 10;
const DAYS_SHOWN = 14;
const DATE_ORDER = ['Received_Date', 'Allocated_Date', 'Invoice_Date']; // first filled date is used

const rows = $('Clean Rows').all().map((i) => i.json);
const quality = $('Summarise Upload').first().json;
const file = $('Pick Tracker File').first().json;

const num = (v) => {
  const n = parseFloat(String(v ?? '').replace(/[^0-9.\-]/g, ''));
  return Number.isFinite(n) ? n : 0;
};
const money = (n) => n.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
const count = (n) => n.toLocaleString('en-US');
const pct = (part, whole) => (whole ? ((part / whole) * 100).toFixed(1) + '%' : '–');
const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const dateOf = (r) => DATE_ORDER.map((c) => r[c]).find(Boolean) || null;

function group(keyOf) {
  const m = new Map();
  for (const r of rows) {
    const k = keyOf(r);
    if (!k) continue;
    const g = m.get(k) || { key: k, invoices: 0, value: 0 };
    g.invoices++;
    g.value += num(r.Value);
    m.set(k, g);
  }
  return [...m.values()];
}
const byValueThenKey = (a, b) => b.value - a.value || String(a.key).localeCompare(String(b.key));

const totalValue = rows.reduce((s, r) => s + num(r.Value), 0);
const months = group((r) => dateOf(r)?.slice(0, 7)).sort((a, b) => b.key.localeCompare(a.key)).slice(0, MONTHS_SHOWN);
const customers = group((r) => r.Customer || 'UNKNOWN CUSTOMER').sort(byValueThenKey);
const companies = group((r) => r.Company_Code || 'UNKNOWN COMPANY').sort(byValueThenKey);
const days = group((r) => dateOf(r)).sort((a, b) => b.key.localeCompare(a.key)).slice(0, DAYS_SHOWN);
const latestDate = days[0]?.key ?? '–';

const th = (align) => `style="text-align:${align};padding:6px 10px;background:#1f3a5f;color:#fff;font-weight:600"`;
const td = 'style="padding:5px 10px;border-bottom:1px solid #e5e7eb"';
const tdr = 'style="padding:5px 10px;border-bottom:1px solid #e5e7eb;text-align:right"';
function table(title, headers, data) {
  const head = headers.map((h, i) => `<th ${th(i ? 'right' : 'left')}>${esc(h)}</th>`).join('');
  const body = data.map((cells) => '<tr>' + cells.map((c, i) => `<td ${i ? tdr : td}>${esc(c)}</td>`).join('') + '</tr>').join('');
  return `<h3 style="margin:22px 0 8px;color:#1f3a5f">${esc(title)}</h3>` +
    `<table cellspacing="0" style="border-collapse:collapse;font-size:13px;min-width:420px">` +
    `<tr>${head}</tr>${body || `<tr><td ${td} colspan="${headers.length}">No data</td></tr>`}</table>`;
}
const kpi = (label, value) =>
  `<td style="padding:10px 18px;border:1px solid #e5e7eb"><div style="font-size:12px;color:#6b7280">${esc(label)}</div>` +
  `<div style="font-size:20px;font-weight:700;color:#111827">${esc(value)}</div></td>`;

const issueLines = [
  ...(quality.blankRows ? [`${count(quality.blankRows)} blank rows skipped`] : []),
  ...(quality.duplicateInvoices.length ? [`${count(quality.duplicateInvoices.length)} invoices appear more than once (last row kept)`] : []),
  ...Object.entries(quality.issues).map(([label, { count: n, examples }]) => `${count(n)} with ${label} (e.g. ${examples.slice(0, 3).join(', ')})`),
];

const html = `<div style="font-family:Segoe UI,Arial,sans-serif;color:#111827;max-width:900px">
<h2 style="margin:0 0 4px;color:#1f3a5f">Production Tracker Report</h2>
<div style="color:#6b7280;font-size:13px">Source: ${esc(file.name)} · file saved ${esc(String(file.lastModified ?? '').slice(0, 16).replace('T', ' '))} UTC · latest activity date ${esc(latestDate)}</div>
<table cellspacing="0" style="border-collapse:collapse;margin:16px 0"><tr>
${kpi('Invoices', count(rows.length))}${kpi('Total value', money(totalValue))}${kpi('Customers', count(customers.length))}${kpi('Company codes', count(companies.length))}
</tr></table>
${table(`Monthly summary (last ${MONTHS_SHOWN} months)`, ['Month', 'Invoices', 'Value'],
    months.map((g) => [g.key, count(g.invoices), money(g.value)]))}
${table(`Top ${TOP_CUSTOMERS} customers by value`, ['Customer', 'Invoices', 'Value', 'Share'],
    customers.slice(0, TOP_CUSTOMERS).map((g) => [g.key, count(g.invoices), money(g.value), pct(g.value, totalValue)]))}
${table('Company codes', ['Company code', 'Invoices', 'Value', 'Share'],
    companies.map((g) => [g.key, count(g.invoices), money(g.value), pct(g.value, totalValue)]))}
${table(`Daily activity (last ${DAYS_SHOWN} active days)`, ['Date', 'Invoices', 'Value'],
    days.map((g) => [g.key, count(g.invoices), money(g.value)]))}
<h3 style="margin:22px 0 8px;color:#1f3a5f">Data quality</h3>
<ul style="font-size:13px;margin:0;padding-left:18px">${issueLines.length ? issueLines.map((l) => `<li>${esc(l)}</li>`).join('') : '<li>No data quality issues found</li>'}</ul>
<p style="color:#9ca3af;font-size:11px;margin-top:24px">Generated automatically by n8n from the tracker file. Dates use ${DATE_ORDER.join(' → ')} (first filled).</p>
</div>`;

return [{
  json: {
    subject: `Production Tracker Report – ${count(rows.length)} invoices · ${money(totalValue)} · as of ${latestDate}`,
    html,
    invoices: rows.length,
    totalValue,
  },
}];
