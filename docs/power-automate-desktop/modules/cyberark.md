# CyberArk

Pull application passwords from CyberArk at runtime.

This page documents every **native action** in this group (1 items).

## Actions

### Get password from CyberArk

- **Inventory id:** `cyberark/get-password-from-cyberark`
- **Kind:** native-action
- **Purpose:** Reads password from CyberArk into a flow variable.
- **Key inputs:** `Server address` (Text value); `Application ID` (Text value); `Safe` (Text value); `Folder` (Text value); `Object` (Text value); `Extra data` (Text value; optional); `Accept untrusted certificates` (Boolean value); `Certificate location` (Don't use certificate, Load certificate from Windows Store, Load certificate from file); `Use only valid certificates` (Boolean value); `Store certificate path` (Text value); `Certificates path` (File); `Certificate password` (Direct encrypted input or Text value); `Timeout` (Numeric value; optional)
- **Produces:** `JSONResponse` (Custom object); `CyberArkPassword` (Encrypted value)
- **Exceptions:** `Failed to send web request`; `Timeout expired`; `Error response from web request`
- **Microsoft Learn:** [Get password from CyberArk](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cyberark#getpasswordbase)
