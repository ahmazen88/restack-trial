# AWS — how each function works

Native Actions pane module **AWS**.

15 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Attach volume

- **Id:** `aws/attach-volume`
- **Kind:** native-action
- **Purpose:** Connects the flow to volume that is already running.

**Use case.** In non-prod EC2 boxes used for month-end jobs, drop **Attach volume** on the canvas. Connects the flow to volume that is already running.

**Demonstration.**

```text
**Attach volume**
- EC2 client: `(set in designer)`
- Volume ID: `INV-1042`
- Instance ID: `INV-1042`
- Device name: `INV-1042`
```

**Analogy.** One tool in that kit: a warehouse of rented machines you start, snapshot, and shut down.

**In combination.** Create EC2 session, act on instances/volumes, End EC2 session.

### Create EC2 session

- **Id:** `aws/create-ec2-session`
- **Kind:** native-action
- **Purpose:** Creates EC2 session.

**Use case.** In non-prod EC2 boxes used for month-end jobs, drop **Create EC2 session** on the canvas. Creates EC2 session.

**Demonstration.**

```text
**Create EC2 session**
- Access keys: `False`
- Access key ID: `INV-1042`
- Secret: `INV-1042`
- Region endpoint: `https://api.contoso.example/v1/invoices`
- Profile name: `C:\RPA\Invoices\INV-1042.pdf`
- Profile location: `C:\RPA\Invoices\INV-1042.pdf`
Produces:
- `%Ec2Client%` (EC2 client)
```

**Analogy.** One tool in that kit: a warehouse of rented machines you start, snapshot, and shut down.

**In combination.** Create EC2 session, act on instances/volumes, End EC2 session.

### Create snapshot

- **Id:** `aws/create-snapshot`
- **Kind:** native-action
- **Purpose:** Creates snapshot.

**Use case.** In non-prod EC2 boxes used for month-end jobs, drop **Create snapshot** on the canvas. Creates snapshot.

**Demonstration.**

```text
**Create snapshot**
- EC2 client: `(set in designer)`
- Volume ID: `INV-1042`
- Name: `INV-1042`
- Description: `INV-1042`
- Purpose: `INV-1042`
Produces:
- `%Snapshot%` (EBS snapshot)
```

**Analogy.** One tool in that kit: a warehouse of rented machines you start, snapshot, and shut down.

**In combination.** Create EC2 session, act on instances/volumes, End EC2 session.

### Create volume

- **Id:** `aws/create-volume`
- **Kind:** native-action
- **Purpose:** Creates volume.

**Use case.** In non-prod EC2 boxes used for month-end jobs, drop **Create volume** on the canvas. Creates volume.

**Demonstration.**

```text
**Create volume**
- EC2 client: `(set in designer)`
- Name: `INV-1042`
- Purpose: `INV-1042`
- Availability zone: `INV-1042`
- From snapshot: `False`
- Snapshot ID: `INV-1042`
- Volume size: `INV-1042`
- Size: `INV-1042`
- … 2 more parameter(s) in the action modal
Produces:
- `%Volume%` (EBS volume)
```

**Analogy.** One tool in that kit: a warehouse of rented machines you start, snapshot, and shut down.

**In combination.** Create EC2 session, act on instances/volumes, End EC2 session.

### Delete snapshot

- **Id:** `aws/delete-snapshot`
- **Kind:** native-action
- **Purpose:** Deletes snapshot.

**Use case.** In non-prod EC2 boxes used for month-end jobs, drop **Delete snapshot** on the canvas. Deletes snapshot.

**Demonstration.**

```text
**Delete snapshot**
- EC2 client: `(set in designer)`
- Snapshot ID: `INV-1042`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Create EC2 session, act on instances/volumes, End EC2 session.

### Delete volume

- **Id:** `aws/delete-volume`
- **Kind:** native-action
- **Purpose:** Deletes volume.

**Use case.** In non-prod EC2 boxes used for month-end jobs, drop **Delete volume** on the canvas. Deletes volume.

**Demonstration.**

```text
**Delete volume**
- EC2 client: `(set in designer)`
- Volume ID: `INV-1042`
```

**Analogy.** Taking a page out of the folder so it is gone.

**In combination.** Create EC2 session, act on instances/volumes, End EC2 session.

### Describe instances

- **Id:** `aws/describe-instances`
- **Kind:** native-action
- **Purpose:** Returns all the information for the specified EC2 instance(s).

**Use case.** In non-prod EC2 boxes used for month-end jobs, drop **Describe instances** on the canvas. Returns all the information for the specified EC2 instance(s).

**Demonstration.**

```text
**Describe instances**
- EC2 client: `(set in designer)`
- Instance IDs: `%Files%`
- Availability zone: `INV-1042`
- Instance state: `All`
Produces:
- `%Ec2Instances%` (List of EC2 instances)
```

**Analogy.** One tool in that kit: a warehouse of rented machines you start, snapshot, and shut down.

**In combination.** Create EC2 session, act on instances/volumes, End EC2 session.

### Describe snapshots

- **Id:** `aws/describe-snapshots`
- **Kind:** native-action
- **Purpose:** Describes the specified EBS snapshots available.

**Use case.** In non-prod EC2 boxes used for month-end jobs, drop **Describe snapshots** on the canvas. Describes the specified EBS snapshots available.

