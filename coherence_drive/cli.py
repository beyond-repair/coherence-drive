"""CLI: print research-index / discovery-ledger status. Not a thrust engine."""

from __future__ import annotations

import argparse
from pathlib import Path

from coherence_drive import CLAIM_FLAGS, __version__
from coherence_drive.ledger import (
    expected_ids,
    index_path,
    load_ledger,
    status_counts,
)
from coherence_drive.paths import repo_root

KEY_DOCS = (
    "README.md",
    "CLAIM_STATUS.md",
    "GOVERNANCE.md",
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

SATELLITES = (
    "m2-renormalization-law",
    "sierpinski-geometry-045",
    "topological-pinch",
    "stress-tensor-modification",
    "momentum-closure",
    "thrust-target-30",
    "ware-constant-phenomenology",
    "finite-gasket-spectral-derivatives",
    "informational-flux-identity",
)


def build_report(root: Path | None = None) -> str:
    base = root or repo_root()
    rows = load_ledger(base)
    counts = status_counts(rows)
    ids = [r.disc_id for r in rows]
    missing = [d for d in expected_ids() if d not in ids]
    present_docs = [d for d in KEY_DOCS if (base / d).is_file()]
    absent_docs = [d for d in KEY_DOCS if not (base / d).is_file()]

    lines = [
        f"coherence-drive {__version__} — Claim-0 research index / discovery ledger",
        "NOT a propulsion engine. NOT thrust. Stage-1 freeze unchanged.",
        "",
        "Locked claim flags (must remain false):",
    ]
    for key, value in CLAIM_FLAGS.items():
        lines.append(f"  {key} = {str(value).lower()}")
    lines.extend(
        [
            "",
            f"Discovery ledger rows: {len(rows)} (expected {len(expected_ids())})",
            f"  status counts: {counts}",
        ]
    )
    if missing:
        lines.append(f"  MISSING IDs: {missing}")
    else:
        lines.append("  DISC-0001..DISC-0037 present.")
    lines.append(f"  index: {index_path(base).relative_to(base)}")
    lines.extend(["", "Key index files:"])
    for doc in present_docs:
        lines.append(f"  present  {doc}")
    for doc in absent_docs:
        lines.append(f"  MISSING  {doc}")
    lines.extend(["", "Satellites (pointers only; not run from this CLI):"])
    for name in SATELLITES:
        lines.append(f"  - beyond-repair/{name}")
    lines.extend(
        [
            "",
            "Classification: RESEARCH / RUNNABLE SKETCH — NOT A COMPLETE PRODUCT.",
            "This CLI indexes repository statements. It does not validate physics.",
        ]
    )
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="coherence-drive",
        description=(
            "Print the Coherence Drive research-index summary and discovery "
            "ledger status. Does not claim thrust or raise claim flags."
        ),
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Repository root (default: parent of the installed package).",
    )
    args = parser.parse_args(argv)
    print(build_report(args.root), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
