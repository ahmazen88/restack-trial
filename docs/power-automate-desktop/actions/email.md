# Email

Send and retrieve mail through IMAP, POP3, and SMTP.

- Actions in this module: **3**
- Official docs: [Email actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/email)

## Actions

### Retrieve email messages

Returns email messages from an IMAP server.

Designer name: **Retrieve email messages**. Official reference: [Email / Retrieve email messages](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/email#retrieveemails).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| IMAP server | Required | Text value | — |
| Port | Optional | Numeric value | 993 |
| Enable SSL | Choice | Boolean value | True |
| User name | Required | Text value | — |
| Password | Required | Direct encrypted input or Text value | — |
| Accept untrusted certificates | Choice | Boolean value | False |
| Mail folder | Required | Text value | — |
| Retrieve | Choice | All email messages, Unread email messages only, Read email messages only | All email messages |
| Mark As read | Choice | Boolean value | True |
| "From" field contains | Optional | Text value | — |
| "To" field contains | Optional | Text value | — |
| "Subject" contains | Optional | Text value | — |
| 'Body' contains | Optional | Text value | — |
| Save attachments | Choice | Save attachments, Do not save attachments | Do not save attachments |
| Save attachments into | Required | Folder | — |

**Outputs**

| Variable | Type |
|---|---|
| RetrievedEmails | List of Mail Messages |

**On error:** `Failed to connect to IMAP server`, `Failed to authenticate to the IMAP server`, `Specified mail-folder doesn't exist`, `Failed to save attachments`, `Failed to retrieve emails`.

---

### Process email messages

Moves, deletes or marks as unread an email (or a list of emails) retrieved by a Retrieve emails action.

Designer name: **Process email messages**. Official reference: [Email / Process email messages](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/email#processemails).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| IMAP server | Required | Text value | — |
| Port | Optional | Numeric value | 993 |
| Enable SSL | Choice | Boolean value | True |
| Username | Required | Text value | — |
| Password | Required | Direct encrypted input or Text value | — |
| Accept Untrusted Certificates | Choice | Boolean value | False |
| Email(s) to process | Required | List of Mail Messages | — |
| Operation | Choice | Delete emails from server, Mark emails as unread, Move emails to mail folder, Mark emails as unread and move to mail folder | Move emails to mail folder |
| Mail folder | Required | Text value | — |

Produces no variables.

**On error:** `Failed to connect to IMAP server`, `Specified mail-folder doesn't exist`, `Failed to process emails`.

---

### Send email

Creates and sends a new email message.

Designer name: **Send email**. Official reference: [Email / Send email](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/email#sendemail).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| SMTP server | Required | Text value | — |
| Server port | Optional | Numeric value | 25 |
| Enable SSL | Choice | Boolean value | False |
| SMTP Server needs authentication | Choice | Boolean value | False |
| User name | Required | Text value | — |
| Password | Required | Direct encrypted input or Text value | — |
| Accept untrusted certificates | Choice | Boolean value | False |
| From | Required | Text value | — |
| Sender display name | Optional | Text value | — |
| To | Required | Text value | — |
| CC | Optional | Text value | — |
| BCC | Optional | Text value | — |
| Subject | Optional | Text value | — |
| Body | Optional | Text value | — |
| Body Is HTML | Choice | Boolean value | False |
| Attachment(s) | Optional | List of Files | — |

Produces no variables.

**On error:** `Invalid email address`, `Failed to send email`, `Attachment not found`.

---
