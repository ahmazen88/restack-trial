// Pick Invoice Files — for each requested number, choose exactly one PDF from the Box search results.
// 1) a single PDF whose file name contains the number, or 2) the only search result (Box also searches inside PDFs).
// Anything else (none, or several) is reported and skipped. The number is checked again inside the PDF later.
const requested = $('Split Invoice Numbers').all().map((i) => i.json.invoice);
const results = requested.map(() => []);
for (const item of $input.all()) {
  const f = item.json;
  if (!f || !f.id || f.type !== 'file') continue;
  const idx = item.pairedItem?.item ?? item.pairedItem?.[0]?.item;
  if (idx !== undefined && results[idx]) results[idx].push(f);
}
const out = [];
const problems = [];
requested.forEach((invoice, i) => {
  const exact = new RegExp(`(^|\\D)${invoice}(\\D|$)`);
  const pdfs = results[i].filter((f) => /\.pdf$/i.test(f.name || ''));
  const byName = pdfs.filter((f) => exact.test(f.name));
  const pick = byName.length === 1 ? byName[0] : byName.length === 0 && pdfs.length === 1 ? pdfs[0] : null;
  if (pick) out.push({ json: { invoice, id: pick.id, fileName: pick.name, folder: pick.path_collection?.entries?.map((e) => e.name).join(' / ') || '' } });
  else if (!pdfs.length) problems.push(`${invoice}: no PDF found in Box`);
  else problems.push(`${invoice}: ${byName.length || pdfs.length} possible files (${(byName.length ? byName : pdfs).map((f) => f.name).slice(0, 5).join(', ')})`);
});
if (!out.length) throw new Error(`No invoice could be prepared. ${problems.join(' · ')}`);
out[0].json.problems = problems; // reported on the Done page
return out;
