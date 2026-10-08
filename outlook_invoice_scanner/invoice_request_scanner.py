"""
Outlook Invoice Distribution Request Scanner
============================================

Scans every Outlook mailbox / PST / shared mailbox loaded in your Outlook profile
(via COM automation - pywin32) and builds an Excel report that answers:

  * Which invoices have been requested for distribution?
  * Who asked (Collections team / Project Manager / external / other), and when?
  * What type of request it was (distribute, resend, hold / do-not-distribute,
    special instructions, cancel/rebill, follow-up, dispute, ...)?
  * Which site / country / company code it belongs to (La Prairie, Charleroi, Clearwater)?
  * Has it been actioned?  - distributed by the distribution specialist (Tushar Alwani),
    already sent by a PM / someone else, put on hold, or still PENDING.

Requirements (Windows, Outlook desktop installed and open/configured):
    pip install pywin32 pandas openpyxl

Usage:
    python invoice_request_scanner.py                    # last 90 days, all mailboxes
    python invoice_request_scanner.py --days 30
    python invoice_request_scanner.py --since 2026-07-01 --output report.xlsx
    python invoice_request_scanner.py --stores "Billing NAM" "tushar"   # only matching mailboxes

NOTE: Tushar's sent mails are only visible if they are in a mailbox this profile can
read (his mailbox / a shared billing mailbox / you were in To/CC). Add the shared
mailbox to Outlook if you want full coverage.

>>> Fill in the CONFIGURATION section below before the first run. <<<
"""

import argparse
import datetime as dt
import re
import sys
from collections import defaultdict

# =============================================================================
# CONFIGURATION - adjust to your organisation
# =============================================================================

# Names or email addresses of the invoice distribution specialist(s).
# Name matching is order-insensitive, so "Alwani, Tushar" also matches.
DISTRIBUTION_SPECIALISTS = ["Tushar Alwani"]

# Known Collections team members / shared mailboxes (names or emails).
COLLECTIONS_TEAM = [
    # "jane.doe@yourcompany.com",
    # "Collections NAM",
]
# Words in job title / department / email signature that indicate Collections.
COLLECTIONS_KEYWORDS = [
    "collections", "collector", "credit control", "credit & collections",
    "accounts receivable", "cash application", "credit analyst", "recouvrement",
]

# Known Project Managers -> site.  Keys are names or emails.
PROJECT_MANAGERS = {
    # "john.smith@yourcompany.com": "Clearwater",
    # "Marie Dubois": "La Prairie",
}
# Words in job title / signature that indicate a Project Manager.
PM_KEYWORDS = ["project manager", "project management", "program manager",
               "chef de projet", "gestionnaire de projet", "project controller"]

# Your internal email domains. If left empty, derived from the Outlook profile.
INTERNAL_DOMAINS = [
    # "yourcompany.com",
]

# Sites -> country, company codes and keywords used to detect them.
# Fill in the real company codes (e.g. SAP BUKRS) for each site.
SITES = {
    "La Prairie": {"country": "Canada", "company_codes": [], "keywords": ["la prairie", "laprairie"]},
    "Charleroi":  {"country": "Belgium", "company_codes": [], "keywords": ["charleroi"]},
    "Clearwater": {"country": "USA", "company_codes": [], "keywords": ["clearwater"]},
}

# How a company code is written in emails, e.g. "Company code: 1234" / "CoCode 1234".
COMPANY_CODE_PATTERN = r"\b(?:company\s*code|co\.?\s*code|cocode|comp\.?\s*code|bukrs)\s*[:#\-]?\s*([A-Z0-9]{2,6})\b"

# Invoice number formats. The first group of each pattern is the invoice number.
INVOICE_PATTERNS = [
    # "Invoice 90012345", "Invoice No. INV-12345", "Inv#123456", "Facture 123456"
    r"\b(?:invoice|inv|facture)\s*(?:no\.?|nr\.?|number|num|#|n°)?\s*[:#\-]?\s*([A-Z]{0,4}-?\d{5,12})\b",
    r"\b(INV[-_]?\d{4,12})\b",
]
# Optional: a pattern for bare invoice numbers (no "invoice" word in front),
# e.g. SAP billing documents r"\b9\d{7}\b". Leave None to disable.
STANDALONE_INVOICE_PATTERN = None

