// Build Report — incoming volume, watchlist, company code & customer split, weekly/monthly trends,
// workload heatmap and forecast. Fixed rules only: the same data and choices always give the same report.
// The email shows the report; the attached dashboard.html lets you change period / company code / customer.
const RECIPIENTS = ['']; // put your email between the quotes, e.g. ['name.surname@company.com']
const RULES = {
  spike: 1.5, // flag when a customer's invoices are 50%+ above their usual (average of previous 3 periods)
  fall: 0.5, // flag when an active customer falls 50%+ below their usual
  share: 0.2, // flag when one customer is over 20% of the period's value
  slowDays: 3, // flag when average Received → Allocated takes more than 3 days
  minInvoices: 3, // ignore customers with fewer invoices than this for spike / fall / turnaround / portal flags
};

// ---------- shared helpers (also embedded in the dashboard) ----------
function analyse(all, opts, RULES) {
  const DAY = 86400000;
  const ms = (d) => Date.UTC(+d.slice(0, 4), +d.slice(5, 7) - 1, +d.slice(8, 10));
  const iso = (t) => new Date(t).toISOString().slice(0, 10);
  const addDays = (d, n) => iso(ms(d) + n * DAY);
  const weekStart = (d) => addDays(d, -((new Date(ms(d)).getUTCDay() + 6) % 7)); // Monday
  const monthStart = (d) => d.slice(0, 8) + '01';
  const monthEnd = (d) => iso(Date.UTC(+d.slice(0, 4), +d.slice(5, 7), 0));
  const addMonths = (d, n) => iso(Date.UTC(+d.slice(0, 4), +d.slice(5, 7) - 1 + n, 1));
  const num = (v) => { const n = parseFloat(String(v ?? '').replace(/[^0-9.\-]/g, '')); return Number.isFinite(n) ? n : 0; };
  const sum = (a, f) => a.reduce((s, r) => s + f(r), 0);

  const dates = all.map((r) => r.d).filter(Boolean).sort();
  if (!dates.length) return { empty: true };
  const first = dates[0];
  const latest = dates[dates.length - 1];

  // ----- period -----
  let from, to, label;
  const type = opts.type || 'Overview';
  if (type === 'Weekly') { from = weekStart(latest); to = addDays(from, 6); label = `Week of ${from}`; }
  else if (type === 'Custom period') {
    from = opts.from || first; to = opts.to || latest; label = `${from} to ${to}`;
  } else { from = monthStart(latest); to = monthEnd(latest); label = type === 'Monthly' ? from.slice(0, 7) : `${from.slice(0, 7)} (month to date)`; }
  if (to < from) [from, to] = [to, from];
  const len = Math.round((ms(to) - ms(from)) / DAY) + 1;
  const shift = (k) => type === 'Weekly' || type === 'Custom period'
    ? [addDays(from, -len * k), addDays(from, -len * (k - 1) - 1)]
    : [addMonths(from, -k), monthEnd(addMonths(from, -k))];

  const cc = String(opts.companyCode || '').trim().toUpperCase();
  const cust = String(opts.customer || '').trim().toUpperCase();
  const pcSel = String(opts.profitCentre || '').trim().toUpperCase();
  const plSel = String(opts.productLine || '').trim().toUpperCase();
  const pcKey = (r) => r.pc || (r.cc === 'G367' ? 'N/A (G367)' : 'NOT FOUND');
  const plKey = (r) => r.pl || 'NOT FOUND';
  const scoped = all.filter((r) => r.d && (!cc || r.cc === cc) && (!cust || r.c.includes(cust))
    && (!pcSel || pcKey(r) === pcSel) && (!plSel || plKey(r) === plSel));
  const inRange = (a, b) => scoped.filter((r) => r.d >= a && r.d <= b);
  const cur = inRange(from, to);
  const [pf, pt] = shift(1);
  const prev = inRange(pf, pt);
  // baseline = previous 3 periods, but only those fully covered by data (so the start of the data isn't a fake "spike")
  const base = [1, 2, 3].map((k) => shift(k)).filter(([a]) => a >= first).map(([a, b]) => inRange(a, b));

  const tat = (r) => (r.rd && r.ad ? Math.max(0, Math.round((ms(r.ad) - ms(r.rd)) / DAY)) : null);
  const avgTat = (rows) => { const t = rows.map(tat).filter((x) => x !== null); return t.length ? sum(t, (x) => x) / t.length : null; };
  const channel = (r) => (!r.p ? 'Not recorded' : r.p.includes('@') ? 'Email' : `Portal: ${r.p.split(/[,;]/)[0].trim()}`);
  const groupBy = (rows, key) => {
    const m = new Map();
    for (const r of rows) { const k = key(r); if (!k) continue; const g = m.get(k) || { key: k, n: 0, v: 0, rows: [] }; g.n++; g.v += num(r.v); g.rows.push(r); m.set(k, g); }
    return [...m.values()];
  };
  const byValue = (a, b) => b.v - a.v || String(a.key).localeCompare(String(b.key));
  const change = (now, before) => (before ? (now - before) / before : null);

  const total = { n: cur.length, v: sum(cur, (r) => num(r.v)) };
  const prevTotal = { n: prev.length, v: sum(prev, (r) => num(r.v)) };

  // ----- watchlist -----
  const firstSeen = new Map();
  for (const r of all) if (r.d && (!firstSeen.has(r.c) || r.d < firstSeen.get(r.c))) firstSeen.set(r.c, r.d);
  const watch = [];
  for (const g of groupBy(cur, (r) => r.c).sort(byValue)) {
    const usual = base.length ? sum(base, (rows) => rows.filter((r) => r.c === g.key).length) / base.length : 0;
    const reasons = [];
    if (firstSeen.get(g.key) >= from) reasons.push(['New customer', `first invoice ${firstSeen.get(g.key)}`]);
    else if (g.n >= RULES.minInvoices && usual > 0 && g.n >= usual * RULES.spike) reasons.push(['Volume spike', `${g.n} invoices vs usual ${usual.toFixed(1)}`]);
    if (total.v && g.v / total.v > RULES.share) reasons.push(['High value share', `${(100 * g.v / total.v).toFixed(1)}% of value`]);
    const t = avgTat(g.rows);
    if (g.n >= RULES.minInvoices && t !== null && t > RULES.slowDays) reasons.push(['Slow turnaround', `${t.toFixed(1)} days received → allocated`]);
    const portal = g.rows.filter((r) => channel(r).startsWith('Portal'));
    if (portal.length >= RULES.minInvoices) reasons.push(['Portal submissions', `${portal.length} via ${channel(portal[0]).slice(8)}`]);
    const missing = g.rows.filter((r) => !num(r.v)).length;
    if (missing) reasons.push(['Data issue', `${missing} without a value`]);
    if (reasons.length) watch.push({ customer: g.key, n: g.n, v: g.v, reasons });
  }
  const curCustomers = new Set(cur.map((r) => r.c));
  const usualAll = new Map();
  for (const rows of base) for (const r of rows) usualAll.set(r.c, (usualAll.get(r.c) || 0) + 1 / base.length);
  for (const [c, usual] of [...usualAll].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))) {
    const n = cur.filter((r) => r.c === c).length;
    if (usual >= RULES.minInvoices && n <= usual * RULES.fall) {
      const item = { customer: c, n, v: sum(cur.filter((r) => r.c === c), (r) => num(r.v)), reasons: [[n ? 'Sharp fall' : 'Gone quiet', `${n} invoices vs usual ${usual.toFixed(1)}`]] };
      if (curCustomers.has(c)) { const w = watch.find((x) => x.customer === c); if (w) w.reasons.push(item.reasons[0]); else watch.push(item); } else watch.push(item);
    }
  }

  // ----- trends -----
  const monthsBack = [];
  for (let k = 11; k >= 0; k--) monthsBack.push(addMonths(monthStart(to), -k));
  const monthly = monthsBack.map((m) => { const rows = scoped.filter((r) => r.d >= m && r.d <= monthEnd(m)); return { key: m.slice(0, 7), n: rows.length, v: sum(rows, (r) => num(r.v)) }; })
    .filter((m, i, a) => m.n || a.slice(0, i).some((x) => x.n));
  const weeksBack = [];
  for (let k = 7; k >= 0; k--) weeksBack.push(addDays(weekStart(to), -7 * k));
  const weekly = weeksBack.map((w) => { const rows = scoped.filter((r) => r.d >= w && r.d <= addDays(w, 6)); return { key: w, n: rows.length, v: sum(rows, (r) => num(r.v)) }; });
  const heat = monthsBack.slice(-6).map((m) => {
    const cells = Array.from({ length: 31 }, (_, i) => scoped.filter((r) => r.d.slice(0, 7) === m.slice(0, 7) && +r.d.slice(8, 10) === i + 1).length);
    return { key: m.slice(0, 7), cells };
  });
  const wd = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
  const last12w = scoped.filter((r) => r.d > addDays(to, -84) && r.d <= to);
  const weekday = wd.map((name, i) => ({ key: name, n: last12w.filter((r) => (new Date(ms(r.d)).getUTCDay() + 6) % 7 === i).length / 12 }));

  // ----- forecast (averages of recent complete periods; range = lowest–highest of those periods) -----
  const doneWeeks = [];
  for (let k = 8; k >= 1; k--) { const w = addDays(weekStart(latest), -7 * k); const rows = scoped.filter((r) => r.d >= w && r.d <= addDays(w, 6)); doneWeeks.push({ n: rows.length, v: sum(rows, (r) => num(r.v)) }); }
  const doneMonths = [];
  for (let k = 3; k >= 1; k--) { const m = addMonths(monthStart(latest), -k); const rows = scoped.filter((r) => r.d >= m && r.d <= monthEnd(m)); doneMonths.push({ n: rows.length, v: sum(rows, (r) => num(r.v)) }); }
  const stat = (a, f) => ({ avg: a.length ? sum(a, f) / a.length : 0, lo: a.length ? Math.min(...a.map(f)) : 0, hi: a.length ? Math.max(...a.map(f)) : 0 });
  const forecast = {
    weekN: stat(doneWeeks, (x) => x.n), weekV: stat(doneWeeks, (x) => x.v),
    monthN: stat(doneMonths, (x) => x.n), monthV: stat(doneMonths, (x) => x.v),
    nextWeeks: [1, 2, 3, 4].map((k) => addDays(weekStart(latest), 7 * k)),
    nextMonth: addMonths(monthStart(latest), 1).slice(0, 7),
  };

  // ----- splits -----
  const companies = groupBy(cur, (r) => r.cc || 'UNKNOWN').sort(byValue).map((g) => ({
    key: g.key, n: g.n, v: g.v, prevN: prev.filter((r) => (r.cc || 'UNKNOWN') === g.key).length,
    top: groupBy(g.rows, (r) => r.c).sort(byValue).slice(0, 5),
  }));
  const split = (keyOf) => groupBy(cur, keyOf).sort(byValue).map((g) => ({
    key: g.key, n: g.n, v: g.v, prevN: prev.filter((r) => keyOf(r) === g.key).length, tat: avgTat(g.rows),
    top: groupBy(g.rows, (r) => r.c).sort(byValue).slice(0, 5),
  }));
  const profitCentres = split(pcKey);
  const productLines = split(plKey);
  const businessTypes = split((r) => r.bt || 'NOT FOUND');
  // ----- breakdown tree: entity → company code → sales org → (profit centre, business type, product line) -----
  const ENTITY = { '3060': 'LA PRAIRIE (CANADA)', '3487': 'LA PRAIRIE (CANADA)', '3485': 'CHARLEROI', G367: 'CLEARWATER' };
  const LEVEL = {
    entity: { name: 'Entity', of: (r) => ENTITY[r.cc] || (r.cc ? 'OTHER' : '') },
    cc: { name: 'Company code', of: (r) => r.cc || '' },
    so: { name: 'Sales org', of: (r) => r.so || '' },
    pc: { name: 'Profit centre', of: (r) => r.pc || '' },
    bt: { name: 'Business type', of: (r) => r.bt || '' },
    pl: { name: 'Product line', of: (r) => r.pl || '' },
  };
  // values of `child` that appear under more than one value of `parent` (checked on all data, not just this period)
  const clashes = (parent, child) => {
    const m = new Map();
    for (const r of scoped) {
      const c = LEVEL[child].of(r); const pv = LEVEL[parent].of(r);
      if (!c || !pv) continue;
      if (!m.has(c)) m.set(c, new Set());
      m.get(c).add(pv);
    }
    return [...m].filter(([, set]) => set.size > 1).map(([c]) => c).sort();
  };
  // order of the lower three levels: the one with the fewest clashes; ties keep the expected order (first in the list)
  const ORDERS = [['pc', 'bt', 'pl'], ['pc', 'pl', 'bt'], ['bt', 'pc', 'pl'], ['bt', 'pl', 'pc'], ['pl', 'pc', 'bt'], ['pl', 'bt', 'pc']];
  const scored = ORDERS.map((o, i) => ({ o, i, n: clashes('cc', o[0]).length + clashes(o[0], o[1]).length + clashes(o[1], o[2]).length }));
  const lower = scored.sort((x, y) => x.n - y.n || x.i - y.i)[0].o;
  const levels = ['entity', 'cc', 'so', ...lower];
  const structure = {
    order: levels.map((k) => LEVEL[k].name),
    // sales org only exists for G367, so the lower levels are checked against the company code
    exceptions: [['entity', 'cc'], ['cc', 'so'], ['cc', lower[0]], [lower[0], lower[1]], [lower[1], lower[2]]]
      .map(([pk, ck]) => ({ parent: LEVEL[pk].name, child: LEVEL[ck].name, values: clashes(pk, ck) }))
      .filter((e) => e.values.length),
  };
  // only overlaps at the top (e.g. one profit centre under two company codes) are data problems;
  // lower down, e.g. "Manufacturing" under several profit centres, is normal and simply repeats under each parent
  structure.problems = structure.exceptions.filter((e) => ['Entity', 'Company code', 'Sales org'].includes(e.parent));
  const MAX_CHILDREN = 8;
  const buildTree = (curRows, prevRows, depth) => {
    if (depth >= levels.length || !curRows.length) return [];
    const lv = LEVEL[levels[depth]];
    // an empty value (e.g. no sales org, no profit centre for G367) skips the level instead of adding a blank row
    if (curRows.every((r) => !lv.of(r))) return buildTree(curRows, prevRows, depth + 1);
    const nodes = groupBy(curRows, (r) => lv.of(r) || '(not set)').sort(byValue).map((g) => {
      const pr = prevRows.filter((r) => (lv.of(r) || '(not set)') === g.key);
      let node = { label: g.key, level: lv.name, n: g.n, v: g.v, prevN: pr.length, tat: avgTat(g.rows), children: buildTree(g.rows, pr, depth + 1) };
      // one child with the same invoices = the same thing again: show it on the same line
      while (node.children.length === 1 && node.children[0].n === node.n) {
        const c = node.children[0];
        node = { ...node, label: `${node.label} › ${c.label}`, level: `${node.level} › ${c.level}`, children: c.children, more: c.more };
      }
      return node;
    });
    const shown = nodes.slice(0, MAX_CHILDREN);
    if (nodes.length > MAX_CHILDREN) {
      const rest = nodes.slice(MAX_CHILDREN);
      shown.push({ label: `+ ${rest.length} more`, level: lv.name, n: sum(rest, (x) => x.n), v: sum(rest, (x) => x.v), prevN: null, tat: null, children: [] });
    }
    return shown;
  };
  const tree = buildTree(cur, prev, 0);
  const mostCommon = (rows, f) => groupBy(rows, f).sort((a, b) => b.n - a.n || String(a.key).localeCompare(String(b.key)))[0]?.key || '';
  const customers = groupBy(cur, (r) => r.c).sort(byValue).slice(0, 15).map((g) => ({
    key: g.key, n: g.n, v: g.v, tat: avgTat(g.rows), prevN: prev.filter((r) => r.c === g.key).length,
    pc: mostCommon(g.rows, (r) => r.pc), pl: mostCommon(g.rows, (r) => r.pl), sap: mostCommon(g.rows, (r) => r.sap),
    trend: monthsBack.slice(-6).map((m) => scoped.filter((r) => r.c === g.key && r.d.slice(0, 7) === m.slice(0, 7)).length),
  }));
  const channels = groupBy(cur, channel).sort((a, b) => b.n - a.n);
  const managers = groupBy(cur, (r) => r.pm || 'Not recorded').sort((a, b) => b.n - a.n);
  const quality = {
    noValue: cur.filter((r) => !num(r.v)).length,
    repeated: groupBy(cur, (r) => String(r.i)).filter((g) => g.n > 1).map((g) => g.key),
    allocatedBeforeReceived: cur.filter((r) => r.rd && r.ad && r.ad < r.rd).length,
  };

  return {
    label, type, from, to, first, latest, cc, cust, pcSel, plSel, profitCentres, productLines, businessTypes, tree, structure, total, prevTotal, avgTat: avgTat(cur), baseN: base.length,
    nChange: change(total.n, prevTotal.n), vChange: change(total.v, prevTotal.v),
    watch, monthly, weekly, heat, weekday, forecast, companies, customers, channels, managers, quality,
  };
}

