# Azure — how each function works

Native Actions pane module **Azure**.

20 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Attach disk

- **Id:** `azure/attach-disk`
- **Kind:** native-action
- **Purpose:** Connects the flow to disk that is already running.

**Use case.** In a test VM that must be running only during the bot window, drop **Attach disk** on the canvas. Connects the flow to disk that is already running.

**Demonstration.**

```text
**Attach disk**
- Azure client: `(set in designer)`
- Virtual machine name: `INV-1042`
- VM resource group: `INV-1042`
- Disk is managed: `True`
- Disk name: `INV-1042`
- Disk's resource group: `INV-1042`
- Storage account: `INV-1042`
- Container: `INV-1042`
- … 1 more parameter(s) in the action modal
```

**Analogy.** One tool in that kit: borrowing a company laptop from a locker, using it, putting it back.

**In combination.** Create session, start or stop the VM, End session.

### Create managed disk

- **Id:** `azure/create-managed-disk`
- **Kind:** native-action
- **Purpose:** Creates managed disk.

**Use case.** In a test VM that must be running only during the bot window, drop **Create managed disk** on the canvas. Creates managed disk.

**Demonstration.**

```text
**Create managed disk**
- Azure client: `(set in designer)`
- Disk name: `INV-1042`
- Resource group option: `Use existing`
- Resource group name: `INV-1042`
- Location: `INV-1042`
- Source type: `None`
- Snapshot name: `INV-1042`
- Snapshot's resource group: `INV-1042`
- … 5 more parameter(s) in the action modal
Produces:
- `%ManagedDisk%` (Azure managed disk)
```

**Analogy.** One tool in that kit: borrowing a company laptop from a locker, using it, putting it back.

**In combination.** Create session, start or stop the VM, End session.

### Create resource group

- **Id:** `azure/create-resource-group`
- **Kind:** native-action
- **Purpose:** Creates resource group.

**Use case.** In a test VM that must be running only during the bot window, drop **Create resource group** on the canvas. Creates resource group.

**Demonstration.**

```text
**Create resource group**
- Azure client: `(set in designer)`
- Resource group name: `INV-1042`
- Location: `INV-1042`
Produces:
- `%ResourceGroup%` (Azure resource group)
```

**Analogy.** One tool in that kit: borrowing a company laptop from a locker, using it, putting it back.

**In combination.** Create session, start or stop the VM, End session.

### Create session

- **Id:** `azure/create-session`
- **Kind:** native-action
- **Purpose:** Creates session.

**Use case.** In a test VM that must be running only during the bot window, drop **Create session** on the canvas. Creates session.

**Demonstration.**

```text
**Create session**
- Client ID: `INV-1042`
- Client secret: `INV-1042`
- Tenant ID: `INV-1042`
- Subscription ID: `INV-1042`
Produces:
- `%AzureClient%` (Azure client)
```

**Analogy.** One tool in that kit: borrowing a company laptop from a locker, using it, putting it back.

**In combination.** Create session, start or stop the VM, End session.

### Create snapshot

- **Id:** `azure/create-snapshot`
- **Kind:** native-action
- **Purpose:** Creates snapshot.

**Use case.** In a test VM that must be running only during the bot window, drop **Create snapshot** on the canvas. Creates snapshot.

**Demonstration.**

```text
**Create snapshot**
- Azure client: `(set in designer)`
- Snapshot name: `INV-1042`
- Resource group option: `Use existing`
- Resource group: `INV-1042`
- Location: `INV-1042`
- Source disk: `INV-1042`
- Source disk's resource group: `INV-1042`
Produces:
- `%Snapshot%` (Azure snapshot)
```

**Analogy.** One tool in that kit: borrowing a company laptop from a locker, using it, putting it back.

**In combination.** Create session, start or stop the VM, End session.

### Delete disk

- **Id:** `azure/delete-disk`
- **Kind:** native-action
- **Purpose:** Deletes disk.

**Use case.** In a test VM that must be running only during the bot window, drop **Delete disk** on the canvas. Deletes disk.

**Demonstration.**

