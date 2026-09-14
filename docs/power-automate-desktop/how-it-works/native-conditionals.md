# Conditionals — how each function works

Native Actions pane module **Conditionals**.

6 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Case

- **Id:** `conditionals/case`
- **Kind:** native-action
- **Purpose:** One match arm inside a Switch block.

**Use case.** In a batch that must follow different paths for empty vs loaded folders, drop **Case** on the canvas. One match arm inside a Switch block.

**Demonstration.**

```text
**Case**
- Operator: `Equal to (=)`
- Value to compare: `(set in designer)`
Place the actions that should run inside this block, then End.
```

**Analogy.** One tool in that kit: a fork in a corridor: you only walk the left hall if the sign says so.

**In combination.** Pair If/Else if/Else, or Switch with Case and Default case, and close with End.

### Default case

- **Id:** `conditionals/default-case`
- **Kind:** native-action
- **Purpose:** Fallback arm when no Case in a Switch matches.

**Use case.** In a batch that must follow different paths for empty vs loaded folders, drop **Default case** on the canvas. Fallback arm when no Case in a Switch matches.

**Demonstration.**

```text
**Default case**
- (no inputs)
Place the actions that should run inside this block, then End.
```

**Analogy.** One tool in that kit: a fork in a corridor: you only walk the left hall if the sign says so.

**In combination.** Pair If/Else if/Else, or Switch with Case and Default case, and close with End.

### Else

- **Id:** `conditionals/else`
- **Kind:** native-action
- **Purpose:** Runs when no earlier If / Else if condition was true.

**Use case.** In a batch that must follow different paths for empty vs loaded folders, drop **Else** on the canvas. Runs when no earlier If / Else if condition was true.

**Demonstration.**

```text
**Else**
- (no inputs)
Place the actions that should run inside this block, then End.
```

**Analogy.** The other road when the light is red.

**In combination.** Pair If/Else if/Else, or Switch with Case and Default case, and close with End.

### Else if

- **Id:** `conditionals/else-if`
- **Kind:** native-action
- **Purpose:** Tests another condition after an If that did not match.

**Use case.** In a batch that must follow different paths for empty vs loaded folders, drop **Else if** on the canvas. Tests another condition after an If that did not match.

**Demonstration.**

```text
**Else if**
- Operator: `Equal to (=)`
- First operand: `(set in designer)`
- Second operand: `(set in designer)`
Place the actions that should run inside this block, then End.
```

**Analogy.** One tool in that kit: a fork in a corridor: you only walk the left hall if the sign says so.

**In combination.** Pair If/Else if/Else, or Switch with Case and Default case, and close with End.

### If

- **Id:** `conditionals/if`
- **Kind:** native-action
- **Purpose:** Marks the beginning of a block of actions that is run if the condition specified in this statement is met.

**Use case.** Run one branch when a check is true (file exists, row count > 0, status = 'Open').

**Demonstration.**

```text
**If**
- Operator: `Equal to (=)`
- First operand: `(set in designer)`
- Second operand: `(set in designer)`
Place the actions that should run inside this block, then End.
```

**Analogy.** Looking at a traffic light before you cross.

**In combination.** Pair If/Else if/Else, or Switch with Case and Default case, and close with End. Combine with Else / Else if and End. Put Wait or If file exists before brittle UI/browser steps.

### Switch

- **Id:** `conditionals/switch`
- **Kind:** native-action
- **Purpose:** Routes execution to the Case that matches an expression.

**Use case.** In a batch that must follow different paths for empty vs loaded folders, drop **Switch** on the canvas. Routes execution to the Case that matches an expression.

**Demonstration.**

```text
**Switch**
- Value to check: `(set in designer)`
Place the actions that should run inside this block, then End.
```

**Analogy.** One tool in that kit: a fork in a corridor: you only walk the left hall if the sign says so.

**In combination.** Pair If/Else if/Else, or Switch with Case and Default case, and close with End.
