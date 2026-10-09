// Build Drafts — read each invoice PDF and prepare a draft email for YOU to check and forward.
// Fixed rules only. Values not found on the PDF are shown as "not found" for you to fill in.
const SEND_DRAFTS_TO = ''; // your email address, e.g. 'name.surname@company.com' (the form can override)

const formTo = (() => { try { return String($('Request Invoices').first().json['Send drafts to (optional)'] || '').trim(); } catch (e) { return ''; } })();
const to = formTo || SEND_DRAFTS_TO;
if (!to) throw new Error('Add your email address to SEND_DRAFTS_TO at the top of "Build Drafts".');

const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const find = (text, labels, valuePattern) => {
  for (const label of labels) {
    const m = text.match(new RegExp(`${label}\\s*[:#.]?\\s*(${valuePattern})`, 'i'));
    if (m) return m[1].trim();
  }
  return '';
};
const DATE = '\\d{1,2}[./-]\\d{1,2}[./-]\\d{2,4}|\\d{4}-\\d{2}-\\d{2}|\\d{1,2}[ -][A-Za-z]{3,9}[ -,]+\\d{4}|[A-Za-z]{3,9} \\d{1,2},? \\d{4}';
const MONEY = '(?:[A-Z]{3}\\s*)?[$€£]?\\s*-?\\d{1,3}(?:[,.\\s]\\d{3})*(?:[.,]\\d{2})?';

const drafts = [];
for (let i = 0; i < $input.all().length; i++) {
  const item = $input.all()[i];
  const picked = $('Pick Invoice Files').itemMatching(i).json;
  const text = String(item.json.text || '').replace(/\r/g, '');
  const flat = text.replace(/\s+/g, ' ');
  const numberOnPdf = text.replace(/\D/g, '').includes(picked.invoice);

  const lines = text.split('\n').map((l) => l.trim()).filter(Boolean);
  const billIdx = lines.findIndex((l) => /^(bill\s*to|sold\s*to|customer)\b/i.test(l));
  const customer = billIdx >= 0 ? (lines[billIdx].replace(/^(bill\s*to|sold\s*to|customer)\s*[:.]?\s*/i, '') || lines[billIdx + 1] || '') : '';
  const facts = {
    'Invoice date': find(flat, ['invoice date', 'date of invoice', 'document date', 'date'], DATE),
    'Amount': find(flat, ['total amount due', 'amount due', 'invoice total', 'total due', 'grand total', 'total amount', 'total'], MONEY),
    'Currency': (flat.match(/\b(USD|CAD|EUR|GBP|INR|AUD|SAR|AED|QAR)\b/) || [''])[0],
    'PO number': find(flat, ['purchase order(?: no\\.?| number)?', 'p\\.?o\\.?(?: no\\.?| number)?', 'your order'], '[A-Z0-9][A-Z0-9-/]{3,}'),
    'Due date': find(flat, ['due date', 'payment due'], DATE),
    'Customer': customer.slice(0, 80),
  };
  const shown = (v) => (v ? esc(v) : '<span style="color:#b91c1c">not found – please check</span>');
  const check = numberOnPdf
    ? '<span style="color:#047857">✔ Invoice number found inside the PDF</span>'
    : '<span style="color:#b91c1c"><b>⚠ Invoice number NOT found inside the PDF – check the attachment before forwarding</b></span>';

  const html = `<div style="font-family:Segoe UI,Arial,sans-serif;font-size:14px;color:#111827;max-width:720px">
<div style="border:2px dashed #b45309;background:#fffbeb;padding:10px 14px;margin-bottom:16px;font-size:13px">
<b>DRAFT – not sent to the customer.</b> Check it, then forward to the customer's distribution address.<br>
${check}<br>File: ${esc(picked.fileName)}${picked.folder ? ` (Box: ${esc(picked.folder)})` : ''}<br>
<table style="margin-top:6px;font-size:13px">${Object.entries(facts).map(([k, v]) => `<tr><td style="padding:1px 10px 1px 0;color:#6b7280">${k}</td><td>${shown(v)}</td></tr>`).join('')}</table></div>
<p>Dear Accounts Payable team,</p>
<p>Please find attached invoice <b>${esc(picked.invoice)}</b>${facts['Invoice date'] ? ` dated ${esc(facts['Invoice date'])}` : ''}${facts.Amount ? ` for ${esc([facts.Currency, facts.Amount].filter(Boolean).join(' '))}` : ''}${facts['PO number'] ? `, referencing PO ${esc(facts['PO number'])}` : ''}.</p>
<p>Please let us know if you need anything further.</p>
<p>Kind regards,</p>
</div>`;

  drafts.push({
    json: {
      to,
      subject: `DRAFT – Invoice ${picked.invoice}${facts.Customer ? ` – ${facts.Customer}` : ''}${numberOnPdf ? '' : ' – CHECK ATTACHMENT'}`,
      html,
      invoice: picked.invoice,
      verified: numberOnPdf,
    },
    binary: item.binary, // the invoice PDF, attached to the draft
  });
}
return drafts;
