# Discovery: Theorem BI, above log3/log5 the L^α Dirichlet extension converges uniformly to a continuous limit

## Discovery ID

DISC-0151

## Status

THEOREM in the mathematical sense only (repository's own proof in GASKET.md; the constant G=0.6031 and the K_α, ε_N values are computer-assisted via python-flint arb). Method KNOWN (decimation, maximum principle, Dirichlet principle, cell-oscillation chaining). Constants novelty UNRESOLVED. Proves Conjecture BG.2 (DISC-0148). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~11:56pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 2e4d0d4ffe30a99ea0154e1aaa8b95069927b162 (2026-10-22 23:18:25 −04:00). Files: GASKET.md "Theorem BI" (new section), CLAIM_STATUS.md (new row "Uniform limit of the L^α Dirichlet extension above log3/log5"), README.md (OPEN item updated), scripts/gasket_fractional_uniform_limit.py (new, 401 lines), scripts/cli.py, tests/test_cli.py (test_theorem_bi_uniform_limit).

## Original Evidence

GASKET.md Theorem BI.1–BI.6 with proofs; certificate in scripts/gasket_fractional_uniform_limit.py (arb on 5763 cells of [1e−5,1] for sup s^(1−γ) r_∞ ≤ 0.601271031, bootstrap along the p-orbit below 1e−5 giving ≤ 0.6016995, analytic bound ≤ 3/5 on [1,∞)).

## Discovery

With w_s=(L_n+s)^−1 x_C, ω_i(s) the largest corner difference of w_s on a level-i cell, z_i=p^(n−i−1)(s), p(s)=s(s+5), ρ=5^α/3, γ=log3/log5:
- BI.1: ω_0 ≤ 2r_n‖x‖ and ω_(i+1) ≤ (3/5)ω_i + κ(z_i) r_n‖x‖, κ(z)=z/(z+2), because a level-i cell's midpoints are the level-1 z_i-harmonic extension of its corners; |w_s| ≤ r_n‖x‖.
- BI.2: orbit lemma p^k(s) ≤ e^(1/2) 5^k s when 5^k s ≤ 1.
- BI.3: osc_Δ u_n ≤ ‖x‖(ρ^n/D_n)∫τ^−α R_n F_N dτ on every level-N cell.
- BI.4: R_n(τ) ≥ 1/(3+τ) and R_n ≤ min(1/3, G τ^(γ−1)), G=0.6031 certified.
- BI.5: for α>γ, osc of u_n on every level-N cell ≤ ‖x‖ε_N(α) ≤ ‖x‖K_α ρ^−N uniformly in n; certified K_0.75≤70.6512, K_0.8≤47.109, K_0.9≤39.005; ε_N(0.8)≤5.90016, 4.78623, 2.19931, 0.347709, 0.0526623, 0.00796134, 1.81925e−4 at N=0,5,10,20,30,40,60.
- BI.6: with BG.3's pointwise limit, u_n → ū uniformly, ū continuous on the gasket, ū=d on the corners (Conjecture BG.2).
- Derived: Hölder exponent (α−γ)/(1−γ) at the resistance scale (3/5)^N.

## Why It Matters

First continuous limit function of the corpus's fractional Dirichlet problem; together with DISC-0146 (flat pointwise limit below γ) and DISC-0149 (corner layer below γ) it completes the qualitative phase picture: below γ flat limit plus a universal corner layer, above γ a genuine continuous extension with an explicit modulus.

## Derivation

Repository's own (GASKET.md, proofs of BI.1–BI.6). Interior decimation inside each cell gives the one-step contraction 3/5 plus a source term from the shifted spectral parameter; chaining through nested cells bounds the oscillation by a sum of ω_i; integrating against the charge form s^−α and rescaling with R_n converts it to an integral that is finite exactly when τ^(γ−1−α) is integrable at infinity, i.e. α>γ.

## Assumptions

AQ, AS, BD.4, BG.3, BH (η enclosure for the G certificate) as stated in the repository. ‖x‖ is the sup norm of the zero-mean corner data. Stage 1 not edited. No W, 0.08, 0.23 or 30 µN/kW enters.

## New Results

Explicit uniform cell modulus K_α ρ^−N and the Hölder exponent (α−γ)/(1−γ); the certified constant sup s^(1−γ) r_∞(s) ≤ 0.6031.

## Prior Art

Spectral decimation and resolvent renormalisation on the Sierpinski gasket (Fukushima–Shima, Strichartz, Teplyaev) KNOWN. Continuity of Green/Dirichlet extensions for subordinated (fractional) Dirichlet forms above the critical order where points have positive capacity is KNOWN in general (d_s/2 threshold; here γ=log3/log5 is half the spectral dimension 2log3/log5). Hölder continuity of functions in the domain of a fractional form at exponent tied to (α−d_s/2) is the standard Sobolev-embedding analogue on p.c.f. fractals. Specific constants not searched.

## Novelty Analysis

Method and qualitative result KNOWN-type (continuity above the capacity threshold). The explicit combinatorial cell recursion, the certified G, K_α and ε_N values are internal to the corpus; novelty UNRESOLVED.

## Falsification Attempts

- Archive /workspace/scratch-ifi/indep_theorem_BI.py (own gasket graph and cell list, own η series, no IFI code): 24/24 PASS, EXIT 0, log indep_theorem_BI.log.
  - sympy: solving the level-1 (L_1+z) problem gives m_ab=α₁(f_a+f_b)+δf_c, m_ab−m_ac=(f_b−f_c)/(z+5), total weight 2/(z+2), β≤3/5 on z≥0.
  - Dense graph solves N=4,6, s∈{1e−4,0.03,0.7,5}, random zero-sum x: max|w_s| ≤ r_n‖x‖ and the full ω-recursion (all levels) hold.
  - R_n(τ) ≥ 1/(3+τ) for n=1..6 on τ∈[1e−4,1e4].
  - Orbit lemma checked for k<12 on dense grids.
  - Float sup over s∈[1e−9,1e3] of s^(1−γ)/(2+s−2η(s)) ≈ 0.6009613, below the repo's certified 0.601271031 and G=0.6031; g ≤ s^−γ(2+s)/(4+s) on [1,1e3].
  - Hölder exponent identity log ρ/log(5/3)=(α−γ)/(1−γ) at α=0.75, 0.8, 0.9.
- Repo witness python3 scripts/gasket_fractional_uniform_limit.py: EXIT 0, 25 ok, 0 FAIL, 382 s (log /workspace/scratch-ifi/repo_theorem_BI.log).
- Not independently re-certified: the arb enclosures for G, K_α, ε_N (archive uses floats only).
- Consistency: the bound is vacuous for α≤γ, matching DISC-0147 (BG.1) and DISC-0149 (BH).

## Experimental Validation

Computational only.

## Mathematical Status

Theorem (BI.1–BI.6; BI.4–BI.5 constants computer-assisted). Sharpness of ρ^−N is Conjecture BI.7 (DISC-0152).

## Patent Relevance

None.

## Related Discoveries

DISC-0146 → DISC-0151 (BG.3 pointwise limit); DISC-0149 → DISC-0151 (η enclosure used for G); DISC-0106 → DISC-0151 (AQ fixed point in the bootstrap); DISC-0151 → DISC-0148 (proves BG.2: CONJECTURE → THEOREM); DISC-0151 → DISC-0152 (Conjecture BI.7).

## Open Questions

Rate of uniform convergence in n; continuum equation for ū; closed forms for W, U, κ; Conjecture BH.7 (DISC-0150).

## Next Experiments

Interval-certify the corner deficit ρ^N(d_a−u(ν_N))/x_a at α=0.8 to decide BI.7; compare ū at α=0.8 with a direct continuum fractional Dirichlet solve.

## Reproduction Instructions

git -C informational-flux-identity checkout 2e4d0d4ffe30a99ea0154e1aaa8b95069927b162; python3 scripts/gasket_fractional_uniform_limit.py (needs sympy, mpmath, python-flint; ~6.5 min). Archive: python3 indep_theorem_BI.py (~3.5 min).

## Evidence Log

- 2026-10-22 ~11:56pm EDT. Repo witness EXIT 0 (25 ok). Archive 24/24 PASS.

## Change History

- 2026-10-22. Initial archive entry.