# Only emails containing one of these words (subject/body/attachment name) are analysed.
INVOICE_HINTS = ["invoice", "inv#", "inv ", "inv-", "billing", "facture", "factura", "rebill", "credit note", "credit memo"]

# Folders that are never scanned.
SKIP_FOLDERS = {
    "deleted items", "junk email", "junk e-mail", "calendar", "contacts", "tasks", "notes",
    "journal", "sync issues", "conflicts", "local failures", "server failures",
    "conversation history", "rss feeds", "outbox", "drafts", "suggested contacts",
}

MAX_BODY_CHARS = 20000

# Request types, in PRIORITY order (first match = primary type).
# Matched against subject + the newest message in the email (quoted history removed).
REQUEST_TYPES = [
    ("Do Not Distribute / Hold", [
        r"\bdo\s*n[o']?t\s+(?:distribute|send|issue|release|submit)",
        r"\bdon'?t\s+(?:distribute|send|issue|release|submit)",
        r"\b(?:put|keep|place)\s+(?:the\s+|this\s+|it\s+)?(?:invoice\s+)?on\s+hold\b",
        r"\bhold\s+(?:off|the\s+invoice|distribution|this\s+invoice)\b",
        r"\bon\s+hold\b", r"\bstop\s+(?:the\s+)?(?:distribution|sending)",
        r"\bne\s+pas\s+(?:envoyer|distribuer|transmettre)", r"\ben\s+attente\b",
    ]),
    ("Cancel / Credit / Rebill", [
        r"\bcancel", r"\bcredit\s*(?:note|memo)", r"\brebill", r"\bre-?issue",
        r"\breverse\s+(?:the\s+)?invoice", r"\bvoid\b", r"\bannul",
    ]),
    ("Already Sent (by requester)", [
        r"\b(?:already|has\s+been|have\s+been|was)\s+(?:sent|distributed|shared|submitted|forwarded|uploaded)",
        r"\b(?:i|we)\s+(?:have\s+|already\s+)?(?:sent|forwarded|shared|submitted|uploaded)\s+(?:the\s+|this\s+|it\s+)?(?:invoice|to\s+the\s+customer|to\s+the\s+client)",
        r"\bno\s+need\s+to\s+(?:send|distribute)", r"\bdéjà\s+(?:envoy|transmis)",
    ]),
    ("Special Instructions", [
        r"\bspecial\s+instruction", r"\bplease\s+(?:also\s+)?(?:attach|include|add|copy|cc|reference|quote)\b",
        r"\b(?:upload|submit)\s+(?:it\s+|the\s+invoice\s+)?(?:to|via|through|in)\s+(?:the\s+)?(?:portal|coupa|ariba|tungsten|jaggaer)",
        r"\bportal\b", r"\b(?:coupa|ariba|tungsten|jaggaer|taulia|basware)\b",
        r"\bpo\s*(?:number|#|no\.?)?\s+(?:must|should|needs?\s+to)", r"\bsend\s+(?:it\s+)?only\s+to\b",
        r"\b(?:new|updated|correct)\s+(?:billing\s+)?(?:address|contact|email)",
        r"\b(?:attention|attn)\s*:", r"\bmust\s+(?:include|reference|show)",
    ]),
    ("Resend / Copy Request", [
        r"\bre-?send", r"\bcop(?:y|ies)\s+of\s+(?:the\s+)?invoice", r"\binvoice\s+cop(?:y|ies)",
        r"\bsend\s+(?:it\s+)?again", r"\brenvoy",
    ]),
    ("Follow-up / Status Check", [
        r"\bfollow(?:ing)?\s*-?\s*up", r"\bany\s+update", r"\bstatus\s+(?:of|on)\b", r"\breminder\b",
        r"\bhas\s+(?:this|the\s+invoice|it)\s+been\s+(?:sent|distributed|issued)", r"\brelance",
    ]),
    ("Dispute / Query", [
        r"\bdisput", r"\bincorrect\b", r"\bwrong\s+(?:amount|address|po|customer|price|rate)",
        r"\bdiscrepanc", r"\bshort[\s-]*pa(?:y|id)", r"\blitige",
    ]),
    ("Distribution Request", [
        r"\bplease\s+(?:distribute|send|issue|release|submit|forward|share)",
        r"\bkindly\s+(?:distribute|send|issue|release|submit|forward|share)",
        r"\bcan\s+you\s+(?:please\s+)?(?:distribute|send|issue|release|submit|forward)",
        r"\b(?:ready|ok|okay|good|approved)\s+(?:to|for)\s+(?:be\s+)?(?:distribut|send|sent|release|billing|invoic)",
        r"\bdistribut", r"\bmerci\s+d['e]\s*(?:envoyer|transmettre|distribuer)",
        r"\bveuillez\s+(?:envoyer|transmettre|distribuer)",
    ]),
]

