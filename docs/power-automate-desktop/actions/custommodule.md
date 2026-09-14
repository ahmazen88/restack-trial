# Custom actions

Organization-built actions uploaded to the **environment**. They show up in the Actions pane like built-in modules, with the names and properties the developer defined.

Official docs: [Custom actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/custommodule), [Assets library](https://learn.microsoft.com/en-us/power-automate/desktop-flows/assets-library).

## Constraints

- Premium Power Automate license.
- Power Automate for desktop **2.32** or later.
- Scoped per environment. Develop in dev, then promote to test/prod.
- Custom action names and property names cannot use [reserved keywords](https://learn.microsoft.com/en-us/power-automate/desktop-flows/reserved-keywords).

## What you use at design time

| Item | Where |
|---|---|
| Uploaded module (`.dll` + manifest) | Assets library in the console / portal |
| Action group named by the developer | Actions pane after the module is available in the environment |
| Inputs / outputs the developer declared | Action properties dialog |

There is no global Microsoft list of custom actions. Inventory them from **Assets library** in each environment.

## Related built-in modules

If you are looking for “write my own logic” without a custom module:

- [Scripting](scripting.md) — PowerShell, Python, VBScript, JavaScript, DOS, .NET
- [HTTP](web.md) — REST / SOAP
- [Run flow](runflow.md) — call another desktop flow
