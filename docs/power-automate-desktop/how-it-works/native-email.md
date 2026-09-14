# Email — how each function works

Native Actions pane module **Email**.

3 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Process email messages

- **Id:** `email/process-email-messages`
- **Kind:** native-action
- **Purpose:** Processes email messages.

**Use case.** In IMAP/SMTP mailbox without a local Outlook profile, drop **Process email messages** on the canvas. Processes email messages.

**Demonstration.**

```text
**Process email messages**
- IMAP server: `INV-1042`
- Port: `993`
- Enable SSL: `True`
- Username: `CONTOSO\rpa.bot`
- Password: `%Credential.Password%  (sensitive)`
- Accept Untrusted Certificates: `False`
- Email(s) to process: `%Files%`
- Operation: `Move emails to mail folder`
- … 1 more parameter(s) in the action modal
```

**Analogy.** One tool in that kit: a post-office box you unlock with a key.

**In combination.** Retrieve email messages, Process or Send email, no Outlook instance required.

### Retrieve email messages

- **Id:** `email/retrieve-email-messages`
- **Kind:** native-action
- **Purpose:** Retrieves email messages.

**Use case.** In IMAP/SMTP mailbox without a local Outlook profile, drop **Retrieve email messages** on the canvas. Retrieves email messages.

**Demonstration.**

```text
**Retrieve email messages**
- IMAP server: `INV-1042`
- Port: `993`
- Enable SSL: `True`
- User name: `CONTOSO\rpa.bot`
- Password: `%Credential.Password%  (sensitive)`
- Accept untrusted certificates: `False`
- Mail folder: `C:\RPA\Invoices`
- Retrieve: `All email messages`
- … 7 more parameter(s) in the action modal
Produces:
- `%RetrievedEmails%` (List of Mail Messages)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Retrieve email messages, Process or Send email, no Outlook instance required.

### Send email

- **Id:** `email/send-email`
- **Kind:** native-action
- **Purpose:** Sends email.

**Use case.** In IMAP/SMTP mailbox without a local Outlook profile, drop **Send email** on the canvas. Sends email.

**Demonstration.**

```text
**Send email**
- SMTP server: `INV-1042`
- Server port: `25`
- Enable SSL: `False`
- SMTP Server needs authentication: `False`
- User name: `CONTOSO\rpa.bot`
- Password: `%Credential.Password%  (sensitive)`
- Accept untrusted certificates: `False`
- From: `INV-1042`
- … 8 more parameter(s) in the action modal
```

**Analogy.** Handing a finished envelope to the mailroom.

**In combination.** Retrieve email messages, Process or Send email, no Outlook instance required.