# Phrases in the distribution specialist's mail that show the invoice was actually sent.
DISTRIBUTED_PHRASES = [
    r"\bplease\s+find\s+(?:attached|enclosed)", r"\battached\s+(?:is|are|please\s+find)",
    r"\b(?:invoice|it)\s+(?:has\s+been|was|is)\s+(?:sent|distributed|submitted|uploaded)",
    r"\b(?:sent|distributed|submitted|uploaded)\s+(?:to\s+the\s+)?(?:customer|client|portal)",
    r"\bdone\b", r"\bcompleted\b", r"\bveuillez\s+trouver\s+ci-joint",
]

# =============================================================================
# End of configuration
# =============================================================================

_REQUEST_TYPES_RE = [(name, [re.compile(p, re.I) for p in pats]) for name, pats in REQUEST_TYPES]
_DISTRIBUTED_RE = [re.compile(p, re.I) for p in DISTRIBUTED_PHRASES]
_INVOICE_RE = [re.compile(p, re.I) for p in INVOICE_PATTERNS]
_INVOICE_LIST_RE = re.compile(
    r"\b(?:invoices|factures)\s*(?:nos?\.?|numbers|#)?\s*[:#\-]?\s*"
    r"((?:[A-Z]{0,4}-?\d{5,12}(?:\s*(?:,|;|/|&|and|et)\s*)?){2,})", re.I)
_STANDALONE_RE = re.compile(STANDALONE_INVOICE_PATTERN) if STANDALONE_INVOICE_PATTERN else None
_COMPANY_CODE_RE = re.compile(COMPANY_CODE_PATTERN, re.I)
_QUOTE_SPLIT_RE = re.compile(
    r"^\s*(?:From:|De\s*:|Von:|Sent:\s|-{2,}\s*Original Message|_{10,}|On .{5,80} wrote:|Le .{5,80} a écrit)",
    re.I | re.M)


def _norm(s):
    return (s or "").strip().lower()


def name_matches(target, name, email=""):
    """True if `target` (a name or email) refers to the given sender/recipient."""
    t = _norm(target)
    if not t:
        return False
    if "@" in t:
        return t == _norm(email)
    tokens = re.findall(r"[a-zà-ÿ]+", t)
    cand = set(re.findall(r"[a-zà-ÿ]+", _norm(name))) | set(re.findall(r"[a-zà-ÿ]+", _norm(email).split("@")[0]))
    return bool(tokens) and all(tok in cand for tok in tokens)


def in_list(targets, name, email):
    return any(name_matches(t, name, email) for t in targets)


def newest_message(body):
    """Strip quoted reply/forward history, keep only the newest message."""
    if not body:
        return ""
    m = _QUOTE_SPLIT_RE.search(body)
    return body[:m.start()] if m else body


