"""Tests for the Power Automate Desktop documentation catalog."""

from __future__ import annotations

import runpy
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent


class PadDocsTests(unittest.TestCase):
    def test_inventory_and_pages_are_consistent(self) -> None:
        runpy.run_path(str(SCRIPTS / "verify_docs.py"), run_name="__main__")


if __name__ == "__main__":
    unittest.main()
