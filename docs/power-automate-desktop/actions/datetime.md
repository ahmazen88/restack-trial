# Date time

Read the current datetime and add or subtract time units.

- Actions in this module: **3**
- Official docs: [Date time actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/datetime)

## Actions

### Add to datetime

Adds (or subtracts) a specific number of seconds, minutes, hours or days to a datetime value.

Designer name: **Add to datetime**. Official reference: [Date time / Add to datetime](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/datetime#add).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Datetime | Required | Datetime | — |
| Add | Required | Numeric value | — |
| Time unit | Choice | Seconds, Minutes, Hours, Days, Months, Years | Seconds |

**Outputs**

| Variable | Type |
|---|---|
| ResultedDate | Datetime |

No module-specific exceptions are listed for this action.

---

### Subtract dates

Finds the time difference between two given dates in days, hours, minutes, or seconds.

Designer name: **Subtract dates**. Official reference: [Date time / Subtract dates](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/datetime#subtract).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| From date | Required | Datetime | — |
| Subtract date | Required | Datetime | — |
| Get difference in | Choice | Seconds, Minutes, Hours, Days | Days |

**Outputs**

| Variable | Type |
|---|---|
| TimeDifference | Numeric value |

No module-specific exceptions are listed for this action.

---

### Get current date and time

Returns the current date or the current date and time.

Designer name: **Get current date and time**. Official reference: [Date time / Get current date and time](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/datetime#getcurrentdatetime).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Retrieve | Choice | Current date and time, Current date only | Current date and time |
| Time zone | Choice | System time zone, Specific time zone (to be deprecated), Windows time zone, Custom input | System time zone |
| Country/region | Required | Text value | Europe/Bucharest |
| Windows time zone | Required | Available Windows time zones | (UTC) Coordinated Universal Time |
| Input Type | Required | Offset, Windows time zone | Offset |
| Offset | Required | Numeric value | N/A |
| Time zone | Required | Text value | N/A |

**Outputs**

| Variable | Type |
|---|---|
| CurrentDateTime | Datetime |

**On error:** `Failed to get current date and time`, `Specified country/region not found`.

---