def extract_invoice_numbers(*texts):
    found = []
    for text in texts:
        if not text:
            continue
        for rx in _INVOICE_RE:
            found += [m.group(1) for m in rx.finditer(text)]
        for m in _INVOICE_LIST_RE.finditer(text):
            found += re.findall(r"[A-Z]{0,4}-?\d{5,12}", m.group(1), re.I)
        if _STANDALONE_RE:
            found += [m.group(0) for m in _STANDALONE_RE.finditer(text)]
    # "INV-55555", "INV_55555" and "55555" are the same invoice: key on the digits.
    seen, out = set(), []
    for f in found:
        key = re.sub(r"\D", "", f)
        if key and key not in seen:
            seen.add(key)
            out.append(key)
    return out


def classify_request(text):
    """Return (primary_type, [all matching types])."""
    types = [name for name, rxs in _REQUEST_TYPES_RE if any(rx.search(text) for rx in rxs)]
    return (types[0] if types else "General / Unclassified"), types


def matching_sentences(text, type_names, limit=2):
    """Sentences that triggered the given request types (used for instructions/holds)."""
    rxs = [rx for name, group in _REQUEST_TYPES_RE if name in type_names for rx in group]
    sentences = re.split(r"(?<=[.!?])\s+|\n+", text)
    hits = [s.strip() for s in sentences if s.strip() and any(rx.search(s) for rx in rxs)]
    return " | ".join(h[:250] for h in hits[:limit])


def looks_distributed(text):
    return any(rx.search(text) for rx in _DISTRIBUTED_RE)


def detect_site(sender_name, sender_email, gal, subject, top_text, full_text):
    """Return (site, country, company_code, how_detected)."""
    codes = [c.upper() for c in _COMPANY_CODE_RE.findall(f"{subject}\n{full_text}")]
    company_code = codes[0] if codes else ""

    for pm, site in PROJECT_MANAGERS.items():
        if name_matches(pm, sender_name, sender_email):
            return site, SITES.get(site, {}).get("country", ""), company_code, "PM directory"

    for code in codes:
        for site, info in SITES.items():
            if code in [str(c).upper() for c in info["company_codes"]]:
                return site, info["country"], code, "Company code"

    # A site named in the email beats the sender's office (a collector may cover several sites).
    sources = [
        ("Subject / latest message", f"{subject}\n{top_text}"),
        ("Outlook directory (office/city)", " ".join([gal.get("office", ""), gal.get("city", ""), gal.get("department", "")])),
        ("Email thread", full_text),
    ]
    for label, text in sources:
        low = _norm(text)
        for site, info in SITES.items():
            if any(k in low for k in info["keywords"]):
                return site, info["country"], company_code, label
    return "Unknown", "", company_code, ""


def classify_requester(name, email, gal, top_text, is_internal):
    """Return requester category."""
    if in_list(DISTRIBUTION_SPECIALISTS, name, email):
        return "Distribution Specialist"
    if in_list(COLLECTIONS_TEAM, name, email):
        return "Collections"
    if any(name_matches(pm, name, email) for pm in PROJECT_MANAGERS):
        return "Project Manager"
    profile = _norm(" ".join([gal.get("title", ""), gal.get("department", "")]))
    if any(k in profile for k in COLLECTIONS_KEYWORDS):
        return "Collections"
    if any(k in profile for k in PM_KEYWORDS):
        return "Project Manager"
    signature = _norm(top_text[-800:])
    if any(k in signature for k in COLLECTIONS_KEYWORDS):
        return "Collections"
    if any(k in signature for k in PM_KEYWORDS):
        return "Project Manager"
    if not is_internal:
        return "External / Customer"
    return "Other Internal"


# =============================================================================
# Outlook access
# =============================================================================

