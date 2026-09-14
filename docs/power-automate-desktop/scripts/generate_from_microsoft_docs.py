#!/usr/bin/env python3
"""Extract PAD action catalog from Microsoft Learn markdown and emit original docs."""

from __future__ import annotations

import html
import json
import os
import re
from pathlib import Path

SRC = Path(
    os.environ.get(
        "PAD_MS_DOCS",
        "/tmp/pad-docs/power-automate-docs/articles/desktop-flows/actions-reference",
    )
)
OUT = Path(
    os.environ.get(
        "PAD_DOC_OUT",
        str(Path(__file__).resolve().parents[1]),
    )
)
LEARN_BASE = "https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference"

SKIP_FILES = {"cognitive.md"}  # redirect only

SKIP_HEADINGS = {
    "prerequisites and limitations",
    "related information",
    "known limitations",
    "known limitations for performing an action by simulation",
    "getting started with sharepoint actions in desktop flows",
    "send an email with attachments",
    "webdriver-based browser automation",
    "adding ui elements",
    "use the recognize entities in text action",
    "use the windows ocr engine",
    "use the tesseract ocr engine",
    "natural language to script powered by copilot (preview)",
    "working with variables in scripting actions",
    "how to download the content of a sharepoint folder",
    "add a fixed number of attachments",
    "add a dynamic number of attachments",
    "use files in cloud connector actions",
    "embed connection references on a desktop flow",
    "handle custom errors raised by the throw custom error action",
}

