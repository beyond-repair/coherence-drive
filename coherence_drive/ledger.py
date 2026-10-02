"""Parse discoveries/DISCOVERY_LEDGER.md rows. Archive only; not physics."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from coherence_drive import EXPECTED_DISC_IDS
from coherence_drive.paths import repo_root

ROW_RE = re.compile(
    r"^\|\s*(DISC-\d{4})\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|"
)


@dataclass(frozen=True)
class DiscoveryRow:
    disc_id: str
    discovery: str
    repository: str
    type_: str
    status: str


def ledger_path(root: Path | None = None) -> Path:
    return (root or repo_root()) / "discoveries" / "DISCOVERY_LEDGER.md"


def index_path(root: Path | None = None) -> Path:
    return (root or repo_root()) / "discoveries" / "INDEX.md"


def parse_ledger(text: str) -> list[DiscoveryRow]:
    rows: list[DiscoveryRow] = []
    for line in text.splitlines():
        match = ROW_RE.match(line.strip())
        if not match:
            continue
        rows.append(
            DiscoveryRow(
                disc_id=match.group(1).strip(),
                discovery=match.group(2).strip(),
                repository=match.group(3).strip(),
                type_=match.group(4).strip(),
                status=match.group(5).strip(),
            )
        )
    return rows


def load_ledger(root: Path | None = None) -> list[DiscoveryRow]:
    path = ledger_path(root)
    return parse_ledger(path.read_text(encoding="utf-8"))


def expected_ids() -> tuple[str, ...]:
    return EXPECTED_DISC_IDS


def status_counts(rows: list[DiscoveryRow]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        counts[row.status] = counts.get(row.status, 0) + 1
    return counts
