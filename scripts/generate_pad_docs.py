#!/usr/bin/env python3
"""Build Power Automate Desktop inventory and per-item docs.

Parses Microsoft Learn action-reference markdown (local clone) plus
curated extras (Triggers, Power Platform, Power Fx, cloud connectors).
Generated prose is original; parameter names are product UI labels.
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "power-automate-desktop"
MODULES = DOCS / "modules"
SOURCE_DEFAULT = Path("/tmp/pad-docs/articles/desktop-flows/actions-reference")
LEARN_BASE = (
    "https://learn.microsoft.com/en-us/power-automate/"
    "desktop-flows/actions-reference"
)
CHEAT_SHEET = Path(
    "/home/ubuntu/.cursor/projects/workspace/agent-tools/"
    "ccbcdd54-5d0f-4f0d-99db-c760eb5bf8fb.txt"
)

HEADING_RE = re.compile(
    r'^(#{2,6})\s+(?:<a\s+name="([^"]+)"></a>\s*)?(.+?)\s*$',
    re.M,
)
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
HTML_TAG_RE = re.compile(r"<[^>]+>")

SKIP_FILES = {
    "cognitive.md",  # index-only redirect
}

SKIP_TITLES = {
    "input parameters",
    "variables produced",
    "exceptions",
    "related information",
    "prerequisites",
    "prerequisites and limitations",
    "known limitations",
    "known limitations for performing an action by simulation",
    "getting started with sharepoint actions in desktop flows",
    "how to download the content of a sharepoint folder",
    "use files in cloud connector actions",
    "embed connection references on a desktop flow",
    "bring your own connection in console runs",
    "list of cloud connectors",
    "webdriver-based browser automation",
    "webdriver limitations",
    "adding ui elements",
    "use the windows ocr engine",
    "use the tesseract ocr engine",
    "natural language to script powered by copilot (preview)",
    "working with variables in scripting actions",
    "use the recognize entities in text action",
    "send an email with attachments",
    "add a fixed number of attachments",
    "add a dynamic number of attachments",
    "example",
    "request builder parameters",
    "attachments parameters",
    "handle custom errors raised by the throw custom error action",
    "using excel files synchronized through onedrive or sharepoint",
    "workaround 1",
    "workaround 2",
    "case with read from excel worksheet",
    "workaround",
    "what are fetchxml queries?",
    "example fetchxml query",
    "query support details and reference data",
    "robin code snippet for creating the data table",
    "powerfx code snippet for creating the data table",
}
SKIP_TITLE_PARTS = (
    "deprecation",
    "limitation",
    "workaround",
    "notice",
    "timeline",
)

SECTION_TITLES = {
    "input parameters",
    "variables produced",
    "exceptions",
}

MODULE_META: dict[str, tuple[str, str]] = {
    "access": (
        "Access",
        "Open local Microsoft Access databases, read tables, and run queries or macros.",
    ),
    "activedirectory": (
        "Active Directory",
        "Connect to AD and manage users, groups, and directory objects.",
    ),
    "aibuilder": (
        "AI Builder (preview)",
        "Call GPT text generation from a desktop flow. Human review is required.",
    ),
    "aws": (
        "AWS",
        "Automate Amazon EC2 instances, EBS volumes, and snapshots.",
    ),
    "azure": (
        "Azure",
        "Create Azure sessions and manage resource groups, VMs, disks, and snapshots.",
    ),
    "clipboard": (
        "Clipboard",
        "Read, write, or clear the Windows clipboard.",
    ),
    "cmd": (
        "CMD session",
        "Drive an interactive Command Prompt session: open, write, wait, and close.",
    ),
    "compression": (
        "Compression",
        "Zip and unzip files and folders.",
    ),
    "conditionals": (
        "Conditionals",
        "Branch with If / Else if / Else and Switch / Case / Default case.",
    ),
    "cryptography": (
        "Cryptography",
        "Hash or AES-encrypt text and files.",
    ),
    "cyberark": (
        "CyberArk",
        "Pull application passwords from CyberArk at runtime.",
    ),
    "database": (
        "Database",
        "Open SQL connections and run statements against databases.",
    ),
    "datetime": (
        "Date time",
        "Read the clock, add intervals, and subtract dates.",
    ),
    "display": (
        "Message boxes",
        "Prompt the user with messages, inputs, file pickers, and custom forms.",
    ),
    "email": (
        "Email",
        "Send and retrieve mail over IMAP/SMTP without Outlook.",
    ),
    "excel": (
        "Excel",
        "Launch Excel, read and write cells, and run worksheet operations.",
    ),
    "exchange": (
        "Exchange Server",
        "Connect to Exchange and process mailbox messages.",
    ),
    "file": (
        "File",
        "Copy, move, read, write, and convert local files, including CSV and binary.",
    ),
    "flowcontrol": (
        "Flow control",
        "Labels, subflows, waits, regions, errors, and flow stop rules.",
    ),
    "folder": (
        "Folder",
        "Create, copy, move, list, and empty folders.",
    ),
    "ftp": (
        "FTP",
        "Open FTP/SFTP sessions and transfer files and folders.",
    ),
    "googlecognitive": (
        "Google Cognitive",
        "Call Google Cloud Natural Language and Vision APIs.",
    ),
    "ibmcognitive": (
        "IBM Cognitive",
        "Call IBM Watson document, vision, translation, and tone APIs.",
    ),
    "logging": (
        "Logging",
        "Write custom messages into desktop flow run action details (premium).",
    ),
    "loops": (
        "Loops",
        "Repeat actions with Loop, Loop condition, For each, Exit loop, and Next loop.",
    ),
    "microsoftcognitive": (
        "Microsoft Cognitive",
        "Call Azure Cognitive Services for vision, OCR, language, and sentiment.",
    ),
    "mouseandkeyboard": (
        "Mouse and keyboard",
        "Move the pointer, click, type keys, and wait on mouse or shortcut events.",
    ),
    "ocr": (
        "OCR",
        "Find or extract on-screen text with Windows OCR or Tesseract.",
    ),
    "outlook": (
        "Outlook",
        "Drive the local Outlook desktop client for send, retrieve, and reply.",
    ),
    "pdf": (
        "PDF",
        "Extract text, tables, images, and pages, or merge PDF files.",
    ),
    "powerautomateenvironment": (
        "Power Automate environment",
        "Read Dataverse environment variables, including secrets at runtime.",
    ),
    "powerautomatesecretvariables": (
        "Power Automate secret variables",
        "Resolve credentials stored in the Power Automate portal.",
    ),
    "runflow": (
        "Run flow",
        "Call another desktop flow and wait for its outputs.",
    ),
    "sap": (
        "SAP automation",
        "Launch SAP GUI, start transactions, and interact with SAP UI elements.",
    ),
    "scripting": (
        "Scripting",
        "Run DOS, VBScript, JavaScript, PowerShell, Python, or .NET snippets.",
    ),
    "services": (
        "Windows services",
        "Start, stop, pause, resume, and wait on Windows services.",
    ),
    "system": (
        "System",
        "Run apps, manage processes, ping hosts, and edit environment variables.",
    ),
    "terminalemulation": (
        "Terminal emulation",
        "Automate terminal sessions (mainframe/AS400-style hosts).",
    ),
    "testing": (
        "Testing",
        "Assert expected results and invoke a desktop flow as a test.",
    ),
    "text": (
        "Text",
        "Join, split, parse, replace, convert, and generate text values.",
    ),
    "uiautomation": (
        "UI automation",
        "Click, fill, extract, and wait on desktop application UI elements.",
    ),
    "variables": (
        "Variables",
        "Set values and manipulate lists, data tables, JSON, and numbers.",
    ),
    "web": (
        "HTTP",
        "Download files, call REST endpoints, and invoke SOAP services.",
    ),
    "webautomation": (
        "Browser automation",
        "Launch browsers, fill web forms, extract data, and run page JavaScript.",
    ),
    "word": (
        "Word",
        "Launch Word, read and write documents, insert images, and replace text.",
    ),
    "workqueues": (
        "Work queues",
        "Pull, add, update, requeue, and filter Power Automate work queue items.",
    ),
    "workstation": (
        "Workstation",
        "Control printers, screenshots, resolution, lock, logoff, and shutdown.",
    ),
    "xml": (
        "XML",
        "Read XML, run XPath, and edit elements and attributes.",
    ),
    "triggers": (
        "Triggers",
        "Pause until a configured mouse or keyboard event hits a UI element.",
    ),
    "power-platform": (
        "Power Platform",
        "Launch a Power App from the desktop flow and exchange inputs/outputs.",
    ),
    "custom-actions": (
        "Custom actions",
        "Load organization-uploaded action groups from the current environment.",
    ),
    "cloud-connectors": (
        "Cloud connectors",
        "Run Power Automate cloud connector operations inside a desktop flow.",
    ),
}

CLOUD_CONNECTOR_META: dict[str, tuple[str, str]] = {
    "sharepoint": (
        "SharePoint (cloud connector)",
        "Same SharePoint connector used in cloud flows, available in the PAD actions pane.",
    ),
    "office365outlook": (
        "Office 365 Outlook (cloud connector)",
        "Mailbox, calendar, and contact operations through Microsoft Graph.",
    ),
    "microsoft-teams": (
        "Microsoft Teams (cloud connector)",
        "Post messages, manage teams/channels, and call Graph team endpoints.",
    ),
    "microsoft-dataverse": (
        "Microsoft Dataverse (cloud connector)",
        "Row, file, and bound/unbound action operations against the current environment.",
    ),
    "excel-online": (
        "Excel Online (Business) (cloud connector)",
        "Tables, worksheets, rows, and Office Scripts in workbooks stored in the cloud.",
    ),
    "onedrive": (
        "OneDrive (cloud connector)",
        "Personal OneDrive files, sharing links, and conversions.",
    ),
    "onedrive-business": (
        "OneDrive for work or school (cloud connector)",
        "Work/school OneDrive files, sharing links, and conversions.",
    ),
    "onenote": (
        "OneNote (Business) (cloud connector)",
        "Notebooks, sections, and page content in OneNote for work or school.",
    ),
    "word-online": (
        "Word Online (Business) (cloud connector)",
        "Populate Word templates and convert Word documents to PDF.",
    ),
    "microsoft-forms": (
        "Microsoft Forms (cloud connector)",
        "Read form response details.",
    ),
    "rss": (
        "RSS (cloud connector)",
        "List items from an RSS feed.",
    ),
}

POWER_FX: list[tuple[str, str, str]] = [
    ("Abs", "Math", "Distance of a number from zero."),
    ("Acos", "Math", "Arccosine of a number, in radians."),
    ("Acot", "Math", "Arccotangent of a number, in radians."),
    ("AddColumns", "Table", "Returns a table with extra calculated columns."),
    ("And", "Logic", "True only when every argument is true (`&&`)."),
    ("Asin", "Math", "Arcsine of a number, in radians."),
    ("Atan", "Math", "Arctangent of a number, in radians."),
    ("Atan2", "Math", "Arctangent from an (x, y) pair, in radians."),
    ("Average", "Math", "Mean of a table expression or argument list."),
    ("Blank", "Utility", "A blank/null value for data sources."),
    ("Boolean", "Conversion", "Coerce text, number, or dynamic data to true/false."),
    ("Char", "Text", "Character for a numeric code."),
    ("Clear", "Collection", "Empty a collection."),
    ("ClearCollect", "Collection", "Empty a collection, then add records."),
    ("Coalesce", "Utility", "First non-blank argument."),
    ("Collect", "Collection", "Create a collection or append records."),
    ("Concat", "Text", "Join strings produced from a table."),
    ("Concatenate", "Text", "Join two or more strings."),
    ("Cos", "Math", "Cosine of an angle in radians."),
    ("Cot", "Math", "Cotangent of an angle in radians."),
    ("Count", "Table", "Count records that hold numbers."),
    ("CountA", "Table", "Count records that are not empty."),
    ("CountIf", "Table", "Count records that match a condition."),
    ("CountRows", "Table", "Count all records."),
    ("Date", "Date", "Build a date from year, month, and day."),
    ("DateAdd", "Date", "Add days, months, quarters, or years."),
    ("DateDiff", "Date", "Difference between two dates in a chosen unit."),
    ("DateTime", "Date", "Build a date/time from date and time parts."),
    ("DateTimeValue", "Date", "Parse a date-and-time string."),
    ("DateValue", "Date", "Parse a date-only string."),
    ("Day", "Date", "Day-of-month from a date/time."),
    ("Dec2Hex", "Conversion", "Number to hexadecimal text."),
    ("Decimal", "Conversion", "Text to a decimal number."),
    ("Degrees", "Math", "Radians to degrees."),
    ("Distinct", "Table", "Unique records from a table."),
    ("DropColumns", "Table", "Table without the named columns."),
    ("EDate", "Date", "Add months without changing the day-of-month."),
    ("EncodeHTML", "Text", "Escape characters for HTML."),
    ("EncodeUrl", "Text", "Percent-encode a URL fragment."),
    ("EndsWith", "Text", "True when a string ends with another string."),
    ("EOMonth", "Date", "Last day of a month after adding months."),
    ("Error", "Logic", "Raise or forward an error."),
    ("Exp", "Math", "e raised to a power."),
    ("Filter", "Table", "Rows that match one or more conditions."),
    ("Find", "Text", "Start position of one string inside another."),
    ("First", "Table", "First record."),
    ("FirstN", "Table", "First N records."),
    ("Float", "Conversion", "Text to a floating-point number."),
    ("ForAll", "Table", "Evaluate a formula for every record."),
    ("GUID", "Utility", "Parse or create a GUID."),
    ("Hex2Dec", "Conversion", "Hexadecimal text to a number."),
    ("Hour", "Date", "Hour portion of a date/time."),
    ("If", "Logic", "Pick a result from a true/false test."),
    ("IfError", "Logic", "Fallback value or action when an error occurs."),
    ("Index", "Table", "Record at a 1-based position."),
    ("Int", "Math", "Round down to the nearest integer."),
    ("IsBlank", "Logic", "True when the value is blank."),
    ("IsBlankOrError", "Logic", "True when the value is blank or an error."),
    ("IsEmpty", "Logic", "True when a table has no records."),
    ("IsError", "Logic", "True when the value is an error."),
    ("IsNumeric", "Logic", "True when the value is numeric."),
    ("IsToday", "Date", "True when the value falls on today's local date."),
    ("Language", "Utility", "Language tag of the current user."),
    ("Last", "Table", "Last record."),
    ("LastN", "Table", "Last N records."),
    ("Left", "Text", "Leftmost characters of a string."),
    ("Len", "Text", "Character length."),
    ("Ln", "Math", "Natural logarithm."),
    ("Log", "Math", "Logarithm in a chosen base."),
    ("LookUp", "Table", "First record that matches a condition."),
    ("Lower", "Text", "Lowercase letters."),
    ("Max", "Math", "Largest value in a set or table."),
    ("Mid", "Text", "Substring from a start position."),
    ("Min", "Math", "Smallest value in a set or table."),
    ("Minute", "Date", "Minute portion of a date/time."),
    ("Mod", "Math", "Remainder after division."),
    ("Month", "Date", "Month number from a date/time."),
    ("Not", "Logic", "Boolean negation (`!`)."),
    ("Now", "Date", "Current local date and time."),
    ("Or", "Logic", "True when any argument is true (`||`)."),
    ("Patch", "Table", "Create or merge records."),
    ("Pi", "Math", "The constant π."),
    ("PlainText", "Text", "Strip HTML/XML tags."),
    ("Power", "Math", "Base raised to an exponent (`^`)."),
    ("Proper", "Text", "Capitalize the first letter of each word."),
    ("Radians", "Math", "Degrees to radians."),
    ("Rand", "Math", "Pseudo-random number between 0 and 1."),
    ("RandBetween", "Math", "Pseudo-random integer in a range."),
    ("Remove", "Table", "Delete specific records from a source."),
    ("RenameColumns", "Table", "Rename one or more columns."),
    ("Replace", "Text", "Overwrite characters by start position."),
    ("Right", "Text", "Rightmost characters of a string."),
    ("Round", "Math", "Nearest value at a given precision."),
    ("RoundDown", "Math", "Round toward zero/down."),
    ("RoundUp", "Math", "Round away from zero/up."),
    ("Search", "Table", "Rows whose selected columns contain a string."),
    ("Second", "Date", "Second portion of a date/time."),
    ("Sequence", "Table", "Table of sequential numbers."),
    ("Set", "Utility", "Assign a global; limited support in PAD."),
    ("ShowColumns", "Table", "Keep only the named columns."),
    ("Shuffle", "Table", "Randomize record order."),
    ("Sin", "Math", "Sine of an angle in radians."),
    ("Sort", "Table", "Sort records by a formula."),
    ("SortByColumns", "Table", "Sort records by column names."),
    ("Split", "Text", "Break a string into a table of pieces."),
    ("Sqrt", "Math", "Square root."),
    ("StartsWith", "Text", "True when a string begins with another string."),
    ("StdevP", "Math", "Population standard deviation."),
    ("Substitute", "Text", "Replace matching substrings."),
    ("Sum", "Math", "Total of a table expression or argument list."),
    ("Summarize", "Table", "Group rows and aggregate the rest."),
    ("Switch", "Logic", "Match a value and evaluate the matching formula."),
    ("Table", "Table", "Build a temporary table from records."),
    ("Tan", "Math", "Tangent of an angle in radians."),
    ("Text", "Conversion", "Format any value as text."),
    ("Time", "Date", "Build a time from hour, minute, and second."),
    ("TimeValue", "Date", "Parse a time-only string."),
    ("TimeZoneOffset", "Date", "Minutes between UTC and local time."),
    ("Today", "Date", "Current local date (no time)."),
    ("Trim", "Text", "Collapse extra interior and edge spaces."),
    ("TrimEnds", "Text", "Strip leading and trailing spaces only."),
    ("Trunc", "Math", "Drop the fractional part of a number."),
    ("UniChar", "Text", "Character for a Unicode code point."),
    ("Upper", "Text", "Uppercase letters."),
    ("Value", "Conversion", "Parse text as a number."),
    ("VarP", "Math", "Population variance."),
    ("Weekday", "Date", "Weekday number from a date/time."),
    ("WeekNum", "Date", "Week number of a date/time."),
    ("With", "Utility", "Evaluate a formula against a named record."),
    ("Year", "Date", "Year from a date/time."),
]

EXTRA_ACTIONS = [
    {
        "id": "triggers/ui-element-event-trigger",
        "name": "UI element event trigger",
        "module": "triggers",
        "kind": "native-action",
        "anchor": "ui-element-event-trigger",
        "purpose": (
            "Pauses the flow until a mouse click or key event occurs on a "
            "chosen UI element, then runs the nested actions."
        ),
        "inputs": [
            {"name": "Trigger name", "optional": True, "accepts": "Text"},
            {"name": "UI element", "optional": False, "accepts": "UI element"},
            {"name": "Event", "optional": False, "accepts": "Mouse click, Keyboard"},
            {"name": "Scheduling mode", "optional": False, "accepts": "One time, Sequential"},
            {"name": "Fail with timeout error", "optional": False, "accepts": "Boolean"},
        ],
        "outputs": [
            {"name": "TriggerEventInstanceHandle", "type": "TriggerEventInstanceHandle"}
        ],
        "exceptions": [
            "UI element event trigger failed",
            "UI element event trigger failed with timeout error",
        ],
        "learn_url": f"{LEARN_BASE}/triggers#ui-element-event-trigger",
    },
    {
        "id": "power-platform/run-power-app",
        "name": "Run Power App (preview)",
        "module": "power-platform",
        "kind": "native-action",
        "anchor": "run-power-app",
        "purpose": (
            "Launches a canvas app from the desktop flow, passes values in, "
            "and collects values the app returns. Needs PAD 2.68+."
        ),
        "inputs": [
            {"name": "App", "optional": False, "accepts": "Power App"},
        ],
        "outputs": [],
        "exceptions": [],
        "learn_url": f"{LEARN_BASE}/power-platform",
    },
]


@dataclass
class Action:
    id: str
    name: str
    module: str
    kind: str
    purpose: str
    anchor: str = ""
    inputs: list[dict] = field(default_factory=list)
    outputs: list[dict] = field(default_factory=list)
    exceptions: list[str] = field(default_factory=list)
    learn_url: str = ""
    source_file: str = ""


def clean_cell(value: str) -> str:
    value = unescape(value or "")
    value = value.replace("\u00ad", "")
    value = MD_LINK_RE.sub(r"\1", value)
    value = HTML_TAG_RE.sub("", value)
    return re.sub(r"\s+", " ", value).strip()


def slug(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def parse_table(block: str) -> list[dict[str, str]]:
    lines = [ln for ln in block.splitlines() if ln.strip().startswith("|")]
    if len(lines) < 2:
        return []
    headers = [clean_cell(c) for c in lines[0].strip().strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for line in lines[1:]:
        if re.match(r"^\|\s*-+", line):
            continue
        cols = [clean_cell(c) for c in line.strip().strip("|").split("|")]
        if not any(cols):
            continue
        row = {}
        for i, header in enumerate(headers):
            row[header] = cols[i] if i < len(cols) else ""
        rows.append(row)
    return rows


def first_sentence(text: str) -> str:
    text = unescape(text)
    text = re.sub(r":::.*?:::", " ", text, flags=re.S)
    text = re.sub(r"!\[.*?\]\(.*?\)", " ", text)
    text = re.sub(r"\[!.*?\]", " ", text)
    text = MD_LINK_RE.sub(r"\1", text)
    text = HTML_TAG_RE.sub("", text)
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return ""
    match = re.match(r"(.+?[.!?])(\s|$)", text)
    return match.group(1) if match else text[:180]


def purpose_from_name(name: str) -> str:
    n = name.strip()
    patterns = [
        (r"^If (.+)$", lambda m: f"Opens a conditional branch that runs when {lower_first(m.group(1))}."),
        (r"^Wait for (.+)$", lambda m: f"Pauses the flow until {lower_first(m.group(1))}."),
        (r"^Launch (.+)$", lambda m: f"Starts {m.group(1)} and returns an instance later actions can reuse."),
        (r"^Attach(?: to)? (.+)$", lambda m: f"Connects the flow to {lower_first(m.group(1))} that is already running."),
        (r"^Get (.+)$", lambda m: f"Reads {lower_first(m.group(1))} into a flow variable."),
        (r"^Set (.+)$", lambda m: f"Writes {lower_first(m.group(1))}."),
        (r"^Create (.+)$", lambda m: f"Creates {lower_first(m.group(1))}."),
        (r"^Add (.+)$", lambda m: f"Adds {lower_first(m.group(1))}."),
        (r"^Insert (.+)$", lambda m: f"Inserts {lower_first(m.group(1))}."),
        (r"^Delete (.+)$", lambda m: f"Deletes {lower_first(m.group(1))}."),
        (r"^Remove (.+)$", lambda m: f"Removes {lower_first(m.group(1))}."),
        (r"^Update (.+)$", lambda m: f"Updates {lower_first(m.group(1))}."),
        (r"^Rename (.+)$", lambda m: f"Renames {lower_first(m.group(1))}."),
        (r"^Copy (.+)$", lambda m: f"Copies {lower_first(m.group(1))}."),
        (r"^Move (.+)$", lambda m: f"Moves {lower_first(m.group(1))}."),
        (r"^Close (.+)$", lambda m: f"Closes {lower_first(m.group(1))}."),
        (r"^Open (.+)$", lambda m: f"Opens {lower_first(m.group(1))}."),
        (r"^Send (.+)$", lambda m: f"Sends {lower_first(m.group(1))}."),
        (r"^Read (.+)$", lambda m: f"Reads {lower_first(m.group(1))}."),
        (r"^Write (.+)$", lambda m: f"Writes {lower_first(m.group(1))}."),
        (r"^Extract (.+)$", lambda m: f"Extracts {lower_first(m.group(1))}."),
        (r"^Convert (.+)$", lambda m: f"Converts {lower_first(m.group(1))}."),
        (r"^Run (.+)$", lambda m: f"Runs {lower_first(m.group(1))}."),
        (r"^Start (.+)$", lambda m: f"Starts {lower_first(m.group(1))}."),
        (r"^Stop (.+)$", lambda m: f"Stops {lower_first(m.group(1))}."),
        (r"^Display (.+)$", lambda m: f"Shows {lower_first(m.group(1))} to the user."),
        (r"^Populate (.+)$", lambda m: f"Types or fills {lower_first(m.group(1))}."),
        (r"^Click (.+)$", lambda m: f"Clicks {lower_first(m.group(1))}."),
        (r"^Press (.+)$", lambda m: f"Presses {lower_first(m.group(1))}."),
        (r"^Focus (.+)$", lambda m: f"Gives focus to {lower_first(m.group(1))}."),
        (r"^Hover (.+)$", lambda m: f"Hovers {lower_first(m.group(1))}."),
        (r"^Merge (.+)$", lambda m: f"Merges {lower_first(m.group(1))}."),
        (r"^Filter (.+)$", lambda m: f"Filters {lower_first(m.group(1))}."),
        (r"^Sort (.+)$", lambda m: f"Sorts {lower_first(m.group(1))}."),
        (r"^Clear (.+)$", lambda m: f"Clears {lower_first(m.group(1))}."),
        (r"^Hash (.+)$", lambda m: f"Hashes {lower_first(m.group(1))}."),
        (r"^Encrypt (.+)$", lambda m: f"Encrypts {lower_first(m.group(1))}."),
        (r"^Decrypt (.+)$", lambda m: f"Decrypts {lower_first(m.group(1))}."),
        (r"^List (.+)$", lambda m: f"Lists {lower_first(m.group(1))}."),
        (r"^Download (.+)$", lambda m: f"Downloads {lower_first(m.group(1))}."),
        (r"^Upload (.+)$", lambda m: f"Uploads {lower_first(m.group(1))}."),
        (r"^Invoke (.+)$", lambda m: f"Calls {lower_first(m.group(1))}."),
        (r"^Retrieve (.+)$", lambda m: f"Retrieves {lower_first(m.group(1))}."),
        (r"^Process (.+)$", lambda m: f"Processes {lower_first(m.group(1))}."),
        (r"^Take (.+)$", lambda m: f"Captures {lower_first(m.group(1))}."),
        (r"^Find (.+)$", lambda m: f"Finds {lower_first(m.group(1))}."),
        (r"^Replace (.+)$", lambda m: f"Replaces {lower_first(m.group(1))}."),
        (r"^Parse (.+)$", lambda m: f"Parses {lower_first(m.group(1))}."),
        (r"^Join (.+)$", lambda m: f"Joins {lower_first(m.group(1))}."),
        (r"^Split (.+)$", lambda m: f"Splits {lower_first(m.group(1))}."),
        (r"^Trim (.+)$", lambda m: f"Trims {lower_first(m.group(1))}."),
        (r"^Pad (.+)$", lambda m: f"Pads {lower_first(m.group(1))}."),
        (r"^End (.+)$", lambda m: f"Ends {lower_first(m.group(1))}."),
        (r"^Close (.+)$", lambda m: f"Closes {lower_first(m.group(1))}."),
        (r"^Save (.+)$", lambda m: f"Saves {lower_first(m.group(1))}."),
        (r"^Select (.+)$", lambda m: f"Selects {lower_first(m.group(1))}."),
        (r"^Expand/collapse (.+)$", lambda m: f"Expands or collapses {lower_first(m.group(1))}."),
        (r"^Drag and drop (.+)$", lambda m: f"Drags and drops {lower_first(m.group(1))}."),
        (r"^Go to (.+)$", lambda m: f"Navigates to {lower_first(m.group(1))}."),
        (r"^For each$", lambda _m: "Repeats nested actions once for every item in a list, table, or row."),
        (r"^Loop$", lambda _m: "Repeats nested actions a fixed number of times."),
        (r"^Loop condition$", lambda _m: "Repeats nested actions while a condition stays true."),
        (r"^Exit loop$", lambda _m: "Leaves the current loop and continues with the next action after it."),
        (r"^Next loop$", lambda _m: "Skips the rest of this iteration and starts the next one."),
        (r"^Else$", lambda _m: "Runs when no earlier If / Else if condition was true."),
        (r"^Else if$", lambda _m: "Tests another condition after an If that did not match."),
        (r"^Switch$", lambda _m: "Routes execution to the Case that matches an expression."),
        (r"^Case$", lambda _m: "One match arm inside a Switch block."),
        (r"^Default case$", lambda _m: "Fallback arm when no Case in a Switch matches."),
        (r"^Comment$", lambda _m: "Adds a note on the canvas. It does not run."),
        (r"^Label$", lambda _m: "Named jump target for a Go to action."),
        (r"^Go to$", lambda _m: "Jumps execution to a Label in the same subflow."),
        (r"^Wait$", lambda _m: "Pauses the flow for a number of seconds."),
        (r"^Region$", lambda _m: "Starts a named visual group of actions."),
        (r"^End region$", lambda _m: "Closes the matching Region group."),
        (r"^End$", lambda _m: "Closes the current block (condition, loop, or error block)."),
        (r"^Stop flow$", lambda _m: "Ends the desktop flow run."),
        (r"^Exit subflow$", lambda _m: "Returns from the current subflow to its caller."),
        (r"^Run subflow$", lambda _m: "Calls another subflow in this desktop flow, then resumes."),
        (r"^On block error$", lambda _m: "Starts a block whose nested failures are handled together."),
        (r"^Throw custom error$", lambda _m: "Raises a maker-defined error for On block error to catch."),
        (r"^Assert$", lambda _m: "Fails a test when an expression is not true."),
        (r"^ZIP files$", lambda _m: "Compresses files or folders into a ZIP archive."),
        (r"^Unzip files$", lambda _m: "Extracts files from a ZIP archive."),
        (r"^Block Input$", lambda _m: "Temporarily blocks the user's mouse and keyboard."),
        (r"^Ping$", lambda _m: "Checks whether a remote host answers on the network."),
        (r"^Log message$", lambda _m: "Writes a custom Info, Warning, or Error line into run details."),
        (r"^Get credential$", lambda _m: "Resolves a portal-stored credential into a flow variable."),
        (r"^Set variable$", lambda _m: "Creates or overwrites a flow variable."),
        (r"^Increase variable$", lambda _m: "Adds a number to a numeric variable."),
        (r"^Decrease variable$", lambda _m: "Subtracts a number from a numeric variable."),
    ]
    for pattern, builder in patterns:
        match = re.match(pattern, n, flags=re.I)
        if match:
            return builder(match)
    return f"Runs **{n}** from the actions pane."


def lower_first(text: str) -> str:
    text = text.strip()
    if not text:
        return text
    if text[:1].isupper() and (len(text) == 1 or not text[1:2].isupper()):
        return text[0].lower() + text[1:]
    return text


def extract_section(body: str, title: str) -> str:
    pattern = re.compile(
        rf"^#{{2,6}}\s+(?:<a\s+name=\"[^\"]+\"></a>\s*)?{re.escape(title)}\s*$",
        re.I | re.M,
    )
    match = pattern.search(body)
    if not match:
        return ""
    start = match.end()
    nxt = re.search(r"^#{2,6}\s+", body[start:], re.M)
    end = start + nxt.start() if nxt else len(body)
    return body[start:end].strip()


def parse_inputs(body: str) -> list[dict]:
    if re.search(r"doesn't require any input", body, re.I):
        return []
    section = extract_section(body, "Input parameters")
    if not section:
        return []
    rows = parse_table(section)
    items = []
    for row in rows:
        name = row.get("Argument") or row.get("Name") or ""
        if not name:
            continue
        items.append(
            {
                "name": name,
                "optional": row.get("Optional", ""),
                "accepts": row.get("Accepts", ""),
                "default": row.get("Default Value", ""),
            }
        )
    return items


def parse_outputs(body: str) -> list[dict]:
    if re.search(r"doesn't produce any variables", body, re.I):
        return []
    section = extract_section(body, "Variables produced")
    if not section:
        return []
    rows = parse_table(section)
    items = []
    for row in rows:
        name = row.get("Argument") or row.get("Name") or ""
        if not name:
            continue
        items.append({"name": name, "type": row.get("Type", "")})
    return items


def parse_exceptions(body: str) -> list[str]:
    if re.search(r"doesn't include any exceptions", body, re.I):
        return []
    section = extract_section(body, "Exceptions")
    if not section:
        return []
    rows = parse_table(section)
    names = []
    for row in rows:
        name = row.get("Exception") or row.get("Argument") or ""
        if name:
            names.append(name)
    return names


def is_action_heading(level: int, anchor: str, title: str) -> bool:
    key = unescape(title).strip().lower()
    key = HTML_TAG_RE.sub("", key).strip().strip("`")
    if level >= 4:
        return False
    if key in SKIP_TITLES or key in SECTION_TITLES:
        return False
    if any(part in key for part in SKIP_TITLE_PARTS):
        return False
    if key.endswith(" exceptions"):
        return False
    if anchor.endswith("_onerror") or "_onerror" in anchor:
        return False
    if any(token in anchor for token in ("_builder", "_attachments")):
        return False
    if re.fullmatch(r"[a-z0-9_]+action", key):
        return False
    if anchor:
        return True
    # Unnamed headings: only H2 action titles (Throw custom error, Edge, work queues).
    return level == 2


def has_action_body(body: str) -> bool:
    has_inputs = bool(re.search(r"^#{2,6}\s+Input parameters\s*$", body, re.I | re.M))
    has_outputs = bool(re.search(r"^#{2,6}\s+Variables produced\s*$", body, re.I | re.M))
    no_input = bool(re.search(r"doesn't require any input", body, re.I))
    return has_inputs or no_input or has_outputs


def parse_action_file(path: Path) -> list[Action]:
    stem = path.stem
    text = path.read_text(encoding="utf-8")
    matches = list(HEADING_RE.finditer(text))
    parsed_heads: list[tuple[int, str, str, int, int]] = []
    for match in matches:
        level = len(match.group(1))
        anchor = match.group(2) or ""
        title = unescape(HTML_TAG_RE.sub("", match.group(3))).strip()
        parsed_heads.append((level, anchor, title, match.start(), match.end()))
    actions: list[Action] = []
    action_indexes = [
        i
        for i, (level, anchor, title, _s, _e) in enumerate(parsed_heads)
        if is_action_heading(level, anchor, title)
    ]
    for pos, index in enumerate(action_indexes):
        level, anchor, title, _start_line, start = parsed_heads[index]
        if pos + 1 < len(action_indexes):
            end = parsed_heads[action_indexes[pos + 1]][3]
        else:
            end = len(text)
        body = text[start:end]
        if not has_action_body(body):
            continue
        lead = first_sentence(body)
        purpose = purpose_from_name(title)
        # Prefer the name-based purpose; keep a short lead only if the
        # template fell back to a generic line and the lead is short.
        if purpose.startswith("Runs **") and lead and len(lead) < 180:
            purpose = lead.rstrip(".") + "."
        action_id = f"{stem}/{slug(title)}"
        learn = f"{LEARN_BASE}/{stem}"
        if anchor:
            learn = f"{learn}#{anchor}"
        actions.append(
            Action(
                id=action_id,
                name=title,
                module=stem,
                kind="native-action",
                purpose=purpose,
                anchor=anchor,
                inputs=parse_inputs(body),
                outputs=parse_outputs(body),
                exceptions=parse_exceptions(body),
                learn_url=learn,
                source_file=path.name,
            )
        )
    return actions


def parse_cheat_sheet_cloud(path: Path) -> list[Action]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    # Sections marked with ♦ are cloud connector groups in the cheat sheet.
    section_re = re.compile(r"^### (.+?) ♦\s*$", re.M)
    heading_re = re.compile(r"^### ", re.M)
    matches = list(section_re.finditer(text))
    mapping = {
        "SharePoint": "sharepoint",
        "Office 365 Outlook": "office365outlook",
        "Microsoft Teams": "microsoft-teams",
        "Microsoft Dataverse": "microsoft-dataverse",
        "Excel Online (Business)": "excel-online",
        "OneDrive": "onedrive",
        "OneDrive for Business": "onedrive-business",
        "OneNote (Business)": "onenote",
        "Word Online (Business)": "word-online",
        "Microsoft Forms": "microsoft-forms",
        "RSS": "rss",
        "Logging": None,  # native, skip
        "AI Builder": None,
        "Power Automate secret variables": None,
        "Work queues": None,
        "SAP automation - Advanced": None,
    }
    actions: list[Action] = []
    for index, match in enumerate(matches):
        raw_name = re.sub(r"\s+", " ", match.group(1)).strip()
        module = mapping.get(raw_name)
        if not module:
            continue
        start = match.end()
        nxt = heading_re.search(text, start)
        end = nxt.start() if nxt else len(text)
        block = text[start:end]
        # Pairs of | Name | then | --- | then | description |
        cells: list[str] = []
        for line in block.splitlines():
            cell_match = re.match(r"^\| (.+?) \|\s*$", line)
            if not cell_match:
                continue
            cell = clean_cell(cell_match.group(1))
            if not cell or set(cell) <= set("- "):
                continue
            cells.append(cell)
        for offset in range(0, len(cells) - 1, 2):
            name = cells[offset]
            if not name:
                continue
            actions.append(
                Action(
                    id=f"{module}/{slug(name)}",
                    name=name,
                    module=module,
                    kind="cloud-connector-operation",
                    purpose=purpose_from_name(name),
                    learn_url="",
                    source_file="cloud-connector-catalog",
                )
            )
    return actions


def extra_as_actions() -> list[Action]:
    out: list[Action] = []
    for item in EXTRA_ACTIONS:
        out.append(
            Action(
                id=item["id"],
                name=item["name"],
                module=item["module"],
                kind=item["kind"],
                purpose=item["purpose"],
                anchor=item.get("anchor", ""),
                inputs=item.get("inputs", []),
                outputs=item.get("outputs", []),
                exceptions=item.get("exceptions", []),
                learn_url=item.get("learn_url", ""),
                source_file="extra",
            )
        )
    return out


def fmt_inputs(inputs: list[dict]) -> str:
    if not inputs:
        return "None"
    parts = []
    for item in inputs:
        bit = f"`{item['name']}`"
        extra = []
        if item.get("accepts"):
            extra.append(item["accepts"])
        if item.get("optional") in {"Yes", "true", "True"}:
            extra.append("optional")
        if extra:
            bit += f" ({'; '.join(extra)})"
        parts.append(bit)
    return "; ".join(parts)


def fmt_outputs(outputs: list[dict]) -> str:
    if not outputs:
        return "None listed"
    parts = []
    for item in outputs:
        bit = f"`{item['name']}`"
        if item.get("type"):
            bit += f" ({item['type']})"
        parts.append(bit)
    return "; ".join(parts)


def write_module_doc(module: str, title: str, blurb: str, actions: list[Action], kind_label: str) -> None:
    lines = [
        f"# {title}",
        "",
        blurb,
        "",
        f"This page documents every **{kind_label}** in this group "
        f"({len(actions)} items).",
        "",
        "## Actions" if kind_label != "cloud connector operations" else "## Operations",
        "",
    ]
    for action in sorted(actions, key=lambda a: a.name.lower()):
        lines.append(f"### {action.name}")
        lines.append("")
        lines.append(f"- **Inventory id:** `{action.id}`")
        lines.append(f"- **Kind:** {action.kind}")
        lines.append(f"- **Purpose:** {action.purpose}")
        if action.inputs or action.kind == "native-action":
            lines.append(f"- **Key inputs:** {fmt_inputs(action.inputs)}")
            lines.append(f"- **Produces:** {fmt_outputs(action.outputs)}")
            if action.exceptions:
                lines.append(
                    "- **Exceptions:** "
                    + "; ".join(f"`{e}`" for e in action.exceptions)
                )
            else:
                lines.append("- **Exceptions:** none listed")
        if action.learn_url:
            lines.append(f"- **Microsoft Learn:** [{action.name}]({action.learn_url})")
        lines.append("")
    MODULES.mkdir(parents=True, exist_ok=True)
    (MODULES / f"{module}.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_inventory(native: list[Action], cloud: list[Action], extra: list[Action]) -> dict:
    fx_items = [
        {
            "id": f"power-fx/{slug(name)}",
            "name": name,
            "module": "power-fx",
            "kind": "power-fx-function",
            "category": category,
            "purpose": purpose,
            "learn_url": (
                "https://learn.microsoft.com/en-us/power-platform/"
                "power-fx/formula-reference-desktop-flows"
            ),
        }
        for name, category, purpose in POWER_FX
    ]
    designer = designer_items()
    data_types = data_type_items()
    native_all = native + extra
    payload = {
        "product": "Power Automate for desktop",
        "source": "Microsoft Learn action reference plus Power Fx formula reference",
        "counts": {
            "native_actions": len(native_all),
            "cloud_connector_operations": len(cloud),
            "power_fx_functions": len(fx_items),
            "designer_usable_items": len(designer),
            "data_types": len(data_types),
            "action_modules": len({a.module for a in native_all}),
        },
        "native_actions": [asdict(a) for a in sorted(native_all, key=lambda a: (a.module, a.name.lower()))],
        "cloud_connector_operations": [asdict(a) for a in sorted(cloud, key=lambda a: (a.module, a.name.lower()))],
        "power_fx_functions": fx_items,
        "designer_usable_items": designer,
        "data_types": data_types,
    }
    (DOCS / "inventory.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return payload


def designer_items() -> list[dict]:
    items = [
        ("Actions pane", "Left-side catalog of modules and actions, with search and favorites."),
        ("Workspace canvas", "Ordered list of deployed actions for the active subflow."),
        ("Subflows", "Tabs besides Main; invoke with Run subflow, including dynamic names."),
        ("Variables pane", "Input, output, and flow variables, including sensitive and optional flags."),
        ("UI elements pane", "Captured desktop and web elements plus their selectors."),
        ("UI element collections", "Reusable shared UI element sets across flows."),
        ("Images pane", "Captured bitmaps used by image-based mouse and wait actions."),
        ("Errors pane", "Design-time and run-time errors and warnings with line and subflow."),
        ("Action modal", "Inputs, produced variables, and On error handling for one action."),
        ("On error handling", "Retry, continue, throw, or go-to-label when an action fails."),
        ("Breakpoints", "Pause a designer run on a chosen action."),
        ("Run / Run from here / Step", "Designer debug controls for the current flow."),
        ("Desktop recorder", "Capture clicks and typing against desktop apps as UI actions."),
        ("Web recorder", "Capture browser interactions as web automation actions."),
        ("Copilot / natural language", "Describe a task in English to draft actions or Power Fx."),
        ("Assets library", "Add extra cloud connectors and custom actions to the pane."),
        ("Custom actions", "Environment-level .dll action groups uploaded by the organization."),
        ("Credentials", "Portal, Azure Key Vault, or CyberArk secrets resolved at runtime."),
        ("Connection references", "Cloud connector connections embedded or brought-your-own."),
        ("Environment variables", "Text, number, JSON, boolean, or secret values from the environment."),
        ("Work queues", "Orchestrated item processing across unattended machines."),
        ("Console - My flows", "Create, run, stop, and schedule desktop flows on this machine."),
        ("Console - examples", "Starter flows shipped with PAD."),
        ("Keyboard shortcut run", "Start a flow from a hotkey registered in the console."),
        ("URL / scheme run", "Start a flow from a PAD URL shortcut."),
        ("Machine registration", "Register this PC for attended or unattended cloud-initiated runs."),
        ("Machine groups", "Pool machines for unattended scale-out."),
        ("Hosted machines / groups", "Microsoft-hosted bots for unattended runs."),
        ("Flow designer menus", "Save, save as, undo/redo, find, comments, and enable/disable actions."),
        ("Safe stop", "Cooperative stop check via If safe stop requested."),
        ("Sensitive variables", "Mask values in logs and the variables viewer."),
        ("Input / output variables", "Contract used when a cloud flow or another desktop flow calls this flow."),
        ("Selectors", "Text-based (and repaired) locators behind UI and web elements."),
        ("Custom forms designer", "Layout used by Display custom form."),
        ("Power Fx toggle", "Per-flow choice of classic % expressions versus Power Fx."),
    ]
    return [
        {
            "id": f"designer/{slug(name)}",
            "name": name,
            "module": "designer",
            "kind": "usable-item",
            "purpose": purpose,
        }
        for name, purpose in items
    ]


def data_type_items() -> list[dict]:
    items = [
        ("Text value", "Any string, including paths and file contents."),
        ("Numeric value", "A number; the only type allowed in math expressions."),
        ("Boolean value", "True or False, often written `%True%` / `%False%`."),
        ("List", "Zero-based collection of items of a common type."),
        ("Datatable", "Rows and columns; like a two-dimensional array."),
        ("Datarow", "One row of a datatable, including For each current items."),
        ("Custom object", "Property/value map, JSON-serializable."),
        ("Connector object", "Structured result from a cloud connector operation."),
        ("General value", "Design-time unknown type; resolved at runtime."),
        ("File", "A file on disk."),
        ("Folder", "A folder on disk."),
        ("FileSystemObject", "Either a file or a folder."),
        ("Datetime", "Date and time, including `%d\"yyyy-MM-dd HH:mm:ss\"%` literals."),
        ("SensitiveValue", "Masked text such as passwords and secret environment variables."),
        ("Credential", "Username/password (or similar) from Get credential."),
        ("Web browser instance", "Chrome, Edge, Firefox, or IE session."),
        ("Window instance", "A desktop window from Get window."),
        ("Excel instance", "A running Excel workbook from Launch/Attach Excel."),
        ("Word instance", "A running Word document from Launch/Attach Word."),
        ("Outlook instance", "A running Outlook profile from Launch Outlook."),
        ("Access instance", "A running Access database from Launch Access."),
        ("SQL connection", "Open database session."),
        ("Exchange connection", "Open Exchange session."),
        ("FTP connection", "Open FTP or secure FTP session."),
        ("CMD session", "Open Command Prompt session."),
        ("Terminal session", "Open terminal emulator session."),
        ("OCR Engine", "Windows OCR or Tesseract engine object."),
        ("XML node", "Loaded XML document or fragment."),
        ("Mail message", "IMAP/SMTP message from Retrieve email messages."),
        ("Outlook mail message", "Message from Retrieve email messages from Outlook."),
        ("Exchange mail message", "Message from Retrieve Exchange email messages."),
        ("Error", "Last error object from Get last error."),
        ("Active Directory entry", "AD server connection."),
        ("Group info / Group member / User info", "AD group and user records."),
        ("EC2 client / instance / volume / snapshot", "AWS automation objects."),
        ("Azure client / VM / disk / snapshot / subscription / resource group", "Azure automation objects."),
        ("FTP file / FTP directory", "Remote FTP items."),
        ("List of PDF table info", "Tables extracted from a PDF, with page metadata."),
        ("TriggerEventInstanceHandle", "Handle raised by a UI element event trigger."),
    ]
    return [
        {
            "id": f"data-type/{slug(name)}",
            "name": name,
            "module": "data-types",
            "kind": "data-type",
            "purpose": purpose,
        }
        for name, purpose in items
    ]


def write_inventory_markdown(payload: dict) -> None:
    counts = payload["counts"]
    lines = [
        "# Power Automate Desktop inventory",
        "",
        "This is **step 1**: a complete catalog of usable items in Power Automate for desktop (PAD). "
        "Each native action and Power Fx function is documented on its module page.",
        "",
        "## Counts",
        "",
        f"- Native designer actions: **{counts['native_actions']}**",
        f"- Cloud connector operations (default pane set): **{counts['cloud_connector_operations']}**",
        f"- Power Fx functions (Power Fx–enabled flows): **{counts['power_fx_functions']}**",
        f"- Designer / console usable items: **{counts['designer_usable_items']}**",
        f"- Variable data types: **{counts['data_types']}**",
        f"- Native action modules: **{counts['action_modules']}**",
        "",
        "Machine-readable copy: [`inventory.json`](inventory.json).",
        "",
        "## How PAD is organized",
        "",
        "1. **Designer surfaces** — panes, recorders, variables, UI elements, images, errors.",
        "2. **Native actions** — modules in the actions pane (Variables, Excel, UI automation, …).",
        "3. **Cloud connectors** — the same operations as cloud flows, run inside PAD.",
        "4. **Power Fx functions** — formula language when the flow is Power Fx–enabled.",
        "5. **Data types** — values that variables and action outputs hold.",
        "",
        "## Native action modules",
        "",
        "| Module | Items | Documentation |",
        "| --- | ---: | --- |",
    ]
    by_mod: dict[str, list] = defaultdict(list)
    for raw in payload["native_actions"]:
        by_mod[raw["module"]].append(raw)
    for module in sorted(by_mod, key=lambda m: MODULE_META.get(m, (m, ""))[0].lower()):
        title = MODULE_META.get(module, (module, ""))[0]
        n = len(by_mod[module])
        lines.append(f"| {title} | {n} | [{module}.md](modules/{module}.md) |")
    lines += [
        "",
        "## Native actions (complete list)",
        "",
        "| Action | Module | Purpose |",
        "| --- | --- | --- |",
    ]
    for raw in payload["native_actions"]:
        title = MODULE_META.get(raw["module"], (raw["module"], ""))[0]
        purpose = raw["purpose"].replace("|", "\\|")
        link = f"modules/{raw['module']}.md#{slug(raw['name'])}"
        lines.append(f"| [{raw['name']}]({link}) | {title} | {purpose} |")
    lines += [
        "",
        "## Default cloud connectors",
        "",
        "| Operation | Connector | Purpose |",
        "| --- | --- | --- |",
    ]
    for raw in payload["cloud_connector_operations"]:
        title = CLOUD_CONNECTOR_META.get(raw["module"], (raw["module"], ""))[0]
        purpose = raw["purpose"].replace("|", "\\|")
        link = f"modules/{raw['module']}.md#{slug(raw['name'])}"
        lines.append(f"| [{raw['name']}]({link}) | {title} | {purpose} |")
    lines += [
        "",
        "## Power Fx functions",
        "",
        "Used only in **Power Fx–enabled** desktop flows. Expressions start with `=`. "
        "Indexes are **1-based**. See [Power Fx functions](03-power-fx-functions.md).",
        "",
        "| Function | Category | Purpose |",
        "| --- | --- | --- |",
    ]
    for raw in payload["power_fx_functions"]:
        lines.append(
            f"| [{raw['name']}](03-power-fx-functions.md#{slug(raw['name'])}) | {raw['category']} | {raw['purpose']} |"
        )
    lines += [
        "",
        "## Designer and console items",
        "",
        "See [Designer usable items](01-designer-usable-items.md).",
        "",
        "| Item | Purpose |",
        "| --- | --- |",
    ]
    for raw in payload["designer_usable_items"]:
        lines.append(f"| {raw['name']} | {raw['purpose']} |")
    lines += [
        "",
        "## Data types",
        "",
        "See [Variable data types](02-data-types.md).",
        "",
        "| Type | Purpose |",
        "| --- | --- |",
    ]
    for raw in payload["data_types"]:
        lines.append(f"| {raw['name']} | {raw['purpose']} |")
    lines.append("")
    (DOCS / "00-inventory.md").write_text("\n".join(lines), encoding="utf-8")


def write_power_fx_doc() -> None:
    lines = [
        "# Power Fx functions in desktop flows",
        "",
        "These functions are available when a desktop flow is **Power Fx–enabled**. "
        "Type `=` in an input to start a formula. Variable names are case-sensitive. "
        "`Index` is **1-based** (unlike classic `%List[0]%` indexing).",
        "",
        "Classic flows keep the `%Expression%` language instead of this list.",
        "",
        "Official catalog: [Formula reference - desktop flows]("
        "https://learn.microsoft.com/en-us/power-platform/power-fx/formula-reference-desktop-flows).",
        "",
        "## Functions",
        "",
    ]
    by_cat: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for name, category, purpose in POWER_FX:
        by_cat[category].append((name, purpose))
    for category in sorted(by_cat):
        lines.append(f"## {category}")
        lines.append("")
        for name, purpose in sorted(by_cat[category], key=lambda x: x[0].lower()):
            lines.append(f"### {name}")
            lines.append("")
            lines.append(f"- **Kind:** power-fx-function")
            lines.append(f"- **Purpose:** {purpose}")
            lines.append(f"- **Example shape:** `={name}(...)`")
            lines.append("")
        lines.append("")
    (DOCS / "03-power-fx-functions.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else SOURCE_DEFAULT
    if not source.exists():
        print(f"Action reference folder not found: {source}", file=sys.stderr)
        return 1
    DOCS.mkdir(parents=True, exist_ok=True)
    MODULES.mkdir(parents=True, exist_ok=True)

    native: list[Action] = []
    for path in sorted(source.glob("*.md")):
        if path.name in SKIP_FILES:
            continue
        native.extend(parse_action_file(path))

    extra = extra_as_actions()
    cloud = parse_cheat_sheet_cloud(CHEAT_SHEET)
    cloud_json = DOCS / "_source" / "cloud_connector_operations.json"
    if not cloud and cloud_json.exists():
        raw = json.loads(cloud_json.read_text(encoding="utf-8"))
        cloud = [
            Action(
                id=f"{item['module']}/{slug(item['name'])}",
                name=item["name"],
                module=item["module"],
                kind="cloud-connector-operation",
                purpose=purpose_from_name(item["name"]),
                source_file="cloud-connector-catalog",
            )
            for item in raw
        ]

    # De-duplicate native by id, keep first
    seen: set[str] = set()
    unique_native: list[Action] = []
    for action in native + extra:
        if action.id in seen:
            continue
        seen.add(action.id)
        unique_native.append(action)

    seen_cloud: set[str] = set()
    unique_cloud: list[Action] = []
    for action in cloud:
        if action.id in seen_cloud:
            continue
        seen_cloud.add(action.id)
        unique_cloud.append(action)

    source_dir = DOCS / "_source"
    source_dir.mkdir(parents=True, exist_ok=True)
    (source_dir / "cloud_connector_operations.json").write_text(
        json.dumps(
            [{"module": a.module, "name": a.name} for a in unique_cloud],
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    payload = write_inventory(unique_native, unique_cloud, [])
    write_inventory_markdown(payload)
    write_power_fx_doc()

    grouped: dict[str, list[Action]] = defaultdict(list)
    for action in unique_native:
        grouped[action.module].append(action)
    for module, actions in grouped.items():
        title, blurb = MODULE_META.get(module, (module, "Native PAD actions in this group."))
        write_module_doc(module, title, blurb, actions, "native action")

    cloud_grouped: dict[str, list[Action]] = defaultdict(list)
    for action in unique_cloud:
        cloud_grouped[action.module].append(action)
    for module, actions in cloud_grouped.items():
        title, blurb = CLOUD_CONNECTOR_META.get(
            module, (module, "Cloud connector operations in the PAD actions pane.")
        )
        write_module_doc(module, title, blurb, actions, "cloud connector operations")

    # Overview stubs that have no parsed actions
    write_module_doc(
        "custom-actions",
        "Custom actions",
        MODULE_META["custom-actions"][1],
        [],
        "native action",
    )
    write_module_doc(
        "cloud-connectors",
        "Cloud connectors",
        MODULE_META["cloud-connectors"][1]
        + " Default connectors are always visible. Add more from the Assets library. "
        "Pass files as binary data (`Convert file to binary data` / `Convert binary data to file`).",
        [],
        "native action",
    )

    print(
        json.dumps(
            {
                "native_actions": len(unique_native),
                "cloud_connector_operations": len(unique_cloud),
                "power_fx": len(POWER_FX),
                "modules_written": len(grouped) + len(cloud_grouped),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
