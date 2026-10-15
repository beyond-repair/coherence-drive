# Discovery: Rigorous derivation of W ≈ 0.08 from Coherence Drive thrust and fractal LDOS

## Discovery ID

DISC-0018

## Status

REJECTED as a derivation of numerical W ≈ 0.08 from the Coherence Drive thrust target, fractal LDOS asymmetry, the pinch-family heat-trace test, or the declared scale functional.

## Date Discovered

2026-10-02. Archive pass for previously unindexed beyond-repair/-ware-constant-derivation at the named evidence commit (tip merge of the Claim-0 offline-runnable sketch PR).

## Source Repositories

- beyond-repair/-ware-constant-derivation at commit ecb4795edcaf831c35ad18305fad051ec14b4880, branch main.
- Files: CLAIM_STATUS.md, README.md, STATUS_LOCK_2026-10-01.md, FALSIFICATION_2026-10-01_PINCH.md, SPECTRAL_ENDPOINT_POINTER.md, ADDENDUM_2026-10-02_SCALE_FUNCTIONAL.md, QUARANTINE_HISTORICAL_CLAIMS.md, PROOF_AND_DERIVATION_LEDGER.md, verify_pinch_cubic.py.
- Parent merge commit message: "Merge pull request #1 from beyond-repair/finish/claim0-offline-runnable-sketch".

## Original Evidence

CLAIM_STATUS.md at ecb4795edcaf831c35ad18305fad051ec14b4880, blob edfc539ce97dbd8d415f6ec78ce603efb9de498c, says: "Numerical W=0.08 from this action | **NOT DERIVED**"; "Pinch-family heat trace selects 0.08 | **REJECTED** on tested families"; "beta=-0.005888 independent of 0.08 | **CIRCULAR**"; "Experimental validation | **false**"; "Thrust validated | **false**". Scripts are "attackable symbolic / numeric checks, not experimental confirmation and not a derivation of W≈0.08 from the Coherence Drive thrust target."

README.md at the same commit, blob 21ec7a2894ed9daf71048e391a706dffaafc71ea: "This tree does not derive W ≈ 0.08. The GitHub description that ties W to a Coherence Drive thrust target is not a proof." Passing `ware-constant-checks` "is not a measurement of 0.08." Printed W from `verify_constant_W_action.py` is not 0.08; `verify_pinch_cubic.py` recovers root 0.08 because 0.08 is the input δ.

STATUS_LOCK_2026-10-01.md, blob 6a70789e0e191f065c4e9d71bc509120d5a2e516: "0.08 is falsified as a universal consequence of the tested (X, L, R) sequences." "Honest status: 0.08 is a phenomenological candidate, not a derived invariant." Cubic: δ=2/25, β=δ³−δ²=−92/15625=−0.005888; recovering 0.08 from that β is circular. Neumann dumbbell gap ratio crosses 0.08 as a level set with R'(w_*) ≠ 0, not a fixed point.

FALSIFICATION_2026-10-01_PINCH.md, blob 51908b2f3a3d166f1812dbfa77b690897d0c55d8: universal root near 0.08 falsified on tested families; no nonzero anomalous fixed point of the tested scale betas; Dirichlet dumbbell and metric-graph bridge have no sign change; conductance pinch β=1 identically.

SPECTRAL_ENDPOINT_POINTER.md, blob 4bba5970e05a1ac958962dbd6e5206a17239730f: "W = 0.08 and xi = 0.23 are not selected by K = omega^2 I - W L."

ADDENDUM_2026-10-02_SCALE_FUNCTIONAL.md, blob 07153dc608a5e656a6b629f41b3aa281742131da: declared I = Perimeter/√Area; β_I has no zero on tested Neumann/Dirichlet dumbbells; comparison with 0.08 is not reached.

QUARANTINE_HISTORICAL_CLAIMS.md, blob 3e42c033edfd87e44ff6a220af732df10552128f: quarantines ζ=0.08 / W=0.08 as a fundamental constant and the circular cubic.

Local run at ecb4795: `python verify_pinch_cubic.py` prints "circular: beta -92/15625 recovers input root 0.08".

