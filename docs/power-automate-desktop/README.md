# Power Automate for desktop — functions and usable items

This folder is a working catalog of **Power Automate for desktop (PAD)**: every action module in the designer, every built-in action name, the classic `%` expression functions, the Power Fx function set, data types, and the other items you can actually use while building a flow.

Microsoft’s product name is **Power Automate for desktop**. “PAD” in this documentation means that designer, not Power Automate cloud flows.

## Start here (the two steps you asked for)

1. **Identify everything usable** — [INVENTORY.md](INVENTORY.md) lists every named built-in action (444) across 52 modules, plus pointers to functions and designer assets. [usable-items.md](usable-items.md) explains the non-action items (variables, UI elements, images, recorders, credentials, connectors).
2. **Document each function / action** — [actions/](actions/README.md) has one page per module. [functions/](functions/README.md) documents classic `%` functions, Power Fx functions, data types, and data-type properties.

Machine-readable action list: [inventory.json](inventory.json).

## Two expression languages

PAD flows use **one** expression language, chosen when you create the flow:

| Mode | How you write it | Function set |
|---|---|---|
| Classic (default) | Wrap expressions in `%...%` | Eight text tests (`Contains`, `StartsWith`, …), arithmetic, comparisons, `AND` / `OR` / `NOT`. Most work is done with **actions**, not formulas. |
| Power Fx | Start a field with `=` or interpolate with `${...}` | [130 functions](functions/power-fx.md) (text, math, dates, tables, error handling, collections). |

You cannot mix the two syntaxes in the same flow. Enable Power Fx with the toggle on **New flow** in the console.

## What “usable items” means in PAD

In the designer, work is not only actions. A complete inventory has five layers:

1. **Actions** — search or drag from the left pane. Recorders drop these in for you.
2. **Expression functions** — classic `%Function()%` or Power Fx `=Function()`.
3. **Data and properties** — `%File.FullName%`, `%List.Count%`, Excel instances, mail messages, and so on.
4. **Designer assets** — variables, UI elements, images, credentials, connections, subflows, UI element collections.
5. **Run / operate items** — console, machines, work queues, environment variables, custom action modules, Copilot, flow checker.

## Counts in this catalog

| Layer | Count | Where documented |
|---|---:|---|
| Action modules (pane groups) | 52 | [actions/README.md](actions/README.md) |
| Named built-in actions | 444 | [INVENTORY.md](INVENTORY.md) |
| Classic `%` text functions | 8 | [functions/percent-notation.md](functions/percent-notation.md) |
| Classic operators | 13 | [functions/percent-notation.md](functions/percent-notation.md) |
| Power Fx functions | 130 | [functions/power-fx.md](functions/power-fx.md) |
| Data types with properties | 24 | [functions/data-type-properties.md](functions/data-type-properties.md) |

Four pane groups are **dynamic catalogs**, not a fixed Microsoft action list: Cloud connectors, SharePoint, Office 365 Outlook, and Custom actions. Those groups still appear in the designer; the operations you see depend on connectors, licenses, and modules uploaded to the environment.

## Official Microsoft pages

- [Actions reference](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference)
- [Variables and the % notation](https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-manipulation)
- [Power Fx in desktop flows](https://learn.microsoft.com/en-us/power-automate/desktop-flows/power-fx)
- [Formula reference — desktop flows](https://learn.microsoft.com/en-us/power-platform/power-fx/formula-reference-desktop-flows)
- [Variable data types](https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-data-types)

Action names and parameter names in this folder follow that public reference. Explanations here are original summaries for builders, not a copy of Microsoft Learn.

## Suggested reading order

1. [Inventory](INVENTORY.md) — scan the full list.
2. [Usable items](usable-items.md) — designer anatomy.
3. [Classic functions](functions/percent-notation.md) and [Power Fx](functions/power-fx.md).
4. Core modules you will use in almost every flow: [Variables](actions/variables.md), [Conditionals](actions/conditionals.md), [Loops](actions/loops.md), [Flow control](actions/flowcontrol.md), [Text](actions/text.md).
5. Automation surfaces: [UI automation](actions/uiautomation.md), [Browser automation](actions/webautomation.md), [Excel](actions/excel.md), [File](actions/file.md) / [Folder](actions/folder.md).
