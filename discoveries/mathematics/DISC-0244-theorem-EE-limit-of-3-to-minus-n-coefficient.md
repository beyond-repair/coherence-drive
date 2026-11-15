# Discovery: Theorem EE, the 3^-n coefficient of the corner-deficit remainder has a limit on (gamma, 1), with explicit integral formulas over the level-infinity scaled profile

## Discovery ID
DISC-0244

## Status
THEOREM (mathematical sense only; EE.1–EE.3 have written proofs in the repository, conditional on AQ (1)–(3), BI.4, BK.1, BK.2, ED.1, ED.2 (a), DZ.1, DZ.2 and EB.1 as stated; EE.4's constants are arb-certified (128 bits, monotone cell bounds plus explicit head and tail) at listed alpha values only; EE.5 is floats, OBSERVED). Method KNOWN (affine recursion for reciprocal resistances, Poincaré-function / Tannery limit of a scaled profile, dominated convergence, interval arithmetic). Novelty of the specific limits and constants UNRESOLVED. Answers DISC-0243's kept limit "no limit of (3/rho)^n eps_n or 3^n R_n is proved" and its open item (dated note on DISC-0243); promotes DISC-0241's EB.4 error ratio rho/3 and DISC-0242's EC.5 ratio w_(k+1)/w_k -> 1/3 from OBSERVED to THEOREM inside the repo (dated notes on both). No archive status change otherwise.

## Date Discovered
2026-11-15 (indexed ~7:05 AM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit d3104a6468849683afa9b4f7b919aae885f95c35 (2026-11-15 6:28 AM EST); parent 417b34c61298 (Theorem ED, DISC-0243).

## Original Evidence
- GASKET.md §Theorem EE (header line 6007; kept limits line 6068; what stays open line 6070; NOT THIS line 6072), +80/-4 lines; ED's kept limit and open item (lines 5992, 5994), EB.4 (line 5852) and EC.5 (line 5912) "not claimed" annotated in place with the original wording kept.
- CLAIM_STATUS.md (+1/-1, new row); README.md (+2/-1).
- scripts/gasket_fractional_corner_remainder_limit.py (new, 409 lines); registered in scripts/cli.py; tests/test_cli.py (+24); tests/test_flux_identity.py (+30, numpy-only CI test).

## Discovery
Setting as in Theorems AZ, DZ, EA, EB, EC, ED: gamma = log3/log5, rho = 5^alpha/3, eps_n AZ (1)'s defect, Mt_k BK.1's weight excess, R_n EB.1's remainder, w_k EC.5's second difference.
- EE.1 (every alpha in (gamma,1)): with u_k = 1/r_k the step is affine, u_(k+1)(s) = beta(s) u_k(ps) - e(s), u_0 - u_1 = (s+6)/(s+5). The scaled profile G = lim (3/5)^k r_k(5^-k x) exists along the Poincaré function Phi = lim p^k(5^-k x) (Tannery), with 1/G = A (3 + Phi) - sum_m e(Phi(5^-m x)) (5/3)^m A_m and D = (5/3) G(5x) - G = G Gh A (Phi+6)/(Phi+5). By dominated convergence in x = 5^k t, (3/rho)^k (Mt_(k+1) - Mt_k) -> d* = (1/3) ∫ x^(1-a) D (G + Gh) > 0.
- EE.2 (with ED.1): (3/rho)^n eps_n -> e* = 3 d* / (2 (1 - rho/3)).
- EE.3 (with DZ.1, DZ.2, EB.1): 3^n eta_n -> (3/2) kappa_N with kappa_N = (1/3) ∫ x^(1-a) G^2 eta_N(Phi(5^-N x)); hence 3^n R_n -> varrho_N = [(1 - delta_N) e* + 1.5 kappa_N] / D'_oo > 0 and R_(n+1)/R_n -> 1/3. EB.4's error ratio rho/3 and EC.5's w_(k+1)/w_k -> 1/3 become theorems; 3^k w_k -> 2 varrho_N (1 - 3/rho) / (9 (1 - delta_N)^2). At alpha = 4 gamma/3 the sign of Y_n - Y_oo is that of -nu^3 (1 - delta_N) - varrho_N, not decided.
- EE.4 (arb, --full, per commit message): at alpha = 0.8, d* in [0.2950750, 0.2950892], e* in [0.7409667, 0.7410025]; varrho_1 in [0.0287924, 0.0288038], varrho_2 [0.239231, 0.239288], varrho_3 [0.705919, 0.706085], varrho_6 [11.6879, 11.6907], varrho_10 [446.091, 446.198]; lim 3^k w_k in [-5.1314, -5.1182] (N = 1); e* at 0.7 [0.78098, 0.78180], 0.9 [0.73737, 0.73802], 0.95 [0.75298, 0.75362].
- EE.5 (floats, OBSERVED): d* = 0.2950821098, e* = 0.7409845866 (independent H-route agrees to 1e-14); direct quadrature 0.29641757, 0.29526654, 0.29510615 at k = 8, 12, 16 approaching the limit formula.

## Why It Matters
It closes the corner-deficit remainder chain AT → AZ → DZ → EA → EB → EC → ED with a limit, not just two-sided bounds: the 3^-n coefficient converges to an explicit integral of the level-infinity scaled profile, so the observed per-level ratios rho/3 (EB.4) and 1/3 (EC.5) are now proved. The one remaining sign question sits exactly at alpha = 4 gamma/3.

## Derivation
Checked here (not the full proof): EE.2 from EE.1 and ED.1's exact eps_n = rho^n Σ_(k>=n) rho^-k (Mt_oo - Mt_k): if (3/rho)^k (Mt_(k+1) - Mt_k) -> d*, then Mt_oo - Mt_k ~ d* (rho/3)^k / (1 - rho/3) and eps_n ~ rho^n d*/(1 - rho/3) Σ_(k>=n) 3^-k = (3 d*/(2 (1 - rho/3))) (rho/3)^n, matching the repo's e* (and ED's L_alpha form with ell replaced by the limit). The exchange of limit and sum is justified by ED.2's lower bound and EC.2's upper bound (both geometric in (rho/3)^k), which the repo cites.

## Assumptions
AQ (1)–(3), BI.4, BK.1, BK.2, ED.1, ED.2 (a), DZ.1, DZ.2, EB.1, all as stated in the repository; python-flint arb correctness; the existence of the Poincaré function Phi as used (standard for analytic maps with a repelling fixed point at 0 with multiplier 5).

## New Results
Existence and integral formulas for lim (3/rho)^n eps_n and lim 3^n R_n on all of (gamma, 1); certified values at 0.8 (five N) and e* at four alpha values; the two observed ratios promoted to theorems; a closed criterion (sign of -nu^3 (1 - delta_N) - varrho_N) for the open boundary case.

## Prior Art
Poincaré functions and Tannery's theorem for scaled limits of iterated maps, and the renormalisation map on the Sierpinski gasket's resistance/spectral decimation (Kigami; Strichartz; Fukushima–Shima; Teplyaev; Derfel–Grabner–Vogl on Poincaré functions for gasket decimation); interval enclosures (Tucker 2011; arb, Johansson). No external source for these specific constants was searched in this slice.

## Novelty Analysis
Method KNOWN. The limits and constants are new to the corpus; external novelty UNRESOLVED and of modest consequence.

## Falsification Attempts
- Independent mpmath (30 digits), alpha = 0.8: rho = 1.207966106, 3/(2(1 - rho/3)) = 2.511113219; d* bracket times this factor gives [0.7409667, 0.7410024] (repo prints upper 0.7410025, outward-rounded, consistent); the float d* = 0.2950821098 gives e* = 0.7409845866 exactly as printed. 4 gamma/3 = 0.9101415926.
- Off 0.8, the d* implied by the --full e* brackets (0.7: [0.34218, 0.34253]; 0.9: [0.25908, 0.25931]; 0.95: [0.24467, 0.24488]) lies inside the default run's coarse d* brackets ([0.34146, 0.34325], [0.25862, 0.25977], [0.24426, 0.24529]). Consistent.
- Containment: every EE.4 varrho_N bracket (N = 1, 2, 3, 6, 10) lies inside DISC-0243's ED.4 every-n >= 60 bracket (checked independently; the witness also checks it). e* / L_0.8 = 133.9, matching ED's "~134x".
- Display check: the commit message says EB.1 + EE.3 reproduce EC.5's w ratios "to 1e-4"; the witness prints model 0.33647, 0.33544, 0.33476, 0.33435 vs observed 0.33637, 0.33541, 0.33475, 0.33426 (max gap 1.0e-4 at k = 14) and its own check is "< 3e-4". The commit phrasing is at the edge, not wrong; noted, not a defect.
- Scope attack: no rate of convergence (every-n bounds unchanged), varrho_N certified only at 0.8, sign at 4 gamma/3 open, no closed forms, (gamma, 1) only. The repo states each as a kept limit. No overclaim found.

## Experimental Validation
None applicable (pure mathematics). Not thrust; no flux; Stage 2 still blocked (no Psi_info).

## Mathematical Status
Theorem as stated (EE.1–EE.3), conditional on the listed inputs; EE.4 computer-assisted; EE.5 observed only.

## Patent Relevance
None. Pure mathematics on a graph; not a mechanism.

## Related Discoveries
DISC-0243 (Theorem ED; kept limit and open item answered), DISC-0242 (Theorem EC; EC.5 ratio now a theorem), DISC-0241 (Theorem EB; EB.4 ratio now a theorem), DISC-0238 (Theorem DZ; DZ.1/DZ.2 inputs), DISC-0127 (Theorem AZ; eps_n's leading coefficient now has a limit).

## Open Questions
Rate of (3/rho)^n eps_n -> e*; sign of Y_n - Y_oo at alpha = 4 gamma/3 (reduced to the sign of -nu^3 (1 - delta_N) - varrho_N); varrho_N certified off 0.8; alpha <= gamma; closed forms for d*, kappa_N.

## Next Experiments
Certify -nu^3 (1 - delta_N) - varrho_N at alpha = 4 gamma/3 (requires certified nu, delta_N, varrho_N there); certify varrho_N at 0.7, 0.9, 0.95; derive an explicit rate from the tail of the dominated-convergence step.

## Reproduction Instructions
Clone informational-flux-identity at d3104a6468849683afa9b4f7b919aae885f95c35; `pip install python-flint sympy numpy`; `python3 scripts/gasket_fractional_corner_remainder_limit.py` (~38 s; `--full` ~206 s per the repo for the tighter brackets); tests `python3 -m pytest -q tests/test_cli.py` and `python3 -m pytest -q tests/test_flux_identity.py`.

## Evidence Log
- 2026-11-15 ~7:00 AM EST: repo default witness EXIT 0 (38.3 s wall), "all EE checks passed", every printed check "ok"; tests/test_flux_identity.py EE subset 2 passed (0.15 s). The --full run was not repeated here; the --full brackets above are as printed in the commit message, and the default run's coarser brackets contain them.
- 2026-11-15 ~7:00 AM EST: mpmath arithmetic PASS; no display defect found.

## Change History
- 2026-11-15: created.
