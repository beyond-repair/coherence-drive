# Discovery: Multi-scale spectral L^α neutrality; nested harmonicity special to α=1 (Theorem X)

## Discovery ID

DISC-0065

## Status

DERIVATIVE

## Date Discovered

2026-10-09 (America/New_York). Archive pass after DISC-0063 / DISC-0064.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 3959241bfd57e6f68e7e906fe10351f446163666. Paths: GASKET.md "Theorem X. Multi-scale spectral L^α: neutrality; nested harmonicity is special to α=1" (Assumption item 7 + spectral calculus item 4, Theorem X parts 1–3, Proof of (1)–(2), Proof of (3) witnessed, Kept Failures X.1–X.2, NOT THIS); scripts/gasket_multiscale_fractional.py; CLAIM_STATUS.md (multi-scale spectral L^α row VERIFIED); README.md gasket summary pointing at Theorem X.

## Original Evidence

On the multi-scale edge set L_ms = Σ_{g=0}^n λ^g L^(g), apply spectral calculus to form L_ms^α. Corner data (1, −1/2, 0). Then for every level n≥1 and λ>0: (1) both L_ms-currents and L_ms^α-currents are neutral and lie on the Schur line (1, −4/5, −1/5) by the cut identity and S_3 symmetry; (2) at α=1 the solution equals the combinatorial harmonic and the audit recovers Theorem W exactly; (3) for α∈(0,1) nested harmonicity fails — L_ms u_H = 0 on the fine interior but L_ms^α u_H ≠ 0 there, so u_ms,α ≠ u_H (witnessed: nest residual ∈(0.18,0.45) and ‖u−u_H‖_∞∈(0.09,0.66) through levels 1–6 at λ=1, α=0.45).

## Discovery

Structural lift of Theorems F/H/J neutrality+Schur and Theorem W (α=1 recovery) to spectral fractional calculus on the multi-scale gasket graph; nested annihilation is special to the linear operator α=1.

## Why It Matters

Settles the multi-scale spectral L^α structure left open by DISC-0063's NOT THIS. Does not decide finest-edge α=0.45 (DISC-0034 stays OPEN). Not thrust.

## Derivation

Checked. Cut identity + L_ms^α 1 = 0 ⇒ neutrality; S_3 ⇒ Schur; α=1 ⇒ Theorem W; part (3) is a uniqueness+witness argument (if L_ms^α u_H vanished interiorly then u_ms,α = u_H, but residual and potential gap are O(0.1)). Same substance class as DISC-0063 / DISC-0051 (gasket lifts), not analogous to Theorems J/K/L.

## Assumptions

Multi-scale edge set (Assumption item 7); spectral calculus on L_ms ⪰ 0 (item 4); corner data (1, −1/2, 0); Theorems F, H, J, W.

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_X.log` (repository witness EXIT:0, all Theorem X / X.1–X.2 checks passed) and `/workspace/scratch-ifi/indep_theorem_X.py` / `indep_theorem_X.log`: α=1 recovers W through level 4 for λ∈{1,5/3,2}; neutrality+Schur through level 6 at λ=1, α=0.45; nested residual ≫0; recorded ‖F_L‖ / ‖F_α‖ match GASKET.md; X.1 freeze-break and X.2 constant-factor-break PASS.

## Prior Art

Theorems F/H/J (cut identity, fractional neutrality, Schur); Theorem W / DISC-0063 (multi-scale harmonic); Kigami nested harmonicity (fails for spectral powers). Classical spectral calculus on finite Laplacians.

## Novelty Analysis

DERIVATIVE: neutrality/Schur already in DISC-0031/0032; α=1 recovers DISC-0063; nested-failure is a witnessed corollary of uniqueness. No novelty claimed. Not elevated to THEOREM (elementary relative to J/K/L; part (3) numerical through level 6).

## Falsification Attempts

Reran the witness; independent rebuild matched records; attempted λ=1 freeze inheritance for α=0.45 fails (‖F_L(6)‖≈10.59 vs freeze 5.73); attempted level-independent constant relating multi-scale and finest audits fails (ratio grows 3.85× from n=1 to n=5). No discrepancy with the repository claim.

## Experimental Validation

None (pure mathematics / finite numerical witness).

## Mathematical Status

Correct elementary corollary of cut identity + S_3 + Theorem W, with nested-failure witnessed through level 6.

## Patent Relevance

None.

## Related Discoveries

- DISC-0031 / DISC-0032. Mathematical. Neutrality, Schur, audit-norm algebra.
- DISC-0063. Mathematical. Theorem W recovered at α=1.
- DISC-0066 / DISC-0067. Failed hypotheses. Freeze inheritance and finest-edge coincidence rejected.
- DISC-0034. Conjecture. Combinatorial α=0.45 limit still OPEN.

## Open Questions

Finest-edge α=0.45 zero-versus-positive (OPEN). Continuum fractional kernel not evaluated.

## Next Experiments

None from the archive.

## Reproduction Instructions

`git checkout 3959241bfd57e6f68e7e906fe10351f446163666 && PYTHONPATH=scripts python3 scripts/gasket_multiscale_fractional.py`. Archive logs: `/workspace/scratch-ifi/repo_theorem_X.log`, `/workspace/scratch-ifi/indep_theorem_X.log`.

## Evidence Log

- 2026-10-09. Recorded from GASKET.md Theorem X at 3959241bfd57e6f68e7e906fe10351f446163666; repo witness EXIT:0; independent check ARCHIVE_INDEP_THEOREM_X_PASS. Repository description still matches its claim fence.

## Change History

- 2026-10-09. Initial archive entry.
- 2026-10-15. Indexed on PR #3 branch (verified 2026-10-09 ~3:10am EDT; not pushed in that slice). No content change to the classification.
