# Word — how each function works

Native Actions pane module **Word**.

8 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Attach to running Word

- **Id:** `word/attach-to-running-word`
- **Kind:** native-action
- **Purpose:** Connects the flow to running Word that is already running.

**Use case.** In a letter or contract template on disk, drop **Attach to running Word** on the canvas. Connects the flow to running Word that is already running.

**Demonstration.**

```text
**Attach to running Word**
- Document name: `(set in designer)`
Produces:
- `%`WordInstance`%` (Word instance)
```

**Analogy.** One tool in that kit: rolling a sheet into a typewriter, typing, pulling it out.

**In combination.** Launch Word, Write or Find and replace, Save Word, Close Word.

### Close Word

- **Id:** `word/close-word`
- **Kind:** native-action
- **Purpose:** Closes word.

**Use case.** In a letter or contract template on disk, drop **Close Word** on the canvas. Closes word.

**Demonstration.**

```text
**Close Word**
- Word instance: `%WordInstance%`
- Before closing Word: `Don't save document`
- Document format: `Default (From Extension)`
- Document path: `C:\RPA\Invoices\INV-1042.pdf`
```

**Analogy.** Turning out the lights when the work in that room is done.

**In combination.** Launch Word, Write or Find and replace, Save Word, Close Word. Call this only after the last use of the instance so you do not break later steps.

### Find and replace words in Word document

- **Id:** `word/find-and-replace-words-in-word-document`
- **Kind:** native-action
- **Purpose:** Finds and replace words in Word document.

**Use case.** In a letter or contract template on disk, drop **Find and replace words in Word document** on the canvas. Finds and replace words in Word document.

**Demonstration.**

```text
**Find and replace words in Word document**
- Word instance: `%WordInstance%`
- All matches: `False`
- Text to find: `The text to find in the worksheet`
- Text to replace with: `INV-1042`
- Use wildcards: `False`
- Match case: `False`
- Match whole words only: `False`
```

**Analogy.** One tool in that kit: rolling a sheet into a typewriter, typing, pulling it out.

**In combination.** Launch Word, Write or Find and replace, Save Word, Close Word.

### Insert image in Word document

- **Id:** `word/insert-image-in-word-document`
- **Kind:** native-action
- **Purpose:** Inserts image in Word document.

**Use case.** In a letter or contract template on disk, drop **Insert image in Word document** on the canvas. Inserts image in Word document.

**Demonstration.**

```text
**Insert image in Word document**
- Word instance: `%WordInstance%`
- Insert image to: `Beginning of Word file`
- Insert image from: `File`
- Image path: `C:\RPA\Invoices\INV-1042.pdf`
- Text to find: `The text to find in the Word document for inserting image`
- Bookmark: `The target bookmark in the Word document where the image will be appended`
```

**Analogy.** One tool in that kit: rolling a sheet into a typewriter, typing, pulling it out.

**In combination.** Launch Word, Write or Find and replace, Save Word, Close Word.

### Launch Word

- **Id:** `word/launch-word`
- **Kind:** native-action
- **Purpose:** Starts Word and returns an instance later actions can reuse.

**Use case.** In a letter or contract template on disk, drop **Launch Word** on the canvas. Starts Word and returns an instance later actions can reuse.

**Demonstration.**

```text
**Launch Word**
- Launch Word: `With a blank document`
- Document path: `C:\RPA\Invoices\INV-1042.pdf`
- Make instance visible: `True`
- Open as ReadOnly: `False`
- Read protection password: `%Credential.Password%  (sensitive)`
- Write protection password: `%Credential.Password%  (sensitive)`
Produces:
- `%`WordInstance`%` (Word instance)
```

**Analogy.** Unlocking the room before you work. Same family as: rolling a sheet into a typewriter, typing, pulling it out.

**In combination.** Launch Word, Write or Find and replace, Save Word, Close Word. Keep the produced instance/connection and pass it into every later action in this module.

### Read from Word document

- **Id:** `word/read-from-word-document`
- **Kind:** native-action
- **Purpose:** Reads from Word document.

**Use case.** In a letter or contract template on disk, drop **Read from Word document** on the canvas. Reads from Word document.

**Demonstration.**

```text
**Read from Word document**
- Word instance: `%WordInstance%`
- Retrieve: `Whole document`
- Page: `1`
- Bookmark: `INV-1042`
Produces:
- `%WordData%` (Text value)
```

**Analogy.** Copying a value off a page into your notebook.

**In combination.** Launch Word, Write or Find and replace, Save Word, Close Word.

### Save Word

- **Id:** `word/save-word`
- **Kind:** native-action
- **Purpose:** Saves word.

**Use case.** In a letter or contract template on disk, drop **Save Word** on the canvas. Saves word.

**Demonstration.**

```text
**Save Word**
- Word instance: `%WordInstance%`
- Save mode: `Save document`
- Document format: `Default (From Extension)`
- Document path: `C:\RPA\Invoices\INV-1042.pdf`
```

**Analogy.** One tool in that kit: rolling a sheet into a typewriter, typing, pulling it out.

**In combination.** Launch Word, Write or Find and replace, Save Word, Close Word.

### Write to Word document

- **Id:** `word/write-to-word-document`
- **Kind:** native-action
- **Purpose:** Writes to Word document.

**Use case.** In a letter or contract template on disk, drop **Write to Word document** on the canvas. Writes to Word document.

**Demonstration.**

```text
**Write to Word document**
- Word instance: `%WordInstance%`
- Text to write: `The text to write in the specified Word document`
- Append new line: `True`
- Write text to: `Beginning of Word file`
- Bookmark: `The target bookmark in the Word document where the text will be appended`
```

**Analogy.** Writing a value onto a page so the next person (or action) can see it.

**In combination.** Launch Word, Write or Find and replace, Save Word, Close Word.
