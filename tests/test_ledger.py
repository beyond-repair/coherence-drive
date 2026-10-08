"""Discovery ledger DISC-0001..0037 parseable and consistent with INDEX.md."""

from pathlib import Path

from coherence_drive import EXPECTED_DISC_IDS
from coherence_drive.ledger import load_ledger, status_counts

ROOT = Path(__file__).resolve().parents[1]


def test_ledger_has_disc_0001_through_0037():
    rows = load_ledger(ROOT)
    ids = [r.disc_id for r in rows]
    assert ids == list(EXPECTED_DISC_IDS), f"ledger IDs mismatch: {ids}"


def test_ledger_statuses_are_known_vocabulary():
    allowed = {
        "KNOWN", "DERIVATIVE", "NOVELTY CANDIDATE", "STRONG NOVELTY CANDIDATE",
        "PATENT CANDIDATE", "UNRESOLVED", "REJECTED", "CONJECTURE", "THEOREM",
    }
    rows = load_ledger(ROOT)
    bad = [r for r in rows if r.status not in allowed]
    assert bad == [], f"unexpected statuses: {[(r.disc_id, r.status) for r in bad]}"


def test_confirmed_and_rejected_set_matches_preamble():
    rows = load_ledger(ROOT)
    by_status = status_counts(rows)
    # Confirmed (KNOWN) rows: DISC-0001, 0005, 0012 — three.
    # DERIVATIVE: 0003, 0004, 0007, 0019, 0021, 0022, 0023, 0025, 0026, 0028, 0031 — eleven.
    # NOVELTY CANDIDATE: 0020 — one.
    # CONJECTURE: 0027, 0030, 0034, 0035 — four (0035 archive-derived).
    # THEOREM: 0029, 0032, 0036 — three (mathematical status only, not novelty claims).
    # REJECTED: the rest (15).
    assert by_status.get("KNOWN") == 3
    assert by_status.get("DERIVATIVE") == 11
    assert by_status.get("NOVELTY CANDIDATE") == 1
    assert by_status.get("CONJECTURE") == 4
    assert by_status.get("THEOREM") == 3
    assert by_status.get("REJECTED") == 15


def test_index_mentions_every_disc_id():
    text = (ROOT / "discoveries" / "INDEX.md").read_text(encoding="utf-8")
    missing = [disc_id for disc_id in EXPECTED_DISC_IDS if disc_id not in text]
    assert missing == [], f"INDEX.md missing IDs: {missing}"


def test_per_disc_note_files_exist():
    math_dir = ROOT / "discoveries" / "mathematics"
    fail_dir = ROOT / "discoveries" / "failed-hypotheses"
    # Known note stems used in the archive (status drives folder).
    rows = load_ledger(ROOT)
    missing = []
    for row in rows:
        # Notes are named DISC-NNNN-*.md in mathematics/ or failed-hypotheses/
        matches = list(math_dir.glob(f"{row.disc_id}-*.md")) + list(
            fail_dir.glob(f"{row.disc_id}-*.md")
        )
        if not matches:
            missing.append(row.disc_id)
    assert missing == [], f"missing per-DISC note files: {missing}"