function render(a) {
  if (a.empty) return '<p>No data for this selection.</p>';
  const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const money = (n) => n.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const int = (n) => Math.round(n).toLocaleString('en-US');
  const pct = (x) => (x === null || x === undefined ? '–' : `${x >= 0 ? '▲' : '▼'} ${Math.abs(100 * x).toFixed(1)}%`);
  const share = (p, w) => (w ? `${(100 * p / w).toFixed(1)}%` : '–');
  const C = { ink: '#111827', mute: '#6b7280', line: '#e5e7eb', head: '#1f3a5f', bar: '#2b6cb0', warn: '#b45309', bad: '#b91c1c', good: '#047857' };
  const th = (t, right) => `<th style="text-align:${right ? 'right' : 'left'};padding:6px 10px;background:${C.head};color:#fff;font-weight:600;font-size:12px">${esc(t)}</th>`;
  const td = (t, right, color) => `<td style="padding:5px 10px;border-bottom:1px solid ${C.line};font-size:12px;${right ? 'text-align:right;' : ''}${color ? `color:${color};` : ''}">${t}</td>`;
  const bar = (part, whole, color = C.bar) => `<table cellpadding="0" cellspacing="0" width="${Math.max(2, Math.round(100 * part / (whole || 1)))}%"><tr><td bgcolor="${color}" height="10" style="font-size:0;line-height:0">&nbsp;</td></tr></table>`;
  const table = (heads, rows) => `<table cellspacing="0" cellpadding="0" style="border-collapse:collapse;width:100%;max-width:860px">` +
    `<tr>${heads.map((h, i) => th(h, i > 0 && h !== '')).join('')}</tr>${rows.join('') || `<tr>${td('No data')}</tr>`}</table>`;
  const h = (t, sub) => `<h3 style="margin:26px 0 4px;color:${C.head};font-size:16px">${esc(t)}</h3>${sub ? `<div style="color:${C.mute};font-size:12px;margin-bottom:8px">${esc(sub)}</div>` : ''}`;
  const kpi = (label, value, note) => `<td style="padding:10px 16px;border:1px solid ${C.line};vertical-align:top"><div style="font-size:11px;color:${C.mute}">${esc(label)}</div>` +
    `<div style="font-size:20px;font-weight:700;color:${C.ink}">${esc(value)}</div><div style="font-size:11px;color:${C.mute}">${esc(note || '')}</div></td>`;
  const changeColor = (x) => (x === null ? C.mute : x >= 0 ? C.good : C.bad);
  const flagColor = { 'Volume spike': C.warn, 'Sharp fall': C.bad, 'Gone quiet': C.bad, 'New customer': C.bar, 'High value share': C.warn, 'Slow turnaround': C.bad, 'Portal submissions': C.head, 'Data issue': C.bad };

  const maxM = Math.max(1, ...a.monthly.map((m) => m.n));
  const maxW = Math.max(1, ...a.weekly.map((w) => w.n));
  const maxH = Math.max(1, ...a.heat.flatMap((r) => r.cells));
  const hex2 = (x) => Math.round(x).toString(16).padStart(2, '0');
  const shade = (n) => { if (!n) return '#f9fafb'; const t = n / maxH; const mix = (x, y) => x + (y - x) * t; return `#${hex2(mix(219, 30))}${hex2(mix(234, 64))}${hex2(mix(254, 175))}`; };
  const maxWd = Math.max(1, ...a.weekday.map((w) => w.n));
  const f = a.forecast;
  const scope = [a.cc && `company code ${a.cc}`, a.pcSel && `profit centre ${a.pcSel}`, a.plSel && `product line ${a.plSel}`,
    a.cust && `customer contains "${a.cust}"`].filter(Boolean).join(', ') || 'all company codes, profit centres, product lines and customers';
  const treeRows = (nodes, depth) => nodes.flatMap((nd) => {
    const ch = nd.prevN ? (nd.n - nd.prevN) / nd.prevN : null;
    const name = depth === 0 ? `<b>${esc(nd.label)}</b>` : `<span style="color:${depth > 1 ? C.mute : C.ink}">${'&nbsp;'.repeat(depth * 4)}↳ ${esc(nd.label)}</span>`;
    const row = `<tr>${td(name)}${td(`<span style="color:${C.mute};font-size:11px">${esc(nd.level)}</span>`)}${td(int(nd.n), 1)}${td(money(nd.v), 1)}${td(share(nd.v, a.total.v), 1)}` +
      `${td(nd.prevN === null ? '' : pct(ch), 1, changeColor(ch))}${td(nd.tat === null ? '–' : nd.tat.toFixed(1), 1)}</tr>`;
    return [row, ...treeRows(nd.children, depth + 1)];
  });

  return `<div style="font-family:Segoe UI,Arial,sans-serif;color:${C.ink};max-width:900px">
<h2 style="margin:0;color:${C.head}">Production Tracker – ${esc(a.type)} report</h2>
<div style="color:${C.mute};font-size:12px">${esc(a.label)} · ${esc(a.from)} to ${esc(a.to)} · ${esc(scope)} · data from ${esc(a.first)} to ${esc(a.latest)}</div>
<table cellspacing="0" style="border-collapse:collapse;margin:14px 0"><tr>
${kpi('Incoming invoices', int(a.total.n), `${pct(a.nChange)} vs previous period`)}${kpi('Value', money(a.total.v), `${pct(a.vChange)} vs previous period`)}
${kpi('Avg received → allocated', a.avgTat === null ? '–' : `${a.avgTat.toFixed(1)} days`, '')}${kpi('Next week (forecast)', int(f.weekN.avg), `range ${int(f.weekN.lo)}–${int(f.weekN.hi)}`)}
</tr></table>
${h(`Customers to look out for (${a.watch.length})`, `Fixed rules: spike / fall vs the previous ${a.baseN} period(s) with full data, value share, turnaround, portal use, data issues`)}
${table(['Customer', 'Invoices', 'Value', 'Why'], a.watch.slice(0, 20).map((w) => `<tr>${td(esc(w.customer))}${td(int(w.n), 1)}${td(money(w.v), 1)}${td(w.reasons.map(([k, d]) => `<b style="color:${flagColor[k] || C.ink}">${esc(k)}</b> – ${esc(d)}`).join('<br>'))}</tr>`))}
${h('Incoming volume by month', 'Invoices received per month, with change from the month before')}
${table(['Month', 'Invoices', 'Value', 'Change', ''], a.monthly.map((m, i) => { const c = i ? (a.monthly[i - 1].n ? (m.n - a.monthly[i - 1].n) / a.monthly[i - 1].n : null) : null; return `<tr>${td(m.key)}${td(int(m.n), 1)}${td(money(m.v), 1)}${td(pct(c), 1, changeColor(c))}<td style="padding:5px 10px;border-bottom:1px solid ${C.line};width:35%">${bar(m.n, maxM)}</td></tr>`; }))}
${h('Weekly details (last 8 weeks)', 'Weeks start on Monday')}
${table(['Week starting', 'Invoices', 'Value', ''], a.weekly.map((w) => `<tr>${td(w.key)}${td(int(w.n), 1)}${td(money(w.v), 1)}<td style="padding:5px 10px;border-bottom:1px solid ${C.line};width:40%">${bar(w.n, maxW)}</td></tr>`))}
${h('Workload heatmap – day of month', 'Darker = more invoices received that day (last 6 months)')}
<table cellspacing="1" cellpadding="0" style="font-size:10px"><tr><td style="padding:2px 6px"></td>${Array.from({ length: 31 }, (_, i) => `<td style="text-align:center;color:${C.mute};width:20px">${i + 1}</td>`).join('')}</tr>
${a.heat.map((r) => `<tr><td style="padding:2px 6px;color:${C.mute};white-space:nowrap">${r.key}</td>${r.cells.map((n) => `<td bgcolor="${shade(n)}" style="text-align:center;height:20px;color:${n / maxH > 0.55 ? '#fff' : C.ink}">${n || ''}</td>`).join('')}</tr>`).join('')}</table>
${h('Busiest weekdays', 'Average invoices received per weekday (last 12 weeks)')}
${table(['Weekday', 'Avg invoices', ''], a.weekday.map((w) => `<tr>${td(w.key)}${td(w.n.toFixed(1), 1)}<td style="padding:5px 10px;border-bottom:1px solid ${C.line};width:50%">${bar(w.n, maxWd)}</td></tr>`))}
${h('Forecast', 'Average of recent complete periods; range = lowest–highest of those periods')}
${table(['Period', 'Expected invoices', 'Range', 'Expected value'], [
    ...f.nextWeeks.map((w) => `<tr>${td(`Week of ${w}`)}${td(int(f.weekN.avg), 1)}${td(`${int(f.weekN.lo)}–${int(f.weekN.hi)}`, 1)}${td(money(f.weekV.avg), 1)}</tr>`),
    `<tr>${td(`<b>${f.nextMonth}</b>`)}${td(`<b>${int(f.monthN.avg)}</b>`, 1)}${td(`${int(f.monthN.lo)}–${int(f.monthN.hi)}`, 1)}${td(`<b>${money(f.monthV.avg)}</b>`, 1)}</tr>`])}
${h('Breakdown: ' + a.structure.order.join(' → '), 'One line per group; a level is skipped where it does not apply (e.g. no profit centre for G367), and repeated single groups are shown on one line')}
${table(['Group', 'Level', 'Invoices', 'Value', 'Share', 'vs previous', 'Avg days'], treeRows(a.tree, 0))}
${a.structure.problems.length ? `<div style="font-size:11px;color:${C.warn};margin-top:4px">Check the data: ${a.structure.problems.map((e) =>
    `${e.values.length} ${esc(e.child.toLowerCase())}(s) appear under more than one ${esc(e.parent.toLowerCase())} (${esc(e.values.slice(0, 5).join(', '))}${e.values.length > 5 ? ' …' : ''})`).join('; ')}</div>` : ''}
${h('Customer details (top 15 by value)', 'Trend = invoices per month, last 6 months')}
${table(['Customer', 'SAP code', 'Profit centre', 'Product line', 'Invoices', 'Value', 'Share', 'Avg days', 'Trend'], a.customers.map((c) => `<tr>${td(esc(c.key))}${td(esc(c.sap || '–'))}${td(esc(c.pc || '–'))}${td(esc(c.pl || '–'))}${td(int(c.n), 1)}${td(money(c.v), 1)}${td(share(c.v, a.total.v), 1)}${td(c.tat === null ? '–' : c.tat.toFixed(1), 1)}${td(c.trend.join(' · '), 1)}</tr>`))}
${h('Channels & project managers')}
${table(['Channel', 'Invoices', 'Share'], a.channels.map((c) => `<tr>${td(esc(c.key))}${td(int(c.n), 1)}${td(share(c.n, a.total.n), 1)}</tr>`))}
<div style="height:10px"></div>
${table(['Project manager', 'Invoices', 'Value'], a.managers.map((m) => `<tr>${td(esc(m.key))}${td(int(m.n), 1)}${td(money(m.v), 1)}</tr>`))}
${h('Data quality')}
<ul style="font-size:12px;margin:0;padding-left:18px">
<li>${int(a.quality.noValue)} invoices without a value</li>
<li>${int(a.quality.allocatedBeforeReceived)} allocated before received</li>
<li>${a.quality.repeated.length ? `${a.quality.repeated.length} invoice numbers appear more than once: ${esc(a.quality.repeated.slice(0, 10).join(', '))}${a.quality.repeated.length > 10 ? ' …' : ''}` : 'No repeated invoice numbers'}</li></ul>
<p style="color:#9ca3af;font-size:11px;margin-top:22px">Generated by n8n from the Production Tracker data table. Workload date = Received_Date (falls back to Allocated, then Invoice date).</p>
</div>`;
}

