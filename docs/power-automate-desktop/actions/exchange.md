# Exchange Server

Connect to Exchange and process mailbox messages.

- Actions in this module: **4**
- Official docs: [Exchange Server actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/exchange)

## Actions

### Connect to Exchange server

Open a new connection to an Exchange server.

Designer name: **Connect to Exchange server**. Official reference: [Exchange Server / Connect to Exchange server](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/exchange#connecttoexchangeserver).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Exchange server version | Choice | Exchange 2010, Exchange 2010 SP1, Exchange 2010 SP2, Exchange 2013, Exchange 2013 SP1 | Exchange 2013 SP1 |
| Connection type | Choice | Auto discovery, Exchange server address | Auto discovery |
| Server address | Required | Text value | — |
| Email address | Required | Text value | — |
| Credentials | Choice | Exchange default, User defined | Exchange default |
| Domain | Optional | Text value | — |
| Username | Required | Text value | — |
| Password | Required | Direct encrypted input or Text value | — |
| Timeout | Optional | Numeric value | 30 |

**Outputs**

| Variable | Type |
|---|---|
| ExchangeConnection | Exchange connection |

**On error:** `Failed to connect to the Exchange server`.

---

### Retrieve Exchange email messages

Retrieve email messages from the specified Exchange server.

Designer name: **Retrieve Exchange email messages**. Official reference: [Exchange Server / Retrieve Exchange email messages](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/exchange#retrieveexchangemessages).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Exchange connection | Required | Exchange connection | — |
| Mailbox type | Choice | Personal, Shared | Personal |
| Shared mailbox address | Required | Text value | — |
| Retrieve email messages from custom folder | Choice | Boolean value | False |
| Exchange folder | Choice | Inbox, Deleted items, Drafts, Outbox, Sent items, Junk email | Inbox |
| Mail folder | Required | Text value | Inbox |
| Retrieve | Choice | All email messages, Unread email messages only, Read email messages only | Unread email messages only |
| Mark as read | Choice | Boolean value | True |
| From contains | Optional | Text value | — |
| To contains | Optional | Text value | — |
| Subject contains | Optional | Text value | — |
| Body contains | Optional | Text value | — |
| Attachments | Choice | Save attachments, Do not save attachments | Do not save attachments |
| Save attachments into | Required | Folder | — |

**Outputs**

| Variable | Type |
|---|---|
| RetrievedEmails | List of Exchange mail messages |

**On error:** `Failed to save attachments`, `Specified mail-folder doesn't exist`, `Failed to retrieve email messages`.

---

### Send Exchange email message

Create and send a new email message.

Designer name: **Send Exchange email message**. Official reference: [Exchange Server / Send Exchange email message](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/exchange#sendmessage).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Exchange connection | Required | Exchange connection | — |
| From | Required | Text value | — |
| Sender display name | Optional | Text value | — |
| To | Required | Text value | — |
| CC | Optional | Text value | — |
| BCC | Optional | Text value | — |
| Subject | Optional | Text value | — |
| Body | Optional | Text value | — |
| Body is HTML | Choice | Boolean value | False |
| Attachment(s) | Optional | List of Files | — |

Produces no variables.

**On error:** `Attachment not found`, `Failed to send email`.

---

### Process Exchange email messages

Move, delete or mark as unread an email message (or a list of email messages).

Designer name: **Process Exchange email messages**. Official reference: [Exchange Server / Process Exchange email messages](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/exchange#processexchangemessages).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Exchange connection | Required | Exchange connection | — |
| Email message(s) to process | Required | List of Exchange mail messages | — |
| Operation | Choice | Delete email messages from server, Mark email messages as unread, Move email messages to mail folder | Move email messages to mail folder |
| Mailbox type | Choice | Personal, Shared | Personal |
| Shared mailbox address | Required | Text value | — |
| Move to custom folder | Choice | Boolean value | False |
| Exchange folder | Choice | Inbox, Deleted items, Drafts, Outbox, Sent items, Junk email | Inbox |
| Mail folder | Required | Text value | Inbox |

Produces no variables.

**On error:** `Specified mail-folder doesn't exist`, `Failed to process email messages`.

---
