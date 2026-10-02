"""Claim flags must remain false. Do not flip them."""

from pathlib import Path

from coherence_drive import CLAIM_FLAGS

ROOT = Path(__file__).resolve().parents[1]

FLAG_LINES = (
    "experimental_validation = false",
    "thrust_validated = false",
    "energy_extraction_validated = false",
)


def test_package_claim_flags_are_false():
    assert CLAIM_FLAGS["experimental_validation"] is False
    assert CLAIM_FLAGS["thrust_validated"] is False
    assert CLAIM_FLAGS["energy_extraction_validated"] is False


def test_readme_locks_claim_flags_false():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for line in FLAG_LINES:
        assert line in text, f"missing locked flag line: {line}"


def test_claim_status_denies_validation():
    text = (ROOT / "CLAIM_STATUS.md").read_text(encoding="utf-8").lower()
    assert "experimental_validation:** false" in text or "experimental_validation: false" in text
    assert "thrust_validated:** false" in text or "thrust_validated: false" in text
    assert "energy_extraction_validated:** false" in text or "energy_extraction_validated: false" in text
    assert "runnable sketch" in text
    assert "not" in text and "thrust" in text
