# Active Directory — how each function works

Native Actions pane module **Active Directory**.

15 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Close connection

- **Id:** `activedirectory/close-connection`
- **Kind:** native-action
- **Purpose:** Closes connection.

**Use case.** In employee joiners and leavers, drop **Close connection** on the canvas. Closes connection.

**Demonstration.**

```text
**Close connection**
- Parent directory entry: `C:\RPA\Invoices`
```

**Analogy.** Turning out the lights when the work in that room is done.

**In combination.** Connect to server, do the user/group change, Close connection. Call this only after the last use of the instance so you do not break later steps.

### Connect to server

- **Id:** `activedirectory/connect-to-server`
- **Kind:** native-action
- **Purpose:** Connects to an Active Directory server.

**Use case.** In employee joiners and leavers, drop **Connect to server** on the canvas. Connects to an Active Directory server.

**Demonstration.**

```text
**Connect to server**
- LDAP path: `C:\RPA\Invoices\INV-1042.pdf`
- Use authentication: `False`
- Username: `CONTOSO\rpa.bot`
- Password: `%Credential.Password%  (sensitive)`
- Authentication type: `Secure`
Produces:
- `%ParentDirectoryEntry%` (Active Directory entry)
```

**Analogy.** One tool in that kit: the office key-cabinet: connect, change who has a key, then lock it.

**In combination.** Connect to server, do the user/group change, Close connection.

### Create group

- **Id:** `activedirectory/create-group`
- **Kind:** native-action
- **Purpose:** Creates group.

**Use case.** In employee joiners and leavers, drop **Create group** on the canvas. Creates group.

**Demonstration.**

```text
**Create group**
- Parent directory entry: `C:\RPA\Invoices`
- Group name: `INV-1042`
- Location: `INV-1042`
- Description: `INV-1042`
- Group scope: `Global`
- Group type: `Security`
```

**Analogy.** One tool in that kit: the office key-cabinet: connect, change who has a key, then lock it.

**In combination.** Connect to server, do the user/group change, Close connection.

### Create object

- **Id:** `activedirectory/create-object`
- **Kind:** native-action
- **Purpose:** Creates object.

**Use case.** In employee joiners and leavers, drop **Create object** on the canvas. Creates object.

**Demonstration.**

```text
**Create object**
- Parent directory entry: `C:\RPA\Invoices`
- Location: `INV-1042`
- Object type: `Computer`
- Object name: `INV-1042`
```

**Analogy.** One tool in that kit: the office key-cabinet: connect, change who has a key, then lock it.

**In combination.** Connect to server, do the user/group change, Close connection.

### Create user

- **Id:** `activedirectory/create-user`
- **Kind:** native-action
- **Purpose:** Creates user.

**Use case.** In employee joiners and leavers, drop **Create user** on the canvas. Creates user.

**Demonstration.**

```text
**Create user**
- Parent directory entry: `C:\RPA\Invoices`
- Location: `INV-1042`
- First name: `INV-1042`
- Initials: `INV-1042`
- Last name: `INV-1042`
- Username: `CONTOSO\rpa.bot`
- Password: `%Credential.Password%  (sensitive)`
- Password never expires: `False`
- … 1 more parameter(s) in the action modal
```

**Analogy.** One tool in that kit: the office key-cabinet: connect, change who has a key, then lock it.

**In combination.** Connect to server, do the user/group change, Close connection.

### Delete object

- **Id:** `activedirectory/delete-object`
- **Kind:** native-action
- **Purpose:** Deletes object.

**Use case.** In employee joiners and leavers, drop **Delete object** on the canvas. Deletes object.

**Demonstration.**

```text
**Delete object**
- Parent directory entry: `C:\RPA\Invoices`
- Distinguished name: `INV-1042`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Connect to server, do the user/group change, Close connection.

### Get group info

- **Id:** `activedirectory/get-group-info`
- **Kind:** native-action
- **Purpose:** Reads group info into a flow variable.

**Use case.** In employee joiners and leavers, drop **Get group info** on the canvas. Reads group info into a flow variable.

**Demonstration.**

```text
**Get group info**
- Parent directory entry: `C:\RPA\Invoices`
- Distinguished name: `INV-1042`
Produces:
- `%GroupInfo%` (Group info)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Connect to server, do the user/group change, Close connection.

### Get group members

- **Id:** `activedirectory/get-group-members`
- **Kind:** native-action
- **Purpose:** Reads group members into a flow variable.

**Use case.** In employee joiners and leavers, drop **Get group members** on the canvas. Reads group members into a flow variable.

