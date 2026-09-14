# Mouse and keyboard

Move the mouse, send clicks and keystrokes, and wait for input.

- Actions in this module: **12**
- Official docs: [Mouse and keyboard actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard)

## Actions

### Block Input

Blocks user mouse and keyboard input, so that the flow can perform mouse and keyboard actions without interference from the user.

Designer name: **Block Input**. Official reference: [Mouse and keyboard / Block Input](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#blockinput).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Block it | Choice | Boolean value | True |

Produces no variables.

**On error:** `Can't block/unblock user input in non interactive mode`, `Failed to block/unblock input`.

---

### Get mouse position

Returns the current position of the mouse cursor on the screen in pixel coordinates.

Designer name: **Get mouse position**. Official reference: [Mouse and keyboard / Get mouse position](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#getmouseposition).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Relative to | Choice | Screen, Foreground window | Screen |

**Outputs**

| Variable | Type |
|---|---|
| MousePosX | Numeric value |
| MousePosY | Numeric value |

**On error:** `Can't retrieve the mouse position in non interactive mode`.

---

### Move mouse

Moves the mouse to a specific position.

Designer name: **Move mouse**. Official reference: [Mouse and keyboard / Move mouse](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#movemouse).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Position X | Required | Numeric value | — |
| Position Y | Required | Numeric value | — |
| Relative to | Choice | Screen, Active window, Current mouse position | Screen |
| Move mouse from previous position | Choice | Instant, With animation (low speed), With animation (normal speed), With animation (high speed) | Instant |

Produces no variables.

**On error:** `Can't move mouse in non interactive mode`, `Failed to move mouse`.

---

### Move mouse to image

Moves the mouse over an image found on screen or on the foreground window.

Designer name: **Move mouse to image**. Official reference: [Mouse and keyboard / Move mouse to image](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#movemousetoimagebase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Image to move mouse to | Required | List of Images | — |
| Mouse movement style | Choice | Instant, With animation (low speed), With animation (normal speed), With animation (high speed) | Instant |
| Occurrence | Optional | Numeric value | 1 |
| Send a click after moving mouse | Choice | Boolean value | False |
| Click type | Choice | Left click, Right click, Double click, Middle click, Left button down, Left button up, Right button down, Right button up | Left click |
| Wait for image to appear | Choice | Boolean value | True |
| Fail timeout | Optional | Numeric value | 0 |
| Seconds before click | Optional | Numeric value | 0 |
| Image matching algorithm | Choice | Basic, Advanced | Basic |
| Mouse position relative to image | Choice | top left corner, top center, top right corner, middle left part, center, middle right part, bottom left corner, bottom center, bottom right corner | center |
| Offset X | Required | Text value | 0 |
| Offset Y | Required | Text value | 0 |
| Tolerance | Optional | Numeric value | 10 |
| Search for image on | Choice | Entire screen, Foreground window only | Entire screen |
| Search mode | Choice | Search whole screen or foreground window, Search on specified subregion of screen or foreground window | Search whole screen or foreground window |
| X1 | Optional | Numeric value | — |
| Y1 | Optional | Numeric value | — |
| X2 | Optional | Numeric value | — |
| Y2 | Optional | Numeric value | — |

**Outputs**

| Variable | Type |
|---|---|
| X | Numeric value |
| Y | Numeric value |

**On error:** `Image not found on screen`, `Can't move mouse in non interactive mode`, `Failed to move mouse`, `Invalid subregion coordinates`, `Not enough Image occurrences found on screen`.

---

### Move mouse to text on screen (OCR)

Moves the mouse over a text found on the screen or on the foreground window using OCR.

Designer name: **Move mouse to text on screen (OCR)**. Official reference: [Mouse and keyboard / Move mouse to text on screen (OCR)](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#movemousetotextonscreenwithocraction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| OCR engine type | Required | OCR engine variable, Tesseract engine | OCR engine variable |
| OCR engine variable | Required | OCREngineObject | — |
| Text to find | Required | Text value | — |
| Is regular expression | Choice | Boolean value | False |
| Occurrence | Optional | Numeric value | 1 |
| Search for text on | Choice | Entire screen, Foreground window only | Entire screen |
| Search mode | Choice | Whole of specified source, Specific subregion only, Subregion relative to image | Whole of specified source |
| Image(s) | Required | List of Images | — |
| X1 | Optional | Numeric value | — |
| Tolerance | Optional | Numeric value | 10 |
| Y1 | Optional | Numeric value | — |
| X1 | Optional | Numeric value | — |
| X2 | Optional | Numeric value | — |
| Y1 | Optional | Numeric value | — |
| Y2 | Optional | Numeric value | — |
| X2 | Optional | Numeric value | — |
| Y2 | Optional | Numeric value | — |
| Move mouse from previous position | Choice | Instant, With animation (low speed), With animation (normal speed), With animation (high speed) | Instant |
| Windows OCR language | Choice | Chinese (Simplified), Chinese (Traditional), Czech, Danish, Dutch, English, Finnish, French, German, Greek, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Romanian, Russian, Serbian (Cyrillic), Serbian (Latin), Slovak, Spanish, Swedish, Turkish | English |
| Use other language | Choice | Boolean value | False |
| Tesseract language | Choice | English, German, Spanish, French, Italian | English |
| Language abbreviation | Required | Text value | — |
| Language data path | Required | Text value | — |
| Image width multiplier | Required | Numeric value | 1 |
| Image height multiplier | Required | Numeric value | 1 |
| Wait for text to appear | Choice | Boolean value | False |
| Fail if text doesn't appear within | Optional | Numeric value | 10 |
| Send a click after moving mouse | Choice | Boolean value | False |
| Click type | Choice | Left click, Right click, Double click, Middle click, Left button down, Left button up, Right button down, Right button up | Left click |
| Wait before clicking for | Optional | Numeric value | 1 |
| Mouse position relative to text | Choice | Top left, Top center, Top right, Middle left, Middle center, Middle right, Bottom left, Bottom center, Bottom right | Middle center |
| Offset X | Required | Text value | 0 |
| Offset Y | Required | Text value | 0 |
| Image matching algorithm | Choice | Basic, Advanced | Basic |

**Outputs**

| Variable | Type |
|---|---|
| LocationOfTextFoundX | Numeric value |
| LocationOfTextFoundY | Numeric value |
| WidthOfTextFound | Numeric value |
| HeightOfTextFound | Numeric value |

**On error:** `Text not found on screen`, `Can't move mouse in non interactive mode`, `Failed to move mouse`, `Invalid subregion coordinates`, `Failed to create the OCR engine`, `Data path folder doesn't exist`, `The selected Windows language pack isn't installed on the machine`, `OCR engine isn't alive`.

---

### Send mouse click

Sends a mouse click event.

Designer name: **Send mouse click**. Official reference: [Mouse and keyboard / Send mouse click](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#sendmouseclick).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Mouse event to send | Choice | Left click, Right click, Double click, Middle click, Left button down, Left button up, Right button down, Right button up | Left click |
| Wait | Optional | Numeric value | 0 |
| Move mouse | Choice | Boolean value | False |
| X | Required | Numeric value | — |
| Y | Required | Numeric value | — |
| Relative to | Choice | Screen, Active window, Current mouse position | Screen |
| Mouse movement style | Choice | Instant, With animation (low speed), With animation (normal speed), With animation (high speed) | Instant |

Produces no variables.

**On error:** `Can't send mouse click in non interactive mode`, `Mouse click out of screen bounds`, `Failed to send mouse click`.

---

### Send keys

Sends keys to the application that is currently active.

Designer name: **Send keys**. Official reference: [Mouse and keyboard / Send keys](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#sendkeys).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Send keys to | Choice | Foreground window, By UI element, By window instance/handle, By title and/or class | Foreground window |
| Text to send | Required | Direct encrypted input or Text value | — |
| Delay between keystrokes | Optional | Numeric value | 10 |
| Send Text as hardware keys | Choice | Boolean value | False |

Produces no variables.

**On error:** `Can't send keystrokes in non interactive mode`, `Text to send doesn't represent valid keystrokes`, `There isn't an active application to send keystrokes to`, `Failed to send keystrokes`, `Category`, `Buttons`, `Keyboard Control`, `Buttons`, `IME keys`, `Browser keys`, `Volume keys`, `Media keys`, `Buttons`, `OEM keys`, `Buttons`, `Buttons`, `D keys`, `Letters`, `Windows keys`, `NumPad keys`, `Calculation keys`, `Function keys`, `Buttons`.

---

### Press/release key

Presses (and holds) or releases one or more modifier keys (Alt, Control, or Shift).

Designer name: **Press/release key**. Official reference: [Mouse and keyboard / Press/release key](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#pressreleasekey).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Action to perform | Choice | Press, Release | Press |
| Control | Choice | Boolean value | False |
| Alt | Choice | Boolean value | False |
| Shift | Choice | Boolean value | False |
| Win | Choice | Boolean value | False |

Produces no variables.

**On error:** `Can't press or release key in non interactive mode`.

---

### Set key state

Writes the state (on or off) for the keys Caps Lock, Num Lock or Scroll Lock.

Designer name: **Set key state**. Official reference: [Mouse and keyboard / Set key state](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#setkeystate).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Key | Choice | Caps Lock, Num Lock, Scroll Lock | Caps Lock |
| State | Choice | Off, On | On |

Produces no variables.

**On error:** `Can't set key state in non interactive mode`.

---

### Wait for mouse

Suspends the execution of the flow until the mouse pointer changes, usually to or from the 'wait cursor' or hourglass.

Designer name: **Wait for mouse**. Official reference: [Mouse and keyboard / Wait for mouse](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#waitformouseaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Wait for mouse pointer to | Choice | Become, Become not | Become |
| Mouse pointer | Choice | Arrow, App starting, Cross, Hand, Help, IBeam, Wait cursor | Arrow |

Produces no variables.

No module-specific exceptions are listed for this action.

---

### Get keyboard identifier

Returns the active keyboard identifier from the machine's registry.

Designer name: **Get keyboard identifier**. Official reference: [Mouse and keyboard / Get keyboard identifier](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#getkeyboardlayout).

This action has no input parameters.

**Outputs**

| Variable | Type |
|---|---|
| KeyboardLayoutId | Numeric value |

**On error:** `Keyboard identifier wasn’t found`.

---

### Wait for shortcut key

Pause the flow run until a specific shortcut key is pressed.

Designer name: **Wait for shortcut key**. Official reference: [Mouse and keyboard / Wait for shortcut key](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#waitforshortcutkeyaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Shortcut keys | Choice | Keys combination | Ctrl + A |
| Continue flow run on timeout | Choice | Boolean value | False |
| Continue after | Optional | Numeric value | 10 |

**Outputs**

| Variable | Type |
|---|---|
| IndexOfShortcutKeyPressed | Numeric value |

**On error:** `Shortcut key failed to register`.

---
