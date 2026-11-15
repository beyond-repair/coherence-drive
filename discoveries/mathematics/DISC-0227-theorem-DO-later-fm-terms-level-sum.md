# Discovery: Theorem DO, the later f_m terms Θ_a(L̃^m f₀, L̃^{m+1} f₀), m = 0..5, a = 2, 100, so the level-sum bound restarts from them; kept failure DO.4 (no cone beats DI.4 at k = 4 by more than 1.0252)

## Discovery ID
DISC-0227

## Status
THEOREM in the mathematical sense only (the repository contains `arb` jets for DO.1, DI.1's exact identity with `arb` cell tables, outward float cell pairs and `arb` floors for DO.2, and DO.3 is CF.1/CF.3 with mixed blocks and stated constants). Method KNOWN (Hilbert-metric contraction; DO.4's inequality Θ_C ≥ osc log(g/f) is the standard fact that point evaluations lie in the dual cone). Constants UNRESOLVED as to novelty. Per-level rate unchanged (< 0.363657, DISC-0226); DO improves constants only.

## Date Discovered
2026-11-12 (indexed ~7:15 AM EST)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit c7264aec2f70 (2026-11-12 06:09:27 EST).

## Original Evidence
- GASKET.md §Theorem DO (line 5193 onward, +45 lines); CLAIM_STATUS.md new row (line 123); README.md (+2/−1).
- scripts/gasket_fractional_profile_level_f0_shift.py (new, 453 lines); scripts/cli.py registration; tests/test_cli.py (+35, local only, needs python-flint).

## Discovery
Answers DISC-0226's kept failure DN.4 ("for k = 4..8 DK.4/DI.5 stay the bound").
- DO.1 (`arb` jets, 4096 cells): (log F_m)′ ∈ [0.035297, 0.790318] for m = 0..6, so every F_m = L̃^m f₀ lies in C₂ and C₁₀₀.
- DO.2: Θ₂(F_m, F_{m+1}) for m = 0..5 in (0.144449, 0.144458), (0.069688, 0.069733), (0.0069152, 0.0069175), (0.0010008, 0.0010024), (0.00016484, 0.00016633), (2.8125, 2.9590)·10⁻⁵; Θ₁₀₀ in (0.0649755, 0.0649756), (0.0375166, 0.0375169), (0.0042202, 0.0042203), (0.00061741, 0.00061746), (0.00010197, 0.00010201), (1.7410, 1.7446)·10⁻⁵.
- DO.3: |log(s_{k+1}/(r s_k))| ≤ B(k) = min over m ≤ min(5, k−4), a ∈ {2, 100} of Θ_a(F_m, F_{m+1}) G_a(k−4−m); min(DN.3, DK.4)/B(k) > 1.731 for every k ≥ 5, > 636.9 at k = 8, > 8.883 for every k ≥ 14 (checked to k = 1995, periodic beyond K₀ = 214). Rate unchanged.
- DO.4 (kept failure): any cone of positive functions has Θ ≥ osc log R_m with R_m = F_{m+1}/F_m; osc log R₀ > 0.0633864, so DI.4's 0.064982 is within a factor 1.0252 of the best any cone can do at k = 4. Θ₂/Θ₁₀₀ ≥ 1.612, so C₂ is never the better cone for the direct terms.

## Why It Matters
Tightens the certified level-sum error bound at every finite k ≥ 5 and shows the k = 4 constant is essentially optimal over all cones. It does not move the asymptotic rate toward the spectral 0.1725.

## Derivation
Hand-checked this slice: B(5) = Θ₁₀₀(F₁, F₂) · G(0) < 0.0375169, and min(DN.3, DK.4) at k = 5 is DK.4's 0.064982, ratio 1.7321 (> 1.731, matches). 0.064982 / 0.0633864 = 1.02517 (matches 1.0252).

