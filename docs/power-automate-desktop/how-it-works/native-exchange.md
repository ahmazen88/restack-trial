# Exchange Server — how each function works

Native Actions pane module **Exchange Server**.

4 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Connect to Exchange server

- **Id:** `exchange/connect-to-exchange-server`
- **Kind:** native-action
- **Purpose:** Open a new connection to an Exchange server.

**Use case.** In a shared mailbox on Exchange when Outlook is not installed, drop **Connect to Exchange server** on the canvas. Open a new connection to an Exchange server.

**Demonstration.**

```text
**Connect to Exchange server**
- Exchange server version: `Exchange 2013 SP1`
- Connection type: `Auto discovery`
- Server address: `INV-1042`
- Email address: `ap@contoso.example`
- Credentials: `Exchange default`
- Domain: `INV-1042`
- Username: `CONTOSO\rpa.bot`
- Password: `%Credential.Password%  (sensitive)`
- … 1 more parameter(s) in the action modal
Produces:
- `%ExchangeConnection%` (Exchange connection)
```

**Analogy.** One tool in that kit: the building mailroom instead of your personal inbox tray.

**In combination.** Connect to Exchange server, retrieve or send, then process messages.

### Process Exchange email messages

- **Id:** `exchange/process-exchange-email-messages`
- **Kind:** native-action
- **Purpose:** Processes exchange email messages.

**Use case.** In a shared mailbox on Exchange when Outlook is not installed, drop **Process Exchange email messages** on the canvas. Processes exchange email messages.

**Demonstration.**

```text
**Process Exchange email messages**
- Exchange connection: `(set in designer)`
- Email message(s) to process: `%Files%`
- Operation: `Move email messages to mail folder`
- Mailbox type: `Personal`
- Shared mailbox address: `INV-1042`
- Move to custom folder: `False`
- Exchange folder: `C:\RPA\Invoices`
- Mail folder: `C:\RPA\Invoices`
```

**Analogy.** One tool in that kit: the building mailroom instead of your personal inbox tray.

**In combination.** Connect to Exchange server, retrieve or send, then process messages.

### Retrieve Exchange email messages

- **Id:** `exchange/retrieve-exchange-email-messages`
- **Kind:** native-action
- **Purpose:** Retrieves exchange email messages.

**Use case.** In a shared mailbox on Exchange when Outlook is not installed, drop **Retrieve Exchange email messages** on the canvas. Retrieves exchange email messages.

**Demonstration.**

```text
**Retrieve Exchange email messages**
- Exchange connection: `(set in designer)`
- Mailbox type: `Personal`
- Shared mailbox address: `INV-1042`
- Retrieve email messages from custom folder: `False`
- Exchange folder: `C:\RPA\Invoices`
- Mail folder: `C:\RPA\Invoices`
- Retrieve: `Unread email messages only`
- Mark as read: `True`
- … 6 more parameter(s) in the action modal
Produces:
- `%RetrievedEmails%` (List of Exchange mail messages)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Connect to Exchange server, retrieve or send, then process messages.

### Send Exchange email message

- **Id:** `exchange/send-exchange-email-message`
- **Kind:** native-action
- **Purpose:** Sends exchange email message.

**Use case.** In a shared mailbox on Exchange when Outlook is not installed, drop **Send Exchange email message** on the canvas. Sends exchange email message.

**Demonstration.**

```text
**Send Exchange email message**
- Exchange connection: `(set in designer)`
- From: `INV-1042`
- Sender display name: `INV-1042`
- To: `ap@contoso.example`
- CC: `INV-1042`
- BCC: `INV-1042`
- Subject: `Invoice INV-1042 processed`
- Body: `Processed by desktop flow Close-P9`
- … 2 more parameter(s) in the action modal
```

**Analogy.** Handing a finished envelope to the mailroom.

**In combination.** Connect to Exchange server, retrieve or send, then process messages.
