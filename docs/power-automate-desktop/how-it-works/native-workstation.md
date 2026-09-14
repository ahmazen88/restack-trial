# Workstation — how each function works

Native Actions pane module **Workstation**.

13 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Control screen saver

- **Id:** `workstation/control-screen-saver`
- **Kind:** native-action
- **Purpose:** Enables, disables, starts or stops the screensaver.

**Use case.** In the physical PC the bot sits on, drop **Control screen saver** on the canvas. Enables, disables, starts or stops the screensaver.

**Demonstration.**

```text
**Control screen saver**
- Screen saver action: `Enable`
```

**Analogy.** One tool in that kit: the room itself: lights, camera, lock, printer.

**In combination.** Take screenshot on failure; Set screen resolution for unattended UI; avoid Shutdown in shared VMs unless intended.

### Empty recycle bin

- **Id:** `workstation/empty-recycle-bin`
- **Kind:** native-action
- **Purpose:** Deletes all files from the windows recycle bin.

**Use case.** In the physical PC the bot sits on, drop **Empty recycle bin** on the canvas. Deletes all files from the windows recycle bin.

**Demonstration.**

```text
**Empty recycle bin**
- (no inputs)
```

**Analogy.** One tool in that kit: the room itself: lights, camera, lock, printer.

**In combination.** Take screenshot on failure; Set screen resolution for unattended UI; avoid Shutdown in shared VMs unless intended.

### Get default printer

- **Id:** `workstation/get-default-printer`
- **Kind:** native-action
- **Purpose:** Reads default printer into a flow variable.

**Use case.** In the physical PC the bot sits on, drop **Get default printer** on the canvas. Reads default printer into a flow variable.

**Demonstration.**

