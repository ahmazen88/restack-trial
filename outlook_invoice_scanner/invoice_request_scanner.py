"""
Outlook Invoice Distribution Request Scanner
============================================

Scans every Outlook mailbox / PST / shared mailbox loaded in your Outlook profile
(via COM automation - pywin32) and builds an Excel report that answers:

  * Which invoices have been requested for distribution?
  * Who asked (Collections team / Project Manager / external / other), and when?
  * What type of request it was (distribute, resend, hold / do-not-distribute,
    release hold, special instructions, cancel/rebill, follow-up, dispute, ...)?
  * Which site / country / company code it belongs to (La Prairie, Charleroi, Clearwater)?
  * Has it been actioned - by ANYONE, not only the distribution specialist:
      - sent to the customer (outgoing email with the invoice attached),
      - someone wrote "sent / distributed / uploaded to Coupa / done / actioned ...",
      - the customer or portal confirmed receipt,
      - someone said "do not distribute / hold / wait until ..." (and whether the hold
        was later released),
    or is it still PENDING?

How "actioned" is detected
--------------------------
Every email is checked against the keyword/alias lists in ACTION_KEYWORDS (English and
French, easy to extend). Matching is sentence-based and ignores:
  * negations      - "has NOT been sent", "please don't hold"
  * questions      - "has it been sent?"  (counted as a follow-up instead)
  * future tense   - "will be sent tomorrow"
  * signatures     - "Sent from my iPhone"
Every keyword hit is listed (with the sentence) in the "Keyword Hits" sheet, so each
decision can be checked by a person.

Requirements (Windows, Outlook desktop installed and configured):
    pip install pywin32 pandas openpyxl

Usage:
    python invoice_request_scanner.py                    # last 90 days, all mailboxes
    python invoice_request_scanner.py --days 30
    python invoice_request_scanner.py --since 2026-07-01 --output report.xlsx
    python invoice_request_scanner.py --stores "Billing NAM" "tushar"   # only matching mailboxes

NOTE: an email is only seen if it is in a mailbox this profile can read (your mailbox,
Tushar's / a shared billing mailbox added to Outlook, or emails where you were in To/CC).

>>> Fill in the CONFIGURATION section below before the first run. <<<
"""

import argparse
import datetime as dt
import re
import sys
import time
import unicodedata
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

# Sender domains of e-invoicing portals / systems whose emails confirm a submission.
PORTAL_DOMAINS = ["coupahost.com", "coupa.com", "ariba.com", "tungsten-network.com",
                  "jaggaer.com", "taulia.com", "basware.com", "sap.com"]

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
    r"\b(?:invoice|inv|facture|factura|bill)\s*(?:no\.?|nr\.?|number|num|#|n°|no°)?\s*[:#\-]?\s*([A-Z]{0,4}-?\d{5,12})\b",
    r"\b(INV[-_]?\d{4,12})\b",
]
# Optional: a pattern for bare invoice numbers (no "invoice" word in front),
# e.g. SAP billing documents r"\b9\d{7}\b". Leave None to disable.
STANDALONE_INVOICE_PATTERN = None

# Emails containing one of these words (subject/body/attachment name) are treated as
# invoice related. Emails WITHOUT them are still kept when they contain an action
# keyword and belong to the same conversation as an invoice email (e.g. a reply "Done").
INVOICE_HINTS = ["invoice", "inv#", "inv ", "inv-", "billing", "facture", "factura",
                 "rebill", "credit note", "credit memo", "distribution"]

# Folders that are never scanned.
SKIP_FOLDERS = {
    "deleted items", "junk email", "junk e-mail", "calendar", "contacts", "tasks", "notes",
    "journal", "sync issues", "conflicts", "local failures", "server failures",
    "conversation history", "rss feeds", "outbox", "drafts", "suggested contacts",
    "elements supprimes", "courrier indesirable", "brouillons",
}

MAX_BODY_CHARS = 20000