class OutlookReader:
    def __init__(self, internal_domains):
        import win32com.client  # noqa: imported here so the logic above is testable anywhere
        self.app = win32com.client.Dispatch("Outlook.Application")
        self.ns = self.app.GetNamespace("MAPI")
        self._smtp_cache = {}
        self._gal_cache = {}
        self.internal_domains = {d.lower() for d in internal_domains}
        if not self.internal_domains:
            try:
                me = self.smtp_of(self.ns.CurrentUser.AddressEntry)
                if "@" in me:
                    self.internal_domains.add(me.split("@")[1].lower())
            except Exception:
                pass

    # --- address helpers -----------------------------------------------------
    def smtp_of(self, ae):
        if ae is None:
            return ""
        try:
            key = ae.Address
        except Exception:
            return ""
        if key in self._smtp_cache:
            return self._smtp_cache[key]
        smtp = key or ""
        try:
            if ae.Type == "EX":
                eu = ae.GetExchangeUser()
                if eu is not None:
                    smtp = eu.PrimarySmtpAddress
                else:
                    dl = ae.GetExchangeDistributionList()
                    if dl is not None:
                        smtp = dl.PrimarySmtpAddress
        except Exception:
            pass
        self._smtp_cache[key] = smtp
        return smtp

    def gal_details(self, ae):
        info = {"title": "", "department": "", "office": "", "city": "", "company": ""}
        if ae is None:
            return info
        try:
            key = ae.Address
        except Exception:
            return info
        if key in self._gal_cache:
            return self._gal_cache[key]
        try:
            eu = ae.GetExchangeUser()
            if eu is not None:
                info = {
                    "title": eu.JobTitle or "", "department": eu.Department or "",
                    "office": eu.OfficeLocation or "", "city": eu.City or "",
                    "company": eu.CompanyName or "",
                }
        except Exception:
            pass
        self._gal_cache[key] = info
        return info

    def is_internal(self, address):
        a = _norm(address)
        if not a or a.startswith("/o="):
            return True
        if "@" not in a:
            return True
        return a.split("@")[1] in self.internal_domains

    # --- folder walking ------------------------------------------------------
    def stores(self, name_filters=None):
        for store in self.ns.Stores:
            try:
                name = store.DisplayName
            except Exception:
                continue
            if name_filters and not any(f.lower() in name.lower() for f in name_filters):
                continue
            yield name, store

    def walk_folders(self, folder, path=""):
        try:
            name = folder.Name
        except Exception:
            return
        if _norm(name) in SKIP_FOLDERS:
            return
        full = f"{path}/{name}" if path else name
        yield full, folder
        try:
            for sub in folder.Folders:
                yield from self.walk_folders(sub, full)
        except Exception:
            pass

    @staticmethod
    def mail_items(folder, since):
        try:
            if folder.DefaultItemType != 0:  # 0 = olMailItem
                return
            items = folder.Items
        except Exception:
            return
        try:
            items = items.Restrict("[ReceivedTime] >= '" + since.strftime("%m/%d/%Y %I:%M %p") + "'")
        except Exception:
            pass  # fall back to manual date check below
        for item in items:
            try:
                if item.Class != 43:  # 43 = olMail
                    continue
                received = to_naive(item.ReceivedTime)
                if received < since:
                    continue
                yield item, received
            except Exception:
                continue


def to_naive(t):
    return dt.datetime(t.year, t.month, t.day, t.hour, t.minute, t.second)


# =============================================================================
# Scan
# =============================================================================

def scan(reader, since, store_filters):
    records = []
    for store_name, store in reader.stores(store_filters):
        print(f"\n[Mailbox] {store_name}")
        try:
            root = store.GetRootFolder()
        except Exception as e:
            print(f"  ! cannot open: {e}")
            continue
        for folder_path, folder in reader.walk_folders(root):
            count = 0
            for item, received in reader.mail_items(folder, since):
                rec = analyse_item(reader, item, received, store_name, folder_path)
                if rec:
                    records.append(rec)
                    count += 1
            if count:
                print(f"  {folder_path}: {count} invoice-related emails")
    return records


