# HTTP

Call REST and SOAP endpoints and download files over HTTP.

- Actions in this module: **3**
- Official docs: [HTTP actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/web)

## Actions

### Download from web

Downloads text or a file from the web and stores it.

Designer name: **Download from web**. Official reference: [HTTP / Download from web](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/web#downloadfromweb).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| URL | Required | Text value | — |
| Method | Choice | GET, POST | GET |
| Post parameters | Required | Datatable | — |
| Save response | Choice | Get text into variable (for web pages), Save to disk (for files) | Get text into variable (for web pages) |
| File name | Choice | Keep original file name (specify only destination folder), Specify full path (destination folder + custom file name) | Keep original file name (specify only destination folder) |
| Destination folder | Required | Folder | — |
| Destination file path | Required | File | — |
| Connection timeout | Optional | Numeric value | 30 |
| Follow redirection | Choice | Boolean value | True |
| Clear cookies | Choice | Boolean value | False |
| User agent | Optional | Text value | Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.21) Gecko/20100312 Firefox/3.6 |
| Encoding | Choice | Auto - detect, IBM037: IBM EBCDIC (US-Canada), IBM437: OEM United States, IBM500: IBM EBCDIC (International), ASMO-708: Arabic (ASMO 708), DOS-720: Arabic (DOS), ibm737: Greek (DOS), ibm775: Baltic (DOS), ibm850: Western European (DOS), ibm852: Central European (DOS), IBM855: OEM Cyrillic, ibm857: Turkish (DOS), IBM00858: OEM Multilingual Latin I, IBM860: Portuguese (DOS), ibm861: Icelandic (DOS), DOS-862: Hebrew (DOS), IBM863: French Canadian (DOS), IBM864: Arabic (864), IBM865: Nordic (DOS), cp866: Cyrillic (DOS), ibm869: Greek, Modern (DOS), IBM870: IBM EBCDIC (Multilingual Latin-2), windows-874: Thai (Windows), cp875: IBM EBCDIC (Greek Modern), shift_jis: Japanese (Shift-JIS), gb2312: Chinese Simplified (GB2312), ks_c_5601-1987: Korean, big5: Chinese Traditional (Big5), IBM1026: IBM EBCDIC (Turkish Latin-5), IBM01047: IBM Latin-1, IBM01140: IBM EBCDIC (US-Canada-Euro), IBM01141: IBM EBCDIC (Germany-Euro), IBM01142: IBM EBCDIC (Denmark-Norway-Euro), IBM01143: IBM EBCDIC (Finland-Sweden-Euro), IBM01144: IBM EBCDIC (Italy Euro), IBM01145: IBM EBCDIC (Spain-Euro), IBM01146: IBM EBCDIC (UK-Euro), IBM01147: IBM EBCDIC (France-Euro), IBM01148: IBM EBCDIC (International-Euro), IBM01149: IBM EBCDIC (Icelandic-Euro), utf-16: Unicode, utf-16BE: Unicode (Big-Endian), windows-1250: Central European (Windows), windows-1251: Cyrillic (Windows), Windows-1252: Western European (Windows), windows-1253: Greek (Windows), windows-1254: Turkish (Windows), windows-1255: Hebrew (Windows), windows-1256: Arabic (Windows), windows-1257: Baltic (Windows), windows-1258: Vietnamese (Windows), Johab: Korean (Johab), macintosh: Western European (Mac), x-mac-japanese: Japanese (Mac), x-mac-chinesetrad: Chinese Traditional (Mac), x-mac-korean: Korean (Mac), x-mac-arabic: Arabic (Mac), x-mac-hebrew: Hebrew (Mac), x-mac-greek: Greek (Mac), x-mac-cyrillic: Cyrillic (Mac), x-mac-chinesesimp: Chinese Simplified (Mac), x-mac-romanian: Romanian (Mac), x-mac-ukrainian: Ukrainian (Mac), x-mac-thai: Thai (Mac), x-mac-ce: Central European (Mac), x-mac-icelandic: Icelandic (Mac), x-mac-turkish: Turkish (Mac), x-mac-croatian: Croatian (Mac), utf-32: Unicode (UTF-32), utf-32BE: Unicode (UTF-32 Big-Endian), x-Chinese-CNS: Chinese Traditional (CNS), x-cp20001: TCA Taiwan, x-Chinese-Eten: Chinese Traditional (Eten), x-cp20003: IBM5550 Taiwan, x-cp20004: TeleText Taiwan, x-cp20005: Wang Taiwan, x-IA5: Western European (IA5), x-IA5-German: German (IA5), x-IA5-Swedish: Swedish (IA5), x-IA5-Norwegian: Norwegian (IA5), us-ascii: US-ASCII, x-cp20261: T.61, x-cp20269: ISO-6937, IBM273: IBM EBCDIC (Germany), IBM277: IBM EBCDIC (Denmark-Norway), IBM278: IBM EBCDIC (Finland-Sweden), IBM280: IBM EBCDIC (Italy), IBM284: IBM EBCDIC (Spain), IBM285: IBM EBCDIC (UK), IBM290: IBM EBCDIC (Japanese katakana), IBM297: IBM EBCDIC (France), IBM420: IBM EBCDIC (Arabic), IBM423: IBM EBCDIC (Greek), IBM424: IBM EBCDIC (Hebrew), x-EBCDIC-KoreanExtended: IBM EBCDIC (Korean Extended), IBM-Thai: IBM EBCDIC (Thai), koi8-r: Cyrillic (KOI8-R), IBM871: IBM EBCDIC (Icelandic), IBM880: IBM EBCDIC (Cyrillic Russian), IBM905: IBM EBCDIC (Turkish), IBM00924: IBM Latin-1, EUC-JP: Japanese (JIS 0208-1990 and 0212-1990), x-cp20936: Chinese Simplified (GB2312-80), x-cp20949: Korean Wansung, cp1025: IBM EBCDIC (Cyrillic Serbian-Bulgarian), koi8-u: Cyrillic (KOI8-U), iso-8859-1: Western European (ISO), iso-8859-2: Central European (ISO), iso-8859-3: Latin 3 (ISO), iso-8859-4: Baltic (ISO), iso-8859-5: Cyrillic (ISO), iso-8859-6: Arabic (ISO), iso-8859-7: Greek (ISO), iso-8859-8: Hebrew (ISO-Visual), iso-8859-9: Turkish (ISO), iso-8859-13: Estonian (ISO), iso-8859-15: Latin 9 (ISO), x-Europa: Europa, iso-8859-8-i: Hebrew (ISO-Logical), iso-2022-jp: Japanese (JIS), csISO2022JP: Japanese (JIS-Allow 1 byte Kana), iso-2022-jp: Japanese (JIS-Allow 1 byte Kana - SO/SI), iso-2022-kr: Korean (ISO), x-cp50227: Chinese Simplified (ISO-2022), euc-jp: Japanese (EUC), EUC-CN: Chinese Simplified (EUC), euc-kr: Korean (EUC), hz-gb-2312: Chinese Simplified (HZ), GB18030: Chinese Simplified (GB18030), x-iscii-de: ISCII Devanagari, x-iscii-be: ISCII Bengali, x-iscii-ta: ISCII Tamil, x-iscii-te: ISCII Telugu, x-iscii-as: ISCII Assamese, x-iscii-or: ISCII Oriya, x-iscii-ka: ISCII Kannada, x-iscii-ma: ISCII Malayalam, x-iscii-gu: ISCII Gujarati, x-iscii-pa: ISCII Punjabi, utf-7: Unicode (UTF-7), utf-8: Unicode (UTF-8) | Auto - detect |
| Accept untrusted certificates | Choice | Boolean value | False |
| Use credentials | Choice | Boolean value | False |
| User name | Required | Text value | — |
| Password | Required | Direct encrypted input or Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| DownloadedFile | File |
| WebPageText | Text value |