# -----------------------------------------------------------------------------
# ACTION KEYWORDS / ALIASES
# Plain phrases, case and accent insensitive.  Write them in lower case.
#   *    = any word ending          ("distribut*" -> distribute, distributed, distribution)
#   '    = optional apostrophe      ("don't" also matches "dont" and "don t")
#   re:  = prefix for a raw regular expression
# Add your team's own wording to the lists - no code changes needed.
# -----------------------------------------------------------------------------
ACTION_KEYWORDS = {
    # Someone asks for the invoice to be sent.
    "DISTRIBUTION_REQUEST": [
        "please distribute", "pls distribute", "plz distribute", "kindly distribute",
        "please send", "pls send", "kindly send", "please forward", "kindly forward",
        "please submit", "kindly submit", "please issue", "please release", "please share",
        "please email", "please e-mail", "please upload", "please process", "please invoice",
        "can you distribute", "could you distribute", "can you please distribute",
        "can you send", "could you send", "can you please send", "could you please send",
        "can you submit", "could you submit", "would you send", "can you forward",
        "ready to distribute", "ready for distribution", "ready to be sent", "ready to send",
        "ready to be distributed", "ok to send", "okay to send", "ok to distribute",
        "okay to distribute", "good to send", "good to distribute", "approved to send",
        "approved for distribution", "approved for billing", "approved to invoice",
        "go ahead and send", "go ahead and distribute", "proceed with distribution",
        "proceed with sending", "send to customer", "send to the customer", "send to client",
        "send to the client", "send it to the customer", "send it to the client",
        "distribute to customer", "distribute to the customer", "distribution request",
        "request for distribution", "for distribution", "to be distributed", "needs to be sent",
        "need to be sent", "needs to go out", "need it sent", "invoice distribution",
        "merci d'envoyer", "merci de transmettre", "merci de distribuer", "merci de faire parvenir",
        "veuillez envoyer", "veuillez transmettre", "veuillez distribuer",
        "pouvez-vous envoyer", "pourriez-vous envoyer", "pouvez vous envoyer", "a envoyer au client",
        "por favor enviar", "favor de enviar",
    ],
    # Resend / copy / customer did not get it.
    "RESEND": [
        "resend", "re-send", "re send", "send again", "send it again", "send them again",
        "resubmit", "re-submit", "re-upload", "reupload", "send a copy", "send me a copy",
        "copy of the invoice", "copy of invoice", "copies of the invoice*", "invoice copy",
        "invoice copies", "duplicate copy", "did not receive", "didn't receive",
        "never received", "not received", "haven't received", "have not received",
        "can't find the invoice", "cannot find the invoice", "not in the portal",
        "renvoyer", "renvoi", "copie de la facture", "pas recu", "jamais recu",
    ],
    # Do not distribute / hold / wait.
    "HOLD": [
        "do not distribute", "don't distribute", "do not send", "don't send", "do not issue",
        "don't issue", "do not release", "don't release", "do not submit", "don't submit",
        "do not forward", "don't forward", "do not upload", "don't upload", "do not invoice",
        "don't invoice", "do not bill", "don't bill", "not to be sent", "not to be distributed",
        "should not be sent", "shouldn't be sent", "must not be sent", "should not be distributed",
        "hold", "on hold", "put on hold", "hold off", "hold the invoice", "hold distribution",
        "keep on hold", "please hold", "withhold", "park the invoice", "park it", "parked",
        "pause", "stop distribution", "stop sending", "stop the invoice", "billing block",
        "block the invoice", "blocked invoice", "invoice is blocked", "wait until",
        "wait before sending", "wait for my confirmation", "wait for approval",
        "wait for my go", "wait for the po", "until further notice", "until further instruction*",
        "until i confirm", "until we confirm", "until approved", "until the po",
        "not ready to send", "not ready for distribution", "not yet ready",
        "pending approval", "pending customer approval", "pending po", "awaiting po",
        "awaiting approval", "ne pas envoyer", "ne pas distribuer", "ne pas transmettre",
        "ne pas emettre", "ne pas facturer", "en attente", "mettre en attente", "bloquer",
        "bloquee", "suspendre", "suspendu", "retenir", "attendre avant", "no enviar",
    ],
    # A hold is lifted.
    "RELEASE": [
        "release the hold", "remove the hold", "lift the hold", "hold lifted", "hold removed",
        "hold released", "hold is released", "hold has been released", "off hold",
        "take it off hold", "no longer on hold", "no need to hold", "no longer needs to be held",
        "you can send now", "can be sent now", "can now be sent", "can now be distributed",
        "ok to send now", "okay to send now", "good to send now", "you may proceed",
        "please proceed", "go ahead", "approved now", "po received", "po has been received",
        "vous pouvez envoyer", "peut etre envoyee", "peut etre envoye", "on peut envoyer",
        "debloquer", "debloquee",
    ],
    # Someone states it was sent / distributed.
    "SENT": [
        "sent", "has been sent", "have sent", "was sent", "were sent", "already sent",
        "sent out", "sent to the customer", "sent to customer", "sent to client",
        "distributed", "has been distributed", "already distributed", "emailed", "e-mailed",
        "mailed", "submitted", "uploaded", "posted to the portal", "posted in the portal",
        "shared with the customer", "shared with the client", "delivered", "transmitted",
        "dispatched", "issued to the customer", "released to the customer", "went out",
        "gone out", "has gone out", "sent via edi", "sent through the portal",
        "uploaded to coupa", "uploaded to ariba", "submitted in coupa", "submitted on ariba",
        "submitted via the portal", "submitted through the portal",
        "envoye", "envoyee", "envoyees", "transmis", "transmise", "deja envoye",
        "depose sur le portail", "deposee sur le portail", "deposees sur le portail",
        "televerse", "televersee", "enviado", "enviada",
    ],
    # "Here is the invoice" - counts as SENT only when the email goes to an external recipient.
    "SENT_ATTACHED": [
        "please find attached", "please find enclosed", "attached please find", "find attached",
        "attached is the invoice", "attached are the invoices", "attached invoice",
        "enclosed invoice", "enclosed please find", "veuillez trouver ci-joint",
        "ci-joint la facture", "vous trouverez ci-joint", "adjunto factura",
    ],
    # Generic completion - resolves the latest open request in the thread (reply emails only).
    "DONE": [
        "done", "completed", "complete", "actioned", "has been actioned", "action taken",
        "taken action", "took action", "taken care of", "took care of", "handled",
        "has been handled", "processed", "has been processed", "all set", "resolved",
        "noted and actioned", "noted and done", "c'est fait", "fait", "traite", "traitee",
        "effectue", "hecho", "listo",
    ],
    "CANCEL": [
        "cancel*", "credit note", "credit memo", "rebill*", "re-bill*", "reissue", "re-issue",
        "reverse the invoice", "reversal", "void", "voided", "annul*", "note de credit",
        "refactur*",
    ],
    "SPECIAL_INSTRUCTION": [
        "special instruction*", "please also attach", "please attach", "please include",
        "please add", "please copy", "please cc", "include the po", "reference the po",
        "quote the po", "po number must", "po must", "must include", "must reference",
        "must show", "re:\\b(?:attention|attn)\\s*:", "portal", "coupa", "ariba", "tungsten",
        "jaggaer", "taulia", "basware", "sap business network", "edi", "send only to",
        "only send to", "send to the following", "new address", "new contact", "new email",
        "updated address", "updated contact", "address change", "change of address",
        "billing address", "bill to", "timesheet*", "proof of delivery", "pod", "backup",
        "supporting document*", "lien waiver*", "joindre", "ajouter le bon de commande",
        "adresse de facturation",
    ],
    "FOLLOW_UP": [
        "follow up", "following up", "follow-up", "any update*", "any news", "status of",
        "status on", "status update", "reminder", "gentle reminder", "friendly reminder",
        "chasing", "has this been sent", "has it been sent", "was it sent",
        "has this been distributed", "has it been distributed", "did you send", "when will",
        "relance", "rappel", "des nouvelles",
    ],
    "DISPUTE": [
        "disput*", "incorrect", "wrong amount", "wrong address", "wrong po", "wrong customer",
        "wrong price", "wrong rate", "discrepanc*", "short pay*", "short-pay*", "overbill*",
        "overcharg*", "duplicate billing", "billed twice", "litige", "contest*", "erreur",
    ],
    # Customer / portal confirms it arrived (only counted for external or portal senders).
    "RECEIPT": [
        "received", "well received", "we have received", "we received", "receipt confirmed",
        "thank you for the invoice", "thanks for the invoice", "invoice has been received",
        "successfully submitted", "successfully received", "has been accepted",
        "invoice accepted", "approved for payment", "bien recu", "bonne reception",
    ],
}