def analyse_item(reader, item, received, store_name, folder_path):
    try:
        subject = item.Subject or ""
        body = (item.Body or "")[:MAX_BODY_CHARS]
    except Exception:
        return None
    attachments = []
    try:
        for a in item.Attachments:
            attachments.append(a.FileName)
    except Exception:
        pass
    att_text = " ".join(attachments)

    haystack = f"{subject}\n{body}\n{att_text}".lower()
    if not any(h in haystack for h in INVOICE_HINTS):
        return None

    top = newest_message(body)
    try:
        sender_ae = item.Sender
    except Exception:
        sender_ae = None
    sender_name = getattr(item, "SenderName", "") or ""
    sender_email = reader.smtp_of(sender_ae) or (getattr(item, "SenderEmailAddress", "") or "")
    gal = reader.gal_details(sender_ae)
    sender_internal = reader.is_internal(sender_email)

    to, cc, external_recipients = [], [], []
    try:
        for r in item.Recipients:
            addr = reader.smtp_of(r.AddressEntry) or r.Address or r.Name
            (to if r.Type == 1 else cc).append(addr)
            if not reader.is_internal(addr):
                external_recipients.append(addr)
    except Exception:
        pass

    # Invoice numbers: subject + newest message + attachment names first; fall back to whole thread.
    invoices = extract_invoice_numbers(subject, top, att_text) or extract_invoice_numbers(body)

    primary, all_types = classify_request(f"{subject}\n{top}")
    category = classify_requester(sender_name, sender_email, gal, top, sender_internal)
    site, country, company_code, site_source = detect_site(sender_name, sender_email, gal, subject, top, body)

    has_invoice_attachment = any(re.search(r"\.(pdf|xml|tif|tiff)$", a, re.I) for a in attachments)
    sent_to_customer = sender_internal and bool(external_recipients) and has_invoice_attachment

    try:
        conversation = item.ConversationID or ""
    except Exception:
        conversation = ""

    return {
        "Received": received,
        "Mailbox": store_name,
        "Folder": folder_path,
        "Subject": subject,
        "From": sender_name,
        "From Email": sender_email,
        "Requester Category": category,
        "Job Title": gal.get("title", ""),
        "Department": gal.get("department", ""),
        "Site": site,
        "Country": country,
        "Company Code": company_code,
        "Site Detected From": site_source,
        "Request Type": primary,
        "All Request Types": ", ".join(all_types),
        "Instruction Text": matching_sentences(top, [
            "Do Not Distribute / Hold", "Special Instructions", "Already Sent (by requester)",
            "Cancel / Credit / Rebill"]),
        "Invoice Numbers": ", ".join(invoices),
        "Attachments": att_text,
        "To": "; ".join(to),
        "CC": "; ".join(cc),
        "External Recipients": "; ".join(external_recipients),
        "Sent To Customer With Attachment": sent_to_customer,
        "From Specialist": category == "Distribution Specialist",
        "Specialist Says Distributed": category == "Distribution Specialist" and (
            looks_distributed(top) or sent_to_customer),
        "Snippet": re.sub(r"\s+", " ", top)[:400],
        "_invoices": invoices,
        "_conversation": conversation,
        "_all_types": all_types,
    }


# =============================================================================
# Status per invoice
# =============================================================================

