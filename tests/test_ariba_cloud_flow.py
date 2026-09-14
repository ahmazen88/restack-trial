"""Checks the importable Power Automate instant flow for Ariba folder upload."""

from __future__ import annotations

import importlib.util
import json
import unittest
import zipfile
from io import BytesIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FLOW = ROOT / "docs" / "power-automate-desktop" / "flows" / "ariba-folder-upload"
CLOUD = FLOW / "cloud"
PACK_PY = CLOUD / "pack.py"


def _load_pack():
    spec = importlib.util.spec_from_file_location("ariba_cloud_pack", PACK_PY)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class AribaCloudFlowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.pack = _load_pack()
        cls.workflow = json.loads(
            (CLOUD / "workflow-definition.json").read_text(encoding="utf-8")
        )
        cls.inputs = json.loads((CLOUD / "inputs.json").read_text(encoding="utf-8"))
        cls.robin = (FLOW / "AribaFolderUpload.robin").read_text(encoding="utf-8")
        cls.cloud_readme = (CLOUD / "README.md").read_text(encoding="utf-8")

    def test_workflow_is_instant_manual_not_scheduled(self) -> None:
        triggers = self.workflow["triggers"]
        self.assertEqual(set(triggers), {"manual"})
        manual = triggers["manual"]
        self.assertEqual(manual["type"], "Request")
        self.assertEqual(manual["kind"], "Button")
        blob = json.dumps(self.workflow)
        self.assertNotIn("Recurrence", blob)
        self.assertNotIn("shared_office365", blob)
        self.assertNotIn("shared_sharepointonline", blob)
        self.assertNotIn("shared_teams", blob)
        self.assertNotIn("When_a_file_is_created", blob)

    def test_run_desktop_flow_action_shape(self) -> None:
        run = self.workflow["actions"]["Run_a_flow_built_with_Power_Automate_for_desktop"]
        self.assertEqual(run["type"], "OpenApiConnection")
        host = run["inputs"]["host"]
        self.assertEqual(host["apiId"], "/providers/Microsoft.PowerApps/apis/shared_uiflow")
        self.assertEqual(host["operationId"], "RunUIFlow_V2")
        self.assertEqual(host["connectionName"], "shared_uiflow")
        self.assertEqual(host["connectionReferenceName"], "shared_uiflow")
        params = run["inputs"]["parameters"]
        self.assertEqual(params["runMode"], "attended")
        self.assertEqual(params["runSession"], "local")
        self.assertEqual(params["runPriority"], "normal")
        self.assertEqual(params["uiFlowId"], self.inputs["uiFlowIdPlaceholder"])
        self.assertEqual(run["runtimeConfiguration"]["timeout"], "PT2H")
        self.assertNotIn("authentication", run["inputs"])
        for item in self.inputs["inputs"]:
            self.assertIn(item["itemKey"], params)

    def test_trigger_fields_match_input_contract(self) -> None:
        props = self.workflow["triggers"]["manual"]["inputs"]["schema"]["properties"]
        self.assertEqual(self.workflow["triggers"]["manual"]["inputs"]["schema"]["required"], [])
        for item in self.inputs["inputs"]:
            field = props[item["triggerProperty"]]
            self.assertEqual(field["type"], "string")
            if item["sensitive"]:
                self.assertEqual(field["format"], "password")
                self.assertEqual(field["x-ms-content-hint"], "PASSWORD")

    def test_package_zip_legacy_layout(self) -> None:
        files = self.pack.package_files()
        prefix = f"Microsoft.Flow/flows/{self.pack.PACKAGE_GUID}"
        self.assertEqual(
            set(files),
            {
                "manifest.json",
                "Microsoft.Flow/flows/manifest.json",
                f"{prefix}/apisMap.json",
                f"{prefix}/connectionsMap.json",
                f"{prefix}/definition.json",
            },
        )
        manifest = json.loads(files["manifest.json"])
        self.assertEqual(manifest["schema"], "1.0")
        flow_res = manifest["resources"][self.pack.PACKAGE_GUID]
        self.assertEqual(flow_res["suggestedCreationType"], "New")
        self.assertEqual(flow_res["type"], "Microsoft.Flow/flows")
        self.assertEqual(flow_res["details"]["displayName"], "Ariba folder upload")

        envelope = json.loads(files[f"{prefix}/definition.json"])
        self.assertTrue(envelope["properties"]["instant"])
        self.assertEqual(
            envelope["properties"]["definition"]["actions"][
                "Run_a_flow_built_with_Power_Automate_for_desktop"
            ]["inputs"]["host"]["operationId"],
            "RunUIFlow_V2",
        )
        self.assertIn("shared_uiflow", envelope["properties"]["connectionReferences"])

        apis = json.loads(files[f"{prefix}/apisMap.json"])
        conns = json.loads(files[f"{prefix}/connectionsMap.json"])
        self.assertEqual(apis["shared_uiflow"], self.pack.API_GUID)
        self.assertEqual(conns["shared_uiflow"], self.pack.CONNECTION_GUID)

    def test_committed_zip_matches_packer(self) -> None:
        built = self.pack.write_zip_bytes()
        zip_path = CLOUD / "AribaFolderUpload-package.zip"
        self.assertTrue(zip_path.is_file(), "run cloud/pack.py to write the zip")
        with zipfile.ZipFile(BytesIO(zip_path.read_bytes())) as committed:
            committed_names = set(committed.namelist())
        with zipfile.ZipFile(BytesIO(built)) as expected:
            expected_names = set(expected.namelist())
        self.assertEqual(committed_names, expected_names)
        self.assertEqual(zip_path.read_bytes(), built)

    def test_robin_keeps_cloud_inputs(self) -> None:
        self.assertIn("IF PortalUrl = $'''''' THEN", self.robin)
        self.assertIn("IF DropFolder = $'''''' THEN", self.robin)
        self.assertIn("IF Username = $'''''' THEN", self.robin)
        self.assertIn("IF Password = $'''''' THEN", self.robin)
        self.assertNotIn(
            "SET PortalUrl TO $'''http://127.0.0.1:8765/index.html'''\nSET DropFolder",
            self.robin,
        )

    def test_readme_points_at_zip_and_forbids_auto_triggers(self) -> None:
        self.assertIn("AribaFolderUpload-package.zip", self.cloud_readme)
        self.assertIn("Import Package (Legacy)", self.cloud_readme)
        self.assertIn("RunUIFlow_V2", self.cloud_readme)
        self.assertIn("Manually trigger", self.cloud_readme)
        how = (FLOW / "README.md").read_text(encoding="utf-8")
        self.assertIn("AribaFolderUpload-package.zip", how)
        self.assertNotIn("Recurrence", self.cloud_readme)


if __name__ == "__main__":
    unittest.main()
