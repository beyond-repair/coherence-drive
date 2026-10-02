"""Resolve the repository root that holds docs/ and discoveries/."""

from __future__ import annotations

from pathlib import Path


def repo_root() -> Path:
    """Return the clone root (parent of the coherence_drive package)."""
    return Path(__file__).resolve().parents[1]
