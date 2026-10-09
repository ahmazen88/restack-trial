// Add AI Charts — the "AI Chart Designer" only CHOOSES which charts to show and why.
// Every figure is taken from the facts built by "Build Report"; numbers written by the AI are never shown.
// If the AI step failed or its answer is not usable, a standard set of charts is drawn instead.
const MAX_CHARTS = 4;
const DEFAULT_CHARTS = [
  { title: 'Who has to act on open invoices', dataset: 'whoActs', metric: 'invoices', chart: 'donut' },
  { title: 'What is holding invoices', dataset: 'rootCauses', metric: 'invoices', chart: 'bar' },
  { title: 'Within 24 hours by company code', dataset: 'within24hByCompanyCode', metric: 'percent', chart: 'bar' },
  { title: 'Invoices received per month', dataset: 'monthlyIncoming', metric: 'invoices', chart: 'column' },
];
// dataset (in facts.charts) → which field is the label and which fields hold each metric ("invoices" = count)
const DATASETS = {
  receivedByArea: { label: 'area', invoices: 'received', value: 'value' },
  receivedByCompanyCode: { label: 'companyCode', invoices: 'received', value: 'value' },
  receivedByProfitCentre: { label: 'profitCentre', invoices: 'received', value: 'value' },
  monthlyIncoming: { label: 'month', invoices: 'received', value: 'value' },
  weeklyIncoming: { label: 'weekStarting', invoices: 'received', value: 'value' },
  weeklyWithin24h: { label: 'weekStarting', percent: 'percent' },
  within24hByCompanyCode: { label: 'companyCode', percent: 'percent' },
  tatBuckets: { label: 'bucket', invoices: 'invoices' },
  openByArea: { label: 'area', invoices: 'open', value: 'value' },
  openByCompanyCode: { label: 'companyCode', invoices: 'open', value: 'value' },
  openByProfitCentre: { label: 'profitCentre', invoices: 'open', value: 'value' },
  whoActs: { label: 'who', invoices: 'open', value: 'value' },
  rootCauses: { label: 'rootCause', invoices: 'open', value: 'value' },
  ageing: { label: 'bucket', invoices: 'open', value: 'value' },
  channels: { label: 'channel', invoices: 'received' },
};
const TIME_SERIES = ['monthlyIncoming', 'weeklyIncoming', 'weeklyWithin24h'];
const KEEP_ORDER = ['ageing', 'tatBuckets']; // shown in their own order, not sorted by size
const PALETTE = ['#2b6cb0', '#0f766e', '#c2410c', '#7c3aed', '#b91c1c', '#6b7280'];
const COLORS = { bar: '#2b6cb0', part: '#9dbbe0', line: '#1f3a5f', grid: '#e5e7eb', ink: '#111827', mute: '#6b7280' };

const base = $('Add AI Commentary').first();
const facts = JSON.parse($('Build Report').first().json.facts || '{}');
// the chart datasets live in facts.charts
Object.assign(facts, facts.charts || {});
const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const fmt = (n, metric) => (metric === 'percent' ? `${n.toLocaleString('en-US', { maximumFractionDigits: 1 })}%`
  : metric === 'value' ? n.toLocaleString('en-US', { maximumFractionDigits: 0 })
    : n.toLocaleString('en-US', { maximumFractionDigits: 1 }));

