// Standard Blockers — puts every pending reason into ONE fixed list of categories, so the same problem always gets
// the same wording. Order of use: 1) the fixed rules below, 2) the category saved for the same wording on an earlier
// upload, 3) only what is still unknown goes to "AI Blocker Classifier", which may only pick from the same list.
// Each category belongs to one group (the level above it in the report).
const CATEGORIES = {
  'PO not available on portal': 'PO issue on portal',
  'PO lines not available on portal': 'PO issue on portal',
  'PO cancelled or closed': 'PO issue on portal',
  'PO line and invoice line mismatch': 'Invoice vs PO mismatch',
  'Price and quantity mismatch': 'Invoice vs PO mismatch',
  'Quantity mismatch': 'Invoice vs PO mismatch',
  'Price mismatch': 'Invoice vs PO mismatch',
  'Amount or freight mismatch': 'Invoice vs PO mismatch',
  'Tax or exemption mismatch': 'Tax / exemption',
  'No portal access / portal migration': 'Portal access',
  'Unable to submit invoice on portal': 'Submission issue',
  Other: 'Other',
};
// first matching rule wins (checked on the Category text, then on the reason)
const RULES = [
  [/cancel|po closed|closed po/i, 'PO cancelled or closed'],
  [/\bpo\b.*line.*(not match|mismatch|differ)|line.*(not match|mismatch).*\bpo\b|po line and invoice line/i, 'PO line and invoice line mismatch'],
  [/(price|unit price).*(quantity|qty)|(quantity|qty).*price/i, 'Price and quantity mismatch'],
  [/quantity|qty/i, 'Quantity mismatch'],
  [/price/i, 'Price mismatch'],
  // tax charged / not charged, exemption certificate, GST / HST / QST / PST: its own root cause (needs a certificate or the GE tax team)
  [/\btax|\bexempt|exemption|\bgst\b|\bhst\b|\bqst\b|\bpst\b|\bvat\b/i, 'Tax or exemption mismatch'],
  [/amount|tariff|freight|variance|mismatch/i, 'Amount or freight mismatch'],
  [/\bpo lines?\b.*(unavailable|not available|missing|not found)|(unavailable|not available|missing).*\bpo lines?\b/i, 'PO lines not available on portal'],
  [/\bpo\b|purchase order/i, 'PO not available on portal'],
  [/access|migrat|coupa|oracle|ariba|login|regist/i, 'No portal access / portal migration'],
  [/(unable|cannot|can not|not able)\b.*invoice/i, 'Unable to submit invoice on portal'],
];
const VAGUE = 'Unable to submit invoice on portal'; // a symptom: if the reason names the cause, the cause wins

const isOpen = (s) => /pend|hold|open|progress|query|block/i.test(String(s || ''));
const textKey = (r) => `${r.Pending_Category || ''} | ${r.Pending_Reason || ''}`.toLowerCase().replace(/\s+/g, ' ').trim();
const byRule = (t) => (t ? (RULES.find(([re]) => re.test(t)) || [])[1] || null : null);

// categories saved on earlier uploads, by wording (read by "Check Table" before anything is changed)
const remembered = new Map();
for (const { json: t } of $('Check Table').all()) {
  if (t && t.Standard_Category && CATEGORIES[t.Standard_Category] && (t.Pending_Category || t.Pending_Reason)) remembered.set(textKey(t), t.Standard_Category);
}

const result = {}; // invoice → { category, how }
const unknown = new Map(); // wording → id for the AI
for (const { json: r } of $('Clean Rows').all()) {
  if (!isOpen(r.Status) || !(r.Pending_Category || r.Pending_Reason)) continue;
  const fromCategory = byRule(r.Pending_Category);
  const fromReason = byRule(r.Pending_Reason);
  let cat = fromCategory && fromCategory !== VAGUE ? fromCategory : (fromReason && fromReason !== VAGUE ? fromReason : fromCategory || fromReason);
  let how = 'rule';
  if (!cat && remembered.has(textKey(r))) { cat = remembered.get(textKey(r)); how = 'earlier upload'; }
  if (!cat) {
    if (!unknown.has(textKey(r))) unknown.set(textKey(r), { id: unknown.size + 1, text: `${r.Pending_Category || ''} — ${r.Pending_Reason || ''}`.slice(0, 220) });
    how = 'ai';
  }
  result[String(r.Invoice)] = { category: cat, how, key: textKey(r) };
}
const items = [...unknown.values()].slice(0, 80); // more than 80 new wordings in one upload: the rest become "Other"
return [{
  json: {
    categories: Object.keys(CATEGORIES), groups: CATEGORIES, result,
    keyToId: Object.fromEntries([...unknown].map(([k, v]) => [k, v.id])),
    items: JSON.stringify(items), itemCount: items.length,
  },
}];
