# Discovery: Theorem EZ, EY.3's tail inequality proved for every n >= 11, with the exact threshold n = 11 for that tail formula

## Discovery ID
DISC-0265

## Status
THEOREM (mathematical sense only) for EZ.0–EZ.2; EZ.3 is an Arb certificate (L(n) < 0 for 11 <= n <= 600, L(10) > 0) plus a KEPT FAILURE at n = 10. Method KNOWN: elementary calculus on an explicit closed form (monotonicity in a and n, then a crude analytic bound for J >= 4). This closes only the tail part of EY.3 (DISC-0264); EY.2's float constants and the constant W(alpha−1)/6 remain uncertified, so EY.3 as a whole is still not Arb-certified. Whether the constants are new is UNRESOLVED (no literature search; the method is textbook).

## Date Discovered
2026-11-23. The commit is from 1:07 AM EST and was indexed at about 2:00 AM EST.

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 3a6c5e27648d6a2dc69b74ea63b9dfd6651f5bf9 (2026-11-23T06:07:08Z = 2026-11-23 1:07:08 AM EST). Parent: 9adc08ff3a1d (Theorem EY, DISC-0264).

## Original Evidence
- GASKET.md §Theorem EZ (+13 lines).
- scripts/gasket_fractional_corner_h_alpha_tail.py (new, 118 lines; python-flint arb at 200 bits, exit 1 on failure).
- CLAIM_STATUS.md (+1 row); tests/test_flux_identity.py (+17 lines).

## Discovery
In 9adc08ff3a1d, EY.3's tail inequality T(n,a) <= (2/5)^n was checked on a float grid for n < 40 only (the repository's own words in 3a6c5e2: "EY's checked n<40 on a grid"). EZ proves it for every n >= 11 and every real a in [−1, 9/10] (complex alpha by |t^-alpha| = t^-Re alpha), and shows n = 11 is exactly where this tail formula starts to work.

With J = floor(n/3), s0 = (5/2)^n / 5^(J+1), T(n,a) = (1/3)·5^((J+1)(1−a))·s0^(1−a−2^J)/(2^J+a−1):
- EZ.0: T(n,a) is exactly the tail integral ∫_{(5/2)^n}^∞ t^-a (1/3)(t/5^(J+1))^(-2^J) dt.
- EZ.1: d ln T/da = −(J+1) ln5 − ln s0 − 1/(2^J+a−1) < 0 for n >= 11, so a = −1 is worst.
- EZ.2: L(n) = ln(T(n,−1)(5/2)^n) = (c+2)B − (c−1)A − ln3 − ln c, c = 2^J−2, A = n ln(5/2), B = (J+1) ln5; dL/dn = −(c−1) ln(5/2) < 0 at fixed J, so the worst n is 3J (or 11 when J = 3); for J >= 4, L <= −J(0.7(2^J−2) − 5.97) + 3.22 < 0.
- EZ.3: Arb: L(11) = −1.78434881…, L(n) < 0 for 11 <= n <= 600; L(10) = +2.79710484… > 0 (KEPT FAILURE).

## Why It Matters
It removes the only purely finite-grid step from EY.3's tail, so DISC-0264's rate rests on EY.1/EY.2 numerics and the repository's earlier theorems, not on an unproved "for all n" extrapolation. It also corrects DISC-0264's write-up, which labelled EY.1–EY.3 THEOREM without noting that the tail was grid-checked for n < 40 only (our own check covered n = 11..60).

## Derivation
Re-derived by hand this run:
- EZ.0: substitute T_n = s0·5^(J+1); 5^((J+1)2^J)·(s0·5^(J+1))^(1−a−2^J) = 5^((J+1)(1−a))·s0^(1−a−2^J). Correct.
- EZ.1: differentiate ln T term by term; each of the three terms is negative when s0 > 1 and 2^J + a − 1 > 0. Correct.
- EZ.2: at n = 3J, L = c(B − A) + 2B + A − ln3 − ln c. B − 3J ln2.5 <= 1.6095 − 1.1391 J <= −0.7J needs J >= 3.67, so J >= 4 is fine. 2B + A <= 3.219(J+1) + 2.749J = 5.968J + 3.219 (3 ln2.5 = 2.74887 < 2.749). With c >= 14, 0.7c − 5.97 >= 3.83 and 3.83J >= 15.3 > 3.22. Correct. s0 > 1 holds for n >= 3J with J >= 2 since 3J ln2.5 − (J+1) ln5 = 1.139J − 1.609 > 0.
- n in {9, 10} have J = 3 but are below 11, so J = 3 contributes only n = 11. Correct.

## Assumptions
- EY.3's tail reduction as stated in the repository: f_n + f <= 1/(3(5 + psi_(n−1)(t/5))) and psi_(n−1)(t/5) >= (t/5^(J+1))^(2^J) (EX.1's chain). Not re-derived here beyond what DISC-0264 records.
- python-flint Arb correctness for EZ.3.

## New Results
- The tail term of EY.3 is now proved for all n >= 11 (THEOREM).
- n = 11 is sharp for this tail formula (not for the true gap).
- DISC-0264 status note: EY.3 = proved tail (EZ) + EY.2 with float-checked constants; EY as a whole stays THEOREM in the mathematical sense but its numeric constants are not certified.

## Prior Art
Elementary monotonicity and exponential-tail bounds; textbook. No external search.

## Novelty Analysis
Method KNOWN. The statement is specific to this repository's construction; novelty UNRESOLVED.

## Falsification Attempts
Independent mpmath check (/workspace/corpus-discovery/ez_check.py, 40 digits, own implementation):
- EZ.0: numerical quadrature of the tail integral matches T(n,a) at (11,−1), (12,0.5), (14,0.9) to <= 2e-15 relative.
- EZ.1: T(n,a) <= T(n,−1) on a 20-point a-grid for every n = 11..300. Held.
- EZ.2/EZ.3: max L(n) over n = 11..300 is L(11) = −1.784348813; L(10) = +2.797104846. Both match the repository to all printed digits.
Nothing broke. Script and CI not rerun from the repository.

## Experimental Validation
Not applicable (pure mathematics). Arb certificate in-repo; independent mpmath reproduction above.

## Mathematical Status
THEOREM (EZ.0–EZ.2), certified computation (EZ.3), KEPT FAILURE at n = 10.

## Patent Relevance
None.

## Related Discoveries
- DISC-0264 (Theorem EY): EZ proves EY.3's tail for all n >= 11. Label: mathematical.
- DISC-0263 (Theorem EX): EX.1's psi lower-bound chain is the assumption used. Label: mathematical.

## Open Questions
Certify EY.2's constants (0.0127, 0.037, 0.127, 0.106) and W(Re alpha − 1) in Arb; prove the 3^-n rate (EY.4); extend below n = 11 with a different tail split.

## Next Experiments
Arb-certify EY.2 on [0, (5/2)^n] for n <= some N and prove the n > N case analytically, mirroring EZ.

## Reproduction Instructions
In informational-flux-identity @ 3a6c5e27648d: `python3 scripts/gasket_fractional_corner_h_alpha_tail.py` (needs python-flint). Independent: ez_check.py (local to the research box, not committed).

## Evidence Log
- 2026-11-23 ~2:00 AM EST: ez_check.py results above.

## Change History
- 2026-11-23 ~2:00 AM EST: created (THEOREM EZ.0–EZ.2, Arb EZ.3, KEPT FAILURE n = 10; method KNOWN, constants UNRESOLVED).
