// Split Invoice Numbers — one item per invoice number typed in the form (any separator, spaces inside are fine)
const typed = String($input.first().json['Invoice numbers'] ?? '');
const numbers = [...new Set(
  typed.split(/[\n,;]+/).map((s) => s.replace(/\D/g, '')).filter((s) => s.length >= 5),
)];
if (!numbers.length) throw new Error('Enter at least one invoice number (one per line, or separated by commas).');
if (numbers.length > 25) throw new Error(`${numbers.length} invoice numbers entered – please request 25 or fewer at a time.`);
return numbers.map((invoice) => ({ json: { invoice } }));
