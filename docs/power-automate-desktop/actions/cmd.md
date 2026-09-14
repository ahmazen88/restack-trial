# CMD session

Open a command prompt session and send commands interactively.

- Actions in this module: **5**
- Official docs: [CMD session actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cmd)

## Actions

### Open CMD session

Open a new CMD session.

Designer name: **Open CMD session**. Official reference: [CMD session / Open CMD session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cmd#open).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Working folder | Optional | Folder | — |
| Change code page | Choice | Boolean value | False |
| Encoding | Required | ASMO-708 : Arabic (ASMO 708), big5 : Chinese Traditional (Big5), cp1025 : IBM EBCDIC (Cyrillic Serbian-Bulgarian), cp866 : Cyrillic (DOS), cp875 : IBM EBCDIC (Greek Modern), csISO2022JP : Japanese (JIS-Allow 1 byte Kana), DOS-720 : Arabic (DOS), DOS-862 : Hebrew (DOS), EUC-CN : Chinese Simplified (EUC), EUC-JP : Japanese (JIS 0208-1990 and 0212-1990), euc-jp : Japanese (EUC), euc-kr : Korean (EUC), GB18030 : Chinese Simplified (GB18030), gb2312 : Chinese Simplified (GB2312), hz-gb-2312 : Chinese Simplified (HZ), IBM-Thai : IBM EBCDIC (Thai), IBM00858 : OEM Multilingual Latin I, IBM00924 : IBM Latin-1, IBM01047 : IBM Latin-1, IBM01140 : IBM EBCDIC (US-Canada-Euro), IBM01141 : IBM EBCDIC (Germany-Euro), IBM01142 : IBM EBCDIC (Denmark-Norway-Euro), IBM01143 : IBM EBCDIC (Finland-Sweden-Euro), IBM01144 : IBM EBCDIC (Italy-Euro), IBM01145 : IBM EBCDIC (Spain-Euro), IBM01146 : IBM EBCDIC (UK-Euro), IBM01147 : IBM EBCDIC (France-Euro), IBM01148 : IBM EBCDIC (International-Euro), IBM01149 : IBM EBCDIC (Icelandic-Euro), IBM037 : IBM EBCDIC (US-Canada), IBM1026 : IBM EBCDIC (Turkish Latin-5), IBM273 : IBM EBCDIC (Germany), IBM277 : IBM EBCDIC (Denmark-Norway), IBM278 : IBM EBCDIC (Finland-Sweden), IBM280 : IBM EBCDIC (Italy), IBM284 : IBM EBCDIC (Spain), IBM285 : IBM EBCDIC (UK), IBM290 : IBM EBCDIC (Japanese katakana), IBM297 : IBM EBCDIC (France), IBM420 : IBM EBCDIC (Arabic), IBM423 : IBM EBCDIC (Greek), IBM424 : IBM EBCDIC (Hebrew), IBM437 : OEM United States, IBM500 : IBM EBCDIC (International), ibm737 : Greek (DOS), ibm775 : Baltic (DOS), ibm850 : Western European (DOS), ibm852 : Central European (DOS), IBM855 : OEM Cyrillic, ibm857 : Turkish (DOS), IBM860 : Portuguese (DOS), ibm861 : Icelandic (DOS), IBM863 : French Canadian (DOS), IBM864 : Arabic (864), IBM865 : Nordic (DOS), ibm869 : Greek, Modern (DOS), IBM870 : IBM EBCDIC (Multilingual Latin-2), IBM871 : IBM EBCDIC (Icelandic), IBM880 : IBM EBCDIC (Cyrillic Russian), IBM905 : IBM EBCDIC (Turkish), iso-2022-jp : Japanese (JIS), iso-2022-jp : Japanese (JIS-Allow 1 byte Kana - SO/SI), iso-2022-kr : Korean (ISO), iso-8859-1 : Western European (ISO), iso-8859-13 : Estonian (ISO), iso-8859-15 : Latin 9 (ISO), iso-8859-2 : Central European (ISO), iso-8859-3 : Latin 3 (ISO), iso-8859-4 : Baltic (ISO), iso-8859-5 : Cyrillic (ISO), iso-8859-6 : Arabic (ISO), iso-8859-7 : Greek (ISO), iso-8859-8 : Hebrew (ISO-Visual), iso-8859-8-i : Hebrew (ISO-Logical), iso-8859-9 : Turkish (ISO), Johab : Korean (Johab), koi8-r : Cyrillic (KOI8-R), koi8-u : Cyrillic (KOI8-U), ks_c_5601-1987 : Korean, macintosh : Western European (Mac), shift_jis : Japanese (Shift-JIS), us-ascii : US-ASCII, utf-16 : Unicode, utf-16BE : Unicode (Big-Endian), utf-32 : Unicode (UTF-32), utf-32BE : Unicode (UTF-32 Big-Endian), utf-7 : Unicode (UTF-7), utf-8 : Unicode (UTF-8), windows-1250 : Central European (Windows), windows-1251 : Cyrillic (Windows), Windows-1252 : Western European (Windows), windows-1253 : Greek (Windows), windows-1254 : Turkish (Windows), windows-1255 : Hebrew (Windows), windows-1256 : Arabic (Windows), windows-1257 : Baltic (Windows), windows-1258 : Vietnamese (Windows), windows-874 : Thai (Windows), x-Chinese-CNS : Chinese Traditional (CNS), x-Chinese-Eten : Chinese Traditional (Eten), x-cp20001 : TCA Taiwan, x-cp20003 : IBM5550 Taiwan, x-cp20004 : TeleText Taiwan, x-cp20005 : Wang Taiwan, x-cp20261 : T.61, x-cp20269 : ISO-6937, x-cp20936 : Chinese Simplified (GB2312-80), x-cp20949 : Korean Wansung, x-cp50227 : Chinese Simplified (ISO-2022), x-EBCDIC-KoreanExtended : IBM EBCDIC (Korean Extended), x-Europa : Europa, x-IA5 : Western European (IA5), x-IA5-German : German (IA5), x-IA5-Norwegian : Norwegian (IA5), x-IA5-Swedish : Swedish (IA5), x-iscii-as : ISCII Assamese, x-iscii-be : ISCII Bengali, x-iscii-de : ISCII Devanagari, x-iscii-gu : ISCII Gujarati, x-iscii-ka : ISCII Kannada, x-iscii-ma : ISCII Malayalam, x-iscii-or : ISCII Oriya, x-iscii-pa : ISCII Punjabi, x-iscii-ta : ISCII Tamil, x-iscii-te : ISCII Telugu, x-mac-arabic : Arabic (Mac), x-mac-ce : Central European (Mac), x-mac-chinesesimp : Chinese Simplified (Mac), x-mac-chinesetrad : Chinese Traditional (Mac), x-mac-croatian : Croatian (Mac), x-mac-cyrillic : Cyrillic (Mac), x-mac-greek : Greek (Mac), x-mac-hebrew : Hebrew (Mac), x-mac-icelandic : Icelandic (Mac), x-mac-japanese : Japanese (Mac), x-mac-korean : Korean (Mac), x-mac-romanian : Romanian (Mac), x-mac-thai : Thai (Mac), x-mac-turkish : Turkish (Mac), x-mac-ukrainian : Ukrainian (Mac)` | utf-8 : Unicode (UTF-8) |

**Outputs**

| Variable | Type |
|---|---|
| CmdSession | CMD session |

**On error:** `Can't start command session`, `Working directory doesn't exist`.

---

### Read from CMD session

Read the output of a CMD session.

Designer name: **Read from CMD session**. Official reference: [CMD session / Read from CMD session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cmd#readfromcmdsession).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| CMD session | Required | CMD session | — |
| Separate output from error | Choice | Boolean value | False |

**Outputs**

| Variable | Type |
|---|---|
| CmdOutput | Text value |
| CmdError | Text value |

**On error:** `CMD session is closed`.

---

### Write to CMD session

Execute a command on an open CMD session.

Designer name: **Write to CMD session**. Official reference: [CMD session / Write to CMD session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cmd#write).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| CMD session | Required | CMD session | — |
| Command | Required | Text value | — |
| Send Enter after command | Choice | Boolean value | True |

Produces no variables.

**On error:** `Can't write to CMD session`, `CMD session is closed`.

---

### Wait for text on CMD session

Wait for a specific text on a previously opened CMD session.

Designer name: **Wait for text on CMD session**. Official reference: [CMD session / Wait for text on CMD session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cmd#waitfortext).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| CMD session | Required | CMD session | — |
| Text to wait | Required | Text value | — |
| Is regular expression | Choice | Boolean value | False |
| Ignore case | Choice | Boolean value | True |
| Timeout | Optional | Numeric value | 0 |

Produces no variables.

**On error:** `CMD session is closed`, `Timeout occurred while waiting for text`.

---

### Close CMD session

Close a previously opened CMD session.

Designer name: **Close CMD session**. Official reference: [CMD session / Close CMD session](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/cmd#close).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| CMD session | Required | CMD session | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---