```text
**Delete disk**
- Azure client: `(set in designer)`
- Disk name: `INV-1042`
- Resource group: `INV-1042`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Create session, start or stop the VM, End session.

### Delete resource group

- **Id:** `azure/delete-resource-group`
- **Kind:** native-action
- **Purpose:** Deletes resource group.

**Use case.** In a test VM that must be running only during the bot window, drop **Delete resource group** on the canvas. Deletes resource group.

**Demonstration.**

```text
**Delete resource group**
- Azure client: `(set in designer)`
- Resource group name: `INV-1042`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Create session, start or stop the VM, End session.

### Delete snapshot

- **Id:** `azure/delete-snapshot`
- **Kind:** native-action
- **Purpose:** Deletes snapshot.

**Use case.** In a test VM that must be running only during the bot window, drop **Delete snapshot** on the canvas. Deletes snapshot.

**Demonstration.**

```text
**Delete snapshot**
- Azure client: `(set in designer)`
- Snapshot name: `INV-1042`
- Resource group: `INV-1042`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Create session, start or stop the VM, End session.

### Describe virtual machine

- **Id:** `azure/describe-virtual-machine`
- **Kind:** native-action
- **Purpose:** Gets all the information for the virtual machine(s) based on the specified criteria.

**Use case.** In a test VM that must be running only during the bot window, drop **Describe virtual machine** on the canvas. Gets all the information for the virtual machine(s) based on the specified criteria.

**Demonstration.**

```text
**Describe virtual machine**
- Azure client: `(set in designer)`
- Describe virtual machines: `All`
- Resource group: `INV-1042`
- Virtual machine name: `INV-1042`
- Status: `Any`
Produces:
- `%VirtualMachines%` (List of Azure virtual machines)
```

**Analogy.** One tool in that kit: borrowing a company laptop from a locker, using it, putting it back.

**In combination.** Create session, start or stop the VM, End session.

### Detach disk

- **Id:** `azure/detach-disk`
- **Kind:** native-action
- **Purpose:** Detaches the disk from the virtual machine with the specified name and resource group.

**Use case.** In a test VM that must be running only during the bot window, drop **Detach disk** on the canvas. Detaches the disk from the virtual machine with the specified name and resource group.

**Demonstration.**

```text
**Detach disk**
- Azure client: `(set in designer)`
- Virtual machine name: `INV-1042`
- Virtual machine's resource group: `INV-1042`
- Disk name: `INV-1042`
- Disk is managed: `True`
```

**Analogy.** One tool in that kit: borrowing a company laptop from a locker, using it, putting it back.

**In combination.** Create session, start or stop the VM, End session.

### End session

- **Id:** `azure/end-session`
- **Kind:** native-action
- **Purpose:** Ends session.

**Use case.** In a test VM that must be running only during the bot window, drop **End session** on the canvas. Ends session.

**Demonstration.**

```text
**End session**
- Azure client: `(set in designer)`
```

**Analogy.** Turning out the lights when the work in that room is done.

**In combination.** Create session, start or stop the VM, End session. Call this only after the last use of the instance so you do not break later steps.

### Get disks

- **Id:** `azure/get-disks`
- **Kind:** native-action
- **Purpose:** Reads disks into a flow variable.

**Use case.** In a test VM that must be running only during the bot window, drop **Get disks** on the canvas. Reads disks into a flow variable.

**Demonstration.**

```text
**Get disks**
- Azure client: `(set in designer)`
- Retrieve disks: `All`
- Resource group: `INV-1042`
- Disk name: `INV-1042`
Produces:
- `%Disks%` (List of Azure managed disks)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Create session, start or stop the VM, End session.

### Get resource groups

- **Id:** `azure/get-resource-groups`
- **Kind:** native-action
- **Purpose:** Reads resource groups into a flow variable.

**Use case.** In a test VM that must be running only during the bot window, drop **Get resource groups** on the canvas. Reads resource groups into a flow variable.

**Demonstration.**

