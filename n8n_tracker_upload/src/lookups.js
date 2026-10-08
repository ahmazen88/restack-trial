// Add Lookups — fill SAP customer code and profit centre from the ZSD log and the Tableau extract.
// Matching is on invoice number only. Nothing is guessed: no match = the value stays empty.
// Values found on an earlier upload are kept, so an invoice that is no longer in a later Tableau extract keeps its codes.
const PROFIT_CENTRE_COMPANY_CODES = ['3060', '3487', '3485']; // profit centre only applies to these
// Clearwater (G367) invoices are not in Tableau: they all get these fixed values
const CLEARWATER = { companyCode: 'G367', Product_Line: 'PQP', Business_Type: 'MANUFACTURING' };
const SOURCES = [ // the read steps, in order of preference for the SAP customer code
  { step: 'Read ZSD Log', label: 'ZSD' },
  { step: 'Read ZSD 2025 Sheet', label: 'ZSD' },
  { step: 'Read Tableau Extract', label: 'Tableau' },
];

const norm = (s) => String(s ?? '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
// cleaned value for matching: "0007001212645", " 7,001,212,645 ", "'7001212645" and 7001212645.0 all become 7001212645
const key = (v) => {
  let t = String(v ?? '').trim().replace(/^'/, '').replace(/\.0+$/, '');
  if (/^[\d\s,]+$/.test(t)) t = t.replace(/[\s,]/g, '').replace(/^0+(?=\d)/, '');
  return t;
};
const tidy = (v) => String(v ?? '').replace(/\s+/g, ' ').trim().toUpperCase(); // profit centre as text, e.g. GPJ908
const rows = $('Clean Rows').all().map((i) => ({ ...i.json, SAP_Customer_Code: null, Profit_Center: null, Product_Line: null, Business_Type: null }));
const wanted = new Set(rows.map((r) => key(r.Invoice)));

// rows from one read step (a missing file or sheet gives an error item, which is skipped)
const readRows = (step) => {
  try { return $(step).all().map((i) => i.json).filter((j) => j && !j.error && Object.keys(j).length > 1); }
  catch (e) { return []; }
};
// the column whose values match the most tracker invoice numbers is the invoice column
const invoiceColumn = (data) => {
  const hits = {};
  for (const r of data) for (const [h, v] of Object.entries(r)) if (wanted.has(key(v))) hits[h] = (hits[h] || 0) + 1;
  return Object.entries(hits).sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))[0]?.[0] ?? null;
};
// the column that passes `test` for the most rows
const columnBy = (data, test) => {
  const counts = {};
  for (const r of data) for (const [h, v] of Object.entries(r)) if (test(norm(h), v) && key(v)) counts[h] = (counts[h] || 0) + 1;
  return Object.entries(counts).sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))[0]?.[0] ?? null;
};
const isCustomerCode = (h, v) => /customer|sold to|payer/.test(h) && !/name|key|group|country|type/.test(h)
  && /^[A-Za-z]?\d{3,}$/.test(key(v)); // e.g. 89598 or 160026
const isProfitCentre = (h) => /profit/.test(h);
const isProductLine = (h) => /product/.test(h) && !/desc|name/.test(h); // e.g. PTI, AIS, PTR, GIS
const isBusinessType = (h) => /nature|business type|type of business/.test(h); // e.g. Manufacturing / Services / Trading

const found = { customer: new Map(), profit: new Map(), product: new Map(), business: new Map() };
const notes = [];
for (const { step, label } of SOURCES) {
  const data = readRows(step);
  if (!data.length) continue;
  const inv = invoiceColumn(data);
  if (!inv) { notes.push(`${step}: no invoice numbers matched the tracker`); continue; }
  const cust = columnBy(data, isCustomerCode);
  const prof = label === 'Tableau' ? columnBy(data, isProfitCentre) : null;
  // a heading with "line" in it wins for product line ("Product Line" over "Product")
  const prod = label === 'Tableau' ? (columnBy(data, (h) => isProductLine(h) && /line/.test(h)) || columnBy(data, isProductLine)) : null;
  const biz = label === 'Tableau' ? columnBy(data, isBusinessType) : null;
  let matched = 0;
  for (const r of data) {
    const k = key(r[inv]);
    if (!wanted.has(k)) continue;
    matched++;
    if (cust && key(r[cust]) && !found.customer.has(k)) found.customer.set(k, key(r[cust]));
    if (prof && key(r[prof]) && !found.profit.has(k)) found.profit.set(k, tidy(r[prof]));
    if (prod && key(r[prod]) && !found.product.has(k)) found.product.set(k, tidy(r[prod]));
    if (biz && key(r[biz]) && !found.business.has(k)) found.business.set(k, tidy(r[biz]));
  }
  notes.push(`${step}: ${matched} matching rows (invoice column "${inv}"` +
    (cust ? `, customer code "${cust}"` : ', no customer code column found') +
    (label === 'Tableau' ? `, profit centre ${prof ? `"${prof}"` : 'not found'}, product line ${prod ? `"${prod}"` : 'not found'}` +
      `, business type ${biz ? `"${biz}"` : 'not found'})` : ')'));
}

// values saved on earlier uploads (read by "Check Table" before anything is changed)
const before = new Map();
for (const { json: t } of $('Check Table').all()) if (t && t.Invoice != null) before.set(key(t.Invoice), t);

for (const r of rows) {
  const k = key(r.Invoice);
  const old = before.get(k) || {};
  r.SAP_Customer_Code = found.customer.get(k) ?? old.SAP_Customer_Code ?? null;
  r.Profit_Center = PROFIT_CENTRE_COMPANY_CODES.includes(String(r.Company_Code))
    ? (found.profit.get(k) ?? old.Profit_Center ?? null) : null;
  if (String(r.Company_Code) === CLEARWATER.companyCode) {
    r.Product_Line = CLEARWATER.Product_Line;
    r.Business_Type = CLEARWATER.Business_Type;
  } else {
    r.Product_Line = found.product.get(k) ?? old.Product_Line ?? null;
    r.Business_Type = found.business.get(k) ?? old.Business_Type ?? null;
  }
}
// which columns were used is shown on the Done page; "_lookupNotes" is removed again before saving
if (rows.length) rows[0]._lookupNotes = notes.length ? notes.join(' · ') : 'no ZSD log or Tableau extract uploaded';
return rows.map((json) => ({ json }));
