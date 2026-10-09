// Build Report — invoice distribution report: volume (scope of work), 24-hour TAT, pending invoices and root causes,
// profit centre analysis, company code analysis (customers always inside their company code) and customer name checks.
// Fixed rules only: the same data and choices always give the same report.
// TAT – ONE rule everywhere: Received date → submission (upload) date; an invoice not submitted yet counts to today.
// The email shows the report; the attached dashboard.html lets you change period / company code / customer.
const RECIPIENTS = ['']; // put your email between the quotes, e.g. ['name.surname@company.com']
const RULES = {
  slaDays: 1, // 24-hour TAT: submitted on the received date or the next day (the tracker has dates, not times)
  followUpDays: 2, // a follow-up is due when nothing was done for this many days (last date in "Reason for Pending")
  // past due needs each customer's payment terms – planned as a later addition, so it is not shown yet
};
const TODAY = new Date().toISOString().slice(0, 10); // days pending are counted up to this date
RULES.today = TODAY;

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
  const val = (r) => num(r.v);
  const avgOf = (rows, f) => { const x = rows.map(f).filter((v) => v !== null && v !== undefined); return x.length ? sum(x, (v) => v) / x.length : null; };
  const median = (x) => { if (!x.length) return null; const y = [...x].sort((p, q) => p - q); const m = Math.floor(y.length / 2); return y.length % 2 ? y[m] : (y[m - 1] + y[m]) / 2; };
  const groupBy = (rows, key) => {
    const m = new Map();
    for (const r of rows) { const k = key(r); if (k === null || k === undefined || k === '') continue; const g = m.get(k) || { key: k, n: 0, v: 0, rows: [] }; g.n++; g.v += val(r); g.rows.push(r); m.set(k, g); }
    return [...m.values()];
  };
  const SLA = RULES.slaDays ?? 1;

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
  const [pf, pt] = type === 'Weekly' || type === 'Custom period'
    ? [addDays(from, -len), addDays(from, -1)] : [addMonths(from, -1), monthEnd(addMonths(from, -1))];
  const today = opts.today || RULES.today || latest;
  const daysBetween = (x, y) => Math.round((ms(y) - ms(x)) / DAY);

  // ----- areas and codes -----
  const ENTITY = { '3060': 'LA PRAIRIE (CANADA)', '3487': 'LA PRAIRIE (CANADA)', '3485': 'CHARLEROI', G367: 'CLEARWATER' };
  const AREA_ORDER = ['LA PRAIRIE (CANADA)', 'CHARLEROI', 'CLEARWATER', 'OTHER', 'NO COMPANY CODE'];
  const areaOf = (r) => ENTITY[r.cc] || (r.cc ? 'OTHER' : 'NO COMPANY CODE');
  // profit centre: Clearwater (G367) usually has none, which is expected, not a gap
  const pcKey = (r) => r.pc || (r.cc === 'G367' ? 'N/A – CLEARWATER' : 'NOT FOUND');
  const plKey = (r) => r.pl || 'NOT FOUND';

  // ----- customers: the SAP customer code identifies a customer; without one, the cleaned name does -----
  const SUFFIX = /\b(INC|INCORPORATED|LTD|LIMITED|LLC|CORP|CORPORATION|CO|COMPANY|PLC|ULC|LP|LLP|THE|SA|AG|GMBH)\b/g;
  const normName = (s) => String(s || '').toUpperCase().replace(/&/g, ' AND ').replace(/[^A-Z0-9]+/g, ' ').replace(SUFFIX, ' ').replace(/\s+/g, ' ').trim();
  const custKey = (r) => (r.sap ? `S:${r.sap}` : `N:${normName(r.c) || r.c}`);
  const spellings = new Map(); // customer → how often each spelling is used (all data, so the name shown never changes with filters)
  for (const r of all) { const k = custKey(r); const m = spellings.get(k) || new Map(); m.set(r.c, (m.get(r.c) || 0) + 1); spellings.set(k, m); }
  const mainName = (k) => [...(spellings.get(k) || new Map([['UNKNOWN CUSTOMER', 1]]))].sort((x, y) => y[1] - x[1] || x[0].localeCompare(y[0]))[0][0];
  const custLabel = (k) => (k.startsWith('S:') ? `${mainName(k)} (SAP ${k.slice(2)})` : `${mainName(k)} (no SAP code)`);

  // ----- selection -----
  const cc = String(opts.companyCode || '').trim().toUpperCase();
  const cust = String(opts.customer || '').trim().toUpperCase();
  const pcSel = String(opts.profitCentre || '').trim().toUpperCase();
  const plSel = String(opts.productLine || '').trim().toUpperCase();
  const isOpen = (r) => /pend|hold|open|progress|query|block/i.test(r.st || '');
  const isDone = (r) => r.st === 'Completed';
  const MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'];
  // dates written in "Reason for Pending" ("email sent on 23 June", "follow up on 3 July", "19th september")
  // a date without a year is read in order: on or after the previous date (and the received date), not after today
  const actionDates = (text, start) => {
    const found = new Set();
    let prev = start ? addDays(start, -7) : null;
    const lastYear = +today.slice(0, 4);
    const re = /\b(\d{1,2})(?:st|nd|rd|th)?\s*(?:of\s+)?(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?(?:,?\s*(\d{4}))?|\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+(\d{1,2})(?:st|nd|rd|th)?\b(?:,?\s*(\d{4}))?/gi;
    for (const m of String(text || '').matchAll(re)) {
      const day = +(m[1] || m[5]); const mon = MONTHS.indexOf(String(m[2] || m[4]).toLowerCase().slice(0, 3));
      if (!(day >= 1 && day <= 31) || mon < 0) continue;
      const at = (y) => `${y}-${String(mon + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
      let yr = +(m[3] || m[6]) || 0;
      if (!yr) {
        if (prev) for (let y = +prev.slice(0, 4); y <= lastYear && !yr; y++) if (at(y) >= prev && at(y) <= addDays(today, 1)) yr = y;
        if (!yr) yr = at(lastYear) <= addDays(today, 1) ? lastYear : lastYear - 1; // fallback: the latest such date up to today
      }
      if (iso(ms(at(yr))) !== at(yr)) continue; // skips impossible dates like 31 Sep
      found.add(at(yr));
      if (!prev || at(yr) > prev) prev = at(yr);
    }
    return [...found].sort();
  };
  // root cause group of the standard category (set when the data is saved); older rows fall back to simple rules
  const GROUP_OF = { 'PO not available on portal': 'PO issue on portal', 'PO lines not available on portal': 'PO issue on portal',
    'PO cancelled or closed': 'PO issue on portal', 'PO line and invoice line mismatch': 'Invoice vs PO mismatch',
    'Price and quantity mismatch': 'Invoice vs PO mismatch', 'Quantity mismatch': 'Invoice vs PO mismatch', 'Price mismatch': 'Invoice vs PO mismatch',
    'Amount, tax or freight mismatch': 'Invoice vs PO mismatch', 'No portal access / portal migration': 'Portal access',
    'Unable to submit invoice on portal': 'Submission issue', Other: 'Other' };
  const BLOCKERS = [
    ['Invoice vs PO mismatch', /mismatch|variance|quantity|qty|price|amount|tax|tariff|freight/i],
    ['Submission issue', /(unable|cannot|can not|not able)\b.*invoice/i],
    ['PO issue on portal', /\bpo\b|purchase order/i],
    ['Portal access', /access|migrat|coupa|oracle|ariba|login|regist|portal/i],
  ];
  const blockerOf = (r) => {
    if (r.sc && GROUP_OF[r.sc]) return GROUP_OF[r.sc];
    const t = r.cat || r.why || ''; if (!t) return 'No reason given';
    return (BLOCKERS.find(([, re]) => re.test(t)) || ['Other'])[0];
  };
  const GROUP_ORDER = ['Portal access', 'Submission issue', 'PO issue on portal', 'Invoice vs PO mismatch', 'Other', 'No reason given'];
  // who has to act: portal access and submitting are the team's own job; PO problems need the customer or GE order management
  const FIX_OF = { 'Portal access': 'Ours (distribution team)', 'Submission issue': 'Ours (distribution team)',
    'PO issue on portal': 'Customer / GE order team', 'Invoice vs PO mismatch': 'Customer / GE order team', Other: 'To be classified', 'No reason given': 'To be classified' };
  const FIX_ORDER = ['Ours (distribution team)', 'Customer / GE order team', 'To be classified'];

  // every row in the selection (whatever its date), with TAT and pending details worked out once
  const scopedAny = all.filter((r) => (!cc || r.cc === cc) && (!cust || r.c.includes(cust) || r.sap === cust)
    && (!pcSel || pcKey(r) === pcSel) && (!plSel || plKey(r) === plSel)).map((r) => {
    const open = isOpen(r); const done = isDone(r);
    // TAT = received → submitted; open items count to today; no received date = unknown
    let tat = null;
    if (r.rd && done && r.ud) { const t = daysBetween(r.rd, r.ud); tat = t >= 0 ? t : null; }
    else if (r.rd && open) tat = Math.max(0, daysBetween(r.rd, today));
    const sla = tat === null ? 'unknown' : done ? (tat <= SLA ? 'met' : 'missed') : open ? (tat <= SLA ? 'window' : 'missed') : 'unknown';
    const x = { ...r, open, done, tat, sla, area: areaOf(r), ck: custKey(r) };
    x.cl = custLabel(x.ck);
    if (open) {
      const acts = actionDates(r.why, r.rd || r.ad || r.d);
      x.age = tat; x.last = acts[acts.length - 1] || null; x.sinceLast = x.last ? Math.max(0, daysBetween(x.last, today)) : null;
      x.followUps = acts.length; x.blocker = blockerOf(r); x.category = r.sc || r.cat || ''; x.fix = FIX_OF[x.blocker] || 'To be classified';
      // follow-up due: nothing logged for 2+ days (or nothing logged at all and the age is unknown)
      x.due = x.sinceLast !== null ? x.sinceLast >= RULES.followUpDays : (x.age === null || x.age >= RULES.followUpDays);
    }
    return x;
  });
  const scoped = scopedAny.filter((r) => r.d);
  const cur = scoped.filter((r) => r.d >= from && r.d <= to); // received in the period
  const prev = scoped.filter((r) => r.d >= pf && r.d <= pt);
  const open = scopedAny.filter((r) => r.open);
  const AREAS = AREA_ORDER.filter((ar) => scopedAny.some((r) => r.area === ar));

  // figures for one group: invoices received in the period (volume, SLA, TAT) + everything open now
  const statsOf = (rec, op) => {
    const n = { met: 0, missed: 0, window: 0, unknown: 0 };
    for (const r of rec) n[r.sla]++;
    const doneT = rec.filter((r) => r.done && r.tat !== null);
    return { received: rec.length, receivedV: sum(rec, val), submitted: rec.filter((r) => r.done).length, ...n,
      slaPct: n.met + n.missed ? n.met / (n.met + n.missed) : null, avgTat: avgOf(doneT, (r) => r.tat), medTat: median(doneT.map((r) => r.tat)),
      open: op.length, openV: sum(op, val), due: op.filter((r) => r.due).length, avgAge: avgOf(op, (r) => r.age),
      oldest: op.some((r) => r.age !== null) ? Math.max(...op.map((r) => r.age || 0)) : null };
  };
  const splitBy = (keyOf) => {
    const m = new Map();
    const add = (r, part) => { const k = keyOf(r); if (k === null || k === undefined || k === '') return; const g = m.get(k) || { key: k, rec: [], op: [] }; g[part].push(r); m.set(k, g); };
    for (const r of cur) add(r, 'rec');
    for (const r of open) add(r, 'op');
    return [...m.values()];
  };

  // ----- headline -----
  const submittedInPeriod = scopedAny.filter((r) => r.done && r.ud && r.ud >= from && r.ud <= to).length;
  const lastDay = [to, latest, today].sort()[0];
  let workDays = 0;
  for (let d = from; d <= lastDay; d = addDays(d, 1)) if ((new Date(ms(d)).getUTCDay() + 6) % 7 < 5) workDays++;
  const kpis = { ...statsOf(cur, open), submittedInPeriod, perWorkDay: workDays ? cur.length / workDays : null, workDays,
    prevReceived: prev.length, change: prev.length ? (cur.length - prev.length) / prev.length : null,
    oursOpen: open.filter((r) => r.fix === FIX_ORDER[0]).length, portalAccessOpen: open.filter((r) => r.blocker === 'Portal access').length };
  const byArea = AREAS.map((ar) => {
    const s = splitBy((r) => (r.area === ar ? r.cc || '(none)' : null)).sort((x, y) => x.key.localeCompare(y.key));
    return { key: ar, ...statsOf(cur.filter((r) => r.area === ar), open.filter((r) => r.area === ar)), codes: s.map((g) => ({ key: g.key, ...statsOf(g.rec, g.op) })) };
  });

  // ----- volume and scope of work -----
  const monthsBack = [];
  for (let k = 11; k >= 0; k--) { const m = addMonths(monthStart(to < latest ? to : latest), -k); if (m >= monthStart(first)) monthsBack.push(m); }
  const CODES = [...new Set(scopedAny.map((r) => r.cc || '(none)'))].sort((x, y) => AREA_ORDER.indexOf(areaOf({ cc: x === '(none)' ? '' : x })) - AREA_ORDER.indexOf(areaOf({ cc: y === '(none)' ? '' : y })) || x.localeCompare(y));
  const months = monthsBack.map((m) => {
    const rows = scoped.filter((r) => r.d >= m && r.d <= monthEnd(m));
    return { key: m.slice(0, 7), n: rows.length, v: sum(rows, val), partial: m === monthStart(latest) && latest < monthEnd(m),
      areas: AREAS.map((ar) => rows.filter((r) => r.area === ar).length), codes: CODES.map((c) => rows.filter((r) => (r.cc || '(none)') === c).length) };
  });
  const fullMonths = months.filter((m) => !m.partial);
  const volume = {
    months, codes: CODES,
    monthlyAvg: fullMonths.length ? sum(fullMonths, (m) => m.n) / fullMonths.length : null,
    last12: sum(months, (m) => m.n), last12V: sum(months, (m) => m.v),
    busiest: [...fullMonths].sort((x, y) => y.n - x.n)[0] || null,
  };
  const lastWeek = weekStart(to < latest ? to : latest);
  volume.weeks = Array.from({ length: 8 }, (_, k) => addDays(lastWeek, -7 * (7 - k))).map((w) => {
    const rows = scoped.filter((r) => r.d >= w && r.d <= addDays(w, 6));
    const met = rows.filter((r) => r.sla === 'met').length; const missed = rows.filter((r) => r.sla === 'missed').length;
    return { key: w, n: rows.length, v: sum(rows, val), areas: AREAS.map((ar) => rows.filter((r) => r.area === ar).length), slaPct: met + missed ? met / (met + missed) : null };
  });
  const channelOf = (r) => (!r.p ? 'Not recorded' : r.p.includes('@') ? 'Email' : 'Portal');
  const CHANNELS = ['Portal', 'Email', 'Not recorded'];
  volume.channels = CHANNELS.map((ch) => ({ key: ch, n: cur.filter((r) => channelOf(r) === ch).length })).filter((x) => x.n);
  volume.channelByArea = AREAS.map((ar) => ({ key: ar, segs: CHANNELS.map((ch) => cur.filter((r) => r.area === ar && channelOf(r) === ch).length) }));
  volume.portals = groupBy(cur.filter((r) => channelOf(r) === 'Portal'), (r) => r.p.split(/[,;/]/)[0].trim().toUpperCase()).sort((x, y) => y.n - x.n).slice(0, 8).map((g) => ({ key: g.key, n: g.n }));
  volume.heat = AREAS.filter((ar) => ar !== 'NO COMPANY CODE').map((ar) => ({ area: ar, months: monthsBack.slice(-6).map((m) => ({ key: m.slice(0, 7),
    cells: Array.from({ length: 31 }, (_, i) => scoped.filter((r) => r.area === ar && r.d.slice(0, 7) === m.slice(0, 7) && +r.d.slice(8, 10) === i + 1).length) })) }));

  // ----- 24-hour TAT (invoices received in the period) -----
  const TAT_BUCKETS = [[0, 0, 'Same day'], [1, 1, 'Next day'], [2, 2, '2 days'], [3, 5, '3–5 days'], [6, 10, '6–10 days'], [11, 30, '11–30 days'], [31, 1e9, 'Over 30 days']];
  const doneCur = cur.filter((r) => r.done && r.tat !== null);
  const tat = {
    buckets: TAT_BUCKETS.map(([lo, hi, key]) => ({ key, n: doneCur.filter((r) => r.tat >= lo && r.tat <= hi).length, within: hi <= SLA }))
      .concat([{ key: 'Not submitted yet', n: cur.filter((r) => r.open).length, openNow: true }]),
    byCode: splitBy((r) => r.cc || '(none)').filter((g) => g.rec.length).sort((x, y) => CODES.indexOf(x.key) - CODES.indexOf(y.key)).map((g) => ({ key: g.key, area: areaOf({ cc: g.key === '(none)' ? '' : g.key }), ...statsOf(g.rec, g.op) })),
    noTat: cur.filter((r) => r.sla === 'unknown').length,
    lateOpen: open.filter((r) => r.age !== null && r.age > SLA).length,
  };

  // ----- pending invoices -----
  const pendingStats = (rows) => ({ n: rows.length, v: sum(rows, val), due: rows.filter((r) => r.due).length, avgAge: avgOf(rows, (r) => r.age),
    oldest: rows.some((r) => r.age !== null) ? Math.max(...rows.map((r) => r.age || 0)) : null });
  const whereOf = (rows) => groupBy(rows, (r) => `${r.area} ${r.cc || ''}`.trim()).sort((x, y) => y.n - x.n || x.key.localeCompare(y.key)).map((g) => `${g.key}: ${g.n}`);
  const byGroupOrder = (x, y) => (GROUP_ORDER.indexOf(x.key) < 0 ? 99 : GROUP_ORDER.indexOf(x.key)) - (GROUP_ORDER.indexOf(y.key) < 0 ? 99 : GROUP_ORDER.indexOf(y.key));
  const rootCauses = groupBy(open, (r) => r.blocker).sort(byGroupOrder).map((g) => ({ key: g.key, fix: FIX_OF[g.key] || 'To be classified', ...pendingStats(g.rows), where: whereOf(g.rows),
    categories: groupBy(g.rows, (r) => r.category || '').sort((x, y) => y.n - x.n || x.key.localeCompare(y.key)).map((c) => ({ key: c.key, ...pendingStats(c.rows), where: whereOf(c.rows) })) }));
  const byFix = FIX_ORDER.map((k) => { const rows = open.filter((r) => r.fix === k); return { key: k, ...pendingStats(rows), causes: groupBy(rows, (r) => r.blocker).sort((x, y) => y.n - x.n).map((g) => `${g.key}: ${g.n}`) }; }).filter((x) => x.n);
  let cum = 0;
  const pareto = groupBy(open, (r) => r.category || r.blocker).sort((x, y) => y.n - x.n || x.key.localeCompare(y.key))
    .map((g) => { cum += g.n; return { key: g.key, n: g.n, v: g.v, cumPct: cum / (open.length || 1), fix: g.rows[0].fix }; });
  const openCodes = CODES.filter((c) => open.some((r) => (r.cc || '(none)') === c));
  const matrix = { codes: openCodes, rows: rootCauses.map((g) => ({ key: g.key, cells: openCodes.map((c) => open.filter((r) => r.blocker === g.key && (r.cc || '(none)') === c).length) })) };
  const AGE_BINS = [[0, 1, '0–1'], [2, 3, '2–3'], [4, 7, '4–7'], [8, 15, '8–15'], [16, 30, '16–30'], [31, 60, '31–60'], [61, 90, '61–90'], [91, 1e9, '90+']];
  const inBin = (r, [lo, hi]) => r.age !== null && r.age >= lo && r.age <= hi;
  const lanes = rootCauses.map((g) => {
    const rows = open.filter((r) => r.blocker === g.key);
    return { key: g.key, fix: g.fix, n: rows.length, noAge: rows.filter((r) => r.age === null).length,
      bins: AGE_BINS.map((b) => { const inb = rows.filter((r) => inBin(r, b)); return { n: inb.length, due: inb.filter((r) => r.due).length, areas: AREAS.map((ar) => inb.filter((r) => r.area === ar).length) }; }),
      points: rows.filter((r) => r.age !== null).slice(0, 400).map((r) => ({ i: String(r.i), age: r.age, v: val(r), area: r.area, cc: r.cc, c: r.cl, cat: r.category, due: r.due })) };
  });
  const ageing = AGE_BINS.map((b) => { const rows = open.filter((r) => inBin(r, b)); return { key: `${b[2]} days`, n: rows.length, v: sum(rows, val), areas: AREAS.map((ar) => rows.filter((r) => r.area === ar).length) }; });
  const pendingList = [...open].sort((x, y) => byGroupOrder({ key: x.blocker }, { key: y.blocker }) || String(x.category).localeCompare(String(y.category))
    || ((y.age ?? -1) - (x.age ?? -1)) || (val(y) - val(x)));
  const pending = {
    today, rules: { followUpDays: RULES.followUpDays, slaDays: SLA }, total: pendingStats(open), byFix, rootCauses, pareto, matrix,
    bins: AGE_BINS.map((b) => b[2]), lanes, ageing, noAge: open.filter((r) => r.age === null).length, list: pendingList,
    noDateInReason: open.filter((r) => !r.last).length,
    owners: groupBy(open.filter((r) => r.due), (r) => r.ub || 'Not recorded').sort((x, y) => y.n - x.n).map((g) => ({ key: g.key, n: g.n })),
  };

  // ----- profit centres -----
  const mainCause = (op) => (op.length ? groupBy(op, (r) => r.blocker).sort((x, y) => y.n - x.n || x.key.localeCompare(y.key))[0].key : '');
  const listOf = (rows, f) => [...new Set(rows.map(f).filter(Boolean))].sort();
  const profitCentres = splitBy(pcKey).map((g) => ({ key: g.key, codes: listOf([...g.rec, ...g.op], (r) => r.cc), lines: listOf([...g.rec, ...g.op], (r) => r.pl),
    ...statsOf(g.rec, g.op), share: cur.length ? g.rec.length / cur.length : 0, cause: mainCause(g.op) }))
    .sort((x, y) => y.received - x.received || y.open - x.open || x.key.localeCompare(y.key));

  // ----- company codes, each with its customers -----
  const companies = splitBy((r) => r.cc || '(none)').sort((x, y) => CODES.indexOf(x.key) - CODES.indexOf(y.key)).map((g) => {
    const st = statsOf(g.rec, g.op);
    const custs = splitBy((r) => ((r.cc || '(none)') === g.key ? r.ck : null)).map((c) => ({ key: c.key, label: custLabel(c.key), sap: c.key.startsWith('S:') ? c.key.slice(2) : '',
      ...statsOf(c.rec, c.op), share: g.rec.length ? c.rec.length / g.rec.length : 0, cause: mainCause(c.op) }))
      .sort((x, y) => y.received - x.received || y.open - x.open || x.label.localeCompare(y.label));
    return { key: g.key, area: areaOf({ cc: g.key === '(none)' ? '' : g.key }), ...st, causes: groupBy(g.op, (r) => r.blocker).sort((x, y) => y.n - x.n).map((c) => `${c.key}: ${c.n}`), customers: custs };
  });

  // ----- customer names and SAP codes (all rows in the selection) -----
  const withSap = scopedAny.filter((r) => r.sap);
  const sameName = [];
  for (const g of groupBy(withSap, (r) => normName(r.c))) {
    const codes = groupBy(g.rows, (r) => r.sap);
    if (codes.length > 1) sameName.push({ key: mainName(`S:${codes.sort((x, y) => y.n - x.n)[0].key}`), codes: codes.map((c) => ({ sap: c.key, n: c.n, ccs: listOf(c.rows, (r) => r.cc) })) });
  }
  // look-alike names inside the same company code (typos, punctuation, Inc / Ltd) – shown for checking, never joined silently
  const near = (a, b, max) => {
    if (Math.abs(a.length - b.length) > max) return false;
    let p = Array.from({ length: b.length + 1 }, (_, j) => j);
    for (let i = 1; i <= a.length; i++) {
      const row = [i]; let best = i;
      for (let j = 1; j <= b.length; j++) { row[j] = Math.min(p[j] + 1, row[j - 1] + 1, p[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1)); if (row[j] < best) best = row[j]; }
      if (best > max) return false;
      p = row;
    }
    return p[b.length] <= max;
  };
  const variants = [];
  for (const g of groupBy(withSap, (r) => r.sap)) {
    const names = groupBy(g.rows, (r) => r.c).sort((x, y) => y.n - x.n || x.key.localeCompare(y.key));
    if (names.length > 1) variants.push({ sap: g.key, main: names[0].key, others: names.slice(1).map((x) => {
      const p = normName(names[0].key); const q = normName(x.key);
      // a spelling far from the main name is more likely a wrong SAP code than a typo
      return { name: x.key, n: x.n, odd: !near(p, q, Math.max(2, Math.floor(0.3 * Math.min(p.length, q.length)))) };
    }), ccs: listOf(g.rows, (r) => r.cc), n: g.n });
  }
  const lookAlike = [];
  for (const code of CODES) {
    const ents = groupBy(scopedAny.filter((r) => (r.cc || '(none)') === code), (r) => r.ck).sort((x, y) => y.n - x.n).slice(0, 600)
      .map((g) => ({ ck: g.key, norm: normName(mainName(g.key)), sap: g.key.startsWith('S:') ? g.key.slice(2) : '', label: custLabel(g.key), n: g.n }));
    for (let i = 0; i < ents.length; i++) {
      for (let j = i + 1; j < ents.length; j++) {
        const A = ents[i]; const B = ents[j];
        if (!A.norm || !B.norm) continue;
        const short = Math.min(A.norm.length, B.norm.length);
        const max = short >= 12 ? 2 : short >= 6 ? 1 : 0;
        if (!near(A.norm, B.norm, max)) continue;
        if (A.sap && B.sap && A.norm === B.norm) continue; // already listed under "same name, different SAP codes"
        lookAlike.push({ cc: code, a: A.label, an: A.n, b: B.label, bn: B.n,
          kind: A.sap && B.sap ? 'Similar names, different SAP codes – kept apart' : 'Possible same customer – please check' });
      }
    }
  }
  const identity = { sameName, variants: variants.sort((x, y) => y.n - x.n), lookAlike: lookAlike.slice(0, 200), lookAlikeAll: lookAlike.length };

  // ----- pending reason wording → standard category -----
  const wording = groupBy(scopedAny.filter((r) => r.sc), (r) => r.sc).sort((x, y) => y.n - x.n).map((g) => {
    const w = groupBy(g.rows, (r) => r.cat || '(no category – read from the reason)').sort((x, y) => y.n - x.n || x.key.localeCompare(y.key));
    return { key: g.key, group: GROUP_OF[g.key] || 'Other', n: g.n, wordings: w.map((x) => ({ key: x.key, n: x.n })) };
  });

  // ----- data quality -----
  const fillIn = [
    ['No status', (r) => !r.st],
    ['Pending without a reason', (r) => r.open && !r.why && !r.cat],
    ['Pending without a category', (r) => r.open && !r.cat && !!r.why],
    ['Pending without an owner (Uploaded by)', (r) => r.open && !r.ub],
    ['Pending but has an upload date', (r) => r.open && !!r.ud],
    ['Completed without an upload date (TAT unknown)', (r) => r.done && !r.ud],
    ['No received date (TAT unknown)', (r) => (r.open || r.done) && !r.rd],
    ['Upload date before received date', (r) => !!(r.rd && r.ud && r.ud < r.rd)],
  ].map(([lbl, test]) => { const hit = scopedAny.filter(test); return { label: lbl, n: hit.length, examples: hit.slice(0, 8).map((r) => String(r.i)) }; }).filter((x) => x.n);
  const clash = (childOf, parentOf, child, parent) => {
    const m = new Map();
    for (const r of scopedAny) { const c = childOf(r); const p = parentOf(r); if (!c || !p) continue; if (!m.has(c)) m.set(c, new Set()); m.get(c).add(p); }
    const values = [...m].filter(([, s]) => s.size > 1).map(([c]) => c).sort();
    return values.length ? { child, parent, values } : null;
  };
  const quality = {
    fillIn,
    noValue: cur.filter((r) => !val(r)).length,
    repeated: groupBy(cur, (r) => String(r.i)).filter((g) => g.n > 1).map((g) => g.key),
    problems: [clash((r) => r.pc, (r) => r.cc, 'profit centre', 'company code'), clash((r) => r.so, (r) => r.cc, 'sales org', 'company code')].filter(Boolean),
  };

  return {
    label, type, from, to, first, latest, cc, cust, pcSel, plSel, today, areas: AREAS,
    kpis, byArea, volume, tat, pending, profitCentres, companies, identity, wording, quality,
  };
}

function render(a, web) {
  if (a.empty) return '<p>No data for this selection.</p>';
  const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const money = (n) => (Number(n) || 0).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const money0 = (n) => (Number(n) || 0).toLocaleString('en-US', { maximumFractionDigits: 0 });
  const int = (n) => Math.round(n || 0).toLocaleString('en-US');
  const d1 = (x) => (x === null || x === undefined ? '–' : x.toFixed(1));
  const pc = (x) => (x === null || x === undefined ? '–' : `${(100 * x).toFixed(0)}%`);
  const nv = (v) => parseFloat(String(v ?? '').replace(/[^0-9.\-]/g, '')) || 0;
  const C = { ink: '#111827', mute: '#6b7280', line: '#e5e7eb', head: '#1f3a5f', bar: '#2b6cb0', warn: '#b45309', bad: '#b91c1c', good: '#047857', soft: '#eef2f7' };
  const AREA_COLOR = { 'LA PRAIRIE (CANADA)': '#2b6cb0', CHARLEROI: '#0f766e', CLEARWATER: '#c2410c', OTHER: '#6b7280', 'NO COMPANY CODE': '#9ca3af' };
  const SLA_SERIES = [{ k: 'met', name: 'Within 24 h', color: '#047857' }, { k: 'missed', name: 'Over 24 h', color: '#b91c1c' },
    { k: 'window', name: 'Still within 24 h (open)', color: '#93c5fd' }, { k: 'unknown', name: 'TAT unknown', color: '#d1d5db' }];
  const FIX_COLOR = { 'Ours (distribution team)': '#7c3aed', 'Customer / GE order team': '#0f766e', 'To be classified': '#9ca3af' };
  const CH_COLOR = ['#2b6cb0', '#0f766e', '#d1d5db'];
  const areaSeries = a.areas.map((ar) => ({ name: ar, color: AREA_COLOR[ar] || '#6b7280' }));
  const hex2 = (x) => Math.round(x).toString(16).padStart(2, '0');
  const shade = (n, mx) => { if (!n) return '#f9fafb'; const t = Math.min(1, n / (mx || 1)); const mix = (x, y) => x + (y - x) * t; return `#${hex2(mix(219, 30))}${hex2(mix(234, 64))}${hex2(mix(254, 175))}`; };
  const W = web ? 1180 : 860;

  // ---------- building blocks (tables work in Outlook; the dashboard also gets SVG charts) ----------
  const th = (t, right) => `<th style="text-align:${right ? 'right' : 'left'};padding:6px 10px;background:${C.head};color:#fff;font-weight:600;font-size:12px">${esc(t)}</th>`;
  const td = (t, right, color) => `<td style="padding:5px 10px;border-bottom:1px solid ${C.line};font-size:12px;${right ? 'text-align:right;' : ''}${color ? `color:${color};` : ''}">${t}</td>`;
  const table = (heads, rows, wide) => `<table cellspacing="0" cellpadding="0" style="border-collapse:collapse;width:100%;max-width:${wide ? 1180 : 860}px">` +
    `<tr>${heads.map((x, i) => th(x, i > 0 && x !== '')).join('')}</tr>${rows.join('') || `<tr>${td('No data')}</tr>`}</table>`;
  const sec = (n, t, sub) => `<h2 style="margin:34px 0 4px;padding-top:10px;border-top:3px solid ${C.head};color:${C.head};font-size:19px">${n}. ${esc(t)}</h2>` +
    (sub ? `<div style="color:${C.mute};font-size:12px;margin-bottom:8px">${esc(sub)}</div>` : '');
  const h = (t, sub) => `<h3 style="margin:22px 0 4px;color:${C.head};font-size:15px">${esc(t)}</h3>${sub ? `<div style="color:${C.mute};font-size:12px;margin-bottom:8px">${esc(sub)}</div>` : ''}`;
  const note = (t, color) => `<div style="font-size:11px;color:${color || C.mute};margin-top:4px">${t}</div>`;
  const kpi = (label, value, sub, color) => `<td style="padding:10px 14px;border:1px solid ${C.line};vertical-align:top;width:25%"><div style="font-size:11px;color:${C.mute}">${esc(label)}</div>` +
    `<div style="font-size:21px;font-weight:700;color:${color || C.ink}">${esc(value)}</div><div style="font-size:11px;color:${C.mute}">${esc(sub || '')}</div></td>`;
  const legend = (items) => `<div style="font-size:11px;color:${C.mute};margin:4px 0">${items.map((s) => `<span style="white-space:nowrap;margin-right:12px"><span style="display:inline-block;width:10px;height:10px;background:${s.color};vertical-align:middle"></span> ${esc(s.name)}</span>`).join('')}</div>`;
  const bar = (part, whole, color = C.bar, hgt = 10) => (part > 0 ? `<table cellpadding="0" cellspacing="0" width="${Math.max(2, Math.round(100 * part / (whole || 1)))}%"><tr><td bgcolor="${color}" height="${hgt}" style="font-size:0;line-height:0">&nbsp;</td></tr></table>` : '');
  const segBar = (segs, widthPct = 100, hgt = 16) => {
    const tot = segs.reduce((s, x) => s + x.n, 0);
    if (!tot) return '';
    return `<table cellspacing="0" cellpadding="0" width="${Math.max(2, Math.round(widthPct))}%"><tr>${segs.filter((x) => x.n > 0).map((x) => `<td bgcolor="${x.color}" width="${Math.max(1, Math.round(100 * x.n / tot))}%" height="${hgt}" title="${esc(x.name)}: ${int(x.n)}" style="font-size:9px;line-height:${hgt}px;color:#fff;text-align:center;white-space:nowrap;overflow:hidden">${100 * x.n / tot >= 14 && widthPct >= 30 ? int(x.n) : ''}</td>`).join('')}</tr></table>`;
  };
  // horizontal bars, one row per item
  const hbars = (items, fmt = int) => {
    const max = Math.max(1, ...items.map((x) => x.n));
    return `<table cellspacing="0" cellpadding="0" style="border-collapse:collapse;width:100%;max-width:860px;font-size:12px">` + items.map((x) =>
      `<tr><td style="padding:3px 8px 3px 0;white-space:nowrap;width:30%">${esc(x.label)}</td><td style="padding:3px 0;width:52%">${bar(x.n, max, x.color || C.bar, 12)}</td>` +
      `<td style="padding:3px 0 3px 8px;text-align:right;white-space:nowrap">${fmt(x.n)}${x.note ? ` <span style="color:${C.mute};font-size:11px">${esc(x.note)}</span>` : ''}</td></tr>`).join('') + '</table>';
  };
  // stacked horizontal bars (absolute: length = total; otherwise 100%)
  const stackRows = (rows, series, absolute, right) => {
    const max = Math.max(1, ...rows.map((r) => r.segs.reduce((s, x) => s + x, 0)));
    return `<table cellspacing="0" cellpadding="0" style="border-collapse:collapse;width:100%;max-width:860px;font-size:12px">` + rows.map((r) => {
      const tot = r.segs.reduce((s, x) => s + x, 0);
      return `<tr><td style="padding:4px 8px 4px 0;white-space:nowrap;width:24%">${esc(r.label)}</td><td style="padding:4px 0;width:60%">${segBar(r.segs.map((n, i) => ({ n, color: series[i].color, name: series[i].name })), absolute ? 100 * tot / max : 100)}</td>` +
        `<td style="padding:4px 0 4px 8px;text-align:right;white-space:nowrap">${right ? right(r) : int(tot)}</td></tr>`;
    }).join('') + '</table>' + legend(series);
  };
  // stacked columns (e.g. invoices per month by area)
  const stackCols = (cols, series, H = 120) => {
    const max = Math.max(1, ...cols.map((c) => c.segs.reduce((s, x) => s + x, 0)));
    return `<table cellspacing="2" cellpadding="0" style="font-size:10px"><tr>` + cols.map((c) => {
      const tot = c.segs.reduce((s, x) => s + x, 0);
      const parts = c.segs.map((n, i) => ({ hgt: n ? Math.max(1, Math.round(H * n / max)) : 0, color: c.light ? '#c7d2fe' : series[i].color, n, name: series[i].name })).filter((x) => x.hgt).reverse();
      return `<td valign="bottom" align="center" style="padding:0 3px"><div style="color:${C.mute};font-size:10px">${int(tot)}</div>` +
        `<table cellspacing="0" cellpadding="0" width="30">${parts.map((x) => `<tr><td bgcolor="${x.color}" height="${x.hgt}" title="${esc(x.name)}: ${int(x.n)}" style="font-size:0;line-height:0">&nbsp;</td></tr>`).join('')}</table></td>`;
    }).join('') + '</tr><tr>' + cols.map((c) => `<td align="center" style="color:${C.mute};padding-top:2px;white-space:nowrap">${esc(c.label)}</td>`).join('') + '</tr></table>' + legend(series);
  };
  // shaded grid: rows × columns of counts
  const heatGrid = (corner, cols, rows, opt = {}) => {
    const mx = Math.max(1, ...rows.flatMap((r) => r.cells));
    return `<table cellspacing="1" cellpadding="0" style="font-size:11px"><tr><td style="padding:3px 8px;color:${C.mute}">${esc(corner)}</td>${cols.map((c) => `<td style="padding:${opt.compact ? '2px 0' : '3px 6px'};text-align:center;color:${C.mute};white-space:nowrap;${opt.compact ? 'font-size:9px;' : ''}">${esc(c)}</td>`).join('')}${opt.total ? `<td style="padding:3px 8px;text-align:right;color:${C.mute}">Total</td>` : ''}</tr>` +
      rows.map((r) => `<tr><td style="padding:3px 8px;white-space:nowrap">${esc(r.label)}</td>${r.cells.map((n) => `<td bgcolor="${shade(n, mx)}" style="text-align:center;${opt.compact ? 'width:19px;height:18px;font-size:9px;' : 'min-width:34px;height:22px;padding:0 4px;'}color:${n / mx > 0.55 ? '#fff' : C.ink}">${n || ''}</td>`).join('')}` +
        `${opt.total ? `<td style="padding:3px 8px;text-align:right;font-weight:600">${int(r.cells.reduce((s, x) => s + x, 0))}</td>` : ''}</tr>`).join('') + '</table>';
  };
  const columns = (pts, fmt = int, H = 100, color = C.bar) => {
    const max = Math.max(1, ...pts.map((p) => p.n || 0));
    return `<table cellspacing="2" cellpadding="0" style="font-size:10px"><tr>` + pts.map((p) => `<td valign="bottom" align="center" style="padding:0 3px"><div style="color:${C.mute}">${p.n === null ? '–' : fmt(p.n)}</div>` +
      `<table cellspacing="0" cellpadding="0" width="30"><tr><td bgcolor="${p.color || color}" height="${p.n ? Math.max(2, Math.round(H * p.n / max)) : 1}" style="font-size:0;line-height:0">&nbsp;</td></tr></table></td>`).join('') +
      '</tr><tr>' + pts.map((p) => `<td align="center" style="color:${C.mute};padding-top:2px;white-space:nowrap">${esc(p.label)}</td>`).join('') + '</tr></table>';
  };
  // --- SVG (dashboard only) ---
  const svgDonut = (segs, centre) => {
    const tot = segs.reduce((s, x) => s + x.n, 0); if (!tot) return '';
    const S = 170; const R = 80; const r = 48; const cx = S / 2; let a0 = -Math.PI / 2;
    const pt = (rad, ang) => `${(cx + rad * Math.cos(ang)).toFixed(2)},${(cx + rad * Math.sin(ang)).toFixed(2)}`;
    const paths = segs.filter((x) => x.n > 0).map((x) => {
      const a1 = a0 + (2 * Math.PI * x.n) / tot; const big = a1 - a0 > Math.PI ? 1 : 0;
      const d = x.n === tot ? `M ${pt(R, -Math.PI / 2)} A ${R} ${R} 0 1 1 ${pt(R, Math.PI * 1.4999)} L ${pt(r, Math.PI * 1.4999)} A ${r} ${r} 0 1 0 ${pt(r, -Math.PI / 2)} Z`
        : `M ${pt(R, a0)} A ${R} ${R} 0 ${big} 1 ${pt(R, a1)} L ${pt(r, a1)} A ${r} ${r} 0 ${big} 0 ${pt(r, a0)} Z`;
      a0 = a1;
      return `<path d="${d}" fill="${x.color}"><title>${esc(x.name)}: ${int(x.n)} (${(100 * x.n / tot).toFixed(0)}%)</title></path>`;
    }).join('');
    return `<table cellspacing="0" cellpadding="0"><tr><td><svg width="${S}" height="${S}" viewBox="0 0 ${S} ${S}" style="font-family:Segoe UI,Arial,sans-serif">${paths}` +
      `<text x="${cx}" y="${cx - 2}" text-anchor="middle" font-size="18" font-weight="700" fill="${C.ink}">${esc(centre ?? int(tot))}</text><text x="${cx}" y="${cx + 15}" text-anchor="middle" font-size="10" fill="${C.mute}">invoices</text></svg></td>` +
      `<td style="padding-left:14px;font-size:12px">${segs.filter((x) => x.n > 0).map((x) => `<div style="margin:3px 0"><span style="display:inline-block;width:10px;height:10px;background:${x.color}"></span> ${esc(x.name)} – <b>${int(x.n)}</b> (${(100 * x.n / tot).toFixed(0)}%)</div>`).join('')}</td></tr></table>`;
  };
  const svgLine = (pts, fmt, color = C.head) => {
    const SW = 840; const SH = 200; const top = 18; const bottom = 30; const plotH = SH - top - bottom; const step = (SW - 50) / pts.length;
    const max = Math.max(1, ...pts.map((p) => p.n || 0));
    const x = (i) => 40 + step * i + step / 2; const y = (v) => top + plotH - (plotH * v) / max;
    const ok = pts.map((p, i) => ({ ...p, i })).filter((p) => p.n !== null);
    return `<svg width="${SW}" height="${SH}" viewBox="0 0 ${SW} ${SH}" style="font-family:Segoe UI,Arial,sans-serif;max-width:100%">` +
      `<line x1="30" y1="${top + plotH}" x2="${SW - 10}" y2="${top + plotH}" stroke="${C.line}"/>` +
      `<polyline fill="none" stroke="${color}" stroke-width="2.5" points="${ok.map((p) => `${x(p.i)},${y(p.n)}`).join(' ')}"/>` +
      ok.map((p) => `<circle cx="${x(p.i)}" cy="${y(p.n)}" r="4" fill="${color}"><title>${esc(p.label)}: ${fmt(p.n)}</title></circle><text x="${x(p.i)}" y="${y(p.n) - 8}" text-anchor="middle" font-size="10" fill="${C.mute}">${fmt(p.n)}</text>`).join('') +
      pts.map((p, i) => `<text x="${x(i)}" y="${SH - 10}" text-anchor="middle" font-size="10" fill="${C.mute}">${esc(p.label)}</text>`).join('') + '</svg>';
  };
  const svgPareto = (items) => {
    const SW = 900; const left = 250; const rowH = 22; const SH = items.length * rowH + 30; const plotW = SW - left - 120;
    const max = Math.max(1, ...items.map((x) => x.n));
    const y = (i) => 10 + i * rowH;
    return `<svg width="${SW}" height="${SH}" viewBox="0 0 ${SW} ${SH}" style="font-family:Segoe UI,Arial,sans-serif;font-size:11px;max-width:100%">` +
      items.map((x, i) => `<text x="${left - 8}" y="${y(i) + 14}" text-anchor="end" fill="${C.ink}">${esc(String(x.key).slice(0, 38))}</text>` +
        `<rect x="${left}" y="${y(i) + 3}" width="${Math.max(2, (plotW * x.n) / max)}" height="15" rx="2" fill="${FIX_COLOR[x.fix] || C.bar}"><title>${esc(x.key)}: ${int(x.n)}</title></rect>` +
        `<text x="${left + Math.max(2, (plotW * x.n) / max) + 4}" y="${y(i) + 14}" fill="${C.mute}">${int(x.n)}</text>`).join('') +
      // running share as a thin bar on the right (0–100%)
      items.map((x, i) => `<rect x="${SW - 100}" y="${y(i) + 7}" width="60" height="7" fill="#fee2e2"/><rect x="${SW - 100}" y="${y(i) + 7}" width="${(60 * x.cumPct).toFixed(1)}" height="7" fill="${C.bad}"/>` +
        `<text x="${SW - 6}" y="${y(i) + 14}" text-anchor="end" fill="${C.bad}">${(100 * x.cumPct).toFixed(0)}%</text>`).join('') +
      `<text x="${SW - 6}" y="${SH - 4}" text-anchor="end" fill="${C.bad}">cumulative share</text></svg>`;
  };
  // swim lanes: one lane per root cause, each dot = an open invoice placed by days pending, colour = area, size = value
  const svgSwim = (P) => {
    const bins = P.bins; const SW = 1100; const left = 210; const laneH = 46; const SH = P.lanes.length * laneH + 46; const bandW = (SW - left - 20) / bins.length;
    const oldest = Math.max(120, ...P.lanes.flatMap((l) => l.points.map((p) => p.age)));
    const RANGES = [[0, 1], [2, 3], [4, 7], [8, 15], [16, 30], [31, 60], [61, 90], [91, oldest]];
    const xOf = (age) => { const i = RANGES.findIndex(([lo, hi]) => age >= lo && age <= hi); const k = i < 0 ? bins.length - 1 : i; const [lo, hi] = RANGES[k]; return left + bandW * k + 6 + (bandW - 12) * Math.min(1, (age - lo) / Math.max(1, hi - lo)); };
    const vmax = Math.max(1, ...P.lanes.flatMap((l) => l.points.map((p) => p.v)));
    const hash = (s) => { let x = 7; for (const ch of String(s)) x = (x * 31 + ch.charCodeAt(0)) % 9973; return x / 9973; };
    return `<svg width="${SW}" height="${SH}" viewBox="0 0 ${SW} ${SH}" style="font-family:Segoe UI,Arial,sans-serif;font-size:11px;max-width:100%">` +
      bins.map((b, i) => `<rect x="${left + bandW * i}" y="20" width="${bandW}" height="${SH - 46}" fill="${i === 0 ? '#ecfdf5' : i % 2 ? '#f9fafb' : '#ffffff'}"/><text x="${left + bandW * i + bandW / 2}" y="14" text-anchor="middle" fill="${C.mute}">${esc(b)} days</text>`).join('') +
      P.lanes.map((l, k) => `<line x1="${left}" y1="${20 + laneH * (k + 1)}" x2="${SW - 20}" y2="${20 + laneH * (k + 1)}" stroke="${C.line}"/>` +
        `<rect x="0" y="${22 + laneH * k}" width="6" height="${laneH - 4}" fill="${FIX_COLOR[l.fix] || '#9ca3af'}"/><text x="12" y="${20 + laneH * k + 20}" fill="${C.ink}" font-weight="600">${esc(l.key)}</text>` +
        `<text x="12" y="${20 + laneH * k + 35}" fill="${C.mute}">${int(l.n)} open · ${esc(l.fix)}</text>` +
        l.points.map((p) => `<circle cx="${xOf(p.age).toFixed(1)}" cy="${(24 + laneH * k + (laneH - 8) * hash(p.i)).toFixed(1)}" r="${(2.5 + 5 * Math.sqrt(p.v / vmax)).toFixed(1)}" fill="${AREA_COLOR[p.area] || '#6b7280'}" fill-opacity="0.75" stroke="${p.due ? C.bad : '#fff'}" stroke-width="${p.due ? 1.5 : 0.5}">` +
          `<title>${esc(p.i)} · ${esc(p.area)} ${esc(p.cc)} · ${esc(p.c)} · ${int(p.age)} days · ${money(p.v)} · ${esc(p.cat)}${p.due ? ' · follow-up due' : ''}</title></circle>`).join('')).join('') +
      `<text x="${left}" y="${SH - 6}" fill="${C.mute}">Green band = within 24 hours · dot size = value · red ring = follow-up due · hover a dot for the invoice</text></svg>` + legend(areaSeries);
  };
  // swim lanes for email: lanes × days-pending bands; each cell shows the count and a bar split by area
  const laneGrid = (P) => {
    const mx = Math.max(1, ...P.lanes.flatMap((l) => l.bins.map((b) => b.n)));
    return `<table cellspacing="0" cellpadding="0" style="border-collapse:collapse;font-size:11px;width:100%;max-width:860px"><tr><td style="padding:4px 8px;color:${C.mute}">Root cause (lane)</td>` +
      P.bins.map((b, i) => `<td style="padding:4px 4px;text-align:center;color:${i === 0 ? C.good : C.mute};white-space:nowrap;${i === 0 ? 'font-weight:600;' : ''}">${esc(b)} d</td>`).join('') + '</tr>' +
      P.lanes.map((l) => `<tr><td style="padding:6px 8px;border-top:1px solid ${C.line};border-left:5px solid ${FIX_COLOR[l.fix] || '#9ca3af'};white-space:nowrap"><b>${esc(l.key)}</b><div style="color:${C.mute};font-size:10px">${int(l.n)} open · ${esc(l.fix)}</div></td>` +
        l.bins.map((b) => `<td style="padding:4px 3px;border-top:1px solid ${C.line};text-align:center;vertical-align:middle;min-width:56px">${b.n ? `<div style="font-weight:600;${b.due ? `color:${C.bad};` : ''}">${int(b.n)}</div>${segBar(b.areas.map((n, i) => ({ n, color: areaSeries[i].color, name: areaSeries[i].name })), Math.max(18, 100 * b.n / mx), 7)}` : `<span style="color:#d1d5db">·</span>`}</td>`).join('') + '</tr>').join('') +
      '</table>' + legend(areaSeries) + note('Number in red = includes invoices with a follow-up due. Bar = split by area.');
  };

  const K = a.kpis; const P = a.pending; const V = a.volume; const T = a.tat;
  const scope = [a.cc && `company code ${a.cc}`, a.pcSel && `profit centre ${a.pcSel}`, a.plSel && `product line ${a.plSel}`,
    a.cust && `customer "${a.cust}"`].filter(Boolean).join(', ') || 'all company codes, profit centres, product lines and customers';
  const ageCell = (n) => td(n === null || n === undefined ? '–' : int(n), 1, n > 60 ? C.bad : n > 30 ? C.warn : '');
  const slaCell = (x) => td(pc(x), 1, x === null ? '' : x >= 0.9 ? C.good : x >= 0.7 ? C.warn : C.bad);
  const nw = (t) => `<span style="white-space:nowrap">${esc(t)}</span>`;
  const statRow = (label, x, sub) => `<tr>${td(sub ? `<span style="color:${C.mute}">&nbsp;&nbsp;&nbsp;&nbsp;↳ ${esc(label)}</span>` : `<b>${esc(label)}</b>`)}${td(int(x.received), 1)}${td(money0(x.receivedV), 1)}` +
    `${td(int(x.submitted), 1)}${slaCell(x.slaPct)}${td(d1(x.avgTat), 1)}${td(int(x.open), 1)}${td(money0(x.openV), 1)}${td(int(x.due), 1, x.due ? C.warn : '')}${ageCell(x.oldest)}</tr>`;
  const STAT_HEAD = ['Received', 'Value', 'Submitted', 'Within 24 h', 'Avg TAT (days)', 'Open now', 'Open value', 'Follow-up due', 'Oldest (days)'];
  const custMax = web ? 1e9 : 25;
  const listMax = web ? 1e9 : 300;

  const out = [];
  out.push(`<div style="font-family:Segoe UI,Arial,sans-serif;color:${C.ink};max-width:${W}px">
<h1 style="margin:0;color:${C.head};font-size:22px">Invoice distribution – ${esc(a.type)} report</h1>
<div style="color:${C.mute};font-size:12px">${esc(a.label)} · ${esc(a.from)} to ${esc(a.to)} · ${esc(scope)} · data from ${esc(a.first)} to ${esc(a.latest)} · days counted to ${esc(a.today)}</div>
<div style="color:${C.mute};font-size:12px;margin-top:2px"><b>TAT rule:</b> received date → submission (upload) date; an invoice not submitted yet counts to today. <b>24-hour TAT</b> = submitted on the received date or the next day.</div>`);

  // 1. headline
  out.push(sec(1, 'Headline'));
  out.push(`<table cellspacing="0" style="border-collapse:collapse;width:100%;max-width:860px"><tr>
${kpi('Invoices received', int(K.received), `${money0(K.receivedV)} · ${K.change === null ? 'no earlier period' : `${K.change >= 0 ? '▲' : '▼'} ${Math.abs(100 * K.change).toFixed(0)}% vs previous`}`)}
${kpi('Per working day', K.perWorkDay === null ? '–' : d1(K.perWorkDay), `${int(K.workDays)} working days`)}
${kpi('Submitted in period', int(K.submittedInPeriod), 'uploaded / sent, any received date')}
${kpi('Within 24 hours', pc(K.slaPct), `${int(K.met)} of ${int(K.met + K.missed)} with a known TAT`, K.slaPct === null ? '' : K.slaPct >= 0.9 ? C.good : K.slaPct >= 0.7 ? C.warn : C.bad)}
</tr><tr>
${kpi('Avg TAT (submitted)', K.avgTat === null ? '–' : `${d1(K.avgTat)} days`, `median ${K.medTat === null ? '–' : d1(K.medTat)} days`)}
${kpi('Open now', int(K.open), money0(K.openV))}
${kpi('Ours to act on', int(K.oursOpen), `incl. ${int(K.portalAccessOpen)} portal access`, K.oursOpen ? C.warn : '')}
${kpi('Follow-up due', int(K.due), `nothing logged ${P.rules.followUpDays}+ days`, K.due ? C.warn : '')}
</tr></table>`);
  out.push(h('24-hour TAT of invoices received in this period'));
  out.push(segBar(SLA_SERIES.map((s) => ({ n: K[s.k], color: s.color, name: s.name })), 100, 20) + legend(SLA_SERIES.map((s) => ({ name: `${s.name}: ${int(K[s.k])}`, color: s.color }))));
  out.push(h('Status by area and company code', `Received in ${a.label}; open now = every open invoice in this selection`));
  out.push(table(['Area › company code', ...STAT_HEAD], a.byArea.map((x) => statRow(x.key, x) + (x.codes.length > 1 || (x.codes[0] && x.codes[0].key !== x.key) ? x.codes.map((c) => statRow(c.key, c, true)).join('') : ''))));

  // 2. volume and scope of work
  out.push(sec(2, 'Volume and scope of work', 'How many invoices flow through each area and company code, and how steady that is'));
  out.push(`<table cellspacing="0" style="border-collapse:collapse;width:100%;max-width:860px"><tr>
${kpi('Last 12 months', int(V.last12), money0(V.last12V))}
${kpi('Monthly average', V.monthlyAvg === null ? '–' : int(V.monthlyAvg), 'complete months only')}
${kpi('Busiest month', V.busiest ? V.busiest.key : '–', V.busiest ? `${int(V.busiest.n)} invoices` : '')}
${kpi('This period', int(K.received), `previous ${int(K.prevReceived)}`)}
</tr></table>`);
  out.push(h('Invoices received per month, by area', 'Last 12 months; a lighter column = month not finished yet'));
  out.push(stackCols(V.months.map((m) => ({ label: m.key.slice(2) + (m.partial ? '*' : ''), segs: m.areas, light: m.partial })), areaSeries));
  out.push(h('Volume heatmap – company code × month', 'Darker = more invoices received'));
  out.push(heatGrid('Company code', V.months.map((m) => m.key.slice(2) + (m.partial ? '*' : '')), V.codes.map((c, i) => ({ label: c, cells: V.months.map((m) => m.codes[i]) })), { total: true }));
  out.push(h('Invoices received per week, by area (last 8 weeks)', 'Weeks start on Monday'));
  out.push(stackCols(V.weeks.map((w) => ({ label: w.key.slice(5), segs: w.areas })), areaSeries, 100));
  out.push(h('How invoices are sent', 'Received in this period, from "Name the Portal/Email ID"'));
  const chSegs = V.channels.map((x) => ({ n: x.n, name: x.key, color: CH_COLOR[['Portal', 'Email', 'Not recorded'].indexOf(x.key)] }));
  out.push(web ? svgDonut(chSegs) : segBar(chSegs, 100, 20) + legend(chSegs.map((s) => ({ name: `${s.name}: ${int(s.n)}`, color: s.color }))));
  out.push(stackRows(V.channelByArea.map((x) => ({ label: x.key, segs: x.segs })), ['Portal', 'Email', 'Not recorded'].map((n, i) => ({ name: n, color: CH_COLOR[i] })), true));
  if (V.portals.length) out.push(h('Busiest portals') + hbars(V.portals.map((x) => ({ label: x.key, n: x.n }))));
  out.push(h('Workload heatmap by area – day of month', 'Darker = more invoices received that day (last 6 months)'));
  out.push(V.heat.map((A) => `<div style="font-weight:600;font-size:12px;color:${C.head};margin:8px 0 2px">${esc(A.area)}</div>` +
    heatGrid('', Array.from({ length: 31 }, (_, i) => String(i + 1)), A.months.map((m) => ({ label: m.key, cells: m.cells })), { compact: true })).join(''));

  // 3. 24-hour TAT
  out.push(sec(3, '24-hour TAT', 'Invoices received in this period: within 24 hours = submitted on the received date or the next day; open invoices already over 24 hours count as over'));
  out.push(h('Within 24 hours by company code'));
  out.push(stackRows(T.byCode.map((x) => ({ label: `${x.key} – ${x.area}`, segs: SLA_SERIES.map((s) => x[s.k]), x })), SLA_SERIES, false,
    (r) => `<b style="color:${r.x.slaPct === null ? C.mute : r.x.slaPct >= 0.9 ? C.good : r.x.slaPct >= 0.7 ? C.warn : C.bad}">${pc(r.x.slaPct)}</b> <span style="color:${C.mute}">avg ${d1(r.x.avgTat)} d</span>`));
  out.push(h('How long invoices took to be submitted', 'Received → submitted, in days; green = within 24 hours'));
  out.push(hbars(T.buckets.map((b) => ({ label: b.key, n: b.n, color: b.openNow ? '#9ca3af' : b.within ? C.good : C.bad }))));
  out.push(h('Within 24 hours – weekly trend (last 8 weeks)', 'By the week the invoice was received'));
  const slaPts = V.weeks.map((w) => ({ label: w.key.slice(5), n: w.slaPct === null ? null : Math.round(100 * w.slaPct) }));
  out.push(web ? svgLine(slaPts, (n) => `${n}%`, C.good) : columns(slaPts, (n) => `${n}%`, 90, C.good));
  if (T.noTat) out.push(note(`${int(T.noTat)} invoice(s) received in this period have no TAT (no received date, or completed without an upload date) – see Data quality.`, C.warn));

  // 4. pending invoices
  out.push(sec(4, 'Pending invoices', `Every open invoice, whatever its date; days pending = received date to ${a.today}; follow-up due = nothing logged for ${P.rules.followUpDays}+ days`));
  out.push(h('Who has to act', 'Portal access and submission are the distribution team\'s own work; PO problems need the customer or GE order management'));
  const fixSegs = P.byFix.map((x) => ({ n: x.n, name: x.key, color: FIX_COLOR[x.key] }));
  out.push(web ? svgDonut(fixSegs) : segBar(fixSegs, 100, 20) + legend(fixSegs.map((s) => ({ name: `${s.name}: ${int(s.n)}`, color: s.color }))));
  out.push(table(['Who has to act', 'Open', 'Value', 'Follow-up due', 'Avg days', 'Oldest', 'Root causes'], P.byFix.map((x) =>
    `<tr>${td(`<span style="color:${FIX_COLOR[x.key]}">■</span> <b>${esc(x.key)}</b>`)}${td(int(x.n), 1)}${td(money0(x.v), 1)}${td(int(x.due), 1, x.due ? C.warn : '')}${td(d1(x.avgAge), 1)}${ageCell(x.oldest)}${td(`<span style="font-size:11px">${esc(x.causes.join(' · '))}</span>`)}</tr>`)));
  out.push(h('Root causes holding invoices', 'Root cause › standard category, and where the invoices sit (area and company code)'));
  const where = (w) => esc(w.slice(0, 4).join(' · ') + (w.length > 4 ? ' …' : ''));
  out.push(table(['Root cause › category', 'Who acts', 'Open', 'Value', 'Follow-up due', 'Avg days', 'Oldest', 'Where'], P.rootCauses.map((g) =>
    `<tr>${td(`<b>${esc(g.key)}</b>`)}${td(`<span style="font-size:11px">${esc(g.fix)}</span>`)}${td(int(g.n), 1)}${td(money0(g.v), 1)}${td(int(g.due), 1, g.due ? C.warn : '')}${td(d1(g.avgAge), 1)}${ageCell(g.oldest)}${td(`<span style="font-size:11px">${where(g.where)}</span>`)}</tr>` +
    (g.categories.length > 1 || (g.categories[0] && g.categories[0].key && g.categories[0].key !== g.key) ? g.categories.filter((c) => c.key).map((c) =>
      `<tr>${td(`<span style="color:${C.mute}">&nbsp;&nbsp;&nbsp;&nbsp;↳ ${esc(c.key)}</span>`)}${td('')}${td(int(c.n), 1)}${td(money0(c.v), 1)}${td(int(c.due), 1, c.due ? C.warn : '')}${td(d1(c.avgAge), 1)}${ageCell(c.oldest)}${td(`<span style="font-size:11px;color:${C.mute}">${where(c.where)}</span>`)}</tr>`).join('') : ''))));
  if (P.pareto.length > 1) {
    out.push(h('Pareto – which categories hold most open invoices', 'Biggest first; the running share shows how few categories explain most of the backlog'));
    out.push(web ? svgPareto(P.pareto.slice(0, 14)) : hbars(P.pareto.slice(0, 12).map((x) => ({ label: x.key, n: x.n, color: FIX_COLOR[x.fix], note: `${(100 * x.cumPct).toFixed(0)}% cumulative` }))));
  }
  if (P.matrix.codes.length) {
    out.push(h('Root cause × company code', 'Open invoices; darker = more'));
    out.push(heatGrid('Root cause', P.matrix.codes, P.matrix.rows.map((r) => ({ label: r.key, cells: r.cells })), { total: true }));
  }
  if (P.lanes.length) {
    out.push(h('Swim lanes – open invoices by root cause and days pending', 'One lane per root cause; left = newest, right = oldest; the first band is within 24 hours'));
    out.push(web ? svgSwim(P) : laneGrid(P));
  }
  out.push(h('Ageing of open invoices by area', 'Days pending = received date to today'));
  out.push(table(['Days pending', 'Open', 'Value', ...a.areas], P.ageing.map((b, i) => `<tr>${td(esc(b.key), 0, i >= 6 ? C.bad : i >= 5 ? C.warn : i === 0 ? C.good : '')}${td(int(b.n), 1)}${td(money0(b.v), 1)}${b.areas.map((n) => td(n ? int(n) : '', 1)).join('')}</tr>`)));
  if (P.noAge) out.push(note(`${int(P.noAge)} open invoice(s) have no received date, so their days pending are unknown.`, C.warn));
  out.push(h(`Pending invoices – full list (${int(P.list.length)})`, 'Grouped by root cause, oldest first; the reason from the tracker is shown under each invoice'));
  out.push(table(['Invoice', 'Area / co. code', 'Profit centre', 'Product line', 'Activity', 'Customer (SAP code)', 'Value', 'Days pending', 'Category', 'Last action', 'Days since', 'Follow-ups', 'Owner'],
    P.list.slice(0, listMax).map((r, i, list) => {
      const g = P.rootCauses.find((x) => x.key === r.blocker);
      const header = i === 0 || list[i - 1].blocker !== r.blocker
        ? `<tr><td colspan="13" bgcolor="${C.soft}" style="padding:6px 10px;font-weight:700;color:${C.head};font-size:12px;border-left:5px solid ${FIX_COLOR[r.fix] || '#9ca3af'}">${esc(r.blocker)} – ${esc(r.fix)}${g ? ` – ${int(g.n)} invoice(s) · ${money0(g.v)} · ${int(g.due)} follow-up due` : ''}</td></tr>` : '';
      return header + `<tr>${td(esc(r.i))}${td(nw(`${r.area} / ${r.cc || '–'}`))}${td(esc(r.pc || '–'))}${td(esc(r.pl || '–'))}${td(esc(r.bt || '–'))}${td(esc(r.cl))}${td(nw(money(nv(r.v))), 1)}${ageCell(r.age)}` +
        `${td(esc(r.category || '–'))}${td(nw(r.last || 'none logged'))}${td(r.sinceLast === null ? '–' : int(r.sinceLast), 1, r.due ? C.warn : '')}${td(int(r.followUps), 1)}${td(esc(r.ub || '–'))}</tr>` +
        (r.why ? `<tr><td colspan="13" style="padding:0 10px 6px;border-bottom:1px solid ${C.line};font-size:11px;color:${C.mute}">${esc(String(r.why).slice(0, 300))}${String(r.why).length > 300 ? ' …' : ''}</td></tr>` : '');
    }), true));
  if (P.list.length > listMax) out.push(note(`The first ${listMax} are shown; dashboard.html lists all of them.`));

  // 5. profit centres
  out.push(sec(5, 'Profit centre analysis', 'Profit centres come from the Tableau extract; Clearwater (G367) usually has none'));
  const pcs = a.profitCentres;
  if (pcs.length > 1) out.push(h('Invoices received by profit centre') + hbars(pcs.filter((x) => x.received).slice(0, 12).map((x) => ({ label: x.key, n: x.received, note: `${(100 * x.share).toFixed(0)}%` }))));
  out.push(table(['Profit centre', 'Co. code', 'Product line', 'Received', 'Share', 'Within 24 h', 'Avg TAT', 'Open', 'Open value', 'Follow-up due', 'Main root cause'], pcs.map((x) =>
    `<tr>${td(`<b>${esc(x.key)}</b>`)}${td(esc(x.codes.join(', ') || '–'))}${td(esc(x.lines.slice(0, 3).join(', ') + (x.lines.length > 3 ? ' …' : '') || '–'))}${td(int(x.received), 1)}${td(`${(100 * x.share).toFixed(1)}%`, 1)}${slaCell(x.slaPct)}${td(d1(x.avgTat), 1)}` +
    `${td(int(x.open), 1)}${td(money0(x.openV), 1)}${td(int(x.due), 1, x.due ? C.warn : '')}${td(`<span style="font-size:11px">${esc(x.cause || '–')}</span>`)}</tr>`), true));

  // 6. company codes with their customers
  out.push(sec(6, 'Company code analysis', 'Each company code with its own customers – a customer is always shown inside its company code, with its SAP customer code'));
  for (const x of a.companies) {
    out.push(`<h3 style="margin:22px 0 2px;color:#fff;background:${AREA_COLOR[x.area] || C.head};padding:6px 10px;font-size:15px;max-width:1160px">${esc(x.key)} – ${esc(x.area)}</h3>`);
    out.push(`<div style="font-size:12px;margin:4px 0 6px">Received <b>${int(x.received)}</b> (${money0(x.receivedV)}) · within 24 h <b>${pc(x.slaPct)}</b> · avg TAT <b>${d1(x.avgTat)}</b> days · open <b>${int(x.open)}</b> (${money0(x.openV)}) · follow-up due <b>${int(x.due)}</b>` +
      `${x.causes.length ? ` · <span style="color:${C.mute}">${esc(x.causes.slice(0, 4).join(' · '))}</span>` : ''}</div>`);
    out.push(table(['Customer (SAP code)', 'Received', 'Value', 'Share of co. code', '', 'Within 24 h', 'Avg TAT', 'Open', 'Open value', 'Follow-up due', 'Oldest', 'Main root cause'], x.customers.slice(0, custMax).map((c) =>
      `<tr>${td(esc(c.label))}${td(int(c.received), 1)}${td(money0(c.receivedV), 1)}${td(`${(100 * c.share).toFixed(1)}%`, 1)}<td style="padding:5px 4px;border-bottom:1px solid ${C.line};width:70px">${bar(c.share, 1, AREA_COLOR[x.area] || C.bar, 8)}</td>` +
      `${slaCell(c.slaPct)}${td(d1(c.avgTat), 1)}${td(int(c.open), 1)}${td(money0(c.openV), 1)}${td(int(c.due), 1, c.due ? C.warn : '')}${ageCell(c.oldest)}${td(`<span style="font-size:11px">${esc(c.cause || '')}</span>`)}</tr>`), true));
    if (x.customers.length > custMax) out.push(note(`${int(x.customers.length - custMax)} more customer(s) in ${esc(x.key)} – dashboard.html lists all of them.`));
  }

  // 7. customer names and SAP codes
  const I = a.identity;
  const idMax = web ? 1e9 : 30;
  out.push(sec(7, 'Customer names and SAP codes', 'The SAP customer code decides who the customer is; differences in names are listed here, not hidden'));
  out.push(h(`Same name, different SAP codes (${int(I.sameName.length)})`, 'Kept as separate customers – check that each code is right'));
  out.push(table(['Customer name', 'SAP codes (invoices · company codes)'], I.sameName.slice(0, idMax).map((x) => `<tr>${td(`<b>${esc(x.key)}</b>`)}${td(esc(x.codes.map((c) => `${c.sap} (${c.n} · ${c.ccs.join(', ')})`).join('; ')))}</tr>`)));
  out.push(h(`One SAP code, different spellings (${int(I.variants.length)})`, 'Counted as one customer under the most used spelling; the other spellings come from the tracker (typos, punctuation, Inc / Ltd)'));
  out.push(table(['SAP code', 'Shown as', 'Also written as (invoices)', 'Co. code'], I.variants.slice(0, idMax).map((x) => `<tr>${td(esc(x.sap))}${td(`<b>${esc(x.main)}</b>`)}${td(x.others.map((o) => `${esc(o.name)} (${o.n})${o.odd ? ` <span style="color:${C.bad};font-size:11px">– very different name, check the SAP code</span>` : ''}`).join('; '))}${td(esc(x.ccs.join(', ')))}</tr>`)));
  out.push(h(`Look-alike names in the same company code (${int(I.lookAlikeAll)})`, 'Names that differ only by a typo or punctuation – not joined automatically; please check'));
  out.push(table(['Co. code', 'Name 1 (invoices)', 'Name 2 (invoices)', 'Check'], I.lookAlike.slice(0, idMax).map((x) => `<tr>${td(esc(x.cc))}${td(`${esc(x.a)} (${int(x.an)})`)}${td(`${esc(x.b)} (${int(x.bn)})`)}${td(`<span style="font-size:11px;color:${/check/.test(x.kind) ? C.warn : C.mute}">${esc(x.kind)}</span>`)}</tr>`)));
  if (I.lookAlikeAll > Math.min(idMax, I.lookAlike.length)) out.push(note(`${int(I.lookAlikeAll - Math.min(idMax, I.lookAlike.length))} more – dashboard.html lists them.`));

  // 8. pending reason wording
  out.push(sec(8, 'Pending reasons – tracker wording → standard category', 'The tracker\'s own words, and the one standard category each was put under'));
  out.push(table(['Standard category', 'Root cause', 'Invoices', 'Tracker wording (invoices)'], a.wording.map((x) =>
    `<tr>${td(`<b>${esc(x.key)}</b>`)}${td(esc(x.group))}${td(int(x.n), 1)}${td(`<span style="font-size:11px">${esc(x.wordings.slice(0, web ? 40 : 8).map((w) => `${w.key} (${w.n})`).join(' · '))}${x.wordings.length > (web ? 40 : 8) ? ` · +${x.wordings.length - (web ? 40 : 8)} more` : ''}</span>`)}</tr>`)));

  // 9. data quality
  out.push(sec(9, 'Data quality', 'Entries to fill in or correct in the tracker'));
  out.push(`<ul style="font-size:12px;margin:0;padding-left:18px">
${a.quality.fillIn.map((x) => `<li style="color:${C.warn}"><b>${int(x.n)} – ${esc(x.label)}</b> (e.g. ${esc(x.examples.join(', '))})</li>`).join('')}
<li>${int(a.quality.noValue)} invoices without a value</li>
<li>${a.quality.repeated.length ? `${a.quality.repeated.length} invoice numbers appear more than once: ${esc(a.quality.repeated.slice(0, 10).join(', '))}${a.quality.repeated.length > 10 ? ' …' : ''}` : 'No repeated invoice numbers'}</li>
${a.quality.problems.map((e) => `<li style="color:${C.warn}">Check the data: ${e.values.length} ${esc(e.child)}(s) appear under more than one ${esc(e.parent)} (${esc(e.values.slice(0, 5).join(', '))}${e.values.length > 5 ? ' …' : ''})</li>`).join('')}
</ul>
<p style="color:#9ca3af;font-size:11px;margin-top:22px">Generated by n8n from the Production Tracker data table. Period volume uses the received date (allocated, then invoice date when it is missing); TAT always uses the received date.</p>
</div>`);
  return out.join('\n');
}

// ---------- main ----------
const settings = $('Report Settings').first().json;
const seen = new Map(); // one row per invoice (last row wins)
for (const { json: r } of $('Get All Rows').all()) {
  const d = r.Received_Date || r.Allocated_Date || r.Invoice_Date || '';
  seen.set(String(r.Invoice ?? r.id), {
    i: r.Invoice, d: String(d).slice(0, 10), rd: String(r.Received_Date || '').slice(0, 10), ad: String(r.Allocated_Date || '').slice(0, 10),
    c: String(r.Customer || 'UNKNOWN CUSTOMER').replace(/\s+/g, ' ').trim().toUpperCase(), cc: String(r.Company_Code || '').trim().toUpperCase(),
    pm: String(r.Project_Manager || '').trim(), p: String(r.Name_the_PortalEmail_ID || '').trim(), v: r.Value,
    sap: String(r.SAP_Customer_Code || '').trim(), pc: String(r.Profit_Center || '').trim().toUpperCase(),
    so: String(r.Sales_Org || '').trim().toUpperCase(),
    pl: String(r.Product_Line || '').trim().toUpperCase(), bt: String(r.Business_Type || '').trim().toUpperCase(),
    st: String(r.Status || '').trim(), ud: String(r.Upload_Date || '').slice(0, 10), ub: String(r.Uploaded_By || '').trim(),
    cat: String(r.Pending_Category || '').trim(), sc: String(r.Standard_Category || '').trim(),
    // the reason text is only kept for open items (keeps the dashboard small)
    why: /pend|hold|open|progress|query|block/i.test(String(r.Status || '')) ? String(r.Pending_Reason || '').trim() : '',
  });
}
const rows = [...seen.values()];
const a = analyse(rows, settings, RULES);
const html = render(a, false);

const recipients = String(settings.sendTo || '').trim() || RECIPIENTS.filter((x) => String(x).trim()).join(', ');
if (!recipients) throw new Error('Add at least one email address to RECIPIENTS at the top of "Build Report".');

const safeJson = (x) => JSON.stringify(x).replace(/</g, '\\u003c');
const listOf = (f) => [...new Set(rows.map(f).filter(Boolean))].sort();
const options = (list) => list.map((c) => `<option>${String(c).replace(/[&<>"]/g, '')}</option>`).join('');
const dashboard = `<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Invoice Distribution Dashboard</title></head><body style="margin:0;padding:18px;background:#fff">
<!--charts-->
<div style="font-family:Segoe UI,Arial,sans-serif;font-size:13px;background:#f3f4f6;padding:12px;border-radius:6px;margin-bottom:12px;max-width:1180px">
<b>Choose:</b> Report <select id="t"><option>Overview</option><option>Weekly</option><option>Monthly</option><option>Custom period</option></select>
From <input id="f" type="date"> To <input id="o" type="date">
Company code <select id="cc"><option value="">All</option>${options(listOf((r) => r.cc))}</select>
Profit centre <select id="pc"><option value="">All</option>${options(listOf((r) => r.pc || (r.cc === 'G367' ? 'N/A – CLEARWATER' : 'NOT FOUND')))}</select>
Product line <select id="pl"><option value="">All</option>${options(listOf((r) => r.pl || 'NOT FOUND'))}</select>
Customer or SAP code <input id="cu" size="18"> <button id="go">Show</button></div>
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
  $id('out').innerHTML = render(analyse(ROWS, opts, RULES), true);
}
const start = ${safeJson({ type: settings.type || 'Overview', from: settings.from || '', to: settings.to || '', companyCode: settings.companyCode || '', customer: settings.customer || '' })};
$id('t').value = start.type; $id('f').value = start.from; $id('o').value = start.to; $id('cc').value = start.companyCode.toUpperCase(); $id('cu').value = start.customer;
$id('go').onclick = show; show();
</script></body></html>`;

const quality = (() => { try { return $('Summarise Upload').first().json.message; } catch (e) { return ''; } })();

// Compact facts for the AI steps (the AI may only use these figures)
const r2 = (x) => (x === null || x === undefined ? null : Math.round(x * 100) / 100);
const p1 = (x) => (x === null || x === undefined ? null : Math.round(x * 1000) / 10);
const facts = a.empty ? { empty: true } : (() => {
  const K = a.kpis; const P = a.pending; const V = a.volume; const T = a.tat;
  const nv = (v) => parseFloat(String(v ?? '').replace(/[^0-9.\-]/g, '')) || 0;
  const st = (x) => ({ received: x.received, receivedValue: r2(x.receivedV), submitted: x.submitted, within24hPercent: p1(x.slaPct), within24h: x.met, over24h: x.missed,
    avgTatDays: r2(x.avgTat), open: x.open, openValue: r2(x.openV), followUpDue: x.due, oldestDaysPending: x.oldest });
  return {
    focus: 'invoice distribution',
    period: `${a.from} to ${a.to}`, daysCountedTo: a.today,
    rules: { tat: 'received date to submission (upload) date; open invoices count to today', within24h: 'submitted on the received date or the next day', followUpDueAfterDays: P.rules.followUpDays },
    scope: { companyCode: a.cc || 'all', profitCentre: a.pcSel || 'all', productLine: a.plSel || 'all', customer: a.cust || 'all' },
    totals: { ...st(K), perWorkingDay: r2(K.perWorkDay), vsPreviousPeriodPercent: p1(K.change), previousPeriodReceived: K.prevReceived, submittedInPeriod: K.submittedInPeriod,
      medianTatDays: r2(K.medTat), stillWithin24hOpen: K.window, tatUnknown: K.unknown, oursToActOn: K.oursOpen, portalAccessOpen: K.portalAccessOpen },
    volume: { last12Months: V.last12, monthlyAverage: r2(V.monthlyAvg), busiestMonth: V.busiest ? { month: V.busiest.key, received: V.busiest.n } : null,
      months: V.months.map((m) => ({ month: m.key, received: m.n, monthToDate: m.partial || undefined, byArea: Object.fromEntries(a.areas.map((ar, i) => [ar, m.areas[i]])) })),
      channels: V.channels.map((x) => ({ channel: x.key, received: x.n })) },
    byArea: a.byArea.map((x) => ({ area: x.key, ...st(x), companyCodes: x.codes.map((c) => ({ companyCode: c.key, ...st(c) })) })),
    tat: { buckets: T.buckets.map((b) => ({ bucket: b.key, invoices: b.n })), weeklyWithin24hPercent: V.weeks.map((w) => ({ weekStarting: w.key, received: w.n, within24hPercent: p1(w.slaPct) })) },
    pending: {
      whoActs: P.byFix.map((x) => ({ who: x.key, open: x.n, value: r2(x.v), followUpDue: x.due, oldest: x.oldest, rootCauses: x.causes })),
      rootCauses: P.rootCauses.map((g) => ({ rootCause: g.key, whoActs: g.fix, open: g.n, value: r2(g.v), followUpDue: g.due, avgDaysPending: r2(g.avgAge), oldest: g.oldest,
        where: g.where.slice(0, 5), categories: g.categories.filter((c) => c.key).slice(0, 5).map((c) => ({ category: c.key, open: c.n, where: c.where.slice(0, 3) })) })),
      oldestOpen: [...P.list].sort((x, y) => (y.age ?? -1) - (x.age ?? -1)).slice(0, 8).map((r) => ({ invoice: String(r.i), area: r.area, companyCode: r.cc, customer: r.cl,
        value: r2(nv(r.v)), daysPending: r.age, rootCause: r.blocker, category: r.category || null, lastAction: r.last, daysSinceLastAction: r.sinceLast, followUps: r.followUps, owner: r.ub || null })),
      followUpDueByOwner: P.owners.map((x) => ({ owner: x.key, followUpDue: x.n })),
    },
    profitCentres: a.profitCentres.slice(0, 12).map((x) => ({ profitCentre: x.key, companyCodes: x.codes, received: x.received, sharePercent: p1(x.share), within24hPercent: p1(x.slaPct), open: x.open, openValue: r2(x.openV), mainRootCause: x.cause || null })),
    companyCodes: a.companies.map((x) => ({ companyCode: x.key, area: x.area, ...st(x), rootCauses: x.causes.slice(0, 3),
      topCustomers: x.customers.slice(0, 4).map((c) => ({ customer: c.label, received: c.received, sharePercent: p1(c.share), within24hPercent: p1(c.slaPct), open: c.open })) })),
    customerNames: { sameNameDifferentSapCodes: a.identity.sameName.length, oneSapCodeSeveralSpellings: a.identity.variants.length, lookAlikeNamesToCheck: a.identity.lookAlikeAll,
      examples: [...a.identity.variants.slice(0, 2).map((x) => `SAP ${x.sap} shown as ${x.main}, also written as ${x.others.slice(0, 2).map((o) => o.name).join(' / ')}`),
        ...a.identity.sameName.slice(0, 2).map((x) => `${x.key} has SAP codes ${x.codes.map((c) => c.sap).join(', ')}`)] },
    dataGaps: a.quality.fillIn.map((x) => ({ issue: x.label, count: x.n, examples: x.examples.slice(0, 3) })),
    // datasets for the chart designer
    charts: {
      receivedByArea: a.byArea.map((x) => ({ area: x.key, received: x.received, value: r2(x.receivedV) })),
      receivedByCompanyCode: a.companies.map((x) => ({ companyCode: x.key, received: x.received, value: r2(x.receivedV) })),
      receivedByProfitCentre: a.profitCentres.map((x) => ({ profitCentre: x.key, received: x.received, value: r2(x.receivedV) })),
      monthlyIncoming: V.months.map((m) => ({ month: m.key, received: m.n, value: r2(m.v), monthToDate: m.partial || undefined })),
      weeklyIncoming: V.weeks.map((w) => ({ weekStarting: w.key, received: w.n, value: r2(w.v) })),
      weeklyWithin24h: V.weeks.filter((w) => w.slaPct !== null).map((w) => ({ weekStarting: w.key, percent: p1(w.slaPct) })),
      within24hByCompanyCode: T.byCode.filter((x) => x.slaPct !== null).map((x) => ({ companyCode: x.key, percent: p1(x.slaPct) })),
      tatBuckets: T.buckets.map((b) => ({ bucket: b.key, invoices: b.n })),
      openByArea: a.byArea.map((x) => ({ area: x.key, open: x.open, value: r2(x.openV) })),
      openByCompanyCode: a.companies.map((x) => ({ companyCode: x.key, open: x.open, value: r2(x.openV) })),
      openByProfitCentre: a.profitCentres.filter((x) => x.open).map((x) => ({ profitCentre: x.key, open: x.open, value: r2(x.openV) })),
      whoActs: P.byFix.map((x) => ({ who: x.key, open: x.n, value: r2(x.v) })),
      rootCauses: P.rootCauses.map((g) => ({ rootCause: g.key, open: g.n, value: r2(g.v) })),
      ageing: P.ageing.map((b) => ({ bucket: b.key, open: b.n, value: r2(b.v) })),
      channels: V.channels.map((x) => ({ channel: x.key, received: x.n })),
    },
  };
})();
const uploadNote = quality
  ? `<p style="font-family:Segoe UI,Arial,sans-serif;font-size:12px;color:#374151;background:#f3f4f6;padding:8px 12px;max-width:860px"><b>Upload result:</b> ${quality.replace(/[&<>]/g, '')}</p>`
  : '';
const K = a.kpis || {};
const subject = `Invoice distribution – ${a.label || ''} – ${K.received ?? 0} received, ${K.slaPct === null || K.slaPct === undefined ? '–' : Math.round(100 * K.slaPct) + '%'} within 24 h, ${K.open ?? 0} open (${K.due ?? 0} follow-up due)`;
return [{
  json: {
    to: recipients,
    subject,
    facts: JSON.stringify(facts),
    html: '<!--charts-->' + html + uploadNote + '<p style="font-family:Segoe UI,Arial,sans-serif;font-size:12px;color:#6b7280">The attached dashboard.html has the same report with interactive charts and every row; you can change the period, company code, profit centre, product line and customer. Open it in your browser.</p>',
    doneMessage: (quality ? quality + '. ' : '') + `Report "${a.label || ''}" sent to ${recipients}.`,
  },
  binary: {
    dashboard: { data: Buffer.from(dashboard, 'utf8').toString('base64'), mimeType: 'text/html', fileName: 'dashboard.html', fileExtension: 'html' },
  },
}];