**On error:** `Directory doesn't exist`, `Download from web error`.

---

### Invoke SOAP web service

Invokes a method from a SOAP web service.

Designer name: **Invoke SOAP web service**. Official reference: [HTTP / Invoke SOAP web service](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/web#invokesoapserviceaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Endpoint | Required | Text value | — |
| Custom headers | Optional | Text value | — |
| Request body | Required | Text value | — |
| Connection timeout | Required | Numeric value | 30 |
| Follow redirection | Choice | Boolean value | True |
| Clear cookies | Choice | Boolean value | False |
| Fail on error status | Choice | Boolean value | False |
| User agent | Required | Text value | Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.21) Gecko/20100312 Firefox/3.6 |
| User agent | Optional | Text value | Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.21) Gecko/20100312 Firefox/3.6 |
| Encoding | Choice | Auto - detect, IBM037: IBM EBCDIC (US-Canada), IBM437: OEM United States, IBM500: IBM EBCDIC (International), ASMO-708: Arabic (ASMO 708), DOS-720: Arabic (DOS), ibm737: Greek (DOS), ibm775: Baltic (DOS), ibm850: Western European (DOS), ibm852: Central European (DOS), IBM855: OEM Cyrillic, ibm857: Turkish (DOS), IBM00858: OEM Multilingual Latin I, IBM860: Portuguese (DOS), ibm861: Icelandic (DOS), DOS-862: Hebrew (DOS), IBM863: French Canadian (DOS), IBM864: Arabic (864), IBM865: Nordic (DOS), cp866: Cyrillic (DOS), ibm869: Greek, Modern (DOS), IBM870: IBM EBCDIC (Multilingual Latin-2), windows-874: Thai (Windows), cp875: IBM EBCDIC (Greek Modern), shift_jis: Japanese (Shift-JIS), gb2312: Chinese Simplified (GB2312), ks_c_5601-1987: Korean, big5: Chinese Traditional (Big5), IBM1026: IBM EBCDIC (Turkish Latin-5), IBM01047: IBM Latin-1, IBM01140: IBM EBCDIC (US-Canada-Euro), IBM01141: IBM EBCDIC (Germany-Euro), IBM01142: IBM EBCDIC (Denmark-Norway-Euro), IBM01143: IBM EBCDIC (Finland-Sweden-Euro), IBM01144: IBM EBCDIC (Italy Euro), IBM01145: IBM EBCDIC (Spain-Euro), IBM01146: IBM EBCDIC (UK-Euro), IBM01147: IBM EBCDIC (France-Euro), IBM01148: IBM EBCDIC (International-Euro), IBM01149: IBM EBCDIC (Icelandic-Euro), utf-16: Unicode, utf-16BE: Unicode (Big-Endian), windows-1250: Central European (Windows), windows-1251: Cyrillic (Windows), Windows-1252: Western European (Windows), windows-1253: Greek (Windows), windows-1254: Turkish (Windows), windows-1255: Hebrew (Windows), windows-1256: Arabic (Windows), windows-1257: Baltic (Windows), windows-1258: Vietnamese (Windows), Johab: Korean (Johab), macintosh: Western European (Mac), x-mac-japanese: Japanese (Mac), x-mac-chinesetrad: Chinese Traditional (Mac), x-mac-korean: Korean (Mac), x-mac-arabic: Arabic (Mac), x-mac-hebrew: Hebrew (Mac), x-mac-greek: Greek (Mac), x-mac-cyrillic: Cyrillic (Mac), x-mac-chinesesimp: Chinese Simplified (Mac), x-mac-romanian: Romanian (Mac), x-mac-ukrainian: Ukrainian (Mac), x-mac-thai: Thai (Mac), x-mac-ce: Central European (Mac), x-mac-icelandic: Icelandic (Mac), x-mac-turkish: Turkish (Mac), x-mac-croatian: Croatian (Mac), utf-32: Unicode (UTF-32), utf-32BE: Unicode (UTF-32 Big-Endian), x-Chinese-CNS: Chinese Traditional (CNS), x-cp20001: TCA Taiwan, x-Chinese-Eten: Chinese Traditional (Eten), x-cp20003: IBM5550 Taiwan, x-cp20004: TeleText Taiwan, x-cp20005: Wang Taiwan, x-IA5: Western European (IA5), x-IA5-German: German (IA5), x-IA5-Swedish: Swedish (IA5), x-IA5-Norwegian: Norwegian (IA5), us-ascii: US-ASCII, x-cp20261: T.61, x-cp20269: ISO-6937, IBM273: IBM EBCDIC (Germany), IBM277: IBM EBCDIC (Denmark-Norway), IBM278: IBM EBCDIC (Finland-Sweden), IBM280: IBM EBCDIC (Italy), IBM284: IBM EBCDIC (Spain), IBM285: IBM EBCDIC (UK), IBM290: IBM EBCDIC (Japanese katakana), IBM297: IBM EBCDIC (France), IBM420: IBM EBCDIC (Arabic), IBM423: IBM EBCDIC (Greek), IBM424: IBM EBCDIC (Hebrew), x-EBCDIC-KoreanExtended: IBM EBCDIC (Korean Extended), IBM-Thai: IBM EBCDIC (Thai), koi8-r: Cyrillic (KOI8-R), IBM871: IBM EBCDIC (Icelandic), IBM880: IBM EBCDIC (Cyrillic Russian), IBM905: IBM EBCDIC (Turkish), IBM00924: IBM Latin-1, EUC-JP: Japanese (JIS 0208-1990 and 0212-1990), x-cp20936: Chinese Simplified (GB2312-80), x-cp20949: Korean Wansung, cp1025: IBM EBCDIC (Cyrillic Serbian-Bulgarian), koi8-u: Cyrillic (KOI8-U), iso-8859-1: Western European (ISO), iso-8859-2: Central European (ISO), iso-8859-3: Latin 3 (ISO), iso-8859-4: Baltic (ISO), iso-8859-5: Cyrillic (ISO), iso-8859-6: Arabic (ISO), iso-8859-7: Greek (ISO), iso-8859-8: Hebrew (ISO-Visual), iso-8859-9: Turkish (ISO), iso-8859-13: Estonian (ISO), iso-8859-15: Latin 9 (ISO), x-Europa: Europa, iso-8859-8-i: Hebrew (ISO-Logical), iso-2022-jp: Japanese (JIS), csISO2022JP: Japanese (JIS-Allow 1 byte Kana), iso-2022-jp: Japanese (JIS-Allow 1 byte Kana - SO/SI), iso-2022-kr: Korean (ISO), x-cp50227: Chinese Simplified (ISO-2022), euc-jp: Japanese (EUC), EUC-CN: Chinese Simplified (EUC), euc-kr: Korean (EUC), hz-gb-2312: Chinese Simplified (HZ), GB18030: Chinese Simplified (GB18030), x-iscii-de: ISCII Devanagari, x-iscii-be: ISCII Bengali, x-iscii-ta: ISCII Tamil, x-iscii-te: ISCII Telugu, x-iscii-as: ISCII Assamese, x-iscii-or: ISCII Oriya, x-iscii-ka: ISCII Kannada, x-iscii-ma: ISCII Malayalam, x-iscii-gu: ISCII Gujarati, x-iscii-pa: ISCII Punjabi, utf-7: Unicode (UTF-7), utf-8: Unicode (UTF-8) | Auto - detect |
| Accept untrusted certificates | Choice | Boolean value | False |
| HTTP Authentication | Choice | Boolean value | False |
| User name | Required | Text value | — |
| Password | Required | Direct encrypted input or Text value | — |
| Trim whitespaces | Choice | Boolean value | True |

