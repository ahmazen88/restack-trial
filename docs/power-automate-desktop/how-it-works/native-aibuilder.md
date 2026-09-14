# AI Builder (preview) — how each function works

Native Actions pane module **AI Builder (preview)**.

1 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Create text with GPT (preview)

- **Id:** `aibuilder/create-text-with-gpt-preview`
- **Kind:** native-action
- **Purpose:** Creates text with GPT (preview).

**Use case.** In drafting a customer reply that a human must approve, drop **Create text with GPT (preview)** on the canvas. Creates text with GPT (preview).

**Demonstration.**

```text
**Create text with GPT (preview)**
- Instructions: `INV-1042`
Produces:
- `%PredictV2Response%` (Connector object)
- `%PredictV2TextResponse%` (Text)
```

**Analogy.** One tool in that kit: asking an intern to draft a letter, then reading it before it is sent.

**In combination.** Follow with Display message or Display input dialog so a person reviews the GPT text.
