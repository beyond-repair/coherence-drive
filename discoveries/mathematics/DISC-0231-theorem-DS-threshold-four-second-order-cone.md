# Discovery: Theorem DS, threshold n0 = 4 for the second-order cone K_(2,6)

## Discovery ID
DISC-0231

## Status
THEOREM (mathematical sense only; computer-assisted, arb-certified; method KNOWN; constants UNRESOLVED). Settles DISC-0230's kept open case n = 4.

## Date Discovered
2026-11-12 (indexed ~5:05 PM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit ec1dd6c8b2fc9189ad58e14fa5cf21b5b8dbefba (2026-11-12 4:05 PM EST).

## Original Evidence
- GASKET.md §Theorem DS (line 5361; NOT THIS disclaimer at line 5377).
- CLAIM_STATUS.md (one new row, Theorem DS).
- scripts/gasket_fractional_profile_level_threshold_four.py (new, 506 lines); registered in scripts/cli.py.
- tests/test_cli.py::test_theorem_ds_profile_level_threshold_four (default 8 cells including the two worst; DS_FULL=1 runs all 200 cells, ~2.4 h).

## Discovery
DR (DISC-0230) left n = 4 open: its certified bound D_4 <= 0.055511 gives per-level 0.3433, above the cap q = rho(L_1)/r >= 0.3170757. DS encloses
0.03604618 <= D_4 = diam Lt^4 K_(2,6) <= 0.03838589 < 4 artanh(q^4) = 0.04043213,
so tanh(D_4/4)^(1/4) lies in [0.3081036, 0.3129858], below the cap. With DQ.5 (n = 1, 2, 3 above the cap) and DR.4 (every n >= 5 below), the threshold is n0 = 4 exactly.

## Why It Matters
It closes the last open finite case in the DP/DQ/DR line: the first level at which a cone-diameter (Birkhoff) bound on K_(2,6) beats the C^1 cap is now known exactly, with a certified two-sided enclosure of D_4 (width ~6.5%) showing the margin is real but small (factor 1.0131).

## Derivation
- DS.1 (sympy): for f in K_(2,6), v = f'/f has |v| <= 2 and v' in [-6 - v^2, 6 - v^2]. Riccati comparison with U_a = sqrt6 tanh(sqrt6 t + artanh(a/sqrt6)) forward and W_b = sqrt6 tan(sqrt6 t + arctan(b/sqrt6)) backward bounds log f(z) - log f(y) <= B(a, b, d) = min over t0 of the two clipped integrals; the reversal v(t) -> -v(d - t) preserves the constraint set and gives the lower bound.
- DS.2: value-function (backward-recursion) certificate over 256 v-cells for point-jet functionals, B from arb tables (t-step 2^-15), recursion in outward-rounded doubles. Replaces DR.1's chain (loses ~1.5x at n = 4).
- DS.3: DR.2's 200 cells x 4 types = 3200 certificates, reference delta_(21/10), D_4 <= 2 max log(t1 t2).
- DS.4: explicit piecewise f, g in K (64 and 63 breakpoints) give the arb lower bound.

## Assumptions
CF.1 (Birkhoff), DQ.1 invariance, DQ.5, DR.2 cell lemma, DR.4, cap value from CI.1/CG.3 (all from earlier records, not re-derived here); correctness of the repository's outward rounding; scalar ODE comparison (textbook).

## New Results
n0 = 4 exactly on K_(2,6); per-level rate at n = 4 in [0.3081, 0.3130]; no cone-diameter bound at n = 4 on this cone can beat 0.3081 per level.

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995; Lemmens–Nussbaum 2012 (Hilbert-metric cone contraction); Riccati comparison for log-derivatives is classical. Rigorous interval certification of such bounds is a known technique. Constants are specific to this operator; their novelty is UNRESOLVED.

## Novelty Analysis
Method KNOWN. The certified constants and the exact threshold are new to the corpus; no external first is claimed or supported.

## Falsification Attempts
- Repo witness (default 8 cells incl. worst cell 199 '1+'): `python3 scripts/gasket_fractional_profile_level_threshold_four.py` EXIT 0, 94.3 s; all checks ok (128 certificates, 0 t-bumps; D_4 <= 0.03838589; lower witness >= 0.03604618). DS_FULL=1 (all 200 cells) started on the archive box 2026-11-12 ~5:00 PM EST, result pending; the full-cover claim is therefore not yet independently reproduced.
- Independent check (archive indep_ds.py, mpmath): 4 artanh(0.3170757^4) = 0.0404321301; tanh(0.03838589/4)^(1/4) = 0.3129857558 (matches); tanh(0.03604618/4)^(1/4) = 0.3081036725. The commit message and script print the lower per-level as 0.3081037, slightly above the value implied by the printed D_4 lower bound (presentation rounding; GASKET's heading and the test use the conservative 0.3081036). DS.1 closed forms verified (ODE residual < 1e-20). 30 random paths with v' sampled in the allowed band and |v| <= 2: max (log f(z) - log f(y) - B) = -0.0066 < 0, no violation of the comparison bound. PASS.
- Consistency: 0.03604618 <= D_4 <= 0.03838589 < DR's 0.055511; per-level interval above DQ.4's limit 0.1725 and below DQ.5's n = 3 floor 0.3221.

## Experimental Validation
None applicable (pure mathematics). Not thrust; Stage 2 still blocked (no Psi_info).

## Mathematical Status
Theorem (computer-assisted) as stated in the repository; full 200-cell cover reproduced only by the repository author so far.

## Patent Relevance
None.

## Related Discoveries
DISC-0230 (DR, open case closed here), DISC-0229 (DQ), DISC-0228 (DP cap).

## Open Questions
Tighten the 6.5% enclosure of D_4; level-sum bound of CF.3/DN.3/DO.3 form on K_(2,6) still not computed; finite-n approach to |l_2|/r = 0.1725.

## Next Experiments
Read the DS_FULL=1 log (/workspace/ds_full_witness.log on the archive box) and record the 200-cell result here.

## Reproduction Instructions
Clone informational-flux-identity at ec1dd6c8b2fc; `pip install python-flint sympy`; `python3 scripts/gasket_fractional_profile_level_threshold_four.py` (~1.5 min) or `DS_FULL=1 ...` (~2.4 h); or `python3 -m pytest -q tests/test_cli.py -k test_theorem_ds`.

## Evidence Log
- 2026-11-12 ~5:00 PM EST: repo witness EXIT 0 (94.3 s, 8 cells); independent arithmetic/comparison check PASS; DS_FULL=1 launched.

## Change History
- 2026-11-12: created.

## Dated note (2026-11-12 ~6:05 PM EST)
- DS_FULL=1 (all 200 cells) finished on the archive box: 3200 certificates, 0 t-bumps, worst cell (199, '1+', 2.49655); D_4 <= 0.03838589, per level <= 0.3129858 < 0.3170757; n0 = 4 exactly; "all Theorem DS checks passed"; elapsed 1808.5 s (~30 min on 8 cores). The full-cover claim is now independently reproduced. Mathematical status unchanged (THEOREM, method KNOWN, constants UNRESOLVED).
- Runtime nit: IFI 84cb64b224d9 replaces CLAIM_STATUS's "~RUNTIME min" placeholder with "~2.4 h"; the archive run took about 30 min. Documentation only, no claim affected.
- Downstream: DS.3's theta_4 is used by Theorem DT, see DISC-0232.
