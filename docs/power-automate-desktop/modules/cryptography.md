# Cryptography

Hash or AES-encrypt text and files.

This page documents every **native action** in this group (8 items).

## Actions

### Decrypt text with AES

- **Inventory id:** `cryptography/decrypt-text-with-aes`
- **Kind:** native-action
- **Purpose:** Decrypts text with AES.
- **Key inputs:** `Encoding` (System default, ASCII, Unicode, Big-endian Unicode, UTF-8); `Text to decrypt` (Text value); `Decryption key` (Direct encrypted input or Text value); `Padding` (None, PKCS7, Zeros, ANSIX923, ISO10126); `Key size` (128 bits, 192 bits, 256 bits); `Use salt` (Boolean value); `Salt` (Text value); `Use initialization vector` (Boolean value); `Initialization vector` (Text value)
- **Produces:** `DecryptedText` (Text value)
- **Exceptions:** `Failed to decrypt text`
- **Microsoft Learn:** [Decrypt text with AES](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cryptography#decrypttextaction)

### Decrypt to file with AES

- **Inventory id:** `cryptography/decrypt-to-file-with-aes`
- **Kind:** native-action
- **Purpose:** Decrypts to file with AES.
- **Key inputs:** `Encoding` (System default, ASCII, Unicode, Big-endian Unicode, UTF-8); `Text to decrypt` (Text value); `Decryption key` (Direct encrypted input or Text value); `Decrypt to file` (File); `If file exists` (Overwrite, Don't decrypt to file, Add sequential suffix); `Padding` (None, PKCS7, Zeros, ANSIX923, ISO10126); `Key size` (128 bits, 192 bits, 256 bits); `Use salt` (Boolean value); `Salt` (Text value); `Use initialization vector` (Boolean value); `Initialization vector` (Text value)
- **Produces:** `DecryptedFile` (File)
- **Exceptions:** `Failed to decrypt and store the contents to a file`
- **Microsoft Learn:** [Decrypt to file with AES](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cryptography#decrypttofileaction)

### Encrypt from file with AES

- **Inventory id:** `cryptography/encrypt-from-file-with-aes`
- **Kind:** native-action
- **Purpose:** Encrypts from file with AES.
- **Key inputs:** `Encoding` (System default, ASCII, Unicode, Big-endian Unicode, UTF-8); `File to encrypt` (File); `Encryption key` (Direct encrypted input or Text value); `Padding` (None, PKCS7, Zeros, ANSIX923, ISO10126); `Key size` (128 bits, 192 bits, 256 bits); `Use salt` (Boolean value); `Use initialization vector` (Boolean value)
- **Produces:** `EncryptedText` (Text value); `Salt` (Text value); `InitializationVector` (Text value)
- **Exceptions:** `File not found`; `Failed to encrypt the contents of the file`
- **Microsoft Learn:** [Encrypt from file with AES](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cryptography#encryptfromfileaction)

### Encrypt text with AES

- **Inventory id:** `cryptography/encrypt-text-with-aes`
- **Kind:** native-action
- **Purpose:** Encrypts text with AES.
- **Key inputs:** `Encoding` (System default, ASCII, Unicode, Big-endian Unicode, UTF-8); `Text to encrypt` (Text value); `Encryption key` (Direct encrypted input or Text value); `Padding` (None, PKCS7, Zeros, ANSIX923, ISO10126); `Key size` (128 bits, 192 bits, 256 bits); `Use salt` (Boolean value); `Use initialization vector` (Boolean value)
- **Produces:** `EncryptedText` (Text value); `Salt` (Text value); `InitializationVector` (Text value)
- **Exceptions:** `Failed to encrypt text`
- **Microsoft Learn:** [Encrypt text with AES](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cryptography#encrypttextaction)

### Hash from file

- **Inventory id:** `cryptography/hash-from-file`
- **Kind:** native-action
- **Purpose:** Hashes from file.
- **Key inputs:** `Hash algorithm` (SHA256, SHA384, SHA512); `Encoding` (System default, ASCII, Unicode, Big-endian Unicode, UTF-8); `File to hash` (File)
- **Produces:** `HashedText` (Text value)
- **Exceptions:** `File not found`; `Failed to hash the file`
- **Microsoft Learn:** [Hash from file](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cryptography#hashfromfile)

### Hash from file with key

- **Inventory id:** `cryptography/hash-from-file-with-key`
- **Kind:** native-action
- **Purpose:** Hashes from file with key.
- **Key inputs:** `Hash algorithm` (HMAC SHA256, HMAC SHA384, HMAC SHA512); `Encoding` (System default, ASCII, Unicode, Big-endian Unicode, UTF-8); `File to hash` (File); `Hash key` (Direct encrypted input or Text value)
- **Produces:** `HashedText` (Text value)
- **Exceptions:** `File not found`; `Failed to hash the file with key`
- **Microsoft Learn:** [Hash from file with key](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cryptography#hashfromfilewithkey)

### Hash text

- **Inventory id:** `cryptography/hash-text`
- **Kind:** native-action
- **Purpose:** Hashes text.
- **Key inputs:** `Hash algorithm` (SHA256, SHA384, SHA512); `Encoding` (System default, ASCII, Unicode, Big-endian Unicode, UTF-8); `Text to hash` (Text value)
- **Produces:** `HashedText` (Text value)
- **Exceptions:** `Failed to hash text`
- **Microsoft Learn:** [Hash text](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cryptography#hashtext)

### Hash text with key

- **Inventory id:** `cryptography/hash-text-with-key`
- **Kind:** native-action
- **Purpose:** Hashes text with key.
- **Key inputs:** `Hash algorithm` (HMAC SHA256, HMAC SHA384, HMAC SHA512); `Encoding` (System default, ASCII, Unicode, Big-endian Unicode, UTF-8); `Text to hash` (Text value); `Hash key` (Direct encrypted input or Text value)
- **Produces:** `HashedText` (Text value)
- **Exceptions:** `Failed to hash text with key`
- **Microsoft Learn:** [Hash text with key](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cryptography#hashtextwithkey)
