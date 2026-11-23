# Discovery: Theorem BH, the corner boundary layer of the L^α Dirichlet extension has a universal limit profile

## Discovery ID

DISC-0149

## Status

THEOREM in the mathematical sense only (repository's own proof in GASKET.md; BH.5 constants computer-assisted via python-flint arb; BH.6 derived from AT and BD.4 as stated). Method KNOWN (spectral decimation, harmonic measure, contraction). Constants novelty UNRESOLVED. Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~10:00pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 156d8ce80c73147e3dc8aa34cbcea2ce6e42d989 (2026-10-22 21:36:58 −04:00). Files: GASKET.md "Theorem BH" (new section after Kept Failure BG.1), CLAIM_STATUS.md (new row "Corner boundary layer of the L^α Dirichlet extension"), scripts/gasket_fractional_corner_layer.py (new, 409 lines), tests/test_cli.py (FractionalCornerLayerTests), scripts/cli.py, pyproject.toml (new optional extra "certify").

## Original Evidence

GASKET.md Theorem BH.1–BH.6 with proofs; certificate in scripts/gasket_fractional_corner_layer.py (742386 monotone cells, arb balls, AS re-run for J_r, J_w).

## Discovery

With level-1 s-harmonic weights α₁(s)=(s+4)/((s+2)(s+5)), β(s)=(s+6)/((s+2)(s+5))≤3/5:
- BH.1: exact corner-cell decomposition of (L_n+s)^−1 x_C on 2^−(n−k)V_k.
- BH.2: h_N(z;ν_b)−h_N(z;ν_c)=(x_b−x_c)∏_{i<N}(5+p^i z)^−1 exactly; |h_N(z;ν)−x_a η(z)|≤2‖x‖(3/5)^N with η(z)=Σ_j α₁(p^j z)∏_{i<j}β(p^i z) (α-free, η(0)=1, strictly decreasing, η≤2/(2+z)); r_∞(s)=1/(2+s−2η(s)); u_n(ν_b)−u_n(ν_c)=(x_b−x_c)I_n/D_n, 0<I_n/D_n≤5^−n.
- BH.3: for α<γ=log3/log5, u_n(2^−n ξ)→d̄+x_a Θ(ξ), Θ universal (x_b, x_c drop out), reflection-symmetric, 0<Θ<1.
- BH.4: for α≥γ, u_n(2^−n ξ)→d_a (no layer).
- BH.5: θ_k=Θ(2^k e_b) strictly decreasing to 0, θ_0=1−J_w/(2J_r)=1−3𝓛/√21; certified at 0.45: θ_0∈[0.4624385835869,0.462438583587], Θ(2,0)∈[0.340381375,0.340407195], Θ(4,0)∈[0.241594653,0.241622693], Θ(1,1)∈[0.382431398,0.382456436].
- BH.6: ρ^−k θ_k→θ_∞∈(0,∞) (derived from AT's small-y lemma and BD.4).

## Why It Matters

Resolves the non-uniformity of DISC-0147 (Kept Failure BG.1): the corner layer converges pointwise in blown-up coordinates to a universal profile, gives the gap x_a θ_0 at each neighbour separately (BG.1 used only the mean), and decays into the bulk at BG's outer rate ρ per doubling. It is a two-scale (inner/outer) description of the refinement limit below γ.

## Derivation

Repository's own (GASKET.md, proofs of BH.1–BH.6). Summary: interior cell vertices have degree 4 and zero source, so the resolvent is s-harmonic on the cell; the BG.1 restriction identity supplies cell-corner values; applying BH.1 with k=1 gives a 2×2 nonnegative recursion with row sums β≤3/5 whose fixed point is (x_a η, x_a η) and whose antisymmetric factor is 1/(z+5); the corner equation (2+s)w_a−w_{ν_b}−w_{ν_c}=x_a passes to the limit.

## Assumptions

AQ (1)–(3), AS (1), AY/AZ (1), BG.1 as stated in the repository; BH.6 additionally AT's small-y lemma, Θ bracket, BD.4. Stage 1 not edited. No W, 0.08, 0.23 or 30 µN/kW enters.

## New Results

Series form of r_∞ via the α-free function η (the repository calls it new; it reproduces AQ's fixed point with c=β). Certified layer constants above.

## Prior Art

Spectral decimation on the Sierpinski gasket (Fukushima–Shima, Strichartz, Teplyaev) and resolvent renormalisation p(s)=s(s+5) are KNOWN. Boundary layers at points of zero capacity / polarity (α below d_s/2) are KNOWN qualitatively. Specific η series and constants not searched.

## Novelty Analysis

Method KNOWN. The explicit η-series for r_∞ and the certified Θ values are internal to the corpus; novelty UNRESOLVED.

## Falsification Attempts

- Archive /workspace/scratch-ifi/indep_theorem_BH.py (own gasket graph builder, own η recursion, own mpmath quadrature in u=log s over ln5-period panels on [−170,80]): 43/43 PASS, EXIT 0, log indep_theorem_BH.log.
  - sympy: antisymmetric factor 1/(z+5), row sum β, β(0)=3/5, β' formula, α₁+β=2/(2+z).
  - Dense graph solves N=4,6,7, s∈{0.01,0.3,2}: |h_N−η|≤2(3/5)^N, corner equation, exact asymmetry product all PASS; r_7 matches 1/(2+s−2η) to 6 digits at s=0.05, 1.
  - J_r(0.45)=4.00130177348199559… (matches repo test 4.0013017734819).
  - θ_0=0.4624385835869492, θ_1=0.3403942883305888, θ_2=0.241608676407193, θ_Y=0.3824439208872447: all inside the certified brackets; (5/6)θ_0=0.3853654863 equals BG.1's gap; ordering θ_0>θ_Y>θ_1>θ_2>0.24 holds.
  - ρ^−k θ_k for k=3..8: 0.5172074, 0.5194682, 0.5202295, 0.5204820, 0.5205656, 0.5205934 (increments shrinking ~3× per level; extrapolates near 0.52061), consistent with BH.6/BH.7.
- Repo witness python3 scripts/gasket_fractional_corner_layer.py: EXIT 0, 25 ok, 0 FAIL, 309 s (log /workspace/scratch-ifi/repo_theorem_BH.log).
- Not independently re-certified: the arb interval enclosures themselves (archive uses floating quadrature only), and BH.6's existence proof beyond the float trend.

## Experimental Validation

Computational only.

## Mathematical Status

Theorem (BH.1–BH.5; BH.5 computer-assisted). BH.6 derived conditional on AT/BD.4 as stated.

## Patent Relevance

None.

## Related Discoveries

DISC-0146 → DISC-0149 (mathematical); DISC-0149 → DISC-0147 (explains the failure; DISC-0147 stays REJECTED); DISC-0106 → DISC-0149 (AQ corner resolvent); DISC-0111 → DISC-0149 (AS J_r, J_w re-run); DISC-0149 → DISC-0150 (Conjecture BH.7). DISC-0148 (BG.2) not decided.

## Open Questions

Closed forms for η, Θ, θ_∞; matching the inner layer Θ with BG.3's outer profile; Conjecture BG.2.

## Next Experiments

Certify θ_∞(0.45) with an interval enclosure of AT's log-periodic Θ_AT; test the inner/outer matching numerically.

## Reproduction Instructions

git -C informational-flux-identity checkout 156d8ce80c73147e3dc8aa34cbcea2ce6e42d989; python3 scripts/gasket_fractional_corner_layer.py (needs sympy, mpmath, python-flint; ~5 min). Archive: python3 indep_theorem_BH.py (~8 min).

## Evidence Log

- 2026-10-22 ~10:00pm EDT. Repo witness EXIT 0 (25 ok). Archive 43/43 PASS.

## Change History

- 2026-10-22. Initial archive entry.
