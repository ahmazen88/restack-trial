# AWS

Manage Amazon EC2, S3, and related AWS resources from a desktop flow.

- Actions in this module: **15**
- Official docs: [AWS actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws)

## Actions

### Start EC2 instance

Start EC2 instance(s).

Designer name: **Start EC2 instance**. Official reference: [AWS / Start EC2 instance](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#startec2instance).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| EC2 client | Required | EC2 client | — |
| Instance IDs | Required | List of Text values | — |

**Outputs**

| Variable | Type |
|---|---|
| StartingEc2Instances | List of Instance state changes |

**On error:** `Authentication failed`, `Unauthorized operation`, `Invalid instance ID`, `Insufficient capacity`, `Amazon service request failed`.

---

### Stop EC2 instance

Stop EC2 instance(s).

Designer name: **Stop EC2 instance**. Official reference: [AWS / Stop EC2 instance](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#stopec2instance).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| EC2 client | Required | EC2 client | — |
| Instance IDs | Required | List of Text values | — |
| Force stop | Choice | Boolean value | False |
| Hibernation: | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| StoppingEc2Instances | List of Instance state changes |

**On error:** `Authentication failed`, `Unauthorized operation`, `Unsupported operation`, `Invalid instance ID`, `Amazon service request failed`.

---

### Reboot EC2 instance

Reboot EC2 instance(s).

Designer name: **Reboot EC2 instance**. Official reference: [AWS / Reboot EC2 instance](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#rebootec2instance).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| EC2 client | Required | EC2 client | — |
| Instance IDs | Required | List of Text values | — |

Produces no variables.

**On error:** `Authentication failed`, `Unauthorized operation`, `Unsupported operation`, `Invalid instance ID`, `Incorrect state for the request`, `Amazon service request failed`.

---

### Get available EC2 instances

Reads information for the relevant EC2 instances.

Designer name: **Get available EC2 instances**. Official reference: [AWS / Get available EC2 instances](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#getavailableec2instances).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| EC2 client | Required | EC2 client | — |
| Availability zone | Optional | Text value | — |
| Instance state | Choice | Pending, All, Unknown, Running, Shutting down, Terminated, Stopping, Stopped | All |

**Outputs**

| Variable | Type |
|---|---|
| Ec2InstancesInfo | List of EC2 instances info |

**On error:** `Authentication failed`, `Unauthorized operation`, `Amazon service request failed`.

---

### Describe instances

Returns all the information for the specified EC2 instance(s).

Designer name: **Describe instances**. Official reference: [AWS / Describe instances](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#describeec2instance).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| EC2 client | Required | EC2 client | — |
| Instance IDs | Optional | List of Text values | — |
| Availability zone | Optional | Text value | — |
| Instance state | Choice | Pending, All, Unknown, Running, Shutting down, Terminated, Stopping, Stopped | All |

**Outputs**

| Variable | Type |
|---|---|
| Ec2Instances | List of EC2 instances |

**On error:** `Authentication failed`, `Unauthorized operation`, `Invalid instance ID`, `Amazon service request failed`.

---

### Create snapshot

Create a snapshot of an EBS volume and stores it in Amazon S3.

Designer name: **Create snapshot**. Official reference: [AWS / Create snapshot](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#createsnapshot).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| EC2 client | Required | EC2 client | — |
| Volume ID | Required | Text value | — |
| Name | Optional | Text value | — |
| Description | Optional | Text value | — |
| Purpose | Optional | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| Snapshot | EBS snapshot |

**On error:** `Authentication failed`, `Unauthorized operation`, `Invalid volume`, `Resource's limit is exceeded`, `Amazon service request failed`.

---

### Describe snapshots

Describes the specified EBS snapshots available.

Designer name: **Describe snapshots**. Official reference: [AWS / Describe snapshots](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#describesnapshots).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| EC2 client | Required | EC2 client | — |
| Describe snapshots mode | Choice | All snapshots, Snapshots by ID, Snapshots by owner ID, Snapshots by restorable user ID, Snapshots by custom filter | All snapshots |
| Snapshot IDs | Optional | List of Text values | — |
| Owner IDs | Optional | List of Text values | — |
| Restorable by user IDs | Optional | List of Text values | — |

**Outputs**

| Variable | Type |
|---|---|
| EBSSnapshots | List of EBS snapshots |

**On error:** `Authentication failed`, `Unauthorized operation`, `Invalid snapshot ID`, `Invalid user ID`, `Amazon service request failed`.

---

### Delete snapshot

Delete the specified snapshot.

Designer name: **Delete snapshot**. Official reference: [AWS / Delete snapshot](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#deletesnapshot).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| EC2 client | Required | EC2 client | — |
| Snapshot ID | Required | Text value | — |

Produces no variables.

**On error:** `Authentication failed`, `Unauthorized operation`, `Invalid snapshot ID`, `The resource is in use`, `Amazon service request failed`.

---

### Create volume

Create an EBS volume.

Designer name: **Create volume**. Official reference: [AWS / Create volume](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#createvolumeaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| EC2 client | Required | EC2 client | — |
| Name | Optional | Text value | — |
| Purpose | Optional | Text value | — |
| Availability zone | Required | Text value | — |
| From snapshot | Choice | Boolean value | False |
| Snapshot ID | Required | Text value | — |
| Volume size | Required | Text value | — |
| Size | Optional | Text value | — |
| Encrypted | Choice | Boolean value | False |
| Volume type | Choice | Gp2, Standard, Io1, Sc1, St1 | Gp2 |

**Outputs**

| Variable | Type |
|---|---|
| Volume | EBS volume |

**On error:** `Authentication failed`, `Unauthorized operation`, `Invalid parameter`, `Invalid zone`, `Resource's limit is exceeded`, `Volume type isn't supported in the specified zone`, `Amazon service request failed`.

---

### Attach volume

Attach an EBS volume to an EC2 instance.

Designer name: **Attach volume**. Official reference: [AWS / Attach volume](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#attachvolume).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| EC2 client | Required | EC2 client | — |
| Volume ID | Required | Text value | — |
| Instance ID | Required | Text value | — |
| Device name | Required | Text value | — |

Produces no variables.

**On error:** `Authentication failed`, `Unauthorized operation`, `Unsupported operation`, `Invalid parameter`, `Invalid volume`, `The resource is in use`, `Amazon service request failed`.

---

### Detach volume

Detach an EBS volume from an EC2 instance.

Designer name: **Detach volume**. Official reference: [AWS / Detach volume](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#detachvolume).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| EC2 client | Required | EC2 client | — |
| Volume ID | Required | Text value | — |
| Instance ID | Optional | Text value | — |
| Device name | Optional | Text value | — |
| Force detachment | Choice | Boolean value | False |

Produces no variables.

**On error:** `Authentication failed`, `Unauthorized operation`, `Unsupported operation`, `Invalid parameter`, `Invalid attempt to detach`, `Incorrect state for the request`, `Amazon service request failed`.

---

### Describe volumes

Describe the specified EBS volumes.

Designer name: **Describe volumes**. Official reference: [AWS / Describe volumes](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#describevolumes).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| EC2 client | Required | EC2 client | — |
| Describe volumes mode | Choice | All volumes, Volumes of the specified instance, Volumes with the specified IDs | All volumes |
| Volume IDs | Required | List of Text values | — |
| Instance ID | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| EBSVolumes | List of EBS volumes |

**On error:** `Authentication failed`, `Unauthorized operation`, `Invalid parameter`, `Amazon service request failed`.

---

### Delete volume

Delete the specified EBS volume.

Designer name: **Delete volume**. Official reference: [AWS / Delete volume](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#deletevolume).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| EC2 client | Required | EC2 client | — |
| Volume ID | Required | Text value | — |

Produces no variables.

**On error:** `Authentication failed`, `Unauthorized operation`, `Invalid parameter`, `Invalid volume`, `Incorrect state for the request`, `The resource is in use`, `Amazon service request failed`.

---

### Create EC2 session

Create an EC2 client to automate EC2 web services.

Designer name: **Create EC2 session**. Official reference: [AWS / Create EC2 session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#createec2sessionaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Access keys | Choice | Boolean value | False |
| Access key ID | Required | Text value | — |
| Secret | Required | Direct encrypted input or Text value | — |
| Region endpoint | Required | Text value | — |
| Profile name | Required | Text value | default |
| Profile location | Optional | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| Ec2Client | EC2 client |

**On error:** `Profile doesn't exist`, `Invalid profile`, `Create session failed`.

---

### End EC2 session

Dispose an open EC2 client.

Designer name: **End EC2 session**. Official reference: [AWS / End EC2 session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#endec2session).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| EC2 client | Required | EC2 client | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---
