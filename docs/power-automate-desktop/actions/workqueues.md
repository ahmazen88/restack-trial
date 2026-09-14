# Work queues

Add, process, and update Power Automate work queue items.

- Actions in this module: **5**
- Official docs: [Work queues actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workqueues)

## Actions

### Process work queue items

The **Process work queue items** action indicates to the queue orchestrator that the machine is ready to process one or more work queue items.

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Work queue | Required | Text | — |
| Filter rows | Optional | Text | — |
| Overwrite work queue auto-retry configuration | Optional | Boolean | False |
| Max retry count | Required | Text value, Numeric value | When not overwritten, it uses the default max-retry count defined on the work queue record. |

**Outputs**

| Variable | Type |
|---|---|
| WorkQueueItem | No |

**On error:** `Work queue not found`, `Work queue paused or stopped`, `Invalid FetchXML`, `Failed to process work queue`.

---

### Add work queue item

The **Add work queue item** action allows users to populate work queue items into a work queue, which has been set up in the flow portal.

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Work queue | Required | Text value | — |
| Priority | Required | High, Normal, Low | Normal |
| Name | Required | Text value, Numeric value | — |
| Input | Required | Text value, Numeric value | — |
| Expires | Optional | Datetime | — |
| Processing notes | Optional | Text value, Numeric value | — |
| Has unique id or reference | Optional | Text value, Numeric value | — |

**Outputs**

| Variable | Type |
|---|---|
| WorkQueueItem | No |

**On error:** `Work queue not found`, `Failed to add item into work queue`.

---

### Add multiple work queue items

The **Add multiple work queue items** action allows users to add one or more work queue items to a work queue based on the data provided as work queue item data table.

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Work queue | Required | Text value | — |
| Work queue item data | Optional | Datatable | — |

**Outputs**

| Variable | Type |
|---|---|
| FailedWorkQueueItems | No |
| HasFailedItems | No |
| SuccessfulWorkQueueItems | Disabled |

**On error:** `Work queue not found`, `Work queue paused or stopped`, `Failed to batch enqueue a list of work queue items`.

---

### Requeue item with delay

The **Requeue item with delay** action allows users to readd a queue item being processed in the desktop flow, back into its originating queue.

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Work queue item | Required | Work queue item | — |
| Delay until | Required | Datetime value | Normal |
| Expires | Optional | Datetime value | — |
| Processing notes | Optional | Text value, Numeric value | — |
| Clear processing notes | Optional | Boolean | False |

Produces no variables.

**On error:** `Work queue not found`, `Work queue item not found`, `Failed to requeue work queue item`.

---

### Get work queue items by filter

The **Get work queue items by filter** action allows users to retrieve one or more work queue items based on a FetchXML filter expression.

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Work queue | Required | Text | — |
| Filter rows | Required | Text | — |
| Rows to return | Required | Number | 5000 |

**Outputs**

| Variable | Type |
|---|---|
| WorkQueueItems | No |

**On error:** `Work queue`, `Filter rows`, `Rows to return`, `Status`, `Queued`, `Processing`, `Processed`, `OnHold`, `Error`, `Status Reason`, `Queued`, `Processing`, `Processed`, `OnHold (Paused)`, `GenericException`, `ITException`, `BusinessException`, `DeadLetter`, `ProcessingTimeout`.

---
