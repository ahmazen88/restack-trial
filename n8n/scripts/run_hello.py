#!/usr/bin/env python3
"""Import and execute Hello n8n against a local Community instance."""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from http.cookiejar import CookieJar
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = os.environ.get("N8N_BASE_URL", "http://localhost:5678")
WORKFLOW_PATH = ROOT / "workflows" / "hello-n8n.json"
TRIGGER = "When clicking ‘Execute workflow’"


def load_owner() -> tuple[str, str]:
    env_path = ROOT / ".local-owner.env"
    email = "local@n8n.local"
    password = ""
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            value = value.strip().strip("'").strip('"')
            if key == "N8N_OWNER_EMAIL":
                email = value
            elif key == "N8N_OWNER_PASSWORD":
                password = value
    if not password:
        raise SystemExit("Missing N8N_OWNER_PASSWORD in n8n/.local-owner.env")
    return email, password


def opener() -> urllib.request.OpenerDirector:
    return urllib.request.build_opener(urllib.request.HTTPCookieProcessor(CookieJar()))


def request(
    http: urllib.request.OpenerDirector,
    method: str,
    path: str,
    data: dict | None = None,
) -> tuple[int, dict | str]:
    body = None if data is None else json.dumps(data).encode()
    req = urllib.request.Request(
        f"{BASE}{path}",
        data=body,
        method=method,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
    )
    try:
        with http.open(req, timeout=90) as resp:
            raw = resp.read().decode()
            try:
                parsed: dict | str = json.loads(raw) if raw else {}
            except json.JSONDecodeError:
                parsed = raw
            return resp.status, parsed
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode()
        try:
            parsed = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            parsed = raw
        return exc.code, parsed


def wait_ready(http: urllib.request.OpenerDirector, timeout_s: int = 180) -> None:
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        try:
            status, _ = request(http, "GET", "/healthz")
            if status == 200:
                return
        except Exception:
            pass
        time.sleep(2)
    raise SystemExit(f"n8n did not become ready at {BASE}")


def find_workflow(http: urllib.request.OpenerDirector, name: str) -> str | None:
    status, payload = request(http, "GET", "/rest/workflows")
    if status != 200 or not isinstance(payload, dict):
        return None
    for row in payload.get("data", []):
        if row.get("name") == name:
            return str(row["id"])
    return None


def main() -> None:
    http = opener()
    wait_ready(http)
    email, password = load_owner()
    status, payload = request(
        http,
        "POST",
        "/rest/login",
        {"emailOrLdapLoginId": email, "password": password},
    )
    if status not in (200, 201):
        raise SystemExit(f"login failed {status}: {payload}")

    workflow = json.loads(WORKFLOW_PATH.read_text())
    name = workflow.get("name", "Hello n8n")
    workflow_id = find_workflow(http, name)
    if workflow_id is None:
        status, created = request(http, "POST", "/rest/workflows", workflow)
        if status not in (200, 201) or not isinstance(created, dict):
            raise SystemExit(f"import failed {status}: {created}")
        workflow_id = str(created.get("id") or created.get("data", {}).get("id"))
        print(f"imported workflow id={workflow_id}")
    else:
        print(f"reusing workflow id={workflow_id}")

    status, run = request(
        http,
        "POST",
        f"/rest/workflows/{workflow_id}/run",
        {"triggerToStartFrom": {"name": TRIGGER}},
    )
    if status not in (200, 201) or not isinstance(run, dict):
        raise SystemExit(f"run failed {status}: {run}")
    execution_id = str(run.get("data", {}).get("executionId") or run.get("executionId"))
    print(f"execution id={execution_id}")

    for _ in range(30):
        status, execution = request(http, "GET", f"/rest/executions/{execution_id}")
        if status == 200 and isinstance(execution, dict):
            data = execution.get("data", execution)
            exec_status = data.get("status")
            finished = data.get("finished")
            print(f"execution status={exec_status} finished={finished}")
            if exec_status in {"success", "error", "crashed", "canceled"} or finished:
                if exec_status != "success":
                    raise SystemExit(f"workflow did not succeed: {exec_status}")
                print("hello n8n run succeeded")
                return
        time.sleep(1)
    raise SystemExit("timed out waiting for execution")


if __name__ == "__main__":
    main()
