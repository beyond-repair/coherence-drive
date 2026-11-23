# Discovery: Theorem BK, u_n→ū uniformly on V_n at rate ρ^−n (exact one-level transfer with weight ω_n≥1)

## Discovery ID

DISC-0155

## Status

THEOREM in the mathematical sense only (repository proof; constants J_α, C_α computer-assisted with python-flint arb, not re-certified here). Method KNOWN; constants novelty UNRESOLVED. Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~2:54am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 00d0d28b71db264b070be23c73f8e3f67de704db (committed 2026-10-23 02:33:31 EDT). Files: GASKET.md (Theorem BK, BK.1–BK.6), CLAIM_STATUS.md (new row), README.md, scripts/gasket_fractional_uniform_rate.py (new, 318 lines), scripts/cli.py, tests/test_cli.py.

## Original Evidence

Commit 00d0d28b71db264b070be23c73f8e3f67de704db message and GASKET.md Theorem BK. Repository witness `python3 scripts/gasket_fractional_uniform_rate.py` at that commit: EXIT 0, all checks ok, 313 s (log archived on the box at /workspace/scratch-ifi/repo_theorem_BK.log).

## Discovery

For the fractional (L^α) Dirichlet extension u_n of corner data on the level-n Sierpinski gasket graph, with γ=log3/log5, ρ=5^α/3, D_n=∫s^−α r_n(s)ds and D'_n=ρ^−n D_n:

