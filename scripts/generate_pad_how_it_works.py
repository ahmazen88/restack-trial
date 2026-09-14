#!/usr/bin/env python3
"""Build use-case / demonstration / analogy pages for every PAD item.

Reads docs/power-automate-desktop/inventory.json (no Microsoft clone required).
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "power-automate-desktop"
OUT = DOCS / "how-it-works"
INVENTORY = DOCS / "inventory.json"

MODULE_TITLE = {
    "access": "Access",
    "activedirectory": "Active Directory",
    "aibuilder": "AI Builder (preview)",
    "aws": "AWS",
    "azure": "Azure",
    "clipboard": "Clipboard",
    "cmd": "CMD session",
    "compression": "Compression",
    "conditionals": "Conditionals",
    "cryptography": "Cryptography",
    "cyberark": "CyberArk",
    "database": "Database",
    "datetime": "Date time",
    "display": "Message boxes",
    "email": "Email",
    "excel": "Excel",
    "exchange": "Exchange Server",
    "file": "File",
    "flowcontrol": "Flow control",
    "folder": "Folder",
    "ftp": "FTP",
    "googlecognitive": "Google Cognitive",
    "ibmcognitive": "IBM Cognitive",
    "logging": "Logging",
    "loops": "Loops",
    "microsoftcognitive": "Microsoft Cognitive",
    "mouseandkeyboard": "Mouse and keyboard",
    "ocr": "OCR",
    "outlook": "Outlook",
    "pdf": "PDF",
    "powerautomateenvironment": "Power Automate environment",
    "powerautomatesecretvariables": "Power Automate secret variables",
    "runflow": "Run flow",
    "sap": "SAP automation",
    "scripting": "Scripting",
    "services": "Windows services",
    "system": "System",
    "terminalemulation": "Terminal emulation",
    "testing": "Testing",
    "text": "Text",
    "uiautomation": "UI automation",
    "variables": "Variables",
    "web": "HTTP",
    "webautomation": "Browser automation",
    "word": "Word",
    "workqueues": "Work queues",
    "workstation": "Workstation",
    "xml": "XML",
    "triggers": "Triggers",
    "power-platform": "Power Platform",
    "sharepoint": "SharePoint (cloud)",
    "office365outlook": "Office 365 Outlook (cloud)",
    "microsoft-teams": "Microsoft Teams (cloud)",
    "microsoft-dataverse": "Microsoft Dataverse (cloud)",
    "excel-online": "Excel Online (cloud)",
    "onedrive": "OneDrive (cloud)",
    "onedrive-business": "OneDrive for work or school (cloud)",
    "onenote": "OneNote (cloud)",
    "word-online": "Word Online (cloud)",
    "microsoft-forms": "Microsoft Forms (cloud)",
    "rss": "RSS (cloud)",
    "power-fx": "Power Fx",
    "designer": "Designer and console",
    "data-types": "Data types",
}

# Workplace "world" used to make each use case concrete.
CONTEXT = {
    "access": (
        "claims database on a shared drive",
        "opening a locked filing cabinet, working the folders, then shutting the drawer",
        "Launch Access first; Close Access when the query work is done so the .accdb file is not left locked.",
    ),
    "activedirectory": (
        "employee joiners and leavers",
        "the office key-cabinet: connect, change who has a key, then lock it",
        "Connect to server, do the user/group change, Close connection.",
    ),
    "aibuilder": (
        "drafting a customer reply that a human must approve",
        "asking an intern to draft a letter, then reading it before it is sent",
        "Follow with Display message or Display input dialog so a person reviews the GPT text.",
    ),
    "aws": (
        "non-prod EC2 boxes used for month-end jobs",
        "a warehouse of rented machines you start, snapshot, and shut down",
        "Create EC2 session, act on instances/volumes, End EC2 session.",
    ),
    "azure": (
        "a test VM that must be running only during the bot window",
        "borrowing a company laptop from a locker, using it, putting it back",
        "Create session, start or stop the VM, End session.",
    ),
    "clipboard": (
        "a hand-off between two apps that have no API",
        "a sticky note you write, carry, then throw away",
        "Copy with Get/Set clipboard; Clear clipboard contents when the secret should not linger.",
    ),
    "cmd": (
        "a legacy CLI tool the business still runs overnight",
        "dictating commands to a clerk at a terminal and waiting for the printout",
        "Open CMD session, Write/Wait/Read, Close CMD session.",
    ),
    "compression": (
        "packing a day's invoices to email or archive",
        "a packing box and a box cutter",
        "ZIP files before send; Unzip files after download.",
    ),
    "conditionals": (
        "a batch that must follow different paths for empty vs loaded folders",
        "a fork in a corridor: you only walk the left hall if the sign says so",
        "Pair If/Else if/Else, or Switch with Case and Default case, and close with End.",
    ),
    "cryptography": (
        "protecting a file drop that leaves the building",
        "a sealed envelope versus a signed receipt",
        "Encrypt before you copy off-box; Decrypt only on the trusted machine.",
    ),
    "cyberark": (
        "a password you must not store in the flow",
        "asking the vault clerk for a key, using it, never copying it to a notebook",
        "Get password from CyberArk, then pass the sensitive value into Launch or HTTP actions.",
    ),
    "database": (
        "reading open orders from SQL Server",
        "calling the warehouse on a dedicated phone line, asking a question, hanging up",
        "Open SQL connection, Execute SQL statement, Close SQL connection.",
    ),
    "datetime": (
        "stamping a filename or aging a queue item",
        "a wall clock and a desk calendar",
        "Get current date and time, then Add to datetime or Subtract dates as needed.",
    ),
    "display": (
        "an attended bot that must ask a person which file to use",
        "tapping a coworker on the shoulder and waiting for an answer",
        "Use Display select file/folder or Display message, then branch on the result.",
    ),
    "email": (
        "IMAP/SMTP mailbox without a local Outlook profile",
        "a post-office box you unlock with a key",
        "Retrieve email messages, Process or Send email, no Outlook instance required.",
    ),
    "excel": (
        "the monthly close workbook",
        "opening a paper ledger, writing lines, closing the book",
        "Launch Excel or Attach to running Excel, then read/write, then Save Excel and Close Excel.",
    ),
    "exchange": (
        "a shared mailbox on Exchange when Outlook is not installed",
        "the building mailroom instead of your personal inbox tray",
        "Connect to Exchange server, retrieve or send, then process messages.",
    ),
    "file": (
        "PDFs and CSVs landing in a watch folder",
        "a filing cabinet: copy, rename, read, or shred a single folder of papers",
        "If file exists or Wait for file, then copy/move/read; convert to binary before cloud connectors.",
    ),
    "flowcontrol": (
        "a long flow that must pause, jump, or fail in a controlled way",
        "stage directions in a play: wait, jump to a scene, or stop the show",
        "Use Wait, Label/Go to, Run subflow, On block error, and Stop flow together.",
    ),
    "folder": (
        "today's drop folder under C:\\Input",
        "a desk inbox tray and the drawers under it",
        "Get files in folder, then loop; Create/Empty/Move folder around the batch.",
    ),
    "ftp": (
        "a vendor SFTP drop that still has no API",
        "a loading dock: open the gate, drop pallets, close the gate",
        "Open FTP or secure FTP connection, transfer, Close connection.",
    ),
    "googlecognitive": (
        "classifying a scanned image the UI cannot read",
        "asking an outside specialist to look at a photo",
        "Call the vision or language action, then branch on the returned JSON/text.",
    ),
    "ibmcognitive": (
        "translating a vendor PDF extract",
        "sending a paragraph to a translation desk and getting it back",
        "Run Identify language or Translate, then write the result to Excel or a file.",
    ),
    "logging": (
        "audit text in the portal run history",
        "writing a line in the shift log so the next operator can see it",
        "Log message at Info/Warning/Error after each business milestone.",
    ),
    "loops": (
        "one CSV row or one file at a time",
        "walking a stack of envelopes and doing the same stamp on each",
        "For each over a list/table, Loop for a count, Loop condition until done; Exit loop to bail out.",
    ),
    "microsoftcognitive": (
        "OCR or sentiment on a document image",
        "a specialist who reads a page and returns notes",
        "Call Analyze image / OCR / Sentiment, then store the text in a variable.",
    ),
    "mouseandkeyboard": (
        "an app with no usable UI selectors",
        "moving your own hand and typing as if you sat at the PC",
        "Block Input in unattended runs, Move mouse / Send keys, then unblock by ending the action.",
    ),
    "ocr": (
        "text painted on a screen the UI tree cannot see",
        "reading a shop window with your eyes instead of asking the cashier",
        "If text on screen (OCR) or Extract text with OCR after an image or window is visible.",
    ),
    "outlook": (
        "the local Outlook profile on the bot PC",
        "your physical inbox tray on the desk",
        "Launch Outlook, Retrieve/Send/Process, Close Outlook.",
    ),
    "pdf": (
        "vendor invoices that arrive as PDF only",
        "photocopying a contract, cutting out the table, stacking the pages",
        "Extract text or tables, then write Excel or a file; Merge PDF files at the end of the day.",
    ),
    "powerautomateenvironment": (
        "a path or flag that changes per DEV/TEST/PROD",
        "a labeled switch on the wall for this office, not hardcoded in the script",
        "Retrieve environment variable at the start of Main and reuse the value.",
    ),
    "powerautomatesecretvariables": (
        "a service account password stored as a credential",
        "a sealed envelope in the safe, opened only when the door is locked",
        "Get credential, then pass Username/Password into Launch, HTTP, or SAP.",
    ),
    "runflow": (
        "reusing a tested child desktop flow",
        "handing a whole job to another trained clerk and waiting for their folder back",
        "Run desktop flow and map input/output variables.",
    ),
    "sap": (
        "posting a document in SAP GUI",
        "a green-screen clerk: log in, run a transaction, type, leave",
        "Launch SAP, Start SAP transaction, populate/click, End SAP transaction, Close SAP connection.",
    ),
    "scripting": (
        "a one-liner PowerShell or Python cannot express as PAD actions",
        "stepping into a side workshop for a custom tool, then returning with the part",
        "Run PowerShell/Python/.NET and capture output variables; keep scripts short.",
    ),
    "services": (
        "a Windows service the bot depends on",
        "checking whether the building boiler is running before you heat the office",
        "If service / Wait for service, then Start or Stop service.",
    ),
    "system": (
        "starting a local EXE or killing a hung process",
        "launching a program from the Start menu or ending it in Task Manager",
        "Run application, Wait for process, Terminate process if it hangs.",
    ),
    "terminalemulation": (
        "an AS/400 or mainframe screen",
        "a typewriter conversation: move the carriage, type, wait for the reply",
        "Open terminal session, Wait for text, Set text / Send key, Close terminal session.",
    ),
    "testing": (
        "a regression pack for a desktop flow",
        "a quiz at the end of a drill: expected answer versus what the student wrote",
        "Test a desktop flow, then Assert on outputs.",
    ),
    "text": (
        "cleaning a filename, invoice number, or CSV line",
        "scissors, tape, and a stamp for words",
        "Parse/Replace/Split/Join text before writing to Excel or a file.",
    ),
    "uiautomation": (
        "a Windows app with no API",
        "a person who can see buttons and type into boxes on a window",
        "Get window, populate/click UI elements, Wait for window content, Close window.",
    ),
    "variables": (
        "lists, tables, JSON, and counters the rest of the flow shares",
        "labeled jars on a workbench you fill, sort, and pour from",
        "Set variable to start; list and data table actions reshape data between Excel/files/HTTP.",
    ),
    "web": (
        "a REST or SOAP API the website already offers",
        "phoning a switchboard instead of walking into the shop",
        "Invoke web service or Download from web; convert files to binary when attaching.",
    ),
    "webautomation": (
        "a web portal with no stable API",
        "a clerk using Chrome at a desk: open, wait, type, copy, close",
        "Launch Chrome/Edge/Firefox, Wait for web page content, extract or fill, Close web browser.",
    ),
    "word": (
        "a letter or contract template on disk",
        "rolling a sheet into a typewriter, typing, pulling it out",
        "Launch Word, Write or Find and replace, Save Word, Close Word.",
    ),
    "workqueues": (
        "many unattended machines sharing one pile of work",
        "a ticket dispenser: take a ticket, do the job, mark it done or return it",
        "Add work queue item (producer), Process work queue items (consumer), Update work queue item.",
    ),
    "workstation": (
        "the physical PC the bot sits on",
        "the room itself: lights, camera, lock, printer",
        "Take screenshot on failure; Set screen resolution for unattended UI; avoid Shutdown in shared VMs unless intended.",
    ),
    "xml": (
        "a vendor XML invoice",
        "a nested set of labeled folders you open with a map (XPath)",
        "Read XML from file, Execute XPath expression, Write XML to file.",
    ),
    "triggers": (
        "starting nested steps when a user clicks a control",
        "a doorbell: the house stays quiet until someone presses it",
        "UI element event trigger wraps the actions that should run after the click or key.",
    ),
    "power-platform": (
        "an attended form that is nicer than Display custom form",
        "handing the customer a tablet app, then taking the filled clipboard back",
        "Run Power App, pass inputs, read outputs when the user closes the app.",
    ),
    "sharepoint": (
        "files that live in a team library, not on the bot disk",
        "the office library: check out a binder, copy pages, put it back",
        "Get file content using path, Convert binary data to file locally, then Excel/PDF actions.",
    ),
    "office365outlook": (
        "mailbox work without a local Outlook install",
        "webmail at the counter instead of the tray on your desk",
        "Convert file to binary data before Send an email (V2) attachments.",
    ),
    "microsoft-teams": (
        "notifying a channel when a bot finishes or fails",
        "leaning into the team room and saying the job is done",
        "Post message in a chat or channel after Stop flow or On block error.",
    ),
    "microsoft-dataverse": (
        "rows in Dataverse the cloud team already uses",
        "the official company register instead of a side spreadsheet",
        "List rows or Get a row by ID, then Update/Add a row in the same environment.",
    ),
    "excel-online": (
        "a workbook in OneDrive/SharePoint, not a local Excel.exe",
        "editing the shared Google-style sheet in the browser, but through Excel Online",
        "List rows present in a table, then Add/Update a row; no Launch Excel instance.",
    ),
    "onedrive": (
        "personal OneDrive files",
        "your own locker at work",
        "Get file content using path, convert binary to a local file, process, upload back.",
    ),
    "onedrive-business": (
        "work OneDrive files",
        "your assigned cabinet in the company records room",
        "Same pattern as OneDrive: content as binary, local convert, then native File/Excel.",
    ),
    "onenote": (
        "run notes a human reads later",
        "a lab notebook on the shelf",
        "Create page in a section with the run summary after Log message.",
    ),
    "word-online": (
        "filling a Word template stored in the cloud",
        "a mail-merge without opening Word on the PC",
        "Populate a Microsoft Word template, then Convert Word Document to PDF.",
    ),
    "microsoft-forms": (
        "a Form response the bot must file",
        "reading one filled survey card",
        "Get response details, then write fields to Excel or Dataverse.",
    ),
    "rss": (
        "a public feed the business still watches",
        "skimming the morning newspaper headlines",
        "List all RSS feed items, then loop and filter with text/date actions.",
    ),
    "power-fx": (
        "a Power Fx–enabled flow",
        "an Excel-style calculator button inside an `=` formula",
        "Nest in If / Filter / With; write the result with Excel, File, or Set.",
    ),
    "designer": (
        "building or running the flow rather than a single action card",
        "the workshop benches and lights, not a single wrench",
        "Use these surfaces while you place the actions in the combination playbooks.",
    ),
    "data-types": (
        "choosing or reading a variable's shape",
        "the shape of the jar, not the tool that fills it",
        "Match the type an action produces to the type the next action accepts.",
    ),
}

SPECIAL_USE = {
    "Set variable": "Keep a path, counter, flag, or JSON blob that later actions and % expressions will read.",
    "If": "Run one branch when a check is true (file exists, row count > 0, status = 'Open').",
    "For each": "Repeat the same nested actions once per file, list item, or data-table row.",
    "Launch Excel": "Open or create the workbook every later Excel action will share as ExcelInstance.",
    "Launch new Chrome": "Start the browser session that all web actions on this site will reuse.",
    "Click UI element in window": "Press a real button in a desktop app when selectors are available.",
    "Invoke web service": "Call a REST API instead of clicking the website, when the API exists.",
    "Get credential": "Resolve a stored username/password at runtime instead of hard-coding secrets.",
    "On block error": "Catch failures from a group of actions and email, log, or retry instead of dying.",
    "Run subflow": "Call a named slice of this flow (Extract, Transform, Load) without copy-paste.",
    "Process work queue items": "Pull the next ticket so several machines can share one backlog.",
    "Display message": "Stop an attended run and tell the person what happened or what to do next.",
    "Extract text from PDF": "Turn an invoice PDF into text you can Parse text and write to Excel.",
    "Convert file to binary data": "Required before most cloud connector upload/attach parameters.",
    "Convert binary data to file": "Required after cloud connector download before Excel/PDF/File actions.",
}

SPECIAL_ANALOGY = {
    "Set variable": "Writing a name on a jar, then putting something in it.",
    "If": "Looking at a traffic light before you cross.",
    "Else": "The other road when the light is red.",
    "For each": "Stamping every envelope in a stack, one after another.",
    "Loop": "Doing ten push-ups because someone said 'ten', not because the list ended.",
    "Wait": "Setting a kitchen timer and not touching the next step until it rings.",
    "Launch Excel": "Opening the ledger so a pen can write in it.",
    "Close Excel": "Closing the ledger so nobody else trips over an open book.",
    "Launch new Chrome": "Sitting down at a computer and opening the browser.",
    "Close web browser": "Logging off that browser so the next job starts clean.",
    "Click UI element in window": "Pressing a labeled button with your finger.",
    "Populate text field in window": "Filling a paper form field with a pen.",
    "Get clipboard text": "Reading whatever is currently on the sticky note.",
    "Set clipboard Text": "Replacing the sticky note with a new one.",
    "On block error": "A safety net under a trapeze act.",
    "Throw custom error": "Pulling the fire alarm on purpose so the net can catch it.",
    "Get credential": "Asking the safe for the key instead of taping the key to the script.",
    "Log message": "Writing a line in the shift diary.",
    "Assert": "The teacher checking the answer key.",
}

FX_DEMO = {
    "Abs": "=Abs(InvoiceVariance)",
    "Acos": "=Acos(0.5)",
    "Acot": "=Acot(1)",
    "AddColumns": '=AddColumns(Orders, "Tax", Amount * 0.2)',
    "And": '=And(Amount > 0, Status = "Open")',
    "Asin": "=Asin(0.5)",
    "Atan": "=Atan(1)",
    "Atan2": "=Atan2(1, 1)",
    "Average": "=Average(AmountColumn)",
    "Blank": "=Blank()",
    "Boolean": '=Boolean("true")',
    "Char": "=Char(65)",
    "Clear": "=Clear(Scratch)",
    "ClearCollect": "=ClearCollect(Scratch, FilteredRows)",
    "Coalesce": '=Coalesce(PreferredEmail, BackupEmail, "unknown")',
    "Collect": "=Collect(Results, CurrentRow)",
    "Concat": '=Concat(Names, Value & ", ")',
    "Concatenate": '=Concatenate(FirstName, " ", LastName)',
    "Cos": "=Cos(Radians(60))",
    "Cot": "=Cot(Radians(45))",
    "Count": "=Count(AmountColumn)",
    "CountA": "=CountA(NameColumn)",
    "CountIf": '=CountIf(Orders, Status = "Open")',
    "CountRows": "=CountRows(Orders)",
    "Date": "=Date(2026, 9, 14)",
    "DateAdd": '=DateAdd(Today(), 7, TimeUnit.Days)',
    "DateDiff": "=DateDiff(StartDate, EndDate)",
    "DateTime": "=DateTime(2026, 9, 14, 9, 30, 0)",
    "DateTimeValue": '=DateTimeValue("2026-09-14 09:30")',
    "DateValue": '=DateValue("2026-09-14")',
    "Day": "=Day(Today())",
    "Dec2Hex": "=Dec2Hex(255)",
    "Decimal": '=Decimal("19.50")',
    "Degrees": "=Degrees(Pi()/2)",
    "Distinct": "=Distinct(Orders, Customer)",
    "DropColumns": '=DropColumns(Orders, "InternalId")',
    "EDate": "=EDate(Today(), 1)",
    "EncodeHTML": "=EncodeHTML(RawComment)",
    "EncodeUrl": "=EncodeUrl(SearchTerm)",
    "EndsWith": '=EndsWith(FileName, ".pdf")',
    "EOMonth": "=EOMonth(Today(), 0)",
    "Error": '=Error("Row is missing Amount")',
    "Exp": "=Exp(1)",
    "Filter": '=Filter(Orders, Status = "Open")',
    "Find": '=Find("INV-", InvoiceText)',
    "First": "=First(Orders)",
    "FirstN": "=FirstN(Orders, 10)",
    "Float": '=Float("3.14")',
    "ForAll": "=ForAll(Orders, Amount * 1.2)",
    "GUID": "=GUID()",
    "Hex2Dec": '=Hex2Dec("FF")',
    "Hour": "=Hour(Now())",
    "If": '=If(Amount > 0, "OK", "Missing")',
    "IfError": '=IfError(Value(RawAmount), 0)',
    "Index": "=Index(Orders, 1)",
    "Int": "=Int(19.8)",
    "IsBlank": "=IsBlank(CustomerName)",
    "IsBlankOrError": "=IsBlankOrError(LookedUpRow)",
    "IsEmpty": "=IsEmpty(Orders)",
    "IsError": "=IsError(Value(RawAmount))",
    "IsNumeric": "=IsNumeric(RawAmount)",
    "IsToday": "=IsToday(DueDate)",
    "Language": "=Language()",
    "Last": "=Last(Orders)",
    "LastN": "=LastN(Orders, 5)",
    "Left": "=Left(AccountCode, 3)",
    "Len": "=Len(CustomerName)",
    "Ln": "=Ln(10)",
    "Log": "=Log(100, 10)",
    "LookUp": '=LookUp(Orders, OrderId = TargetId)',
    "Lower": "=Lower(EmailAddress)",
    "Max": "=Max(AmountColumn)",
    "Mid": "=Mid(AccountCode, 4, 2)",
    "Min": "=Min(AmountColumn)",
    "Minute": "=Minute(Now())",
    "Mod": "=Mod(RowNumber, 2)",
    "Month": "=Month(Today())",
    "Not": "=Not(IsEmpty(Orders))",
    "Now": "=Now()",
    "Or": '=Or(Status = "Open", Status = "Held")',
    "Patch": "=Patch(Orders, First(Orders), {Status: \"Posted\"})",
    "Pi": "=Pi()",
    "PlainText": "=PlainText(HtmlBody)",
    "Power": "=Power(2, 8)",
    "Proper": "=Proper(CustomerName)",
    "Radians": "=Radians(180)",
    "Rand": "=Rand()",
    "RandBetween": "=RandBetween(1, 6)",
    "Remove": "=Remove(Scratch, First(Scratch))",
    "RenameColumns": '=RenameColumns(Orders, "Amt", "Amount")',
    "Replace": '=Replace(AccountCode, 1, 3, "XX-")',
    "Right": "=Right(FileName, 4)",
    "Round": "=Round(Amount, 2)",
    "RoundDown": "=RoundDown(Amount, 0)",
    "RoundUp": "=RoundUp(Amount, 0)",
    "Search": '=Search(Orders, "acme", "Customer")',
    "Second": "=Second(Now())",
    "Sequence": "=Sequence(10)",
    "Set": "=Set(Index(Scratch, 1), 42)",
    "ShowColumns": '=ShowColumns(Orders, "OrderId", "Amount")',
    "Shuffle": "=Shuffle(Orders)",
    "Sin": "=Sin(Radians(30))",
    "Sort": "=Sort(Orders, Amount, Descending)",
    "SortByColumns": '=SortByColumns(Orders, "Customer")',
    "Split": '=Split(FileName, ".")',
    "Sqrt": "=Sqrt(9)",
    "StartsWith": '=StartsWith(InvoiceNumber, "INV")',
    "StdevP": "=StdevP(AmountColumn)",
    "Substitute": '=Substitute(FileName, " ", "_")',
    "Sum": "=Sum(Orders, Amount)",
    "Summarize": '=Summarize(Orders, Customer, "Total", Sum(Amount))',
    "Switch": '=Switch(Status, "Open", 1, "Closed", 2, 0)',
    "Table": '=Table({Name: "Ada", Amount: 10})',
    "Tan": "=Tan(Radians(45))",
    "Text": '=Text(Today(), "yyyy-mm-dd")',
    "Time": "=Time(9, 30, 0)",
    "TimeValue": '=TimeValue("09:30")',
    "TimeZoneOffset": "=TimeZoneOffset()",
    "Today": "=Today()",
    "Trim": "=Trim(CustomerName)",
    "TrimEnds": "=TrimEnds(CustomerName)",
    "Trunc": "=Trunc(19.8)",
    "UniChar": "=UniChar(9731)",
    "Upper": "=Upper(CountryCode)",
    "Value": '=Value("19.50")',
    "VarP": "=VarP(AmountColumn)",
    "Weekday": "=Weekday(Today())",
    "WeekNum": "=WeekNum(Today())",
    "With": '=With({Rate: 0.2}, Amount * Rate)',
    "Year": "=Year(Today())",
}


def slug(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def lower_first(text: str) -> str:
    text = (text or "").strip()
    if not text:
        return text
    if text[:1].isupper() and (len(text) == 1 or not text[1:2].isupper()):
        return text[0].lower() + text[1:]
    return text


def context(module: str) -> tuple[str, str, str]:
    return CONTEXT.get(
        module,
        (
            "this automation",
            "a specialist tool on the workbench",
            "Use neighboring actions in the same module before and after this one.",
        ),
    )


def sample_value(inp: dict, action: dict) -> str:
    name = (inp.get("name") or "").lower()
    accepts = (inp.get("accepts") or "").lower()
    default = (inp.get("default") or "").strip()
    module = action.get("module", "")
    aname = action.get("name", "")

    if "excel instance" in accepts or "excel instance" in name:
        return "%ExcelInstance%"
    if "word instance" in accepts or "word instance" in name:
        return "%WordInstance%"
    if "outlook instance" in accepts:
        return "%OutlookInstance%"
    if "access instance" in accepts:
        return "%AccessInstance%"
    if "browser" in accepts or "web browser" in accepts:
        return "%Browser%"
    if "window instance" in accepts or name == "window":
        return "%Window%"
    if "ui element" in accepts:
        return "UI element: Submit button"
    if "sql connection" in accepts:
        return "%SQLConnection%"
    if "ftp connection" in accepts:
        return "%FTPConnection%"
    if "cmd session" in accepts:
        return "%CMDSession%"
    if "terminal" in accepts:
        return "%TerminalSession%"
    if "ocr" in accepts:
        return "%OCREngine%"
    if "xml" in accepts:
        return "%XmlDoc%"
    if "datatable" in accepts:
        return "%InvoiceTable%"
    if "datarow" in accepts:
        return "%CurrentRow%"
    if "list" in accepts:
        return "%Files%"
    if "credential" in accepts:
        return "%Credential%"
    if "boolean" in accepts:
        return default or "True"
    if name in {"duration", "wait", "timeout"} or "seconds" in name:
        return "30"
    if "folder" in name or "directory" in name:
        return r"C:\RPA\Invoices"
    if "path" in name or "file" in name and "filter" not in name:
        if "csv" in name or "csv" in aname.lower():
            return r"C:\RPA\Invoices\batch.csv"
        if "pdf" in name or "pdf" in aname.lower():
            return r"C:\RPA\Invoices\INV-1042.pdf"
        if "xml" in name:
            return r"C:\RPA\Invoices\INV-1042.xml"
        if "excel" in module or "xlsx" in name:
            return r"C:\RPA\Close\FY26-P9.xlsx"
        return r"C:\RPA\Invoices\INV-1042.pdf"
    if "filter" in name and "file" in name:
        return "*.pdf"
    if "url" in name or "endpoint" in name:
        return "https://api.contoso.example/v1/invoices"
    if "worksheet" in name:
        return "TrialBalance"
    if name in {"column", "column name"}:
        return "Amount"
    if name in {"row", "row index"}:
        return "1"
    if "email" in name or name in {"to", "recipient"}:
        return "ap@contoso.example"
    if "subject" in name:
        return "Invoice INV-1042 processed"
    if "message" in name or "body" in name or "comment" in name:
        return "Processed by desktop flow Close-P9"
    if "password" in name:
        return "%Credential.Password%  (sensitive)"
    if "user" in name and "agent" not in name:
        return "CONTOSO\\rpa.bot"
    if "expression" in name or name == "if":
        return "%Count% > 0"
    if "json" in name:
        return '{ "InvoiceId": "INV-1042", "Amount": 190.5 }'
    if "xpath" in name:
        return "//Invoice/Total"
    if "sql" in name or "statement" in name:
        return "SELECT TOP 100 * FROM dbo.OpenOrders"
    if "macro" in name:
        return "RefreshAll"
    if "transaction" in name:
        return "FB60"
    if default and default not in {"N/A"} and "path" not in name:
        return default
    if "numeric" in accepts or "number" in accepts:
        return "1"
    if "text" in accepts:
        return "INV-1042"
    return default or "(set in designer)"


def demonstration(action: dict) -> str:
    kind = action.get("kind", "")
    name = action["name"]
    if kind == "power-fx-function":
        formula = FX_DEMO.get(name, f"={name}(...)")
        return (
            "In a Power Fx–enabled flow, type this in an input that accepts a formula:\n\n"
            f"```powerfx\n{formula}\n```\n\n"
            "Store the result with Set / a produced variable, or nest it inside If / Filter."
        )
    if kind in {"usable-item", "data-type"}:
        return (
            f"You do not drop **{name}** as an action card. "
            "You use it in the designer while building other actions "
            "(pane, type of a variable, or a locator)."
        )

    lines = [f"**{name}**"]
    inputs = action.get("inputs") or []
    if not inputs:
        lines.append("- (no inputs)")
    else:
        for inp in inputs[:8]:
            lines.append(f"- {inp['name']}: `{sample_value(inp, action)}`")
        if len(inputs) > 8:
            lines.append(f"- … {len(inputs) - 8} more parameter(s) in the action modal")
    outputs = action.get("outputs") or []
    if outputs:
        lines.append("Produces:")
        for out in outputs:
            typ = f" ({out['type']})" if out.get("type") else ""
            lines.append(f"- `%{out['name']}%`{typ}")
    nested = name.lower().startswith("if ") or name in {
        "If",
        "Else",
        "Else if",
        "Switch",
        "Case",
        "Default case",
        "For each",
        "Loop",
        "Loop condition",
        "On block error",
        "Region",
        "UI element event trigger",
    }
    if nested:
        lines.append("Place the actions that should run inside this block, then End.")
    return "```text\n" + "\n".join(lines) + "\n```"


def use_case(action: dict) -> str:
    name = action["name"]
    kind = action.get("kind", "")
    if name in SPECIAL_USE:
        return SPECIAL_USE[name]
    purpose = (action.get("purpose") or f"Run {name}").rstrip(".")
    if kind == "power-fx-function":
        return f"Put **{name}** in an `=` formula when you need this: {purpose}."
    if kind == "data-type":
        return f"A variable becomes **{name}** when PAD infers or you select this shape. {purpose}."
    if kind == "usable-item":
        return f"Use the **{name}** surface in the designer or console. {purpose}."
    job, _analogy, _combo = context(action.get("module", ""))
    return f"In {job}, drop **{name}** on the canvas. {purpose}."


def analogy(action: dict) -> str:
    name = action["name"]
    if name in SPECIAL_ANALOGY:
        return SPECIAL_ANALOGY[name]
    _job, base, _combo = context(action.get("module", ""))
    kind = action.get("kind", "")
    if kind == "power-fx-function":
        return f"A calculator button labeled {name}: same idea as Excel, used inside `=` formulas."
    if kind == "data-type":
        return f"The shape of the thing in the jar — {lower_first(action.get('purpose', name))}."
    if kind == "usable-item":
        return f"A part of the workshop itself, not a tool you pick up: {lower_first(action.get('purpose', name))}."
    n = name.lower()
    if n.startswith("wait"):
        return "Standing at the microwave until it beeps, so you do not grab a cold plate."
    if n.startswith("if "):
        return "Checking a condition on a clipboard before you choose a door."
    if n.startswith("launch") or n.startswith("open"):
        return f"Unlocking the room before you work. Same family as: {base}."
    if n.startswith("close") or n.startswith("end "):
        return "Turning out the lights when the work in that room is done."
    if n.startswith("get ") or n.startswith("read ") or n.startswith("retrieve"):
        return "Copying a value off a page into your notebook."
    if n.startswith("set ") or n.startswith("write ") or n.startswith("update") or n.startswith("populate"):
        return "Writing a value onto a page so the next person (or action) can see it."
    if n.startswith("delete") or n.startswith("remove") or n.startswith("clear"):
        return "Taking a page out of the folder so it is gone."
    if n.startswith("send") or n.startswith("post"):
        return "Handing a finished envelope to the mailroom."
    if n.startswith("click") or n.startswith("press"):
        return "Pushing the exact button a trained operator would push."
    return f"One tool in that kit: {base}."


def works_with(action: dict) -> str:
    _job, _a, combo = context(action.get("module", ""))
    name = action["name"].lower()
    extra = []
    if "launch" in name or "open" in name:
        extra.append("Keep the produced instance/connection and pass it into every later action in this module.")
    if "close" in name or name.startswith("end "):
        extra.append("Call this only after the last use of the instance so you do not break later steps.")
    if name.startswith("if ") or name == "if":
        extra.append("Combine with Else / Else if and End. Put Wait or If file exists before brittle UI/browser steps.")
    if "binary" in name:
        extra.append("Bridge native File/Excel actions and cloud connector operations.")
    return " ".join([combo] + extra)


def render_item(action: dict) -> list[str]:
    name = action["name"]
    return [
        f"### {name}",
        "",
        f"- **Id:** `{action.get('id', slug(name))}`",
        f"- **Kind:** {action.get('kind', '')}",
        f"- **Purpose:** {action.get('purpose', '')}",
        "",
        f"**Use case.** {use_case(action)}",
        "",
        "**Demonstration.**",
        "",
        demonstration(action),
        "",
        f"**Analogy.** {analogy(action)}",
        "",
        f"**In combination.** {works_with(action)}",
        "",
    ]


def write_group(path: Path, title: str, intro: str, items: list[dict]) -> None:
    lines = [
        f"# {title} — how each function works",
        "",
        intro,
        "",
        f"{len(items)} items. Each entry has a use case, a designer-style demonstration, an analogy, and how it combines with neighbors.",
        "",
    ]
    for item in sorted(items, key=lambda x: x["name"].lower()):
        lines.extend(render_item(item))
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    if not INVENTORY.is_file():
        print(f"Missing {INVENTORY}", file=sys.stderr)
        return 1
    data = json.loads(INVENTORY.read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)

    native_by: dict[str, list] = defaultdict(list)
    for item in data["native_actions"]:
        native_by[item["module"]].append(item)
    cloud_by: dict[str, list] = defaultdict(list)
    for item in data["cloud_connector_operations"]:
        cloud_by[item["module"]].append(item)

    index = [
        "# How each PAD function works",
        "",
        "Companion chapters for [How each function works (hub)](../05-how-each-function-works.md). "
        "Every native action, default cloud operation, Power Fx function, designer item, and data type has a use case, demonstration, analogy, and combination note.",
        "",
        "## Native actions",
        "",
        "| Module | Items | Chapter |",
        "| --- | ---: | --- |",
    ]
    for module in sorted(native_by, key=lambda m: MODULE_TITLE.get(m, m).lower()):
        items = native_by[module]
        title = MODULE_TITLE.get(module, module)
        fname = f"native-{module}.md"
        write_group(
            OUT / fname,
            title,
            f"Native Actions pane module **{title}**.",
            items,
        )
        index.append(f"| {title} | {len(items)} | [{fname}]({fname}) |")

    index += ["", "## Cloud connector operations", "", "| Connector | Items | Chapter |", "| --- | ---: | --- |"]
    for module in sorted(cloud_by, key=lambda m: MODULE_TITLE.get(m, m).lower()):
        items = cloud_by[module]
        title = MODULE_TITLE.get(module, module)
        fname = f"cloud-{module}.md"
        write_group(
            OUT / fname,
            title,
            f"Default-pane **{title}** operations. Requires a connection reference. File payloads are binary data.",
            items,
        )
        index.append(f"| {title} | {len(items)} | [{fname}]({fname}) |")

    write_group(
        OUT / "power-fx.md",
        "Power Fx functions",
        "Only in Power Fx–enabled desktop flows. Formulas start with `=`. `Index` is 1-based.",
        data["power_fx_functions"],
    )
    write_group(
        OUT / "designer-and-data-types.md",
        "Designer items and data types",
        "These are not action cards. They are the workshop (panes, recorders, types) the actions run in.",
        data["designer_usable_items"] + data["data_types"],
    )
    index += [
        "",
        "## Other",
        "",
        "| Chapter | Items |",
        "| --- | ---: |",
        f"| [Power Fx functions](power-fx.md) | {len(data['power_fx_functions'])} |",
        f"| [Designer items and data types](designer-and-data-types.md) | {len(data['designer_usable_items']) + len(data['data_types'])} |",
        "",
        "Cross-module flows: [Combination playbooks](../06-combination-playbooks.md).",
        "",
    ]
    (OUT / "README.md").write_text("\n".join(index), encoding="utf-8")
    print(
        json.dumps(
            {
                "native_modules": len(native_by),
                "cloud_modules": len(cloud_by),
                "power_fx": len(data["power_fx_functions"]),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