# Display names and priority (first = most important) for the primary request type.
SIGNAL_LABELS = {
    "HOLD": "Do Not Distribute / Hold",
    "RELEASE": "Release Hold / OK to Send",
    "CANCEL": "Cancel / Credit / Rebill",
    "SENT": "Already Sent",
    "SENT_ATTACHED": "Invoice Attached",
    "SPECIAL_INSTRUCTION": "Special Instructions",
    "RESEND": "Resend / Copy Request",
    "DISPUTE": "Dispute / Query",
    "FOLLOW_UP": "Follow-up / Status Check",
    "DISTRIBUTION_REQUEST": "Distribution Request",
    "DONE": "Done / Actioned",
    "RECEIPT": "Receipt Confirmed",
}
SIGNAL_PRIORITY = list(SIGNAL_LABELS)

# =============================================================================
# End of configuration
# =============================================================================


def fold(text):
    """Lower-case, strip accents, normalise apostrophes/spaces (so 'reçu' == 'recu')."""
    text = unicodedata.normalize("NFKD", text or "")
    text = "".join(c for c in text if not unicodedata.combining(c))
    return text.replace("’", "'").replace("‘", "'").replace(" ", " ").lower()


def phrase_to_regex(phrase):
    if phrase.startswith("re:"):
        return phrase[3:]
    p = fold(phrase).strip()
    out = []
    for part in re.split(r"(\s+|\*|')", p):
        if not part:
            continue
        if part.isspace():
            out.append(r"[\s\-]+")
        elif part == "*":
            out.append(r"\w*")
        elif part == "'":
            out.append(r"(?:'|\s)?")
        else:
            out.append(re.escape(part))
    return r"(?<!\w)" + "".join(out) + (r"" if p.endswith("*") else r"(?!\w)")


_SIGNAL_RE = {
    sig: re.compile("|".join(f"(?:{phrase_to_regex(p)})" for p in phrases), re.I)
    for sig, phrases in ACTION_KEYWORDS.items()
}
_INVOICE_RE = [re.compile(p, re.I) for p in INVOICE_PATTERNS]
_INVOICE_LIST_RE = re.compile(
    r"\b(?:invoices|factures|inv)\s*(?:nos?\.?|numbers|#)?\s*[:#\-]?\s*"
    r"((?:[A-Z]{0,4}-?\d{5,12}(?:\s*(?:,|;|/|&|\band\b|\bet\b)\s*)?){2,})", re.I)
_STANDALONE_RE = re.compile(STANDALONE_INVOICE_PATTERN) if STANDALONE_INVOICE_PATTERN else None
_COMPANY_CODE_RE = re.compile(COMPANY_CODE_PATTERN, re.I)
_QUOTE_SPLIT_RE = re.compile(
    r"^\s*(?:From:|De\s*:|Von:|Envoy[eé]\s*:|Sent:\s|-{2,}\s*Original Message|_{10,}|"
    r"On .{5,120} wrote:|Le .{5,120} a [eé]crit)", re.I | re.M)
_SIGNATURE_LINE_RE = re.compile(
    r"^\s*(?:sent from my|envoy[eé] de mon|get outlook for|sent from outlook|sent from mail for).*$",
    re.I | re.M)
_REPLY_SUBJECT_RE = re.compile(r"^\s*(?:re|aw|tr|ref|rep|antw|sv)\s*:", re.I)
_FWD_PREFIX_RE = re.compile(r"^\s*(?:(?:re|fw|fwd|aw|tr|ref|rep|wg|antw|sv)\s*:\s*)+", re.I)

