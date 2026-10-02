"""Docs-presence checks. Not physics validation."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = (
    "README.md",
    "CLAIM_STATUS.md",
    "GOVERNANCE.md",
    "LICENSE",
    "pyproject.toml",
    "requirements.txt",
    "docs/MATH_THEORY_CLOSURE.md",
    "docs/LAYER_MAP.md",
    "docs/ARCHITECTURE.md",
    "docs/SURVIVED_REJECTED_UNRESOLVED.md",
    "docs/SPECTRAL_ENDPOINT.md",
    "docs/STATUS_LOCK_2026-10-01.md",
    "docs/FALSIFICATION_2026-10-01_PINCH.md",
    "docs/ADDENDUM_2026-10-02_SCALE_FUNCTIONAL.md",
    "discoveries/INDEX.md",
    "discoveries/DISCOVERY_LEDGER.md",
)


def test_required_docs_exist():
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    assert missing == [], f"missing required docs: {missing}"


def test_readme_is_research_claim0_sketch():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "RESEARCH" in text
    assert "RUNNABLE SKETCH" in text
    assert "pip install" in text
    assert "Stage 1" in text or "Stage-1" in text
    assert "not" in text.lower() and "thrust" in text.lower()


def test_no_secret_files_in_tree():
    banned_names = {".env", "credentials.json", "secrets.yaml", "id_rsa"}
    found = []
    for path in ROOT.rglob("*"):
        if path.is_file() and path.name in banned_names:
            # ignore anything under .git or venvs if present
            parts = set(path.parts)
            if ".git" in parts or ".venv" in parts or "egg-info" in str(path):
                continue
            found.append(str(path.relative_to(ROOT)))
    assert found == [], f"secret-like files present: {found}"