def build_status(records):
    """Group emails per invoice number (or per conversation when no number) and decide status."""
    groups = defaultdict(list)
    conv_to_keys = defaultdict(set)
    for r in records:
        keys = r["_invoices"] or [f"(no invoice #) {r['Subject'][:60]}"]
        for k in keys:
            groups[k].append(r)
            if r["_conversation"]:
                conv_to_keys[r["_conversation"]].add(k)

    # Replies in the same conversation without the invoice number still count as evidence.
    for r in records:
        if not r["_invoices"] and r["_conversation"]:
            for k in conv_to_keys.get(r["_conversation"], ()):
                if r not in groups[k]:
                    groups[k].append(r)

    rows = []
    for key, emails in groups.items():
        emails.sort(key=lambda e: e["Received"])
        requests = [e for e in emails if e["Requester Category"] != "Distribution Specialist"
                    and e["Request Type"] != "General / Unclassified"]
        anchor = requests[0] if requests else emails[0]
        first_req = anchor["Received"]

        def after(e):
            return e["Received"] >= first_req

        specialist_done = [e for e in emails if e["Specialist Says Distributed"] and after(e)]
        specialist_any = [e for e in emails if e["From Specialist"] and after(e)]
        others_sent = [e for e in emails if not e["From Specialist"] and (
            e["Sent To Customer With Attachment"] or "Already Sent (by requester)" in e["_all_types"])]
        holds = [e for e in emails if "Do Not Distribute / Hold" in e["_all_types"]]
        cancels = [e for e in emails if "Cancel / Credit / Rebill" in e["_all_types"]]
        dist_requests = [e for e in requests if e["Request Type"] in (
            "Distribution Request", "Resend / Copy Request", "Special Instructions", "Follow-up / Status Check")]

        last_hold = holds[-1]["Received"] if holds else None
        last_dist_req = dist_requests[-1]["Received"] if dist_requests else None
        last_specialist_done = specialist_done[-1]["Received"] if specialist_done else None

        actioned_by, actioned_on = "", None
        if last_hold and (not last_dist_req or last_hold >= last_dist_req) and (
                not last_specialist_done or last_hold >= last_specialist_done):
            status = "ON HOLD - do not distribute"
            actioned_by, actioned_on = holds[-1]["From"], last_hold
        elif specialist_done:
            # A newer request after the last distribution (e.g. resend) re-opens it.
            if last_dist_req and last_dist_req > last_specialist_done:
                status = "PENDING - new request after last distribution"
            else:
                status = "DISTRIBUTED by specialist"
            actioned_by, actioned_on = specialist_done[-1]["From"], last_specialist_done
        elif others_sent:
            status = "SENT by someone else"
            actioned_by, actioned_on = others_sent[-1]["From"], others_sent[-1]["Received"]
        elif cancels:
            status = "CANCEL / REBILL requested - review"
            actioned_by, actioned_on = cancels[-1]["From"], cancels[-1]["Received"]
        elif specialist_any:
            status = "IN PROGRESS - specialist replied (verify)"
            actioned_by, actioned_on = specialist_any[-1]["From"], specialist_any[-1]["Received"]
        elif requests:
            status = "PENDING"
        else:
            status = "NO REQUEST FOUND (info only)"

        def uniq(values):
            return ", ".join(dict.fromkeys(v for v in values if v))

        site_rec = next((e for e in requests if e["Site"] != "Unknown"),
                        next((e for e in emails if e["Site"] != "Unknown"), anchor))
        instructions = " || ".join(dict.fromkeys(e["Instruction Text"] for e in emails if e["Instruction Text"]))

        rows.append({
            "Invoice #": key,
            "Status": status,
            "Site": site_rec["Site"],
            "Country": site_rec["Country"],
            "Company Code": uniq(e["Company Code"] for e in emails),
            "First Request Date": first_req,
            "Requested By": anchor["From"],
            "Requester Category": anchor["Requester Category"],
            "Primary Request Type": anchor["Request Type"],
            "All Request Types": uniq(t for e in requests for t in e["_all_types"]),
            "All Requesters": uniq(f"{e['From']} ({e['Requester Category']})" for e in requests),
            "Latest Request Date": requests[-1]["Received"] if requests else None,
            "Special Instructions / Hold Notes": instructions[:1000],
            "Actioned By": actioned_by,
            "Actioned On": actioned_on,
            "Days Open": (dt.datetime.now() - first_req).days if status.startswith("PENDING") else None,
            "Emails In Thread": len(emails),
            "Subjects": uniq(e["Subject"] for e in emails)[:500],
            "Mailboxes": uniq(e["Mailbox"] for e in emails),
        })
    return rows


# =============================================================================
# Excel output
# =============================================================================

