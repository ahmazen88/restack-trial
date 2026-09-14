# Windows services — how each function works

Native Actions pane module **Windows services**.

6 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### If service

- **Id:** `services/if-service`
- **Kind:** native-action
- **Purpose:** Opens a conditional branch that runs when service.

**Use case.** In a Windows service the bot depends on, drop **If service** on the canvas. Opens a conditional branch that runs when service.

**Demonstration.**

```text
**If service**
- If service: `Is running`
- Service name: `INV-1042`
Place the actions that should run inside this block, then End.
```

**Analogy.** Checking a condition on a clipboard before you choose a door.

**In combination.** If service / Wait for service, then Start or Stop service. Combine with Else / Else if and End. Put Wait or If file exists before brittle UI/browser steps.

### Pause service

- **Id:** `services/pause-service`
- **Kind:** native-action
- **Purpose:** Pause a running Windows service.

**Use case.** In a Windows service the bot depends on, drop **Pause service** on the canvas. Pause a running Windows service.

**Demonstration.**

```text
**Pause service**
- Service to pause: `INV-1042`
```

**Analogy.** One tool in that kit: checking whether the building boiler is running before you heat the office.

**In combination.** If service / Wait for service, then Start or Stop service.

### Resume service

- **Id:** `services/resume-service`
- **Kind:** native-action
- **Purpose:** Resume a paused Windows service.

**Use case.** In a Windows service the bot depends on, drop **Resume service** on the canvas. Resume a paused Windows service.

**Demonstration.**

```text
**Resume service**
- Service to resume: `INV-1042`
```

**Analogy.** One tool in that kit: checking whether the building boiler is running before you heat the office.

**In combination.** If service / Wait for service, then Start or Stop service.

### Start service

- **Id:** `services/start-service`
- **Kind:** native-action
- **Purpose:** Starts service.

**Use case.** In a Windows service the bot depends on, drop **Start service** on the canvas. Starts service.

**Demonstration.**

```text
**Start service**
- Service to start: `INV-1042`
```

**Analogy.** One tool in that kit: checking whether the building boiler is running before you heat the office.

**In combination.** If service / Wait for service, then Start or Stop service.

### Stop service

- **Id:** `services/stop-service`
- **Kind:** native-action
- **Purpose:** Stops service.

**Use case.** In a Windows service the bot depends on, drop **Stop service** on the canvas. Stops service.

**Demonstration.**

```text
**Stop service**
- Service to stop: `INV-1042`
```

**Analogy.** One tool in that kit: checking whether the building boiler is running before you heat the office.

**In combination.** If service / Wait for service, then Start or Stop service.

### Wait for service

- **Id:** `services/wait-for-service`
- **Kind:** native-action
- **Purpose:** Pauses the flow until service.

**Use case.** In a Windows service the bot depends on, drop **Wait for service** on the canvas. Pauses the flow until service.

**Demonstration.**

```text
**Wait for service**
- Wait for service to: `Start`
- Service name: `INV-1042`
```

**Analogy.** Standing at the microwave until it beeps, so you do not grab a cold plate.

**In combination.** If service / Wait for service, then Start or Stop service.
