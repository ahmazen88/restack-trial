# AWS

Automate Amazon EC2 instances, EBS volumes, and snapshots.

This page documents every **native action** in this group (15 items).

## Actions

### Attach volume

- **Inventory id:** `aws/attach-volume`
- **Kind:** native-action
- **Purpose:** Connects the flow to volume that is already running.
- **Key inputs:** `EC2 client` (EC2 client); `Volume ID` (Text value); `Instance ID` (Text value); `Device name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Authentication failed`; `Unauthorized operation`; `Unsupported operation`; `Invalid parameter`; `Invalid volume`; `The resource is in use`; `Amazon service request failed`
- **Microsoft Learn:** [Attach volume](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#attachvolume)

### Create EC2 session

- **Inventory id:** `aws/create-ec2-session`
- **Kind:** native-action
- **Purpose:** Creates EC2 session.
- **Key inputs:** `Access keys` (Boolean value); `Access key ID` (Text value); `Secret` (Direct encrypted input or Text value); `Region endpoint` (Text value); `Profile name` (Text value); `Profile location` (Text value; optional)
- **Produces:** `Ec2Client` (EC2 client)
- **Exceptions:** `Profile doesn't exist`; `Invalid profile`; `Create session failed`
- **Microsoft Learn:** [Create EC2 session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#createec2sessionaction)

### Create snapshot

- **Inventory id:** `aws/create-snapshot`
- **Kind:** native-action
- **Purpose:** Creates snapshot.
- **Key inputs:** `EC2 client` (EC2 client); `Volume ID` (Text value); `Name` (Text value; optional); `Description` (Text value; optional); `Purpose` (Text value; optional)
- **Produces:** `Snapshot` (EBS snapshot)
- **Exceptions:** `Authentication failed`; `Unauthorized operation`; `Invalid volume`; `Resource's limit is exceeded`; `Amazon service request failed`
- **Microsoft Learn:** [Create snapshot](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#createsnapshot)

### Create volume

- **Inventory id:** `aws/create-volume`
- **Kind:** native-action
- **Purpose:** Creates volume.
- **Key inputs:** `EC2 client` (EC2 client); `Name` (Text value; optional); `Purpose` (Text value; optional); `Availability zone` (Text value); `From snapshot` (Boolean value); `Snapshot ID` (Text value); `Volume size` (Text value); `Size` (Text value; optional); `Encrypted` (Boolean value); `Volume type` (Gp2, Standard, Io1, Sc1, St1)
- **Produces:** `Volume` (EBS volume)
- **Exceptions:** `Authentication failed`; `Unauthorized operation`; `Invalid parameter`; `Invalid zone`; `Resource's limit is exceeded`; `Volume type isn't supported in the specified zone`; `Amazon service request failed`
- **Microsoft Learn:** [Create volume](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#createvolumeaction)

### Delete snapshot

- **Inventory id:** `aws/delete-snapshot`
- **Kind:** native-action
- **Purpose:** Deletes snapshot.
- **Key inputs:** `EC2 client` (EC2 client); `Snapshot ID` (Text value)
- **Produces:** None listed
- **Exceptions:** `Authentication failed`; `Unauthorized operation`; `Invalid snapshot ID`; `The resource is in use`; `Amazon service request failed`
- **Microsoft Learn:** [Delete snapshot](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#deletesnapshot)

### Delete volume

- **Inventory id:** `aws/delete-volume`
- **Kind:** native-action
- **Purpose:** Deletes volume.
- **Key inputs:** `EC2 client` (EC2 client); `Volume ID` (Text value)
- **Produces:** None listed
- **Exceptions:** `Authentication failed`; `Unauthorized operation`; `Invalid parameter`; `Invalid volume`; `Incorrect state for the request`; `The resource is in use`; `Amazon service request failed`
- **Microsoft Learn:** [Delete volume](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#deletevolume)

### Describe instances

- **Inventory id:** `aws/describe-instances`
- **Kind:** native-action
- **Purpose:** Returns all the information for the specified EC2 instance(s).
- **Key inputs:** `EC2 client` (EC2 client); `Instance IDs` (List of Text values; optional); `Availability zone` (Text value; optional); `Instance state` (Pending, All, Unknown, Running, Shutting down, Terminated, Stopping, Stopped)
- **Produces:** `Ec2Instances` (List of EC2 instances)
- **Exceptions:** `Authentication failed`; `Unauthorized operation`; `Invalid instance ID`; `Amazon service request failed`
- **Microsoft Learn:** [Describe instances](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#describeec2instance)

### Describe snapshots

- **Inventory id:** `aws/describe-snapshots`
- **Kind:** native-action
- **Purpose:** Describes the specified EBS snapshots available.
- **Key inputs:** `EC2 client` (EC2 client); `Describe snapshots mode` (All snapshots, Snapshots by ID, Snapshots by owner ID, Snapshots by restorable user ID, Snapshots by custom filter); `Snapshot IDs` (List of Text values; optional); `Owner IDs` (List of Text values; optional); `Restorable by user IDs` (List of Text values; optional)
- **Produces:** `EBSSnapshots` (List of EBS snapshots)
- **Exceptions:** `Authentication failed`; `Unauthorized operation`; `Invalid snapshot ID`; `Invalid user ID`; `Amazon service request failed`
- **Microsoft Learn:** [Describe snapshots](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#describesnapshots)

### Describe volumes

- **Inventory id:** `aws/describe-volumes`
- **Kind:** native-action
- **Purpose:** Describe the specified EBS volumes.
- **Key inputs:** `EC2 client` (EC2 client); `Describe volumes mode` (All volumes, Volumes of the specified instance, Volumes with the specified IDs); `Volume IDs` (List of Text values); `Instance ID` (Text value)
- **Produces:** `EBSVolumes` (List of EBS volumes)
- **Exceptions:** `Authentication failed`; `Unauthorized operation`; `Invalid parameter`; `Amazon service request failed`
- **Microsoft Learn:** [Describe volumes](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#describevolumes)

### Detach volume

- **Inventory id:** `aws/detach-volume`
- **Kind:** native-action
- **Purpose:** Detach an EBS volume from an EC2 instance.
- **Key inputs:** `EC2 client` (EC2 client); `Volume ID` (Text value); `Instance ID` (Text value; optional); `Device name` (Text value; optional); `Force detachment` (Boolean value)
- **Produces:** None listed
- **Exceptions:** `Authentication failed`; `Unauthorized operation`; `Unsupported operation`; `Invalid parameter`; `Invalid attempt to detach`; `Incorrect state for the request`; `Amazon service request failed`
- **Microsoft Learn:** [Detach volume](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#detachvolume)

### End EC2 session

- **Inventory id:** `aws/end-ec2-session`
- **Kind:** native-action
- **Purpose:** Ends EC2 session.
- **Key inputs:** `EC2 client` (EC2 client)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [End EC2 session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#endec2session)

### Get available EC2 instances

- **Inventory id:** `aws/get-available-ec2-instances`
- **Kind:** native-action
- **Purpose:** Reads available EC2 instances into a flow variable.
- **Key inputs:** `EC2 client` (EC2 client); `Availability zone` (Text value; optional); `Instance state` (Pending, All, Unknown, Running, Shutting down, Terminated, Stopping, Stopped)
- **Produces:** `Ec2InstancesInfo` (List of EC2 instances info)
- **Exceptions:** `Authentication failed`; `Unauthorized operation`; `Amazon service request failed`
- **Microsoft Learn:** [Get available EC2 instances](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#getavailableec2instances)

### Reboot EC2 instance

- **Inventory id:** `aws/reboot-ec2-instance`
- **Kind:** native-action
- **Purpose:** Reboot EC2 instance(s).
- **Key inputs:** `EC2 client` (EC2 client); `Instance IDs` (List of Text values)
- **Produces:** None listed
- **Exceptions:** `Authentication failed`; `Unauthorized operation`; `Unsupported operation`; `Invalid instance ID`; `Incorrect state for the request`; `Amazon service request failed`
- **Microsoft Learn:** [Reboot EC2 instance](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#rebootec2instance)

### Start EC2 instance

- **Inventory id:** `aws/start-ec2-instance`
- **Kind:** native-action
- **Purpose:** Starts EC2 instance.
- **Key inputs:** `EC2 client` (EC2 client); `Instance IDs` (List of Text values)
- **Produces:** `StartingEc2Instances` (List of Instance state changes)
- **Exceptions:** `Authentication failed`; `Unauthorized operation`; `Invalid instance ID`; `Insufficient capacity`; `Amazon service request failed`
- **Microsoft Learn:** [Start EC2 instance](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#startec2instance)

### Stop EC2 instance

- **Inventory id:** `aws/stop-ec2-instance`
- **Kind:** native-action
- **Purpose:** Stops EC2 instance.
- **Key inputs:** `EC2 client` (EC2 client); `Instance IDs` (List of Text values); `Force stop` (Boolean value); `Hibernation:` (Boolean value)
- **Produces:** `StoppingEc2Instances` (List of Instance state changes)
- **Exceptions:** `Authentication failed`; `Unauthorized operation`; `Unsupported operation`; `Invalid instance ID`; `Amazon service request failed`
- **Microsoft Learn:** [Stop EC2 instance](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/aws#stopec2instance)
