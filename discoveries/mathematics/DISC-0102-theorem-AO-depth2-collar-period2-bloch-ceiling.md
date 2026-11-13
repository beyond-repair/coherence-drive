# Discovery: Depth-2 collar resistance ceiling via period-2 Bloch spectrum (Theorem AO)

## Discovery ID

DISC-0102

## Status

THEOREM

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0103.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 7f0099c3161ce2fa714c414cbae44bb316fc68f2 (main tip at archive time). Paths: GASKET.md "Theorem AO. Depth-2 collar resistance ceiling via period-2 Bloch spectrum" (after Theorem AN: ASSUMPTION, THEOREM AO, Proof (i)–(iv), Witness, Kept Failure AO.1, NOT THIS; Conjecture J.1 evidence paragraph and OPEN updated); CLAIM_STATUS.md (AO floors cited; audit-norm row now ‖F(n,0.45)‖≥0.222331); scripts/gasket_fractional_depth2_ceiling.py (new); README.md.

## Original Evidence

GASKET.md Theorem AO, for every α∈(0,1/2) and every even m≥2 (m=2^n, N=3m; M the Laplacian of the depth-2 collar H_n^(2) — edges of every unit triangle that meets the outer boundary or shares an edge with such a triangle — padded by zero on non-collar vertices; Theorems AA, AK, AM, AN used as stated):
1. 0≤M≤L, so M^α≤L^α (Löwner–Heinz), hence Q_α(u_n)≥(7/3)/R^col2 by the three-corner pairing of AM (ii).
2. The abstract period-2 fence (N-cycle, apex on every edge, every-other apex–apex edge) has a 4×4 Bloch symbol Ĥ(φ) on basis (x0,x1,a0,a1); G_00(φ;α)=(Ĥ(φ)^(−α))_{x0x0}; R^d2_α(m) < R^d2_∞(α)=(1/π)∫_0^{2π}G_00(φ;α)dφ (heat-kernel periodization; λ_min∼(7/32)φ², integrable iff α<1/2).
3. Three-corner defect δ₂(m)=R^col2(m)−R^d2(m)<0.55 "for every checked m (increasing toward ≈0.525)", so R^col2 < R^d2_∞+11/20.
4. At α=0.45 the repository states R^d2_∞≈4.270047 (AN fence ≈4.502104), ceiling ≈4.820047, Q≥0.484089, ‖F_frac‖≥0.316911 (≈1.038× AN's 0.305377); with σ_AK≈0.701556, ‖F(n,0.45)‖≥0.222331 (≈1.038× AN's 0.214239).

## Discovery

Theorem AO refines DISC-0100 by adding one inward layer to AN's boundary collar. On the gasket the extra layer consists exactly of the every-other apex–apex edges that close the smallest holes at odd boundary vertices (archive check: 0, 0, 6, 18, 42, 90, 186, 378, 762, 1530 new edges on levels 1–10, all apex–apex, same vertex set as the AN collar). The translation-invariant model becomes a period-2 fence with a 4×4 Bloch symbol. The proved audit floor at α=0.45 rises from 0.214239 to 0.222331. Incremental constant improvement. Convergence of ‖F(n,0.45)‖ and Conjecture J.1 (L≥0.70) stay OPEN.

## Why It Matters

Further (thin, ≈1.038×) sharpening of the proved positive floor for DISC-0034's sequence; still far below live ‖F(7)‖≈0.861 and below 0.70. Kept Failure AO.1 (DISC-0103) confirms the σ_AK chain cannot reach 0.70 through this ceiling either. Not thrust.

## Derivation

Repository proof, checked step by step in this archive:
1. Depth-2 collar edges ⊂ G_n ⇒ 0≤M≤L ⇒ M^α≤L^α; three-corner pairing of AM (ii) on M^α.
2. The infinite period-2 strip is block-circulant; Fourier in the supercell coordinate gives the 4×4 Hermitian Ĥ(φ). Archive closed forms: det Ĥ(φ)=84 sin²(φ/2), spec Ĥ(0)={0,4,4,6}, so λ_min=84 sin²(φ/2)/(λ₂λ₃λ₄)∼(84/96)(φ²/4)=(7/32)φ²; the Goldstone vector is uniform over the four supercell sites, |U_x0|²→1/4, so κ=(1/4)(7/32)^(−α) exactly (≈0.495408 at 0.45; repo "≈0.496").
3. Periodization as in AM (iv)/AN (ii) gives R^d2(m)<R^d2_∞ (archive: holds and is increasing on dyadic m≤2^16 at α∈{0.05,0.2,0.45,0.49}; α=0.5 control grows).
4. Defect δ₂(m) positive and increasing; witnessed below 0.55 (finite range; see Assumptions).
5. Floors: ‖F_frac‖=Q√21/7 (AA); AK (4)–(5).

## Assumptions

