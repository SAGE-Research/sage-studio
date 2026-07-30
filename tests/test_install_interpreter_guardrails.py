"""Guardrails for interpreter-bound package installation."""

from __future__ import annotations

import pathlib
import re

_REPO = pathlib.Path(__file__).parent.parent


def _read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def test_quickstart_installs_with_selected_interpreter():
    script = _read(_REPO / "quickstart.sh")

    assert 'PYTHON_BIN="${PYTHON_BIN:-python}"' in script
    assert '"$PYTHON_BIN" -m pip install' in script
    assert "sys.executable" in script


def test_install_surfaces_do_not_use_bare_pip():
    bare_pip = re.compile(r"(?<![-\\w])pip\\s+install\\b")

    for relative_path in (
        "README.md",
        "CONTRIBUTING.md",
        ".github/workflows/ci-test.yml",
    ):
        content = _read(_REPO / relative_path)
        assert not bare_pip.search(content), (
            f"{relative_path} must use an interpreter-bound pip command"
        )