def write_report(records, status_rows, path):
    import pandas as pd

    detail_cols = [c for c in records[0].keys() if not c.startswith("_")] if records else []
    detail = pd.DataFrame([{c: r[c] for c in detail_cols} for r in records])
    if not detail.empty:
        detail = detail.sort_values("Received", ascending=False)

    status = pd.DataFrame(status_rows)
    if not status.empty:
        order = {"PENDING": 0, "ON HOLD": 1, "CANCEL": 2, "IN PROGRESS": 3, "SENT": 4, "DISTRIBUTED": 5, "NO REQUEST": 6}
        status["_o"] = status["Status"].map(lambda s: next((v for k, v in order.items() if s.startswith(k)), 9))
        status = status.sort_values(["_o", "First Request Date"]).drop(columns="_o")
        pending = status[status["Status"].str.startswith(("PENDING", "IN PROGRESS", "CANCEL"))]
    else:
        pending = status

    with pd.ExcelWriter(path, engine="openpyxl") as xw:
        status.to_excel(xw, sheet_name="Invoice Status", index=False)
        pending.to_excel(xw, sheet_name="Pending - Action", index=False)
        if not detail.empty:
            requests = detail[detail["Requester Category"] != "Distribution Specialist"]
            pd.crosstab(requests["Request Type"], requests["Requester Category"], margins=True,
                        margins_name="Total").to_excel(xw, sheet_name="Summary", startrow=1)
            row = len(requests["Request Type"].unique()) + 6
            pd.crosstab(requests["Site"], requests["Requester Category"], margins=True,
                        margins_name="Total").to_excel(xw, sheet_name="Summary", startrow=row)
            row += len(requests["Site"].unique()) + 6
            if not status.empty:
                pd.crosstab(status["Status"], status["Site"], margins=True,
                            margins_name="Total").to_excel(xw, sheet_name="Summary", startrow=row)
            ws = xw.sheets["Summary"]
            ws.cell(row=1, column=1, value="Requests by type x requester category")
        detail.to_excel(xw, sheet_name="All Emails", index=False)

        for ws in xw.book.worksheets:
            if ws.title != "Summary":
                ws.freeze_panes = "A2"
                ws.auto_filter.ref = ws.dimensions
            for col in ws.columns:
                width = max((len(str(c.value)) for c in col[:200] if c.value is not None), default=8)
                ws.column_dimensions[col[0].column_letter].width = min(max(width + 2, 10), 60)


# =============================================================================
# Main
# =============================================================================

def main():
    ap = argparse.ArgumentParser(description="Scan Outlook for invoice distribution requests.")
    ap.add_argument("--days", type=int, default=90, help="look back this many days (default 90)")
    ap.add_argument("--since", help="start date YYYY-MM-DD (overrides --days)")
    ap.add_argument("--stores", nargs="*", help="only scan mailboxes whose name contains one of these")
    ap.add_argument("--output", help="output .xlsx path")
    args = ap.parse_args()

    if sys.platform != "win32":
        sys.exit("This script needs Windows with Outlook desktop (COM automation).")
    try:
        import pythoncom
        pythoncom.CoInitialize()
    except ImportError:
        sys.exit("pywin32 is required:  pip install pywin32 pandas openpyxl")

    since = dt.datetime.strptime(args.since, "%Y-%m-%d") if args.since \
        else dt.datetime.now() - dt.timedelta(days=args.days)
    output = args.output or f"invoice_distribution_report_{dt.datetime.now():%Y%m%d_%H%M}.xlsx"

    reader = OutlookReader(INTERNAL_DOMAINS)
    print(f"Scanning emails since {since:%Y-%m-%d}. Internal domains: {sorted(reader.internal_domains) or 'unknown'}")
    records = scan(reader, since, args.stores)
    if not records:
        print("\nNo invoice-related emails found.")
        return

    status_rows = build_status(records)
    write_report(records, status_rows, output)

    counts = defaultdict(int)
    for r in status_rows:
        counts[r["Status"]] += 1
    print(f"\n{len(records)} invoice-related emails, {len(status_rows)} invoices/threads")
    for s, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"  {n:5d}  {s}")
    print(f"\nReport written to: {output}")


if __name__ == "__main__":
    main()
