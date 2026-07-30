"""Keep public Studio documentation aligned with the repository surface."""

from __future__ import annotations

import pathlib
import re

_REPO = pathlib.Path(__file__).parent.parent
_PUBLIC_DOCS = (
    _REPO / "README.md",
    _REPO / "CONTRIBUTING.md",
    _REPO / ".github" / "copilot-instructions.md",
)


def _read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def test_public_docs_do_not_reference_removed_runtime_paths():
    removed_paths = (
        "config/backend/api.py",
        "src/sage/studio/chat_manager.py",
        "application/chat_manager.py",
        "runtime/chat/",
    )

    for path in _PUBLIC_DOCS:
        content = _read(path)
        for removed_path in removed_paths:
            assert removed_path not in content, (
                f"{path.relative_to(_REPO)} references removed path {removed_path}"
            )


def test_readme_local_markdown_links_exist():
    readme = _read(_REPO / "README.md")
    local_links = re.findall(r"\[[^\]]+\]\((?!https?://|#)([^)]+)\)", readme)

    for target in local_links:
        path_text = target.split("#", maxsplit=1)[0]
        assert (_REPO / path_text).exists(), f"README link target does not exist: {target}"


def test_readme_names_current_backend_entrypoint():
    readme = _read(_REPO / "README.md")

    assert "sage.studio.api.app:app" in readme
    assert "src/sage/studio/api/app.py" in readme
