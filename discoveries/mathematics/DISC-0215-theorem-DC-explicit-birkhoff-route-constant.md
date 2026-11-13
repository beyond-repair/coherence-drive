# Discovery: Theorem DC — CF.3's Birkhoff-route constant made explicit (general log-Lipschitz f, and the level sums)

## Discovery ID
DISC-0215

## Status
THEOREM in the mathematical sense only (interval-certified with `arb` at 200 bits, computer-assisted, test local only, not in CI). Method KNOWN (Birkhoff/Hilbert-metric cone contraction with explicit cone diameter, as in DISC-0190). Constants UNRESOLVED as to novelty. Closes the kept limit of DISC-0190 (C_G "not made explicit") and DISC-0205's kept item (Birkhoff-route Θ_a(f_0, L̃f_0) not computed) on the Birkhoff route. The resulting constant is explicit but 35.4 times the sharp spectral constant of DISC-0205, so it improves nothing quantitatively. Not a flux, not thrust.

## Date Discovered
2026-10-31 (repo commit 07:56 EDT; indexed ~8:25 AM EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 4996a9fca8782a8a80ceb41494872f85dacbb55d

## Original Evidence
- GASKET.md §"Theorem DC" (+44 lines at 4996a9fca878, line ~4645)
- CLAIM_STATUS.md (+1 row), README.md (+3/−1)
- scripts/gasket_fractional_profile_level_birkhoff.py (new, 339 lines; imports CF's, CO's and CN's scripts unchanged)
- tests/test_cli.py (+29, `test_theorem_dc_profile_level_birkhoff`), scripts/cli.py (+1)

## Discovery
Setting of CE/CF/CS: L̃f = w̃_1 f∘σ_1 + w̃_2 f∘σ_2 on X = [−5, 0], s = √(t + 25/4) ∈ [√5/2, 5/2], cones C_b = {f > 0 : log f b-Lipschitz in s}, a = 47/2, θ = tanh(Δ/4) = 0.5441333187…, φ(b) = max(M_1 + c_1 b, M_2 + c_2 b), b* = M_1/(1 − c_1) = 1.688415861….

- DC.1 (proved): L̃^j C_b ⊂ C_{β_j}, β_j = b* + c_1^j (b − b*)_+; for every f > 0 with log f b-Lipschitz, every j with β_j < a and m ≥ j, |log(L̃^{m+1}f/L̃^m f) − log r| ≤ θ^{⌊(m−j)/5⌋} K(β_j), K(β) = 2 log((a+B)/(a−B)) + (β + φ(β))|X_s|, B = max(β, φ(β)).
- DC.2 (certified): for f_0 = L̃^4 G, F_0 ∈ [0.0029654816, 0.0048349722], b_0 ≤ 0.77333706, B_0 = φ(b_0) ≤ 1.2791803, Θ_G ≤ 0.28154093.
- DC.3: |log(s_{k+1}/(r s_k))| ≤ θ^{⌊(k−4)/5⌋} Θ_G ≤ 0.74544057 θ^{k/5} for every k ≥ 4.
- DC.4: the Birkhoff route has a floor log(sup R_0/inf R_0) ≥ 0.0633864 for this f_0 and cone; C_G^B/C_G* = 35.411.

## Why It Matters
It removes the last "not made explicit" constant in CF.3, using no spectral input at all, and it quantifies exactly how much the Birkhoff route loses against the spectral route (factor 35.4 in the constant, rate θ^{1/5} < 0.8855 against |λ_2|/r = 0.1725). Its value is bookkeeping and a clean comparison of two proof routes, not a sharper estimate.

## Derivation
Checked by hand: DC.1(i) (first branch of φ fixes b* exactly since M_1 = b*(1 − c_1); second branch lies below because M_2 < M_1 and c_2 < c_1); DC.1(ii) from the cone lemma (α_a ≥ ((a−B)/(a+B)) inf v/u, β_a ≤ ((a+B)/(a−B)) sup v/u) and sup/inf ≤ exp(osc log u + osc log v); the shift L̃^{m+1}f/L̃^m f = L̃^{m−j+1}g/L̃^{m−j}g with g = L̃^j f; DC.3's second inequality from ⌊(k−4)/5⌋ ≥ (k−8)/5. DC.2's cell enclosures are machine computations I re-ran but did not re-derive.

## Assumptions
CE.1–CE.3 and CE.3's cone lemma; CF.1–CF.3 (CF.2's constants); CO.1–CO.2's Taylor data for F_0 (re-run unchanged by the repo); CN.1's box argument; CG.3's enclosure of r; CC's level sums s_4, s_5 (consistency and DC.4 only).

## New Results
As above. Archive arithmetic: K(0) = 1.448784, K(M_1) = 3.386667, K(b*) = 4.954553, K(10) = 23.107546, K(23) = 56.355034; b = 100 needs j_0 = 2 (β = 21.350733), b = 10^4 needs j_0 = 8 (β = 17.685714); full-precision θ = 0.54413331871978955232.

## Prior Art
Birkhoff's contraction theorem for the Hilbert projective metric (Birkhoff 1957; Bushell 1973) and its use for transfer operators with explicit cone constants (Liverani 1995, "Decay of correlations"; Baladi 2000). Method KNOWN; the constants are corpus-specific. Novelty UNRESOLVED (no literature search beyond this).

## Novelty Analysis
No new method. The explicit constants are specific to this operator. Nothing here is a candidate for novelty beyond "computed for this operator".

## Falsification Attempts
- Independent check `mathematics/scripts/indep_theorem_DC.py` (own code, no repo imports; mpmath 200-bit arithmetic on DC.1/DC.3/DC.4 constants and a float64 branch-tree test of DC.1(ii)): v1 **21/23 PASS**. Both failures were my bugs, kept here: (1) I tested log(sup R_0/inf R_0) from the 10-digit printed R_0 endpoints in the wrong direction (0.0635926995 vs the certified upper 0.063592701; they agree to 1.5·10⁻⁹); (2) I computed C_G^B from the *rounded* Θ_G = 0.28154093 and a 10-digit θ, giving 0.7454405771, which exceeds the printed 0.74544057 by 7.1·10⁻⁹. v2 `indep_theorem_DC_v2.py` recomputes θ in full (CF.2 recipe) and Θ_G unrounded (0.2815409263): C_G^B = 0.7454405672 ≤ 0.74544057, and the repo's own ball is [0.74544056 ± 2.37·10⁻⁹]. So with v2 every check passes (23/23).
- Presentational note (not a contradiction): the chain "Θ_G ≤ 0.28154093 ⇒ C_G^B ≤ 0.74544057" does not follow from the printed rounded number alone (7·10⁻⁹ short); it holds from the unrounded enclosure the script uses.
- Attack on DC.1(ii)'s general-f bound: 40 random f with log f = sum of four sines in s scaled to Lipschitz constant b ∈ {0.5, 1, b*, 5, 15, 23, 60, 300}, j = j_0(b), m − j ≤ 13, 13 points of X: no violation; largest used fraction of the bound 0.326.
- Not checked independently: DC.2's 16384-cell enclosures of F_0, b_0 and R_0 (need G and CO's Taylor data); s_6..s_13 consistency (CC's digits not printed in GASKET.md).

## Experimental Validation
Computational only. No physical claim.

## Mathematical Status
Theorem (interval-certified, computer-assisted) for DC.2/DC.3; DC.1 is a short proof checked by hand.

## Patent Relevance
None. The repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0190 → DISC-0215 (mathematical): CF.3's constant made explicit. DISC-0205 → DISC-0215 (mathematical): comparison with CS's sharp C_G* (ratio 35.411). DISC-0188 → DISC-0215 (mathematical): CE's setting and cone lemma. DISC-0214 → DISC-0215 (historical): DB listed this item as open.

## Open Questions
A better cone (smaller Δ) for the Birkhoff route; re-optimising a and θ; second-order terms of Γ_±^(k) − ((2k+3)/12)κ_∓ and of q^(k) + 1/3; circle eigenvalues; λ_6, a_6; closed forms; Ψ_info / Stage 2 still blocked.

## Next Experiments
Scan a ∈ (b*, ∞) and the block length 5 to minimise C_G^B·θ^{k/5} for fixed k, to see how close the Birkhoff route can get to the spectral constant; independently enclose F_0 from CE's definition of G to close the one unchecked step.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at 4996a9fca878; `pip install python-flint mpmath sympy`; `python3 scripts/gasket_fractional_profile_level_birkhoff.py`. Independent: `python3 discoveries/mathematics/scripts/indep_theorem_DC.py` (about 3 min, numpy + mpmath), then `python3 discoveries/mathematics/scripts/indep_theorem_DC_v2.py` (seconds).

## Evidence Log
- 2026-10-31 ~8:05 AM EDT: my first witness launch failed with `python: command not found` (EXIT 127; my invocation, not the repo). Relaunched with python3.
- 2026-10-31 ~8:10 AM EDT: repo witness at 4996a9fca878 EXIT 0 ("elapsed 122.3s", 20 `ok` lines, 0 failures, "all Theorem DC checks passed"); faster than the stated ~15 min, no content discrepancy. Repo ball C_G^B = [0.74544056 ± 2.37e-9], Θ_G = [0.28154092 ± 4.45e-9], θ = [0.5441333187 ± 1.98e-11].
- 2026-10-31 ~8:12 AM EDT: independent check v1 21/23 (two failures, my bugs, above); v2 resolves both.
- 2026-10-31 ~8:20 AM EDT: repo pytest `tests/test_cli.py -k theorem_dc` EXIT 0 (1 passed, 116.94 s).

## Change History
- 2026-10-31: created from IFI 4996a9fca878.
