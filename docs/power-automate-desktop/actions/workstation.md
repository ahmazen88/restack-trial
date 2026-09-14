# Workstation

Control the local workstation: screenshots, printers, lock, shutdown.

- Actions in this module: **13**
- Official docs: [Workstation actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation)

## Actions

### Print document

Prints a document on the default printer.

Designer name: **Print document**. Official reference: [Workstation / Print document](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#printdocument).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Document to print | Required | File | — |

Produces no variables.

**On error:** `Document not found`, `Access denied for document`, `Can't print document`.

---

### Get default printer

Reads the name of the default printer.

Designer name: **Get default printer**. Official reference: [Workstation / Get default printer](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#getdefaultprinter).

This action has no input parameters.

**Outputs**

| Variable | Type |
|---|---|
| PrinterName | Text value |

**On error:** `Can't get default printer`.

---

### Set default printer

Writes a printer as the default printer.

Designer name: **Set default printer**. Official reference: [Workstation / Set default printer](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#setdefaultprinter).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Printer name | Required | Text value | — |

Produces no variables.

**On error:** `Can't set default printer`.

---

### Show desktop

Shows the desktop.

Designer name: **Show desktop**. Official reference: [Workstation / Show desktop](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#showdesktop).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Operation | Choice | Minimize all windows (show desktop), Restore all windows (undo show desktop) | Minimize all windows (show desktop) |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Lock workstation

Locks the workstation's display to protect it from unauthorized use.

Designer name: **Lock workstation**. Official reference: [Workstation / Lock workstation](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#lockworkstation).

This action has no input parameters.

Produces no variables.

**On error:** `Can't lock the computer in non interactive mode`, `Can't lock the computer`.

---

### Play sound

Plays a system sound or a wav file.

Designer name: **Play sound**. Official reference: [Workstation / Play sound](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#playsoundbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Play sound from | Choice | System, WAV file | System |
| Sound to play | Choice | Asterisk, Beep, Exclamation, Hand, Question | Asterisk |
| File to play | Required | File | — |

Produces no variables.

**On error:** `Can't find sound file`, `Invalid sound file`.

---

### Empty recycle bin

Deletes all files from the windows recycle bin.

Designer name: **Empty recycle bin**. Official reference: [Workstation / Empty recycle bin](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#emptyrecyclebin).

This action has no input parameters.

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Take screenshot

Takes a screenshot of the foreground window or the specified screen and saves the image in a file or to the clipboard.

Designer name: **Take screenshot**. Official reference: [Workstation / Take screenshot](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#takescreenshotbase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Capture | Choice | All screens, Primary screen, Select screen, Foreground window | All screens |
| Screen to capture | Required | Numeric value | — |
| Save screenshot to | Choice | Clipboard, File | Clipboard |
| Image file | Required | File | — |
| Image format | Choice | BMP, EMF, EXIF, GIF, JPG, PNG, TIFF, WMF | BMP |

Produces no variables.

**On error:** `Failed to take screenshot`, `Failed to save screenshot to file`, `Failed to set screenshot to clipboard`, `Failed to get specified screen`.

---

### Control screen saver

Enables, disables, starts or stops the screensaver.

Designer name: **Control screen saver**. Official reference: [Workstation / Control screen saver](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#controlscreensaver).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Screen saver action | Choice | Enable, Disable, Start, Stop | Enable |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Get screen resolution

Reads the width, height, bit count and frequency of a selected monitor.

Designer name: **Get screen resolution**. Official reference: [Workstation / Get screen resolution](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#getscreenresolution).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Monitor number | Required | Numeric value | — |

**Outputs**

| Variable | Type |
|---|---|
| MonitorWidth | Numeric value |
| MonitorHeight | Numeric value |
| MonitorBitCount | Numeric value |
| MonitorFrequency | Numeric value |

**On error:** `Failed to get the screen's resolution`.

---

### Set screen resolution

Writes the width, height, bit count and frequency of a selected monitor during an attended desktop flow run.

Designer name: **Set screen resolution**. Official reference: [Workstation / Set screen resolution](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#setscreenresolution).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Monitor number | Required | Numeric value | — |
| Monitor width | Required | Numeric value | — |
| Monitor height | Required | Numeric value | — |
| Monitor bit count | Required | Numeric value | — |
| Monitor frequency | Required | Numeric value | — |

Produces no variables.

**On error:** `Failed to set the screen's resolution`.

---

### Log off user

Logs off the current user.

Designer name: **Log off user**. Official reference: [Workstation / Log off user](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#logoffuser).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Force log off | Choice | Boolean value | False |

Produces no variables.

**On error:** `Can't log off user in non interactive mode`, `Can't log off the current user`.

---

### Shutdown computer

Instructs the computer to shut down.

Designer name: **Shutdown computer**. Official reference: [Workstation / Shutdown computer](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#shutdowncomputer).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Action to perform | Choice | Shutdown, Restart, Suspend, Hibernate | Shutdown |
| Force | Choice | Boolean value | False |

Produces no variables.

**On error:** `Can't shut down the computer`.

---
