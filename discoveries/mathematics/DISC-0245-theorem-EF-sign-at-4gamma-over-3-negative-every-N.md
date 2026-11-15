# Discovery: Theorem EF, the sign of the second correction at alpha = 4 gamma/3 is negative for every N (S_N < 0), with nu_alpha written as a ratio of integrals of the alpha-free level-infinity profile

## Discovery ID
DISC-0245

## Status
THEOREM (mathematical sense only; EF.2 is an exact identity proved in the repository, EF.1 is DERIVED there from AQ (1)–(4), BH.2, BI.4, BL, AZ (1), DZ.1, ED.1 and EE.1–EE.3 as stated; EF.3–EF.4 are arb-certified (128 bits, monotone cell bounds plus explicit head and tail) at the listed alpha values only; EF.5 is floats, OBSERVED). Method KNOWN (dominated / monotone convergence, interval arithmetic). Novelty of the specific constants UNRESOLVED. Answers DISC-0244's open item "sign of Y_n - Y_oo at alpha = 4 gamma/3" (and the same item carried by DISC-0243) and DISC-0238's open item "a certified nu_alpha at other alpha" (dated notes on DISC-0244 and DISC-0238). No archive status change otherwise.

## Date Discovered
2026-11-15 (indexed ~8:05 AM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 9ab32c906761fda1228b6f300d63774fbe920767 (2026-11-15 7:25 AM EST); parent d3104a646884 (Theorem EE, DISC-0244).

## Original Evidence
- GASKET.md §Theorem EF (header line 6083; kept limits line 6126; what stays open line 6128; NOT THIS line 6130), +70/-8 lines overall; EE.3 (iii), EE's kept limit and open item (line 6070), ED's kept limit and open item, and DZ's open item "a certified nu_alpha at other alpha" annotated in place with the original wording kept.
- CLAIM_STATUS.md (+1/-1, new row); README.md (+2/-1).
- scripts/gasket_fractional_corner_critical_sign.py (new, 375 lines); registered in scripts/cli.py; tests/test_cli.py (+22); tests/test_flux_identity.py (+27, numpy-only CI test).

## Discovery
Setting as in Theorems AZ, DZ, EA–EE: gamma = log3/log5, rho = 5^alpha/3, so alpha = 4 gamma/3 = 4 log3/(3 log5) = 0.9101415926 is exactly the point where rho^3 = 3 (rho = 3^(1/3)), the boundary at which DISC-0243 showed the J-term expansion breaks.
- EF.1 (DERIVED, every alpha in (gamma,1), N >= 1): by EE.1's scaling and dominated convergence, D'_oo = ∫ x^-a G and (1 - delta_N) D'_oo = ∫ x^-a G eta_N(Phi(5^-N x)) with G, Phi, eta_N alpha-free; by monotone convergence nu = C'/D'_oo = -rho Mt_oo / ((rho - 1) D'_oo), Mt_oo = ∫ t^-a r_oo (omega^0/(1 - b r_oo) - 1). So every ingredient can be enclosed at the irrational alpha = 4 gamma/3 as a ball.
- EF.2 (THEOREM, exact): S_N = -nu^3 (1 - delta_N) - varrho_N = (1 - delta_N)(|nu|^3 - e*/D'_oo) - 1.5 kappa_N / D'_oo. Since kappa_N > 0, |nu|^3 < e*/D'_oo gives S_N < 0 for every N.
- EF.3 (arb, --full, per commit message) at alpha = 4 gamma/3: D'_oo in [6.005548, 6.005766], Mt_oo [0.7302557, 0.7305328], nu [-0.396698, -0.396533], e* [0.7396903, 0.7399065], |nu|^3 [0.06235, 0.06243] < e*/D'_oo [0.12316, 0.12320], hence S_N < 0 for every N >= 1; directly S_1 [-0.0233127, -0.0232863], S_2 [-0.174681, -0.174497], S_3 [-0.454529, -0.454077], S_6 [-4.69362, -4.68928], S_10 [-89.0757, -88.9943]. With EE.3 (iii): rho^n (Y_n - Y_oo) -> S_N < 0, X_n = C_delta + Y_oo rho^-n + S_N rho^-2n + o(rho^-2n), and Y_n < Y_oo for all large n (from above on (gamma, 4 gamma/3), from below on [4 gamma/3, 1)).
- EF.4 (arb consistency): at 0.8 the EF.1 integrals overlap AZ (3)'s A, C, nu, EA.4's C_delta(0.8, N) and EE.4's varrho_N; first certified nu off 0.8: nu_0.7 [-0.962092, -0.961514], nu_0.9 [-0.432534, -0.432350], nu_0.95 [-0.240608, -0.240516].
- EF.5 (floats, OBSERVED): at 0.8 nu = -0.7274453809, A = 2.3964097029 (AZ (3): -0.7274453844, 2.3964097040); at 4 gamma/3 nu = -0.39661562, S_1 = -0.0232995.

## Why It Matters
It closes the last open sign in the corner-deficit chain AT → AZ → DZ → EA → EB → EC → ED → EE: the second correction to the renormalised corner deficit has a definite sign at the critical exponent 4 gamma/3 for every N, and nu_alpha is now a certified quantity at five exponents instead of one.

## Derivation
Checked here: EF.2 is pure algebra from EE.3's varrho_N = [(1 - delta_N) e* + 1.5 kappa_N]/D'_oo and nu < 0 (DZ: C_alpha < 0), since -nu^3 = |nu|^3; the sign conclusion needs only 1 - delta_N > 0, kappa_N > 0 (both certified by the witness) and |nu|^3 < e*/D'_oo. EF.1's nu formula is EF's restatement of AZ/DZ's C/A ratio as integrals; the witness checks it against AZ (3) at 0.8.

## Assumptions
AQ (1)–(4), BH.2, BI.4, BL, AZ (1), DZ.1, ED.1, EE.1–EE.3, all as stated in the repository; python-flint arb correctness; exchange of limits justified as in EE.1.

## New Results
Sign of S_N at alpha = 4 gamma/3 is negative for every N >= 1 (a margin of about 2x: |nu|^3 ≈ 0.0624 vs e*/D'_oo ≈ 0.1232); certified nu at 0.7, 0.9, 0.95, 4 gamma/3; three-term asymptotic of X_n at the critical exponent.

## Prior Art
Same as DISC-0244: Poincaré functions and scaled limits for gasket decimation (Kigami; Strichartz; Fukushima–Shima; Teplyaev; Derfel–Grabner–Vogl); interval enclosures (Tucker 2011; arb, Johansson). No external source for these specific constants was searched in this slice.

## Novelty Analysis
Method KNOWN. Constants and the critical-point sign are new to the corpus; external novelty UNRESOLVED and of modest consequence.

## Falsification Attempts
- Independent mpmath (30 digits): alpha = 4 log3/(3 log5) = 0.910141592647980; rho^3 = 3.0 exactly to working precision.
- Interval quotient of the quoted brackets: e*/D'_oo in [0.1231634, 0.1232038]; |nu|^3 from the nu bracket in [0.0623502, 0.0624281]; disjoint by a factor ~1.97, so the EF.2 criterion holds with large margin. The repo prints the quotient upper end as 0.12320; the naive quotient of the quoted brackets is 0.1232038, but the witness computes the quotient directly in arb (correlated), so this is not established as a rounding defect, and it cannot affect the sign (the comparison uses the lower end 0.12316 > 0.06243).
- S_1 from its parts: -nu^3 (1 - delta_1) - varrho_1 with the quoted brackets gives [-0.0233130, -0.0232859], which contains the repo's direct bracket [-0.0233127, -0.0232863]. Consistent.
- nu from EF.1's formula with the quoted Mt_oo and D'_oo brackets (rho = 3^(1/3)): [-0.3966981, -0.3965332], reproducing the repo's nu bracket [-0.396698, -0.396533].
- Floats: -rho Mt_oo/((rho - 1) D'_oo) with the printed floats Mt_oo = 0.73039423, D'_oo = 6.00565694 gives -0.3966156179, matching the printed nu = -0.39661562; e*/D'_oo float = 0.1231836, inside the bracket.
- Plausibility: certified nu at 0.7, 0.8, 0.9, 4 gamma/3, 0.95 = -0.962, -0.727, -0.432, -0.397, -0.241, monotone increasing toward 0 as alpha -> 1 (not claimed monotone by the repo; listed as open).
- Scope attack: no explicit n_0 (no rate), sign decided at the single point 4 gamma/3, varrho_N and 1 - delta_N certified at 4 gamma/3 and 0.8 only, Mt_oo bracket first-order, no closed forms, (gamma, 1) only. All stated as kept limits; KEPT FAILURE: none. No overclaim found.

## Experimental Validation
None applicable (pure mathematics). Not thrust; no flux; Stage 2 still blocked (no Psi_info).

## Mathematical Status
Theorem as stated (EF.2 exact; conclusion conditional on the listed inputs); EF.3–EF.4 computer-assisted; EF.5 observed only.

## Patent Relevance
None. Pure mathematics on a graph; not a mechanism.

## Related Discoveries
DISC-0244 (Theorem EE; open sign answered), DISC-0243 (Theorem ED; 4 gamma/3 as sharp threshold, its open sign item answered), DISC-0238 (Theorem DZ; certified nu at other alpha), DISC-0127 (Theorem AZ; nu_0.8, A, C reproduced).

## Open Questions
A rate for (3/rho)^n eps_n -> e* and 3^n R_n -> varrho_N (explicit n_0); nu_alpha as a certified function of alpha (monotonicity, closed form); alpha <= gamma.

## Next Experiments
Certify nu_alpha on a grid with a monotonicity proof; derive an explicit rate from the dominated-convergence tail to get an explicit n_0 at 4 gamma/3.

## Reproduction Instructions
Clone informational-flux-identity at 9ab32c906761fda1228b6f300d63774fbe920767; `pip install python-flint sympy numpy`; `python3 scripts/gasket_fractional_corner_critical_sign.py` (~28 s; `--full` ~296 s per the repo for the tighter brackets); tests `python3 -m pytest -q tests/test_flux_identity.py`.

## Evidence Log
- 2026-11-15 ~8:00 AM EST: repo default witness EXIT 0 (28.0 s wall), "all EF checks passed", every printed check "ok" (default-run brackets are coarser, e.g. e*/D'_oo - |nu|^3 in [0.05992, 0.06167] > 0); tests/test_flux_identity.py EF subset 1 passed (0.19 s). The --full run was not repeated here; the --full brackets above are as printed in the commit message.
- 2026-11-15 ~8:00 AM EST: mpmath arithmetic PASS; no display defect established.

## Change History
- 2026-11-15: created.
- 2026-11-15 (dated note): Theorem EG (IFI b819534ca2ef, DISC-0246) answers the 'no explicit n_0' limit on the lower side: at alpha = 4 gamma/3, Y_n < Y_oo for every N >= 1 and every n >= N (L(2) >= 0.483482 > |nu|^3 D'_oo <= 0.374929; n = 1 by kappa_lo(1,1) >= 0.017260). An every-n upper bound stays open. No status change.
- 2026-11-15 (dated note): Theorem EH (IFI 4e198bae1a55, DISC-0247) extends EF's single point to all of [4 gamma/3, 1): nu_alpha and D'_oo are enclosed on 36 alpha-cells (arb, 128 bits), |nu| in [0.38461, 0.40022] on [4 gamma/3, 0.9125] and <= 0.01359 on [0.9975, 1). EF's S_N < 0 itself stays at the single point alpha = 4 gamma/3 (where rho^3 = 3). No status change.
