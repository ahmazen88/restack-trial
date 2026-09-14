# Workstation

Control printers, screenshots, resolution, lock, logoff, and shutdown.

This page documents every **native action** in this group (13 items).

## Actions

### Control screen saver

- **Inventory id:** `workstation/control-screen-saver`
- **Kind:** native-action
- **Purpose:** Enables, disables, starts or stops the screensaver.
- **Key inputs:** `Screen saver action` (Enable, Disable, Start, Stop)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Control screen saver](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#controlscreensaver)

### Empty recycle bin

- **Inventory id:** `workstation/empty-recycle-bin`
- **Kind:** native-action
- **Purpose:** Deletes all files from the windows recycle bin.
- **Key inputs:** None
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Empty recycle bin](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#emptyrecyclebin)

### Get default printer

- **Inventory id:** `workstation/get-default-printer`
- **Kind:** native-action
- **Purpose:** Reads default printer into a flow variable.
- **Key inputs:** None
- **Produces:** `PrinterName` (Text value)
- **Exceptions:** `Can't get default printer`
- **Microsoft Learn:** [Get default printer](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#getdefaultprinter)

### Get screen resolution

- **Inventory id:** `workstation/get-screen-resolution`
- **Kind:** native-action
- **Purpose:** Reads screen resolution into a flow variable.
- **Key inputs:** `Monitor number` (Numeric value)
- **Produces:** `MonitorWidth` (Numeric value); `MonitorHeight` (Numeric value); `MonitorBitCount` (Numeric value); `MonitorFrequency` (Numeric value)
- **Exceptions:** `Failed to get the screen's resolution`
- **Microsoft Learn:** [Get screen resolution](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#getscreenresolution)

### Lock workstation

- **Inventory id:** `workstation/lock-workstation`
- **Kind:** native-action
- **Purpose:** Locks the workstation's display to protect it from unauthorized use.
- **Key inputs:** None
- **Produces:** None listed
- **Exceptions:** `Can't lock the computer in non interactive mode`; `Can't lock the computer`
- **Microsoft Learn:** [Lock workstation](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#lockworkstation)

### Log off user

- **Inventory id:** `workstation/log-off-user`
- **Kind:** native-action
- **Purpose:** Logs off the current user.
- **Key inputs:** `Force log off` (Boolean value)
- **Produces:** None listed
- **Exceptions:** `Can't log off user in non interactive mode`; `Can't log off the current user`
- **Microsoft Learn:** [Log off user](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#logoffuser)

### Play sound

- **Inventory id:** `workstation/play-sound`
- **Kind:** native-action
- **Purpose:** Plays a system sound or a wav file.
- **Key inputs:** `Play sound from` (System, WAV file); `Sound to play` (Asterisk, Beep, Exclamation, Hand, Question); `File to play` (File)
- **Produces:** None listed
- **Exceptions:** `Can't find sound file`; `Invalid sound file`
- **Microsoft Learn:** [Play sound](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#playsoundbase)

### Print document

- **Inventory id:** `workstation/print-document`
- **Kind:** native-action
- **Purpose:** Prints a document on the default printer.
- **Key inputs:** `Document to print` (File)
- **Produces:** None listed
- **Exceptions:** `Document not found`; `Access denied for document`; `Can't print document`
- **Microsoft Learn:** [Print document](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#printdocument)

### Set default printer

- **Inventory id:** `workstation/set-default-printer`
- **Kind:** native-action
- **Purpose:** Writes default printer.
- **Key inputs:** `Printer name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Can't set default printer`
- **Microsoft Learn:** [Set default printer](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#setdefaultprinter)

### Set screen resolution

- **Inventory id:** `workstation/set-screen-resolution`
- **Kind:** native-action
- **Purpose:** Writes screen resolution.
- **Key inputs:** `Monitor number` (Numeric value); `Monitor width` (Numeric value); `Monitor height` (Numeric value); `Monitor bit count` (Numeric value); `Monitor frequency` (Numeric value)
- **Produces:** None listed
- **Exceptions:** `Failed to set the screen's resolution`
- **Microsoft Learn:** [Set screen resolution](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#setscreenresolution)

### Show desktop

- **Inventory id:** `workstation/show-desktop`
- **Kind:** native-action
- **Purpose:** Shows the desktop.
- **Key inputs:** `Operation` (Minimize all windows (show desktop), Restore all windows (undo show desktop))
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Show desktop](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#showdesktop)

### Shutdown computer

- **Inventory id:** `workstation/shutdown-computer`
- **Kind:** native-action
- **Purpose:** Instructs the computer to shut down.
- **Key inputs:** `Action to perform` (Shutdown, Restart, Suspend, Hibernate); `Force` (Boolean value)
- **Produces:** None listed
- **Exceptions:** `Can't shut down the computer`
- **Microsoft Learn:** [Shutdown computer](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#shutdowncomputer)

### Take screenshot

- **Inventory id:** `workstation/take-screenshot`
- **Kind:** native-action
- **Purpose:** Captures screenshot.
- **Key inputs:** `Capture` (All screens, Primary screen, Select screen, Foreground window); `Screen to capture` (Numeric value); `Save screenshot to` (Clipboard, File); `Image file` (File); `Image format` (BMP, EMF, EXIF, GIF, JPG, PNG, TIFF, WMF)
- **Produces:** None listed
- **Exceptions:** `Failed to take screenshot`; `Failed to save screenshot to file`; `Failed to set screenshot to clipboard`; `Failed to get specified screen`
- **Microsoft Learn:** [Take screenshot](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/workstation#takescreenshotbase)
