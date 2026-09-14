# Power Automate environment — how each function works

Native Actions pane module **Power Automate environment**.

1 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Retrieve environment variable

- **Id:** `powerautomateenvironment/retrieve-environment-variable`
- **Kind:** native-action
- **Purpose:** Retrieves environment variable.

**Use case.** In a path or flag that changes per DEV/TEST/PROD, drop **Retrieve environment variable** on the canvas. Retrieves environment variable.

**Demonstration.**

```text
**Retrieve environment variable**
- Environment variable: `INV-1042`
Produces:
- `%EnvironmentVariableValue%` (*Depends on the selected environment variable type*)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Retrieve environment variable at the start of Main and reuse the value.
