# Flow control

Labels, subflows, waits, regions, errors, and flow stop rules.

This page documents every **native action** in this group (14 items).

## Actions

### Comment

- **Inventory id:** `flowcontrol/comment`
- **Kind:** native-action
- **Purpose:** Adds a note on the canvas. It does not run.
- **Key inputs:** `Comment` (Text value; optional)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Comment](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#comment)

### End

- **Inventory id:** `flowcontrol/end`
- **Kind:** native-action
- **Purpose:** Closes the current block (condition, loop, or error block).
- **Key inputs:** None
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [End](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#end)

### End region

- **Inventory id:** `flowcontrol/end-region`
- **Kind:** native-action
- **Purpose:** Ends region.
- **Key inputs:** None
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [End region](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#endregion)

### Exit subflow

- **Inventory id:** `flowcontrol/exit-subflow`
- **Kind:** native-action
- **Purpose:** Returns from the current subflow to its caller.
- **Key inputs:** None
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Exit subflow](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#exitfunction)

### Get last error

- **Inventory id:** `flowcontrol/get-last-error`
- **Kind:** native-action
- **Purpose:** Reads last error into a flow variable.
- **Key inputs:** `Clear error` (Boolean value)
- **Produces:** `LastError` (Error)
- **Exceptions:** none listed
- **Microsoft Learn:** [Get last error](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#getlasterror)

### Go to

- **Inventory id:** `flowcontrol/go-to`
- **Kind:** native-action
- **Purpose:** Jumps execution to a Label in the same subflow.
- **Key inputs:** `Go to label` (Text value)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Go to](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#goto)

### If safe stop requested

- **Inventory id:** `flowcontrol/if-safe-stop-requested`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when safe stop requested.
- **Key inputs:** `Stop the flow` (Boolean value)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [If safe stop requested](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#ifsafestopaction)

### Label

- **Inventory id:** `flowcontrol/label`
- **Kind:** native-action
- **Purpose:** Named jump target for a Go to action.
- **Key inputs:** `Label name` (Text value)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Label](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#label)

### On block error

- **Inventory id:** `flowcontrol/on-block-error`
- **Kind:** native-action
- **Purpose:** Starts a block whose nested failures are handled together.
- **Key inputs:** `Name` (Text value); `Retry policy` (None, Fixed, Exponential); `Handle flow terminating errors` (Boolean value)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [On block error](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#block)

### Region

- **Inventory id:** `flowcontrol/region`
- **Kind:** native-action
- **Purpose:** Starts a named visual group of actions.
- **Key inputs:** `Name` (Text value; optional)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Region](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#region)

### Run subflow

- **Inventory id:** `flowcontrol/run-subflow`
- **Kind:** native-action
- **Purpose:** Runs subflow.
- **Key inputs:** `Subflow name` (Subflow); `Input as expression` (Boolean value)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Run subflow](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#callfunction)

### Stop flow

- **Inventory id:** `flowcontrol/stop-flow`
- **Kind:** native-action
- **Purpose:** Stops flow.
- **Key inputs:** `End flow` (Successfully, With error message); `Error message` (Text value)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Stop flow](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#exit)

### Throw custom error

- **Inventory id:** `flowcontrol/throw-custom-error`
- **Kind:** native-action
- **Purpose:** Raises a maker-defined error for On block error to catch.
- **Key inputs:** `Error name` (Text value); `Error message` (Text value)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Throw custom error](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol)

### Wait

- **Inventory id:** `flowcontrol/wait`
- **Kind:** native-action
- **Purpose:** Pauses the flow for a number of seconds.
- **Key inputs:** `Duration` (Numeric value)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Wait](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/flowcontrol#wait)
