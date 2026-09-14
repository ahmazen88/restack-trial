# Mouse and keyboard

Move the pointer, click, type keys, and wait on mouse or shortcut events.

This page documents every **native action** in this group (12 items).

## Actions

### Block Input

- **Inventory id:** `mouseandkeyboard/block-input`
- **Kind:** native-action
- **Purpose:** Temporarily blocks the user's mouse and keyboard.
- **Key inputs:** `Block it` (Boolean value)
- **Produces:** None listed
- **Exceptions:** `Can't block/unblock user input in non interactive mode`; `Failed to block/unblock input`
- **Microsoft Learn:** [Block Input](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#blockinput)

### Get keyboard identifier

- **Inventory id:** `mouseandkeyboard/get-keyboard-identifier`
- **Kind:** native-action
- **Purpose:** Reads keyboard identifier into a flow variable.
- **Key inputs:** None
- **Produces:** `KeyboardLayoutId` (Numeric value)
- **Exceptions:** `Keyboard identifier wasn’t found`
- **Microsoft Learn:** [Get keyboard identifier](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#getkeyboardlayout)

### Get mouse position

- **Inventory id:** `mouseandkeyboard/get-mouse-position`
- **Kind:** native-action
- **Purpose:** Reads mouse position into a flow variable.
- **Key inputs:** `Relative to` (Screen, Foreground window)
- **Produces:** `MousePosX` (Numeric value); `MousePosY` (Numeric value)
- **Exceptions:** `Can't retrieve the mouse position in non interactive mode`
- **Microsoft Learn:** [Get mouse position](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#getmouseposition)

### Move mouse

- **Inventory id:** `mouseandkeyboard/move-mouse`
- **Kind:** native-action
- **Purpose:** Moves mouse.
- **Key inputs:** `Position X` (Numeric value); `Position Y` (Numeric value); `Relative to` (Screen, Active window, Current mouse position); `Move mouse from previous position` (Instant, With animation (low speed), With animation (normal speed), With animation (high speed))
- **Produces:** None listed
- **Exceptions:** `Can't move mouse in non interactive mode`; `Failed to move mouse`
- **Microsoft Learn:** [Move mouse](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#movemouse)

### Move mouse to image

- **Inventory id:** `mouseandkeyboard/move-mouse-to-image`
- **Kind:** native-action
- **Purpose:** Moves mouse to image.
- **Key inputs:** `Image to move mouse to` (List of Images); `Mouse movement style` (Instant, With animation (low speed), With animation (normal speed), With animation (high speed)); `Occurrence` (Numeric value; optional); `Send a click after moving mouse` (Boolean value); `Click type` (Left click, Right click, Double click, Middle click, Left button down, Left button up, Right button down, Right button up); `Wait for image to appear` (Boolean value); `Fail timeout` (Numeric value; optional); `Seconds before click` (Numeric value; optional); `Image matching algorithm` (Basic, Advanced); `Mouse position relative to image` (top left corner, top center, top right corner, middle left part, center, middle right part, bottom left corner, bottom center, bottom right corner); `Offset X` (Text value); `Offset Y` (Text value); `Tolerance` (Numeric value; optional); `Search for image on` (Entire screen, Foreground window only); `Search mode` (Search whole screen or foreground window, Search on specified subregion of screen or foreground window); `X1` (Numeric value; optional); `Y1` (Numeric value; optional); `X2` (Numeric value; optional); `Y2` (Numeric value; optional)
- **Produces:** `X` (Numeric value); `Y` (Numeric value)
- **Exceptions:** `Image not found on screen`; `Can't move mouse in non interactive mode`; `Failed to move mouse`; `Invalid subregion coordinates`; `Not enough Image occurrences found on screen`
- **Microsoft Learn:** [Move mouse to image](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#movemousetoimagebase)

### Move mouse to text on screen (OCR)

- **Inventory id:** `mouseandkeyboard/move-mouse-to-text-on-screen-ocr`
- **Kind:** native-action
- **Purpose:** Moves mouse to text on screen (OCR).
- **Key inputs:** `OCR engine type` (OCR engine variable, Tesseract engine); `OCR engine variable` (OCREngineObject); `Text to find` (Text value); `Is regular expression` (Boolean value); `Occurrence` (Numeric value; optional); `Search for text on` (Entire screen, Foreground window only); `Search mode` (Whole of specified source, Specific subregion only, Subregion relative to image); `Image(s)` (List of Images); `X1` (Numeric value; optional); `Tolerance` (Numeric value; optional); `Y1` (Numeric value; optional); `X1` (Numeric value; optional); `X2` (Numeric value; optional); `Y1` (Numeric value; optional); `Y2` (Numeric value; optional); `X2` (Numeric value; optional); `Y2` (Numeric value; optional); `Move mouse from previous position` (Instant, With animation (low speed), With animation (normal speed), With animation (high speed)); `Windows OCR language` (Chinese (Simplified), Chinese (Traditional), Czech, Danish, Dutch, English, Finnish, French, German, Greek, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Romanian, Russian, Serbian (Cyrillic), Serbian (Latin), Slovak, Spanish, Swedish, Turkish); `Use other language` (Boolean value); `Tesseract language` (English, German, Spanish, French, Italian); `Language abbreviation` (Text value); `Language data path` (Text value); `Image width multiplier` (Numeric value); `Image height multiplier` (Numeric value); `Wait for text to appear` (Boolean value); `Fail if text doesn't appear within` (Numeric value; optional); `Send a click after moving mouse` (Boolean value); `Click type` (Left click, Right click, Double click, Middle click, Left button down, Left button up, Right button down, Right button up); `Wait before clicking for` (Numeric value; optional); `Mouse position relative to text` (Top left, Top center, Top right, Middle left, Middle center, Middle right, Bottom left, Bottom center, Bottom right); `Offset X` (Text value); `Offset Y` (Text value); `Image matching algorithm` (Basic, Advanced)
- **Produces:** `LocationOfTextFoundX` (Numeric value); `LocationOfTextFoundY` (Numeric value); `WidthOfTextFound` (Numeric value); `HeightOfTextFound` (Numeric value)
- **Exceptions:** `Text not found on screen`; `Can't move mouse in non interactive mode`; `Failed to move mouse`; `Invalid subregion coordinates`; `Failed to create the OCR engine`; `Data path folder doesn't exist`; `The selected Windows language pack isn't installed on the machine`; `OCR engine isn't alive`
- **Microsoft Learn:** [Move mouse to text on screen (OCR)](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#movemousetotextonscreenwithocraction)

### Press/release key

- **Inventory id:** `mouseandkeyboard/press-release-key`
- **Kind:** native-action
- **Purpose:** Presses (and holds) or releases one or more modifier keys (Alt, Control, or Shift).
- **Key inputs:** `Action to perform` (Press, Release); `Control` (Boolean value); `Alt` (Boolean value); `Shift` (Boolean value); `Win` (Boolean value)
- **Produces:** None listed
- **Exceptions:** `Can't press or release key in non interactive mode`
- **Microsoft Learn:** [Press/release key](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#pressreleasekey)

### Send keys

- **Inventory id:** `mouseandkeyboard/send-keys`
- **Kind:** native-action
- **Purpose:** Sends keys.
- **Key inputs:** `Send keys to` (Foreground window, By UI element, By window instance/handle, By title and/or class); `Text to send` (Direct encrypted input or Text value); `Delay between keystrokes` (Numeric value; optional); `Send Text as hardware keys` (Boolean value)
- **Produces:** None listed
- **Exceptions:** `Can't send keystrokes in non interactive mode`; `Text to send doesn't represent valid keystrokes`; `There isn't an active application to send keystrokes to`; `Failed to send keystrokes`
- **Microsoft Learn:** [Send keys](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#sendkeys)

### Send mouse click

- **Inventory id:** `mouseandkeyboard/send-mouse-click`
- **Kind:** native-action
- **Purpose:** Sends mouse click.
- **Key inputs:** `Mouse event to send` (Left click, Right click, Double click, Middle click, Left button down, Left button up, Right button down, Right button up); `Wait` (Numeric value; optional); `Move mouse` (Boolean value); `X` (Numeric value); `Y` (Numeric value); `Relative to` (Screen, Active window, Current mouse position); `Mouse movement style` (Instant, With animation (low speed), With animation (normal speed), With animation (high speed))
- **Produces:** None listed
- **Exceptions:** `Can't send mouse click in non interactive mode`; `Mouse click out of screen bounds`; `Failed to send mouse click`
- **Microsoft Learn:** [Send mouse click](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#sendmouseclick)

### Set key state

- **Inventory id:** `mouseandkeyboard/set-key-state`
- **Kind:** native-action
- **Purpose:** Writes key state.
- **Key inputs:** `Key` (Caps Lock, Num Lock, Scroll Lock); `State` (Off, On)
- **Produces:** None listed
- **Exceptions:** `Can't set key state in non interactive mode`
- **Microsoft Learn:** [Set key state](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#setkeystate)

### Wait for mouse

- **Inventory id:** `mouseandkeyboard/wait-for-mouse`
- **Kind:** native-action
- **Purpose:** Pauses the flow until mouse.
- **Key inputs:** `Wait for mouse pointer to` (Become, Become not); `Mouse pointer` (Arrow, App starting, Cross, Hand, Help, IBeam, Wait cursor)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Wait for mouse](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#waitformouseaction)

### Wait for shortcut key

- **Inventory id:** `mouseandkeyboard/wait-for-shortcut-key`
- **Kind:** native-action
- **Purpose:** Pauses the flow until shortcut key.
- **Key inputs:** `Shortcut keys` (Keys combination); `Continue flow run on timeout` (Boolean value); `Continue after` (Numeric value; optional)
- **Produces:** `IndexOfShortcutKeyPressed` (Numeric value)
- **Exceptions:** `Shortcut key failed to register`
- **Microsoft Learn:** [Wait for shortcut key](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#waitforshortcutkeyaction)
