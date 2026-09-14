# Word

Launch Word, read and write documents, insert images, and replace text.

This page documents every **native action** in this group (8 items).

## Actions

### Attach to running Word

- **Inventory id:** `word/attach-to-running-word`
- **Kind:** native-action
- **Purpose:** Connects the flow to running Word that is already running.
- **Key inputs:** `Document name` (File)
- **Produces:** ``WordInstance`` (Word instance)
- **Exceptions:** `Failed to attach to Word document`; `Specified Word document not found`; `Failed to launch Word`
- **Microsoft Learn:** [Attach to running Word](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/word#attachtorunningword)

### Close Word

- **Inventory id:** `word/close-word`
- **Kind:** native-action
- **Purpose:** Closes word.
- **Key inputs:** `Word instance` (Word instance); `Before closing Word` (Do not save document, Save document, Save document as); `Document format` (All available formats from Word app); `Document path` (File)
- **Produces:** None listed
- **Exceptions:** `Failed to close Word`; `Failed to save Word`; `The operation cannot be performed on a read-only document`
- **Microsoft Learn:** [Close Word](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/word#closeword)

### Find and replace words in Word document

- **Inventory id:** `word/find-and-replace-words-in-word-document`
- **Kind:** native-action
- **Purpose:** Finds and replace words in Word document.
- **Key inputs:** `Word instance` (Word instance); `All matches` (Boolean value); `Text to find` (Text value); `Text to replace with` (Text value); `Use wildcards` (Boolean value); `Match case` (Boolean value); `Match whole words only` (Boolean value)
- **Produces:** None listed
- **Exceptions:** `Failed to replace text in Word document`; `The Word instance or the Word document is not initialized`; `The operation cannot be performed on a read-only document`
- **Microsoft Learn:** [Find and replace words in Word document](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/word#findandreplaceword)

### Insert image in Word document

- **Inventory id:** `word/insert-image-in-word-document`
- **Kind:** native-action
- **Purpose:** Inserts image in Word document.
- **Key inputs:** `Word instance` (Word instance); `Insert image to` (Beginning of Word file/End of Word file/Before of Bookmark/After of Bookmark/Before specific text /After specific text); `Insert image from` (File/Clipboard); `Image path` (File); `Text to find` (Text value); `Bookmark` (Text value)
- **Produces:** None listed
- **Exceptions:** `The Word instance or the Word document is not initialized`; `The operation cannot be performed on a read-only document`; `Failed to insert image`
- **Microsoft Learn:** [Insert image in Word document](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/word#insertimagetoword)

### Launch Word

- **Inventory id:** `word/launch-word`
- **Kind:** native-action
- **Purpose:** Starts Word and returns an instance later actions can reuse.
- **Key inputs:** `Launch Word` (With a blank document, and open the following document); `Document path` (File); `Make instance visible` (Boolean value); `Open as ReadOnly` (Boolean value); `Read protection password` (Direct encrypted input or Text value; optional); `Write protection password` (Direct encrypted input or Text value; optional)
- **Produces:** ``WordInstance`` (Word instance)
- **Exceptions:** `Failed to launch Word`; `The Word document was not found`; `Failed to open existing Word document`; `Failed to launch Word application`; `Word application is not installed`
- **Microsoft Learn:** [Launch Word](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/word#launchword)

### Read from Word document

- **Inventory id:** `word/read-from-word-document`
- **Kind:** native-action
- **Purpose:** Reads from Word document.
- **Key inputs:** `Word instance` (Word instance); `Retrieve` (Whole document/Pages/Bookmark); `Page` (Numeric value); `Bookmark` (Text value)
- **Produces:** `WordData` (Text value)
- **Exceptions:** `Failed to read the content from a Word document`; `The Word instance or the Word document is not initialized`
- **Microsoft Learn:** [Read from Word document](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/word#readfromword)

### Save Word

- **Inventory id:** `word/save-word`
- **Kind:** native-action
- **Purpose:** Saves word.
- **Key inputs:** `Word instance` (Word instance); `Save mode` (Save document, Save document as); `Document format` (All available formats from Word app); `Document path` (File)
- **Produces:** None listed
- **Exceptions:** `Failed to save Word`; `The Word instance or the Word document is not initialized`; `The operation cannot be performed on a read-only document`
- **Microsoft Learn:** [Save Word](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/word#saveword)

### Write to Word document

- **Inventory id:** `word/write-to-word-document`
- **Kind:** native-action
- **Purpose:** Writes to Word document.
- **Key inputs:** `Word instance` (Word instance); `Text to write` (General value; optional); `Append new line` (Boolean value); `Write text to` (Beginning of Word file/End of Word file/Before of Bookmark/After of Bookmark); `Bookmark` (Text value)
- **Produces:** None listed
- **Exceptions:** `The Word instance or the Word document is not initialized`; `The operation cannot be performed on a read-only document`; `The write operation on the Word document instance failed`
- **Microsoft Learn:** [Write to Word document](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/word#writetoword)
