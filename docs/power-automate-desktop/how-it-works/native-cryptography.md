# Cryptography — how each function works

Native Actions pane module **Cryptography**.

8 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Decrypt text with AES

- **Id:** `cryptography/decrypt-text-with-aes`
- **Kind:** native-action
- **Purpose:** Decrypts text with AES.

**Use case.** In protecting a file drop that leaves the building, drop **Decrypt text with AES** on the canvas. Decrypts text with AES.

**Demonstration.**

```text
**Decrypt text with AES**
- Encoding: `Unicode`
- Text to decrypt: `INV-1042`
- Decryption key: `INV-1042`
- Padding: `PKCS7`
- Key size: `256 bits`
- Use salt: `False`
- Salt: `INV-1042`
- Use initialization vector: `False`
- … 1 more parameter(s) in the action modal
Produces:
- `%DecryptedText%` (Text value)
```

**Analogy.** One tool in that kit: a sealed envelope versus a signed receipt.

**In combination.** Encrypt before you copy off-box; Decrypt only on the trusted machine.

### Decrypt to file with AES

- **Id:** `cryptography/decrypt-to-file-with-aes`
- **Kind:** native-action
- **Purpose:** Decrypts to file with AES.

**Use case.** In protecting a file drop that leaves the building, drop **Decrypt to file with AES** on the canvas. Decrypts to file with AES.

**Demonstration.**

```text
**Decrypt to file with AES**
- Encoding: `Unicode`
- Text to decrypt: `INV-1042`
- Decryption key: `INV-1042`
- Decrypt to file: `C:\RPA\Invoices\INV-1042.pdf`
- If file exists: `C:\RPA\Invoices\INV-1042.pdf`
- Padding: `PKCS7`
- Key size: `256 bits`
- Use salt: `False`
- … 3 more parameter(s) in the action modal
Produces:
- `%DecryptedFile%` (File)
```

**Analogy.** One tool in that kit: a sealed envelope versus a signed receipt.

**In combination.** Encrypt before you copy off-box; Decrypt only on the trusted machine.

### Encrypt from file with AES

- **Id:** `cryptography/encrypt-from-file-with-aes`
- **Kind:** native-action
- **Purpose:** Encrypts from file with AES.

**Use case.** In protecting a file drop that leaves the building, drop **Encrypt from file with AES** on the canvas. Encrypts from file with AES.

**Demonstration.**

```text
**Encrypt from file with AES**
- Encoding: `Unicode`
- File to encrypt: `C:\RPA\Invoices\INV-1042.pdf`
- Encryption key: `INV-1042`
- Padding: `PKCS7`
- Key size: `256 bits`
- Use salt: `False`
- Use initialization vector: `False`
Produces:
- `%EncryptedText%` (Text value)
- `%Salt%` (Text value)
- `%InitializationVector%` (Text value)
```

**Analogy.** One tool in that kit: a sealed envelope versus a signed receipt.

**In combination.** Encrypt before you copy off-box; Decrypt only on the trusted machine.

### Encrypt text with AES

- **Id:** `cryptography/encrypt-text-with-aes`
- **Kind:** native-action
- **Purpose:** Encrypts text with AES.

**Use case.** In protecting a file drop that leaves the building, drop **Encrypt text with AES** on the canvas. Encrypts text with AES.

**Demonstration.**

```text
**Encrypt text with AES**
- Encoding: `Unicode`
- Text to encrypt: `INV-1042`
- Encryption key: `INV-1042`
- Padding: `PKCS7`
- Key size: `256 bits`
- Use salt: `False`
- Use initialization vector: `False`
Produces:
- `%EncryptedText%` (Text value)
- `%Salt%` (Text value)
- `%InitializationVector%` (Text value)
```

**Analogy.** One tool in that kit: a sealed envelope versus a signed receipt.

**In combination.** Encrypt before you copy off-box; Decrypt only on the trusted machine.

### Hash from file

- **Id:** `cryptography/hash-from-file`
- **Kind:** native-action
- **Purpose:** Hashes from file.

**Use case.** In protecting a file drop that leaves the building, drop **Hash from file** on the canvas. Hashes from file.

**Demonstration.**

```text
**Hash from file**
- Hash algorithm: `SHA256`
- Encoding: `Unicode`
- File to hash: `C:\RPA\Invoices\INV-1042.pdf`
Produces:
- `%HashedText%` (Text value)
```

**Analogy.** One tool in that kit: a sealed envelope versus a signed receipt.

**In combination.** Encrypt before you copy off-box; Decrypt only on the trusted machine.

### Hash from file with key

- **Id:** `cryptography/hash-from-file-with-key`
- **Kind:** native-action
- **Purpose:** Hashes from file with key.

**Use case.** In protecting a file drop that leaves the building, drop **Hash from file with key** on the canvas. Hashes from file with key.

**Demonstration.**

```text
**Hash from file with key**
- Hash algorithm: `HMAC SHA256`
- Encoding: `Unicode`
- File to hash: `C:\RPA\Invoices\INV-1042.pdf`
- Hash key: `INV-1042`
Produces:
- `%HashedText%` (Text value)
```

**Analogy.** One tool in that kit: a sealed envelope versus a signed receipt.

**In combination.** Encrypt before you copy off-box; Decrypt only on the trusted machine.

### Hash text

- **Id:** `cryptography/hash-text`
- **Kind:** native-action
- **Purpose:** Hashes text.

**Use case.** In protecting a file drop that leaves the building, drop **Hash text** on the canvas. Hashes text.

**Demonstration.**

```text
**Hash text**
- Hash algorithm: `SHA256`
- Encoding: `Unicode`
- Text to hash: `INV-1042`
Produces:
- `%HashedText%` (Text value)
```

**Analogy.** One tool in that kit: a sealed envelope versus a signed receipt.

**In combination.** Encrypt before you copy off-box; Decrypt only on the trusted machine.

### Hash text with key

- **Id:** `cryptography/hash-text-with-key`
- **Kind:** native-action
- **Purpose:** Hashes text with key.

**Use case.** In protecting a file drop that leaves the building, drop **Hash text with key** on the canvas. Hashes text with key.

**Demonstration.**

```text
**Hash text with key**
- Hash algorithm: `HMAC SHA256`
- Encoding: `Unicode`
- Text to hash: `INV-1042`
- Hash key: `INV-1042`
Produces:
- `%HashedText%` (Text value)
```

**Analogy.** One tool in that kit: a sealed envelope versus a signed receipt.

**In combination.** Encrypt before you copy off-box; Decrypt only on the trusted machine.