// ---------- main ----------
const settings = $('Report Settings').first().json;
const seen = new Map(); // one row per invoice (last row wins)
for (const { json: r } of $('Get All Rows').all()) {
  const d = r.Received_Date || r.Allocated_Date || r.Invoice_Date || '';
  seen.set(String(r.Invoice ?? r.id), {
    i: r.Invoice, d: String(d).slice(0, 10), rd: String(r.Received_Date || '').slice(0, 10), ad: String(r.Allocated_Date || '').slice(0, 10),
    c: String(r.Customer || 'UNKNOWN CUSTOMER').trim().toUpperCase(), cc: String(r.Company_Code || '').trim().toUpperCase(),
    pm: String(r.Project_Manager || '').trim(), p: String(r.Name_the_PortalEmail_ID || '').trim(), v: r.Value,
    sap: String(r.SAP_Customer_Code || '').trim(), pc: String(r.Profit_Center || '').trim().toUpperCase(),
    so: String(r.Sales_Org || '').trim().toUpperCase(),
    pl: String(r.Product_Line || '').trim().toUpperCase(), bt: String(r.Business_Type || '').trim().toUpperCase(),
  });
}
const rows = [...seen.values()];
const a = analyse(rows, settings, RULES);
const html = render(a);

const recipients = String(settings.sendTo || '').trim() || RECIPIENTS.filter((x) => String(x).trim()).join(', ');
if (!recipients) throw new Error('Add at least one email address to RECIPIENTS at the top of "Build Report".');

