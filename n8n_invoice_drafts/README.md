# Invoice Drafts – Box to my inbox

Enter invoice numbers in a form. For each one, n8n searches **all of Box** for the PDF, reads it, and emails
**you** a ready-to-forward draft with the PDF attached. Nothing is sent to customers.

```
Request Invoices (form) → Split Invoice Numbers → Search Box → Pick Invoice Files → Download Invoice
  → Read Invoice PDF → Build Drafts → [GEV Send Email → you] → Summary → Done Page
```

## Safety
- Drafts go only to you (`SEND_DRAFTS_TO` in **Build Drafts**, or the address typed in the form).
- **No guessing:** a PDF is used only if exactly one file name contains the number, or the search returns exactly
  one PDF. Two candidates means it's reported, not picked.
- The invoice number is checked **inside** the PDF. If it isn't there, the draft says "CHECK ATTACHMENT" in red.
- Values read from the PDF (date, amount, currency, PO, due date, customer) are shown at the top of the draft;
  anything not found is marked "not found – please check".
- At most 25 invoice numbers per request.

## Setup (one time)
1. Import `invoice_drafts_workflow.json`.
2. **Search Box** and **Download Invoice**: choose your working Box credential.
3. **Build Drafts**: your email in `SEND_DRAFTS_TO`.
4. Replace the grey **Send Draft to Me – paste GEV Send Email here** with the *Send an Email* node from *Report
   copy*: connect Build Drafts → it → Summary, then set To `{{ $json.to }}`, Subject `{{ $json.subject }}`,
   Email Format HTML, HTML `{{ $json.html }}`, Attachments `data`.
5. Publish and open the form (Request Invoices → Production URL).

## Notes
- Box can take a few minutes to make newly uploaded files searchable.
- The PDF reading uses generic labels ("Invoice Date", "Total Amount Due", "Purchase Order", "Bill To"…). Once a
  real invoice has been seen, the labels in **Build Drafts** can be tuned to its exact layout.

Edit `src/*.js`, run `python3 build.py`, test with `node test/run.js`.
