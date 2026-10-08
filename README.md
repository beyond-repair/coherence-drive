<div align="center">

# COHERENCE DRIVE

### Research index — Stage 1 frozen · Claim-0 runnable sketch

[![RESEARCH](https://img.shields.io/badge/RESEARCH-f59e0b?style=for-the-badge)](https://github.com/beyond-repair/ADL-Governance)
[![Stage 1](https://img.shields.io/badge/Stage_1-FROZEN-22c55e?style=for-the-badge)](docs/MATH_THEORY_CLOSURE.md)
[![Claim](https://img.shields.io/badge/claim_%E2%89%A42-a855f7?style=for-the-badge)](docs/LAYER_MAP.md)
[![Claim-0](https://img.shields.io/badge/Claim--0-RUNNABLE_SKETCH-64748b?style=for-the-badge)](CLAIM_STATUS.md)

</div>

**RUNNABLE SKETCH — NOT A COMPLETE PRODUCT.**

This repository is the official Coherence Drive **research index** and
**discovery ledger**. It is **not** a propulsion engine, **not** a thruster
simulator, and **not** a physics-closed product. The GitHub repository
description that still says otherwise is **stale provenance**; the file-level
claim flags below govern.

Symbolic chain frozen. No silent energy-extraction claims.

```text
experimental_validation = false
thrust_validated = false
energy_extraction_validated = false
```

## Install, run, and test

```bash
git clone https://github.com/beyond-repair/coherence-drive.git
cd coherence-drive
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e .
coherence-drive
python -m coherence_drive
pytest -q
```

| Command | What passes | What it does not say |
|---------|-------------|----------------------|
| `coherence-drive` | Research-index summary; DISC-0001..0046 ledger status; locked claim flags all false; key docs present | Thrust, energy extraction, or a physics-closed engine |
| `pytest -q` | Docs presence, ledger parse consistency, claim flags remain false, no secret files | Product physics CI |

## Index (read these first)

- [Claim status](CLAIM_STATUS.md)
- [Governance](GOVERNANCE.md)
- [Math freeze](docs/MATH_THEORY_CLOSURE.md)
- [Layer map A–F](docs/LAYER_MAP.md)
- [Architecture](docs/ARCHITECTURE.md)
- [0.45 audit](docs/ZERO_POINT_FOUR_FIVE.md)
- [Survived / rejected / unresolved](docs/SURVIVED_REJECTED_UNRESOLVED.md)
- [Spectral endpoint](docs/SPECTRAL_ENDPOINT.md)
- [Master audit 2026-09-16](docs/MASTER_AUDIT_2026-09-16.md)
- [Sweep-159 conductance / shear pointer](docs/AUDIT_2026-09-21.md)
- [Portfolio math 2026-09-21](docs/PORTFOLIO_MATH_2026-09-21.md)
- [Pinch falsification 2026-10-01](docs/FALSIFICATION_2026-10-01_PINCH.md)
- [Status lock 2026-10-01](docs/STATUS_LOCK_2026-10-01.md)
- [Scale-functional addendum 2026-10-02](docs/ADDENDUM_2026-10-02_SCALE_FUNCTIONAL.md)
- [Discovery index](discoveries/INDEX.md)
- [Discovery ledger](discoveries/DISCOVERY_LEDGER.md)

Satellites: m2-renormalization-law · sierpinski-geometry-045 · topological-pinch · stress-tensor-modification · momentum-closure · thrust-target-30 · ware-constant-phenomenology · finite-gasket-spectral-derivatives · informational-flux-identity

2026-10-01: pinch-family heat trace does not derive 0.08. Stage 1 freeze is not reopened.

The discoveries archive indexes what named satellite repositories already say.
It does not change the Stage-1 freeze and does not raise any claim level.
