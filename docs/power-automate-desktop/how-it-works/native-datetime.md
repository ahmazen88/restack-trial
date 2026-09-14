# Date time — how each function works

Native Actions pane module **Date time**.

3 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Add to datetime

- **Id:** `datetime/add-to-datetime`
- **Kind:** native-action
- **Purpose:** Adds to datetime.

**Use case.** In stamping a filename or aging a queue item, drop **Add to datetime** on the canvas. Adds to datetime.

**Demonstration.**

```text
**Add to datetime**
- Datetime: `(set in designer)`
- Add: `1`
- Time unit: `Seconds`
Produces:
- `%ResultedDate%` (Datetime)
```

**Analogy.** One tool in that kit: a wall clock and a desk calendar.

**In combination.** Get current date and time, then Add to datetime or Subtract dates as needed.

### Get current date and time

- **Id:** `datetime/get-current-date-and-time`
- **Kind:** native-action
- **Purpose:** Reads current date and time into a flow variable.

**Use case.** In stamping a filename or aging a queue item, drop **Get current date and time** on the canvas. Reads current date and time into a flow variable.

**Demonstration.**

```text
**Get current date and time**
- Retrieve: `Current date and time`
- Time zone: `System time zone`
- Country/region: `Europe/Bucharest`
- Windows time zone: `(UTC) Coordinated Universal Time`
- Input Type: `Offset`
- Offset: `1`
- Time zone: `INV-1042`
Produces:
- `%CurrentDateTime%` (Datetime)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Get current date and time, then Add to datetime or Subtract dates as needed.

### Subtract dates

- **Id:** `datetime/subtract-dates`
- **Kind:** native-action
- **Purpose:** Finds the time difference between two given dates in days, hours, minutes, or seconds.

**Use case.** In stamping a filename or aging a queue item, drop **Subtract dates** on the canvas. Finds the time difference between two given dates in days, hours, minutes, or seconds.

**Demonstration.**

```text
**Subtract dates**
- From date: `(set in designer)`
- Subtract date: `(set in designer)`
- Get difference in: `Days`
Produces:
- `%TimeDifference%` (Numeric value)
```

**Analogy.** One tool in that kit: a wall clock and a desk calendar.

**In combination.** Get current date and time, then Add to datetime or Subtract dates as needed.
