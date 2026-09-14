# Work queues

Pull, add, update, requeue, and filter Power Automate work queue items.

This page documents every **native action** in this group (5 items).

## Actions

### Add multiple work queue items

- **Inventory id:** `workqueues/add-multiple-work-queue-items`
- **Kind:** native-action
- **Purpose:** Adds multiple work queue items.
- **Key inputs:** `----------` (---------); `**Work queue**` (Text value); `**Work queue item data**` (Datatable; optional)
- **Produces:** `----------` (------); `**FailedWorkQueueItems**` (No); `**HasFailedItems**` (No); `**SuccessfulWorkQueueItems**` (Disabled)
- **Exceptions:** `**Work queue not found**`; `**Work queue paused or stopped**`; `**Failed to batch enqueue a list of work queue items**`
- **Microsoft Learn:** [Add multiple work queue items](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workqueues)

### Add work queue item

- **Inventory id:** `workqueues/add-work-queue-item`
- **Kind:** native-action
- **Purpose:** Adds work queue item.
- **Key inputs:** `----------` (---------); `**Work queue**` (Text value); `**Priority**` (High, Normal, Low); `**Name**` (Text value, Numeric value); `**Input**` (Text value, Numeric value); `**Expires**` (Datetime; optional); `**Processing notes**` (Text value, Numeric value; optional); `**Has unique id or reference**` (Text value, Numeric value; optional)
- **Produces:** `----------` (------); `**WorkQueueItem**` (No)
- **Exceptions:** `**Work queue not found**`; `**Failed to add item into work queue**`
- **Microsoft Learn:** [Add work queue item](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workqueues)

### Get work queue items by filter

- **Inventory id:** `workqueues/get-work-queue-items-by-filter`
- **Kind:** native-action
- **Purpose:** Reads work queue items by filter into a flow variable.
- **Key inputs:** `----------` (---------); `**Work queue**` (Text); `**Filter rows**` (Text); `**Rows to return**` (Number)
- **Produces:** `----------` (------); `**WorkQueueItems**` (No)
- **Exceptions:** `**Work queue**`; `**Filter rows**`; `**Rows to return**`
- **Microsoft Learn:** [Get work queue items by filter](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workqueues)

### Process work queue items

- **Inventory id:** `workqueues/process-work-queue-items`
- **Kind:** native-action
- **Purpose:** Processes work queue items.
- **Key inputs:** `-----` (-----); `**Work queue**` (Text); `**Filter rows**` (Text; optional); `**Overwrite work queue auto-retry configuration**` (Boolean; optional); `**Max retry count**` (Text value, Numeric value)
- **Produces:** `----------` (------); `**WorkQueueItem**` (No)
- **Exceptions:** `----------`; `**Work queue not found**`; `**Work queue paused or stopped**`; `**Invalid FetchXML**`; `**Failed to process work queue**`
- **Microsoft Learn:** [Process work queue items](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workqueues)

### Requeue item with delay

- **Inventory id:** `workqueues/requeue-item-with-delay`
- **Kind:** native-action
- **Purpose:** The **Requeue item with delay** action allows users to readd a queue item being processed in the desktop flow, back into its originating queue.
- **Key inputs:** `----------` (---------); `**Work queue item**` (Work queue item); `**Delay until**` (Datetime value); `**Expires**` (Datetime value; optional); `**Processing notes**` (Text value, Numeric value; optional); `**Clear processing notes**` (Boolean; optional)
- **Produces:** None listed
- **Exceptions:** `**Work queue not found**`; `**Work queue item not found**`; `**Failed to requeue work queue item**`
- **Microsoft Learn:** [Requeue item with delay](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workqueues)