**Demonstration.**

```text
**Describe snapshots**
- EC2 client: `(set in designer)`
- Describe snapshots mode: `All snapshots`
- Snapshot IDs: `%Files%`
- Owner IDs: `%Files%`
- Restorable by user IDs: `%Files%`
Produces:
- `%EBSSnapshots%` (List of EBS snapshots)
```

**Analogy.** One tool in that kit: a warehouse of rented machines you start, snapshot, and shut down.

**In combination.** Create EC2 session, act on instances/volumes, End EC2 session.

### Describe volumes

- **Id:** `aws/describe-volumes`
- **Kind:** native-action
- **Purpose:** Describe the specified EBS volumes.

**Use case.** In non-prod EC2 boxes used for month-end jobs, drop **Describe volumes** on the canvas. Describe the specified EBS volumes.

**Demonstration.**

```text
**Describe volumes**
- EC2 client: `(set in designer)`
- Describe volumes mode: `All volumes`
- Volume IDs: `%Files%`
- Instance ID: `INV-1042`
Produces:
- `%EBSVolumes%` (List of EBS volumes)
```

**Analogy.** One tool in that kit: a warehouse of rented machines you start, snapshot, and shut down.

**In combination.** Create EC2 session, act on instances/volumes, End EC2 session.

### Detach volume

- **Id:** `aws/detach-volume`
- **Kind:** native-action
- **Purpose:** Detach an EBS volume from an EC2 instance.

**Use case.** In non-prod EC2 boxes used for month-end jobs, drop **Detach volume** on the canvas. Detach an EBS volume from an EC2 instance.

**Demonstration.**

```text
**Detach volume**
- EC2 client: `(set in designer)`
- Volume ID: `INV-1042`
- Instance ID: `INV-1042`
- Device name: `INV-1042`
- Force detachment: `False`
```

**Analogy.** One tool in that kit: a warehouse of rented machines you start, snapshot, and shut down.

**In combination.** Create EC2 session, act on instances/volumes, End EC2 session.

### End EC2 session

- **Id:** `aws/end-ec2-session`
- **Kind:** native-action
- **Purpose:** Ends EC2 session.

**Use case.** In non-prod EC2 boxes used for month-end jobs, drop **End EC2 session** on the canvas. Ends EC2 session.

**Demonstration.**

```text
**End EC2 session**
- EC2 client: `(set in designer)`
```

**Analogy.** Turning out the lights when the work in that room is done.

**In combination.** Create EC2 session, act on instances/volumes, End EC2 session. Call this only after the last use of the instance so you do not break later steps.

### Get available EC2 instances

- **Id:** `aws/get-available-ec2-instances`
- **Kind:** native-action
- **Purpose:** Reads available EC2 instances into a flow variable.

**Use case.** In non-prod EC2 boxes used for month-end jobs, drop **Get available EC2 instances** on the canvas. Reads available EC2 instances into a flow variable.

**Demonstration.**

```text
**Get available EC2 instances**
- EC2 client: `(set in designer)`
- Availability zone: `INV-1042`
- Instance state: `All`
Produces:
- `%Ec2InstancesInfo%` (List of EC2 instances info)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Create EC2 session, act on instances/volumes, End EC2 session.

### Reboot EC2 instance

- **Id:** `aws/reboot-ec2-instance`
- **Kind:** native-action
- **Purpose:** Reboot EC2 instance(s).

**Use case.** In non-prod EC2 boxes used for month-end jobs, drop **Reboot EC2 instance** on the canvas. Reboot EC2 instance(s).

**Demonstration.**

```text
**Reboot EC2 instance**
- EC2 client: `(set in designer)`
- Instance IDs: `%Files%`
```

**Analogy.** One tool in that kit: a warehouse of rented machines you start, snapshot, and shut down.

**In combination.** Create EC2 session, act on instances/volumes, End EC2 session.

### Start EC2 instance

- **Id:** `aws/start-ec2-instance`
- **Kind:** native-action
- **Purpose:** Starts EC2 instance.

**Use case.** In non-prod EC2 boxes used for month-end jobs, drop **Start EC2 instance** on the canvas. Starts EC2 instance.

**Demonstration.**

```text
**Start EC2 instance**
- EC2 client: `(set in designer)`
- Instance IDs: `%Files%`
Produces:
- `%StartingEc2Instances%` (List of Instance state changes)
```

**Analogy.** One tool in that kit: a warehouse of rented machines you start, snapshot, and shut down.

**In combination.** Create EC2 session, act on instances/volumes, End EC2 session.

### Stop EC2 instance

- **Id:** `aws/stop-ec2-instance`
- **Kind:** native-action
- **Purpose:** Stops EC2 instance.

**Use case.** In non-prod EC2 boxes used for month-end jobs, drop **Stop EC2 instance** on the canvas. Stops EC2 instance.

**Demonstration.**

```text
**Stop EC2 instance**
- EC2 client: `(set in designer)`
- Instance IDs: `%Files%`
- Force stop: `False`
- Hibernation:: `False`
Produces:
- `%StoppingEc2Instances%` (List of Instance state changes)
```

**Analogy.** One tool in that kit: a warehouse of rented machines you start, snapshot, and shut down.

**In combination.** Create EC2 session, act on instances/volumes, End EC2 session.