// ---------- read the AI's choice (JSON list), keep only valid entries ----------
const raw = String($input.first().json.text ?? $input.first().json.output ?? '');
let picked = [];
try {
  const m = raw.replace(/```[a-z]*\n?/gi, '').match(/\[[\s\S]*\]/);
  picked = m ? JSON.parse(m[0]) : [];
} catch (e) { picked = []; }
const valid = (c) => c && DATASETS[c.dataset] && DATASETS[c.dataset][c.metric] && ['bar', 'column', 'line', 'donut'].includes(c.chart)
  && Array.isArray(facts[c.dataset]) && facts[c.dataset].filter((x) => Number(x[DATASETS[c.dataset][c.metric]]) > 0).length >= 2; // at least 2 non-zero values
let charts = (Array.isArray(picked) ? picked : []).filter(valid).slice(0, MAX_CHARTS).map((c) => ({
  title: String(c.title || '').replace(/[<>]/g, '').slice(0, 80) || `${c.metric} by ${c.dataset}`,
  dataset: c.dataset, metric: c.metric,
  // a line only for a time series; a donut only for a few parts of a whole (not for percentages)
  chart: c.chart === 'line' && !TIME_SERIES.includes(c.dataset) ? 'bar'
    : c.chart === 'donut' && (c.metric === 'percent' || TIME_SERIES.includes(c.dataset) || facts[c.dataset].length > 6) ? 'bar' : c.chart,
  // a short "why", only kept if it contains no numbers (figures must come from the data, not the AI)
  why: /\d/.test(String(c.why || '')) ? '' : String(c.why || '').replace(/[<>]/g, '').slice(0, 160),
}));
const aiUsed = charts.length > 0;
if (!aiUsed) charts = DEFAULT_CHARTS.filter(valid).map((c) => ({ ...c, why: '' }));

const points = (c) => {
  const d = DATASETS[c.dataset];
  // a month that is not finished yet is marked with * and drawn lighter, so it is not read as a fall in volume
  let list = facts[c.dataset].map((x) => ({ label: String(x[d.label]) + (x.monthToDate ? '*' : ''), y: Number(x[d[c.metric]]) || 0, part: !!x.monthToDate }));
  if (!TIME_SERIES.includes(c.dataset) && !KEEP_ORDER.includes(c.dataset)) {
    list = list.sort((a, b) => b.y - a.y).slice(0, 10); // biggest first, top 10
  }
  return list;
};

// ---------- email version: plain tables, works in Outlook ----------
const partNote = (pts) => (pts.some((p) => p.part)
  ? `<div style="color:${COLORS.mute};font-size:11px;margin-top:2px">* month to date – not a full month yet</div>` : '');
const emailChart = (c) => {
  const pts = points(c);
  const max = Math.max(1, ...pts.map((p) => p.y));
  const head = `<div style="font-weight:600;color:${COLORS.line};font-size:14px;margin:14px 0 2px">${esc(c.title)}</div>` +
    (c.why ? `<div style="color:${COLORS.mute};font-size:12px;margin-bottom:6px">${esc(c.why)}</div>` : '');
  if (c.chart === 'donut') { // email: one bar split into its parts
    const tot = pts.reduce((s, p) => s + p.y, 0) || 1;
    return head + '<table cellspacing="0" cellpadding="0" width="100%" style="max-width:860px"><tr>' +
      pts.filter((p) => p.y > 0).map((p, i) => `<td bgcolor="${PALETTE[i % PALETTE.length]}" width="${Math.max(1, Math.round((100 * p.y) / tot))}%" height="18" style="font-size:0;line-height:0">&nbsp;</td>`).join('') + '</tr></table>' +
      `<div style="font-size:11px;color:${COLORS.mute};margin-top:3px">${pts.filter((p) => p.y > 0).map((p, i) => `<span style="white-space:nowrap;margin-right:12px"><span style="display:inline-block;width:10px;height:10px;background:${PALETTE[i % PALETTE.length]}"></span> ${esc(p.label)}: ${fmt(p.y, c.metric)} (${((100 * p.y) / tot).toFixed(0)}%)</span>`).join('')}</div>`;
  }
  if (c.chart === 'bar') {
    return head + '<table cellspacing="0" cellpadding="0" style="border-collapse:collapse;width:100%;max-width:860px;font-size:12px">' +
      pts.map((p) => `<tr><td style="padding:3px 8px 3px 0;white-space:nowrap;width:28%">${esc(p.label)}</td>` +
        `<td style="padding:3px 0;width:57%"><table cellspacing="0" cellpadding="0" width="${Math.max(2, Math.round((100 * p.y) / max))}%"><tr>` +
        `<td bgcolor="${COLORS.bar}" height="12" style="font-size:0;line-height:0">&nbsp;</td></tr></table></td>` +
        `<td style="padding:3px 0 3px 8px;text-align:right;white-space:nowrap">${fmt(p.y, c.metric)}</td></tr>`).join('') + '</table>';
  }
  const H = 110; // column (and line, drawn as columns in email)
  return head + '<table cellspacing="2" cellpadding="0" style="font-size:10px;max-width:860px"><tr>' +
    pts.map((p) => { const h = Math.max(2, Math.round((H * p.y) / max)); return `<td valign="bottom" align="center" style="padding:0 2px">` +
      `<div style="color:${COLORS.mute};font-size:10px">${fmt(p.y, c.metric)}</div>` +
      `<table cellspacing="0" cellpadding="0" width="26"><tr><td bgcolor="${p.part ? COLORS.part : COLORS.bar}" height="${h}" style="font-size:0;line-height:0">&nbsp;</td></tr></table></td>`; }).join('') +
    '</tr><tr>' + pts.map((p) => `<td align="center" style="color:${COLORS.mute};padding-top:2px;white-space:nowrap">${esc(p.label)}</td>`).join('') +
    '</tr></table>' + partNote(pts);
};

// ---------- dashboard version: real SVG charts ----------
const svgChart = (c) => {
  const pts = points(c);
  const max = Math.max(1, ...pts.map((p) => p.y));
  const W = 840; const head = `<h3 style="margin:22px 0 2px;color:${COLORS.line};font-size:15px">${esc(c.title)}</h3>` +
    (c.why ? `<div style="color:${COLORS.mute};font-size:12px;margin-bottom:6px">${esc(c.why)}</div>` : '');
  if (c.chart === 'donut') {
    const live = pts.filter((p) => p.y > 0); const tot = live.reduce((s, p) => s + p.y, 0) || 1;
    const S = 170; const R = 80; const r = 48; const cx = S / 2; let a0 = -Math.PI / 2;
    const pt = (rad, ang) => `${(cx + rad * Math.cos(ang)).toFixed(2)},${(cx + rad * Math.sin(ang)).toFixed(2)}`;
    const paths = live.map((p, i) => {
      const a1 = a0 + Math.min(2 * Math.PI * 0.9999, (2 * Math.PI * p.y) / tot); const big = a1 - a0 > Math.PI ? 1 : 0;
      const d = `M ${pt(R, a0)} A ${R} ${R} 0 ${big} 1 ${pt(R, a1)} L ${pt(r, a1)} A ${r} ${r} 0 ${big} 0 ${pt(r, a0)} Z`; a0 = a1;
      return `<path d="${d}" fill="${PALETTE[i % PALETTE.length]}"><title>${esc(p.label)}: ${fmt(p.y, c.metric)}</title></path>`;
    }).join('');
    return head + `<table cellspacing="0" cellpadding="0"><tr><td><svg width="${S}" height="${S}" viewBox="0 0 ${S} ${S}">${paths}</svg></td><td style="padding-left:14px;font-size:12px;font-family:Segoe UI,Arial,sans-serif">` +
      live.map((p, i) => `<div style="margin:3px 0"><span style="display:inline-block;width:10px;height:10px;background:${PALETTE[i % PALETTE.length]}"></span> ${esc(p.label)} – <b>${fmt(p.y, c.metric)}</b> (${((100 * p.y) / tot).toFixed(0)}%)</div>`).join('') + '</td></tr></table>';
  }
  if (c.chart === 'bar') {
    const rowH = 24; const left = 200; const H = pts.length * rowH + 10;
    return head + `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" style="font-family:Segoe UI,Arial,sans-serif;font-size:12px">` +
      pts.map((p, i) => { const w = Math.max(2, ((W - left - 90) * p.y) / max); const y = i * rowH + 4;
        return `<text x="${left - 8}" y="${y + 14}" text-anchor="end" fill="${COLORS.ink}">${esc(p.label.slice(0, 28))}</text>` +
          `<rect x="${left}" y="${y + 2}" width="${w}" height="16" rx="2" fill="${COLORS.bar}"><title>${esc(p.label)}: ${fmt(p.y, c.metric)}</title></rect>` +
          `<text x="${left + w + 6}" y="${y + 14}" fill="${COLORS.mute}">${fmt(p.y, c.metric)}</text>`; }).join('') + '</svg>';
  }
  const H = 220; const top = 16; const bottom = 34; const plotH = H - top - bottom; const step = (W - 40) / pts.length;
  const x = (i) => 30 + step * i + step / 2; const y = (v) => top + plotH - (plotH * v) / max;
  const labels = pts.map((p, i) => `<text x="${x(i)}" y="${H - 14}" text-anchor="middle" fill="${COLORS.mute}" font-size="11">${esc(p.label.slice(0, 10))}</text>`).join('');
  const grid = `<line x1="20" y1="${top + plotH}" x2="${W - 10}" y2="${top + plotH}" stroke="${COLORS.grid}"/>`;
  const marks = c.chart === 'line'
    ? `<polyline fill="none" stroke="${COLORS.line}" stroke-width="2" points="${pts.map((p, i) => (p.part ? '' : `${x(i)},${y(p.y)}`)).join(' ')}"/>` +
      // the unfinished month is joined with a dashed, lighter line
      pts.map((p, i) => (p.part && i > 0 ? `<line x1="${x(i - 1)}" y1="${y(pts[i - 1].y)}" x2="${x(i)}" y2="${y(p.y)}" stroke="${COLORS.part}" stroke-width="2" stroke-dasharray="5 4"/>` : '')).join('') +
      pts.map((p, i) => `<circle cx="${x(i)}" cy="${y(p.y)}" r="3.5" fill="${p.part ? COLORS.part : COLORS.line}"><title>${esc(p.label)}: ${fmt(p.y, c.metric)}</title></circle>` +
        `<text x="${x(i)}" y="${y(p.y) - 7}" text-anchor="middle" fill="${COLORS.mute}" font-size="10">${fmt(p.y, c.metric)}</text>`).join('')
    : pts.map((p, i) => { const bw = Math.min(46, step * 0.7); const h = Math.max(1, top + plotH - y(p.y));
      return `<rect x="${x(i) - bw / 2}" y="${top + plotH - h}" width="${bw}" height="${h}" rx="2" fill="${p.part ? COLORS.part : COLORS.bar}"><title>${esc(p.label)}: ${fmt(p.y, c.metric)}</title></rect>` +
        `<text x="${x(i)}" y="${top + plotH - h - 4}" text-anchor="middle" fill="${COLORS.mute}" font-size="10">${fmt(p.y, c.metric)}</text>`; }).join('');
  return head + `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" style="font-family:Segoe UI,Arial,sans-serif">${grid}${marks}${labels}</svg>` + partNote(pts);
};

