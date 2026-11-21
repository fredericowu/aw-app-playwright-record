"""Playwright Record app.

The version has a single source of truth: ``aw-app.json``, the only file the
release automation bumps. Everything else derives from it.
"""
import json
from pathlib import Path


def _manifest_version() -> str:
    try:
        manifest = Path(__file__).resolve().parent.parent / "aw-app.json"
        return json.loads(manifest.read_text())["version"]
    except (OSError, KeyError, ValueError):
        return "0.0.0+unknown"


__version__ = _manifest_version()