const safeJson = (x) => JSON.stringify(x).replace(/</g, '\\u003c');
const companyCodes = [...new Set(rows.map((r) => r.cc).filter(Boolean))].sort();
const listOf = (f) => [...new Set(rows.map(f))].sort();
const options = (list) => list.map((c) => `<option>${String(c).replace(/[&<>"]/g, '')}</option>`).join('');
const profitCentreList = listOf((r) => r.pc || (r.cc === 'G367' ? 'N/A (G367)' : 'NOT FOUND'));
const productLineList = listOf((r) => r.pl || 'NOT FOUND');
const dashboard = `<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Production Tracker Dashboard</title></head><body style="margin:0;padding:18px;background:#fff">
<!--charts-->
<div style="font-family:Segoe UI,Arial,sans-serif;font-size:13px;background:#f3f4f6;padding:12px;border-radius:6px;margin-bottom:12px;max-width:900px">
<b>Choose:</b> Report <select id="t"><option>Overview</option><option>Weekly</option><option>Monthly</option><option>Custom period</option></select>
From <input id="f" type="date"> To <input id="o" type="date">
Company code <select id="cc"><option value="">All</option>${companyCodes.map((c) => `<option>${c}</option>`).join('')}</select>
Profit centre <select id="pc"><option value="">All</option>${options(profitCentreList)}</select>
Product line <select id="pl"><option value="">All</option>${options(productLineList)}</select>
Customer contains <input id="cu" size="18"> <button id="go">Show</button></div>
<div id="out"></div>
<script>
const ROWS = ${safeJson(rows)};
const RULES = ${safeJson(RULES)};
${analyse.toString()}
${render.toString()}
const $id = (x) => document.getElementById(x);
function show() {
  const opts = { type: $id('t').value, from: $id('f').value, to: $id('o').value, companyCode: $id('cc').value, customer: $id('cu').value, profitCentre: $id('pc').value, productLine: $id('pl').value };
  if ((opts.from || opts.to) && opts.type !== 'Custom period') { opts.type = 'Custom period'; $id('t').value = opts.type; }
  $id('out').innerHTML = render(analyse(ROWS, opts, RULES));
}
const start = ${safeJson({ type: settings.type || 'Overview', from: settings.from || '', to: settings.to || '', companyCode: settings.companyCode || '', customer: settings.customer || '' })};
$id('t').value = start.type; $id('f').value = start.from; $id('o').value = start.to; $id('cc').value = start.companyCode.toUpperCase(); $id('cu').value = start.customer;
$id('go').onclick = show; show();
</script></body></html>`;

