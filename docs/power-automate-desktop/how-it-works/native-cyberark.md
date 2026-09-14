# CyberArk — how each function works

Native Actions pane module **CyberArk**.

1 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Get password from CyberArk

- **Id:** `cyberark/get-password-from-cyberark`
- **Kind:** native-action
- **Purpose:** Reads password from CyberArk into a flow variable.

**Use case.** In a password you must not store in the flow, drop **Get password from CyberArk** on the canvas. Reads password from CyberArk into a flow variable.

**Demonstration.**

```text
**Get password from CyberArk**
- Server address: `INV-1042`
- Application ID: `INV-1042`
- Safe: `INV-1042`
- Folder: `C:\RPA\Invoices`
- Object: `INV-1042`
- Extra data: `INV-1042`
- Accept untrusted certificates: `False`
- Certificate location: `Don't use certificate`
- … 5 more parameter(s) in the action modal
Produces:
- `%JSONResponse%` (Custom object)
- `%CyberArkPassword%` (Encrypted value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Get password from CyberArk, then pass the sensitive value into Launch or HTTP actions.
