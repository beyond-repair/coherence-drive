# Discovery: Every shift-invariant polynomial reading is zero or surface-dependent (Theorem Q)

## Discovery ID

DISC-0053

## Status

KNOWN

## Date Discovered

2026-10-08 (America/New_York). Archive pass after DISC-0052; indexes unread Theorems Q/R at the same IFI commit as DISC-0051/0052.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit d22771de4351d86c5b04d52e36bcfe1a0a22744f (Theorem Q introduced at 014b8d083388fdd5f2e602f45371639899a60412; HEAD includes Theorem S). Paths: README.md "Theorem Q. Every shift-invariant polynomial reading, of any order and degree, is zero or surface-dependent" (Assumption Q, Theorem Q.1–Q.3, Lemma Q.0, Proofs, Kept Failure Q.1, Witness, NOT THIS); CLAIM_STATUS.md Theorem Q row (VERIFIED, not thrust); scripts/nonlinear_reading_flux.py.

## Original Evidence

Inside Assumption Q (shift-invariant O(3)-covariant constant-coefficient polynomial readings of any order and degree; static massless C6; isolated device), every vacuum surface S satisfies G(S) = −∫_{outside S} ∂_j T^{ij}. On-shell conserved readings give G = 0 on every vacuum surface; otherwise G moves with S (Q.3 via Lemma Q.0). Witness: four readings T1..T4; exact Fraction divergence identities 25/25; on harmonic Ψ_h, div T1 and div T2 vanish; recorded div T3/T4 at (1,1/2,−1); Lemma Q.0 ranks 16 and 25; quadrature on three spheres and dilation monopole coefficients.

## Discovery

Decay of multipole derivatives (D+m ≥ 3), the divergence theorem on exterior regions, and the fact that harmonic jets are realised by point charges (Lemma Q.0). Classical continuum identities applied to the whole shift-invariant polynomial family of readings of the frozen rank-2 symbol.

## Why It Matters

It closes every shift-invariant polynomial reading (any order, any degree) under static massless C6: either G vanishes on every vacuum surface or it is surface-dependent (see DISC-0054).

## Derivation

Checked. Q.1: exterior multipole bound O(r^{−(D+m)}) with D+m ≥ 3 from O(3) parity and shift invariance; flux through large spheres → 0; divergence theorem. Q.2: vacuum integrand vanishes. Lemma Q.0: Fourier support argument for P(∂)|w|^{−1}. Q.3: jet matching plus a small outward bump. No gap.

## Assumptions

Assumption Q (a family of readings, not a change to the freeze); C6 static massless A_0; isolated device; d = 3.

## New Results

Archive `/workspace/scratch-ifi/indep_nonlinear_Q.py`: exact Fraction identities for div T1..T4 hold 25/25; Ψ_h harmonic; div T1/T2 vanish on Ψ_h; recorded div T3 = (858843/32, 327369/8, −970097/128) and div T4 = (19927/8, −45683/4, 1024) at (1,1/2,−1); Lemma Q.0 ranks 16 (K=3) and 25 (K=4) reproduced via sympy Coulomb jets. Repository script `scripts/nonlinear_reading_flux.py` at d22771de: all checks passed (quadrature |G|≤4e−14 for T1; three-sphere and dilation figures match README).

## Prior Art

Classical: multipole expansion of exterior harmonic functions; divergence theorem; Maxwell-stress divergence (special case T1); isotropic tensors / O(3) parity.

## Novelty Analysis

None. Classical identities applied to the repository's polynomial reading family.

## Falsification Attempts

Attacked the four divergence formulas, the harmonic vanishing, the recorded exact values, and Lemma Q.0 ranks with an independent Fraction/sympy implementation. No discrepancy. Full quadrature witness re-run from the repository script.

## Experimental Validation

None.

## Mathematical Status

Classical results; proof correct.

## Patent Relevance

None.

## Related Discoveries

- DISC-0044, DISC-0048. Mathematical. Two-derivative and linear special cases.
- DISC-0054. Failed hypothesis. Kept Failure Q.1.
- DISC-0055. Mathematical. Theorem R drops shift invariance.

## Open Questions

Non-shift-invariant readings (closed by Theorem R / DISC-0055); screened field equations; non-polynomial readings; Ψ_info ≠ A_0; the 0.45 mesh solve (Stage 2 stays OPEN).

## Next Experiments

None from the archive.

## Reproduction Instructions

`git checkout d22771de4351d86c5b04d52e36bcfe1a0a22744f && python3 scripts/nonlinear_reading_flux.py`. Archive: `python3 /workspace/scratch-ifi/indep_nonlinear_Q.py`.

## Evidence Log

- 2026-10-08 ~8:20pm EDT. Recorded from README Theorem Q at d22771de4351d86c5b04d52e36bcfe1a0a22744f; script rerun OK; archive checks as above.

## Change History

- 2026-10-08. Initial archive entry.
