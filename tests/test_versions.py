import json
from pathlib import Path

from playwright_record_app import __version__

ROOT = Path(__file__).resolve().parents[1]


def test_all_version_metadata_is_synchronized():
    # aw-app.json is the only file the release bot bumps; the package version
    # and pyproject derive from it, so nothing may hardcode a second copy.
    manifest_version = json.loads((ROOT / "aw-app.json").read_text())["version"]
    pyproject = (ROOT / "pyproject.toml").read_text()
    assert 'dynamic = ["version"]' in pyproject
    assert manifest_version == __version__
