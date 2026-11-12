# Discovery: Theorem DN, the f₀ term on the small cone C₂ (0.14444 < Θ₂(f₀, L̃f₀) < 0.14473), so DK.4's level-sum bound carries to C₂ (per-level rate < 0.363657)

## Discovery ID
DISC-0226

## Status
THEOREM in the mathematical sense only (the repository contains `arb` cell tables for DN.1, DI.1's exact identity with outward float cell pairs plus an `arb` floor for DN.2, and DN.3 is CF.3's proof applied with stated constants). Method KNOWN (Hilbert-metric contraction / Birkhoff cone argument, DI's machinery from DISC-0221 re-run at a = 2). Constants UNRESOLVED as to novelty. DN.3 uses DL.5's and DM.5's θ values as stated; its asymptotic rate rests on DM's n = 9 cover (DISC-0225), which the repo author reports re-running cleanly but this archive has not reproduced.

## Date Discovered
2026-11-12 (indexed ~5:05 AM EST)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 928bc79323cc (2026-11-12 04:41:26 EST).

## Original Evidence
- GASKET.md §Theorem DN (line 5159 onward, +34 lines); CLAIM_STATUS.md new row (line 122); README.md (+2/−1).
- scripts/gasket_fractional_profile_level_f0_small_cone.py (new, 162 lines; imports DI's script `gasket_fractional_profile_level_f0_coupled`); scripts/cli.py registration; tests/test_cli.py (+29, local only, needs python-flint).

## Discovery
Answers DISC-0225's open question / DM's kept limit "DK.4's level-sum bound is not carried to C₂, because Θ₂(f₀, L̃f₀) is not computed".
- DN.1 (`arb`, 16384 cells): (log F0)′ ∈ [0.035291, 0.77334], (log L̃F0)′ ∈ [0.17682, 0.79038], so f₀, L̃f₀ ∈ C_b with b < 2 (CF.3's hypothesis).
- DN.2: 0.14444 < Θ₂(f₀, L̃f₀) < 0.14473 (65536 cells: < 0.14452). DI.3's factor lemma gives only 0.9448 at a = 2.
- DN.3: for k ≥ 4, |log(s_{k+1}/(r s_k))| ≤ 0.14473 · min(θ_L^⌊(k−4)/5⌋, θ₇^⌊(k−4)/7⌋, θ₉^⌊(k−4)/9⌋), with θ_L < 0.0108954, θ₇ < 0.0011028, θ₉ < 0.00011123; per-level rate θ₉^{1/9} < 0.363657 (DK.4: 0.53349). Taken as a minimum with DK.4, it divides DK.4's bound by 41.2, 14.1, 445, 1.38·10⁷, 1.34·10¹⁶ at k = 9, 13, 22, 49, 103.
- DN.4 (kept failure): the C₂ constant is > 0.14444 = 2.22 × DI.4's Θ_I′, so for k = 4..8 (before the first C₂ block step) DK.4/DI.5 stays the better bound.

## Why It Matters
It closes the last gap between the C₂ contraction results (DISC-0224, DISC-0225) and the level-sum convergence statement, so the certified per-level convergence rate of s_{k+1}/s_k → r drops from 0.53349 to 0.363657. The spectral value 0.1725 is still not reached.

## Derivation
Hand-checked this slice: at k = 9, DK.4's bound is 0.064982 (no block step yet on C₁₀₀ with n = 8, 9), DN.3's is 0.14473 × 0.0108954 = 0.0015769, ratio 41.21 (matches). 0.00011123^{1/9} = 0.3636565 (< 0.363657, matches). DN.4: 0.14444 / 0.064982 = 2.223 (matches).

## Assumptions
CF's Θ_a and CF.3's proof; DI.1's exact quotient identity and DI.4's cell-pair method (DISC-0221); DL.1's cone step L̃C₂ ⊂ C₂ (DISC-0224); DL.5, DM.5 θ values (DISC-0224, DISC-0225) used as stated; CE.4's r; CC's s_k; cell pairs are outward floats (repo's kept limit).

## New Results
0.14444 < Θ₂(f₀, L̃f₀) < 0.14473; combined level-sum bound min(DK.4, DN.3) with asymptotic per-level rate < 0.363657.

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995; Baladi 2000 (Hilbert-metric contraction and its use for convergence rates of positive operators). Specific constants for this operator: no prior computation found; not searched further, so UNRESOLVED.

## Novelty Analysis
Technique KNOWN; DN re-runs DI's machinery at a different cone parameter and combines published-in-repo constants. No first claimed.

## Falsification Attempts
Archive scripts `mathematics/scripts/indep_theorem_DN_grid.py` and `indep_theorem_DN.py` (my own pair sampling; they reuse only the repo's Taylor data for F0 via `gasket_fractional_profile_level_birkhoff`, not DN's or DI's cell code):
- Grid (1601 points, numerical gradient): slopes [0.035517, 0.772850] and [0.177238, 0.789863], inside DN.1's enclosures (PASS ×2). Grid pair sampling gave Θ₂ ≈ 0.144311, which is below the certified floor 0.14444; this is a sampling miss, not a contradiction (a sampled sup can only undershoot).
- v2 (endpoint pairs at 200 log-spaced offsets plus interior scan): β = 0.4373444, α = 0.3785210, Θ₂ = 0.1444494, inside (0.14444, 0.14473) and equal to the repo's `arb` floor 0.14444945 to 7 digits. PASS. The extremes sit at the endpoint cells (β near s = 5/2, α near s = √5/2), as the repo reports (cells 16383 and 0).
- DN.3 and DN.4 arithmetic rechecked by hand (above).
- Not independently recomputed: `arb` cell tables, the outward cell-pair upper bound, DL.5/DM.5's θ values.

## Experimental Validation
Repo witness `python3 scripts/gasket_fractional_profile_level_f0_small_cone.py` at 928bc79: EXIT 0 in 160.7 s, all checks ok (Θ_N′ = [0.14472564 ± 4.4·10⁻⁹], floor [0.14444945 ± 3.3·10⁻⁹], gap 0.0002762; DI.3 at a = 2 [0.944707 ± 3.7·10⁻⁷]; rate [0.3636565 ± 2.4·10⁻⁸]; CC s₄..s₁₃ max ratio 0.1991; CE.4 r re-certified). DN_CELLS=65536 and pytest not rerun.

## Mathematical Status
Theorem (proof in repository; cell-pair upper bound in outward-padded floats with `arb` tables). The rate part inherits DISC-0225's n = 9 status.

## Patent Relevance
None. A convergence-rate bound for a positive transfer operator. Not a flux, not thrust.

## Related Discoveries
DISC-0225 (kept limit answered; θ₇, θ₉ used), DISC-0224 (θ_L, cone step used), DISC-0223 (DK.4 bound improved for k ≥ 9), DISC-0221 (DI machinery re-run at a = 2), DISC-0205 (spectral 0.1725 still out of reach).

## Open Questions
A cone or block reaching 0.1725; whether an a between 1.69 and 2 lowers Θ_a(f₀, L̃f₀) enough to beat DK.4 for k = 4..8; full interval cell pairs.

## Next Experiments
Scan Θ_a(f₀, L̃f₀) over a ∈ [1.69, 3] with indep_theorem_DN.py; run DN_CELLS=65536 once; reproduce DM_N=9.

## Reproduction Instructions
In informational-flux-identity @ 928bc79: `pip install python-flint numpy`, `python3 scripts/gasket_fractional_profile_level_f0_small_cone.py` (~3 min). Archive checks: edit the `sys.path` line to point at that checkout's `scripts/`, then `python3 discoveries/mathematics/scripts/indep_theorem_DN.py` (~2 min) and `indep_theorem_DN_grid.py` (~2 min).

## Evidence Log
- 2026-11-12 ~5:00 AM EST: read commit 928bc79 message, file list, script docstring, GASKET.md section header and CLAIM_STATUS row; repo witness EXIT 0 (160.7 s); grid check 4/4 PASS (with a noted sampling undershoot); v2 endpoint check PASS (0.1444494).

## Change History
- 2026-11-12: created.
