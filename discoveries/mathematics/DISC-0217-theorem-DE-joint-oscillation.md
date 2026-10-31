# Discovery: Theorem DE, the joint (ratio-of-sums) oscillation for CF.2's cone (θ 0.4267 → 0.1599, per-level rate 0.8434 → 0.6931)

## Discovery ID
DISC-0217

## Status
THEOREM in the mathematical sense only (the repository contains the proof and a certified witness: `arb` enclosures plus a float dynamic programme with outward rounding). Method KNOWN (Birkhoff–Hilbert-metric cone contraction; exact maximisation of a linear-fractional functional under Lipschitz constraints). Constants UNRESOLVED as to novelty. The spectral rate 0.1725 is unchanged and still reached only by the spectral route.

## Date Discovered
2026-10-31 (indexed ~11:00 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 8cbaea3aa21f89007e5f01a4f3ee4c7f449f1cc3 (2026-10-31 10:10:04 EDT).

## Original Evidence
- GASKET.md §"Theorem DE. The joint oscillation for CF.2's cone" (inserted after Theorem DD, before Conjecture J.1).
- CLAIM_STATUS.md, one new row.
- scripts/gasket_fractional_profile_level_joint.py (new, 442 lines; imports DD's script, hence CF's, unchanged; CE's for r; CC's for level sums).
- tests/test_cli.py `test_theorem_de_profile_level_joint`; README.md reproduction list; scripts/cli.py registration.

## Discovery
Same setting as CE/CF/DC/DD (X_s = [√5/2, 5/2], σ_{1,2}(s) = √(15/4 ∓ s), cone C_a with a = 47/2, block L̃⁵, b₅ = 2.0785933). DD bounded the last term of the cone-lemma diameter, log(sup(v/u)/inf(v/u)), by osc log u + osc log v ≤ 2V_D. DE computes that joint term directly.
- DE.1 (exact): for fixed (x, y) the sups over f and g separate, so the joint term is ≤ W = sup_{x,y}[ρ(x,y) + ρ(y,x)], with ρ(x,y) = sup_{f∈C_a} log(L̃⁵f(x)/L̃⁵f(y)). ρ is the value of a 64-point linear-fractional programme on the line (consecutive log-Lipschitz constraints suffice), solved by a backward recursion whose maximiser is bang-bang.
- DE.2 (certified, adaptive 128 → 65536 cell cover): W ≤ 0.29040 (DD: 2V_D = 1.46876), Δ_E ≤ 0.64513, θ_E = tanh(Δ_E/4) ≤ 0.15990, θ_E^{1/5} < 0.69306.
- DE.3 (arb floors): W ≥ 0.29009 (W_E/W_low ≤ 1.0011); sup_f osc log L̃⁵f ≥ 0.66531, so DD's V_D = 0.73438 was already within 1.104× of the single-function value and DE's gain is from the joint term.
- DE.4: CF.3, CF.5, DC.1–DC.3, DD.3 hold with θ_E: non-leading C¹ eigenvalues |μ| < 0.29367 (DD: 0.3575); level-sum bound |log(s_{k+1}/(r s_k))| ≤ θ_E^{⌊(k−4)/5⌋}·0.28154093 ≤ 5.28923·θ_E^{k/5}, smaller than DD.3's by 2.6687, 7.1219, 50.722, 1.83·10⁴ at k = 9, 14, 24, 54.

## Why It Matters
Closes DD's open item "the true ratio-of-sums oscillation" to 0.11%, and roughly halves the gap in the Birkhoff route (0.8434 → 0.6931 per level). The float observation (no claim) that the joint term → 0 with larger (a, n) reverses DD's float finding that the separated term stalls near 0.594, so log-Lipschitz cones are no longer shown to stall.

## Derivation
sup(v/u)/inf(v/u) = sup_{x,y} v(x)u(y)/(u(x)v(y)); for fixed (x,y) the first factor depends on g only, the second on f only. For ρ: Σ A_k u_k ≤ t Σ B_k u_k for all admissible u iff max Σ(A_k − tB_k)u_k ≤ 0 with u_1 = 1, computed backward as V_k = c_k + max(e^{ad_k}V_{k+1}, e^{−ad_k}V_{k+1}). Monotone in c, V, d, so cell enclosures give upper bounds. Δ_E = 2 log((a+b₅)/(a−b₅)) + W_E; θ = tanh(Δ/4) (Birkhoff).

## Assumptions
CE.3 cone lemma; CF.1; CF.2's cone step and b₅ (re-run in repo); CF.3/CF.5 arguments (use Δ only through θ); DC.1–DC.3 proofs and DC.2's Θ_G ≤ 0.28154093 (not re-run). Float DP correctness with nextafter outward rounding and 10⁻¹² exponential pads (same rigour level as DD.2).

## New Results
θ_E ≤ 0.15990; per-level Birkhoff rate < 0.69306; non-leading C¹ spectral radius < 0.29367; joint term known to 0.11%; single-function oscillation floor 0.66531.

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995; Baladi 2000 (cone contraction for transfer operators). Maximising a linear-fractional functional over Lipschitz functions on finitely many points is a standard LP / Charnes–Cooper problem. No prior computation of these specific constants found; not searched beyond that, so novelty of constants is UNRESOLVED.

## Novelty Analysis
Technique KNOWN. Contribution is a certified sharper constant for this repository's operator. Not a world first; no claim made.

## Falsification Attempts
- Independent script `mathematics/scripts/indep_theorem_DE.py` (numpy + mpmath + scipy HiGHS, written from GASKET.md text; ρ computed as a Charnes–Cooper linear programme, not the repo's recursion): 9/9 PASS. Endpoint joint term 0.29009723 (inside [W_low, W_E]); 41×41 point grid maximum 0.29009723 at (√5/2, 5/2), ≤ W_E; single-function maximum 0.6653165 (inside [0.66531, V_D]); Δ_E = 0.6451291, θ_E = 0.1598982, rate 0.6930567, C_E = 5.2892200, DD.3/DE.4 ratios, θ_E^{1/5}·r < 0.29367 (r = 0.4237313 from DD's independent power iteration) all reproduced. One of 1640 LPs failed numerically under HiGHS simplex (status 15); the interior-point fallback solved it; documented, no effect on the maximum.
- Attack on DE.1's separation: correct, since sup over (f,g,x,y) of a sum whose two parts depend on disjoint variable sets for fixed (x,y) equals sup_{x,y} of the sum of the two sups.
- Not independently recomputed: the certified outward-rounded cell cover (my check is pointwise, so it confirms the value, not the rigorous upper bound); CF.2's b₅; DC.2's Θ_G. θ_E^{1/5}·r = 0.293670 sits close to 0.29367 in floats; the repo certifies it in arb.

## Experimental Validation
Repo witness `python3 scripts/gasket_fractional_profile_level_joint.py` EXIT 0 in 28.1 s ("all Theorem DE checks passed"). `pytest tests/test_cli.py -k joint`: 1 passed (27.1 s).

## Mathematical Status
Theorem (proof in repository; certified constants). The (a, n) observation is floats only, no claim.

## Patent Relevance
None. A contraction constant for a transfer operator, not a mechanism. Not thrust, not a flux.

## Related Discoveries
DISC-0216 (Theorem DD; DE replaces 2V_D by the joint term), DISC-0215 (Theorem DC; constants used), DISC-0190 (Theorem CF; cone, block, b₅), DISC-0188 (Theorem CE; setting, cone lemma), DISC-0205 (spectral route, 0.1725, still sharper).

## Open Questions
Certify a larger (a, n) with the joint term and carry CF.3/DC to that cone; the cone-lemma term 0.35473 (now more than half of Δ_E) versus the true Hilbert diameter; whether this cone family can approach 0.1725.

## Next Experiments
Certify the (a, n) = (100, 8) observation (rate ≈ 0.643); replace the cone-lemma bound by an exact Hilbert-diameter computation.

## Reproduction Instructions
In informational-flux-identity @ 8cbaea3aa21f: `pip install python-flint numpy sympy mpmath`, `python3 scripts/gasket_fractional_profile_level_joint.py` (~30 s). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_DE.py` (needs scipy; ~4 s).

## Evidence Log
- 2026-10-31 ~11:00 EDT: read commit 8cbaea3aa21f diff; repo witness EXIT 0 (28.1 s); pytest 1 passed; independent 9/9 PASS.

## Change History
- 2026-10-31: created.

### Dated note 2026-10-31 (~12:20 EDT)
DE's open item "certify a larger (a, n)" is done by Theorem DF (informational-flux-identity 3f0579e83c80): C₁₀₀ under L̃⁸, θ_F < 0.02958, rate < 0.64398. See DISC-0218. DE's bound stays smaller at k = 9, 10, 11, 19. This record is otherwise unchanged.