MODULE_META = {
    "access": {
        "title": "Access",
        "summary": "Open, query, and close local Microsoft Access databases.",
    },
    "activedirectory": {
        "title": "Active Directory",
        "summary": "Connect to Active Directory and manage users, groups, and objects.",
    },
    "aibuilder": {
        "title": "AI Builder (preview)",
        "summary": "Call AI Builder models from a desktop flow.",
    },
    "aws": {
        "title": "AWS",
        "summary": "Manage Amazon EC2, S3, and related AWS resources from a desktop flow.",
    },
    "azure": {
        "title": "Azure",
        "summary": "Manage Azure resource groups, disks, blobs, and related cloud resources.",
    },
    "clipboard": {
        "title": "Clipboard",
        "summary": "Read, write, and clear Windows clipboard text.",
    },
    "cloudconnectors": {
        "title": "Cloud connectors",
        "summary": "Run Power Automate cloud connector operations inside a desktop flow.",
    },
    "cmd": {
        "title": "CMD session",
        "summary": "Open a command prompt session and send commands interactively.",
    },
    "compression": {
        "title": "Compression",
        "summary": "Zip and unzip files and folders.",
    },
    "conditionals": {
        "title": "Conditionals",
        "summary": "Branch the flow with If, Else if, Else, Switch, and Case.",
    },
    "cryptography": {
        "title": "Cryptography",
        "summary": "Hash, encrypt, decrypt, and encode values.",
    },
    "custommodule": {
        "title": "Custom actions",
        "summary": "Use organization-uploaded custom action modules in a desktop flow.",
    },
    "cyberark": {
        "title": "CyberArk",
        "summary": "Retrieve secrets from CyberArk vaults at runtime.",
    },
    "database": {
        "title": "Database",
        "summary": "Open SQL connections and run statements against databases.",
    },
    "datetime": {
        "title": "Date time",
        "summary": "Read the current datetime and add or subtract time units.",
    },
    "display": {
        "title": "Message boxes",
        "summary": "Show dialogs, input boxes, and custom forms to the user.",
    },
    "email": {
        "title": "Email",
        "summary": "Send and retrieve mail through IMAP, POP3, and SMTP.",
    },
    "excel": {
        "title": "Excel",
        "summary": "Launch Excel, read and write cells, and manage worksheets and macros.",
    },
    "exchange": {
        "title": "Exchange Server",
        "summary": "Connect to Exchange and process mailbox messages.",
    },
    "file": {
        "title": "File",
        "summary": "Create, copy, move, read, write, and convert files.",
    },
    "flowcontrol": {
        "title": "Flow control",
        "summary": "Control execution order, errors, subflows, waits, and regions.",
    },
    "folder": {
        "title": "Folder",
        "summary": "Create, copy, move, list, and delete folders.",
    },
    "ftp": {
        "title": "FTP",
        "summary": "Connect to FTP/FTPS servers and transfer files.",
    },
    "googlecognitive": {
        "title": "Google Cognitive",
        "summary": "Call Google Cloud Vision and Natural Language APIs.",
    },
    "ibmcognitive": {
        "title": "IBM Cognitive",
        "summary": "Call IBM Watson language and visual recognition APIs.",
    },
    "logging": {
        "title": "Logging",
        "summary": "Write custom log entries during a desktop flow run.",
    },
    "loops": {
        "title": "Loops",
        "summary": "Repeat actions with Loop, Loop condition, and For each.",
    },
    "microsoftcognitive": {
        "title": "Microsoft Cognitive",
        "summary": "Call Azure Cognitive Services for text, vision, and language.",
    },
    "mouseandkeyboard": {
        "title": "Mouse and keyboard",
        "summary": "Move the mouse, send clicks and keystrokes, and wait for input.",
    },
    "ocr": {
        "title": "OCR",
        "summary": "Extract or wait for on-screen text with Windows or Tesseract OCR.",
    },
    "office365outlook": {
        "title": "Office 365 Outlook",
        "summary": "Use the Office 365 Outlook cloud connector from a desktop flow.",
    },
    "outlook": {
        "title": "Outlook",
        "summary": "Automate the local Outlook desktop client.",
    },
    "pdf": {
        "title": "PDF",
        "summary": "Extract text, tables, and images from PDFs and merge or split files.",
    },
    "powerautomateenvironment": {
        "title": "Power Automate environment",
        "summary": "Read Dataverse / Power Platform environment variables.",
    },
    "powerautomatesecretvariables": {
        "title": "Power Automate secret variables",
        "summary": "Fetch credentials stored in the Power Automate environment.",
    },
    "runflow": {
        "title": "Run flow",
        "summary": "Call another desktop flow and wait for its outputs.",
    },
    "sap": {
        "title": "SAP automation",
        "summary": "Drive SAP GUI: login, transactions, and UI element interaction.",
    },
    "scripting": {
        "title": "Scripting",
        "summary": "Run DOS, VBScript, JavaScript, PowerShell, Python, and .NET scripts.",
    },
    "services": {
        "title": "Windows services",
        "summary": "Start, stop, pause, resume, and wait for Windows services.",
    },
    "sharepoint": {
        "title": "SharePoint",
        "summary": "Use the SharePoint cloud connector from a desktop flow.",
    },
    "system": {
        "title": "System",
        "summary": "Run processes, ping hosts, and manage Windows environment variables.",
    },
    "terminalemulation": {
        "title": "Terminal emulation",
        "summary": "Automate mainframe and terminal sessions (HLLAPI / terminal emulators).",
    },
    "testing": {
        "title": "Testing",
        "summary": "Build desktop-flow test cases with Assert and Test a desktop flow.",
    },
    "text": {
        "title": "Text",
        "summary": "Parse, split, join, convert, and transform text values.",
    },
    "uiautomation": {
        "title": "UI automation",
        "summary": "Click, type, extract, and wait on Windows UI elements and images.",
    },
    "variables": {
        "title": "Variables",
        "summary": "Set variables and work with lists, data tables, JSON, and Power Fx.",
    },
    "web": {
        "title": "HTTP",
        "summary": "Call REST and SOAP endpoints and download files over HTTP.",
    },
    "webautomation": {
        "title": "Browser automation",
        "summary": "Launch browsers and interact with web pages and web elements.",
    },
    "word": {
        "title": "Word",
        "summary": "Launch Word and read, write, or replace document content.",
    },
    "workqueues": {
        "title": "Work queues",
        "summary": "Add, process, and update Power Automate work queue items.",
    },
    "workstation": {
        "title": "Workstation",
        "summary": "Control the local workstation: screenshots, printers, lock, shutdown.",
    },
    "xml": {
        "title": "XML",
        "summary": "Read, query, and edit XML documents and nodes.",
    },
}

