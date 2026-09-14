# Loops — how each function works

Native Actions pane module **Loops**.

5 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Exit loop

- **Id:** `loops/exit-loop`
- **Kind:** native-action
- **Purpose:** Leaves the current loop and continues with the next action after it.

**Use case.** In one CSV row or one file at a time, drop **Exit loop** on the canvas. Leaves the current loop and continues with the next action after it.

**Demonstration.**

```text
**Exit loop**
- (no inputs)
```

**Analogy.** One tool in that kit: walking a stack of envelopes and doing the same stamp on each.

**In combination.** For each over a list/table, Loop for a count, Loop condition until done; Exit loop to bail out.

### For each

- **Id:** `loops/for-each`
- **Kind:** native-action
- **Purpose:** Repeats nested actions once for every item in a list, table, or row.

**Use case.** Repeat the same nested actions once per file, list item, or data-table row.

**Demonstration.**

```text
**For each**
- Value to iterate: `(set in designer)`
Produces:
- `%*%` (The value name that will store the current item value in each iteration.)
Place the actions that should run inside this block, then End.
```

**Analogy.** Stamping every envelope in a stack, one after another.

**In combination.** For each over a list/table, Loop for a count, Loop condition until done; Exit loop to bail out.

### Loop

- **Id:** `loops/loop`
- **Kind:** native-action
- **Purpose:** Repeats nested actions a fixed number of times.

**Use case.** In one CSV row or one file at a time, drop **Loop** on the canvas. Repeats nested actions a fixed number of times.

**Demonstration.**

```text
**Loop**
- Start from: `1`
- Increment by: `1`
- End to: `1`
Produces:
- `%*%` (The value name that will store the current index, starting at the start from value. The value will change by the increment with each iteration.)
Place the actions that should run inside this block, then End.
```

**Analogy.** Doing ten push-ups because someone said 'ten', not because the list ended.

**In combination.** For each over a list/table, Loop for a count, Loop condition until done; Exit loop to bail out.

### Loop condition

- **Id:** `loops/loop-condition`
- **Kind:** native-action
- **Purpose:** Repeats nested actions while a condition stays true.

**Use case.** In one CSV row or one file at a time, drop **Loop condition** on the canvas. Repeats nested actions while a condition stays true.

**Demonstration.**

```text
**Loop condition**
- Operator: `Equal to (=)`
- First operand: `(set in designer)`
- Second operand: `(set in designer)`
Place the actions that should run inside this block, then End.
```

**Analogy.** One tool in that kit: walking a stack of envelopes and doing the same stamp on each.

**In combination.** For each over a list/table, Loop for a count, Loop condition until done; Exit loop to bail out.

### Next loop

- **Id:** `loops/next-loop`
- **Kind:** native-action
- **Purpose:** Skips the rest of this iteration and starts the next one.

**Use case.** In one CSV row or one file at a time, drop **Next loop** on the canvas. Skips the rest of this iteration and starts the next one.

**Demonstration.**

```text
**Next loop**
- (no inputs)
```

**Analogy.** One tool in that kit: walking a stack of envelopes and doing the same stamp on each.

**In combination.** For each over a list/table, Loop for a count, Loop condition until done; Exit loop to bail out.
