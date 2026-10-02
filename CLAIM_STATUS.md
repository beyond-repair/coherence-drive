# Claim status — coherence-drive

**Classification:** RESEARCH  
**Claim level:** ≤ 2 (symbolic / Stage-1 freeze index); stranger path is **Claim-0**  
**Status:** RUNNABLE SKETCH — NOT A COMPLETE PRODUCT (Claim-0). Unverified as physics.  
**experimental_validation:** false  
**thrust_validated:** false  
**energy_extraction_validated:** false

This repository is the official Coherence Drive **research index** and
**discovery ledger**. It is **not** a propulsion engine and does **not**
certify thrust, energy extraction, or a physics-closed product.

## Explicit tokens (docs-presence)

The following remain **UNSUPPORTED** / false:

- experimental_validation — **false**
- thrust_validated — **false**
- energy_extraction_validated — **false**
- Any laboratory thrust or energy-extraction measurement — **UNSUPPORTED**
- Inheritance of W ≈ 0.08 as a universal consequence of locked K — **UNSUPPORTED**
  (see `docs/FALSIFICATION_2026-10-01_PINCH.md`, `docs/SPECTRAL_ENDPOINT.md`)
- GitHub repository description claiming a physics-closed engine — **stale provenance**;
  file-level claim flags and this document govern

## Feature matrix

| Feature | State |
|---------|-------|
| Stage-1 freeze docs (`docs/MATH_THEORY_CLOSURE.md` et al.) | VERIFIED present |
| Discovery archive (`discoveries/`, DISC-0001..0017) | VERIFIED present |
| Installable CLI (`coherence-drive`) | VERIFIED present |
| Docs-presence + ledger pytest | VERIFIED present |
| Propulsion / thruster simulator | ABSENT (out of scope) |
| Product physics CI | ABSENT (not required at Claim-0) |

Stranger path: `pip install -r requirements.txt && pip install -e .`, then
`coherence-drive` / `python -m coherence_drive` / `pytest -q`.
Constants are not refit. A green run is an index check, not a thrust result.

Stage-1 freeze is unchanged by the discoveries archive and by this Claim-0 sketch.
