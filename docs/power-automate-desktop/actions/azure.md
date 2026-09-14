# Azure

Manage Azure resource groups, disks, blobs, and related cloud resources.

- Actions in this module: **20**
- Official docs: [Azure actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure)

## Actions

### Get resource groups

Reads the resource groups based on the specified criteria.

Designer name: **Get resource groups**. Official reference: [Azure / Get resource groups](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#getresourcegroups).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |
| Resource group name | Optional | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| ResourceGroups | List of Azure resource groups |

**On error:** `Failed to get the resource groups with the specified criteria`.

---

### Create resource group

Creates a new resource group.

Designer name: **Create resource group**. Official reference: [Azure / Create resource group](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#createresourcegroup).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |
| Resource group name | Required | Text value | — |
| Location | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| ResourceGroup | Azure resource group |

**On error:** `Resource group already exists`, `Failed to create resource group`.

---

### Delete resource group

Deletes the specified resource group and all the contained resources.

Designer name: **Delete resource group**. Official reference: [Azure / Delete resource group](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#deleteresourcegroup).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |
| Resource group name | Required | Text value | — |

Produces no variables.

**On error:** `Failed to delete the resource group`.

---

### Get disks

Reads the disks based on the specified criteria.

Designer name: **Get disks**. Official reference: [Azure / Get disks](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#getdisksaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |
| Retrieve disks | Choice | All, With the specified resource group, With the specified name in all resource groups, With specific name in the specified resource group | All |
| Resource group | Required | Text value | — |
| Disk name | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| Disks | List of Azure managed disks |

**On error:** `Disk wasn't found`, `Resource group wasn't found`, `Failed to get the disks with the specified criteria`.

---

### Attach disk

Attaches an existing disk to the virtual machine with the specified name and resource group.

Designer name: **Attach disk**. Official reference: [Azure / Attach disk](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#attachdisk).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |
| Virtual machine name | Required | Text value | — |
| VM resource group | Required | Text value | — |
| Disk is managed | Choice | Boolean value | True |
| Disk name | Required | Text value | — |
| Disk's resource group | Required | Text value | — |
| Storage account | Required | Text value | — |
| Container | Required | Text value | — |
| VHD file | Required | Text value | — |

Produces no variables.

**On error:** `VM wasn't found`, `Disk wasn't found`, `Both unmanaged and managed disk can't exist together in a VM`, `Failed to attach the disk`.

---

### Detach disk

Detaches the disk from the virtual machine with the specified name and resource group.

Designer name: **Detach disk**. Official reference: [Azure / Detach disk](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#detachdisk).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |
| Virtual machine name | Required | Text value | — |
| Virtual machine's resource group | Required | Text value | — |
| Disk name | Required | Text value | — |
| Disk is managed | Choice | Boolean value | True |

Produces no variables.

**On error:** `VM wasn't found`, `Failed to detach because the disk isn't attached to the specified VM`, `Failed to detach disk`.

---

### Create managed disk

Creates a managed disk with the specified settings.

Designer name: **Create managed disk**. Official reference: [Azure / Create managed disk](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#createmanageddiskaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |
| Disk name | Required | Text value | — |
| Resource group option | Choice | Use existing, Create new | Use existing |
| Resource group name | Required | Text value | — |
| Location | Required | Text value | — |
| Source type | Choice | None, Snapshot, Storage blob | None |
| Snapshot name | Required | Text value | — |
| Snapshot's resource group | Required | Text value | — |
| Blob URL | Required | Text value | — |
| Disk size in GB | Required | Numeric value | — |
| Storage account type | Choice | Standard HDD, Premium SSD, Standard SSD, Ultra disk SSD | Standard HDD |
| Storage account name | Required | Text value | — |
| Availability zone | Optional | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| ManagedDisk | Azure managed disk |

**On error:** `Resource group already exists`, `Resource group wasn't found`, `The resource with the specified name already exists`, `Snapshot wasn't found`, `Failed to create disk`.

---

### Delete disk

Deletes the managed disk with the specified name and resource group.

Designer name: **Delete disk**. Official reference: [Azure / Delete disk](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#deletedisk).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |
| Disk name | Required | Text value | — |
| Resource group | Required | Text value | — |

Produces no variables.

**On error:** `Disk wasn't found`, `Failed to delete the disk because it's attached to a VM`, `Failed to delete disk`.

---

### Get snapshots

Reads the snapshots based on the specified criteria.

Designer name: **Get snapshots**. Official reference: [Azure / Get snapshots](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#getsnapshotsaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |
| Retrieve snapshots | Choice | All, With the specified resource group, With the specified name in all resource groups, With specific name in the specified resource group | All |
| Resource group | Required | Text value | — |
| Snapshot name | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| Snapshots | List of Azure snapshots |

**On error:** `Snapshot wasn't found`, `Resource group wasn't found`, `Failed to get the snapshots with the specified criteria`.

---

### Create snapshot

Creates a snapshot from the specified disk.

Designer name: **Create snapshot**. Official reference: [Azure / Create snapshot](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#createsnapshot).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |
| Snapshot name | Required | Text value | — |
| Resource group option | Choice | Use existing, Create new | Use existing |
| Resource group | Required | Text value | — |
| Location | Required | Text value | — |
| Source disk | Required | Text value | — |
| Source disk's resource group | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| Snapshot | Azure snapshot |

**On error:** `Resource group already exists`, `Resource group wasn't found`, `The resource with the specified name already exists`, `Disk wasn't found`, `Failed to create snapshot`.

---

### Delete snapshot

Deletes the snapshot with the specified name and resource group.

Designer name: **Delete snapshot**. Official reference: [Azure / Delete snapshot](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#deletesnapshot).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |
| Snapshot name | Required | Text value | — |
| Resource group | Required | Text value | — |

Produces no variables.

**On error:** `Snapshot wasn't found`, `Failed to delete snapshot`.

---

### Get virtual machines

Reads the basic information for the virtual machines.

Designer name: **Get virtual machines**. Official reference: [Azure / Get virtual machines](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#getvirtualmachines).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |
| Resource group | Optional | Text value | — |
| Status | Choice | Running, Deallocating, Deallocated, Starting, Stopped, Stopping, Unknown, Any | Any |

**Outputs**

| Variable | Type |
|---|---|
| VirtualMachinesInfo | List of Azure virtual machine info |

**On error:** `Resource group wasn't found`, `Failed to get the VMs with basic information`.

---

### Describe virtual machine

Reads all the information for the virtual machine(s) based on the specified criteria.

Designer name: **Describe virtual machine**. Official reference: [Azure / Describe virtual machine](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#describevirtualmachineaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |
| Describe virtual machines | Choice | All, With the specified resource group, With the specified name in all resource groups, With specific name in the specified resource group | All |
| Resource group | Required | Text value | — |
| Virtual machine name | Required | Text value | — |
| Status | Choice | Running, Deallocating, Deallocated, Starting, Stopped, Stopping, Unknown, Any | Any |

**Outputs**

| Variable | Type |
|---|---|
| VirtualMachines | List of Azure virtual machines |

**On error:** `VM wasn't found`, `Resource group wasn't found`, `Failed to get basic information of the VM(s)`.

---

### Start virtual machine

Starts the virtual machine.

Designer name: **Start virtual machine**. Official reference: [Azure / Start virtual machine](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#startvirtualmachine).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |
| Virtual machine name | Required | Text value | — |
| Resource group | Required | Text value | — |

Produces no variables.

**On error:** `VM wasn't found`, `Failed to start the VM`.

---

### Stop virtual machine

Stops the virtual machine and delocates the related hardware (CPU and memory) and network resources.

Designer name: **Stop virtual machine**. Official reference: [Azure / Stop virtual machine](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#stopvirtualmachine).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |
| Virtual machine name | Required | Text value | — |
| Resource group | Required | Text value | — |

Produces no variables.

**On error:** `VM wasn't found`, `Failed to stop the VM`.

---

### Shut down virtual machine

Shuts down the operating system of a virtual machine.

Designer name: **Shut down virtual machine**. Official reference: [Azure / Shut down virtual machine](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#shutdownvirtualmachine).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |
| Virtual machine name | Required | Text value | — |
| Resource group | Required | Text value | — |

Produces no variables.

**On error:** `VM wasn't found`, `Failed to shut down the VM`.

---

### Restart virtual machine

Restarts a virtual machine.

Designer name: **Restart virtual machine**. Official reference: [Azure / Restart virtual machine](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#restartvirtualmachine).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |
| Virtual machine name | Required | Text value | — |
| Resource group | Required | Text value | — |

Produces no variables.

**On error:** `VM wasn't found`, `Failed to restart the VM`.

---

### Create session

Creates an Azure session.

Designer name: **Create session**. Official reference: [Azure / Create session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#createsessionaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Client ID | Required | Text value | — |
| Client secret | Required | Direct encrypted input or Text value | — |
| Tenant ID | Required | Text value | — |
| Subscription ID | Optional | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| AzureClient | Azure client |

**On error:** `Failed to create Azure client`.

---

### Get subscriptions

Reads subscriptions that the current account can access.

Designer name: **Get subscriptions**. Official reference: [Azure / Get subscriptions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#getsubscriptions).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |

**Outputs**

| Variable | Type |
|---|---|
| Subscriptions | List of Azure subscriptions |

**On error:** `Failed to get the subscriptions with the specified criteria`.

---

### End session

Ends an Azure session.

Designer name: **End session**. Official reference: [Azure / End session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/azure#endsession).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Azure client | Required | Azure client | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---