```text
**Get resource groups**
- Azure client: `(set in designer)`
- Resource group name: `INV-1042`
Produces:
- `%ResourceGroups%` (List of Azure resource groups)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Create session, start or stop the VM, End session.

### Get snapshots

- **Id:** `azure/get-snapshots`
- **Kind:** native-action
- **Purpose:** Reads snapshots into a flow variable.

**Use case.** In a test VM that must be running only during the bot window, drop **Get snapshots** on the canvas. Reads snapshots into a flow variable.

**Demonstration.**

```text
**Get snapshots**
- Azure client: `(set in designer)`
- Retrieve snapshots: `All`
- Resource group: `INV-1042`
- Snapshot name: `INV-1042`
Produces:
- `%Snapshots%` (List of Azure snapshots)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Create session, start or stop the VM, End session.

### Get subscriptions

- **Id:** `azure/get-subscriptions`
- **Kind:** native-action
- **Purpose:** Reads subscriptions into a flow variable.

**Use case.** In a test VM that must be running only during the bot window, drop **Get subscriptions** on the canvas. Reads subscriptions into a flow variable.

**Demonstration.**

```text
**Get subscriptions**
- Azure client: `(set in designer)`
Produces:
- `%Subscriptions%` (List of Azure subscriptions)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Create session, start or stop the VM, End session.

### Get virtual machines

- **Id:** `azure/get-virtual-machines`
- **Kind:** native-action
- **Purpose:** Reads virtual machines into a flow variable.

**Use case.** In a test VM that must be running only during the bot window, drop **Get virtual machines** on the canvas. Reads virtual machines into a flow variable.

**Demonstration.**

```text
**Get virtual machines**
- Azure client: `(set in designer)`
- Resource group: `INV-1042`
- Status: `Any`
Produces:
- `%VirtualMachinesInfo%` (List of Azure virtual machine info)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Create session, start or stop the VM, End session.

### Restart virtual machine

- **Id:** `azure/restart-virtual-machine`
- **Kind:** native-action
- **Purpose:** Restarts a virtual machine.

**Use case.** In a test VM that must be running only during the bot window, drop **Restart virtual machine** on the canvas. Restarts a virtual machine.

**Demonstration.**

```text
**Restart virtual machine**
- Azure client: `(set in designer)`
- Virtual machine name: `INV-1042`
- Resource group: `INV-1042`
```

**Analogy.** One tool in that kit: borrowing a company laptop from a locker, using it, putting it back.

**In combination.** Create session, start or stop the VM, End session.

### Shut down virtual machine

- **Id:** `azure/shut-down-virtual-machine`
- **Kind:** native-action
- **Purpose:** Shuts down the operating system of a virtual machine.

**Use case.** In a test VM that must be running only during the bot window, drop **Shut down virtual machine** on the canvas. Shuts down the operating system of a virtual machine.

**Demonstration.**

```text
**Shut down virtual machine**
- Azure client: `(set in designer)`
- Virtual machine name: `INV-1042`
- Resource group: `INV-1042`
```

**Analogy.** One tool in that kit: borrowing a company laptop from a locker, using it, putting it back.

**In combination.** Create session, start or stop the VM, End session.

### Start virtual machine

- **Id:** `azure/start-virtual-machine`
- **Kind:** native-action
- **Purpose:** Starts virtual machine.

**Use case.** In a test VM that must be running only during the bot window, drop **Start virtual machine** on the canvas. Starts virtual machine.

**Demonstration.**

```text
**Start virtual machine**
- Azure client: `(set in designer)`
- Virtual machine name: `INV-1042`
- Resource group: `INV-1042`
```

**Analogy.** One tool in that kit: borrowing a company laptop from a locker, using it, putting it back.

**In combination.** Create session, start or stop the VM, End session.

### Stop virtual machine

- **Id:** `azure/stop-virtual-machine`
- **Kind:** native-action
- **Purpose:** Stops virtual machine.

**Use case.** In a test VM that must be running only during the bot window, drop **Stop virtual machine** on the canvas. Stops virtual machine.

**Demonstration.**

```text
**Stop virtual machine**
- Azure client: `(set in designer)`
- Virtual machine name: `INV-1042`
- Resource group: `INV-1042`
```

**Analogy.** One tool in that kit: borrowing a company laptop from a locker, using it, putting it back.

**In combination.** Create session, start or stop the VM, End session.
