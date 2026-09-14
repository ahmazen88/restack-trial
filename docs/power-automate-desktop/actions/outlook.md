# Outlook

Automate the local Outlook desktop client.

- Actions in this module: **7**
- Official docs: [Outlook actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/outlook)

## Actions

### Launch Outlook

Launch Outlook and create a new Outlook instance.

Designer name: **Launch Outlook**. Official reference: [Outlook / Launch Outlook](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/outlook#launch).

This action has no input parameters.

**Outputs**

| Variable | Type |
|---|---|
| OutlookInstance | Outlook instance |

**On error:** `Failed to launch Outlook`.

---

### Retrieve email messages from Outlook

Retrieve email messages from an Outlook account.

Designer name: **Retrieve email messages from Outlook**. Official reference: [Outlook / Retrieve email messages from Outlook](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/outlook#retrieveemailmessages).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Outlook instance | Required | Outlook instance | — |
| Account | Required | Text value | — |
| Mail folder | Required | Text value | — |
| Retrieve | Choice | All email messages, Unread email messages only, Read email messages only | All email messages |
| Mark as read | Choice | Boolean value | True |
| From contains | Optional | Text value | — |
| To contains | Optional | Text value | — |
| Subject contains | Optional | Text value | — |
| Body contains | Optional | Text value | — |
| Attachments | Choice | Save attachments, Don't save attachments | Don't save attachments |
| Save attachments into | Required | Folder | — |

**Outputs**

| Variable | Type |
|---|---|
| RetrievedEmails | List of Outlook mail messages |

**On error:** `Failed to find Outlook account`, `Mail-folder specified not valid in Outlook`, `Directory for saving attachments not found`, `Failed to retrieve email messages from Outlook`.

---

### Send email through Outlook

Create and send a new email message through Outlook.

Designer name: **Send email through Outlook**. Official reference: [Outlook / Send email through Outlook](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/outlook#sendemailthroughoutlook).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Outlook instance | Required | Outlook instance | — |
| Account | Required | Text value | — |
| Send email from | Choice | Account, Other mailbox | Account |
| Send from | Required | Text value | — |
| To | Required | Text value | — |
| CC | Optional | Text value | — |
| BCC | Optional | Text value | — |
| Subject | Optional | Text value | — |
| Body | Optional | Text value | — |
| Body is HTML | Choice | Boolean value | False |
| Attachment(s) | Optional | List of Files | — |

Produces no variables.

**On error:** `Failed to find Outlook account`, `Failed to send email`, `Attachment not found`.

---

### Process email messages in Outlook

Move or deletes an email (or a list of email messages) retrieved by a 'Retrieve emails from Outlook' action.

Designer name: **Process email messages in Outlook**. Official reference: [Outlook / Process email messages in Outlook](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/outlook#processemailmessages).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Outlook instance | Required | Outlook instance | — |
| Account | Required | Text value | — |
| Email messages to process | Required | List of Outlook mail messages | — |
| Operation | Choice | Delete email messages, Move email messages to mail folder, Mark as unread | Move email messages to mail folder |
| Mail folder | Required | Text value | — |

Produces no variables.

**On error:** `Failed to find Outlook account`, `Specified mail-folder doesn't exist`, `Failed to process email messages in Outlook`.

---

### Save Outlook email messages

Save Outlook email messages given an account.

Designer name: **Save Outlook email messages**. Official reference: [Outlook / Save Outlook email messages](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/outlook#saveoutlookemailmessages).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Outlook instance | Required | Outlook instance | — |
| Account | Required | Text value | — |
| Email message(s) to save | Required | List of Outlook mail messages | — |
| Save format | Choice | Text only (*.txt), Outlook template (*.oft), Outlook message format (*.msg), Outlook message format - Unicode (*.msg), HTML (*.html), MHT files (*.mht) | Outlook message format (*.msg) |
| File name | Choice | Default, Custom | Default |
| Save as | Required | Text value | — |
| Save email message(s) to | Required | Folder | — |

**Outputs**

| Variable | Type |
|---|---|
| StoredMessagesFiles | List of Text values |

**On error:** `Failed to find Outlook account`, `Directory not found`, `Email message is deleted or moved to another folder`, `Failed to save email message(s)`.

---

### Respond to Outlook mail message

Respond to an Outlook message, by replying, replying to all or forwarding it.

Designer name: **Respond to Outlook mail message**. Official reference: [Outlook / Respond to Outlook mail message](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/outlook#respondtomailmessage).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Outlook instance | Required | Outlook instance | — |
| Account | Required | Text value | — |
| Mail message | Required | Outlook mail message | — |
| Response action | Choice | Reply, Reply all, Forward | Reply |
| To | Required | Text value | — |
| CC | Optional | Text value | — |
| BCC | Optional | Text value | — |
| Body | Optional | Text value | — |
| Attachment(s) | Optional | List of Files | — |

Produces no variables.

**On error:** `Failed to find Outlook account`, `Failed to send email`, `Attachment not found`.

---

### Close Outlook

Close a previously launched Outlook instance.

Designer name: **Close Outlook**. Official reference: [Outlook / Close Outlook](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/outlook#close).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Outlook instance | Required | Outlook instance | — |

Produces no variables.

**On error:** `Failed to close Outlook instance`.

---
