# Terminal emulation

Automate mainframe and terminal sessions (HLLAPI / terminal emulators).

- Actions in this module: **8**
- Official docs: [Terminal emulation actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/terminalemulation)

## Actions

### Open terminal session

Open a new terminal session.

Designer name: **Open terminal session**. Official reference: [Terminal emulation / Open terminal session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/terminalemulation#openterminalsession).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Provider | Choice | Micro focus reflection, HLLAPI | Micro focus reflection |
| HLLAPI DLL path | Required | File | — |
| Installation path | Required | Folder | — |
| Configuration | Choice | Existing profile, Specify connection | Existing profile |
| Session name | Required | Text value | — |
| Host type | Choice | IBM 3270, IBM 5250 | IBM 3270 |
| Profile | Required | File | — |
| Host address | Required | Text value | — |
| Port | Required | Numeric value | — |
| Attach to running session | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| TerminalSession | Terminal session |

**On error:** `Error communicating with the emulator`, `Profile error`.

---

### Close terminal session

Close an open terminal session.

Designer name: **Close terminal session**. Official reference: [Terminal emulation / Close terminal session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/terminalemulation#closesession).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Terminal session to close | Required | Terminal session | — |

Produces no variables.

**On error:** `Error communicating with the emulator`.

---

### Move cursor on terminal session

Move the terminal's cursor on the specified position.

Designer name: **Move cursor on terminal session**. Official reference: [Terminal emulation / Move cursor on terminal session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/terminalemulation#movecursor).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Terminal session | Required | Terminal session | — |
| Row | Required | Numeric value | — |
| Column | Required | Numeric value | — |

Produces no variables.

**On error:** `Screen position out of bounds`, `Position commands aren't supported by the emulator`, `Operation is unavailable for this session type`, `Error communicating with the emulator`.

---

### Get text from terminal session

Reads text from a terminal session.

Designer name: **Get text from terminal session**. Official reference: [Terminal emulation / Get text from terminal session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/terminalemulation#gettextfromterminalsession).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Terminal session | Required | Terminal session | — |
| Get text from | Choice | Field, Entire screen, Cursor position, Specific position | Field |
| Get field by | Choice | Label, Index, Position | Label |
| Label | Required | Text value | — |
| Index | Required | Numeric value | — |
| Text length | Required | Numeric value | — |
| Row | Required | Numeric value | — |
| Column | Required | Numeric value | — |

**Outputs**

| Variable | Type |
|---|---|
| TerminalText | Text value |

**On error:** `Error communicating with the emulator`, `Field index out of bounds`, `Field label not found`, `Screen position out of bounds`, `No field found at the given position`, `Terminal screen is unformatted`, `Position commands aren't supported by the emulator`, `Operation is unavailable for this session type`.

---

### Set text on terminal session

Writes text on a terminal session.

Designer name: **Set text on terminal session**. Official reference: [Terminal emulation / Set text on terminal session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/terminalemulation#settextonterminalsession).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Terminal session | Required | Terminal session | — |
| Text | Required | Direct encrypted input or Text value | — |
| Set text | Choice | Cursor position, Field | Field |
| Get field by | Choice | Label, Index, Position | Label |
| Label | Required | Text value | — |
| Index | Required | Numeric value | — |
| Row | Required | Numeric value | — |
| Column | Required | Numeric value | — |
| Treat @ character as literal | Choice | Boolean value | False |

Produces no variables.

**On error:** `Error communicating with the emulator`, `Field index out of bounds`, `Field label not found`, `Screen position out of bounds`, `No field found at the given position`, `Terminal screen is unformatted`, `Position commands aren't supported by the emulator`, `Operation is unavailable for this session type`, `Input text was rejected`.

---

### Send key to terminal session

Send a control key to a terminal session.

Designer name: **Send key to terminal session**. Official reference: [Terminal emulation / Send key to terminal session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/terminalemulation#sendkey).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Terminal session | Required | Terminal session | — |
| Control key | Choice | Transmit, Alt cursor, Attention, Backspace, Back tab, Block toggle, Break, Cancel, Center, Clear, Clear comm, Clear display, Clear line, Clear page, Clear partition, Comma, Command line, Command window, Compose, Ctrl+F1, Ctrl+F2, Ctrl+F3, Ctrl+F4, Ctrl+F5, Ctrl+F6, Ctrl+F7, Ctrl+F8, Ctrl+F9, Ctrl+F10, Ctrl+F11, Ctrl+F12, Ctrl+Shift+F1, Ctrl+Shift+F2, Ctrl+Shift+F3, Ctrl+Shift+F4, Ctrl+Shift+F5, Ctrl+Shift+F6, Ctrl+Shift+F7, Ctrl+Shift+F8, Ctrl+Shift+F9, Ctrl+Shift+F10, Ctrl+Shift+F11, Ctrl+Shift+F12, Cursor blink, Cursor select, Decimal, Delete, Delete char, Delete line, Delete word, Destructive back space, Disconnect, Do, Down, Down double, Dup, Duplicate, Edit script, Key end, End of field, Erase EOF, Erase EOL, Erase EOP, Erase input, Escape, ExtGr, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20, F21, F22, F23, F24, F25, F26, F27, F28, F29, F30, F31, F32, F33, F34, F35, F36, F37, F38, F39, F40, F41, F42, F43, F44, F45, F46, F47, F48, Field delimiter, Field exit, Field mark, Field minus, Field plus, Find, Hard reset, Help, Hex, Hex 00, Hex 01, Hex 02, Hex 03, Hex 04, Hex 05, Hex 06, Hex 07, Hex 08, Hex 09, Hex 0A, Hex 0B, Hex 0C, Hex 0D, Hex 0E, Hex 0F, Hex 10, Hex 11, Hex 12, Hex 13, Hex 14, Hex 15, Hex 16, Hex 17, Hex 18, Hex 19, Hex 1A, Hex 1B, Hex 1C, Hex 1D, Hex 1E, Hex 1F, Hex 7F, Hold, Hold clear, Hold set, Home, Home down, Home up, Insert, Insert char, Insert here, Insert line, Insert mode, Invalid key, KeyPad0, KeyPad1, KeyPad2, KeyPad3, KeyPad4, KeyPad5, KeyPad6, KeyPad7, KeyPad8, KeyPad9, Left, Left double, Line feed, Minus, Monitor toggle, New line, Next page, Next screen, Next word, Nul, NumLock, PA1, PA2, PA3, Page, Page down, Page up, Pan left, Pan right, Partition jump, PF1, PF2, PF3, PF4, Plus Cr, Previous word, PrevPage, PrevScreen, Print, Print line, Print Msg, Prent screen, Remove, Replace, Reset, Return, Reserve field, Right, Right double, Roll down, Roll up, Rile line, Run script, Scroll down, Scroll left, Scroll right, Scroll up, Select, Send, Send answer back, Send delete, Send line, Send Msg, Shift+Backspace, Shift+Delete, Shift+Down, Shift+F1, Shift+F2, Shift+F3, Shift+F4, Shift+F5, Shift+F6, Shift+F7, Shift+F8, Shift+F9, Shift+F10, Shift+F11, Shift+F12, Shift+F13, Shift+F14, Shift+F15, Shift F16, Shift+F17, Shift+F18, Shift+F19, Shift+F20, Shift+Home, Shift+Insert, Shift+Left, Shift+Print screen, Shift+Right, Shift+Up, Soft reset, System request, Tab, Tek zoom, Term next page, Term prev page, Test, Text assist begin bold, Text assist begin of line, Text assist begin underline, Text assist bottom of page, Text assist carrier return, Text assist center, Text assist end bold, Text assist end of line, Text assist half index down, Text assist half index up, Text assist insert symbols, Text assist next stop, Text assist next text column, Text assist page end, Text assist required space, Text assist required tab, Text assist stop, Text assist text tab advance, Text assist top of page, Text assist word underline, Trace Toggle, Udk 10, Udk 6, Udk 7, Udk 8, Udk 9, Udk 11, Udk 12, Udk 13, Udk 14, Udk 15, Udk 16, Udk 17, Udk 18, Udk 19, Udk 20, Up, Up double | Transmit |

Produces no variables.

**On error:** `Error communicating with the emulator`, `Key not supported`.

---

### Wait for text on terminal session

Wait for a specific text to appear on a terminal session.

Designer name: **Wait for text on terminal session**. Official reference: [Terminal emulation / Wait for text on terminal session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/terminalemulation#waitfortextonterminalsession).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Terminal session | Required | Terminal session | — |
| Text to wait for | Required | Text value | — |
| Regular expression | Choice | Boolean value | False |
| Wait for text location | Choice | Screen, Field | Screen |
| Get field by | Choice | Label, Index, Position | Label |
| Label | Required | Text value | — |
| Index | Required | Numeric value | — |
| Row | Required | Numeric value | — |
| Column | Required | Numeric value | — |
| Timeout | Optional | Numeric value | 0 |

Produces no variables.

**On error:** `Error communicating with the emulator`, `Field index out of bounds`, `Field label not found`, `Screen position out of bounds`, `No field found at the given position`, `Terminal screen is unformatted`, `Position commands aren't supported by the emulator`, `Operation is unavailable for this session type`, `Timeout expired`.

---

### Search for text on terminal session

Search for all occurrences of a specific text on a terminal session.

Designer name: **Search for text on terminal session**. Official reference: [Terminal emulation / Search for text on terminal session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/terminalemulation#searchfortextonterminalsession).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Terminal session | Required | Terminal session | — |
| Text to search for | Required | Text value | — |
| Regular expression | Choice | Boolean value | False |
| Column size | Required | Numeric value | 80 |

**Outputs**

| Variable | Type |
|---|---|
| FindResults | Datatable |

**On error:** `Error communicating with the emulator`, `Text not found`, `Invalid regex expression`.

---
