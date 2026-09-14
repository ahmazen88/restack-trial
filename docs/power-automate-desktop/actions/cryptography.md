# Cryptography

Hash, encrypt, decrypt, and encode values.

- Actions in this module: **8**
- Official docs: [Cryptography actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cryptography)

## Actions

### Encrypt text with AES

Encrypt a string with AES, using a key and a specified encoding format.

Designer name: **Encrypt text with AES**. Official reference: [Cryptography / Encrypt text with AES](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cryptography#encrypttextaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Encoding | Choice | System default, ASCII, Unicode, Big-endian Unicode, UTF-8 | Unicode |
| Text to encrypt | Required | Text value | — |
| Encryption key | Required | Direct encrypted input or Text value | — |
| Padding | Choice | None, PKCS7, Zeros, ANSIX923, ISO10126 | PKCS7 |
| Key size | Choice | 128 bits, 192 bits, 256 bits | 256 bits |
| Use salt | Choice | Boolean value | False |
| Use initialization vector | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| EncryptedText | Text value |
| Salt | Text value |
| InitializationVector | Text value |

**On error:** `Failed to encrypt text`.

---

### Decrypt text with AES

Decrypt a string with AES based on a specified key and an encoding format.

Designer name: **Decrypt text with AES**. Official reference: [Cryptography / Decrypt text with AES](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cryptography#decrypttextaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Encoding | Choice | System default, ASCII, Unicode, Big-endian Unicode, UTF-8 | Unicode |
| Text to decrypt | Required | Text value | — |
| Decryption key | Required | Direct encrypted input or Text value | — |
| Padding | Choice | None, PKCS7, Zeros, ANSIX923, ISO10126 | PKCS7 |
| Key size | Choice | 128 bits, 192 bits, 256 bits | 256 bits |
| Use salt | Choice | Boolean value | False |
| Salt | Required | Text value | — |
| Use initialization vector | Choice | Boolean value | False |
| Initialization vector | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| DecryptedText | Text value |

**On error:** `Failed to decrypt text`.

---

### Encrypt from file with AES

Encrypt the contents of a file with AES, using a key and a specified encoding format.

Designer name: **Encrypt from file with AES**. Official reference: [Cryptography / Encrypt from file with AES](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cryptography#encryptfromfileaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Encoding | Choice | System default, ASCII, Unicode, Big-endian Unicode, UTF-8 | Unicode |
| File to encrypt | Required | File | — |
| Encryption key | Required | Direct encrypted input or Text value | — |
| Padding | Choice | None, PKCS7, Zeros, ANSIX923, ISO10126 | PKCS7 |
| Key size | Choice | 128 bits, 192 bits, 256 bits | 256 bits |
| Use salt | Choice | Boolean value | False |
| Use initialization vector | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| EncryptedText | Text value |
| Salt | Text value |
| InitializationVector | Text value |

**On error:** `File not found`, `Failed to encrypt the contents of the file`.

---

### Decrypt to file with AES

Decrypt a string to a file with AES based on a specified key and an encoding format.

Designer name: **Decrypt to file with AES**. Official reference: [Cryptography / Decrypt to file with AES](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cryptography#decrypttofileaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Encoding | Choice | System default, ASCII, Unicode, Big-endian Unicode, UTF-8 | Unicode |
| Text to decrypt | Required | Text value | — |
| Decryption key | Required | Direct encrypted input or Text value | — |
| Decrypt to file | Required | File | — |
| If file exists | Choice | Overwrite, Don't decrypt to file, Add sequential suffix | Add sequential suffix |
| Padding | Choice | None, PKCS7, Zeros, ANSIX923, ISO10126 | PKCS7 |
| Key size | Choice | 128 bits, 192 bits, 256 bits | 256 bits |
| Use salt | Choice | Boolean value | False |
| Salt | Required | Text value | — |
| Use initialization vector | Choice | Boolean value | False |
| Initialization vector | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| DecryptedFile | File |

**On error:** `Failed to decrypt and store the contents to a file`.

---

### Hash text

Hash a string, using a specified algorithm and an encoding format.

Designer name: **Hash text**. Official reference: [Cryptography / Hash text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cryptography#hashtext).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Hash algorithm | Choice | SHA256, SHA384, SHA512 | SHA256 |
| Encoding | Choice | System default, ASCII, Unicode, Big-endian Unicode, UTF-8 | Unicode |
| Text to hash | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| HashedText | Text value |

**On error:** `Failed to hash text`.

---

### Hash from file

Hash the contents of a file, using a specified algorithm and an encoding format.

Designer name: **Hash from file**. Official reference: [Cryptography / Hash from file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cryptography#hashfromfile).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Hash algorithm | Choice | SHA256, SHA384, SHA512 | SHA256 |
| Encoding | Choice | System default, ASCII, Unicode, Big-endian Unicode, UTF-8 | Unicode |
| File to hash | Required | File | — |

**Outputs**

| Variable | Type |
|---|---|
| HashedText | Text value |

**On error:** `File not found`, `Failed to hash the file`.

---

### Hash text with key

Hash a string with a key, using a specified algorithm and an encoding format.

Designer name: **Hash text with key**. Official reference: [Cryptography / Hash text with key](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cryptography#hashtextwithkey).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Hash algorithm | Choice | HMAC SHA256, HMAC SHA384, HMAC SHA512 | HMAC SHA256 |
| Encoding | Choice | System default, ASCII, Unicode, Big-endian Unicode, UTF-8 | Unicode |
| Text to hash | Required | Text value | — |
| Hash key | Required | Direct encrypted input or Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| HashedText | Text value |

**On error:** `Failed to hash text with key`.

---

### Hash from file with key

Hash the contents of a file with a key, using a specified algorithm and an encoding format.

Designer name: **Hash from file with key**. Official reference: [Cryptography / Hash from file with key](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cryptography#hashfromfilewithkey).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Hash algorithm | Choice | HMAC SHA256, HMAC SHA384, HMAC SHA512 | HMAC SHA256 |
| Encoding | Choice | System default, ASCII, Unicode, Big-endian Unicode, UTF-8 | Unicode |
| File to hash | Required | File | — |
| Hash key | Required | Direct encrypted input or Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| HashedText | Text value |

**On error:** `File not found`, `Failed to hash the file with key`.

---
