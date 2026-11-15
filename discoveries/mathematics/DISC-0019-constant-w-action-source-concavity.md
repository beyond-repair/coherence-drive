# Discovery: Constant-W action source and concavity

## Discovery ID

DISC-0019

## Status

DERIVATIVE

## Date Discovered

2026-10-02. Archive pass for beyond-repair/-ware-constant-derivation at the named evidence commit.

## Source Repositories

beyond-repair/-ware-constant-derivation at commit ecb4795edcaf831c35ad18305fad051ec14b4880. Files: CONSTANT_W_ACTION_PRINCIPLE.md, PROOF_AND_DERIVATION_LEDGER.md (P1–P9), verify_constant_W_action.py, CLAIM_STATUS.md, README.md.

## Original Evidence

CLAIM_STATUS.md at ecb4795edcaf831c35ad18305fad051ec14b4880 states Constant-W action / source / concavity **DERIVED** (checkable via `verify_constant_W_action.py`), while Numerical W=0.08 from this action is **NOT DERIVED**.

CONSTANT_W_ACTION_PRINCIPLE.md, blob 32c0843787ac6157a9a98d34eb5ee96a23647e3c: Euclidean Gaussian Γ_E = S_W + (1/2) Tr ln K[W]; one-loop V''_1-loop(W) < 0 on K ≻ 0; spectral pole as W → (ω²/λ_max)⁻; finite normalized graph bound W < 1/6 at λ_max=6, ω=1. Explicitly does **not** derive W=0.08, W_★=1/(4π), ξ=0.23, or healthy local W(x).

PROOF_AND_DERIVATION_LEDGER.md, blob 99cd097b3ea73b28b7bf4e991f86cc0d1ee4d458: P1–P9 lock the model form K(W)=ω²I−WL, the Gaussian identity, the spectral source δS_W/δW = (1/2) Tr[K⁻¹ L], strict concavity V''<0, and the finite-graph window W < 1/6. "Only constant-W steps 1–5 are fully locked as theorems." Quarantine: 0.08, 0.23, W(n), propulsion NOT DERIVED.

README.md: `verify_constant_W_action.py` passes when trace source matches the spectral sum and V''<0 on a seed-0 random positive matrix; that matrix is not λ_max=6; printed W_crit is not 1/6 and printed W is not 0.08.

Local run at ecb4795: `python verify_constant_W_action.py` PASS with λ_max≈28.79, W_crit≈0.0347, W≈0.0139, matching Tr/spec sources, V''≈−1843.

## Discovery

The constant-W Euclidean action identities (Gaussian effective action, spectral source, one-loop concavity, finite-graph positivity window) are derivative of classical Gaussian path-integral algebra under the model assumption K=ω²I−WL. They do not select a numerical W inside the window and do not yield thrust.

## Why It Matters

Separating DERIVATIVE constant-W infrastructure from the REJECTED 0.08 derivation claim (DISC-0018) in the same repository keeps Stage-1 claim levels from drifting when verifiers exit 0.

## Derivation

No new derivation is added here. The repository already writes P1–P9 and the constant-W freeze. This archive does not add another form.

## Assumptions

Real scalar quadratic Euclidean action; constant W; K(W)≻0; L=L†⪰0. S_W is not derived. Continuum local W(x) is not assumed.

## New Results

None.

## Prior Art

Classical Euclidean Gaussian effective action (1/2) Tr ln K. Finite-gasket W < 1/6 window already indexed via DISC-0003 / DISC-0005.

## Novelty Analysis

There is no novelty claim. Status is DERIVATIVE.

## Falsification Attempts

In-repo verifiers; CLAIM_STATUS refuses upgrade to numerical 0.08. Local re-run PASS without printing 0.08.

## Experimental Validation

None. experimental_validation false.

## Mathematical Status

Derivative classical / model-specific identities.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0018. Historical. Same repository; 0.08 from thrust/LDOS REJECTED.
- DISC-0003. Mathematical. Finite-gasket trace / W < 1/6 window.
- DISC-0002. Mathematical. Constant-W bounds do not select thrust or 0.08.

## Open Questions

Local dynamical W(x), Z_ren, Lorentzian pole, and any independent scale functional with a universal stationary point remain open.

## Next Experiments

Keep constant-W checks separate from phenomenological 0.08. Do not treat exit 0 as a measurement of 0.08.

## Reproduction Instructions

Check out beyond-repair/-ware-constant-derivation at ecb4795edcaf831c35ad18305fad051ec14b4880. Read CONSTANT_W_ACTION_PRINCIPLE.md and PROOF_AND_DERIVATION_LEDGER.md P1–P9. Run `python verify_constant_W_action.py`.

## Evidence Log

- 2026-10-02. Read CONSTANT_W_ACTION_PRINCIPLE.md (32c08437…), PROOF_AND_DERIVATION_LEDGER.md (99cd097b…), CLAIM_STATUS.md, README.md at ecb4795edcaf831c35ad18305fad051ec14b4880.
- 2026-10-02. Local run: verify_constant_W_action.py PASS; printed W ≠ 0.08.

## Change History

- 2026-10-02. Initial archive entry. No Stage-1 freeze file was changed.
