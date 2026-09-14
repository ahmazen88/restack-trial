# Word

Launch Word and read, write, or replace document content.

- Actions in this module: **8**
- Official docs: [Word actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/word)

## Actions

### Launch Word

Opens a new Word instance or opens a Word document.

Designer name: **Launch Word**. Official reference: [Word / Launch Word](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/word#launchword).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Launch Word | Choice | With a blank document, and open the following document | With a blank document |
| Document path | Required | File | — |
| Make instance visible | Choice | Boolean value | True |
| Open as ReadOnly | Choice | Boolean value | False |
| Read protection password | Optional | Direct encrypted input or Text value | — |
| Write protection password | Optional | Direct encrypted input or Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| WordInstance | Word instance |

**On error:** `Failed to launch Word`, `The Word document was not found`, `Failed to open existing Word document`, `Failed to launch Word application`, `Word application is not installed`.

---

### Attach to running Word

Attaches to a Word document that's already open.

Designer name: **Attach to running Word**. Official reference: [Word / Attach to running Word](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/word#attachtorunningword).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Document name | Required | File | — |

**Outputs**

| Variable | Type |
|---|---|
| WordInstance | Word instance |

**On error:** `Failed to attach to Word document`, `Specified Word document not found`, `Failed to launch Word`.

---

### Save Word

Saves a previously launched Word instance.

Designer name: **Save Word**. Official reference: [Word / Save Word](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/word#saveword).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Word instance | Required | Word instance | — |
| Save mode | Choice | Save document, Save document as | Save document |
| Document format | Choice | All available formats from Word app | Default (From Extension) |
| Document path | Required | File | — |

Produces no variables.

**On error:** `Failed to save Word`, `The Word instance or the Word document is not initialized`, `The operation cannot be performed on a read-only document`.

---

### Close Word

Closes a Word instance.

Designer name: **Close Word**. Official reference: [Word / Close Word](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/word#closeword).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Word instance | Required | Word instance | — |
| Before closing Word | Choice | Do not save document, Save document, Save document as | Don't save document |
| Document format | Choice | All available formats from Word app | Default (From Extension) |
| Document path | Required | File | — |

Produces no variables.

**On error:** `Failed to close Word`, `Failed to save Word`, `The operation cannot be performed on a read-only document`.

---

### Read from Word document

Reads the text content from a document of a Word instance.

Designer name: **Read from Word document**. Official reference: [Word / Read from Word document](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/word#readfromword).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Word instance | Required | Word instance | The Word instance to work with |
| Retrieve | Choice | Whole document/Pages/Bookmark | Whole document |
| Page | Required | Numeric value | 1 |
| Bookmark | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| WordData | Text value |

**On error:** `Failed to read the content from a Word document`, `The Word instance or the Word document is not initialized`.

---

### Write to Word document

Write or append text to a Word file.

Designer name: **Write to Word document**. Official reference: [Word / Write to Word document](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/word#writetoword).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Word instance | Required | Word instance | The Word instance to work with |
| Text to write | Optional | General value | The text to write in the specified Word document |
| Append new line | Choice | Boolean value | True |
| Write text to | Choice | Beginning of Word file/End of Word file/Before of Bookmark/After of Bookmark | Beginning of Word file |
| Bookmark | Required | Text value | The target bookmark in the Word document where the text will be appended |

Produces no variables.

**On error:** `The Word instance or the Word document is not initialized`, `The operation cannot be performed on a read-only document`, `The write operation on the Word document instance failed`.

---

### Insert image in Word document

Insert an image to a Word file.

Designer name: **Insert image in Word document**. Official reference: [Word / Insert image in Word document](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/word#insertimagetoword).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Word instance | Required | Word instance | The Word instance to work with |
| Insert image to | Choice | Beginning of Word file/End of Word file/Before of Bookmark/After of Bookmark/Before specific text /After specific text | Beginning of Word file |
| Insert image from | Choice | File/Clipboard | File |
| Image path | Required | File | — |
| Text to find | Required | Text value | The text to find in the Word document for inserting image |
| Bookmark | Required | Text value | The target bookmark in the Word document where the image will be appended |

Produces no variables.

**On error:** `The Word instance or the Word document is not initialized`, `The operation cannot be performed on a read-only document`, `Failed to insert image`.

---

### Find and replace words in Word document

Finds text and replaces it with another in the active worksheet of an Excel instance.

Designer name: **Find and replace words in Word document**. Official reference: [Word / Find and replace words in Word document](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/word#findandreplaceword).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Word instance | Required | Word instance | The Word instance to work with |
| All matches | Choice | Boolean value | False |
| Text to find | Required | Text value | The text to find in the worksheet |
| Text to replace with | Required | Text value | — |
| Use wildcards | Choice | Boolean value | False |
| Match case | Choice | Boolean value | False |
| Match whole words only | Choice | Boolean value | False |

Produces no variables.

**On error:** `Failed to replace text in Word document`, `The Word instance or the Word document is not initialized`, `The operation cannot be performed on a read-only document`.

---
