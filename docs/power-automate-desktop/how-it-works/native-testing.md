# Testing — how each function works

Native Actions pane module **Testing**.

2 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Assert

- **Id:** `testing/assert`
- **Kind:** native-action
- **Purpose:** Fails a test when an expression is not true.

**Use case.** In a regression pack for a desktop flow, drop **Assert** on the canvas. Fails a test when an expression is not true.

**Demonstration.**

```text
**Assert**
- Assert expression: `%Count% > 0`
- Assert message: `Processed by desktop flow Close-P9`
```

**Analogy.** The teacher checking the answer key.

**In combination.** Test a desktop flow, then Assert on outputs.

### Test a desktop flow

- **Id:** `testing/test-a-desktop-flow`
- **Kind:** native-action
- **Purpose:** Test a desktop flow that receives input variables and might produce output variables.

**Use case.** In a regression pack for a desktop flow, drop **Test a desktop flow** on the canvas. Test a desktop flow that receives input variables and might produce output variables.

**Demonstration.**

```text
**Test a desktop flow**
- Desktop flow: `(set in designer)`
```

**Analogy.** One tool in that kit: a quiz at the end of a drill: expected answer versus what the student wrote.

**In combination.** Test a desktop flow, then Assert on outputs.