**Demonstration.**

```text
**Get group members**
- Parent directory entry: `C:\RPA\Invoices`
- Distinguished name: `INV-1042`
Produces:
- `%GroupMembers%` (List of Group members)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Connect to server, do the user/group change, Close connection.

### Get user info

- **Id:** `activedirectory/get-user-info`
- **Kind:** native-action
- **Purpose:** Reads user info into a flow variable.

**Use case.** In employee joiners and leavers, drop **Get user info** on the canvas. Reads user info into a flow variable.

**Demonstration.**

```text
**Get user info**
- Parent directory entry: `C:\RPA\Invoices`
- Distinguished name: `INV-1042`
Produces:
- `%UserInfo%` (User info)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Connect to server, do the user/group change, Close connection.

### Modify group

- **Id:** `activedirectory/modify-group`
- **Kind:** native-action
- **Purpose:** Modifies a group in the Active Directory.

**Use case.** In employee joiners and leavers, drop **Modify group** on the canvas. Modifies a group in the Active Directory.

**Demonstration.**

```text
**Modify group**
- Parent directory entry: `C:\RPA\Invoices`
- Distinguished name: `INV-1042`
- Operation: `Rename group`
- New name: `INV-1042`
- User distinguished name: `CONTOSO\rpa.bot`
```

**Analogy.** One tool in that kit: the office key-cabinet: connect, change who has a key, then lock it.

**In combination.** Connect to server, do the user/group change, Close connection.

### Modify user

- **Id:** `activedirectory/modify-user`
- **Kind:** native-action
- **Purpose:** Modify a user in the Active Directory.

**Use case.** In employee joiners and leavers, drop **Modify user** on the canvas. Modify a user in the Active Directory.

**Demonstration.**

```text
**Modify user**
- Parent directory entry: `C:\RPA\Invoices`
- Distinguished name: `INV-1042`
- Operation: `Enable/disable user`
- Enable user: `False`
- New name: `INV-1042`
- New password: `%Credential.Password%  (sensitive)`
```

**Analogy.** One tool in that kit: the office key-cabinet: connect, change who has a key, then lock it.

**In combination.** Connect to server, do the user/group change, Close connection.

### Move object

- **Id:** `activedirectory/move-object`
- **Kind:** native-action
- **Purpose:** Moves object.

**Use case.** In employee joiners and leavers, drop **Move object** on the canvas. Moves object.

**Demonstration.**

```text
**Move object**
- Parent directory entry: `C:\RPA\Invoices`
- Distinguished name: `INV-1042`
- Move to location: `INV-1042`
```

**Analogy.** One tool in that kit: the office key-cabinet: connect, change who has a key, then lock it.

**In combination.** Connect to server, do the user/group change, Close connection.

### Rename object

- **Id:** `activedirectory/rename-object`
- **Kind:** native-action
- **Purpose:** Renames object.

**Use case.** In employee joiners and leavers, drop **Rename object** on the canvas. Renames object.

**Demonstration.**

```text
**Rename object**
- Parent directory entry: `C:\RPA\Invoices`
- Distinguished name: `INV-1042`
- New name: `INV-1042`
```

**Analogy.** One tool in that kit: the office key-cabinet: connect, change who has a key, then lock it.

**In combination.** Connect to server, do the user/group change, Close connection.

### Unlock user

- **Id:** `activedirectory/unlock-user`
- **Kind:** native-action
- **Purpose:** Unlocks an Active Directory user.

**Use case.** In employee joiners and leavers, drop **Unlock user** on the canvas. Unlocks an Active Directory user.

**Demonstration.**

```text
**Unlock user**
- Parent directory entry: `C:\RPA\Invoices`
- Distinguished name: `INV-1042`
```

**Analogy.** One tool in that kit: the office key-cabinet: connect, change who has a key, then lock it.

**In combination.** Connect to server, do the user/group change, Close connection.

### Update user info

- **Id:** `activedirectory/update-user-info`
- **Kind:** native-action
- **Purpose:** Updates user info.

**Use case.** In employee joiners and leavers, drop **Update user info** on the canvas. Updates user info.

**Demonstration.**

```text
**Update user info**
- Parent directory entry: `C:\RPA\Invoices`
- Distinguished name: `INV-1042`
- Display name: `INV-1042`
- First name: `INV-1042`
- Initials: `INV-1042`
- Last name: `INV-1042`
- Title: `INV-1042`
- The email of the user: `ap@contoso.example`
- … 7 more parameter(s) in the action modal
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Connect to server, do the user/group change, Close connection.
