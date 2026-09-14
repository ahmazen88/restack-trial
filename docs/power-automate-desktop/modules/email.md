# Email

Send and retrieve mail over IMAP/SMTP without Outlook.

This page documents every **native action** in this group (3 items).

## Actions

### Process email messages

- **Inventory id:** `email/process-email-messages`
- **Kind:** native-action
- **Purpose:** Processes email messages.
- **Key inputs:** `IMAP server` (Text value); `Port` (Numeric value; optional); `Enable SSL` (Boolean value); `Username` (Text value); `Password` (Direct encrypted input or Text value); `Accept Untrusted Certificates` (Boolean value); `Email(s) to process` (List of Mail Messages); `Operation` (Delete emails from server, Mark emails as unread, Move emails to mail folder, Mark emails as unread and move to mail folder); `Mail folder` (Text value)
- **Produces:** None listed
- **Exceptions:** `Failed to connect to IMAP server`; `Specified mail-folder doesn't exist`; `Failed to process emails`
- **Microsoft Learn:** [Process email messages](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/email#processemails)

### Retrieve email messages

- **Inventory id:** `email/retrieve-email-messages`
- **Kind:** native-action
- **Purpose:** Retrieves email messages.
- **Key inputs:** `IMAP server` (Text value); `Port` (Numeric value; optional); `Enable SSL` (Boolean value); `User name` (Text value); `Password` (Direct encrypted input or Text value); `Accept untrusted certificates` (Boolean value); `Mail folder` (Text value); `Retrieve` (All email messages, Unread email messages only, Read email messages only); `Mark As read` (Boolean value); `"From" field contains` (Text value; optional); `"To" field contains` (Text value; optional); `"Subject" contains` (Text value; optional); `'Body' contains` (Text value; optional); `Save attachments` (Save attachments, Do not save attachments); `Save attachments into` (Folder)
- **Produces:** `RetrievedEmails` (List of Mail Messages)
- **Exceptions:** `Failed to connect to IMAP server`; `Failed to authenticate to the IMAP server`; `Specified mail-folder doesn't exist`; `Failed to save attachments`; `Failed to retrieve emails`
- **Microsoft Learn:** [Retrieve email messages](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/email#retrieveemails)

### Send email

- **Inventory id:** `email/send-email`
- **Kind:** native-action
- **Purpose:** Sends email.
- **Key inputs:** `SMTP server` (Text value); `Server port` (Numeric value; optional); `Enable SSL` (Boolean value); `SMTP Server needs authentication` (Boolean value); `User name` (Text value); `Password` (Direct encrypted input or Text value); `Accept untrusted certificates` (Boolean value); `From` (Text value); `Sender display name` (Text value; optional); `To` (Text value); `CC` (Text value; optional); `BCC` (Text value; optional); `Subject` (Text value; optional); `Body` (Text value; optional); `Body Is HTML` (Boolean value); `Attachment(s)` (List of Files; optional)
- **Produces:** None listed
- **Exceptions:** `Invalid email address`; `Failed to send email`; `Attachment not found`
- **Microsoft Learn:** [Send email](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/email#sendemail)
