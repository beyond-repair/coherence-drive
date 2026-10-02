# Discovery: Ware surface integral inherits 0.08 from the pinch test

## Discovery ID

DISC-0015

## Status

REJECTED as a derivation of 0.08 and as a certification of momentum closure.

## Date Discovered

2026-10-02. Archive pass after momentum-closure HEAD moved past the DISC-0002 snapshot.

## Source Repositories

- beyond-repair/momentum-closure at commit 5643f4b0ee388eb81616b4c897f593fefdbfd605, branch main.
- File: PINCH_FALSIFICATION_POINTER_2026-10-01.md.
- DISC-0002 cited this repository at 36949d00023eef7edabd875ca5836ad1ca39f312 for the sentence that momentum for locked K is undefined, not measured zero. That sentence is not reopened here.

## Original Evidence

PINCH_FALSIFICATION_POINTER_2026-10-01.md at 5643f4b0ee388eb81616b4c897f593fefdbfd605 says: "A surface-integral identity that assumes a Ware term does not derive the number 0.08. The 2026-10-01 pinch-family sequence produced no universal Q, and beta = -0.005888 equals (2/25)^3 - (2/25)^2."

The same file says: "This file does not reopen or certify the momentum-closure calculation."

It sets experimental_validation false, thrust_validated false, and energy_extraction_validated false. It points at the canonical falsification note in beyond-repair/-ware-constant-derivation and does not reproduce that note's calculation here.

## Discovery

HEAD changed, from 36949d00023eef7edabd875ca5836ad1ca39f312 to 5643f4b0ee388eb81616b4c897f593fefdbfd605. The new testable statement is the pointer: a surface-integral identity that assumes a Ware term does not derive 0.08, the pinch-family sequence produced no universal Q, and the recorded beta is the stated algebraic value rather than a new momentum result. The file refuses to certify the momentum-closure calculation.

## Why It Matters

The GitHub description still says the repository proves that the Ware term supplies real net momentum flux. The new file says the pinch test does not hand this repository the number 0.08 and does not certify the calculation. That is a failed inheritance, not a measured force.

## Derivation

No derivation of 0.08 or of net momentum flux is recorded in the new file. The beta sentence is quoted as the file states it. This row does not recompute it and does not add an equation.

## Assumptions

The rejection uses only the pointer text. It does not assume the canonical falsification note was re-derived in this pass. It does not treat ConvergenceTensor as a physical residual. tensor.py at this commit says it "never certifies a physical residual by itself."

## New Results

None. No claim level is raised.

## Prior Art

DISC-0002 already records that momentum for this K is undefined, not measured zero, and that 0.08 is not a consequence of K. DISC-0011 already rejects an engineering 0.08 pin as a theorem from K. DISC-0014 records the neck-side refusal to select 0.08. This entry indexes only the momentum-closure pointer added after 36949d00023eef7edabd875ca5836ad1ca39f312.

## Novelty Analysis

There is no novelty claim. Status is REJECTED. The relation to DISC-0002 and DISC-0014 is historical: the pointer says it does not reopen the calculation and does not inherit 0.08 from the pinch test.

## Falsification Attempts

The pointer is the in-file attack. It denies both a derived 0.08 and a universal Q from the 2026-10-01 pinch-family sequence.

## Experimental Validation

None. The pointer sets experimental_validation false.

## Mathematical Status

Rejected as a derivation and as a certification. Not a theorem. The repository does not contain a proof or a prior-art comparison for this pointer.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0002. Historical. Momentum undefined, not measured zero, stays that earlier row. Not duplicated here.
- DISC-0011. Mathematical. 0.08 is already rejected as a theorem from K on a different pin.
- DISC-0014. Historical. The pinch-side refusal to select 0.08 is the test this pointer refuses to inherit.

## Open Questions

Mesh-converged residual force remains the unsupported token already stated in CLAIM_STATUS.md and GOVERNANCE.md at this HEAD. It is not given a new row. The analytic dipole fixture in docs/MOMENTUM_CLOSURE_FRAMEWORK_REVIEW.md remains a specified target. README.md still lists "Analytic radiation fixtures + positivity" as PLANNED (specified). The framework review says the working v1.6 artifact is not present in this repo. That fixture was not classified as KNOWN, THEOREM, or a patent candidate, because this tree does not execute it and does not contain a proof. SPECTRAL_ENDPOINT_POINTER.md still says discrete and continuum momentum are undefined for the locked Gaussian K, not measured to be zero. That sentence stays on DISC-0002.

## Next Experiments

Do not cite the pointer as a momentum closure, a universal Q, or a derivation of 0.08. Do not treat a planned dipole fixture or ConvergenceTensor bookkeeping as a mesh-converged residual.

## Reproduction Instructions

Read PINCH_FALSIFICATION_POINTER_2026-10-01.md at 5643f4b0ee388eb81616b4c897f593fefdbfd605. For the unchanged fences, read SPECTRAL_ENDPOINT_POINTER.md, CLAIM_STATUS.md, and the analytic-fixture row in README.md at the same commit. The DISC-0002 snapshot of this repository is 36949d00023eef7edabd875ca5836ad1ca39f312.

## Evidence Log

- 2026-10-02. list_commits on main: HEAD 5643f4b0ee388eb81616b4c897f593fefdbfd605, message "Pointer: momentum-closure does not inherit 0.08 from the pinch test." Parent snapshot used by DISC-0002 was 36949d00023eef7edabd875ca5836ad1ca39f312.
- 2026-10-02. Read PINCH_FALSIFICATION_POINTER_2026-10-01.md, SPECTRAL_ENDPOINT_POINTER.md, CLAIM_STATUS.md, README.md, GOVERNANCE.md, and docs/MOMENTUM_CLOSURE_FRAMEWORK_REVIEW.md at 5643f4b0ee388eb81616b4c897f593fefdbfd605.
- Provenance, not a physics result. The momentum-closure description fetched on 2026-10-02 still says: "Full momentum closure for the Coherence Drive using surface integral of the stress tensor + Poynting flux. Proves the Ware term supplies real net momentum flux." It was not edited. The same description was already logged on DISC-0002.

## Change History

- 2026-10-02. Initial archive entry. No Stage-1 freeze file was changed. No repository description was edited.
