"""Discovery ledger parseable and consistent with INDEX.md and per-DISC notes."""

from pathlib import Path

from coherence_drive.ledger import load_ledger, status_counts

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_STATUSES = {
    "KNOWN",
    "DERIVATIVE",
    "NOVELTY CANDIDATE",
    "STRONG NOVELTY CANDIDATE",
    "PATENT CANDIDATE",
    "UNRESOLVED",
    "REJECTED",
    "CONJECTURE",
    "THEOREM",
}


def _note_dirs():
    return (
        ROOT / "discoveries" / "mathematics",
        ROOT / "discoveries" / "failed-hypotheses",
    )


def _disc_ids_from_note_files() -> list[str]:
    """DISC IDs present as note files, sorted by numeric id."""
    math_dir, fail_dir = _note_dirs()
    ids: set[str] = set()
    for directory in (math_dir, fail_dir):
        for path in directory.glob("DISC-????-*.md"):
            ids.add(path.name[:9])  # DISC-NNNN
    return sorted(ids, key=lambda s: int(s.split("-")[1]))


def test_ledger_has_disc_0001_through_0049():
    """Ledger IDs are contiguous from DISC-0001 through the max present in the archive."""
    rows = load_ledger(ROOT)
    ids = [r.disc_id for r in rows]
    assert ids, "ledger has no rows"
    note_ids = _disc_ids_from_note_files()
    assert note_ids, "no per-DISC note files found"
    max_n = max(int(i.split("-")[1]) for i in note_ids)
    expected = [f"DISC-{i:04d}" for i in range(1, max_n + 1)]
    assert ids == expected, (
        f"ledger IDs not contiguous DISC-0001..DISC-{max_n:04d}: {ids}"
    )
    assert note_ids == expected, (
        f"note-file IDs not contiguous DISC-0001..DISC-{max_n:04d}: {note_ids}"
    )


def test_ledger_statuses_are_known_vocabulary():
    rows = load_ledger(ROOT)
    bad = [r for r in rows if r.status not in ALLOWED_STATUSES]
    assert bad == [], f"unexpected statuses: {[(r.disc_id, r.status) for r in bad]}"


def test_confirmed_and_rejected_set_matches_preamble():
    """Status buckets are derived from the archive: allowed vocabulary, full coverage,
    and note-file folder matches status (REJECTED → failed-hypotheses/, else mathematics/).
    """
    rows = load_ledger(ROOT)
    math_dir, fail_dir = _note_dirs()
    by_status = status_counts(rows)

    bad_status = [(r.disc_id, r.status) for r in rows if r.status not in ALLOWED_STATUSES]
    assert bad_status == [], f"unexpected statuses: {bad_status}"

    assert sum(by_status.values()) == len(rows)
    assert len(rows) == len(_disc_ids_from_note_files())

    wrong_folder = []
    missing = []
    for row in rows:
        matches_math = list(math_dir.glob(f"{row.disc_id}-*.md"))
        matches_fail = list(fail_dir.glob(f"{row.disc_id}-*.md"))
        if not matches_math and not matches_fail:
            missing.append(row.disc_id)
        elif row.status == "REJECTED":
            if not matches_fail or matches_math:
                wrong_folder.append((row.disc_id, row.status))
        else:
            if not matches_math or matches_fail:
                wrong_folder.append((row.disc_id, row.status))
    assert missing == [], f"missing per-DISC note files: {missing}"
    assert wrong_folder == [], f"note file folder mismatches status: {wrong_folder}"


def test_index_mentions_every_disc_id():
    text = (ROOT / "discoveries" / "INDEX.md").read_text(encoding="utf-8")
    rows = load_ledger(ROOT)
    missing = [row.disc_id for row in rows if row.disc_id not in text]
    assert missing == [], f"INDEX.md missing IDs: {missing}"


def test_per_disc_note_files_exist():
    math_dir, fail_dir = _note_dirs()
    rows = load_ledger(ROOT)
    missing = []
    for row in rows:
        matches = list(math_dir.glob(f"{row.disc_id}-*.md")) + list(
            fail_dir.glob(f"{row.disc_id}-*.md")
        )
        if not matches:
            missing.append(row.disc_id)
    assert missing == [], f"missing per-DISC note files: {missing}"
