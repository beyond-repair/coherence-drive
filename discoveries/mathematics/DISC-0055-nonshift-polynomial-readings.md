# Discovery: Dropping shift invariance, every polynomial reading is still zero or surface-dependent (Theorem R)

## Discovery ID

DISC-0055

## Status

KNOWN

## Date Discovered

2026-10-08 (America/New_York). Same archive pass as DISC-0053.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit d22771de4351d86c5b04d52e36bcfe1a0a22744f (Theorem R introduced at b6bf27d78cb468a141da395066fe4dd2726cfc3c). Paths: README.md "Theorem R. Dropping shift invariance: every polynomial reading is still zero or surface-dependent" (Assumption R, Lemma R.0, Theorem R.1–R.4, Proofs, Kept Failure R.1, Witness, NOT THIS); CLAIM_STATUS.md Theorem R row (VERIFIED, not thrust); scripts/nonshift_reading_flux.py.

## Original Evidence

Undifferentiated factors (δ^{ij}Ψ, δ^{ij}Ψ², Ψ ∂^i∂^jΨ, …) allowed. Lemma R.0: conservation is graded in (m,D). R.1: if e=f=0, Q.1 holds. R.2: on-shell conserved ⇒ e=f=0 and G=0 on every vacuum surface. R.3: otherwise G moves with S. R.4: δ^{ij}Ψ² has a nonzero shape-dependent dilation limit 2πQ²(1/a − (1+a²)/(2a²)ln((1+a)/(1−a))) C/a. Witness: U1/U2/U3; exact identities; R.4 closed form (−42.690617678, 28.460411786, −14.230205893).

## Discovery

O(3) parity (D even), graded conservation, multipole decay for D+m≥3, and the Coulomb monopole limit for Ψ². Classical; applied to the non-shift-invariant polynomial family of the frozen symbol.

## Why It Matters

It closes the gap left by Theorem Q: dropping shift invariance does not open a surface-independent nonzero G (see DISC-0056).

## Derivation

Checked. Lemma R.0 by λ,μ scaling. R.2: on h=x, div(eδΨ+fδΨ²)=(e,0,0)+(2fx,0,0) forces e=f=0. R.4: uniform convergence R A_0(Ry)→Q/|y| on the off-centre unit sphere; explicit angular integral. No gap.

## Assumptions

Assumption R; C6 static massless; isolated device; d=3; massless equation only for δΨ² reading.

## New Results

Archive `/workspace/scratch-ifi/indep_nonshift_R.py`: div U1/U2/U3 identities 25/25; U1 not shift-invariant (U1[Ψ+1]−U1[Ψ]=H); div U1 vanishes on Ψ_h; recorded div U2/U3; among 49 integer (e,f) pairs only (0,0) conserved on h=x; R.4 closed form and independent monopole quadrature agree to 1e−9 with README. Repository script `scripts/nonshift_reading_flux.py` at d22771de: all checks passed.

## Prior Art

Classical: divergence theorem; multipole expansion; electrostatic energy/flux integrals of Ψ² on off-centre spheres.

## Novelty Analysis

None. Classical identities applied to the repository's non-shift-invariant polynomial family.

## Falsification Attempts

Attacked divergence formulas, non-shift-invariance of U1, graded e/f conservation, and the R.4 closed form vs monopole quadrature. No discrepancy.

## Experimental Validation

None.

## Mathematical Status

Classical results; proof correct.

## Patent Relevance

None.

## Related Discoveries

- DISC-0053. Mathematical. Theorem Q (shift-invariant special case).
- DISC-0048. Mathematical. Linear undifferentiated term eδΨ is P.2 / R special case.
- DISC-0056. Failed hypothesis. Kept Failure R.1.

## Open Questions

Screened field equations (ΔΨ=m²Ψ); non-polynomial readings; position-dependent coefficients; Ψ_info ≠ A_0; Stage 2 mesh.

## Next Experiments

None from the archive.

## Reproduction Instructions

`git checkout d22771de4351d86c5b04d52e36bcfe1a0a22744f && python3 scripts/nonshift_reading_flux.py`. Archive: `python3 /workspace/scratch-ifi/indep_nonshift_R.py`.

## Evidence Log

- 2026-10-08 ~8:20pm EDT. Recorded from README Theorem R at d22771de4351d86c5b04d52e36bcfe1a0a22744f; script rerun OK; archive checks as above.

## Change History

- 2026-10-08. Initial archive entry.
