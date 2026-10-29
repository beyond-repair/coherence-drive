# Discovery: Theorem BY, a deeper sandwich certifies θ̂_21≠0 and the Toeplitz sections T_18, T_19, T_20 of BX's spectral measure positive definite

## Discovery ID

DISC-0179

## Status

THEOREM in the mathematical sense only (repository proof = AU (3)'s certified routine with new parameters, plus BX.2/BX.3 and an arb LDL* Toeplitz certificate with a Weyl bound; computer-assisted). Method KNOWN (same routine as DISC-0116/0173/0176; Carathéodory–Toeplitz positivity). Constants: novelty UNRESOLVED (not searched). Closed form of F, G*, t_max, t_min: UNRESOLVED. Not thrust.

## Date Discovered

2026-10-29 (America/New_York), ~4:54am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 4e57bb8631cdd295862ec1cb636fd89577a3e3f8 (committed 2026-10-29 3:56am EDT).

## Original Evidence

GASKET.md Theorem BY (heading line 3152; BY.1 line 3159; BY.2 line 3160; BY.3 line 3161; proof line 3163; Kept Failure BY.3 line 3165; Observation (no claim) line 3167; open list line 3169; witness paragraph line 3175), CLAIM_STATUS.md new row (line 81), README.md (line 1140 and reproduce list), scripts/gasket_fractional_profile_toeplitz.py (new, 128 lines), scripts/cli.py, tests/test_cli.py.

## Discovery

Setting as in Theorem BX (DISC-0177): F=θ the 1-periodic profile in t=log_5 u, θ̂_k=a_k−ib_k, m≥0 the periodic spectral measure with θ̂_k=(π/ln5)m̂_k/sin π(γ+iωk), ρ_k=|m̂_k|/m̂_0.

- BY.1: AU (3)'s routine with period [5^−341,5^−340], 1024 cells, sandwich b=u=40/41, mpmath.iv outward at 380 digits, node cap 1e310 encloses ⟨F⟩ to ±9.3e−134 and a_k, b_k (k≤21) to ±1.9e−133 (BW: ±2.0e−113). θ̂_k≠0 for every 1≤|k|≤21; a_21=−2.55838576504077e−113, b_21=−9.60025191043711e−113, |θ̂_21|≥9.93e−113. AU's and BV.4's tables reproduced.
- BY.2: ρ_k∈[0.60,0.92] for every k≤21, ρ_21=0.706371132…; BX.3's bound holds for k≤21.
- BY.3: T_n=(m̂_(i−j)) is positive definite for n=18,19,20 (exact-midpoint LDL* of T_n−2ε_nI in arb, ε_n≥‖E‖_F; Weyl); smallest pivots 5.33e−15, 4.51e−16, 1.21e−16; ε_20≤3.0e−32.
- Kept Failure BY.3: ν is not carried by ≤19 geometric series λ_j5^Z (m has ≥20 support points per period). This is DISC-0178's hypothesis with r widened from ≤16 to ≤19; recorded there, no new ID (same precedent as Kept Failure BT.5 → DISC-0114).
- Observation (no claim): T_21 not certified at this precision.

## Why It Matters

Answers two finite questions BX left open (θ̂_21≠0; T_18≻0) and pushes the lower bound on the support size of m from 17 to 20 points per period. It narrows, but does not decide, whether ν is purely atomic.

## Derivation

Repository proof (GASKET.md line 3163): BY.1 is AU (3)'s routine with new parameters; a nonzero real or imaginary part certifies θ̂_k≠0. BY.2 is BX.2's exact factorisation in acb plus BX.3. BY.3: T_n=T_n^mid+E, E Hermitian, ‖E‖_2≤‖E‖_F≤ε_n, so T_n^mid≻2ε_nI (certified by positive pivots) gives T_n≻ε_nI≻0. The same certificate passes on an exact 3-atom measure for T_3 and fails for T_4 (sanity check).

## Assumptions

As stated in the repository and not re-run there: AQ (3), BN.1, BS.1, BT.2, BU.1, BV.2, AU (1); Assumption BX (Nevanlinna characterisation of Stieltjes functions, literature); BX.2, BX.3 and BX.5's rank lemma; AU (3)'s certified routine imported unchanged.

## New Results

- θ̂_21 certified nonzero; ρ_21=0.70637 inside the band, so the certified ρ band now covers k≤21 with no visible limit (Conjecture BV.6, DISC-0175, unchanged).
- T_18, T_19, T_20 ≻0; ≥20 atoms per period.
- Observation of mine (floats, not a repo claim): T_21's smallest eigenvalue is ≈2.14e−27 in two independent runs (300 digits/depth 5^−440 and 340 digits/depth 5^−520, agreeing to 6 digits). That is below the repository's 2ε_21≈1.3e−26, which is why BY could not certify it, but it is positive in floats. ρ_22≈0.6466 (floats), still in the band. Evidence only.

## Prior Art

Same as DISC-0176/0177: exponentially decaying log-periodic Fourier coefficients (Grabner–Woess 1997 on Sierpinski graphs), Stieltjes representations, and the Carathéodory–Toeplitz rank bound for finitely atomic measures are classical. Re-running a certified routine at higher precision is standard. No search for these constants.

## Novelty Analysis

Method KNOWN; precision and range extension of DISC-0176/0177. Constants not searched: UNRESOLVED.

## Falsification Attempts

Independent mpmath script /workspace/scratch-ifi/indep_theorem_BY.py on the box (own η-series r_∞, no repo code imported, 80-node rectangle rule; two precisions: 300 digits at depth 5^−440, 340 digits at depth 5^−520). Results identical between precisions:
- a_21, b_21 match all 15 printed digits; |θ̂_21|=9.9353e−113≥9.93e−113.
- ρ_21=0.706371132108; ρ_k∈[0.60,0.92] and BX.3's bound for every k≤21.
- Toeplitz: smallest LDL* pivots 5.32739e−15 (T_18), 4.5109e−16 (T_19), 1.20763e−16 (T_20), matching the printed 5.33e−15, 4.51e−16, 1.21e−16; smallest eigenvalues 5.11e−23, 1.20e−24, 9.06e−26, all far above ε_20≤3.0e−32 and far above my float error.
- One FAIL line in my log is my own threshold (I required λ_min(T_20)>1e−25; it is 9.06e−26). Not a repository defect; the substantive check (λ_min ≫ ε_20) passes.

**Presentation note (no claim affected).** The Observation says T_21's "21st midpoint pivot falls below 2ε_21". In my run the 21st pivot of T_21 itself is ≈9.5e−18; what fails is the shifted matrix T_21−2ε_21I, whose last pivot turns negative because λ_min(T_21)≈2.1e−27<2ε_21. The conclusion (T_21 undecided at this precision) is correct; the wording is loose.

## Experimental Validation

Not applicable (pure mathematics on a graph). Computational: repo witness scripts/gasket_fractional_profile_toeplitz.py (see Evidence Log; /workspace/scratch-ifi/repo_theorem_BY.log on the box); archive indep_theorem_BY.py as above. Repo reports pytest -k "not reproduce": 38 passed (not re-run here).

## Mathematical Status

Theorem (repository proof) with computer-assisted certified constants (interval enclosures not re-certified here; reproduced in 300- and 340-digit floats).

## Patent Relevance

None. The repository's NOT THIS fence: functions on a graph, not a flux, not thrust.

## Related Discoveries

DISC-0177 (Theorem BX; T_17 → T_20), DISC-0178 (Kept Failure BX.5; scope widened to r≤19 by Kept Failure BY.3, stays REJECTED), DISC-0176 (Theorem BW; θ̂_k≠0 k≤20 → k≤21), DISC-0175 (Conjecture BV.6; one more data point, stays CONJECTURE), DISC-0116 (Theorem AU; routine reused).

## Open Questions

Is ν purely atomic, with finitely or infinitely many atoms per period? T_21≻0 (floats say λ_min≈2.1e−27)? θ̂_k≠0 for k≥22 (~5.3 digits per k)? Conjecture BV.6; closed forms of F, G*, t_max, t_min; carried-over items.

## Next Experiments

Certify T_21 by shrinking ε_21 below ~1e−27 (BY's ε_21≈6.5e−27 must drop below ~1e−27, i.e. θ̂_k radii roughly ten times smaller than BY's 1.9e−133; BW observed that the sandwich order, not the depth, sets the radius). Track λ_min(T_n) in floats for n up to ~30 to see whether the decay is geometric (consistent with a continuous part) or stalls.

## Reproduction Instructions

```
git clone https://github.com/beyond-repair/informational-flux-identity
git -C informational-flux-identity checkout 4e57bb8631cdd295862ec1cb636fd89577a3e3f8
cd informational-flux-identity && python3 scripts/gasket_fractional_profile_toeplitz.py   # needs python-flint, mpmath, sympy; ~18 min
```

## Evidence Log

- 2026-10-29 ~4:54am EDT. Indexed; independent float checks pass at two precisions (one over-strict threshold of mine noted); repo witness EXIT 0 (717 s; 13 ok lines, "all Theorem BY checks passed"; |θ̂_21|≥9.935299e−113, ε_20≤2.96e−32, T_21 not certified with ‖E‖_F≤6.3e−27).

## Change History

- 2026-10-29. Initial archive entry.
