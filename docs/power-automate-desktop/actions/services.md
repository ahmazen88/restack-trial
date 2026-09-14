# Windows services

Start, stop, pause, resume, and wait for Windows services.

- Actions in this module: **6**
- Official docs: [Windows services actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/services)

## Actions

### If service

Marks the beginning of a conditional block of actions depending on whether a service is running, paused, stopped or installed on the computer.

Designer name: **If service**. Official reference: [Windows services / If service](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/services#ifserviceaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| If service | Choice | Is stopped, Is installed, Isn't installed, Is running, Is paused | Is running |
| Service name | Required | Text value | — |

Produces no variables.

**On error:** `Service not found`, `Can't retrieve status for service`.

---

### Wait for service

Suspend the execution of the automation until a service is running, paused or stopped on the computer.

Designer name: **Wait for service**. Official reference: [Windows services / Wait for service](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/services#waitforserviceaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Wait for service to | Choice | Stop, Start, Pause | Start |
| Service name | Required | Text value | — |

Produces no variables.

**On error:** `Service not found`, `Can't retrieve status for service`.

---

### Start service

Start a stopped Windows service.

Designer name: **Start service**. Official reference: [Windows services / Start service](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/services#start).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Service to start | Required | Text value | — |

Produces no variables.

**On error:** `Service not found`, `Service is already running`, `Can't start service`.

---

### Stop service

Stop a running Windows service.

Designer name: **Stop service**. Official reference: [Windows services / Stop service](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/services#stop).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Service to stop | Required | Text value | — |

Produces no variables.

**On error:** `Service not found`, `Service isn't running`, `Can't stop service`.

---

### Pause service

Pause a running Windows service.

Designer name: **Pause service**. Official reference: [Windows services / Pause service](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/services#pause).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Service to pause | Required | Text value | — |

Produces no variables.

**On error:** `Service not found`, `Service isn't running`, `Can't pause service`.

---

### Resume service

Resume a paused Windows service.

Designer name: **Resume service**. Official reference: [Windows services / Resume service](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/services#resume).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Service to resume | Required | Text value | — |

Produces no variables.

**On error:** `Service not found`, `Service isn't running`, `Can't resume service`.

---