**Outputs**

| Variable | Type |
|---|---|
| SoapServiceResponseHeaders | List of Text values |
| SoapServiceResponse | Text value |
| StatusCode | Numeric value |

**On error:** `Invoke SOAP service error`, `Invalid header in custom headers`.

---

### Invoke web service

Invokes a web service by sending data and stores the response text.

Designer name: **Invoke web service**. Official reference: [HTTP / Invoke web service](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/web#invokewebservicebase).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| URL | Required | Text value | — |
| Method | Choice | GET, POST, CONNECT, HEAD, PUT, DELETE, OPTIONS, TRACE, PATCH | GET |
| Accept | Optional | Text value | application/xml |
| Custom headers | Optional | Text value | — |
| Upload attachments | Choice | Boolean value | False |
| Content type | Optional | Text value | application/xml |
| Request body | Optional | Text value | — |
| Attachments | Choice | Attachments | No attachments selected |
| Attach | Choice | File, Binary | File |
| Save response | Choice | Get text into variable (for web pages), Save to disk (for files) | Get text into variable (for web pages) |
| File name | Choice | Keep original file name (specify only destination folder), Specify full path (destination folder + custom file name) | Keep original file name (specify only destination folder) |
| Destination folder | Required | Folder | — |
| Destination file path | Required | File | — |
| Connection timeout | Optional | Numeric value | 30 |
| Follow redirection | Choice | Boolean value | True |
| Clear cookies | Choice | Boolean value | False |
| Fail on error status | Choice | Boolean value | False |
| Encode request body | Choice | Boolean value | True |
| User agent | Optional | Text value | Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.21) Gecko/20100312 Firefox/3.6 |
| Encoding | Choice | Auto - detect, IBM037: IBM EBCDIC (US-Canada), IBM437: OEM United States, IBM500: IBM EBCDIC (International), ASMO-708: Arabic (ASMO 708), DOS-720: Arabic (DOS), ibm737: Greek (DOS), ibm775: Baltic (DOS), ibm850: Western European (DOS), ibm852: Central European (DOS), IBM855: OEM Cyrillic, ibm857: Turkish (DOS), IBM00858: OEM Multilingual Latin I, IBM860: Portuguese (DOS), ibm861: Icelandic (DOS), DOS-862: Hebrew (DOS), IBM863: French Canadian (DOS), IBM864: Arabic (864), IBM865: Nordic (DOS), cp866: Cyrillic (DOS), ibm869: Greek, Modern (DOS), IBM870: IBM EBCDIC (Multilingual Latin-2), windows-874: Thai (Windows), cp875: IBM EBCDIC (Greek Modern), shift_jis: Japanese (Shift-JIS), gb2312: Chinese Simplified (GB2312), ks_c_5601-1987: Korean, big5: Chinese Traditional (Big5), IBM1026: IBM EBCDIC (Turkish Latin-5), IBM01047: IBM Latin-1, IBM01140: IBM EBCDIC (US-Canada-Euro), IBM01141: IBM EBCDIC (Germany-Euro), IBM01142: IBM EBCDIC (Denmark-Norway-Euro), IBM01143: IBM EBCDIC (Finland-Sweden-Euro), IBM01144: IBM EBCDIC (Italy Euro), IBM01145: IBM EBCDIC (Spain-Euro), IBM01146: IBM EBCDIC (UK-Euro), IBM01147: IBM EBCDIC (France-Euro), IBM01148: IBM EBCDIC (International-Euro), IBM01149: IBM EBCDIC (Icelandic-Euro), utf-16: Unicode, utf-16BE: Unicode (Big-Endian), windows-1250: Central European (Windows), windows-1251: Cyrillic (Windows), Windows-1252: Western European (Windows), windows-1253: Greek (Windows), windows-1254: Turkish (Windows), windows-1255: Hebrew (Windows), windows-1256: Arabic (Windows), windows-1257: Baltic (Windows), windows-1258: Vietnamese (Windows), Johab: Korean (Johab), macintosh: Western European (Mac), x-mac-japanese: Japanese (Mac), x-mac-chinesetrad: Chinese Traditional (Mac), x-mac-korean: Korean (Mac), x-mac-arabic: Arabic (Mac), x-mac-hebrew: Hebrew (Mac), x-mac-greek: Greek (Mac), x-mac-cyrillic: Cyrillic (Mac), x-mac-chinesesimp: Chinese Simplified (Mac), x-mac-romanian: Romanian (Mac), x-mac-ukrainian: Ukrainian (Mac), x-mac-thai: Thai (Mac), x-mac-ce: Central European (Mac), x-mac-icelandic: Icelandic (Mac), x-mac-turkish: Turkish (Mac), x-mac-croatian: Croatian (Mac), utf-32: Unicode (UTF-32), utf-32BE: Unicode (UTF-32 Big-Endian), x-Chinese-CNS: Chinese Traditional (CNS), x-cp20001: TCA Taiwan, x-Chinese-Eten: Chinese Traditional (Eten), x-cp20003: IBM5550 Taiwan, x-cp20004: TeleText Taiwan, x-cp20005: Wang Taiwan, x-IA5: Western European (IA5), x-IA5-German: German (IA5), x-IA5-Swedish: Swedish (IA5), x-IA5-Norwegian: Norwegian (IA5), us-ascii: US-ASCII, x-cp20261: T.61, x-cp20269: ISO-6937, IBM273: IBM EBCDIC (Germany), IBM277: IBM EBCDIC (Denmark-Norway), IBM278: IBM EBCDIC (Finland-Sweden), IBM280: IBM EBCDIC (Italy), IBM284: IBM EBCDIC (Spain), IBM285: IBM EBCDIC (UK), IBM290: IBM EBCDIC (Japanese katakana), IBM297: IBM EBCDIC (France), IBM420: IBM EBCDIC (Arabic), IBM423: IBM EBCDIC (Greek), IBM424: IBM EBCDIC (Hebrew), x-EBCDIC-KoreanExtended: IBM EBCDIC (Korean Extended), IBM-Thai: IBM EBCDIC (Thai), koi8-r: Cyrillic (KOI8-R), IBM871: IBM EBCDIC (Icelandic), IBM880: IBM EBCDIC (Cyrillic Russian), IBM905: IBM EBCDIC (Turkish), IBM00924: IBM Latin-1, EUC-JP: Japanese (JIS 0208-1990 and 0212-1990), x-cp20936: Chinese Simplified (GB2312-80), x-cp20949: Korean Wansung, cp1025: IBM EBCDIC (Cyrillic Serbian-Bulgarian), koi8-u: Cyrillic (KOI8-U), iso-8859-1: Western European (ISO), iso-8859-2: Central European (ISO), iso-8859-3: Latin 3 (ISO), iso-8859-4: Baltic (ISO), iso-8859-5: Cyrillic (ISO), iso-8859-6: Arabic (ISO), iso-8859-7: Greek (ISO), iso-8859-8: Hebrew (ISO-Visual), iso-8859-9: Turkish (ISO), iso-8859-13: Estonian (ISO), iso-8859-15: Latin 9 (ISO), x-Europa: Europa, iso-8859-8-i: Hebrew (ISO-Logical), iso-2022-jp: Japanese (JIS), csISO2022JP: Japanese (JIS-Allow 1 byte Kana), iso-2022-jp: Japanese (JIS-Allow 1 byte Kana - SO/SI), iso-2022-kr: Korean (ISO), x-cp50227: Chinese Simplified (ISO-2022), euc-jp: Japanese (EUC), EUC-CN: Chinese Simplified (EUC), euc-kr: Korean (EUC), hz-gb-2312: Chinese Simplified (HZ), GB18030: Chinese Simplified (GB18030), x-iscii-de: ISCII Devanagari, x-iscii-be: ISCII Bengali, x-iscii-ta: ISCII Tamil, x-iscii-te: ISCII Telugu, x-iscii-as: ISCII Assamese, x-iscii-or: ISCII Oriya, x-iscii-ka: ISCII Kannada, x-iscii-ma: ISCII Malayalam, x-iscii-gu: ISCII Gujarati, x-iscii-pa: ISCII Punjabi, utf-7: Unicode (UTF-7), utf-8: Unicode (UTF-8) | Auto - detect |
| Accept untrusted certificates | Choice | Boolean value | False |
| HTTP Authentication | Choice | Boolean value | False |
| User name | Required | Text value | — |
| Password | Required | Direct encrypted input or Text value | — |
| Trim whitespaces | Choice | Boolean value | True |

**Outputs**

| Variable | Type |
|---|---|
| WebServiceResponseHeaders | List of Text values |
| DownloadedFile | File |
| WebServiceResponse | Text value |
| StatusCode | Numeric value |

**On error:** `Invoke web service error`, `Directory doesn't exist`, `Invalid header in custom headers`.

---
