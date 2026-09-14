# Loops

Repeat actions with Loop, Loop condition, For each, Exit loop, and Next loop.

This page documents every **native action** in this group (5 items).

## Actions

### Exit loop

- **Inventory id:** `loops/exit-loop`
- **Kind:** native-action
- **Purpose:** Leaves the current loop and continues with the next action after it.
- **Key inputs:** None
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Exit loop](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops#break)

### For each

- **Inventory id:** `loops/for-each`
- **Kind:** native-action
- **Purpose:** Repeats nested actions once for every item in a list, table, or row.
- **Key inputs:** `Value to iterate` (*)
- **Produces:** `*` (The value name that will store the current item value in each iteration.)
- **Exceptions:** none listed
- **Microsoft Learn:** [For each](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops#foreach)

### Loop

- **Inventory id:** `loops/loop`
- **Kind:** native-action
- **Purpose:** Repeats nested actions a fixed number of times.
- **Key inputs:** `Start from` (Numeric value); `Increment by` (Numeric value); `End to` (Numeric value)
- **Produces:** `*` (The value name that will store the current index, starting at the start from value. The value will change by the increment with each iteration.)
- **Exceptions:** none listed
- **Microsoft Learn:** [Loop](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops#loop)

### Loop condition

- **Inventory id:** `loops/loop-condition`
- **Kind:** native-action
- **Purpose:** Repeats nested actions while a condition stays true.
- **Key inputs:** `Operator` (Equal to (=), Not equal to (<>), Greater than (>), Greater than or equal to (>=), Less than (<), Less than or equal to (<=)); `First operand` (*); `Second operand` (*)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Loop condition](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops#while)

### Next loop

- **Inventory id:** `loops/next-loop`
- **Kind:** native-action
- **Purpose:** Skips the rest of this iteration and starts the next one.
- **Key inputs:** None
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Next loop](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops#continue)