# Negation directly before a keyword (same clause): "has NOT been sent", "please don't hold".
_NEGATION_RE = re.compile(
    r"(?:\bnot\b|n't\b|n t\b|\bnever\b|\bno\b(?!\.|\s*[\d#:])|\byet to\b|\bwithout\b|\bpas\b|\bjamais\b|\bnon\b|\bne\b|\bnor\b)"
    r"(?:\s+\w+){0,3}\s*$", re.I)
# Future / intention: "will be sent tomorrow", "going to distribute".
_FUTURE_RE = re.compile(
    r"(?:\bwill\b|'ll\b|\bgoing to\b|\bgonna\b|\bto be\b|\bshall\b|\bbeing\b|\bplan to\b|"
    r"\babout to\b|\bonce\b|\bwhen\b|\bafter\b|\bas soon as\b|\bif\b|\bwhether\b|\buntil\b|\bbefore\b|"
    r"\bmake sure\b|\bensure\b|\bconfirm\b|\bsera\b|\bva\b|\bvais\b|\ballons\b|\bquand\b|\bdes que\b|\bsi\b)"
    r"(?:\s+\w+){0,3}\s*$", re.I)
# Phrases that contain a negation word but are not negations.
_NOT_NEGATION_RE = re.compile(
    r"\b(?:no problem|no worries|no issues?|not a problem|no rush|pas de (?:souci|probleme))\b", re.I)
_QUESTION_START_RE = re.compile(
    r"^\s*(?:(?:has|have|had|was|were|did|is|are|could|can|would|will|do|does|should|shall)\s+"
    r"(?:you|we|i|it|this|that|they|he|she|the|these|those|anyone|someone)\b|"
    r"(?:when|why|what|which|who)\b|est-ce|avez-vous|as-tu|a-t-il)", re.I)
_REQUEST_LIKE_RE = re.compile(
    r"\b(?:can|could|would|will)\s+you\b|\bplease\b|\bpls\b|\bkindly\b|\bpourriez\b|\bpouvez\b|\bmerci de\b",
    re.I)

# Signals that describe something that HAPPENED - questions/negations/future don't count.
_STATEMENT_SIGNALS = {"SENT", "SENT_ATTACHED", "DONE", "RECEIPT", "RELEASE"}
# Signals that are requests - a request-like question still counts ("can you hold it?").
_REQUEST_SIGNALS = {"HOLD", "CANCEL", "RESEND", "DISTRIBUTION_REQUEST", "SPECIAL_INSTRUCTION"}


def _norm(s):
    return (s or "").strip().lower()


def name_matches(target, name, email=""):
    """True if `target` (a name or email) refers to the given sender/recipient."""
    t = fold(target).strip()
    if not t:
        return False
    if "@" in t:
        return t == fold(email).strip()
    tokens = re.findall(r"[a-z]+", t)
    cand = set(re.findall(r"[a-z]+", fold(name))) | set(re.findall(r"[a-z]+", fold(email).split("@")[0]))
    return bool(tokens) and all(tok in cand for tok in tokens)


def in_list(targets, name, email):
    return any(name_matches(t, name, email) for t in targets)


def newest_message(body):
    """Strip quoted reply/forward history and mobile signatures, keep only the newest message."""
    if not body:
        return ""
    m = _QUOTE_SPLIT_RE.search(body)
    top = body[:m.start()] if m else body
    return _SIGNATURE_LINE_RE.sub("", top)


def thread_topic(subject):
    return fold(_FWD_PREFIX_RE.sub("", subject or "")).strip()


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


def split_sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+|\s*[•·]\s*", text) if s.strip()]


def find_signals(text):
    """
    Find action keywords sentence by sentence.
    Returns {signal: [evidence sentence, ...]} after removing negated, future-tense and
    question matches, and resolving overlaps (longest phrase wins: "no longer on hold"
    beats "on hold").
    """
    hits = defaultdict(list)
    for sentence in split_sentences(fold(text)):
        sentence = _NOT_NEGATION_RE.sub(",", sentence)
        is_question = sentence.endswith("?") or bool(_QUESTION_START_RE.match(sentence))
        request_like = bool(_REQUEST_LIKE_RE.search(sentence))
        matches = []
        for sig, rx in _SIGNAL_RE.items():
            for m in rx.finditer(sentence):
                before = re.split(r"[,;:()]", sentence[:m.start()])[-1]
                if _NEGATION_RE.search(before):
                    continue  # "not sent", "don't hold"
                if sig in _STATEMENT_SIGNALS and (_FUTURE_RE.search(before) or is_question):
                    continue  # "will be sent", "has it been sent?", "confirm once sent"
                if sig == "DONE" and request_like:
                    continue  # "please complete the form" is not "done"
                if sig in _REQUEST_SIGNALS and is_question and not request_like and sig != "RESEND":
                    continue  # "should we hold?" is a question, "can you hold it?" is a request
                matches.append((m.start(), m.end(), sig))
        # Overlap resolution: keep the longest match, then the higher-priority signal.
        matches.sort(key=lambda x: (-(x[1] - x[0]), SIGNAL_PRIORITY.index(x[2])))
        kept = []
        for s, e, sig in matches:
            if all(e <= ks or s >= ke for ks, ke, _ in kept):
                kept.append((s, e, sig))
        for _, _, sig in kept:
            if sentence[:300] not in hits[sig]:
                hits[sig].append(sentence[:300])
    return dict(hits)


