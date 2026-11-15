# Discovery: Theorem DR, effective threshold for the second-order cone K_(2,6)

## Discovery ID
DISC-0230

## Status
THEOREM (mathematical sense only; certified finite-n bounds; method KNOWN; constants UNRESOLVED) with a kept open case n = 4.

## Date Discovered
2026-11-12 (indexed ~12:10 PM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit e8d5c2122c2a (2026-11-12 11:58 AM EST).

## Original Evidence
- GASKET.md §Theorem DR (line 5320; NOT THIS disclaimer at line 5352).
- CLAIM_STATUS.md line 126 (PROVED DR.1–DR.4, arb-certified; KEPT OPEN n = 4; float LP chains are only proposals, their arb replay is what is claimed).
- scripts/gasket_fractional_profile_level_effective_threshold.py (new, 399 lines); registered in scripts/cli.py.
- tests/test_cli.py::test_theorem_dr_profile_level_effective_threshold (default n = 3, 5, 6).

## Discovery
DQ.5 (DISC-0229) left the threshold n0 (after which the per-level Birkhoff rate on K_(2,6) drops below the cap rho(L_1)/r > 0.3170757) non-effective. Theorem DR certifies Hilbert diameters D_n = diam Lt^n K_(2,6):
D_3 <= 0.25513, D_4 <= 0.055511, D_5 <= 0.0098240, D_6 <= 0.0018378, D_7 <= 0.00041195, D_8 <= 0.00017543.
Per-level tanh(D_n/4)^(1/n): 0.39937, 0.34322 (n = 3, 4, above the cap) and 0.30064, 0.27779, 0.26940, 0.28527 (n = 5..8, below it). By sub-multiplicativity of the Birkhoff contraction coefficient (CF.1 composition) every n >= 5 has per-level <= 0.3135158 < 0.3170757, and tanh(D_n/4) <= 2.33914 * 0.2852680^n. With DQ.5, n0 is 4 or 5.

## Why It Matters
It converts DQ.4's limit statement into an explicit, checkable contraction bound on the second-order cone, the first certified finite-n rate below the C^1 cap in this line (DP, DQ). It does not reach the spectral limit 0.1725.

## Derivation
DR.1 chain lemma (sympy): m f(y) + mu f'(y) = m f(z) + (mu - m d) f'(z) + int_y^z (m(x-y) - mu) f'', with |f''| <= 6f and f(x) <= f(z) e^(2|z-x|), so a point-jet functional is >= 0 on K_(2,6) when a Taylor/collapse chain ends with m - 2|mu| >= 0. DR.2 cell lemma (affine in tau after rescaling, arb jets to order 4), reference functional delta_(9/5), D_n <= 2 max log(t1 t2). DR.3: float LP chains (200 cells, 3200 chains per n) replayed in arb. DR.4: composition.

## Assumptions
DQ.1 invariance of K_(2,6) and the cap value from DP/DQ (not recomputed here); correctness of the arb replay in the repository script; CF.1 composition (standard Birkhoff sub-multiplicativity).

## New Results
n0 in {4, 5}; explicit exponential envelope for tanh(D_n/4) on K_(2,6).

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995 (cone contraction for transfer operators); Lemmens–Nussbaum 2012. Rigorous interval/LP certification of cone contraction is a known technique; the constants are specific to this gasket operator and their novelty is UNRESOLVED.

## Novelty Analysis
Method KNOWN. The specific certified constants are new to the corpus; no external claim of a first is supported.

## Falsification Attempts
- Repo witness (default n = 3, 5, 6): `python3 -m pytest -q tests/test_cli.py -k test_theorem_dr` EXIT 0, 1 passed in 132.5 s (python 3.13, python-flint, sympy, scipy 1.18.1). DR_FULL=1 (n = 4, 7, 8; ~66 min) not rerun.
- Independent DR.4 check (/workspace/ifi-dr-indep/indep_dr4.py, mpmath 40 digits): recomputed per-level values from the printed D_n match the commit to 5 digits; dynamic-programming over block decompositions {3..8} for n = 5..400 gives a worst per-level 0.3135171 at n = 9 (block 3 + block 6) and envelope 2.33924. These are slightly above the stated 0.3135158 and 2.33914 only because the printed D_n are rounded upward; the margin to the cap (> 0.0035) is unaffected. Every n >= 5 decomposes. PASS.
- Consistency: n = 3 per-level 0.39937 > 0.3221 lower bound from DQ.5, consistent.

## Experimental Validation
None applicable (pure mathematics). Not thrust; Stage 2 still blocked.

## Mathematical Status
Theorem (computer-assisted, arb-certified) for n = 3, 5..8 and DR.4; n = 4 open.

## Patent Relevance
None.

## Related Discoveries
DISC-0229 (DQ), DISC-0228 (DP cap), DISC-0225 (DM diameters).

## Open Questions
Is D_4 per-level below the cap (floats straddle it)? Can the rate approach |l_2|/r = 0.1725 at finite n?

## Next Experiments
Rerun DR_FULL=1 to reproduce n = 4, 7, 8; refine cells at n = 4.

## Reproduction Instructions
Clone informational-flux-identity at e8d5c2122c2a; `pip install python-flint sympy scipy`; `python3 -m pytest -q tests/test_cli.py -k test_theorem_dr`.

## Evidence Log
- 2026-11-12 ~12:05 PM EST: repo witness EXIT 0 (132.5 s); independent DR.4 composition check PASS.

## Change History
- 2026-11-12: created.

## Dated note (2026-11-12 ~5:05 PM EST)
The kept open case n = 4 is settled by Theorem DS (informational-flux-identity ec1dd6c8b2fc), see DISC-0231: 0.03604618 <= D_4 <= 0.03838589, per level <= 0.3129858 < 0.3170757, so n0 = 4 exactly. The text above is preserved as first recorded.