Spectral calculus as GASKET item 4; corner data (1,−1/2,0); Theorems AA (DISC-0072), AK (DISC-0094), AM (DISC-0098), AN (DISC-0100) as stated. α∈(0,1/2) only. As in DISC-0100, the defect bound δ₂(m)<0.55 is a finite-range witness, not a closed-form bound: the repository checks levels 2–6; this archive extends it to levels 1–10 (δ₂ = 0.277293, 0.339005, 0.393358, 0.420812, 0.433865, 0.439983, 0.442839, 0.444172, 0.444794, 0.445084; increments contract by ≈0.4665, geometric-tail extrapolation lim δ₂≈0.4453). The "at every level n" form of the floors rests on that step.

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_AO.log` (repository witness `python3 scripts/gasket_fractional_depth2_ceiling.py` at 7f0099c3161ce2fa714c414cbae44bb316fc68f2, EXIT 0, 84 PASS, 0 FAIL, "All checks passed. Not thrust.") and `/workspace/scratch-ifi/indep_theorem_AO.py` / `indep_theorem_AO.log` (own builder `/workspace/scratch-ifi/sg_indep_common.py` with integer lattice coordinates, own depth-2 collar from 3-cycles of G_n, own 4×4 symbol in a different basis order, no repo import, numpy only; EXIT 0, 81 PASS, 0 FAIL, ALL PASS):
- det Ĥ=84 sin²(φ/2) in both phases; λ_min/φ²→7/32; |U_x0|²→1/4; κ exact; G_00(φ)=G_00(2π−φ);
- **R^d2_∞(0.45)=4.269089239** by two independent quadratures (Gauss–Legendre after φ=πv^10 and φ=πv^20; midpoint with exact-κ singularity removal at 50k/200k/2M nodes; all agree to <1e-8). The repository's 4.270047 is an overestimate by ≈9.6e-4, traced to extracting κ by plain eigh at φ=1e-6 (relative κ error +3.6e-4; the repo's own 50k-vs-200k stability check already drifts by 1.4e-4). Because the error is upward, the repository ceiling 4.820047 and floors 0.484089 / 0.316911 / 0.222331 remain valid lower bounds; the accurate ceiling 4.819089 gives Q≥0.484185, ‖F_frac‖≥0.316974, ‖F‖≥0.222375. Digit erratum only; no inequality changes;
- period-2 Fourier R^d2(m) = dense pseudo-inverse (rel err ~5e-15); R^d2(m), m=2..256, reproduces the repo log to 1e-6; the repo's phase (hole at x0) has the larger R_∞ (gasket phase 4.238393), so the phase choice is the safe one;
- own depth-2 collar edge counts 27/69/153/321/657 on L2–6 match the repository; R^col2 ≤ R^col1 (AN collar) on all levels; R^col2 < R^d2_∞+0.55 on L1–10 (R^col2(L10)=3.097725);
- live levels 1–7 at α=0.45: L−M≥0 and L^α−M^α≥0; R_live≤R^col2; Q≥(7/3)/R^col2≥0.484089; ‖F_frac‖≥0.316911; ‖F‖≥0.222331; live ‖F‖ table 1.439599…0.880109 reproduced (L7 ‖F‖≈0.860818);
- floor digits 0.484089 / 0.316911 / 0.222331 reproduced from the repository ceiling; σ_AK=0.701556 recomputed; gain vs AN 1.0378×.

## Prior Art

Elementary: Löwner–Heinz, Bloch/Floquet reduction of a period-2 strip, spectral calculus on 4×4 Hermitians, heat-kernel periodization. Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only, on the same terms as DISC-0100 (repository proof with a finite-range defect step, verified here). Incremental sharpening of DISC-0100 / DISC-0094; not a novelty claim and not a Stage-1 / claim-level raise.

## Falsification Attempts

Rebuilt the gasket, the AN collar and the depth-2 collar independently; recomputed the Bloch integral with an exact Goldstone constant by two quadratures; matched Fourier against dense pseudo-inverses; checked the ceiling across α∈(0,1/2) and dyadic m≤2^16; extended δ₂ to level 10. Found one numerical defect (R^d2_∞ overstated by ≈9.6e-4, conservative) and one unsupported side remark (repo says δ₂ "increasing toward ≈0.525"; levels 1–10 point to ≈0.445, below the cap, so the remark is conservative and does not affect the theorem). No break of any stated inequality.

## Experimental Validation

None (pure mathematics / finite numerical witness).

## Mathematical Status

Proved in-repo up to the same finite-range defect step as DISC-0100; proof and witness verified; digit erratum on R^d2_∞ recorded above. Supersedes DISC-0100's numerical floor (DISC-0100 row not edited). DISC-0034 remains CONJECTURE for existence of lim ‖F(n,0.45)‖ and L≥0.70.

## Patent Relevance

None.

## Related Discoveries

- DISC-0100. Mathematical. Theorem AN; AO adds one inward layer to the collar, R^d2_∞+11/20.
- DISC-0094. Mathematical. Theorem AK; AO uses σ_AK with the new ‖F_frac‖ floor.
- DISC-0098. Mathematical. Theorem AM; three-corner pairing and periodization reused.
- DISC-0103. Failed hypothesis. Kept Failure AO.1.
- DISC-0034. Conjecture. Convergence and L≥0.70 stay OPEN (row not edited).

## Open Questions

A closed-form proof of δ₂(m)<0.55 (or of the limit ≈0.445) for all m would remove the finite-range step. Whether ‖F(n,0.45)‖ converges and whether L≥0.70 stay OPEN.

## Next Experiments

Optional: the repository could correct R^d2_∞(0.45) to ≈4.269089 by using κ=(1/4)(7/32)^(−α) in closed form (not done here; repository not edited).

## Reproduction Instructions

`git checkout 7f0099c3161ce2fa714c414cbae44bb316fc68f2 && python3 scripts/gasket_fractional_depth2_ceiling.py`. Archive: `python3 /workspace/scratch-ifi/indep_theorem_AO.py`. Logs: `/workspace/scratch-ifi/repo_theorem_AO.log`, `/workspace/scratch-ifi/indep_theorem_AO.log`.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Theorem AO at 7f0099c3161ce2fa714c414cbae44bb316fc68f2; repo witness EXIT 0 (84 PASS); independent check ALL PASS (81 PASS). Repository description still matches its claim fence (closed-surface identity / not a net force).

## Change History

- 2026-10-15. Initial archive entry.