```text
**Get default printer**
- (no inputs)
Produces:
- `%PrinterName%` (Text value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Take screenshot on failure; Set screen resolution for unattended UI; avoid Shutdown in shared VMs unless intended.

### Get screen resolution

- **Id:** `workstation/get-screen-resolution`
- **Kind:** native-action
- **Purpose:** Reads screen resolution into a flow variable.

**Use case.** In the physical PC the bot sits on, drop **Get screen resolution** on the canvas. Reads screen resolution into a flow variable.

**Demonstration.**

```text
**Get screen resolution**
- Monitor number: `1`
Produces:
- `%MonitorWidth%` (Numeric value)
- `%MonitorHeight%` (Numeric value)
- `%MonitorBitCount%` (Numeric value)
- `%MonitorFrequency%` (Numeric value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Take screenshot on failure; Set screen resolution for unattended UI; avoid Shutdown in shared VMs unless intended.

### Lock workstation

- **Id:** `workstation/lock-workstation`
- **Kind:** native-action
- **Purpose:** Locks the workstation's display to protect it from unauthorized use.

**Use case.** In the physical PC the bot sits on, drop **Lock workstation** on the canvas. Locks the workstation's display to protect it from unauthorized use.

**Demonstration.**

```text
**Lock workstation**
- (no inputs)
```

**Analogy.** One tool in that kit: the room itself: lights, camera, lock, printer.

**In combination.** Take screenshot on failure; Set screen resolution for unattended UI; avoid Shutdown in shared VMs unless intended.

### Log off user

- **Id:** `workstation/log-off-user`
- **Kind:** native-action
- **Purpose:** Logs off the current user.

**Use case.** In the physical PC the bot sits on, drop **Log off user** on the canvas. Logs off the current user.

**Demonstration.**

```text
**Log off user**
- Force log off: `False`
```

**Analogy.** One tool in that kit: the room itself: lights, camera, lock, printer.

**In combination.** Take screenshot on failure; Set screen resolution for unattended UI; avoid Shutdown in shared VMs unless intended.

### Play sound

- **Id:** `workstation/play-sound`
- **Kind:** native-action
- **Purpose:** Plays a system sound or a wav file.

**Use case.** In the physical PC the bot sits on, drop **Play sound** on the canvas. Plays a system sound or a wav file.

**Demonstration.**

```text
**Play sound**
- Play sound from: `System`
- Sound to play: `Asterisk`
- File to play: `C:\RPA\Invoices\INV-1042.pdf`
```

**Analogy.** One tool in that kit: the room itself: lights, camera, lock, printer.

**In combination.** Take screenshot on failure; Set screen resolution for unattended UI; avoid Shutdown in shared VMs unless intended.

### Print document

- **Id:** `workstation/print-document`
- **Kind:** native-action
- **Purpose:** Prints a document on the default printer.

**Use case.** In the physical PC the bot sits on, drop **Print document** on the canvas. Prints a document on the default printer.

**Demonstration.**

```text
**Print document**
- Document to print: `(set in designer)`
```

**Analogy.** One tool in that kit: the room itself: lights, camera, lock, printer.

**In combination.** Take screenshot on failure; Set screen resolution for unattended UI; avoid Shutdown in shared VMs unless intended.

### Set default printer

- **Id:** `workstation/set-default-printer`
- **Kind:** native-action
- **Purpose:** Writes default printer.

**Use case.** In the physical PC the bot sits on, drop **Set default printer** on the canvas. Writes default printer.

**Demonstration.**

```text
**Set default printer**
- Printer name: `INV-1042`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Take screenshot on failure; Set screen resolution for unattended UI; avoid Shutdown in shared VMs unless intended.

### Set screen resolution

- **Id:** `workstation/set-screen-resolution`
- **Kind:** native-action
- **Purpose:** Writes screen resolution.

**Use case.** In the physical PC the bot sits on, drop **Set screen resolution** on the canvas. Writes screen resolution.

**Demonstration.**

```text
**Set screen resolution**
- Monitor number: `1`
- Monitor width: `1`
- Monitor height: `1`
- Monitor bit count: `1`
- Monitor frequency: `1`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Take screenshot on failure; Set screen resolution for unattended UI; avoid Shutdown in shared VMs unless intended.

### Show desktop

- **Id:** `workstation/show-desktop`
- **Kind:** native-action
- **Purpose:** Shows the desktop.

**Use case.** In the physical PC the bot sits on, drop **Show desktop** on the canvas. Shows the desktop.

**Demonstration.**

```text
**Show desktop**
- Operation: `Minimize all windows (show desktop)`
```

**Analogy.** One tool in that kit: the room itself: lights, camera, lock, printer.

**In combination.** Take screenshot on failure; Set screen resolution for unattended UI; avoid Shutdown in shared VMs unless intended.

### Shutdown computer

- **Id:** `workstation/shutdown-computer`
- **Kind:** native-action
- **Purpose:** Instructs the computer to shut down.

**Use case.** In the physical PC the bot sits on, drop **Shutdown computer** on the canvas. Instructs the computer to shut down.

**Demonstration.**

```text
**Shutdown computer**
- Action to perform: `Shutdown`
- Force: `False`
```

**Analogy.** One tool in that kit: the room itself: lights, camera, lock, printer.

**In combination.** Take screenshot on failure; Set screen resolution for unattended UI; avoid Shutdown in shared VMs unless intended.

### Take screenshot

- **Id:** `workstation/take-screenshot`
- **Kind:** native-action
- **Purpose:** Captures screenshot.

**Use case.** In the physical PC the bot sits on, drop **Take screenshot** on the canvas. Captures screenshot.

**Demonstration.**

```text
**Take screenshot**
- Capture: `All screens`
- Screen to capture: `1`
- Save screenshot to: `Clipboard`
- Image file: `C:\RPA\Invoices\INV-1042.pdf`
- Image format: `BMP`
```

**Analogy.** One tool in that kit: the room itself: lights, camera, lock, printer.

**In combination.** Take screenshot on failure; Set screen resolution for unattended UI; avoid Shutdown in shared VMs unless intended.
