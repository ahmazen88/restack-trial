#!/usr/bin/env python3
"""Import and execute Hello n8n against a local Community instance."""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = os.environ.get("N8N_BASE_URL", "http://localhost:5678")
WORKFLOW_PATH = ROOT / "workflows" / "hello-n8n.json"


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


def request(
    method: str,
    path: str,
    data: dict | None = None,
    cookie: str | None = None,
) -> tuple[int, dict | str, str | None]:
    body = None if data is None else json.dumps(data).encode()
    req = urllib.request.Request(
        f"{BASE}{path}",
        data=body,
        method=method,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
    )
    if cookie:
        req.add_header("Cookie", cookie)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read().decode()
            set_cookie = resp.headers.get("Set-Cookie")
            parsed: dict | str
            try:
                parsed = json.loads(raw) if raw else {}
            except json.JSONDecodeError:
                parsed = raw
            return resp.status, parsed, set_cookie
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode()
        try:
            parsed = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            parsed = raw
        return exc.code, parsed, exc.headers.get("Set-Cookie")


def wait_ready(timeout_s: int = 180) -> None:
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        try:
            status, _, _ = request("GET", "/healthz")
            if status == 200:
                return
        except Exception:
            pass
        time.sleep(2)
    raise SystemExit(f"n8n did not become ready at {BASE}")


def cookie_header(set_cookie: str | None) -> str | None:
    if not set_cookie:
        return None
    return set_cookie.split(";", 1)[0]


def main() -> None:
    wait_ready()
    email, password = load_owner()
    status, payload, set_cookie = request(
        "POST",
        "/rest/login",
        {"emailOrLdapLoginId": email, "password": password},
    )
    cookie = cookie_header(set_cookie)
    if status not in (200, 201) or not cookie:
        # n8n 1.x used email/password
        status, payload, set_cookie = request(
            "POST",
            "/rest/login",
            {"email": email, "password": password},
        )
        cookie = cookie_header(set_cookie)
    if status not in (200, 201) or not cookie:
        raise SystemExit(f"login failed {status}: {payload}")

    workflow = json.loads(WORKFLOW_PATH.read_text())
    status, created, _ = request("POST", "/rest/workflows", workflow, cookie)
    if status not in (200, 201):
        raise SystemExit(f"import failed {status}: {created}")
    if not isinstance(created, dict):
        raise SystemExit(f"unexpected import payload: {created}")
    workflow_id = created.get("id") or created.get("data", {}).get("id")
    print(f"imported workflow id={workflow_id} status={status}")

    run_body = {
        "workflowData": created if "nodes" in created else workflow,
    }
    status, run, _ = request("POST", "/rest/workflows/run", run_body, cookie)
    print(f"run status={status}")
    print(json.dumps(run if isinstance(run, dict) else {"raw": run}, indent=2)[:4000])
    if status not in (200, 201):
        raise SystemExit("workflow run failed")


if __name__ == "__main__":
    main()
