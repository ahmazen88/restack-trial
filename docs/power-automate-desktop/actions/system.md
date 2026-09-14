# System

Run processes, ping hosts, and manage Windows environment variables.

- Actions in this module: **8**
- Official docs: [System actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system)

## Actions

### If process

Marks the beginning of a conditional block of actions depending on whether a process is running or not.

Designer name: **If process**. Official reference: [System / If process](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system#ifprocessaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| If process | Choice | Is running, Isn't running | Is running |
| Process name | Required | Text value | — |
| From User | Choice | Boolean value | False |
| User name | Required | Text value | — |

Produces no variables.

**On error:** `Can't retrieve list of processes`.

---

### Wait for process

Suspends the execution until a process starts or stops.

Designer name: **Wait for process**. Official reference: [System / Wait for process](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system#waitprocessaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Process name | Required | Text value | — |
| From User | Choice | Boolean value | False |
| User name | Required | Text value | — |
| Wait for process to | Choice | Start, Stop | Start |
| Fail with timeout error | Choice | Boolean value | False |

Produces no variables.

**On error:** `Can't retrieve list of processes`, `Timeout error`.

---

### Run application

Executes an application or opens a document by executing the associated application.

Designer name: **Run application**. Official reference: [System / Run application](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system#runapplicationbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Application path | Required | File | — |
| Command line arguments | Optional | Text value | — |
| Working folder | Optional | Folder | — |
| Window style | Choice | Normal, Hidden, Minimized, Maximized | Normal |
| After application launch | Choice | Continue immediately, Wait for application to load, Wait for application to complete | Continue immediately |
| Timeout | Optional | Numeric value | 0 |

**Outputs**

| Variable | Type |
|---|---|
| AppProcessId | Numeric value |
| AppExitCode | Numeric value |
| WindowHandle | Numeric value |

**On error:** `File or application not found`, `Access denied for application or File`, `Can't retrieve application's main window handle`, `Can't execute application or open file`.

---

### Terminate process

Immediately stops a running process.

Designer name: **Terminate process**. Official reference: [System / Terminate process](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system#terminateprocess).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Specify process by | Choice | Process ID, Process name | Process name |
| Process ID | Required | Numeric value | — |
| Process name | Required | Text value | — |
| From User | Choice | Boolean value | False |
| User name | Required | Text value | — |

Produces no variables.

**On error:** `Process with specified ID not running`, `Failed to terminate process`.

---

### Ping

Sends a message to determine whether a remote computer is accessible over the network.

Designer name: **Ping**. Official reference: [System / Ping](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system#ping).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Host name | Required | Text value | — |
| Timeout | Optional | Numeric value | 5000 |

**Outputs**

| Variable | Type |
|---|---|
| PingResult | Text value |
| RoundTripTime | Numeric value |

**On error:** `Can't complete ping action`.

---

### Set Windows environment variable

Writes an environment variable to a given value.

Designer name: **Set Windows environment variable**. Official reference: [System / Set Windows environment variable](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system#setenvironmentvariable).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Environment variable name | Required | Text value | — |
| New environment variable value | Required | Text value | — |
| Type | Choice | User, System | User |

Produces no variables.

**On error:** `Indicates a problem setting the environment variable's value`, `Insufficient permissions`.

---

### Get Windows environment variable

Returns the value of an environment variable.

Designer name: **Get Windows environment variable**. Official reference: [System / Get Windows environment variable](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system#getenvironmentvariable).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Environment variable name | Required | Text value | — |
| Search for variable only in scope | Choice | Boolean value | False |
| Scope | Choice | User, System | User |

**Outputs**

| Variable | Type |
|---|---|
| EnvironmentVariableValue | Text value |

**On error:** `Environment variable doesn't exist`, `Insufficient permissions`.

---

### Delete Windows environment variable

Deletes an environment variable from a given scope.

Designer name: **Delete Windows environment variable**. Official reference: [System / Delete Windows environment variable](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system#deleteenvironmentvariable).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Environment variable name | Required | Text value | — |
| Type | Choice | User, System | User |

Produces no variables.

**On error:** `Failed to delete environment variable`, `Insufficient permissions`.

---