## Assumptions
CF.1, CF.3's proof, DL.1, DL.5, DM.5 (θ values as stated), DG.3, DK.4, DI.1, CO.1/CO.2 (Taylor data), as listed in the repo row.

## New Results
None beyond the repository's. The independent float check reproduces every DO.2 and DO.4 number.

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995; Baladi 2000. The oscillation lower bound for Hilbert's projective metric is textbook (Bushell 1973). Specific constants for this operator: no prior computation found; not searched further, so UNRESOLVED.

## Novelty Analysis
Technique KNOWN. Contribution is sharper certified constants at finite k and an optimality certificate at k = 4. No first claimed.

## Falsification Attempts
Independent script `mathematics/scripts/indep_theorem_DO.py` (numpy, imports only CO's Taylor data from the repo, none of DO's code): iterates L̃ on a degree-60 Chebyshev table (relative error 9.3·10⁻¹⁵ at m = 1), samples slopes and Θ_a by endpoint and interior pairs, computes osc log R_m on 2001 points. All within the certified enclosures:
- slopes m = 0..6 within [0.035648, 0.789591] ⊂ [0.035297, 0.790318];
- Θ₂: 0.1444493, 0.06968876, 0.006915215, 0.001000825, 0.0001648473, 2.812588·10⁻⁵ (each just above its floor, as expected for a sampled sup);
- Θ₁₀₀: 0.06497545, 0.03751665, 0.004220202, 0.0006174175, 0.0001019731, 1.741058·10⁻⁵;
- osc log R_m: 0.06338649, 0.03682711, 0.004151549, 0.0006077893, 0.0001004014, 1.714302·10⁻⁵ (all above the stated floors).
- Not independently recomputed: the `arb` jets and cell tables, the cell-pair upper bounds, the θ values, the K₀ = 214 periodic argument.

## Experimental Validation
Repo witness `python3 scripts/gasket_fractional_profile_level_f0_shift.py` at c7264ae: EXIT 0 in 276.4 s, "all Theorem DO checks passed". `DO_CELLS=16384` and pytest not rerun.

## Mathematical Status
Theorem (proof in repository; cell pairs outward-padded floats with `arb` floors). Kept failure DO.4 is a proved lower bound.

## Patent Relevance
None. Error constants for a transfer operator. Not a flux, not thrust.

## Related Discoveries
DISC-0226 (kept failure DN.4 answered), DISC-0221 (DI.1/DI.4 machinery), DISC-0223 (DK.4 bound improved at finite k), DISC-0224/0225 (θ values used), DISC-0205 (spectral 0.1725 still out of reach).

## Open Questions
m > 5 terms; whether any route moves the asymptotic rate below 0.3637; DC.1's K(β); Stage 2 (no Ψ_info).

## Next Experiments
Run `DO_CELLS=16384` once (~30 min); extend indep_theorem_DO.py to m = 6..10 to see how fast the direct terms shrink relative to θ₉^{1/9}.

## Reproduction Instructions
In informational-flux-identity @ c7264ae: `pip install python-flint numpy`, `python3 scripts/gasket_fractional_profile_level_f0_shift.py` (~5 min). Archive check: edit the `sys.path` line to point at that checkout's `scripts/`, then `python3 discoveries/mathematics/scripts/indep_theorem_DO.py` (~1.5 min).

## Evidence Log
- 2026-11-12 ~7:00 AM EST: read commit c7264ae message, file list, GASKET.md section header and CLAIM_STATUS row; independent float check all within enclosures (92.9 s); repo witness EXIT 0 (276.4 s).

## Change History
- 2026-11-12: created.
- 2026-11-12 ~8:10 AM EST (dated note): informational-flux-identity 7c94df4d7979 (Theorem DP, DISC-0228) proves every CF.1-form per-level rate on a C¹-open cone is ≥ 0.3170757, so the kept limit above (rate far from spectral 0.1725) cannot be closed by this route. Original text above preserved.
