# Mouse and keyboard — how each function works

Native Actions pane module **Mouse and keyboard**.

12 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Block Input

- **Id:** `mouseandkeyboard/block-input`
- **Kind:** native-action
- **Purpose:** Temporarily blocks the user's mouse and keyboard.

**Use case.** In an app with no usable UI selectors, drop **Block Input** on the canvas. Temporarily blocks the user's mouse and keyboard.

**Demonstration.**

```text
**Block Input**
- Block it: `True`
```

**Analogy.** One tool in that kit: moving your own hand and typing as if you sat at the PC.

**In combination.** Block Input in unattended runs, Move mouse / Send keys, then unblock by ending the action.

### Get keyboard identifier

- **Id:** `mouseandkeyboard/get-keyboard-identifier`
- **Kind:** native-action
- **Purpose:** Reads keyboard identifier into a flow variable.

**Use case.** In an app with no usable UI selectors, drop **Get keyboard identifier** on the canvas. Reads keyboard identifier into a flow variable.

**Demonstration.**

```text
**Get keyboard identifier**
- (no inputs)
Produces:
- `%KeyboardLayoutId%` (Numeric value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Block Input in unattended runs, Move mouse / Send keys, then unblock by ending the action.

### Get mouse position

- **Id:** `mouseandkeyboard/get-mouse-position`
- **Kind:** native-action
- **Purpose:** Reads mouse position into a flow variable.

**Use case.** In an app with no usable UI selectors, drop **Get mouse position** on the canvas. Reads mouse position into a flow variable.

**Demonstration.**

```text
**Get mouse position**
- Relative to: `Screen`
Produces:
- `%MousePosX%` (Numeric value)
- `%MousePosY%` (Numeric value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Block Input in unattended runs, Move mouse / Send keys, then unblock by ending the action.

### Move mouse

- **Id:** `mouseandkeyboard/move-mouse`
- **Kind:** native-action
- **Purpose:** Moves mouse.

**Use case.** In an app with no usable UI selectors, drop **Move mouse** on the canvas. Moves mouse.

**Demonstration.**

```text
**Move mouse**
- Position X: `1`
- Position Y: `1`
- Relative to: `Screen`
- Move mouse from previous position: `Instant`
```

**Analogy.** One tool in that kit: moving your own hand and typing as if you sat at the PC.

**In combination.** Block Input in unattended runs, Move mouse / Send keys, then unblock by ending the action.

### Move mouse to image

- **Id:** `mouseandkeyboard/move-mouse-to-image`
- **Kind:** native-action
- **Purpose:** Moves mouse to image.

**Use case.** In an app with no usable UI selectors, drop **Move mouse to image** on the canvas. Moves mouse to image.

**Demonstration.**

```text
**Move mouse to image**
- Image to move mouse to: `%Files%`
- Mouse movement style: `Instant`
- Occurrence: `1`
- Send a click after moving mouse: `False`
- Click type: `Left click`
- Wait for image to appear: `True`
- Fail timeout: `0`
- Seconds before click: `30`
- … 11 more parameter(s) in the action modal
Produces:
- `%X%` (Numeric value)
- `%Y%` (Numeric value)
```

**Analogy.** One tool in that kit: moving your own hand and typing as if you sat at the PC.

**In combination.** Block Input in unattended runs, Move mouse / Send keys, then unblock by ending the action.

### Move mouse to text on screen (OCR)

- **Id:** `mouseandkeyboard/move-mouse-to-text-on-screen-ocr`
- **Kind:** native-action
- **Purpose:** Moves mouse to text on screen (OCR).

**Use case.** In an app with no usable UI selectors, drop **Move mouse to text on screen (OCR)** on the canvas. Moves mouse to text on screen (OCR).

**Demonstration.**

```text
**Move mouse to text on screen (OCR)**
- OCR engine type: `%OCREngine%`
- OCR engine variable: `%OCREngine%`
- Text to find: `INV-1042`
- Is regular expression: `False`
- Occurrence: `1`
- Search for text on: `Entire screen`
- Search mode: `Whole of specified source`
- Image(s): `%Files%`
- … 26 more parameter(s) in the action modal
Produces:
- `%LocationOfTextFoundX%` (Numeric value)
- `%LocationOfTextFoundY%` (Numeric value)
- `%WidthOfTextFound%` (Numeric value)
- `%HeightOfTextFound%` (Numeric value)
```

**Analogy.** One tool in that kit: moving your own hand and typing as if you sat at the PC.

**In combination.** Block Input in unattended runs, Move mouse / Send keys, then unblock by ending the action.

### Press/release key

- **Id:** `mouseandkeyboard/press-release-key`
- **Kind:** native-action
- **Purpose:** Presses (and holds) or releases one or more modifier keys (Alt, Control, or Shift).

**Use case.** In an app with no usable UI selectors, drop **Press/release key** on the canvas. Presses (and holds) or releases one or more modifier keys (Alt, Control, or Shift).

**Demonstration.**

```text
**Press/release key**
- Action to perform: `Press`
- Control: `False`
- Alt: `False`
- Shift: `False`
- Win: `False`
```

**Analogy.** Pushing the exact button a trained operator would push.

**In combination.** Block Input in unattended runs, Move mouse / Send keys, then unblock by ending the action.

### Send keys

- **Id:** `mouseandkeyboard/send-keys`
- **Kind:** native-action
- **Purpose:** Sends keys.

**Use case.** In an app with no usable UI selectors, drop **Send keys** on the canvas. Sends keys.

**Demonstration.**

```text
**Send keys**
- Send keys to: `%Window%`
- Text to send: `INV-1042`
- Delay between keystrokes: `10`
- Send Text as hardware keys: `False`
```

**Analogy.** Handing a finished envelope to the mailroom.

**In combination.** Block Input in unattended runs, Move mouse / Send keys, then unblock by ending the action.

### Send mouse click

- **Id:** `mouseandkeyboard/send-mouse-click`
- **Kind:** native-action
- **Purpose:** Sends mouse click.

**Use case.** In an app with no usable UI selectors, drop **Send mouse click** on the canvas. Sends mouse click.

**Demonstration.**

```text
**Send mouse click**
- Mouse event to send: `Left click`
- Wait: `30`
- Move mouse: `False`
- X: `1`
- Y: `1`
- Relative to: `Screen`
- Mouse movement style: `Instant`
```

**Analogy.** Handing a finished envelope to the mailroom.

**In combination.** Block Input in unattended runs, Move mouse / Send keys, then unblock by ending the action.

### Set key state

- **Id:** `mouseandkeyboard/set-key-state`
- **Kind:** native-action
- **Purpose:** Writes key state.

**Use case.** In an app with no usable UI selectors, drop **Set key state** on the canvas. Writes key state.

**Demonstration.**

```text
**Set key state**
- Key: `Caps Lock`
- State: `On`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Block Input in unattended runs, Move mouse / Send keys, then unblock by ending the action.

### Wait for mouse

- **Id:** `mouseandkeyboard/wait-for-mouse`
- **Kind:** native-action
- **Purpose:** Pauses the flow until mouse.

**Use case.** In an app with no usable UI selectors, drop **Wait for mouse** on the canvas. Pauses the flow until mouse.

**Demonstration.**

```text
**Wait for mouse**
- Wait for mouse pointer to: `Become`
- Mouse pointer: `Arrow`
```

**Analogy.** Standing at the microwave until it beeps, so you do not grab a cold plate.

**In combination.** Block Input in unattended runs, Move mouse / Send keys, then unblock by ending the action.

### Wait for shortcut key

- **Id:** `mouseandkeyboard/wait-for-shortcut-key`
- **Kind:** native-action
- **Purpose:** Pauses the flow until shortcut key.

**Use case.** In an app with no usable UI selectors, drop **Wait for shortcut key** on the canvas. Pauses the flow until shortcut key.

**Demonstration.**

```text
**Wait for shortcut key**
- Shortcut keys: `Ctrl + A`
- Continue flow run on timeout: `False`
- Continue after: `10`
Produces:
- `%IndexOfShortcutKeyPressed%` (Numeric value)
```

**Analogy.** Standing at the microwave until it beeps, so you do not grab a cold plate.

**In combination.** Block Input in unattended runs, Move mouse / Send keys, then unblock by ending the action.
