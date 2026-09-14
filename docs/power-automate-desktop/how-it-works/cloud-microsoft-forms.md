# Microsoft Forms (cloud) — how each function works

Default-pane **Microsoft Forms (cloud)** operations. Requires a connection reference. File payloads are binary data.

1 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Get response details

- **Id:** `microsoft-forms/get-response-details`
- **Kind:** cloud-connector-operation
- **Purpose:** Reads response details into a flow variable.

**Use case.** In a Form response the bot must file, drop **Get response details** on the canvas. Reads response details into a flow variable.

**Demonstration.**

```text
**Get response details**
- (no inputs)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Get response details, then write fields to Excel or Dataverse.