def primary_type(signals):
    for sig in SIGNAL_PRIORITY:
        if sig in signals:
            return SIGNAL_LABELS[sig]
    return "General / Unclassified"


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
        low = fold(text)
        for site, info in SITES.items():
            if any(fold(k) in low for k in info["keywords"]):
                return site, info["country"], company_code, label
    return "Unknown", "", company_code, ""


def classify_requester(name, email, gal, top_text, is_internal, is_portal=False):
    """Return requester category."""
    if is_portal:
        return "Portal / System"
    if in_list(DISTRIBUTION_SPECIALISTS, name, email):
        return "Distribution Specialist"
    if in_list(COLLECTIONS_TEAM, name, email):
        return "Collections"
    if any(name_matches(pm, name, email) for pm in PROJECT_MANAGERS):
        return "Project Manager"
    profile = fold(" ".join([gal.get("title", ""), gal.get("department", "")]))
    if any(fold(k) in profile for k in COLLECTIONS_KEYWORDS):
        return "Collections"
    if any(fold(k) in profile for k in PM_KEYWORDS):
        return "Project Manager"
    if not is_internal:
        return "External / Customer"
    signature = fold(top_text[-800:])
    if any(fold(k) in signature for k in COLLECTIONS_KEYWORDS):
        return "Collections"
    if any(fold(k) in signature for k in PM_KEYWORDS):
        return "Project Manager"
    return "Other Internal"


# =============================================================================
# Outlook access
# =============================================================================

_BUSY_HRESULTS = {-2147418111, -2147417846, -2147352567}  # call rejected / busy / exception


def com_get(obj, attr, default=None, retries=3):
    """Read a COM property, retrying when Outlook is busy."""
    for attempt in range(retries):
        try:
            return getattr(obj, attr)
        except Exception as e:
            code = getattr(e, "hresult", None) or (e.args[0] if getattr(e, "args", None) else None)
            if code in _BUSY_HRESULTS and attempt < retries - 1:
                time.sleep(0.5 * (attempt + 1))
                continue
            return default
    return default


class OutlookReader:
    def __init__(self, internal_domains):
        import win32com.client  # imported here so the logic above is testable anywhere
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
        key = com_get(ae, "Address", "")
        if not key:
            return ""
        if key in self._smtp_cache:
            return self._smtp_cache[key]
        smtp = key
        try:
            if com_get(ae, "Type") == "EX":
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
        key = com_get(ae, "Address", "")
        if not key:
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
        domain = a.split("@")[1]
        return any(domain == d or domain.endswith("." + d) for d in self.internal_domains)

    @staticmethod
    def message_id(item):
        try:
            return item.PropertyAccessor.GetProperty(
                "http://schemas.microsoft.com/mapi/proptag/0x1035001F") or ""
        except Exception:
            return ""

    # --- folder walking ------------------------------------------------------
    def stores(self, name_filters=None):
        for store in self.ns.Stores:
            name = com_get(store, "DisplayName")
            if not name:
                continue
            if name_filters and not any(f.lower() in name.lower() for f in name_filters):
                continue
            yield name, store

    def walk_folders(self, folder, path=""):
        name = com_get(folder, "Name")
        if name is None or fold(name) in SKIP_FOLDERS:
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
        """Newest first; stops at the first email older than `since` (locale-independent)."""
        if com_get(folder, "DefaultItemType") != 0:  # 0 = olMailItem
            return
        items = com_get(folder, "Items")
        if items is None:
            return
        sorted_ok = True
        try:
            items.Sort("[ReceivedTime]", True)
        except Exception:
            sorted_ok = False
        for item in items:
            try:
                if com_get(item, "Class") != 43:  # 43 = olMail
                    continue
                t = com_get(item, "ReceivedTime") or com_get(item, "SentOn")
                if t is None:
                    continue
                received = to_naive(t)
                if received < since:
                    if sorted_ok:
                        break
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
    records, seen = [], {}
    for store_name, store in reader.stores(store_filters):
        print(f"\n[Mailbox] {store_name}")
        try:
            root = store.GetRootFolder()
        except Exception as e:
            print(f"  ! cannot open: {e}")
            continue
        for folder_path, folder in reader.walk_folders(root):
            count = scanned = 0
            for item, received in reader.mail_items(folder, since):
                scanned += 1
                rec = analyse_item(reader, item, received, store_name, folder_path)
                if not rec:
                    continue
                # The same email can sit in several mailboxes (yours + shared): keep one.
                key = rec["_message_id"] or (fold(rec["Subject"]), fold(rec["From Email"]),
                                             received.replace(second=0))
                if key in seen:
                    seen[key]["Mailbox"] += f"; {store_name}/{folder_path}"
                    continue
                seen[key] = rec
                records.append(rec)
                count += 1
            if scanned:
                print(f"  {folder_path}: {scanned} emails checked, {count} relevant")
    return records


