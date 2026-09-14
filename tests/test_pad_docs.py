"""Checks for the Power Automate Desktop documentation catalog."""

from __future__ import annotations

import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "power-automate-desktop"
INVENTORY = DOCS / "inventory.json"
MODULES = DOCS / "modules"
HEADING_RE = re.compile(r"^### (.+)\s*$", re.M)


class PadDocsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(INVENTORY.read_text(encoding="utf-8"))

    def test_inventory_file_exists(self) -> None:
        self.assertTrue(INVENTORY.is_file())

    def test_minimum_counts(self) -> None:
        counts = self.data["counts"]
        self.assertGreaterEqual(counts["native_actions"], 400)
        self.assertGreaterEqual(counts["cloud_connector_operations"], 150)
        self.assertEqual(counts["power_fx_functions"], 130)
        self.assertGreaterEqual(counts["designer_usable_items"], 30)
        self.assertGreaterEqual(counts["data_types"], 30)
        self.assertGreaterEqual(counts["action_modules"], 45)

    def test_no_false_positive_headings(self) -> None:
        names = [a["name"].lower() for a in self.data["native_actions"]]
        banned = (
            "deprecation timeline",
            "webdriver limitations",
            "known limitations",
            "related information",
        )
        for bad in banned:
            self.assertNotIn(bad, names)

    def test_required_native_actions_present(self) -> None:
        names = {a["name"] for a in self.data["native_actions"]}
        required = {
            "Set variable",
            "If",
            "For each",
            "Launch Excel",
            "Launch new Chrome",
            "Launch new Microsoft Edge",
            "Launch new Internet Explorer",
            "Click UI element in window",
            "If text on screen (OCR)",
            "Throw custom error",
            "Run Power Fx expression",
            "UI element event trigger",
            "Run Power App (preview)",
            "Launch Access",
            "Assert",
        }
        missing = required - names
        self.assertEqual(missing, set())

    def test_native_action_ids_unique(self) -> None:
        ids = [a["id"] for a in self.data["native_actions"]]
        dupes = [item for item, n in Counter(ids).items() if n > 1]
        self.assertEqual(dupes, [])

    def test_every_native_action_has_module_heading(self) -> None:
        missing = []
        for action in self.data["native_actions"]:
            path = MODULES / f"{action['module']}.md"
            if not path.is_file():
                missing.append(f"missing file for {action['id']}")
                continue
            text = path.read_text(encoding="utf-8")
            headings = {h.strip() for h in HEADING_RE.findall(text)}
            if action["name"] not in headings:
                missing.append(action["id"])
        self.assertEqual(missing[:10], [], msg=f"{len(missing)} actions lack headings")

    def test_every_cloud_operation_has_module_heading(self) -> None:
        missing = []
        for action in self.data["cloud_connector_operations"]:
            path = MODULES / f"{action['module']}.md"
            self.assertTrue(path.is_file(), action["module"])
            headings = {
                h.strip() for h in HEADING_RE.findall(path.read_text(encoding="utf-8"))
            }
            if action["name"] not in headings:
                missing.append(action["id"])
        self.assertEqual(missing, [])

    def test_power_fx_page_lists_every_function(self) -> None:
        text = (DOCS / "03-power-fx-functions.md").read_text(encoding="utf-8")
        headings = {h.strip() for h in HEADING_RE.findall(text)}
        missing = [
            item["name"]
            for item in self.data["power_fx_functions"]
            if item["name"] not in headings
        ]
        self.assertEqual(missing, [])

    def test_readme_and_inventory_counts_match(self) -> None:
        readme = (DOCS / "README.md").read_text(encoding="utf-8")
        catalog = (DOCS / "00-inventory.md").read_text(encoding="utf-8")
        native = self.data["counts"]["native_actions"]
        self.assertIn(f"**{native}**", catalog)
        self.assertIn(str(native), readme)

    def test_clipboard_exceptions_captured(self) -> None:
        action = next(
            a
            for a in self.data["native_actions"]
            if a["id"] == "clipboard/get-clipboard-text"
        )
        self.assertTrue(action["exceptions"])

    def test_how_it_works_covers_every_native_action(self) -> None:
        how = DOCS / "how-it-works"
        missing = []
        for action in self.data["native_actions"]:
            path = how / f"native-{action['module']}.md"
            if not path.is_file():
                missing.append(f"file {path.name}")
                continue
            text = path.read_text(encoding="utf-8")
            if f"### {action['name']}\n" not in text:
                missing.append(action["id"])
            if "**Use case.**" not in text or "**Demonstration.**" not in text:
                missing.append(f"blocks {action['module']}")
            if "**Analogy.**" not in text or "**In combination.**" not in text:
                missing.append(f"combo {action['module']}")
        self.assertEqual(missing[:8], [], msg=f"{len(missing)} how-it-works gaps")

    def test_how_it_works_covers_power_fx_and_cloud(self) -> None:
        fx = (DOCS / "how-it-works" / "power-fx.md").read_text(encoding="utf-8")
        self.assertEqual(fx.count("**Use case.**"), 130)
        cloud_count = 0
        for action in self.data["cloud_connector_operations"]:
            path = DOCS / "how-it-works" / f"cloud-{action['module']}.md"
            self.assertTrue(path.is_file(), action["module"])
            text = path.read_text(encoding="utf-8")
            self.assertIn(f"### {action['name']}\n", text)
            cloud_count += 1
        self.assertGreaterEqual(cloud_count, 150)

    def test_combination_playbooks_exist(self) -> None:
        text = (DOCS / "06-combination-playbooks.md").read_text(encoding="utf-8")
        self.assertGreaterEqual(text.count("## "), 19)
        self.assertIn("**Use case.**", text)
        self.assertIn("**Analogy.**", text)
        self.assertIn("**Demonstration.**", text)
        self.assertIn("## 19. Ariba-style portal upload: drop PDF in a folder", text)

    def test_portal_uploads_ariba_guide(self) -> None:
        text = (DOCS / "07-portal-uploads-ariba.md").read_text(encoding="utf-8")
        self.assertIn("## Drop folder", text)
        self.assertIn("**Analogy", text)
        self.assertIn("AribaFolderUpload.robin", text)
        self.assertIn("AribaFolderUpload-package.zip", text)
        self.assertIn("Populate text field on web page", text)
        self.assertIn("Wait for window", text)
        self.assertIn("Send keys", text)
        self.assertIn("type=file", text)
        self.assertIn("Add Attachment", text)
        self.assertIn("Workbench", text)
        self.assertIn("C:\\RPA\\Ariba\\Inbox", text)
        self.assertIn("No PAD trigger", text)
        self.assertNotIn("Launch Outlook", text)
        self.assertNotIn("Process a work queue item", text)
        readme = (DOCS / "README.md").read_text(encoding="utf-8")
        self.assertIn("07-portal-uploads-ariba.md", readme)
        self.assertIn("flows/ariba-folder-upload", readme)
        combo = (DOCS / "06-combination-playbooks.md").read_text(encoding="utf-8")
        self.assertIn("AribaFolderUpload.robin", combo)
        self.assertIn("AribaFolderUpload-package.zip", combo)

    def test_connected_ariba_folder_upload_flow(self) -> None:
        flow_dir = DOCS / "flows" / "ariba-folder-upload"
        robin = (flow_dir / "AribaFolderUpload.robin").read_text(encoding="utf-8")
        mock = (flow_dir / "mock-portal" / "index.html").read_text(encoding="utf-8")
        captures = (flow_dir / "ui-elements.md").read_text(encoding="utf-8")
        how = (flow_dir / "README.md").read_text(encoding="utf-8")

        self.assertIn("IF PortalUrl = $'''''' THEN", robin)
        self.assertIn("Folder.GetFiles", robin)
        self.assertIn("ON BLOCK ERROR", robin)
        self.assertIn("WebAutomation.LaunchEdge.LaunchEdge", robin)
        self.assertIn("WebPageToNotContainText", robin)
        self.assertIn("WebPageToContainText", robin)
        self.assertIn("OCR.WaitForTextOnScreen", robin)
        self.assertIn("UIAutomation.WaitForWindow", robin)
        self.assertIn("MouseAndKeyboard.SendKeys", robin)
        self.assertIn("DateTime.GetCurrentDateTime", robin)
        self.assertIn("DateTime.Subtract", robin)
        self.assertIn("Text.ParseText", robin)
        self.assertNotIn("UI element event trigger", robin)
        self.assertNotIn("LaunchOutlook", robin)
        self.assertNotIn("Display.SelectFileDialog", robin)

        questions = [
            "Workbench",
            "Create Invoice",
            "Standard Invoice",
            "Add to Header",
            "Add Attachment",
            "Invoice submitted",
        ]
        for label in questions:
            self.assertIn(label, robin)
            self.assertIn(label, mock)

        for name in (
            "Txt_Username",
            "Txt_Password",
            "Btn_SignIn",
            "Tab_Workbench",
            "Tile_Orders",
            "Txt_OrderNumbers",
            "Btn_Apply",
            "Lnk_PONumber",
            "Btn_CreateInvoice",
            "Btn_StandardInvoice",
            "Txt_InvoiceNumber",
            "Txt_InvoiceDate",
            "Btn_AddToHeader",
            "Mnu_Attachment",
            "Inp_File",
            "Btn_ChooseFile",
            "Btn_AddAttachment",
            "Btn_Next",
            "Btn_Submit",
            "Btn_BackToWorkbench",
        ):
            self.assertIn(f"['{name}']", robin)
            self.assertIn(f"`{name}`", captures)

        self.assertIn("FOR 90", robin)
        self.assertIn("FOR 120", robin)
        self.assertIn("FOR 15", robin)
        self.assertIn("FOR 60", robin)
        self.assertIn("Timeout: 20", robin)
        self.assertIn("Tolerance is 10", how)
        self.assertIn("127.0.0.1:8765", robin)
        self.assertIn('id="file-input"', mock)
        self.assertIn("Loading", mock)
        self.assertIn("Invoice submitted", mock)
        self.assertIn("KB0399884", (flow_dir / "ariba-sources.md").read_text(encoding="utf-8"))
        self.assertTrue((flow_dir / "cloud" / "workflow-definition.json").is_file())
        self.assertIn("RunUIFlow_V2", (flow_dir / "cloud" / "README.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
