# Discovery: Theorem BG, pointwise refinement limit of the fractional Dirichlet extension on the combinatorial gasket

## Discovery ID

DISC-0146

## Status

THEOREM in the mathematical sense only (BG.1–BG.2 complete proofs in the repository; BG.3 constants by mpmath.iv certificate; BG.4–BG.5 derived). Method KNOWN (spectral decimation / Schur complement of the gasket resolvent, Woodbury rank-one step, maximum principle, dominated convergence). The qualitative phenomenon (data survive only on the corners when α ≤ log3/log5 = d_s/2) matches the KNOWN continuum fact that points are polar for a fractional operator of order below half the spectral dimension; the repository labels this an interpretation, not proved. Constants U(0.45), W(0.45), W(0.8), κ_0.8: novelty UNRESOLVED (not searched; internal to this construction). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~8:55pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 073ace5091ac17b2adcd2eb956ef8f0bf0a14bce (committed 2026-10-22 20:20:10 −0400). Files: GASKET.md "Theorem BG" (new section, Kept Failure BG.1, Conjecture BG.2, OPEN item extended), README.md (OPEN item "Distributional flux on the infinite gasket"), CLAIM_STATUS.md (new VERIFIED row), scripts/gasket_fractional_extension_limit.py (new, 379 lines), scripts/cli.py, tests/test_cli.py.

## Original Evidence

GASKET.md Theorem BG at 073ace5091ac17b2adcd2eb956ef8f0bf0a14bce: BG.1 u_n(x) = d̄ + ∫ s^−α r_n(s) h_m(p^(n−m)(s); x) ds / ∫ s^−α r_n(s) ds for x ∈ V_m, h_m(z;x) = [(L_m+z)^−1 x_C]_x / r_m(z), h_1(z; m_ab) = −x_c/(5+z); BG.2 |u_n(x) − d̄| ≤ (8/3) 4^−α 5^(m(1−α)) ‖x‖_∞ ρ^n / R_α(n), ρ = 5^α/3; BG.3 renormalised profile P_m, W(0.45) ∈ [0.5754299822, 0.5757467849], U(0.45) ∈ [0.143810693, 0.143889868], W(0.8) ∈ [0.5512217593, 0.5513327730], κ_0.8 ∈ [0.086072435, 0.086089770]; BG.4 Q_α(u_n) = 2‖x‖_2² / R_α(n); BG.5 corner-neighbour mean 1 − 5‖F‖/(2√21).

## Discovery

The first non-scalar refinement limit in the IFI gasket programme: the L_n^α-Dirichlet extension u_n itself converges pointwise on V_* \ V_0. For α ≤ γ = log3/log5 the limit is the constant d̄ (rate ρ^n below γ, 1/n at γ); for α > γ the limit is not flat, e.g. lim u_n(m_ab) = d̄ − κ_α x_c with κ_0.8 ≈ 0.08608 against the harmonic κ = 1/5. The flat / non-flat split coincides exactly with zero / nonzero renormalised energy ρ^n Q_α(u_n).

## Why It Matters

Earlier corpus limits (DISC-0106..0145) concern scalar audit norms. This is a function-level limit and it shows that below γ the discrete fractional Dirichlet problem forgets its corner data everywhere except on the corners, which bounds what any infinite-gasket flux functional built from u_n could carry.

## Derivation

Repository's (verified here): charge form u_n = Gq + d̄1 (README BB.1), Stieltjes integral for G = (L_n^α)^+, one decimation step via AQ's Schur complement c(L_k + p(s)) − eP_C with c p = 2e + s, S3 symmetry makes the corner block of (L_k + p)^−1 act as r_k(p) on the zero-sum plane, Woodbury gives restriction factor r_{k+1}(s)/r_k(ps), telescoping over k = m..n−1. BG.2 from p^k(s) ≥ 5^k s, r_n ≤ r_n(0) = (1/3)(5/3)^n and the maximum-principle bound |h_m| ≤ 4‖x‖/(4+z). BG.3 by s = 5^−n τ and dominated convergence with BD.4's scaling limits.

## Assumptions

IFI Assumption 4 (combinatorial gasket, corner data), AQ (1)–(3), AR (3)–(4), AS (1), AY, AZ (1),(3), BD.4 as stated in the repository; Assumption BG (renormalisation 3^−n 5^(nα)) for BG.4 only; correctness of mpmath.iv outward rounding for BG.3's intervals.

## New Results