const note = aiUsed ? 'Highlights chosen by the AI chart designer; all figures come from the report data. The full set of charts is in each section below.' : 'Standard highlight charts. The full set of charts is in each section below.';
const emailBlock = charts.length
  ? `<div style="font-family:Segoe UI,Arial,sans-serif;max-width:860px;margin:0 0 18px;padding:6px 16px 12px;border:1px solid ${COLORS.grid}">` +
    `<div style="font-size:11px;color:${COLORS.mute};margin-top:6px">${note}</div>${charts.map(emailChart).join('')}</div>`
  : '';
const svgBlock = charts.length
  ? `<div style="font-family:Segoe UI,Arial,sans-serif;max-width:900px;margin-bottom:12px"><div style="font-size:11px;color:${COLORS.mute}">${note} These charts show the report period; use the filters below for the detailed sections.</div>${charts.map(svgChart).join('')}</div>`
  : '';

const html = String(base.json.html).replace('<!--charts-->', emailBlock);
const binary = { ...base.binary };
if (binary.dashboard?.data) {
  const page = Buffer.from(binary.dashboard.data, 'base64').toString('utf8').replace('<!--charts-->', svgBlock);
  binary.dashboard = { ...binary.dashboard, data: Buffer.from(page, 'utf8').toString('base64') };
}
return [{ json: { ...base.json, html, chartsUsed: charts.map((c) => `${c.dataset}/${c.metric}/${c.chart}`), aiCharts: aiUsed }, binary }];
