# CyberArk

Retrieve secrets from CyberArk vaults at runtime.

- Actions in this module: **1**
- Official docs: [CyberArk actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cyberark)

## Actions

### Get password from CyberArk

Returns a password for a specific application from CyberArk.

Designer name: **Get password from CyberArk**. Official reference: [CyberArk / Get password from CyberArk](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cyberark#getpasswordbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Server address | Required | Text value | — |
| Application ID | Required | Text value | — |
| Safe | Required | Text value | — |
| Folder | Required | Text value | — |
| Object | Required | Text value | — |
| Extra data | Optional | Text value | — |
| Accept untrusted certificates | Choice | Boolean value | False |
| Certificate location | Choice | Don't use certificate, Load certificate from Windows Store, Load certificate from file | Don't use certificate |
| Use only valid certificates | Choice | Boolean value | False |
| Store certificate path | Required | Text value | — |
| Certificates path | Required | File | — |
| Certificate password | Required | Direct encrypted input or Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| JSONResponse | Custom object |
| CyberArkPassword | Encrypted value |

**On error:** `Failed to send web request`, `Timeout expired`, `Error response from web request`.

---