Exact profile representation (BG.1); explicit pointwise rate (BG.2); certified renormalised midpoint profile U(0.45) and non-flat limit constant κ_0.8 (BG.3); energy dichotomy (BG.4). Kept Failure BG.1 (non-uniformity) is DISC-0147; Conjecture BG.2 is DISC-0148.

## Prior Art

Spectral decimation of the Sierpinski-gasket Laplacian (Fukushima–Shima; Strichartz, *Differential Equations on Fractals*) and its resolvent form are classical. Polarity of points for stable-like / subordinated processes on the gasket when the order is below d_s/2 is known in the Dirichlet-form literature (e.g. subordinated Brownian motion on fractals). No search on the specific constants.

## Novelty Analysis

Method KNOWN; qualitative dichotomy expected from known continuum theory. The specific discrete statement with explicit rate constant and certified U, κ is internal to the corpus; external novelty UNRESOLVED.

## Falsification Attempts

- Archive /workspace/scratch-ifi/indep_theorem_BG.py (own gasket builder sg_indep_common.py, no IFI code imported): 92/92 PASS. h_1(z; m_ab) = −x_c/(5+z) at four z; corner block is scalar; r_n recursion vs dense solves n = 2..4; decimation identity [(L_n+s)^−1 x_C]|_{V_m} = r_n(s) h_m(p^(n−m)s) for every m < n ≤ 4 at three s (err ≤ 1e−11); BG.1 against the direct Dirichlet solve of L_n^α at α = 0.45, 0.8, n = 1..6 (closed form via ∫ s^−α (λ+s)^−1 ds = π λ^−α / sin πα); BG.4 energy identity at every such n; BG.2 bound at every non-corner vertex of V_1..V_3 for n ≤ 6; ρ^−6(u_6(m_ab) − 1/6) = 0.025637485 (repo 0.025637); recursion quadrature ρ^−n W_n = 0.575588239694 and U_30 = 0.1438514532 at n = 30 (repo 0.57558823969, 0.143851453), inside the certified U window.
- Wording point found: the repository's "dense values at levels 1–6" (0.214634, …, 0.519861) are the corner-neighbour **means**, not the gap "neighbour mean − d̄" displayed in the formula just above them; the archive reproduces both (gap 0.047967 … 0.353195). Not an error in the theorem; recorded as a reading note.
- Repo witness rerun: see Evidence Log.
- Not independently re-certified: the 13485-cell interval enclosures of W(0.45), W(0.8) (archive floats only).

## Experimental Validation

Computational only. No physical claim; not thrust.

## Mathematical Status

Theorem (BG.1–BG.2 proof; BG.3 computer-assisted constants; BG.4–BG.5 derived).

## Patent Relevance

None.

## Related Discoveries

- DISC-0106 → DISC-0146 (mathematical): AQ's decimation of r_n drives the telescoping.
- DISC-0132 → DISC-0146 (mathematical): BB.1 charge form u_n = Gq + d̄1.
- DISC-0138 → DISC-0146 (mathematical): BD.4 scaling limits ψ, 𝒴 give the renormalised profile.
- DISC-0127 → DISC-0146 (mathematical): AZ's A_α gives the non-flat limit above γ.
- DISC-0111 → DISC-0146 (computational): AS's certified 𝓛(0.45), D_∞(0.45) re-run.
- DISC-0146 → DISC-0147 (failed hypothesis), DISC-0146 → DISC-0148 (mathematical).

## Open Questions

Closed forms for W, U, κ_α, P_m; continuum characterisation of u_∞ and of P_m/D_∞.

## Next Experiments

Interval re-certification of W(0.45) with an independent tail bound; compute κ_α across α ∈ (γ, 1) and test κ_α → 1/5 as α → 1.

## Reproduction Instructions

`git clone https://github.com/beyond-repair/informational-flux-identity && git checkout 073ace5091ac17b2adcd2eb956ef8f0bf0a14bce && python3 scripts/gasket_fractional_extension_limit.py` (expects EXIT 0, about 3 min). Archive: `cd /workspace/scratch-ifi && python3 indep_theorem_BG.py` (needs sg_indep_common.py).

## Evidence Log

- 2026-10-22 ~9:00pm EDT. Archive 92/92 PASS (/workspace/scratch-ifi/indep_theorem_BG.log). Repo witness: EXIT 0 (24 ok, 0 FAIL, 262 s; log /workspace/scratch-ifi/repo_theorem_BG.log).

## Change History

- 2026-10-22. Initial archive entry.
