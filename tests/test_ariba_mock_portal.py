"""Optional browser check of the Ariba mock portal the PAD flow waits on."""

from __future__ import annotations

import threading
import unittest
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOCK = ROOT / "docs" / "power-automate-desktop" / "flows" / "ariba-folder-upload" / "mock-portal"


class _SilentHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args) -> None:  # noqa: A003
        return


class _MockHandler(_SilentHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(MOCK), **kwargs)


def _playwright_available() -> bool:
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        return False
    return Path("/usr/bin/google-chrome-stable").is_file()


@unittest.skipUnless(_playwright_available(), "Playwright + Chrome not installed")
class AribaMockPortalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.httpd = ThreadingHTTPServer(("127.0.0.1", 0), _MockHandler)
        cls.port = cls.httpd.server_address[1]
        cls.thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.httpd.shutdown()
        cls.httpd.server_close()
        cls.thread.join(timeout=5)

    def test_wizard_reaches_confirmation(self) -> None:
        from playwright.sync_api import sync_playwright

        pdf = Path("/tmp/rpa-inbox/INV-1001.pdf")
        pdf.parent.mkdir(parents=True, exist_ok=True)
        if not pdf.is_file():
            pdf.write_bytes(b"%PDF-1.4\ntrailer<<>>\n%%EOF\n")
        url = f"http://127.0.0.1:{self.port}/index.html"
        with sync_playwright() as p:
            browser = p.chromium.launch(
                executable_path="/usr/bin/google-chrome-stable",
                headless=True,
                args=["--no-sandbox"],
            )
            page = browser.new_page()
            page.goto(url)
            page.fill("#txt-username", "demo")
            page.fill("#txt-password", "demo")
            page.click("#btn-signin")
            page.locator("#btn-create-invoice").click(timeout=10000)
            page.locator("#q1-label").wait_for(state="visible", timeout=10000)
            page.fill("#txt-po", "INV-1001")
            page.click("#btn-next-q1")
            page.locator("#q2-label").wait_for(state="visible", timeout=10000)
            page.fill("#txt-invoice-number", "INV-1001")
            page.fill("#txt-invoice-date", "09/14/2026")
            page.click("#btn-next-q2")
            page.locator("#q3-label").wait_for(state="visible", timeout=10000)
            page.set_input_files("#file-input", str(pdf))
            page.click("#btn-next-q3")
            page.locator("#q4-label").wait_for(state="visible", timeout=10000)
            page.click("#btn-submit")
            page.locator("#screen-done").wait_for(state="visible", timeout=10000)
            self.assertIn("IR1042", page.inner_text("#confirm-banner"))
            browser.close()


if __name__ == "__main__":
    unittest.main()
