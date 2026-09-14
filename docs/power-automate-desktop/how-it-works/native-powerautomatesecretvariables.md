# Power Automate secret variables — how each function works

Native Actions pane module **Power Automate secret variables**.

1 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Get credential

- **Id:** `powerautomatesecretvariables/get-credential`
- **Kind:** native-action
- **Purpose:** Reads credential into a flow variable.

**Use case.** Resolve a stored username/password at runtime instead of hard-coding secrets.

**Demonstration.**

```text
**Get credential**
- Credential: `INV-1042`
- Timeout: `30`
Produces:
- `%Credential%` (Credential)
```

**Analogy.** Asking the safe for the key instead of taping the key to the script.

**In combination.** Get credential, then pass Username/Password into Launch, HTTP, or SAP.
