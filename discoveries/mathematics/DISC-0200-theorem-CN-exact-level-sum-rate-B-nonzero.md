# Discovery: Theorem CN — B ≠ 0 in CG.4, so |λ_2|/r is the exact rate of the level sums, with alternating signs and an explicit constant

## Discovery ID
DISC-0200

## Status
THEOREM (mathematical sense only; proof and arb/acb/sympy witness are in the source repository). Method: KNOWN (Riesz spectral projections and resolvent contour bounds; Krawczyk/Brouwer existence for complex roots; Noshiro–Warschawski univalence; annihilator/Prony-type extraction of exponential-sum coefficients from certified data). The specific constants (a_2, B, C = 14.5952) for this operator: UNRESOLVED as to novelty; no claim of a mathematical first. Not a flux, not thrust.

## Date Discovered
2026-10-30 (indexed ~11:00 EDT; source commit 2026-10-30 10:03:59 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 077b6fc50dc0239ad57c87dd24633558a27d75bc

## Original Evidence
- GASKET.md, new section "Theorem CN" (+60 lines) and the CA–CG "What stays open" item on B ≠ 0 updated in place to point to CN.
- CLAIM_STATUS.md, new row after Theorem CM.
- scripts/gasket_fractional_profile_level_coefficient.py (new, 457 lines); scripts/cli.py; tests/test_cli.py (+28); README.md.

## Discovery
- CN.1: on V = [−26/5, −4/5] × [−3/10, 3/10], Re ψ' ≥ 0.5436, so ψ is injective there; complex Krawczyk boxes on 1024 arcs put ψ^{-1}(tΦ(∂D)) in V, so F_0 = L̃⁴G continues holomorphically near the closed disk, ‖F_0‖_{H²} ≤ 0.016909.
- CN.2: four certified resolvent circles give s_{k+4} = a_1 r^k + a_2 λ_2^k + a_3 λ_3^k + e_k with |e_k| ≤ 2.889·10⁴·10^{−3k}.
- CN.3: annihilators on CC's certified s_4..s_13 give a_1 = 0.0057125687…, a_2 = −4.158·10⁻⁵ ± 4.4·10⁻⁹ ≠ 0, |a_3| ≤ 1.125·10⁻⁴, B = −8.211 ± 5·10⁻⁴.
- CN.4: for every n ≥ 4, sign(s_{n+1}/s_n − r) = (−1)^n and |log(s_{n+1}/(r s_n))| ≤ 14.5952 (|λ_2|/r)^n; for n ≥ 13 also ≥ 9.626 (|λ_2|/r)^n. So |λ_2|/r = 0.172547602129… is the exact rate, not just an upper bound.

## Why It Matters
Closes the open item "whether B ≠ 0 in CG.4" carried by DISC-0191 and every later record in this chain (DISC-0194 through DISC-0199). It upgrades CE.5's observed alternation (through n = 12) to all levels, and makes CF.3's non-explicit Birkhoff constant C_G unnecessary for the level sums.

## Derivation
GASKET.md CN.1–CN.4 proofs. Checked by hand here:
- CN.1: the mean-value integral with positive real part gives injectivity on convex V°; the Riemann-sphere complement argument for tΦ(D̄) ⊂ Ω is standard and correct given the boundary inclusion.
- CN.2: rank-one Riesz projections for the simple eigenvalues r, λ_2, λ_3 plus the inner contour |z| = 10⁻³; point evaluation bound (1 − u_0²)^{−1/2} on H²(D) is the reproducing-kernel norm. Sound.
- CN.3: the (r, λ_3)-annihilator kills the a_1, a_3 terms up to enclosure widths, so |Q_7| = 1.293·10⁻¹⁴ against a 2.21·10⁻¹⁹ bound on everything else forces a_2 ≠ 0. This is the decisive step and the margin is about 5·10⁴.
- CN.4: B = (a_2/a_1)(r/λ_2)⁴ by the reindexing; monotone decrease of each term of ρ_n/q^n justifies extending the n = 13 bound to all n ≥ 13. Sound.

## Assumptions
CE.1–CE.4, CG.3 eigenvalue enclosures and count, CC.4 certified level sums (re-run by the script), BJ.6/CB.5 majorants (all imported). Textbook facts only (Noshiro–Warschawski, Krawczyk/Brouwer, open mapping, maximum principle, Riesz projections).

## New Results
Exact second-order asymptotics of the level sums: log(s_{n+1}/(r s_n)) / (λ_2/r)^n → B(λ_2/r − 1) = 9.628…, with an explicit all-n constant.

## Prior Art
- Riesz projections / spectral asymptotics of transfer operators: Ruelle; Baladi, "Positive Transfer Operators and Decay of Correlations" (2000).
- Krawczyk operator: R. Krawczyk (1969); interval Newton/Krawczyk for complex roots is standard in validated numerics (Moore, Neumaier).
- Noshiro–Warschawski theorem (1934/1935).
- Exponential-sum coefficient extraction by annihilating polynomials (Prony 1795).
The mechanism is standard; I found no prior statement about this specific operator, which is expected for a repository-specific object.

## Novelty Analysis
Method KNOWN. Specific: the certified nonvanishing of a_2 and the explicit constant for this gasket level-sum operator. Not a first in any general sense.

## Falsification Attempts
- Repo witness: `python3 scripts/gasket_fractional_profile_level_coefficient.py` EXIT 0 in 134.7 s (wall 2m15s) at 077b6fc, 26 `ok` checks; a_r best k = 7 enclosure 0.0057125687 ± 1.09e-11; a_λ2 enclosure −4.158e-5 ± 4.32e-9 with |Q_7| = 1.293e-14 vs other-term bound 2.21e-19; a_3 enclosure ± 1.13e-4 (contains 0, as the repo says).
- Independent script `mathematics/scripts/indep_theorem_CN.py` (mpmath floats, no repo imports; uses only CC's printed 12-significant-digit level sums s_4..s_14 and r = 0.4237312869626079 from DISC-0190/CE), 8/8 PASS: alternation of s_{n+1}/s_n − r for n = 4..13; max |log|/q^n = 14.5951 at n = 4 (repo 14.5952); normalized logs 9.631, 9.628, 9.6275, 9.6268 at n = 9..12 converging to the repo's 9.628; least-squares a_1 = 0.005712568711, a_2 = −4.1591·10⁻⁵, B = −8.2136 (repo −8.211 ± 5·10⁻⁴; my fit ignores the λ_3 term and uses 12-digit data, so agreement to 0.03% is what to expect); implied λ_3 contribution at n = 4 ≈ −2.38·10⁻⁵, inside |a_3| ≤ 1.125·10⁻⁴.
- Caveat on my own check: at n = 13 my value is 9.616, slightly under the repo's lower bound 9.626. This is precision noise, not a contradiction: q^13 ≈ 1.2·10⁻¹⁰ and the 12-digit printed sums carry relative errors of a few 10⁻¹², i.e. about ±0.5 in the normalized value. The repo's certified sums carry absolute error < 10⁻²⁸.
- Logic attacked: whether a_2 = 0 could hide behind enclosure width (no, margin ~5·10⁴); whether a branch error in ψ^{-1} could fake F_0 (the repo checks 3σ_{−3}F_0(x_0) = s_4 to 10⁻¹⁸ and injectivity excludes a second preimage). No break found.

## Experimental Validation
Computational only. None needed for the theorem.

## Mathematical Status
Theorem (computer-assisted constants; CC/CE/CG enclosures imported).

## Patent Relevance
None. Pure spectral asymptotics; repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0191 → DISC-0200 (mathematical): CG.4's open B ≠ 0 question answered. DISC-0190 → DISC-0200: CF.3's C_G no longer needed for the level sums. Parallel to the DISC-0194 → … → DISC-0199 C^k-spectrum chain, which this does not change.

## Open Questions
Whether a_3 ≠ 0; explicit C_G in CF.3; eigenvalues on |z| = ρ(L_k); a rate for inf R_n → ρ(L_1); closed forms of r, λ_2, B, ρ(L_k).

## Next Experiments
Decide a_3 ≠ 0 by extending CC's certified sums past level 14 (the (r, λ_2)-annihilator is currently within a factor ~4 of its remainder bound); certify λ_4 to push the error term e_k.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at 077b6fc; `pip install python-flint mpmath sympy numpy`; run `python3 scripts/gasket_fractional_profile_level_coefficient.py` (about 2–3 min, exits nonzero on any failed check). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_CN.py` in this repo.

## Evidence Log
- 2026-10-30 ~11:00 EDT: repo witness EXIT 0 (134.7 s, 26 checks ok); independent check 8/8 PASS.

## Change History
- 2026-10-30: created from IFI 077b6fc50dc0.
- 2026-10-30: note added (status unchanged); open item a_3 ≠ 0 answered by DISC-0201.

## Note (2026-10-30, appended; text above unchanged)
The open item "whether a_3 ≠ 0" is answered by IFI Theorem CO at 888d3bee13fa78755b539ba0870959b5153a360b: a_3 = −2.36116·10⁻⁵ ± 4.6·10⁻⁸ ≠ 0 (Riesz projection, not level sums), and B is sharpened to −8.21069 ± 10⁻⁵, inside this record's −8.211 ± 5·10⁻⁴. The independent fit here (implied λ_3 contribution ≈ −2.38·10⁻⁵ at n = 4) agrees in sign and size. See DISC-0201.

## Note (2026-10-30, appended; text above unchanged)
IFI Theorem CS at 9cb3b84d6b2863320e2903993b9a31927af2d6ce makes CN.4's constants sharp: D_n = log(s_{n+1}/(rs_n))/q_2ⁿ strictly decreases for every n ≥ 4 from D_4 = 14.59509785 ± 5.9·10⁻¹⁰ (CN.4: 14.60) to L = B(q_2 − 1) = 9.6274 ± 3.6·10⁻⁵, so the lower bound L|q_2|ⁿ holds for every n ≥ 4 (CN.4: 9.626 only for n ≥ 13). Status unchanged. See DISC-0205.
