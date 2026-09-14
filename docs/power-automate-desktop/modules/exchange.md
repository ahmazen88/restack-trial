# Exchange Server

Connect to Exchange and process mailbox messages.

This page documents every **native action** in this group (4 items).

## Actions

### Connect to Exchange server

- **Inventory id:** `exchange/connect-to-exchange-server`
- **Kind:** native-action
- **Purpose:** Open a new connection to an Exchange server.
- **Key inputs:** `Exchange server version` (Exchange 2010, Exchange 2010 SP1, Exchange 2010 SP2, Exchange 2013, Exchange 2013 SP1); `Connection type` (Auto discovery, Exchange server address); `Server address` (Text value); `Email address` (Text value); `Credentials` (Exchange default, User defined); `Domain` (Text value; optional); `Username` (Text value); `Password` (Direct encrypted input or Text value); `Timeout` (Numeric value; optional)
- **Produces:** `ExchangeConnection` (Exchange connection)
- **Exceptions:** `Failed to connect to the Exchange server`
- **Microsoft Learn:** [Connect to Exchange server](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/exchange#connecttoexchangeserver)

### Process Exchange email messages

- **Inventory id:** `exchange/process-exchange-email-messages`
- **Kind:** native-action
- **Purpose:** Processes exchange email messages.
- **Key inputs:** `Exchange connection` (Exchange connection); `Email message(s) to process` (List of Exchange mail messages); `Operation` (Delete email messages from server, Mark email messages as unread, Move email messages to mail folder); `Mailbox type` (Personal, Shared); `Shared mailbox address` (Text value); `Move to custom folder` (Boolean value); `Exchange folder` (Inbox, Deleted items, Drafts, Outbox, Sent items, Junk email); `Mail folder` (Text value)
- **Produces:** None listed
- **Exceptions:** `Specified mail-folder doesn't exist`; `Failed to process email messages`
- **Microsoft Learn:** [Process Exchange email messages](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/exchange#processexchangemessages)

### Retrieve Exchange email messages

- **Inventory id:** `exchange/retrieve-exchange-email-messages`
- **Kind:** native-action
- **Purpose:** Retrieves exchange email messages.
- **Key inputs:** `Exchange connection` (Exchange connection); `Mailbox type` (Personal, Shared); `Shared mailbox address` (Text value); `Retrieve email messages from custom folder` (Boolean value); `Exchange folder` (Inbox, Deleted items, Drafts, Outbox, Sent items, Junk email); `Mail folder` (Text value); `Retrieve` (All email messages, Unread email messages only, Read email messages only); `Mark as read` (Boolean value); `From contains` (Text value; optional); `To contains` (Text value; optional); `Subject contains` (Text value; optional); `Body contains` (Text value; optional); `Attachments` (Save attachments, Do not save attachments); `Save attachments into` (Folder)
- **Produces:** `RetrievedEmails` (List of Exchange mail messages)
- **Exceptions:** `Failed to save attachments`; `Specified mail-folder doesn't exist`; `Failed to retrieve email messages`
- **Microsoft Learn:** [Retrieve Exchange email messages](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/exchange#retrieveexchangemessages)

### Send Exchange email message

- **Inventory id:** `exchange/send-exchange-email-message`
- **Kind:** native-action
- **Purpose:** Sends exchange email message.
- **Key inputs:** `Exchange connection` (Exchange connection); `From` (Text value); `Sender display name` (Text value; optional); `To` (Text value); `CC` (Text value; optional); `BCC` (Text value; optional); `Subject` (Text value; optional); `Body` (Text value; optional); `Body is HTML` (Boolean value); `Attachment(s)` (List of Files; optional)
- **Produces:** None listed
- **Exceptions:** `Attachment not found`; `Failed to send email`
- **Microsoft Learn:** [Send Exchange email message](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/exchange#sendmessage)