def analyse_item(reader, item, received, store_name, folder_path):
    subject = com_get(item, "Subject", "") or ""
    body = (com_get(item, "Body", "") or "")[:MAX_BODY_CHARS]
    attachments = []
    try:
        for a in item.Attachments:
            fn = com_get(a, "FileName", "")
            if fn and not re.match(r"^image\d*\.(png|jpg|jpeg|gif)$", fn, re.I):  # skip signature logos
                attachments.append(fn)
    except Exception:
        pass
    att_text = " ".join(attachments)

    top = newest_message(body)
    # A RE:/FW: subject just repeats the original ask - only the new text counts.
    signals = find_signals(top if _FWD_PREFIX_RE.match(subject) else f"{subject}\n{top}")
    hint_text = fold(f"{subject}\n{body}\n{att_text}")
    has_hint = any(h in hint_text for h in INVOICE_HINTS)
    if not has_hint and not signals:
        return None

    sender_ae = com_get(item, "Sender")
    sender_name = com_get(item, "SenderName", "") or ""
    sender_email = reader.smtp_of(sender_ae) or (com_get(item, "SenderEmailAddress", "") or "")
    gal = reader.gal_details(sender_ae)
    sender_internal = reader.is_internal(sender_email)
    sender_domain = sender_email.lower().split("@")[-1] if "@" in sender_email else ""
    is_portal = any(sender_domain == d or sender_domain.endswith("." + d) for d in PORTAL_DOMAINS)

    to, cc, external_recipients = [], [], []
    try:
        for r in item.Recipients:
            addr = reader.smtp_of(com_get(r, "AddressEntry")) or com_get(r, "Address", "") or com_get(r, "Name", "")
            (to if com_get(r, "Type") == 1 else cc).append(addr)
            if not reader.is_internal(addr):
                external_recipients.append(addr)
    except Exception:
        pass

    # Invoice numbers: subject + newest message + attachment names first.
    invoices = extract_invoice_numbers(subject, top, att_text)
    body_invoices = extract_invoice_numbers(body)

    category = classify_requester(sender_name, sender_email, gal, top, sender_internal, is_portal)
    site, country, company_code, site_source = detect_site(sender_name, sender_email, gal, subject, top, body)

    has_invoice_attachment = any(re.search(r"\.(pdf|xml|tif|tiff|zip)$", a, re.I) for a in attachments)
    outbound_with_invoice = sender_internal and bool(external_recipients) and has_invoice_attachment
    is_reply = bool(_REPLY_SUBJECT_RE.match(subject)) or len(top) < len(body) - 20

    return {
        "Received": received,
        "Mailbox": f"{store_name}/{folder_path}",
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
        "Request Type": primary_type(signals),
        "Keywords Found": ", ".join(SIGNAL_LABELS[s] for s in SIGNAL_PRIORITY if s in signals),
        "Invoice Numbers": ", ".join(invoices or body_invoices),
        "Attachments": att_text,
        "To": "; ".join(to),
        "CC": "; ".join(cc),
        "External Recipients": "; ".join(external_recipients),
        "Outbound With Invoice Attached": outbound_with_invoice,
        "Snippet": re.sub(r"\s+", " ", top)[:400],
        "_invoices": invoices,
        "_body_invoices": body_invoices,
        "_signals": signals,
        "_has_hint": has_hint,
        "_internal": sender_internal,
        "_is_reply": is_reply,
        "_conversation": com_get(item, "ConversationID", "") or "",
        "_topic": thread_topic(subject),
        "_message_id": reader.message_id(item),
    }


# =============================================================================
# Status per invoice
# =============================================================================

def group_records(records):
    """Group emails per invoice number; attach replies without a number via conversation/topic."""
    groups = defaultdict(list)
    conv_keys, topic_keys = defaultdict(set), defaultdict(set)

    def add(key, r):
        if r not in groups[key]:
            groups[key].append(r)
            if r["_conversation"]:
                conv_keys[r["_conversation"]].add(key)
            if r["_topic"]:
                topic_keys[r["_topic"]].add(key)

    for r in records:
        for k in r["_invoices"] or r["_body_invoices"]:
            add(k, r)

    for r in records:
        if r["_invoices"] or r["_body_invoices"]:
            continue
        keys = conv_keys.get(r["_conversation"]) or topic_keys.get(r["_topic"]) if (
            r["_conversation"] or r["_topic"]) else None
        if keys:
            for k in list(keys):
                add(k, r)
        elif r["_has_hint"] and r["_signals"]:
            add(f"(no invoice #) {r['Subject'][:60]}", r)
    return groups


