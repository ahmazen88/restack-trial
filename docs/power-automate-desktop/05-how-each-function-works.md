# How each Power Automate Desktop function works

## Do we have all the information?

**We have a complete catalog of the product surface**, and this chapter adds **how each item is used**.

| Layer | Status |
| --- | --- |
| Every native Actions-pane action (448) | Named, purpose, inputs, outputs, exceptions, **use case, demonstration, analogy, combination note** |
| Default cloud connector operations (185) | Same, plus connection/binary-file notes |
| Every documented Power Fx function for desktop flows (130) | Purpose, formula demonstration, analogy |
| Designer / console usable items (35) | How the workshop itself works |
| Variable data types (39) | What each “jar shape” is |
| Actions used **together** | [Combination playbooks](06-combination-playbooks.md) |
| Portal file uploads (Ariba, Coupa, …) | [Connected folder-upload flow](flows/ariba-folder-upload/README.md) |

**This set does not replace Microsoft Learn** for:

- Every advanced dropdown value and screenshot in the action modal
- Connector operations you add later from the **Assets library** (those appear after you add the connector)
- Service limits, licensing (premium vs standard), and tenant DLP policy
- Exact SAP/selector repair click-paths for your application

Parameter **names and types** come from the product. Use cases, demonstrations, and analogies are original working notes for makers.

## How to read a function page

Each item in [how-it-works/](how-it-works/README.md) has four blocks:

1. **Use case** — when you reach for this card
2. **Demonstration** — designer-style parameters with sample Contoso/RPA paths
3. **Analogy** — one everyday picture of the same job
4. **In combination** — which neighbors it expects (Launch before Close, binary convert before SharePoint, and so on)

Classic flows use `%Variable%` and **0-based** indexes. Power Fx flows use `=` and **1-based** `Index`. Do not mix them in one flow.

## Open the chapters

- [How-it-works index (every function)](how-it-works/README.md)
- [Combination playbooks (actions together)](06-combination-playbooks.md)
- [Portal uploads like Ariba](07-portal-uploads-ariba.md)
- [Connected Ariba folder-upload flow](flows/ariba-folder-upload/README.md)
- [Inventory](00-inventory.md) if you need the raw list

Example of the four-block shape (Clipboard):

### Get clipboard text

**Use case.** In a hand-off between two apps that have no API, drop **Get clipboard text** on the canvas. Reads clipboard text into a flow variable.

**Demonstration.**

**Get clipboard text**
- (no inputs)
Produces:
- `%ClipboardText%` (Text value)

**Analogy.** Reading whatever is currently on the sticky note.

**In combination.** Copy with Get/Set clipboard; Clear clipboard contents when the secret should not linger.