HEADING_RE = re.compile(
    r"^## (?:<a name=\"([^\"]+)\"></a>\s*)?(.+?)\s*$",
    re.M,
)
INPUT_TABLE_RE = re.compile(
    r"###+\s+Input parameters\s*(.*?)(?=\n###+\s|\Z)",
    re.S | re.I,
)
OUTPUT_TABLE_RE = re.compile(
    r"###+\s+Variables produced\s*(.*?)(?=\n###+\s|\Z)",
    re.S | re.I,
)
EXCEPT_TABLE_RE = re.compile(
    r"###+\s+(?:<a name=\"[^\"]+\"></a>\s*)?Exceptions\s*(.*?)(?=\n## |\Z)",
    re.S | re.I,
)
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")


def clean_cell(value: str) -> str:
    value = html.unescape(value or "")
    value = MD_LINK_RE.sub(r"\1", value)
    value = re.sub(r"\*\*(.+?)\*\*", r"\1", value)
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"<[^>]+>", "", value)
    return " ".join(value.split()).strip()


def parse_md_table(block: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        raw_cells = line.split("|")
        if raw_cells and raw_cells[0].strip() == "":
            raw_cells = raw_cells[1:]
        if raw_cells and raw_cells[-1].strip() == "":
            raw_cells = raw_cells[:-1]
        cells = [clean_cell(c) for c in raw_cells]
        if cells and set("".join(cells)) <= set("-: "):
            continue
        rows.append(cells)
    return rows


def first_sentence(text: str) -> str:
    text = MD_LINK_RE.sub(r"\1", text)
    text = re.sub(r":image[^\n]*", "", text)
    text = re.sub(r"!\[.*?\]\([^)]+\)", "", text)
    text = re.sub(r">\s*\[!.*?\]", "", text)
    text = " ".join(text.split())
    if not text:
        return ""
    match = re.match(r"(.+?[.!?])(?:\s|$)", text)
    return (match.group(1) if match else text[:240]).strip()


def paraphrase(name: str, sentence: str) -> str:
    """Write a short original summary from the action name and first fact line."""
    s = sentence.rstrip(".")
    lower = s.lower()
    name_l = name.lower()
    if not s or lower in {name_l, f"the {name_l}"}:
        return f"Runs the **{name}** action."
    # Prefer an independent phrasing that still stays factual.
    if lower.startswith(("gets ", "get ")):
        return f"Reads {s.split(' ', 1)[1]}."
    if lower.startswith(("sets ", "set ")):
        return f"Writes {s.split(' ', 1)[1]}."
    if lower.startswith("retrieves "):
        return f"Returns {s[10:]}."
    if lower.startswith("creates "):
        return f"Creates {s[8:]}."
    if lower.startswith("launches "):
        return f"Starts {s[9:]}."
    if lower.startswith("terminates "):
        return f"Stops {s[11:]}."
    if lower.startswith("marks the beginning"):
        return s[0].upper() + s[1:] + "."
    if not s.endswith("."):
        s = s + "."
    # Capitalize if needed
    return s[0].upper() + s[1:] if s else f"Runs the **{name}** action."


def parse_inputs(block: str) -> list[dict]:
    if "doesn't require any input" in block.lower() or "does not require any input" in block.lower():
        return []
    tables = parse_md_table(block)
    if not tables:
        return []
    header = [h.lower() for h in tables[0]]
    items = []
    for row in tables[1:]:
        if len(row) < 2:
            continue
        # Argument | Optional | Accepts | Default Value | Description
        name = row[0] if row else ""
        if not name or name.lower() in {"argument", "parameter"}:
            continue
        optional = row[1] if len(row) > 1 else ""
        accepts = row[2] if len(row) > 2 else ""
        default = row[3] if len(row) > 3 else ""
        desc = row[4] if len(row) > 4 else ""
        items.append(
            {
                "name": name,
                "optional": optional,
                "accepts": accepts,
                "default": default,
                "note": desc,
            }
        )
    return items


def parse_outputs(block: str) -> list[dict]:
    if "doesn't produce any variables" in block.lower() or "does not produce any variables" in block.lower():
        return []
    tables = parse_md_table(block)
    if not tables:
        # sometimes "This action produces the output variables of the selected flow."
        text = " ".join(block.split())
        if text:
            return [{"name": "(flow outputs)", "type": "*", "note": clean_cell(text)}]
        return []
    items = []
    for row in tables[1:]:
        if len(row) < 2:
            continue
        name = row[0]
        if name.lower() in {"argument", "parameter"}:
            continue
        items.append(
            {
                "name": name or "(designer-named)",
                "type": row[1] if len(row) > 1 else "",
                "note": row[2] if len(row) > 2 else "",
            }
        )
    return items


def parse_exceptions(block: str) -> list[dict]:
    if "doesn't include any exceptions" in block.lower() or "does not include any exceptions" in block.lower():
        return []
    tables = parse_md_table(block)
    items = []
    for row in tables[1:] if tables else []:
        if not row or row[0].lower() in {"exception", "argument"}:
            continue
        items.append({"name": row[0], "note": row[1] if len(row) > 1 else ""})
    return items


def split_sections(text: str) -> list[tuple[str, str, str]]:
    """Return (anchor, title, body) for each ## section."""
    matches = list(HEADING_RE.finditer(text))
    sections = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections.append((m.group(1) or "", m.group(2).strip(), text[start:end]))
    return sections


def parse_module(path: Path) -> dict | None:
    slug = path.stem
    if path.name in SKIP_FILES:
        return None
    raw = path.read_text(encoding="utf-8")
    # drop yaml
    raw = re.sub(r"^---\n.*?\n---\n", "", raw, count=1, flags=re.S)
    raw = re.sub(r"\[!INCLUDE\[.*?\]\([^)]+\)\]", "", raw)
    meta = MODULE_META.get(slug, {"title": slug, "summary": ""})
    actions = []
    for anchor, title, body in split_sections(raw):
        title_l = title.lower().strip()
        if title_l in SKIP_HEADINGS or title_l.startswith("known limitation"):
            continue
        if "### Input parameters" not in body and "##### Input parameters" not in body:
            continue
        in_m = INPUT_TABLE_RE.search(body)
        out_m = OUTPUT_TABLE_RE.search(body)
        ex_m = EXCEPT_TABLE_RE.search(body)
        lead = body
        if in_m:
            lead = body[: in_m.start()]
        sentence = first_sentence(lead)
        actions.append(
            {
                "name": title,
                "anchor": anchor,
                "summary": paraphrase(title, sentence),
                "inputs": parse_inputs(in_m.group(1) if in_m else ""),
                "outputs": parse_outputs(out_m.group(1) if out_m else ""),
                "exceptions": parse_exceptions(ex_m.group(1) if ex_m else ""),
            }
        )
    return {
        "slug": slug,
        "title": meta["title"],
        "summary": meta["summary"],
        "learn_url": f"{LEARN_BASE}/{slug if slug != 'webautomation' else 'webautomation'}",
        "file": path.name,
        "actions": actions,
        "action_count": len(actions),
    }


def md_escape(text: str) -> str:
    return text.replace("|", "\\|")


def render_action(action: dict, module: dict) -> str:
    lines = [f"### {action['name']}", ""]
    lines.append(action["summary"])
    lines.append("")
    if action["anchor"]:
        lines.append(
            f"Designer name: **{action['name']}**. "
            f"Official reference: [{module['title']} / {action['name']}]"
            f"({module['learn_url']}#{action['anchor']})."
        )
        lines.append("")
    if action["inputs"]:
        lines.append("**Inputs**")
        lines.append("")
        lines.append("| Parameter | Required | Accepts | Default |")
        lines.append("|---|---|---|---|")
        for p in action["inputs"]:
            req = "No" if str(p["optional"]).lower() in {"yes", "n/a", "true"} and p["optional"].lower() == "yes" else (
                "Optional" if str(p["optional"]).lower() == "yes" else (
                    "Depends" if str(p["optional"]).upper() == "N/A" else "Yes"
                )
            )
            # Optional column in MS docs: Yes = optional, No = required, N/A = enum/toggle
            opt_raw = str(p["optional"]).strip()
            if opt_raw.lower() == "yes":
                req = "Optional"
            elif opt_raw.lower() == "no":
                req = "Required"
            elif opt_raw.upper() == "N/A":
                req = "Choice"
            else:
                req = opt_raw or "—"
            lines.append(
                f"| {md_escape(p['name'])} | {req} | {md_escape(p['accepts'] or '—')} | {md_escape(p['default'] or '—')} |"
            )
        lines.append("")
    else:
        lines.append("This action has no input parameters.")
        lines.append("")
    if action["outputs"]:
        lines.append("**Outputs**")
        lines.append("")
        lines.append("| Variable | Type |")
        lines.append("|---|---|")
        for o in action["outputs"]:
            lines.append(f"| {md_escape(o['name'])} | {md_escape(o['type'] or '—')} |")
        lines.append("")
    else:
        lines.append("Produces no variables.")
        lines.append("")
    if action["exceptions"]:
        names = ", ".join(f"`{e['name']}`" for e in action["exceptions"])
        lines.append(f"**On error:** {names}.")
        lines.append("")
    else:
        lines.append("No module-specific exceptions are listed for this action.")
        lines.append("")
    return "\n".join(lines)


def render_module(module: dict) -> str:
    parts = [
        f"# {module['title']}",
        "",
        module["summary"],
        "",
        f"- Actions in this module: **{module['action_count']}**",
        f"- Official docs: [{module['title']} actions]({module['learn_url']})",
        "",
        "## Actions",
        "",
    ]
    if not module["actions"]:
        parts.append(
            "This group is a designer category rather than a fixed list of built-in actions. "
            "Items that appear here depend on connectors, custom modules, or the environment."
        )
        parts.append("")
        return "\n".join(parts)
    for action in module["actions"]:
        parts.append(render_action(action, module))
        parts.append("---")
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def main() -> None:
    modules = []
    for path in sorted(SRC.glob("*.md")):
        parsed = parse_module(path)
        if parsed:
            modules.append(parsed)

    actions_dir = OUT / "actions"
    actions_dir.mkdir(parents=True, exist_ok=True)

    catalog = {
        "product": "Power Automate for desktop",
        "source": "Microsoft Learn actions reference (action names and parameter names)",
        "source_url": LEARN_BASE,
        "module_count": len(modules),
        "action_count": sum(m["action_count"] for m in modules),
        "modules": [
            {
                "slug": m["slug"],
                "title": m["title"],
                "summary": m["summary"],
                "learn_url": m["learn_url"],
                "action_count": m["action_count"],
                "actions": [{"name": a["name"], "anchor": a["anchor"]} for a in m["actions"]],
            }
            for m in modules
        ],
    }
    (OUT / "inventory.json").write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")

    inv = [
        "# Power Automate Desktop inventory",
        "",
        "Step 1 of this documentation set: every **usable item** in Power Automate for desktop (PAD), grouped the way the designer presents them.",
        "",
        f"- Built-in actions with a fixed designer name: **{catalog['action_count']}**",
        f"- Action modules / pane groups: **{catalog['module_count']}**",
        "- Plus expression functions, data-type properties, and designer assets listed in [usable items](usable-items.md).",
        "",
        "Source of action names: [Microsoft Learn actions reference](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference).",
        "",
        "## How to read this list",
        "",
        "| Kind | Where you use it | Count in this catalog |",
        "|---|---|---|",
        f"| Actions | Actions pane, search box, recorder | {catalog['action_count']} named actions |",
        "| Classic expression functions | `%Function(...)%` in non-Power Fx flows | 8 text tests + operators |",
        "| Power Fx functions | `=` formula bar when Power Fx is enabled | 130 functions |",
        "| Data-type properties | `%Variable.Property%` | 20+ types |",
        "| Designer assets | Variables, UI elements, images, credentials, subflows | see [usable items](usable-items.md) |",
        "",
        "## Action modules",
        "",
    ]
    total = 0
    for m in sorted(modules, key=lambda x: x["title"].lower()):
        total += m["action_count"]
        inv.append(f"### {m['title']} ({m['action_count']})")
        inv.append("")
        inv.append(m["summary"])
        inv.append("")
        inv.append(f"Docs: [{m['title']}](actions/{m['slug']}.md)")
        inv.append("")
        if m["actions"]:
            for a in m["actions"]:
                inv.append(f"- {a['name']}")
            inv.append("")
        else:
            inv.append("Dynamic catalog (connector operations, custom modules, or environment-specific items).")
            inv.append("")
    inv.append(f"Named built-in actions counted above: **{total}**.")
    inv.append("")
    inv.extend(
        [
            "## Expression functions (not in the Actions pane)",
            "",
            "### Classic `%` functions (8)",
            "",
            "Documented in [functions/percent-notation.md](functions/percent-notation.md).",
            "",
            "- `StartsWith`",
            "- `NotStartsWith`",
            "- `EndsWith`",
            "- `NotEndsWith`",
            "- `Contains`",
            "- `NotContains`",
            "- `IsEmpty`",
            "- `IsNotEmpty`",
            "",
            "Plus operators `+` `-` `*` `/` `=` `<>` `<` `<=` `>` `>=` `AND` `OR` `NOT`.",
            "",
            "### Power Fx functions (130)",
            "",
            "Documented in [functions/power-fx.md](functions/power-fx.md). Enabled per flow at creation time.",
            "",
            "## Designer assets (usable, not functions)",
            "",
            "See [usable-items.md](usable-items.md): variables, UI elements, images, credentials, connections, subflows, recorders, Copilot, work queues, machines, custom action modules, environment variables, test cases.",
            "",
            "Microsoft Learn also mentions a **Triggers** group in some indexes. In current PAD, starting a flow is done from the console, a cloud flow, a shortcut, or work queues — not a separate 445th action module in this catalog.",
            "",
        ]
    )
    (OUT / "INVENTORY.md").write_text("\n".join(inv), encoding="utf-8")

    # per-module docs
    for m in modules:
        if m["action_count"] == 0:
            continue
        (actions_dir / f"{m['slug']}.md").write_text(render_module(m), encoding="utf-8")

    # actions index
    index_lines = [
        "# Actions by module",
        "",
        "Every built-in action group in the Power Automate for desktop **Actions** pane. "
        "Cloud connector, SharePoint, and Office 365 Outlook groups expose the connector operation catalog rather than a fixed built-in list.",
        "",
        f"Documented built-in actions: **{catalog['action_count']}** across **{catalog['module_count']}** modules.",
        "",
        "| Module | Actions | What it is for |",
        "|---|---:|---|",
    ]
    for m in sorted(modules, key=lambda x: x["title"].lower()):
        index_lines.append(
            f"| [{m['title']}]({m['slug']}.md) | {m['action_count']} | {m['summary']} |"
        )
    index_lines.append("")
    (actions_dir / "README.md").write_text("\n".join(index_lines), encoding="utf-8")

    print(f"modules={catalog['module_count']} actions={catalog['action_count']}")
    for m in modules:
        print(f"  {m['slug']:28} {m['action_count']:3}  {m['title']}")


if __name__ == "__main__":
    main()