const quality = (() => { try { return $('Summarise Upload').first().json.message; } catch (e) { return ''; } })();

// Compact facts for the AI commentary step (the AI may only use these figures)
const r2 = (x) => Math.round(x * 100) / 100;
const p1 = (x) => (x === null || x === undefined ? null : Math.round(x * 1000) / 10);
const facts = a.empty ? { empty: true } : {
  report: a.type, period: `${a.from} to ${a.to}`, scope: { companyCode: a.cc || 'all', profitCentre: a.pcSel || 'all', productLine: a.plSel || 'all', customer: a.cust || 'all' },
  invoices: a.total.n, value: r2(a.total.v),
  previousPeriod: { invoices: a.prevTotal.n, value: r2(a.prevTotal.v) },
  changePercent: { invoices: p1(a.nChange), value: p1(a.vChange) },
  avgDaysReceivedToAllocated: a.avgTat === null ? null : r2(a.avgTat),
  watchlist: a.watch.slice(0, 10).map((w) => ({ customer: w.customer, invoices: w.n, value: r2(w.v), flags: w.reasons.map(([k, d]) => `${k}: ${d}`) })),
  monthly: a.monthly.slice(-6).map((m) => ({ month: m.key, invoices: m.n, value: r2(m.v),
    ...(m.key === a.latest.slice(0, 7) && a.latest.slice(8, 10) !== String(new Date(Date.UTC(+m.key.slice(0, 4), +m.key.slice(5, 7), 0)).getUTCDate())
      ? { monthToDate: true } : {}) })),
  weekly: a.weekly.map((w) => ({ weekStarting: w.key, invoices: w.n, value: r2(w.v) })),
  busiestDaysOfMonth: Array.from({ length: 31 }, (_, d) => ({ day: d + 1, avgInvoices: r2(a.heat.reduce((s, m) => s + m.cells[d], 0) / Math.max(1, a.heat.length)) }))
    .sort((x, y) => y.avgInvoices - x.avgInvoices || x.day - y.day).slice(0, 5),
  busiestWeekdays: [...a.weekday].sort((x, y) => y.n - x.n).slice(0, 3).map((w) => ({ weekday: w.key, avgInvoices: r2(w.n) })),
  forecast: {
    nextWeekInvoices: { expected: Math.round(a.forecast.weekN.avg), low: a.forecast.weekN.lo, high: a.forecast.weekN.hi },
    nextMonth: { month: a.forecast.nextMonth, expectedInvoices: Math.round(a.forecast.monthN.avg), low: a.forecast.monthN.lo, high: a.forecast.monthN.hi, expectedValue: r2(a.forecast.monthV.avg) },
  },
  companyCodes: a.companies.map((c) => ({ code: c.key, invoices: c.n, value: r2(c.v), valueSharePercent: a.total.v ? p1(c.v / a.total.v) : null, previousPeriodInvoices: c.prevN, topCustomers: c.top.slice(0, 3).map((t) => t.key) })),
  structure: { order: a.structure.order, exceptions: a.structure.exceptions.map((e) => `${e.values.length} ${e.child} values under more than one ${e.parent}`) },
  breakdown: (function flat(nodes, depth, path) { return nodes.flatMap((nd) => [{ group: [...path, nd.label].join(' / '), level: nd.level, invoices: nd.n, value: r2(nd.v), previousPeriodInvoices: nd.prevN },
    ...(depth < 2 ? flat(nd.children, depth + 1, [...path, nd.label]) : [])]); })(a.tree, 0, []).slice(0, 40),
  profitCentres: a.profitCentres.slice(0, 12).map((c) => ({ profitCentre: c.key, invoices: c.n, value: r2(c.v), valueSharePercent: a.total.v ? p1(c.v / a.total.v) : null, previousPeriodInvoices: c.prevN, avgDays: c.tat === null ? null : r2(c.tat), topCustomers: c.top.slice(0, 3).map((t) => t.key) })),
  productLines: a.productLines.map((c) => ({ productLine: c.key, invoices: c.n, value: r2(c.v), previousPeriodInvoices: c.prevN })),
  businessTypes: a.businessTypes.map((c) => ({ businessType: c.key, invoices: c.n, value: r2(c.v), previousPeriodInvoices: c.prevN })),
  topCustomers: a.customers.slice(0, 8).map((c) => ({ customer: c.key, sapCode: c.sap || null, profitCentre: c.pc || null, invoices: c.n, value: r2(c.v), avgDays: c.tat === null ? null : r2(c.tat), invoicesLast6Months: c.trend })),
  channels: a.channels.map((c) => ({ channel: c.key, invoices: c.n })),
  dataQuality: { withoutValue: a.quality.noValue, allocatedBeforeReceived: a.quality.allocatedBeforeReceived, repeatedInvoiceNumbers: a.quality.repeated.length },
};
const uploadNote = quality
  ? `<p style="font-family:Segoe UI,Arial,sans-serif;font-size:12px;color:#374151;background:#f3f4f6;padding:8px 12px;max-width:860px"><b>Upload result:</b> ${quality.replace(/[&<>]/g, '')}</p>`
  : '';
const subject = `Production Tracker ${a.type || ''} report – ${a.label || ''} – ${Math.round(a.total?.n ?? 0)} invoices, ${a.watch?.length ?? 0} customers to watch`;
return [{
  json: {
    to: recipients,
    subject,
    facts: JSON.stringify(facts),
    html: '<!--charts-->' + uploadNote + html + '<p style="font-family:Segoe UI,Arial,sans-serif;font-size:12px;color:#6b7280">The attached dashboard.html lets you change the period, company code, profit centre, product line and customer. Open it in your browser.</p>',
    doneMessage: (quality ? quality + '. ' : '') + `Report "${a.label || ''}" sent to ${recipients}.`,
  },
  binary: {
    dashboard: { data: Buffer.from(dashboard, 'utf8').toString('base64'), mimeType: 'text/html', fileName: 'dashboard.html', fileExtension: 'html' },
  },
}];
