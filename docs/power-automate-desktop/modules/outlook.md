# Outlook

Drive the local Outlook desktop client for send, retrieve, and reply.

This page documents every **native action** in this group (7 items).

## Actions

### Close Outlook

- **Inventory id:** `outlook/close-outlook`
- **Kind:** native-action
- **Purpose:** Closes outlook.
- **Key inputs:** `Outlook instance` (Outlook instance)
- **Produces:** None listed
- **Exceptions:** `Failed to close Outlook instance`
- **Microsoft Learn:** [Close Outlook](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/outlook#close)

### Launch Outlook

- **Inventory id:** `outlook/launch-outlook`
- **Kind:** native-action
- **Purpose:** Starts Outlook and returns an instance later actions can reuse.
- **Key inputs:** None
- **Produces:** `OutlookInstance` (Outlook instance)
- **Exceptions:** `Failed to launch Outlook`
- **Microsoft Learn:** [Launch Outlook](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/outlook#launch)

### Process email messages in Outlook

- **Inventory id:** `outlook/process-email-messages-in-outlook`
- **Kind:** native-action
- **Purpose:** Processes email messages in Outlook.
- **Key inputs:** `Outlook instance` (Outlook instance); `Account` (Text value); `Email messages to process` (List of Outlook mail messages); `Operation` (Delete email messages, Move email messages to mail folder, Mark as unread); `Mail folder` (Text value)
- **Produces:** None listed
- **Exceptions:** `Failed to find Outlook account`; `Specified mail-folder doesn't exist`; `Failed to process email messages in Outlook`
- **Microsoft Learn:** [Process email messages in Outlook](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/outlook#processemailmessages)

### Respond to Outlook mail message

- **Inventory id:** `outlook/respond-to-outlook-mail-message`
- **Kind:** native-action
- **Purpose:** Respond to an Outlook message, by replying, replying to all or forwarding it.
- **Key inputs:** `Outlook instance` (Outlook instance); `Account` (Text value); `Mail message` (Outlook mail message); `Response action` (Reply, Reply all, Forward); `To` (Text value); `CC` (Text value; optional); `BCC` (Text value; optional); `Body` (Text value; optional); `Attachment(s)` (List of Files; optional)
- **Produces:** None listed
- **Exceptions:** `Failed to find Outlook account`; `Failed to send email`; `Attachment not found`
- **Microsoft Learn:** [Respond to Outlook mail message](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/outlook#respondtomailmessage)

### Retrieve email messages from Outlook

- **Inventory id:** `outlook/retrieve-email-messages-from-outlook`
- **Kind:** native-action
- **Purpose:** Retrieves email messages from Outlook.
- **Key inputs:** `Outlook instance` (Outlook instance); `Account` (Text value); `Mail folder` (Text value); `Retrieve` (All email messages, Unread email messages only, Read email messages only); `Mark as read` (Boolean value); `From contains` (Text value; optional); `To contains` (Text value; optional); `Subject contains` (Text value; optional); `Body contains` (Text value; optional); `Attachments` (Save attachments, Don't save attachments); `Save attachments into` (Folder)
- **Produces:** `RetrievedEmails` (List of Outlook mail messages)
- **Exceptions:** `Failed to find Outlook account`; `Mail-folder specified not valid in Outlook`; `Directory for saving attachments not found`; `Failed to retrieve email messages from Outlook`
- **Microsoft Learn:** [Retrieve email messages from Outlook](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/outlook#retrieveemailmessages)

### Save Outlook email messages

- **Inventory id:** `outlook/save-outlook-email-messages`
- **Kind:** native-action
- **Purpose:** Saves outlook email messages.
- **Key inputs:** `Outlook instance` (Outlook instance); `Account` (Text value); `Email message(s) to save` (List of Outlook mail messages); `Save format` (Text only (*.txt), Outlook template (*.oft), Outlook message format (*.msg), Outlook message format - Unicode (*.msg), HTML (*.html), MHT files (*.mht)); `File name` (Default, Custom); `Save as` (Text value); `Save email message(s) to` (Folder)
- **Produces:** `StoredMessagesFiles` (List of Text values)
- **Exceptions:** `Failed to find Outlook account`; `Directory not found`; `Email message is deleted or moved to another folder`; `Failed to save email message(s)`
- **Microsoft Learn:** [Save Outlook email messages](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/outlook#saveoutlookemailmessages)

### Send email through Outlook

- **Inventory id:** `outlook/send-email-through-outlook`
- **Kind:** native-action
- **Purpose:** Sends email through Outlook.
- **Key inputs:** `Outlook instance` (Outlook instance); `Account` (Text value); `Send email from` (Account, Other mailbox); `Send from` (Text value); `To` (Text value); `CC` (Text value; optional); `BCC` (Text value; optional); `Subject` (Text value; optional); `Body` (Text value; optional); `Body is HTML` (Boolean value); `Attachment(s)` (List of Files; optional)
- **Produces:** None listed
- **Exceptions:** `Failed to find Outlook account`; `Failed to send email`; `Attachment not found`
- **Microsoft Learn:** [Send email through Outlook](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/outlook#sendemailthroughoutlook)
