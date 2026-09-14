#!/usr/bin/env python3
"""Build the Power Automate Import Package (Legacy) zip for Ariba folder upload.

The zip is what you upload at make.powerautomate.com → My flows → Import →
Import Package (Legacy). Microsoft does not let a raw .robin file become a
desktop flow on import; paste AribaFolderUpload.robin in PAD first, then bind
it in the imported cloud action.
"""

from __future__ import annotations

import json
import zipfile
from io import BytesIO
from pathlib import Path
from zipfile import ZipInfo

HERE = Path(__file__).resolve().parent
WORKFLOW_PATH = HERE / "workflow-definition.json"
OUT_ZIP = HERE / "AribaFolderUpload-package.zip"

PACKAGE_GUID = "9a4b8c76-71a3-43d0-8482-60718293a4b5"
FLOW_GUID = "ab5c9d87-82b4-44e1-9593-718293a4b5c6"
API_GUID = "bc6dae98-93c5-45f2-a6a4-8293a4b5c6d7"
CONNECTION_GUID = "cd7ebfa9-a4d6-4603-b7b5-93a4b5c6d7e8"
TELEMETRY_GUID = "de8fc0ba-b5e7-4714-88c6-a4b5c6d7e890"
DISPLAY_NAME = "Ariba folder upload"
CREATED_TIME = "2026-09-14T00:00:00.0000000Z"
ZIP_DATE = (2026, 9, 14, 0, 0, 0)
UIFLOW_API = "/providers/Microsoft.PowerApps/apis/shared_uiflow"


def load_workflow() -> dict:
    return json.loads(WORKFLOW_PATH.read_text(encoding="utf-8"))


def connection_references() -> dict:
    return {
        "shared_uiflow": {
            "id": UIFLOW_API,
            "apiName": "uiflow",
            "connectionName": "shared_uiflow",
            "source": "Embedded",
            "tier": "NotSpecified",
        }
    }


def definition_envelope(workflow: dict | None = None) -> dict:
    inner = workflow if workflow is not None else load_workflow()
    return {
        "name": FLOW_GUID,
        "id": f"/providers/Microsoft.Flow/flows/{FLOW_GUID}",
        "type": "Microsoft.Flow/flows",
        "properties": {
            "apiId": "/providers/Microsoft.PowerApps/apis/shared_logicflows",
            "displayName": DISPLAY_NAME,
            "definition": inner,
            "connectionReferences": connection_references(),
            "flowFailureAlertSubscribed": False,
            "isManaged": False,
            "instant": True,
        },
    }


def root_manifest() -> dict:
    return {
        "schema": "1.0",
        "details": {
            "displayName": DISPLAY_NAME,
            "description": (
                "Instant cloud flow: you drop PDFs in a folder, then Run. "
                "Calls the AribaFolderUpload desktop flow attended on the local "
                "machine. No schedule, Outlook, SharePoint, or notifications."
            ),
            "createdTime": CREATED_TIME,
            "packageTelemetryId": TELEMETRY_GUID,
            "creator": "N/A",
            "sourceEnvironment": "",
        },
        "resources": {
            PACKAGE_GUID: {
                "type": "Microsoft.Flow/flows",
                "suggestedCreationType": "New",
                "creationType": "Existing, New, Update",
                "details": {"displayName": DISPLAY_NAME},
                "configurableBy": "User",
                "hierarchy": "Root",
                "dependsOn": [API_GUID, CONNECTION_GUID],
            },
            API_GUID: {
                "id": UIFLOW_API,
                "name": "shared_uiflow",
                "type": "Microsoft.PowerApps/apis",
                "suggestedCreationType": "Existing",
                "details": {"displayName": "Desktop flows"},
                "configurableBy": "System",
                "hierarchy": "Child",
                "dependsOn": [],
            },
            CONNECTION_GUID: {
                "type": "Microsoft.PowerApps/apis/connections",
                "suggestedCreationType": "Existing",
                "creationType": "Existing",
                "details": {"displayName": "shared_uiflow"},
                "configurableBy": "User",
                "hierarchy": "Child",
                "dependsOn": [API_GUID],
            },
        },
    }


def inner_manifest() -> dict:
    return {
        "packageSchemaVersion": "1.0",
        "flowAssets": {"assetPaths": [PACKAGE_GUID]},
    }


def package_files() -> dict[str, bytes]:
    workflow = load_workflow()
    dumps = lambda obj: json.dumps(obj, indent=2, ensure_ascii=False).encode("utf-8") + b"\n"
    prefix = f"Microsoft.Flow/flows/{PACKAGE_GUID}"
    return {
        "manifest.json": dumps(root_manifest()),
        "Microsoft.Flow/flows/manifest.json": dumps(inner_manifest()),
        f"{prefix}/apisMap.json": dumps({"shared_uiflow": API_GUID}),
        f"{prefix}/connectionsMap.json": dumps({"shared_uiflow": CONNECTION_GUID}),
        f"{prefix}/definition.json": dumps(definition_envelope(workflow)),
    }


def write_zip_bytes(files: dict[str, bytes] | None = None) -> bytes:
    files = files if files is not None else package_files()
    buf = BytesIO()
    with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name in sorted(files):
            info = ZipInfo(filename=name, date_time=ZIP_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, files[name])
    return buf.getvalue()


def pack(out: Path | None = None) -> Path:
    dest = out if out is not None else OUT_ZIP
    dest.write_bytes(write_zip_bytes())
    return dest


def main() -> None:
    path = pack()
    print(f"Wrote {path} ({path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