## Discovery

The testable claim at this HEAD — and the GitHub description claim of a rigorous derivation of W ≈ 0.08 from the Coherence Drive thrust target and fractal LDOS asymmetry — is rejected by the repository's own fences. Numerical 0.08 is NOT DERIVED from the constant-W action. Pinch-family selection is REJECTED. The cubic β route is CIRCULAR. The scale functional has no stationary point on the tested families. experimental_validation and thrust_validated stay false. Claim level stays ≤2 / RUNNABLE SKETCH.

## Why It Matters

This is the dedicated derivation repository. Indexing its own rejection of the description claim closes the unread W≈0.08 derivation cluster without manufacturing novelty. It aligns with DISC-0002 / 0011 / 0014 / 0016 / 0017.

## Derivation

No derivation of 0.08, of thrust, or of LDOS-selected W is recorded in the cited files. This row does not supply one.

## Assumptions

Model and symbolic checks in this tree are as stated in CLAIM_STATUS.md. No laboratory measurement is assumed.

## New Results

None beyond what that evidence commit already states.

## Prior Art

DISC-0002 already fences thrust and W(n) off locked K. DISC-0011, DISC-0014, DISC-0016, and DISC-0017 already reject related 0.08 readings. This row indexes the derivation repo itself.

## Novelty Analysis

There is no novelty claim. Status is REJECTED.

## Falsification Attempts

In-repo: STATUS_LOCK, FALSIFICATION_2026-10-01_PINCH, verify_pinch_cubic.py, ADDENDUM scale-functional no stationary point. Local re-run confirmed circular recovery of 0.08.

## Experimental Validation

false (CLAIM_STATUS.md).

## Mathematical Status

Failed hypothesis / not derived.

## Patent Relevance

None established. Do not promote to PATENT CANDIDATE.

## Related Discoveries

- DISC-0002. Mathematical. Kernel fence: W(n) and thrust not consequences of locked K.
- DISC-0011. Mathematical. M2 0.08 pin is not a theorem from K.
- DISC-0014. Mathematical. Necks and geometric I do not select 0.08.
- DISC-0016. Historical. Pinch/scale do not derive the M2 seed.
- DISC-0017. Computational. SPARC χ² pass unsupported.
- DISC-0019. Historical. Same repository; constant-W identities stay DERIVATIVE and do not select 0.08.

## Open Questions

Whether some independently defined I[L_ell] has a universal stationary point remains open (STATUS_LOCK required order). Local dynamical W(x), Z_ren, and Lorentzian mode stay open per the ledger.

## Next Experiments

Do not cite the GitHub description as a proof. Prefer CLAIM_STATUS. Do not flip experimental_validation or thrust_validated.

## Reproduction Instructions

Check out beyond-repair/-ware-constant-derivation at ecb4795edcaf831c35ad18305fad051ec14b4880. Read CLAIM_STATUS.md, STATUS_LOCK_2026-10-01.md, FALSIFICATION_2026-10-01_PINCH.md. Run `python verify_pinch_cubic.py`.

## Evidence Log

- 2026-10-02. Read CLAIM_STATUS.md (edfc539c…), README.md (21ec7a28…), STATUS_LOCK (6a70789e…), FALSIFICATION (51908b2f…), SPECTRAL_ENDPOINT_POINTER (4bba5970…), ADDENDUM (07153dc6…), QUARANTINE (3e42c033…), PROOF_AND_DERIVATION_LEDGER (99cd097b…) at ecb4795edcaf831c35ad18305fad051ec14b4880.
- 2026-10-02. Local run: verify_pinch_cubic.py circular recovery of 0.08.
- Provenance, not a physics result. The -ware-constant-derivation description fetched on 2026-10-02 still says: "Rigorous mathematical derivation of the Ware Constant $  W \\approx 0.08  $ from the Coherence Drive thrust target and fractal LDOS asymmetry." It was not edited.

## Change History

- 2026-10-02. Initial archive entry. No Stage-1 freeze file was changed. No repository description was edited.
