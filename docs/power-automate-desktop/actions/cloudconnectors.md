# Cloud connectors

Run Power Automate **cloud connector** operations inside a desktop flow. This pane is a live catalog, not a fixed list of 10 actions: every connector your license and DLP policy allow can appear here.

Official docs: [Cloud connectors as desktop actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cloudconnectors).

## What shows up in the pane

| You see | When |
|---|---|
| Standard connectors | Work/school account with permission. |
| Premium connectors | Attended RPA license (and DLP must allow them). |
| Connection picker | First use of a connector in the flow. |
| Embedded connection references | Co-owners can run the flow with your connection. |

Operations use the **same parameters and payloads** as the cloud connector of the same name. Desktop-specific wrapping is the file conversion pattern below.

## Files in and out

Connector actions do not take a Windows file path. Convert first:

1. **Convert file to binary data** (File module) → send `ContentBytes`.
2. After a connector returns a file body → **Convert binary data to file**.

## Microsoft Dataverse operations supported in desktop flows

These Dataverse operations are the ones Microsoft lists as available in PAD. The Environment parameter supports **Current** (resolve to the flow’s environment).

| Operation | Purpose |
|---|---|
| Add a new row to selected environment | Create a row. |
| Delete a row from selected environment | Delete by id. |
| Download a file or an image from selected environment | File/image column → binary. |
| Get a row by ID from selected environment | Read one row. |
| List rows from selected environment | Query / FetchXML-style list. |
| Perform a bound action in selected environment | Table-bound custom API / action. |
| Perform an unbound action in selected environment | Global custom API / action. |
| Relate rows in selected environment | Associate. |
| Unrelate rows in selected environment | Disassociate. |
| Update a row in selected environment | Patch a row. |
| Upload a file or an image to selected environment | Binary → file/image column. |

## Other connectors you will search for in this pane

Search the pane by connector name. Common ones used next to UI/Excel automation:

- Office 365 Users, Office 365 Groups
- Teams
- OneDrive for Business
- Excel Online (Business)
- SharePoint (also has its own PAD module)
- Office 365 Outlook (also has its own PAD module)
- Dataverse
- Azure AD / Microsoft Entra ID
- SQL Server (cloud), Approvals, Content Conversion

The full cloud catalog is [Connector reference for Power Automate](https://learn.microsoft.com/en-us/connectors/connector-reference/connector-reference-powerautomate-connectors). If an operation exists there and DLP allows it, expect it (or a close versioned twin such as *Send an email (V2)*) in this desktop pane.

## Run requirements

- Cloud-initiated attended/unattended runs need the [v2 schema](https://learn.microsoft.com/en-us/power-automate/desktop-flows/schema) and embedded connection references for shared flows.
- Run-only users run from the console with **their** connections.
- Allowlist the desktop-flow service endpoints or connector actions fail at runtime.
