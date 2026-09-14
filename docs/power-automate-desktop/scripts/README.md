# Regenerating the action catalog

Action names and parameter tables in `actions/*.md` (except the four dynamic panes) are generated from a sparse clone of [MicrosoftDocs/power-automate-docs](https://github.com/MicrosoftDocs/power-automate-docs).

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/MicrosoftDocs/power-automate-docs.git
cd power-automate-docs
git sparse-checkout set articles/desktop-flows/actions-reference

PAD_MS_DOCS=/path/to/power-automate-docs/articles/desktop-flows/actions-reference \
PAD_DOC_OUT=/path/to/docs/power-automate-desktop \
python3 docs/power-automate-desktop/scripts/generate_from_microsoft_docs.py
```

The generator **does not overwrite** modules with no fixed action list (Cloud connectors, SharePoint, Office 365 Outlook, Custom actions). Those pages are maintained by hand.

After regenerating, run:

```bash
python3 docs/power-automate-desktop/scripts/verify_docs.py
```
