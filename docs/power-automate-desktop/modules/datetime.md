# Date time

Read the clock, add intervals, and subtract dates.

This page documents every **native action** in this group (3 items).

## Actions

### Add to datetime

- **Inventory id:** `datetime/add-to-datetime`
- **Kind:** native-action
- **Purpose:** Adds to datetime.
- **Key inputs:** `Datetime` (Datetime); `Add` (Numeric value); `Time unit` (Seconds, Minutes, Hours, Days, Months, Years)
- **Produces:** `ResultedDate` (Datetime)
- **Exceptions:** none listed
- **Microsoft Learn:** [Add to datetime](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/datetime#add)

### Get current date and time

- **Inventory id:** `datetime/get-current-date-and-time`
- **Kind:** native-action
- **Purpose:** Reads current date and time into a flow variable.
- **Key inputs:** `Retrieve` (Current date and time, Current date only); `Time zone` (System time zone, Specific time zone **(to be deprecated)**, Windows time zone, Custom input); `Country/region` (Text value); `Windows time zone` (Available Windows time zones); `Input Type` (Offset, Windows time zone); `Offset` (Numeric value); `Time zone` (Text value)
- **Produces:** `CurrentDateTime` (Datetime)
- **Exceptions:** `Failed to get current date and time`; `Specified country/region not found`
- **Microsoft Learn:** [Get current date and time](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/datetime#getcurrentdatetime)

### Subtract dates

- **Inventory id:** `datetime/subtract-dates`
- **Kind:** native-action
- **Purpose:** Finds the time difference between two given dates in days, hours, minutes, or seconds.
- **Key inputs:** `From date` (Datetime); `Subtract date` (Datetime); `Get difference in` (Seconds, Minutes, Hours, Days)
- **Produces:** `TimeDifference` (Numeric value)
- **Exceptions:** none listed
- **Microsoft Learn:** [Subtract dates](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/datetime#subtract)
