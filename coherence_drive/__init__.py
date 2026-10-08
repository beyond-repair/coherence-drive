"""Coherence Drive research index — Claim-0 runnable sketch.

This package indexes Stage-1 freeze docs and the discoveries archive.
It does not compute thrust, extract energy, or raise claim flags.
"""

__version__ = "0.1.0"

# Locked claim flags. Do not flip these to true from this package.
CLAIM_FLAGS = {
    "experimental_validation": False,
    "thrust_validated": False,
    "energy_extraction_validated": False,
}

EXPECTED_DISC_IDS = tuple(f"DISC-{i:04d}" for i in range(1, 28))