1. BK.1 (exact transfer). Substituting τ=5^(n+1)y at level n+1 and τ'=5^n p(y), p(y)=y(y+5), gives u_(n+1)(x)−d̄=⟨ω_n F_n⟩/⟨ω_n⟩ under the level-n probability measure μ_n=τ^−α R_n dτ/D'_n, with F_n the BG.3 profile and ω_n=(1+y/5)^α/((1+2y/5)(5/3)(β(y)−e(y)r_n(p(y)))), ⟨ω_n⟩=D'_(n+1)/D'_n.
2. BK.2. (1+2y/5)(5/3)β(y)=1−y(y+4)/(3(y+2)(y+5))≤1, so ω_n≥1 for every α, D'_n strictly increases, and |u_(n+1)(x)−u_n(x)|≤2 sup|F_n−c| log(D'_(n+1)/D'_n).
3. BK.3. For α>γ the logs telescope: sup_(V_n)|u_n−ū|≤2‖x‖log(D'_∞/D'_n); data-free corner-deficit error |δ_N^(n)−δ_N|≤(3/2)log(D'_∞/D'_n).
4. BK.4 (certified). D'_(k+1)−D'_k≤J_α ρ^−k with J_0.75≤1.256914, J_0.8≤1.188154, J_0.9≤1.101281, hence sup_(V_n)|u_n−ū|≤C_α‖x‖ρ^−n for every n with C_0.75≤12.5476, C_0.8≤6.2192, C_0.9≤1.9725.
5. BK.5 (derived from Theorem AZ's C_0.8 as stated). ρ^n(D'_∞−D'_n)→4.658677573, so limsup ρ^n sup|u_n−ū|≤1.454890769‖x‖.

This proves Conjecture BJ.7 (DISC-0154) as an upper bound of order ρ^−n, uniformly on V_n, not only at the corner neighbours.

## Why It Matters

Gives a quantitative rate for the convergence proved in Theorem BI (DISC-0151), and the matching order to BJ's ρ^−N lower bound on cell oscillation (DISC-0153). The mechanism (a one-level transfer whose weight is ≥1, so a covariance bound telescopes) is short and closed-form apart from the J_α constant.

## Derivation

Repository's. Independently re-derived here: the covariance step. With ω≥1 and any constant c, Cov(ω,F)=⟨(ω−1)(F−c)⟩−(⟨ω⟩−1)⟨F−c⟩, so |Cov|≤2(⟨ω⟩−1)sup|F−c|, and u_(n+1)−u_n=Cov/⟨ω⟩, with (t−1)/t≤log t for t≥1. This step is correct.

## Assumptions

AQ's Schur-complement step 1/r_(k+1)(s)=β(s)/r_k(p(s))−e(s) (DISC-0106, DISC-0153); BG.3's exact profile formula (DISC-0146); BI.4's G=0.6031 (re-run in the witness); AZ's A_0.8 and C_0.8 for BK.5 only; correctness of the arb enclosures.

## New Results

- Uniform rate ρ^−n with explicit certified constants at α=0.75, 0.8, 0.9.
- D'_n is strictly increasing for every α≥0 (derived).
- Below γ the same transfer holds but log(D'_(n+1)/D'_n)→−log ρ>0 is not summable, consistent with Kept Failure BG.1 (DISC-0147).

## Prior Art

Not searched for the specific gasket constants. The ingredients (renormalisation/decimation on p.c.f. fractals, resolvent integral representation of fractional powers, covariance bounds under a change of measure) are standard. Treat method as KNOWN.

## Novelty Analysis

The specific transfer identity and the constants J_α, C_α are not found elsewhere in this corpus. Whether they appear in the analysis-on-fractals literature is UNRESOLVED.

## Falsification Attempts

Independent script /workspace/scratch-ifi/indep_theorem_BK.py (own gasket graph builder, own spectral L^−α extension, no repository imports): 17/17 PASS. Checked the sympy identity behind ω≥1; the change of variables; AQ's step and the agreement of both ω forms on the graph at levels 0–4 for six y values; ω_n≥1 at α∈{0.3,0.75,0.8,0.9} (min 1.000075); D'_0=3^−απ/sin(πα); D'_n strictly increasing for n=0..7 at α=0.75, 0.8, 0.9; the BK.2 per-step bound on V_n for n=0..6 (observed/bound ratios ≤0.336); sup_(V_n)|u_7−u_n|≤C_α‖x‖ρ^−n for n=0..6; and at 0.8, 0<D'_∞−D'_n≤6.901366ρ^−n for n=0..7 with ρ^n gap rising 4.1848→4.6574, toward the repository's 4.6587. A first run of the independent script reported 4 FAIL. Those came from a bug in the check itself: it compared level-n and level-(n+1) vertices by unscaled integer lattice coordinates. After the vertices were rescaled to the unit triangle, every check passed. No defect in the repository claim was found. arb enclosures not re-certified.

## Experimental Validation

Numerical only (graph levels ≤7). Repository's own floats: dense L^0.8 one-level differences 0.0137–0.0337 under per-step bounds 0.297–0.109.

## Mathematical Status

Theorem (computer-assisted constants).

## Patent Relevance

None.

## Related Discoveries

DISC-0151 → DISC-0155 (mathematical); DISC-0153 → DISC-0155 (mathematical, lower-bound counterpart); DISC-0146 → DISC-0155 (mathematical, BG.3 profile); DISC-0106 → DISC-0155 (mathematical, AQ's step); DISC-0155 → DISC-0154 (proves BJ.7, CONJECTURE → THEOREM); DISC-0155 → DISC-0156 (Conjecture BK.6); DISC-0147 (consistency below γ).

## Open Questions

Sharpness (DISC-0156); closed forms for c_corner, W, U, κ; a continuum equation for ū; Conjectures BH.7 and BF.2; the Stage 2 question.

## Next Experiments

Re-certify J_0.8 with an independent interval library; test monotonicity of ω_k in y (would give BK.6).

## Reproduction Instructions

git -C informational-flux-identity checkout 00d0d28b71db264b070be23c73f8e3f67de704db; python3 scripts/gasket_fractional_uniform_rate.py (about 5 min). Independent: python3 /workspace/scratch-ifi/indep_theorem_BK.py (about 3 min).

## Evidence Log

- 2026-10-23 ~2:54am EDT. Repository witness EXIT 0 (313 s). Independent check 17/17 PASS after the lattice-scaling bug in the check was fixed.

## Change History

- 2026-10-23. Initial archive entry.