def evaluate_invoice(emails):
    """
    Replay the thread in date order and keep a status:
      request -> PENDING, hold -> ON HOLD, release -> PENDING, cancel -> CANCEL,
      sent/outbound/done -> DISTRIBUTED, customer receipt -> CONFIRMED, resend -> PENDING again.
    """
    state, conf, by, by_cat, on, evidence = None, "", "", "", None, ""
    hold_note, hold_by, timeline, flags = "", "", [], []

    def set_state(new, e, confidence="", ev=""):
        nonlocal state, conf, by, by_cat, on, evidence
        state, conf, by, by_cat, on, evidence = new, confidence, e["From"], e["Requester Category"], e["Received"], ev

    for e in sorted(emails, key=lambda x: x["Received"]):
        sig = e["_signals"]
        external = not e["_internal"] and e["Requester Category"] != "Portal / System"
        portal = e["Requester Category"] == "Portal / System"
        events = []

        if external:
            if "RESEND" in sig:
                set_state("PENDING - customer asks for resend / did not receive", e, "", sig["RESEND"][0])
                events.append("customer resend")
            elif "RECEIPT" in sig and state and state.startswith("DISTRIBUTED"):
                set_state("DISTRIBUTED - customer confirmed receipt", e, "High", sig["RECEIPT"][0])
                events.append("customer confirmed")
            if "DISPUTE" in sig:
                flags.append(f"Customer dispute {e['Received']:%Y-%m-%d}")
                events.append("dispute")
        elif portal:
            if "RECEIPT" in sig or "SENT" in sig:
                ev = (sig.get("RECEIPT") or sig.get("SENT"))[0]
                set_state("DISTRIBUTED - portal confirmation", e, "High", ev)
                events.append("portal confirmed")
        else:
            # 1. requests
            for s in ("DISTRIBUTION_REQUEST", "SPECIAL_INSTRUCTION", "FOLLOW_UP"):
                if s in sig:
                    events.append(SIGNAL_LABELS[s])
                    if state is None:
                        set_state("PENDING", e)
            if "DISTRIBUTION_REQUEST" in sig and "HOLD" not in sig and state and state.startswith("ON HOLD"):
                if fold(e["From"]) == fold(hold_by):
                    events.append("hold released (same person asks to send)")
                    set_state("PENDING - hold released", e, "", sig["DISTRIBUTION_REQUEST"][0])
                else:
                    flags.append(f"Distribution requested by {e['From']} while on hold (hold by {hold_by})")
            if "RESEND" in sig:
                events.append("resend request")
                set_state("PENDING - resend requested", e, "", sig["RESEND"][0])
            # 2. release / hold / cancel
            if "RELEASE" in sig:
                events.append("hold released")
                if state is None or state.startswith(("ON HOLD", "PENDING")):
                    set_state("PENDING - hold released", e, "", sig["RELEASE"][0])
            if "HOLD" in sig:
                events.append("HOLD")
                hold_note, hold_by = sig["HOLD"][0], e["From"]
                if state and state.startswith("DISTRIBUTED"):
                    set_state("HOLD REQUESTED AFTER DISTRIBUTION - review / recall", e, "", hold_note)
                else:
                    set_state("ON HOLD - do not distribute", e, "", hold_note)
            if "CANCEL" in sig:
                events.append("cancel/rebill")
                set_state("CANCEL / REBILL requested - review", e, "", sig["CANCEL"][0])
            # 3. evidence that it went out
            attached_external = "SENT_ATTACHED" in sig and e["External Recipients"]
            if e["Outbound With Invoice Attached"]:
                events.append("SENT to customer (attachment)")
                set_state("DISTRIBUTED", e, "High",
                          f"Email to {e['External Recipients']} with {e['Attachments']}")
            elif attached_external:
                events.append("SENT to customer")
                set_state("DISTRIBUTED", e, "Medium", sig["SENT_ATTACHED"][0])
            elif "SENT" in sig and "HOLD" not in sig:
                events.append("says SENT")
                strength = "Medium" if e["External Recipients"] or e["Requester Category"] in (
                    "Distribution Specialist", "Project Manager", "Collections") else "Low"
                set_state("DISTRIBUTED", e, strength, sig["SENT"][0])
            elif "DONE" in sig and e["_is_reply"]:
                events.append("DONE")
                strength = "Medium" if e["Requester Category"] == "Distribution Specialist" else "Low"
                if state and state.startswith(("PENDING", "IN PROGRESS")):
                    set_state("DISTRIBUTED", e, strength, sig["DONE"][0])
                elif state and state.startswith("ON HOLD"):
                    flags.append(f"Hold acknowledged by {e['From']}")
                elif state and state.startswith("CANCEL"):
                    flags.append(f"Cancel/rebill actioned by {e['From']}")
            elif e["Requester Category"] == "Distribution Specialist" and state and state.startswith("PENDING"):
                events.append("specialist replied")
                set_state("IN PROGRESS - specialist replied (verify)", e, "Low", e["Snippet"][:200])

        if events:
            timeline.append(f"{e['Received']:%m-%d} {e['From']} ({e['Requester Category']}): {', '.join(events)}")

    if state is None:
        state = "NO REQUEST FOUND (info only)"
    return {
        "status": state, "confidence": conf, "by": by, "by_cat": by_cat, "on": on,
        "evidence": evidence, "hold_note": hold_note, "timeline": timeline, "flags": flags,
    }


