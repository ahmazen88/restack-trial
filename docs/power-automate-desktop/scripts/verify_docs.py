#!/usr/bin/env python3
"""Verify the PAD documentation set is internally consistent."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIONS = ROOT / "actions"
FUNCTIONS = ROOT / "functions"

REQUIRED_PAGES = [
    ROOT / "README.md",
    ROOT / "INVENTORY.md",
    ROOT / "usable-items.md",
    ROOT / "inventory.json",
    ACTIONS / "README.md",
    FUNCTIONS / "README.md",
    FUNCTIONS / "percent-notation.md",
    FUNCTIONS / "power-fx.md",
    FUNCTIONS / "data-types.md",
    FUNCTIONS / "data-type-properties.md",
]

CLASSIC_FUNCTIONS = [
    "StartsWith",
    "NotStartsWith",
    "EndsWith",
    "NotEndsWith",
    "Contains",
    "NotContains",
    "IsEmpty",
    "IsNotEmpty",
]

POWER_FX_HEADING = re.compile(r"^### ([A-Za-z][A-Za-z0-9 /]+)\s*$", re.M)
ACTION_HEADING = re.compile(r"^### (.+)$", re.M)


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    errors: list[str] = []

    for path in REQUIRED_PAGES:
        if not path.is_file():
            errors.append(f"missing {path.relative_to(ROOT)}")

    catalog = json.loads((ROOT / "inventory.json").read_text(encoding="utf-8"))
    modules = catalog["modules"]
    action_count = catalog["action_count"]
    named = sum(m["action_count"] for m in modules)
    if named != action_count:
        errors.append(f"inventory action_count {action_count} != sum of modules {named}")
    if len(modules) != 52:
        errors.append(f"expected 52 modules, found {len(modules)}")
    if action_count != 444:
        errors.append(f"expected 444 named actions, found {action_count}")

    for module in modules:
        slug = module["slug"]
        page = ACTIONS / f"{slug}.md"
        if not page.is_file():
            errors.append(f"missing actions/{slug}.md")
            continue
        text = page.read_text(encoding="utf-8")
        headings = ACTION_HEADING.findall(text)
        # Module pages start with # title then ## Actions then ### per action.
        # Dynamic catalogs have extra ### operation groups.
        if module["action_count"] > 0:
            missing = [a["name"] for a in module["actions"] if f"### {a['name']}" not in text]
            if missing:
                errors.append(f"{slug}: missing headings {missing[:5]}")

    inventory_md = (ROOT / "INVENTORY.md").read_text(encoding="utf-8")
    if "444" not in inventory_md:
        errors.append("INVENTORY.md does not mention 444 actions")
    for module in modules:
        for action in module["actions"]:
            if f"- {action['name']}" not in inventory_md:
                errors.append(f"INVENTORY.md missing {module['slug']}: {action['name']}")
                break

    classic = (FUNCTIONS / "percent-notation.md").read_text(encoding="utf-8")
    for name in CLASSIC_FUNCTIONS:
        if f"### {name}" not in classic:
            errors.append(f"classic function heading missing: {name}")

    fx = (FUNCTIONS / "power-fx.md").read_text(encoding="utf-8")
    fx_names: list[str] = []
    for heading in POWER_FX_HEADING.findall(fx):
        if heading in {"Operators (used with the functions)", "Quick mapping from classic PAD habits", "Function picker"}:
            continue
        fx_names.extend(part.strip() for part in heading.split("/"))
    # Combined headings like "Min / Max" already split. Drop section-like leftovers.
    fx_names = [n for n in fx_names if n[:1].isupper() and " " not in n]
    unique = sorted(set(fx_names))
    if len(unique) < 120:
        errors.append(f"Power Fx function headings look too few: {len(unique)}")

    if errors:
        print("PAD docs verification failed:")
        for item in errors:
            print(f"  - {item}")
        raise SystemExit(1)

    print("PAD docs verification passed")
    print(f"  modules: {len(modules)}")
    print(f"  named built-in actions: {action_count}")
    print(f"  classic % functions: {len(CLASSIC_FUNCTIONS)}")
    print(f"  Power Fx headings parsed: {len(unique)}")
    print(f"  action pages: {len(list(ACTIONS.glob('*.md')))}")


if __name__ == "__main__":
    main()
