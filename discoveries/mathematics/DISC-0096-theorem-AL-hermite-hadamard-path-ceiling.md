# Discovery: Hermite–Hadamard sharpens the path-resistance ceiling (Theorem AL)

## Discovery ID

DISC-0096

## Status

THEOREM

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0097.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 483de961575bca353a2cd3ff6719b8a357610a87 (main tip at archive time). Paths: GASKET.md "Theorem AL" (after Theorem AK: ASSUMPTION, THEOREM AL, Proof, Witness, Kept Failure AL.1, NOT THIS; Conjecture J.1 evidence paragraph, "What this does not say", and OPEN updated); CLAIM_STATUS.md (new row "Sharp path-resistance ceiling R_∞ via Hermite–Hadamard; improved fractional and audit floors" VERIFIED); scripts/gasket_fractional_path_ceiling.py (new); scripts/cli.py; README.md.

## Original Evidence

GASKET.md Theorem AL, for every α∈[α_*,1/2) with α_*=(14−8√2)/34≈0.079009 and every path length m≥1 (notation of Theorem AA; Theorems AA and AK used as stated):
1. Path integrand f(θ)=(2sinθ)^(−2α)cos²θ is convex on (0,π/2) (analytic second-derivative minimum 5b−2+2√(2b(b+1)) with b=2α, nonnegative precisely when α≥α_*).
2. AA's cosine sum is the midpoint Riemann sum of f; Hermite–Hadamard on each midpoint interval gives R_α(m) ≤ R_∞(α) = 4^(−α)(4/π)B(1/2−α,3/2) < C(α).
3. Löwner–Heinz and path duality of AA with C→R_∞: Q_α(u_n) ≥ (9/4)/R_∞(α) and ‖F_frac(n,α)‖ ≥ 9√21/(28 R_∞(α)).
4. At α=0.45: R_∞≈13.245199, Q≥0.169873, ‖F_frac‖≥0.111208 (~1.324× AA's 0.084015); with AK's σ_AK≈0.701556, ‖F(n,0.45)‖ ≥ 0.078019 (~1.324× AK's 0.058941).

## Discovery

Theorem AL refines DISC-0072 by replacing AA's crude path ceiling C(α) with the Hermite–Hadamard limit R_∞(α) for α≥α_*, and lifts the DISC-0094 audit floor from 0.058941 to 0.078019 at α=0.45. Incremental constant improvement. Convergence of ‖F(n,0.45)‖ and Conjecture J.1 (L≥0.70) stay OPEN.

## Why It Matters

Further sharpening of the proved positive floor for DISC-0034's sequence; still far below live ‖F(6)‖≈0.880 and below 0.70. Kept Failure AL.1 (DISC-0097) closes the sharp-path-ceiling route to 0.70 (different from the one-step neighbor-Harnack family closed in DISC-0095). Not thrust.

## Derivation

Repository proof, checked step by step in this archive (no gap found):
1. Write Δ=π/(m+1) and f(θ)=(2sinθ)^(−2α)cos²θ. AA's cosine sum is the midpoint Riemann sum of f on intervals in (0,π/2] (exact cover when m odd).
2. Set b=2α, g=sin^(−b)cos². Direct differentiation: g''/g = b(b+1)/sin²θ + 2/cos²θ + 4b−4−b². In x=sin²θ this is h(x)=b(b+1)/x+2/(1−x)+4b−4−b², minimized at x_*=√(b(b+1))/(√(b(b+1))+√2) with value 5b−2+2√(2b(b+1)).
3. That minimum is ≥0 iff b≥(14−8√2)/17, i.e. α≥α_* (rearrangement 17b²−28b+4≤0 for the relevant root).
4. Hermite–Hadamard on each midpoint interval: f(mid)≤average ⇒ R_α(m)≤(8/π)∫_0^{π/2}f = R_∞(α). R_∞ < C because C−R_∞=4^(−α)·8.
5. AA Löwner–Heinz / duality with C→R_∞; AK (4)–(5) with AA's 0.084015 → 0.111208.

## Assumptions

Spectral calculus as GASKET item 4; corner data (1,−1/2,0); Theorems AA (DISC-0072) and AK (DISC-0094) as stated. Convexity / R_∞ bound for α∈[α_*,1/2); AA's C still applies below α_*.

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_AL.log` (repository witness `python3 scripts/gasket_fractional_path_ceiling.py` at 483de961575bca353a2cd3ff6719b8a357610a87, EXIT 0, 376 PASS, 0 FAIL, "All checks passed. Theorem AL / Kept Failure AL.1. Not thrust.") and `/workspace/scratch-ifi/indep_theorem_AL.py` / `indep_theorem_AL.log` (own builder `/workspace/scratch-ifi/sg_indep_common.py`, no repo import, numpy only; EXIT 0, 442 PASS, 0 FAIL, ALL PASS):
- α_*≈0.079008573559; min(f''/pos) vanishes at b_*; positive at b=0.9 (~6.198648); analytic critical formula matches brute force; convexity fails below α_* (attack);
- R_∞(0.45)≈13.245199 < C≈17.532293 (factor ≈1.323672); Q floor ≈0.169873; ‖F_frac‖ floor ≈0.111208 (~1.324× AA); σ_AK recomputed ≈0.701556; ‖F‖ floor ≈0.078019 (~1.324× AK);
- R(m)≤R_∞ through m≤64 and m=2^k up to 2^11 at α∈{0.10,0.25,0.45,0.49}; 40 random (α,m) attack samples; closed form matches dense pseudo-inverse; odd-m exact midpoint cover; Hermite–Hadamard midpoint≤avg on intervals;
- live levels 1–6 at α=0.45: Q, ‖F_frac‖, ‖F‖ dominate new floors; Q ≥ path energy (9/4)/R(2^n) ≥ Q floor; live ‖F‖ table and level-2 lock 1.165909 reproduced; level 4 clears floors at α∈{0.10,0.25,0.49}.

## Prior Art

Elementary: Hermite–Hadamard inequality for convex integrands, Beta-function path resistance of AA, midpoint Riemann sums. Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only (complete elementary proof in the repository, verified here). Incremental sharpening of DISC-0072 / DISC-0094; not a novelty claim and not a Stage-1 / claim-level raise.

## Falsification Attempts

Recomputed α_*, convexity threshold, R_∞, C, floors, and σ_AK independently; checked R(m)≤R_∞ on dense m-grids and random attacks; verified Hermite–Hadamard numerically on midpoint intervals; rebuilt live gasket through level 6 with own builder. Attack: to reach 0.70 via σ_AK would need R_∞≤≈1.48, below live gasket resistance ~2.35 and far below R_∞≈13.25. No break found.

## Experimental Validation

None (pure mathematics / finite numerical witness).

## Mathematical Status

Proved in-repo; proof and witness verified. Supersedes DISC-0094's numerical floor (DISC-0094 row not edited). DISC-0034 remains CONJECTURE for existence of lim ‖F(n,0.45)‖ and L≥0.70.

## Patent Relevance

None.

## Related Discoveries

- DISC-0072. Mathematical. Theorem AA; AL replaces C(α) by R_∞(α) for α≥α_*.
- DISC-0094. Mathematical. Theorem AK; AL uses σ_AK with the new ‖F_frac‖ floor.
- DISC-0092, DISC-0090, DISC-0088. Mathematical. Earlier Harnack floors.
- DISC-0097. Failed hypothesis. Kept Failure AL.1.
- DISC-0034. Conjecture. Convergence and L≥0.70 stay OPEN (row not edited).

## Open Questions

Whether ‖F(n,0.45)‖ converges and whether L≥0.70. DISC-0097 shows the sharp path ceiling cannot reach 0.70; a different comparison is needed.

## Next Experiments

None required.

## Reproduction Instructions

`git checkout 483de961575bca353a2cd3ff6719b8a357610a87 && python3 scripts/gasket_fractional_path_ceiling.py`. Archive: `python3 /workspace/scratch-ifi/indep_theorem_AL.py`. Logs: `/workspace/scratch-ifi/repo_theorem_AL.log`, `/workspace/scratch-ifi/indep_theorem_AL.log`.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Theorem AL at 483de961575bca353a2cd3ff6719b8a357610a87; repo witness EXIT 0 (376 PASS); independent check ALL PASS (442 PASS). Repository description still matches its claim fence (closed-surface identity / not a net force).

## Change History

- 2026-10-15. Initial archive entry.
