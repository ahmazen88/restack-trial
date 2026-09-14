# System

Run apps, manage processes, ping hosts, and edit environment variables.

This page documents every **native action** in this group (8 items).

## Actions

### Delete Windows environment variable

- **Inventory id:** `system/delete-windows-environment-variable`
- **Kind:** native-action
- **Purpose:** Deletes windows environment variable.
- **Key inputs:** `Environment variable name` (Text value); `Type` (User, System)
- **Produces:** None listed
- **Exceptions:** `Failed to delete environment variable`; `Insufficient permissions`
- **Microsoft Learn:** [Delete Windows environment variable](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system#deleteenvironmentvariable)

### Get Windows environment variable

- **Inventory id:** `system/get-windows-environment-variable`
- **Kind:** native-action
- **Purpose:** Reads windows environment variable into a flow variable.
- **Key inputs:** `Environment variable name` (Text value); `Search for variable only in scope` (Boolean value); `Scope` (User, System)
- **Produces:** `EnvironmentVariableValue` (Text value)
- **Exceptions:** `Environment variable doesn't exist`; `Insufficient permissions`
- **Microsoft Learn:** [Get Windows environment variable](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system#getenvironmentvariable)

### If process

- **Inventory id:** `system/if-process`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when process.
- **Key inputs:** `If process` (Is running, Isn't running); `Process name` (Text value); `From User` (Boolean value); `User name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Can't retrieve list of processes`
- **Microsoft Learn:** [If process](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system#ifprocessaction)

### Ping

- **Inventory id:** `system/ping`
- **Kind:** native-action
- **Purpose:** Checks whether a remote host answers on the network.
- **Key inputs:** `Host name` (Text value); `Timeout` (Numeric value; optional)
- **Produces:** `PingResult` (Text value); `RoundTripTime` (Numeric value)
- **Exceptions:** `Can't complete ping action`
- **Microsoft Learn:** [Ping](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system#ping)

### Run application

- **Inventory id:** `system/run-application`
- **Kind:** native-action
- **Purpose:** Runs application.
- **Key inputs:** `Application path` (File); `Command line arguments` (Text value; optional); `Working folder` (Folder; optional); `Window style` (Normal, Hidden, Minimized, Maximized); `After application launch` (Continue immediately, Wait for application to load, Wait for application to complete); `Timeout` (Numeric value; optional)
- **Produces:** `AppProcessId` (Numeric value); `AppExitCode` (Numeric value); `WindowHandle` (Numeric value)
- **Exceptions:** `File or application not found`; `Access denied for application or File`; `Can't retrieve application's main window handle`; `Can't execute application or open file`
- **Microsoft Learn:** [Run application](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system#runapplicationbase)

### Set Windows environment variable

- **Inventory id:** `system/set-windows-environment-variable`
- **Kind:** native-action
- **Purpose:** Writes windows environment variable.
- **Key inputs:** `Environment variable name` (Text value); `New environment variable value` (Text value); `Type` (User, System)
- **Produces:** None listed
- **Exceptions:** `Indicates a problem setting the environment variable's value`; `Insufficient permissions`
- **Microsoft Learn:** [Set Windows environment variable](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system#setenvironmentvariable)

### Terminate process

- **Inventory id:** `system/terminate-process`
- **Kind:** native-action
- **Purpose:** Immediately stops a running process.
- **Key inputs:** `Specify process by` (Process ID, Process name); `Process ID` (Numeric value); `Process name` (Text value); `From User` (Boolean value); `User name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Process with specified ID not running`; `Failed to terminate process`
- **Microsoft Learn:** [Terminate process](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system#terminateprocess)

### Wait for process

- **Inventory id:** `system/wait-for-process`
- **Kind:** native-action
- **Purpose:** Pauses the flow until process.
- **Key inputs:** `Process name` (Text value); `From User` (Boolean value); `User name` (Text value); `Wait for process to` (Start, Stop); `Fail with timeout error` (Boolean value)
- **Produces:** None listed
- **Exceptions:** `Can't retrieve list of processes`; `Timeout error`
- **Microsoft Learn:** [Wait for process](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system#waitprocessaction)
