# Azure

Create Azure sessions and manage resource groups, VMs, disks, and snapshots.

This page documents every **native action** in this group (20 items).

## Actions

### Attach disk

- **Inventory id:** `azure/attach-disk`
- **Kind:** native-action
- **Purpose:** Connects the flow to disk that is already running.
- **Key inputs:** `Azure client` (Azure client); `Virtual machine name` (Text value); `VM resource group` (Text value); `Disk is managed` (Boolean value); `Disk name` (Text value); `Disk's resource group` (Text value); `Storage account` (Text value); `Container` (Text value); `VHD file` (Text value)
- **Produces:** None listed
- **Exceptions:** `VM wasn't found`; `Disk wasn't found`; `Both unmanaged and managed disk can't exist together in a VM`; `Failed to attach the disk`
- **Microsoft Learn:** [Attach disk](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#attachdisk)

### Create managed disk

- **Inventory id:** `azure/create-managed-disk`
- **Kind:** native-action
- **Purpose:** Creates managed disk.
- **Key inputs:** `Azure client` (Azure client); `Disk name` (Text value); `Resource group option` (Use existing, Create new); `Resource group name` (Text value); `Location` (Text value); `Source type` (None, Snapshot, Storage blob); `Snapshot name` (Text value); `Snapshot's resource group` (Text value); `Blob URL` (Text value); `Disk size in GB` (Numeric value); `Storage account type` (Standard HDD, Premium SSD, Standard SSD, Ultra disk SSD); `Storage account name` (Text value); `Availability zone` (Text value; optional)
- **Produces:** `ManagedDisk` (Azure managed disk)
- **Exceptions:** `Resource group already exists`; `Resource group wasn't found`; `The resource with the specified name already exists`; `Snapshot wasn't found`; `Failed to create disk`
- **Microsoft Learn:** [Create managed disk](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#createmanageddiskaction)

### Create resource group

- **Inventory id:** `azure/create-resource-group`
- **Kind:** native-action
- **Purpose:** Creates resource group.
- **Key inputs:** `Azure client` (Azure client); `Resource group name` (Text value); `Location` (Text value)
- **Produces:** `ResourceGroup` (Azure resource group)
- **Exceptions:** `Resource group already exists`; `Failed to create resource group`
- **Microsoft Learn:** [Create resource group](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#createresourcegroup)

### Create session

- **Inventory id:** `azure/create-session`
- **Kind:** native-action
- **Purpose:** Creates session.
- **Key inputs:** `Client ID` (Text value); `Client secret` (Direct encrypted input or Text value); `Tenant ID` (Text value); `Subscription ID` (Text value; optional)
- **Produces:** `AzureClient` (Azure client)
- **Exceptions:** `Failed to create Azure client`
- **Microsoft Learn:** [Create session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#createsessionaction)

### Create snapshot

- **Inventory id:** `azure/create-snapshot`
- **Kind:** native-action
- **Purpose:** Creates snapshot.
- **Key inputs:** `Azure client` (Azure client); `Snapshot name` (Text value); `Resource group option` (Use existing, Create new); `Resource group` (Text value); `Location` (Text value); `Source disk` (Text value); `Source disk's resource group` (Text value)
- **Produces:** `Snapshot` (Azure snapshot)
- **Exceptions:** `Resource group already exists`; `Resource group wasn't found`; `The resource with the specified name already exists`; `Disk wasn't found`; `Failed to create snapshot`
- **Microsoft Learn:** [Create snapshot](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#createsnapshot)

### Delete disk

- **Inventory id:** `azure/delete-disk`
- **Kind:** native-action
- **Purpose:** Deletes disk.
- **Key inputs:** `Azure client` (Azure client); `Disk name` (Text value); `Resource group` (Text value)
- **Produces:** None listed
- **Exceptions:** `Disk wasn't found`; `Failed to delete the disk because it's attached to a VM`; `Failed to delete disk`
- **Microsoft Learn:** [Delete disk](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#deletedisk)

### Delete resource group

- **Inventory id:** `azure/delete-resource-group`
- **Kind:** native-action
- **Purpose:** Deletes resource group.
- **Key inputs:** `Azure client` (Azure client); `Resource group name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Failed to delete the resource group`
- **Microsoft Learn:** [Delete resource group](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#deleteresourcegroup)

### Delete snapshot

- **Inventory id:** `azure/delete-snapshot`
- **Kind:** native-action
- **Purpose:** Deletes snapshot.
- **Key inputs:** `Azure client` (Azure client); `Snapshot name` (Text value); `Resource group` (Text value)
- **Produces:** None listed
- **Exceptions:** `Snapshot wasn't found`; `Failed to delete snapshot`
- **Microsoft Learn:** [Delete snapshot](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#deletesnapshot)

### Describe virtual machine

- **Inventory id:** `azure/describe-virtual-machine`
- **Kind:** native-action
- **Purpose:** Gets all the information for the virtual machine(s) based on the specified criteria.
- **Key inputs:** `Azure client` (Azure client); `Describe virtual machines` (All, With the specified resource group, With the specified name in all resource groups, With specific name in the specified resource group); `Resource group` (Text value); `Virtual machine name` (Text value); `Status` (Running, Deallocating, Deallocated, Starting, Stopped, Stopping, Unknown, Any)
- **Produces:** `VirtualMachines` (List of Azure virtual machines)
- **Exceptions:** `VM wasn't found`; `Resource group wasn't found`; `Failed to get basic information of the VM(s)`
- **Microsoft Learn:** [Describe virtual machine](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#describevirtualmachineaction)

### Detach disk

- **Inventory id:** `azure/detach-disk`
- **Kind:** native-action
- **Purpose:** Detaches the disk from the virtual machine with the specified name and resource group.
- **Key inputs:** `Azure client` (Azure client); `Virtual machine name` (Text value); `Virtual machine's resource group` (Text value); `Disk name` (Text value); `Disk is managed` (Boolean value)
- **Produces:** None listed
- **Exceptions:** `VM wasn't found`; `Failed to detach because the disk isn't attached to the specified VM`; `Failed to detach disk`
- **Microsoft Learn:** [Detach disk](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#detachdisk)

### End session

- **Inventory id:** `azure/end-session`
- **Kind:** native-action
- **Purpose:** Ends session.
- **Key inputs:** `Azure client` (Azure client)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [End session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#endsession)

### Get disks

- **Inventory id:** `azure/get-disks`
- **Kind:** native-action
- **Purpose:** Reads disks into a flow variable.
- **Key inputs:** `Azure client` (Azure client); `Retrieve disks` (All, With the specified resource group, With the specified name in all resource groups, With specific name in the specified resource group); `Resource group` (Text value); `Disk name` (Text value)
- **Produces:** `Disks` (List of Azure managed disks)
- **Exceptions:** `Disk wasn't found`; `Resource group wasn't found`; `Failed to get the disks with the specified criteria`
- **Microsoft Learn:** [Get disks](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#getdisksaction)

### Get resource groups

- **Inventory id:** `azure/get-resource-groups`
- **Kind:** native-action
- **Purpose:** Reads resource groups into a flow variable.
- **Key inputs:** `Azure client` (Azure client); `Resource group name` (Text value; optional)
- **Produces:** `ResourceGroups` (List of Azure resource groups)
- **Exceptions:** `Failed to get the resource groups with the specified criteria`
- **Microsoft Learn:** [Get resource groups](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#getresourcegroups)

### Get snapshots

- **Inventory id:** `azure/get-snapshots`
- **Kind:** native-action
- **Purpose:** Reads snapshots into a flow variable.
- **Key inputs:** `Azure client` (Azure client); `Retrieve snapshots` (All, With the specified resource group, With the specified name in all resource groups, With specific name in the specified resource group); `Resource group` (Text value); `Snapshot name` (Text value)
- **Produces:** `Snapshots` (List of Azure snapshots)
- **Exceptions:** `Snapshot wasn't found`; `Resource group wasn't found`; `Failed to get the snapshots with the specified criteria`
- **Microsoft Learn:** [Get snapshots](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#getsnapshotsaction)

### Get subscriptions

- **Inventory id:** `azure/get-subscriptions`
- **Kind:** native-action
- **Purpose:** Reads subscriptions into a flow variable.
- **Key inputs:** `Azure client` (Azure client)
- **Produces:** `Subscriptions` (List of Azure subscriptions)
- **Exceptions:** `Failed to get the subscriptions with the specified criteria`
- **Microsoft Learn:** [Get subscriptions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#getsubscriptions)

### Get virtual machines

- **Inventory id:** `azure/get-virtual-machines`
- **Kind:** native-action
- **Purpose:** Reads virtual machines into a flow variable.
- **Key inputs:** `Azure client` (Azure client); `Resource group` (Text value; optional); `Status` (Running, Deallocating, Deallocated, Starting, Stopped, Stopping, Unknown, Any)
- **Produces:** `VirtualMachinesInfo` (List of Azure virtual machine info)
- **Exceptions:** `Resource group wasn't found`; `Failed to get the VMs with basic information`
- **Microsoft Learn:** [Get virtual machines](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#getvirtualmachines)

### Restart virtual machine

- **Inventory id:** `azure/restart-virtual-machine`
- **Kind:** native-action
- **Purpose:** Restarts a virtual machine.
- **Key inputs:** `Azure client` (Azure client); `Virtual machine name` (Text value); `Resource group` (Text value)
- **Produces:** None listed
- **Exceptions:** `VM wasn't found`; `Failed to restart the VM`
- **Microsoft Learn:** [Restart virtual machine](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#restartvirtualmachine)

### Shut down virtual machine

- **Inventory id:** `azure/shut-down-virtual-machine`
- **Kind:** native-action
- **Purpose:** Shuts down the operating system of a virtual machine.
- **Key inputs:** `Azure client` (Azure client); `Virtual machine name` (Text value); `Resource group` (Text value)
- **Produces:** None listed
- **Exceptions:** `VM wasn't found`; `Failed to shut down the VM`
- **Microsoft Learn:** [Shut down virtual machine](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#shutdownvirtualmachine)

### Start virtual machine

- **Inventory id:** `azure/start-virtual-machine`
- **Kind:** native-action
- **Purpose:** Starts virtual machine.
- **Key inputs:** `Azure client` (Azure client); `Virtual machine name` (Text value); `Resource group` (Text value)
- **Produces:** None listed
- **Exceptions:** `VM wasn't found`; `Failed to start the VM`
- **Microsoft Learn:** [Start virtual machine](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#startvirtualmachine)

### Stop virtual machine

- **Inventory id:** `azure/stop-virtual-machine`
- **Kind:** native-action
- **Purpose:** Stops virtual machine.
- **Key inputs:** `Azure client` (Azure client); `Virtual machine name` (Text value); `Resource group` (Text value)
- **Produces:** None listed
- **Exceptions:** `VM wasn't found`; `Failed to stop the VM`
- **Microsoft Learn:** [Stop virtual machine](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#stopvirtualmachine)
