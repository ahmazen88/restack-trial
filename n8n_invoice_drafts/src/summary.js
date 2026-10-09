// Summary — what happened, for the Done page
const drafts = $('Build Drafts').all().map((i) => i.json);
const problems = $('Pick Invoice Files').first().json.problems || [];
const unverified = drafts.filter((d) => !d.verified).map((d) => d.invoice);
const parts = [`${drafts.length} draft email(s) sent to ${drafts[0]?.to}: ${drafts.map((d) => d.invoice).join(', ')}`];
if (unverified.length) parts.push(`Check the attachment for: ${unverified.join(', ')} (number not found inside the PDF)`);
if (problems.length) parts.push(`Not prepared: ${problems.join(' · ')}`);
return [{ json: { message: parts.join('. ') + '.' } }];
