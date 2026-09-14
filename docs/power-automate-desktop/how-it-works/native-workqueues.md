# Work queues — how each function works

Native Actions pane module **Work queues**.

5 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Add multiple work queue items

- **Id:** `workqueues/add-multiple-work-queue-items`
- **Kind:** native-action
- **Purpose:** Adds multiple work queue items.

**Use case.** In many unattended machines sharing one pile of work, drop **Add multiple work queue items** on the canvas. Adds multiple work queue items.

**Demonstration.**

```text
**Add multiple work queue items**
- ----------: `---------------`
- **Work queue**: `INV-1042`
- **Work queue item data**: `%InvoiceTable%`
Produces:
- `%----------%` (------)
- `%**FailedWorkQueueItems**%` (No)
- `%**HasFailedItems**%` (No)
- `%**SuccessfulWorkQueueItems**%` (Disabled)
```

**Analogy.** One tool in that kit: a ticket dispenser: take a ticket, do the job, mark it done or return it.

**In combination.** Add work queue item (producer), Process work queue items (consumer), Update work queue item.

### Add work queue item

- **Id:** `workqueues/add-work-queue-item`
- **Kind:** native-action
- **Purpose:** Adds work queue item.

**Use case.** In many unattended machines sharing one pile of work, drop **Add work queue item** on the canvas. Adds work queue item.

**Demonstration.**

```text
**Add work queue item**
- ----------: `---------------`
- **Work queue**: `INV-1042`
- **Priority**: `Normal`
- **Name**: `1`
- **Input**: `1`
- **Expires**: `(set in designer)`
- **Processing notes**: `1`
- **Has unique id or reference**: `1`
Produces:
- `%----------%` (------)
- `%**WorkQueueItem**%` (No)
```

**Analogy.** One tool in that kit: a ticket dispenser: take a ticket, do the job, mark it done or return it.

**In combination.** Add work queue item (producer), Process work queue items (consumer), Update work queue item.

### Get work queue items by filter

- **Id:** `workqueues/get-work-queue-items-by-filter`
- **Kind:** native-action
- **Purpose:** Reads work queue items by filter into a flow variable.

**Use case.** In many unattended machines sharing one pile of work, drop **Get work queue items by filter** on the canvas. Reads work queue items by filter into a flow variable.

**Demonstration.**

```text
**Get work queue items by filter**
- ----------: `---------------`
- **Work queue**: `INV-1042`
- **Filter rows**: `INV-1042`
- **Rows to return**: `5000`
Produces:
- `%----------%` (------)
- `%**WorkQueueItems**%` (No)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Add work queue item (producer), Process work queue items (consumer), Update work queue item.

### Process work queue items

- **Id:** `workqueues/process-work-queue-items`
- **Kind:** native-action
- **Purpose:** Processes work queue items.

**Use case.** Pull the next ticket so several machines can share one backlog.

**Demonstration.**

```text
**Process work queue items**
- -----: `---------------`
- **Work queue**: `INV-1042`
- **Filter rows**: `INV-1042`
- **Overwrite work queue auto-retry configuration**: `False`
- **Max retry count**: `When not overwritten, it uses the default max-retry count defined on the work queue record.`
Produces:
- `%----------%` (------)
- `%**WorkQueueItem**%` (No)
```

**Analogy.** One tool in that kit: a ticket dispenser: take a ticket, do the job, mark it done or return it.

**In combination.** Add work queue item (producer), Process work queue items (consumer), Update work queue item.

### Requeue item with delay

- **Id:** `workqueues/requeue-item-with-delay`
- **Kind:** native-action
- **Purpose:** The **Requeue item with delay** action allows users to readd a queue item being processed in the desktop flow, back into its originating queue.

**Use case.** In many unattended machines sharing one pile of work, drop **Requeue item with delay** on the canvas. The **Requeue item with delay** action allows users to readd a queue item being processed in the desktop flow, back into its originating queue.

**Demonstration.**

```text
**Requeue item with delay**
- ----------: `---------------`
- **Work queue item**: `(set in designer)`
- **Delay until**: `Normal`
- **Expires**: `(set in designer)`
- **Processing notes**: `1`
- **Clear processing notes**: `False`
```

**Analogy.** One tool in that kit: a ticket dispenser: take a ticket, do the job, mark it done or return it.

**In combination.** Add work queue item (producer), Process work queue items (consumer), Update work queue item.
