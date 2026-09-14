# Scripting

Run DOS, VBScript, JavaScript, PowerShell, Python, and .NET scripts.

- Actions in this module: **6**
- Official docs: [Scripting actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/scripting)

## Actions

### Run DOS command

Executes a DOS command or console application in invisible mode and retrieves its output upon completion.

Designer name: **Run DOS command**. Official reference: [Scripting / Run DOS command](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/scripting#rundoscommand).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| DOS command or application | Required | File | — |
| Working folder | Optional | Folder | — |
| Fail after timeout | Optional | Boolean value | — |
| Timeout | Required | Numeric value | 10 |
| Change code page | Choice | Boolean value | False |
| Encoding | Required | ASMO-708: Arabic (ASMO 708), big5: Chinese Traditional (Big5), cp1025: IBM EBCDIC (Cyrillic Serbian-Bulgarian), cp866: Cyrillic (DOS), cp875: IBM EBCDIC (Greek Modern), csISO2022JP: Japanese (JIS-Allow 1 byte Kana), DOS-720: Arabic (DOS), DOS-862: Hebrew (DOS), EUC-CN: Chinese Simplified (EUC), EUC-JP: Japanese (JIS 0208-1990 and 0212-1990), euc-jp: Japanese (EUC), euc-kr: Korean (EUC), GB18030: Chinese Simplified (GB18030), gb2312: Chinese Simplified (GB2312), hz-gb-2312: Chinese Simplified (HZ), IBM-Thai: IBM EBCDIC (Thai), IBM00858: OEM Multilingual Latin I, IBM00924: IBM Latin-1, IBM01047: IBM Latin-1, IBM01140: IBM EBCDIC (US-Canada-Euro), IBM01141: IBM EBCDIC (Germany-Euro), IBM01142: IBM EBCDIC (Denmark-Norway-Euro), IBM01143: IBM EBCDIC (Finland-Sweden-Euro), IBM01144: IBM EBCDIC (Italy Euro), IBM01145: IBM EBCDIC (Spain-Euro), IBM01146: IBM EBCDIC (UK-Euro), IBM01147: IBM EBCDIC (France-Euro), IBM01148: IBM EBCDIC (International-Euro), IBM01149: IBM EBCDIC (Icelandic-Euro), IBM037: IBM EBCDIC (US-Canada), IBM1026: IBM EBCDIC (Turkish Latin-5), IBM273: IBM EBCDIC (Germany), IBM277: IBM EBCDIC (Denmark-Norway), IBM278: IBM EBCDIC (Finland-Sweden), IBM280: IBM EBCDIC (Italy), IBM284: IBM EBCDIC (Spain), IBM285: IBM EBCDIC (UK), IBM290: IBM EBCDIC (Japanese katakana), IBM297: IBM EBCDIC (France), IBM420: IBM EBCDIC (Arabic), IBM423: IBM EBCDIC (Greek), IBM424: IBM EBCDIC (Hebrew), IBM437: OEM United States, IBM500: IBM EBCDIC (International), ibm737: Greek (DOS), ibm775: Baltic (DOS), ibm850: Western European (DOS), ibm852: Central European (DOS), IBM855: OEM Cyrillic, ibm857: Turkish (DOS), IBM860: Portuguese (DOS), ibm861: Icelandic (DOS), IBM863: French Canadian (DOS), IBM864: Arabic (864), IBM865: Nordic (DOS), ibm869: Greek, Modern (DOS), IBM870: IBM EBCDIC (Multilingual Latin-2), IBM871: IBM EBCDIC (Icelandic), IBM880: IBM EBCDIC (Cyrillic Russian), IBM905: IBM EBCDIC (Turkish), iso-2022-jp: Japanese (JIS), iso-2022-jp: Japanese (JIS-Allow 1 byte Kana - SO/SI), iso-2022-kr: Korean (ISO), iso-8859-1: Western European (ISO), iso-8859-13: Estonian (ISO), iso-8859-15: Latin 9 (ISO), iso-8859-2: Central European (ISO), iso-8859-3: Latin 3 (ISO), iso-8859-4: Baltic (ISO), iso-8859-5: Cyrillic (ISO), iso-8859-6: Arabic (ISO), iso-8859-7: Greek (ISO), iso-8859-8: Hebrew (ISO-Visual), iso-8859-8-i: Hebrew (ISO-Logical), iso-8859-9: Turkish (ISO), Johab: Korean (Johab), koi8-r: Cyrillic (KOI8-R), koi8-u: Cyrillic (KOI8-U), ks_c_5601-1987: Korean, macintosh: Western European (Mac), shift_jis: Japanese (Shift-JIS), us-ascii: US-ASCII, utf-16: Unicode, utf-16BE: Unicode (Big-Endian), utf-32: Unicode (UTF-32), utf-32BE: Unicode (UTF-32 Big-Endian), utf-7: Unicode (UTF-7), utf-8: Unicode (UTF-8), windows-1250: Central European (Windows), windows-1251: Cyrillic (Windows), Windows-1252: Western European (Windows), windows-1253: Greek (Windows), windows-1254: Turkish (Windows), windows-1255: Hebrew (Windows), windows-1256: Arabic (Windows), windows-1257: Baltic (Windows), windows-1258: Vietnamese (Windows), windows-874: Thai (Windows), x-Chinese-CNS: Chinese Traditional (CNS), x-Chinese-Eten: Chinese Traditional (Eten), x-cp20001: TCA Taiwan, x-cp20003: IBM5550 Taiwan, x-cp20004: TeleText Taiwan, x-cp20005: Wang Taiwan, x-cp20261: T.61, x-cp20269: ISO-6937, x-cp20936: Chinese Simplified (GB2312-80), x-cp20949: Korean Wansung, x-cp50227: Chinese Simplified (ISO-2022), x-EBCDIC-KoreanExtended: IBM EBCDIC (Korean Extended), x-Europa: Europa, x-IA5: Western European (IA5), x-IA5-German: German (IA5), x-IA5-Norwegian: Norwegian (IA5), x-IA5-Swedish: Swedish (IA5), x-iscii-as: ISCII Assamese, x-iscii-be: ISCII Bengali, x-iscii-de: ISCII Devanagari, x-iscii-gu: ISCII Gujarati, x-iscii-ka: ISCII Kannada, x-iscii-ma: ISCII Malayalam, x-iscii-or: ISCII Oriya, x-iscii-pa: ISCII Punjabi, x-iscii-ta: ISCII Tamil, x-iscii-te: ISCII Telugu, x-mac-arabic: Arabic (Mac), x-mac-ce: Central European (Mac), x-mac-chinesesimp: Chinese Simplified (Mac), x-mac-chinesetrad: Chinese Traditional (Mac), x-mac-croatian: Croatian (Mac), x-mac-cyrillic: Cyrillic (Mac), x-mac-greek: Greek (Mac), x-mac-hebrew: Hebrew (Mac), x-mac-icelandic: Icelandic (Mac), x-mac-japanese: Japanese (Mac), x-mac-korean: Korean (Mac), x-mac-romanian: Romanian (Mac), x-mac-thai: Thai (Mac), x-mac-turkish: Turkish (Mac), x-mac-ukrainian: Ukrainian (Mac)` | utf-8: Unicode (UTF-8) |

**Outputs**

| Variable | Type |
|---|---|
| CommandOutput | Text value |
| CommandErrorOutput | Text value |
| CommandExitCode | Numeric value |

**On error:** `Can't execute command or console application`, `Failed to run script in the allotted time`.

---

### Run VBScript

Executes some custom VBScript code and retrieves its output into a variable.

Designer name: **Run VBScript**. Official reference: [Scripting / Run VBScript](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/scripting#runvbscript).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| VBScript to run | Optional | Text value | — |
| Fail after timeout | Optional | Boolean value | N/A |
| Timeout | Required | Numeric value | 10 |

**Outputs**

| Variable | Type |
|---|---|
| VBScriptOutput | Text value |
| ScriptError | Text value |

**On error:** `Failed to run script in the allotted time`.

---

### Run JavaScript

Executes some custom JavaScript code and retrieves its output into a variable.

Designer name: **Run JavaScript**. Official reference: [Scripting / Run JavaScript](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/scripting#runjavascript).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| JavaScript to run | Optional | Text value | — |
| Fail after timeout | Optional | Boolean value | — |
| Timeout | Required | Numeric value | 10 |

**Outputs**

| Variable | Type |
|---|---|
| JavascriptOutput | Text value |
| ScriptError | Text value |

**On error:** `Failed to run script in the allotted time`.

---

### Run PowerShell script

Executes some custom PowerShell script and retrieves its output into a variable.

Designer name: **Run PowerShell script**. Official reference: [Scripting / Run PowerShell script](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/scripting#runpowershellscript).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| PowerShell code to run | Optional | Text value | — |
| Fail after timeout | Optional | Boolean value | — |
| Timeout | Required | Numeric value | 10 |

**Outputs**

| Variable | Type |
|---|---|
| PowershellOutput | Text value |
| ScriptError | Text value |

**On error:** `Failed to run PowerShell script`, `Failed to run script in the allotted time`.

---

### Run Python script

Executes Python script code and retrieves its output.

Designer name: **Run Python script**. Official reference: [Scripting / Run Python script](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/scripting#runpythonscript).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Python script to run | Required | Text value | — |
| Python version | Required | Python 2.7, Python 3.4 | Python 2.7 |
| Module folder paths | Optional | List of Folders | — |

**Outputs**

| Variable | Type |
|---|---|
| PythonScriptOutput | Text value |
| ScriptError | Text value |

**On error:** `Failed to run Python script`, `Directory not found`.

---

### Run .NET script

Executes .NET (C#/VB.NET) script code and retrieves its output.

Designer name: **Run .NET script**. Official reference: [Scripting / Run .NET script](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/scripting#rundotnetscript).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Language | Choice | C#/ VB.NET | C# |
| .NET script imports | Optional | Text value | — |
| References to be loaded | Optional | Folder | — |
| Script parameters | Optional | Script Parameters as defined by the user | — |
| .NET code to run | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| (flow outputs) | * |

**On error:** `Failed to run the .NET script`.

---
