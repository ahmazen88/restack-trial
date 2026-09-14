# Windows services

Start, stop, pause, resume, and wait on Windows services.

This page documents every **native action** in this group (6 items).

## Actions

### If service

- **Inventory id:** `services/if-service`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when service.
- **Key inputs:** `If service` (Is stopped, Is installed, Isn't installed, Is running, Is paused); `Service name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Service not found`; `Can't retrieve status for service`
- **Microsoft Learn:** [If service](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/services#ifserviceaction)

### Pause service

- **Inventory id:** `services/pause-service`
- **Kind:** native-action
- **Purpose:** Pause a running Windows service.
- **Key inputs:** `Service to pause` (Text value)
- **Produces:** None listed
- **Exceptions:** `Service not found`; `Service isn't running`; `Can't pause service`
- **Microsoft Learn:** [Pause service](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/services#pause)

### Resume service

- **Inventory id:** `services/resume-service`
- **Kind:** native-action
- **Purpose:** Resume a paused Windows service.
- **Key inputs:** `Service to resume` (Text value)
- **Produces:** None listed
- **Exceptions:** `Service not found`; `Service isn't running`; `Can't resume service`
- **Microsoft Learn:** [Resume service](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/services#resume)

### Start service

- **Inventory id:** `services/start-service`
- **Kind:** native-action
- **Purpose:** Starts service.
- **Key inputs:** `Service to start` (Text value)
- **Produces:** None listed
- **Exceptions:** `Service not found`; `Service is already running`; `Can't start service`
- **Microsoft Learn:** [Start service](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/services#start)

### Stop service

- **Inventory id:** `services/stop-service`
- **Kind:** native-action
- **Purpose:** Stops service.
- **Key inputs:** `Service to stop` (Text value)
- **Produces:** None listed
- **Exceptions:** `Service not found`; `Service isn't running`; `Can't stop service`
- **Microsoft Learn:** [Stop service](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/services#stop)

### Wait for service

- **Inventory id:** `services/wait-for-service`
- **Kind:** native-action
- **Purpose:** Pauses the flow until service.
- **Key inputs:** `Wait for service to` (Stop, Start, Pause); `Service name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Service not found`; `Can't retrieve status for service`
- **Microsoft Learn:** [Wait for service](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/services#waitforserviceaction)
