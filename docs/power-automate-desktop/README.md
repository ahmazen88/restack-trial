# Power Automate for desktop — function reference

This folder is a working catalog of **every usable item** in Power Automate for desktop (PAD): designer surfaces, native actions, default cloud connector operations, Power Fx functions, and variable data types.

It is original reference text built from the product surface area (action names, modules, inputs, outputs). Parameter tables on Microsoft Learn remain the authoritative source for long descriptions.

## Read this in order

1. **Identify everything (step 1):** [00-inventory.md](00-inventory.md)  
   Complete list with counts. Machine-readable: [inventory.json](inventory.json).
2. **Designer items:** [01-designer-usable-items.md](01-designer-usable-items.md)
3. **Data types:** [02-data-types.md](02-data-types.md)
4. **Power Fx functions:** [03-power-fx-functions.md](03-power-fx-functions.md)
5. **Classic `%` expressions:** [04-expression-syntax.md](04-expression-syntax.md)
6. **Each function / action (reference):** [modules/](modules/) — purpose, inputs, outputs, exceptions.
7. **How each function works:** [05-how-each-function-works.md](05-how-each-function-works.md) — use case, demonstration, analogy for every item.
8. **In combination:** [06-combination-playbooks.md](06-combination-playbooks.md) — 19 end-to-end playbooks.
9. **Portal uploads (Ariba-like):** [07-portal-uploads-ariba.md](07-portal-uploads-ariba.md) — HTML file input vs Windows Open dialog, iframes, submit, confirmation.

## Counts (current catalog)

| Kind | Count |
| --- | ---: |
| Native designer actions | 448 |
| Default cloud connector operations | 185 |
| Power Fx functions | 130 |
| Designer / console usable items | 35 |
| Variable data types | 39 |
| Native action modules | 50 |

Cloud connector operations change as Microsoft ships connector updates. Add more connectors from the **Assets library**. The 185 operations documented here are the default pane set (SharePoint, Outlook, Teams, Dataverse, OneDrive, Excel Online, OneNote, Word Online, Forms, RSS).

## What “function” means in PAD

PAD makers usually mean one of these:

| You say | In the product | Documented in |
| --- | --- | --- |
| Action | A card in the **Actions** pane | `modules/*.md` |
| Function | A **Power Fx** formula (`=Len(...)`) | `03-power-fx-functions.md` |
| Expression | Classic `%Value + 1%` syntax | `04-expression-syntax.md` |
| Connector | Cloud operation (SharePoint, Teams, …) | `modules/sharepoint.md` and siblings |
| UI element / image | Captured locator used by UI/web/OCR actions | `01-designer-usable-items.md` |
| Variable type | Text, list, Excel instance, … | `02-data-types.md` |

## Official Microsoft Learn

- [Actions reference](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference)
- [Formula reference - desktop flows](https://learn.microsoft.com/en-us/power-platform/power-fx/formula-reference-desktop-flows)
- [Variable data types](https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-data-types)

## Regenerate

If a local clone of [MicrosoftDocs/power-automate-docs](https://github.com/MicrosoftDocs/power-automate-docs) is available:

```bash
python3 scripts/generate_pad_docs.py /path/to/power-automate-docs/articles/desktop-flows/actions-reference
python3 scripts/generate_pad_how_it_works.py
```

Default action-reference path: `/tmp/pad-docs/articles/desktop-flows/actions-reference`. The how-it-works generator reads `inventory.json` only.