def build_status(records):
    rows = []
    for key, emails in group_records(records).items():
        emails.sort(key=lambda e: e["Received"])
        requests = [e for e in emails if e["_internal"]
                    and e["Requester Category"] != "Distribution Specialist"
                    and set(e["_signals"]) & {"DISTRIBUTION_REQUEST", "RESEND", "HOLD", "RELEASE",
                                              "CANCEL", "SPECIAL_INSTRUCTION", "FOLLOW_UP", "SENT"}]
        anchor = requests[0] if requests else emails[0]
        result = evaluate_invoice(emails)

        def uniq(values):
            return ", ".join(dict.fromkeys(v for v in values if v))

        site_rec = next((e for e in requests if e["Site"] != "Unknown"),
                        next((e for e in emails if e["Site"] != "Unknown"), anchor))
        instructions = uniq(s for e in emails for sig in ("SPECIAL_INSTRUCTION", "HOLD", "RELEASE", "CANCEL")
                            for s in e["_signals"].get(sig, []))

        rows.append({
            "Invoice #": key,
            "Status": result["status"],
            "Confidence": result["confidence"],
            "Site": site_rec["Site"],
            "Country": site_rec["Country"],
            "Company Code": uniq(e["Company Code"] for e in emails),
            "First Request Date": anchor["Received"],
            "Requested By": anchor["From"],
            "Requester Category": anchor["Requester Category"],
            "Primary Request Type": anchor["Request Type"],
            "All Request Types": uniq(t.strip() for e in requests for t in e["Keywords Found"].split(",")),
            "All Requesters": uniq(f"{e['From']} ({e['Requester Category']})" for e in requests),
            "Latest Request Date": requests[-1]["Received"] if requests else None,
            "Actioned By": result["by"] if not result["status"].startswith(("PENDING", "NO REQUEST")) else "",
            "Actioned By Category": result["by_cat"] if not result["status"].startswith(("PENDING", "NO REQUEST")) else "",
            "Actioned On": result["on"] if not result["status"].startswith(("PENDING", "NO REQUEST")) else None,
            "Evidence": result["evidence"][:500],
            "Special Instructions / Hold Notes": instructions[:1000],
            "Flags": "; ".join(result["flags"]),
            "Timeline": " -> ".join(result["timeline"])[:2000],
            "Days Open": (dt.datetime.now() - anchor["Received"]).days if result["status"].startswith("PENDING") else None,
            "Emails In Thread": len(emails),
            "Subjects": uniq(e["Subject"] for e in emails)[:500],
            "Mailboxes": uniq(e["Mailbox"] for e in emails)[:500],
        })
    return rows


# =============================================================================
# Excel output
# =============================================================================

def keyword_hits(records):
    rows = []
    for r in records:
        for sig in SIGNAL_PRIORITY:
            for sentence in r["_signals"].get(sig, []):
                rows.append({
                    "Received": r["Received"], "From": r["From"], "Requester Category": r["Requester Category"],
                    "Keyword Type": SIGNAL_LABELS[sig], "Sentence": sentence, "Invoice Numbers": r["Invoice Numbers"],
                    "Subject": r["Subject"], "Mailbox": r["Mailbox"],
                })
    return rows


def write_report(records, status_rows, path):
    import pandas as pd

    detail_cols = [c for c in records[0].keys() if not c.startswith("_")] if records else []
    detail = pd.DataFrame([{c: r[c] for c in detail_cols} for r in records])
    if not detail.empty:
        detail = detail.sort_values("Received", ascending=False)

    status = pd.DataFrame(status_rows)
    if not status.empty:
        order = ["PENDING", "IN PROGRESS", "HOLD REQUESTED AFTER", "ON HOLD", "CANCEL", "DISTRIBUTED", "NO REQUEST"]
        status["_o"] = status["Status"].map(lambda s: next((i for i, k in enumerate(order) if s.startswith(k)), 9))
        status = status.sort_values(["_o", "First Request Date"]).drop(columns="_o")
        action = status[status["Status"].str.startswith(("PENDING", "IN PROGRESS", "HOLD REQUESTED", "CANCEL"))
                        | (status["Confidence"] == "Low")]
        holds = status[status["Status"].str.startswith(("ON HOLD", "HOLD REQUESTED"))]
    else:
        action = holds = status

    hits = pd.DataFrame(keyword_hits(records))

    with pd.ExcelWriter(path, engine="openpyxl") as xw:
        status.to_excel(xw, sheet_name="Invoice Status", index=False)
        action.to_excel(xw, sheet_name="Action Needed", index=False)
        holds.to_excel(xw, sheet_name="On Hold", index=False)
        if not detail.empty:
            internal = detail[~detail["Requester Category"].isin(["Distribution Specialist", "External / Customer",
                                                                  "Portal / System"])]
            ws_row = 1
            for idx, (title, rows_, cols_) in enumerate([
                ("Requests by type x requester category", internal["Request Type"], internal["Requester Category"]),
                ("Requests by site x requester category", internal["Site"], internal["Requester Category"]),
            ] + ([("Invoice status x site", status["Status"], status["Site"])] if not status.empty else [])):
                table = pd.crosstab(rows_, cols_, margins=True, margins_name="Total")
                table.to_excel(xw, sheet_name="Summary", startrow=ws_row)
                xw.sheets["Summary"].cell(row=ws_row, column=1, value=title)
                ws_row += len(table) + 4
        hits.to_excel(xw, sheet_name="Keyword Hits", index=False)
        detail.to_excel(xw, sheet_name="All Emails", index=False)

        for ws in xw.book.worksheets:
            if ws.title != "Summary" and ws.max_row > 1:
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
    ap.add_argument("--specialist", nargs="*", help="distribution specialist name(s)/email(s)")
    ap.add_argument("--output", help="output .xlsx path")
    args = ap.parse_args()

    if sys.platform != "win32":
        sys.exit("This script needs Windows with Outlook desktop (COM automation).")
    try:
        import pythoncom
        pythoncom.CoInitialize()
    except ImportError:
        sys.exit("pywin32 is required:  pip install pywin32 pandas openpyxl")

    if args.specialist:
        DISTRIBUTION_SPECIALISTS[:] = args.specialist

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
    print(f"\n{len(records)} relevant emails, {len(status_rows)} invoices/threads")
    for s, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"  {n:5d}  {s}")
    print(f"\nReport written to: {output}")


if __name__ == "__main__":
    main()
