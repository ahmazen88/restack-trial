// Add AI Commentary — put the AI's commentary above the fixed report. The figures in the report itself never come
// from the AI. If the AI step failed or returned nothing usable, the report is sent without commentary.
const base = $('Build Report').first();
const raw = String($input.first().json.text ?? $input.first().json.output ?? '');
const ALLOWED = ['h3', 'h4', 'p', 'ul', 'ol', 'li', 'b', 'strong', 'i', 'em', 'br'];

let ai = raw.replace(/```[a-z]*\n?/gi, '').replace(/<(script|style)[\s\S]*?<\/\1>/gi, '');
ai = ai.replace(/<\/?([a-z0-9]+)\b[^>]*>/gi, (tag, name) =>
  ALLOWED.includes(name.toLowerCase()) ? tag.replace(/\s[^>]*?(\/?)>$/, '$1>') : '');
if (!/<(p|li|h3)>/i.test(ai)) {
  ai = ai.split(/\n\s*\n/).map((p) => p.trim()).filter(Boolean).map((p) => `<p>${p.replace(/[&<>]/g, '')}</p>`).join('');
}

if (ai.replace(/<[^>]+>/g, '').trim().length < 40) {
  return [{ json: { ...base.json, aiUsed: false }, binary: base.binary }];
}
const box = '<div style="border-left:4px solid #2b6cb0;background:#f0f6ff;padding:10px 16px;margin:0 0 18px;' +
  'font-family:Segoe UI,Arial,sans-serif;font-size:13px;color:#111827;max-width:860px">' +
  '<div style="font-size:11px;color:#6b7280;margin-bottom:4px">AI commentary – written from the figures in this ' +
  'report. Check before acting.</div>' + ai + '</div>';
return [{ json: { ...base.json, html: box + base.json.html, aiUsed: true }, binary: base.binary }];
