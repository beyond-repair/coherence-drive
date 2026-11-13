# Discovery: Theorem EB, the level-n corner deficit is a Möbius function of rho^-n up to O(5^-0.65n), so DZ's limit is approached strictly from above with second-order coefficient nu_alpha^2 (1 - delta_N)

## Discovery ID
DISC-0241

## Status
THEOREM (mathematical sense only; EB.1–EB.2 have written proofs in the repository, conditional on DZ.1/DZ.2 and AZ (1)/(3) as stated; EB.3's numbers are arb-certified at alpha = 0.8 only, and its every-k monotonicity statements are finite windows). Method KNOWN (exact rational identity, geometric-series expansion, exponent comparison, outward-rounded interval arithmetic). Novelty of the specific results and constants UNRESOLVED. Answers DZ's kept limit "the second-order term of X_k - C_delta not certified" and EA's open item "DZ's second-order term in n, not N" (see dated notes on DISC-0238 and DISC-0240).

## Date Discovered
2026-11-13 (indexed ~10:05 AM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit f0c35377564e1eb18fabcaceba7bf6278be7a950 (2026-11-13 9:05 AM EST); parent 0a46e2094140 (Theorem EA, DISC-0240).

## Original Evidence
- GASKET.md §Theorem EB (header line 5817; NOT THIS line 5862), +58 lines; GASKET.md line 5804 (EA's open item annotated "now Theorem EB", original wording kept).
- CLAIM_STATUS.md (+3/-1, new row); README.md (+3/-1).
- scripts/gasket_fractional_corner_limit_mobius.py (new, 296 lines); registered in scripts/cli.py; tests/test_cli.py test_theorem_eb_corner_limit_mobius (+28); tests/test_flux_identity.py CornerMobiusFloatTests (+14, numpy-only CI test).

## Discovery
Setting as in Theorems AZ, DZ, EA: alpha in (gamma, 1), gamma = log3/log5, rho = 5^alpha/3, delta_N^(k) the level-k corner deficit, delta_N its limit, X_k = rho^k (delta_N - delta_N^(k)), C_delta(alpha, N) = -nu_alpha (1 - delta_N) DZ's limit of X_k, nu_alpha < 0 (AZ/DZ).
- EB.1 (proved, exact, every alpha, N >= 1, k >= N): X_k = C_delta/(1 + nu rho^-k) - [(1 - delta_N) eps_k/(1 + nu rho^-k) + rho^k eta_k]/D'_k. Equivalently delta_N^(k) = (delta_N + nu rho^-k)/(1 + nu rho^-k) + R_k, so 1/(1 - delta_N^(k)) is linear in rho^-k up to R_k.
- EB.2 (proved, every alpha): R_n = O(5^-0.65n) (AZ (1)'s eps rate; 5^0.65 < 3). Since rho^2 5^-0.65 < 1 and rho^2/3 < 1 on (gamma, 1), rho^n (X_n - C_delta) -> -nu C_delta = nu^2 (1 - delta_N) > 0: X_n approaches C_delta strictly from above at exact rate rho^-n and is eventually strictly decreasing. The third term -nu^3 (1 - delta_N) rho^-2n > 0 is controlled only for alpha < alpha* = (log_5 27 + 0.65)/3 = 0.89927.
- EB.3 (arb, alpha = 0.8, N = 1, 2, 3, 6, 10): -6.7e-21 <= X_k - C_delta/(1 + nu rho^-k) <= 8.7e-35 for every k >= 60; Y_oo = nu^2 (1 - delta_N) in [0.022763, 0.022789], [0.115609, 0.115629], [0.187830, 0.187845], [0.335697, 0.335707], [0.438309, 0.438314]; X_k > C_delta and X_k decreasing on [60, 232] (all N); Y_k > Y_oo and decreasing on [60, 115]; rho^60 (Y_60/Y_oo - 1)/(-nu) in [1.000008, 1.000010].
- EB.4 (floats only, OBSERVED): the slope of 1/(1 - delta_N^(k)) against rho^-k recovers an N-independent nu_alpha (0.8: -0.727445869; 0.9: -0.43284356; 0.7: -0.96180312; 0.95: -0.24827785); remainder ratio about rho/3 per level, i.e. R_n ~ 3^-n observed, not claimed.

## Why It Matters
Turns DZ's limit statement into a closed Möbius-form law in rho^-n with an explicit, sign-definite second-order coefficient, and gives a practical estimator of nu_alpha that does not depend on N. It closes the last second-order gap in the corner-deficit chain AZ → DZ → EA → EB.

## Derivation
EB.1 re-derived by hand here: with x = rho^-k and C_delta = -nu (1 - delta), delta - x C_delta/(1 + nu x) = (delta + delta nu x + nu x - nu x delta)/(1 + nu x) = (delta + nu x)/(1 + nu x), and 1 - that = (1 - delta)/(1 + nu x), linear reciprocal in x. Expanding C_delta/(1 + nu x) = C_delta (1 - nu x + nu^2 x^2 - ...) gives second coefficient -nu C_delta = nu^2 (1 - delta) > 0 and third nu^2 C_delta = -nu^3 (1 - delta) > 0 (nu < 0). EB.2's thresholds: with rho = 5^alpha/3, rho^2 5^-0.65 < 1 iff alpha < (0.65 + 2 log_5 3)/2 = 1.0076; the third term dominates the remainder iff rho^3 < 5^0.65 iff alpha < (log_5 27 + 0.65)/3 = 0.899273 (recomputed in mpmath).

## Assumptions
DZ.1 (K_1, m_0, ebar), DZ.2's exact form of X_k, AZ (1)'s eps rate 5^-0.65n, AZ (3)'s nu_0.8, EA.4's C_delta(0.8, N) brackets, all as stated in the repository. python-flint arb and sympy correctness.

## New Results
Exact Möbius representation of the level-n deficit; sign and exact order of the second-order term for every alpha in (gamma, 1); third-order sign for alpha < 0.89927; certified Y_oo(0.8, N) for five N; N-independent float estimator of nu_alpha.

## Prior Art
Möbius/linear-fractional dependence of renormalised resistances or Dirichlet forms on the decimation parameter is standard on the Sierpinski gasket (Kigami; Strichartz; Fukushima–Shima spectral decimation; Teplyaev); asymptotic expansion of a ratio by geometric series is textbook; interval enclosures follow Tucker 2011 / arb (Johansson). No external source for these constants was searched in this slice.

## Novelty Analysis
Method KNOWN. The specific identity, the coefficient nu^2 (1 - delta_N) and the certified constants are new to the corpus; external novelty UNRESOLVED and of modest consequence.

## Falsification Attempts
- Hand re-derivation of EB.1's Möbius form and its series coefficients: holds.
- Independent mpmath (30 digits): alpha* = 0.8992728612 and 5^0.65 = 2.8466 < 3 reproduced; Y_oo = -nu C_delta recomputed from EA.4's C_delta brackets with nu = -0.727445869 gives [0.0227640, 0.0227887], [0.1156101, 0.1156282], [0.1878302, 0.1878447], [0.3356981, 0.3357068], [0.4383094, 0.4383138], inside the published brackets; 1/(1 + nu rho^-60) = 1.0000086800 at rho(0.8) = 1.2079661 matches the printed third-order ratio 1.000008680.
- Rounding check: the commit message's Y_oo brackets are outward roundings of the script's printed ones (for example N = 2 printed [0.115610, 0.115628], stated [0.115609, 0.115629]): consistent, no defect found.
- Scope attack: EB.3's "every k" monotonicity claims are windows ([60, 232] for X_k, [60, 115] for Y_k), and the remainder exponent 0.65 is weaker than the observed 3^-n; the repo states both as kept limits. The third-order sign is not claimed for alpha >= 0.89927.

## Experimental Validation
None applicable (pure mathematics). Not thrust; no flux; Stage 2 still blocked (no Psi_info).

## Mathematical Status
Theorem as stated (EB.1–EB.2), conditional on the listed inputs; EB.3 computer-assisted at alpha = 0.8 only; EB.4 observed only.

## Patent Relevance
None. Pure mathematics on a graph; not a mechanism.

## Related Discoveries
DISC-0238 (Theorem DZ; kept limit answered), DISC-0240 (Theorem EA; open item answered, C_delta(0.8, N) brackets used), DISC-0239 (Kept Failure DZ.4; consistency checked), DISC-0127 (Theorem AZ; eps rate and nu_0.8 used).

## Open Questions
Sharpen the remainder from 5^-0.65n to the observed 3^-n; the third-order sign for alpha in [0.89927, 1); every-k (not windowed) monotonicity at 0.8; certified values off 0.8; closed forms for nu_alpha, delta_N.

## Next Experiments
Prove R_n = O(3^-n) from AZ's eps structure; certify Y_oo at alpha = 0.9 or 0.95 (above alpha*); use EB.4's slope estimator to cross-check nu_alpha at the 0.7/0.9/0.95 values against an independent arb computation.

## Reproduction Instructions
Clone informational-flux-identity at f0c35377564e1eb18fabcaceba7bf6278be7a950; `pip install python-flint sympy numpy`; `python3 scripts/gasket_fractional_corner_limit_mobius.py` (~5 s); tests `python3 -m pytest -q tests/test_cli.py -k test_theorem_eb` and `python3 -m pytest -q tests/test_flux_identity.py -k CornerMobius`.

## Evidence Log
- 2026-11-13 ~9:58 AM EST: repo default witness `python3 scripts/gasket_fractional_corner_limit_mobius.py` EXIT 0, 21 "ok" checks, no failures (~5 s wall; repo states 4.7 s).
- 2026-11-13 ~10:00 AM EST: hand derivation and mpmath arithmetic PASS; no display defect found.

## Change History
- 2026-11-13: created.
- 2026-11-13 (dated note): Theorem EC (IFI ebaa8c8629b4, DISC-0242) answers EB's kept limit: R_n = O(3^-n) (upper bound), third-order sign for alpha < 4 gamma/3 = 0.910142, and EB.3's windows at 0.8 become every k >= 60. No status change.
- 2026-11-13 (dated note): Theorem ED (IFI 417b34c61298, DISC-0243) proves R_n = Theta(3^-n): EB's third term holds exactly on (gamma, 4 gamma/3) and fails above; EB.4's rho/3 ratio still needs a limit and stays observed. No status change.
