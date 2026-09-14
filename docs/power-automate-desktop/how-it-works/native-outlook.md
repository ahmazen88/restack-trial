# Outlook — how each function works

Native Actions pane module **Outlook**.

7 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Close Outlook

- **Id:** `outlook/close-outlook`
- **Kind:** native-action
- **Purpose:** Closes outlook.

**Use case.** In the local Outlook profile on the bot PC, drop **Close Outlook** on the canvas. Closes outlook.

**Demonstration.**

```text
**Close Outlook**
- Outlook instance: `%OutlookInstance%`
```

**Analogy.** Turning out the lights when the work in that room is done.

**In combination.** Launch Outlook, Retrieve/Send/Process, Close Outlook. Call this only after the last use of the instance so you do not break later steps.

### Launch Outlook

- **Id:** `outlook/launch-outlook`
- **Kind:** native-action
- **Purpose:** Starts Outlook and returns an instance later actions can reuse.

**Use case.** In the local Outlook profile on the bot PC, drop **Launch Outlook** on the canvas. Starts Outlook and returns an instance later actions can reuse.

**Demonstration.**

```text
**Launch Outlook**
- (no inputs)
Produces:
- `%OutlookInstance%` (Outlook instance)
```

**Analogy.** Unlocking the room before you work. Same family as: your physical inbox tray on the desk.

**In combination.** Launch Outlook, Retrieve/Send/Process, Close Outlook. Keep the produced instance/connection and pass it into every later action in this module.

### Process email messages in Outlook

- **Id:** `outlook/process-email-messages-in-outlook`
- **Kind:** native-action
- **Purpose:** Processes email messages in Outlook.

**Use case.** In the local Outlook profile on the bot PC, drop **Process email messages in Outlook** on the canvas. Processes email messages in Outlook.

**Demonstration.**

```text
**Process email messages in Outlook**
- Outlook instance: `%OutlookInstance%`
- Account: `INV-1042`
- Email messages to process: `%Files%`
- Operation: `Move email messages to mail folder`
- Mail folder: `C:\RPA\Invoices`
```

**Analogy.** One tool in that kit: your physical inbox tray on the desk.

**In combination.** Launch Outlook, Retrieve/Send/Process, Close Outlook.

### Respond to Outlook mail message

- **Id:** `outlook/respond-to-outlook-mail-message`
- **Kind:** native-action
- **Purpose:** Respond to an Outlook message, by replying, replying to all or forwarding it.

**Use case.** In the local Outlook profile on the bot PC, drop **Respond to Outlook mail message** on the canvas. Respond to an Outlook message, by replying, replying to all or forwarding it.

**Demonstration.**

```text
**Respond to Outlook mail message**
- Outlook instance: `%OutlookInstance%`
- Account: `INV-1042`
- Mail message: `Processed by desktop flow Close-P9`
- Response action: `Reply`
- To: `ap@contoso.example`
- CC: `INV-1042`
- BCC: `INV-1042`
- Body: `Processed by desktop flow Close-P9`
- … 1 more parameter(s) in the action modal
```

**Analogy.** One tool in that kit: your physical inbox tray on the desk.

**In combination.** Launch Outlook, Retrieve/Send/Process, Close Outlook.

### Retrieve email messages from Outlook

- **Id:** `outlook/retrieve-email-messages-from-outlook`
- **Kind:** native-action
- **Purpose:** Retrieves email messages from Outlook.

**Use case.** In the local Outlook profile on the bot PC, drop **Retrieve email messages from Outlook** on the canvas. Retrieves email messages from Outlook.

**Demonstration.**

```text
**Retrieve email messages from Outlook**
- Outlook instance: `%OutlookInstance%`
- Account: `INV-1042`
- Mail folder: `C:\RPA\Invoices`
- Retrieve: `All email messages`
- Mark as read: `True`
- From contains: `INV-1042`
- To contains: `INV-1042`
- Subject contains: `Invoice INV-1042 processed`
- … 3 more parameter(s) in the action modal
Produces:
- `%RetrievedEmails%` (List of Outlook mail messages)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Launch Outlook, Retrieve/Send/Process, Close Outlook.

### Save Outlook email messages

- **Id:** `outlook/save-outlook-email-messages`
- **Kind:** native-action
- **Purpose:** Saves outlook email messages.

**Use case.** In the local Outlook profile on the bot PC, drop **Save Outlook email messages** on the canvas. Saves outlook email messages.

**Demonstration.**

```text
**Save Outlook email messages**
- Outlook instance: `%OutlookInstance%`
- Account: `INV-1042`
- Email message(s) to save: `%Files%`
- Save format: `Outlook message format (*.msg)`
- File name: `C:\RPA\Invoices\INV-1042.pdf`
- Save as: `INV-1042`
- Save email message(s) to: `ap@contoso.example`
Produces:
- `%StoredMessagesFiles%` (List of Text values)
```

**Analogy.** One tool in that kit: your physical inbox tray on the desk.

**In combination.** Launch Outlook, Retrieve/Send/Process, Close Outlook.

### Send email through Outlook

- **Id:** `outlook/send-email-through-outlook`
- **Kind:** native-action
- **Purpose:** Sends email through Outlook.

**Use case.** In the local Outlook profile on the bot PC, drop **Send email through Outlook** on the canvas. Sends email through Outlook.

**Demonstration.**

```text
**Send email through Outlook**
- Outlook instance: `%OutlookInstance%`
- Account: `INV-1042`
- Send email from: `ap@contoso.example`
- Send from: `INV-1042`
- To: `ap@contoso.example`
- CC: `INV-1042`
- BCC: `INV-1042`
- Subject: `Invoice INV-1042 processed`
- … 3 more parameter(s) in the action modal
```

**Analogy.** Handing a finished envelope to the mailroom.

**In combination.** Launch Outlook, Retrieve/Send/Process, Close Outlook.
