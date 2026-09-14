# HTTP — how each function works

Native Actions pane module **HTTP**.

3 items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.

### Download from web

- **Id:** `web/download-from-web`
- **Kind:** native-action
- **Purpose:** Downloads from web.

**Use case.** In a REST or SOAP API the website already offers, drop **Download from web** on the canvas. Downloads from web.

**Demonstration.**

```text
**Download from web**
- URL: `https://api.contoso.example/v1/invoices`
- Method: `GET`
- Post parameters: `%InvoiceTable%`
- Save response: `Get text into variable (for web pages)`
- File name: `C:\RPA\Invoices\INV-1042.pdf`
- Destination folder: `C:\RPA\Invoices`
- Destination file path: `C:\RPA\Invoices\INV-1042.pdf`
- Connection timeout: `30`
- … 8 more parameter(s) in the action modal
Produces:
- `%DownloadedFile%` (File)
- `%WebPageText%` (Text value)
```

**Analogy.** One tool in that kit: phoning a switchboard instead of walking into the shop.

**In combination.** Invoke web service or Download from web; convert files to binary when attaching.

### Invoke SOAP web service

- **Id:** `web/invoke-soap-web-service`
- **Kind:** native-action
- **Purpose:** Calls SOAP web service.

**Use case.** In a REST or SOAP API the website already offers, drop **Invoke SOAP web service** on the canvas. Calls SOAP web service.

**Demonstration.**

```text
**Invoke SOAP web service**
- Endpoint: `https://api.contoso.example/v1/invoices`
- Custom headers: `INV-1042`
- Request body: `Processed by desktop flow Close-P9`
- Connection timeout: `30`
- Follow redirection: `True`
- Clear cookies: `False`
- Fail on error status: `False`
- User agent: `Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.21) Gecko/20100312 Firefox/3.6`
- … 7 more parameter(s) in the action modal
Produces:
- `%SoapServiceResponseHeaders%` (List of Text values)
- `%SoapServiceResponse%` (Text value)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: phoning a switchboard instead of walking into the shop.

**In combination.** Invoke web service or Download from web; convert files to binary when attaching.

### Invoke web service

- **Id:** `web/invoke-web-service`
- **Kind:** native-action
- **Purpose:** Calls web service.

**Use case.** Call a REST API instead of clicking the website, when the API exists.

**Demonstration.**

```text
**Invoke web service**
- URL: `https://api.contoso.example/v1/invoices`
- Method: `GET`
- Accept: `application/xml`
- Custom headers: `INV-1042`
- Upload attachments: `False`
- Content type: `application/xml`
- Request body: `Processed by desktop flow Close-P9`
- Attachments: `No attachments selected`
- … 17 more parameter(s) in the action modal
Produces:
- `%WebServiceResponseHeaders%` (List of Text values)
- `%DownloadedFile%` (File)
- `%WebServiceResponse%` (Text value)
- `%StatusCode%` (Numeric value)
```

**Analogy.** One tool in that kit: phoning a switchboard instead of walking into the shop.

**In combination.** Invoke web service or Download from web; convert files to binary when attaching.
