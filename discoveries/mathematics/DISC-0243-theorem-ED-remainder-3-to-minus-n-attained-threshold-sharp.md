# Discovery: Theorem ED, the corner-deficit remainder is exactly of order 3^-n on (gamma, 1), so EC's 4 gamma/3 threshold is sharp and the third-order term fails above it

## Discovery ID
DISC-0243

## Status
THEOREM (mathematical sense only; ED.1–ED.3 have written proofs in the repository, conditional on AQ (1)–(3), BK.1, BK.2, AZ (1)/(3), DZ.1, DZ.3, EB.1, EC.2 and EA.4 as stated; ED.2's constants and ED.4 are arb-certified at listed alpha values only; ED.5 is floats, OBSERVED). Method KNOWN (monotonicity of a weight excess, pointwise comparison lemmas, geometric-tail sums, outward-rounded interval arithmetic). Novelty of the specific results and constants UNRESOLVED. Answers DISC-0242's kept limit "Theta(3^-n) observed only" and its open item "a lower bound on the 3^-n coefficient" (dated note on DISC-0242). No status change elsewhere.

## Date Discovered
2026-11-13 (indexed ~12:05 PM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 417b34c6129847a0abd28f85eb5d91b8db106059 (2026-11-13 11:14 AM EST); parent ebaa8c8629b4 (Theorem EC, DISC-0242).

## Original Evidence
- GASKET.md §Theorem ED (header line 5933; NOT THIS line 5996), +84/-8 lines; EC's kept limit (line 5918), EC.3's "not claimed either" (line 5897), EC's and EB's "What stays open" (lines 5920, 5860) annotated in place with original wording kept; EC's B_0.7 corrected from 3.88e3 to 3.89e3 in place with a note (line 5889).
- CLAIM_STATUS.md (+2/-2, new row); README.md (+2/-1).
- scripts/gasket_fractional_corner_remainder_lower.py (new, 270 lines); registered in scripts/cli.py; tests/test_cli.py (+27); tests/test_flux_identity.py (+29, numpy-only CI test).

## Discovery
Setting as in Theorems AT, AZ, DZ, EA, EB, EC: gamma = log3/log5, rho = 5^alpha/3, eps_n AZ (1)'s defect, R_n EB.1's remainder, X_n = rho^n (delta_N - delta_N^(n)).
- ED.1 (exact, every alpha in (gamma,1)): BK.1's weight excess Mt_k = ∫ t^-alpha r_k(t)(omega_k(q(t)) - 1) dt >= 0 is nondecreasing in k; D'_(k+1) - D'_k = rho^-k Mt_k; C' = -Mt_oo rho/(rho-1); eps_n = rho^n Σ_(k>=n) rho^-k (Mt_oo - Mt_k) >= 0 for every n.
- ED.2 (explicit, every k >= 0): Mt_(k+1) - Mt_k >= ell_alpha (rho/3)^k from four pointwise lemmas, hence eps_n >= L_alpha (rho/3)^n with L_alpha = 3 ell_alpha / (2(1 - rho/3)). Certified: ell_gamma >= 0.0016681 (uniform L_alpha >= 0.0025021), L_0.7 >= 0.0039644, L_0.8 >= 0.0055320, L_0.9 >= 0.0080303, L_0.95 >= 0.0098674. With EC.2, (3/rho)^n eps_n in [0.005532, 1.94e3] at 0.8 for n >= 6.
- ED.3: R_n >= (1 - delta_N) L_alpha 3^-n / D'_oo, so R_n = Theta(3^-n); X_n < C_delta/(1 + nu rho^-n) strictly; the J-term expansion of X_n holds if and only if rho^J < 3 (alpha < (J+1) gamma/J). So EB's third term holds exactly on (gamma, 4 gamma/3); for rho^J > 3, rho^((J-1)n)(X_n - partial sum) = -Theta((rho^J/3)^n); for alpha in (4 gamma/3, 1), Y_n < Y_oo for all large n (approach from below).
- ED.4 (arb, alpha = 0.8): 3^n R_n in [3.716e-5, 13.97] (N=1), [1.887e-4, 68.44] (2), [3.066e-4, 113.2] (3), [5.480e-4, 280.6] (6), [7.155e-4, 3.624e3] (10) for every n >= 60.
- ED.5 (floats, OBSERVED): (3/rho)^k (Mt_(k+1) - Mt_k) ~ 0.295, (3/rho)^n eps_n ~ 0.741 at 0.8; C' from Mt_oo = -4.658677537 vs AZ (3)'s -4.658677573.

## Why It Matters
It completes the corner-deficit remainder chain AT → AZ → DZ → EA → EB → EC with a matching lower bound, turning EC's "end of route, neither claimed nor refuted" at 4 gamma/3 into a sharp if-and-only-if: the Möbius expansion's third term is exactly valid below 4 gamma/3 and fails above it, where the approach to Y_oo flips side.

## Derivation
Checked here: from ED.2's increment bound, Mt_oo - Mt_k >= ell (rho/3)^k / (1 - rho/3), and then eps_n >= rho^n ℓ/(1 - rho/3) Σ_(k>=n) 3^-k = (3 ell/(2(1 - rho/3))) (rho/3)^n, which is the repo's L_alpha. The iff threshold: rho^J < 3 iff J(alpha log5 - log3) < log3 iff alpha < (J+1) gamma/J (J = 3 gives 0.9101416). The lemma domain endpoint: U(x1) = 5 x1 exp(5 x1 e^0.1/20) with x1 = 0.4 e^-0.1 equals exactly 2, so "U <= 2 on x <= x1" is tight at the endpoint and consistent.

## Assumptions
AQ (1)–(3), BK.1, BK.2, AZ (1)/(3), DZ.1, DZ.3, EB.1, EC.2, EA.4, all as stated in the repository; the uniform constant assumes ell_alpha >= ell_gamma on (gamma,1) as the repo states. python-flint arb correctness.

## New Results
Two-sided Theta(3^-n) for R_n and Theta((rho/3)^n) for eps_n on (gamma,1) with explicit lower constants at five alpha values; sharpness of EC.3's thresholds (iff); side-flip of Y_n's approach above 4 gamma/3; certified two-sided 3^n R_n brackets at 0.8 for five N.

## Prior Art
Lower bounds from monotone positive increments and pointwise comparison are standard; renormalisation and decimation on the Sierpinski gasket (Kigami; Strichartz; Fukushima–Shima; Teplyaev); interval enclosures (Tucker 2011; arb, Johansson). No external source for these constants was searched in this slice.

## Novelty Analysis
Method KNOWN. The constants and the sharpness statement are new to the corpus; external novelty UNRESOLVED and of modest consequence.

## Falsification Attempts
- Independent mpmath (30 digits): rho at 0.7, 0.8, 0.9, 0.95 (1.028390, 1.207966, 1.418900, 1.537801); L_alpha recomputed from the printed ell_alpha matches the printed L_alpha to the last printed digit (L_0.95 from the rounded-down ell gives 0.0098673 vs printed 0.0098674, consistent with ell being printed rounded down); 4 gamma/3 = 0.910141593; 0.741/L_0.8 = 133.9, matching the repo's "~134x below floats"; ED.5's 0.295 × 3/(2(1 - rho/3)) = 0.741, internally consistent.
- Slack remark (not a defect): since rho > 1 on (gamma,1), 1 - rho/3 < 2/3, so the uniform bound could be 2.25 ell_gamma >= 0.0037532 rather than the repo's 1.5 ell_gamma = 0.0025021, given the same ell_alpha >= ell_gamma assumption. The repo's value is valid, just looser.
- Scope attack: the limit of 3^n R_n is not claimed (EB.4/EC.5 ratios stay observed); brackets are loose (~134x); thresholds "all large n" non-explicit; sign at exactly alpha = 4 gamma/3 open; (gamma,1) only. The repo states each of these as kept limits. No overclaim found.
- Display check: commit-message numbers match the witness output (ell and L values, 3^n R_n brackets, ratio 1.067, C' = -4.658677537).

## Experimental Validation
None applicable (pure mathematics). Not thrust; no flux; Stage 2 still blocked (no Psi_info).

## Mathematical Status
Theorem as stated (ED.1–ED.3), conditional on the listed inputs; ED.2 constants and ED.4 computer-assisted; ED.5 observed only.

## Patent Relevance
None. Pure mathematics on a graph; not a mechanism.

## Related Discoveries
DISC-0242 (Theorem EC; kept limit and open item answered, B_0.7 rounding corrected), DISC-0241 (Theorem EB; third term now exact on (gamma, 4 gamma/3), EB.4 ratio still observed), DISC-0127 (Theorem AZ; eps_n now proved positive), DISC-0238 (Theorem DZ), DISC-0240 (Theorem EA).

## Open Questions
The limit of 3^n R_n (and of (3/rho)^n eps_n, observed ~0.741 at 0.8); the sign at alpha = 4 gamma/3; explicit "large n" thresholds; alpha <= gamma; closed forms.

## Next Experiments
Prove convergence of (3/rho)^k (Mt_(k+1) - Mt_k) (observed ~0.295 at 0.8); certify ED.4 off 0.8; tighten L_alpha toward the floats.

## Reproduction Instructions
Clone informational-flux-identity at 417b34c6129847a0abd28f85eb5d91b8db106059; `pip install python-flint sympy numpy`; `python3 scripts/gasket_fractional_corner_remainder_lower.py` (~1.5 s); tests `python3 -m pytest -q tests/test_cli.py` and `python3 -m pytest -q tests/test_flux_identity.py`.

## Evidence Log
- 2026-11-13 ~12:00 PM EST: repo default witness EXIT 0 (1.7 s wall), "all ED checks passed", every printed check "ok"; tests/test_flux_identity.py ED subset 2 passed (0.34 s).
- 2026-11-13 ~12:00 PM EST: mpmath arithmetic PASS; no display defect found; one slack remark recorded.

## Change History
- 2026-11-13: created.
