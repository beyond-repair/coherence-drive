# Discovery: Theorem CO — a_3 ≠ 0 in CN.2, so |λ_3|/r is the exact second-order rate of the level sums

## Discovery ID
DISC-0201

## Status
THEOREM (mathematical sense only; proof and arb/acb witness are in the source repository). Method: KNOWN (Riesz projections, Krawczyk/Brouwer eigenvector enclosures, Cauchy estimates and trapezoid aliasing bounds for power series, second resolvent identity). The specific constants (a_3, B_3, sharpened B) for this operator: UNRESOLVED as to novelty; no claim of a mathematical first. Not a flux, not thrust.

## Date Discovered
2026-10-30 (indexed ~12:00 EDT; source commit 2026-10-30 11:34:20 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 888d3bee13fa (full SHA in the ledger row)

## Original Evidence
- GASKET.md, new section "Theorem CO" (line 3956, +49 lines); the CA–CN "What stays open" item on a_3 (line 3944) edited in place to point to CO.
- CLAIM_STATUS.md, new row 97 after Theorem CN.
- scripts/gasket_fractional_profile_level_third.py (new, 335 lines; imports BZ, CB, CE, CG, CN scripts unchanged); scripts/cli.py; tests/test_cli.py (+29); README.md.

## Discovery
- CO.1: F_0 = L̃⁴G continues holomorphically to |s − c| < (51/50)R (exact pole/real-part conditions; |v_i| ≤ 0.6211 on 4096 arcs; CN.1's Krawczyk boundary test), sup |F_0| ≤ S_ρ = 0.0249397.
- CO.2: 2048-point trapezoid sums of certified values enclose Taylor coefficients f_0..f_80 with aliasing ≤ 6.1·10⁻²⁰.
- CO.3: Krawczyk encloses right/left eigenvectors of M_80 at r, λ_2, λ_3; a_j^N = c_0 (w·f)/(w·v) (L̃v)(x_0)/μ_N exactly.
- CO.4: second resolvent identity bounds |a_j − a_j^N|; result a_3 = −2.36116·10⁻⁵ ± 4.6·10⁻⁸ ≠ 0, a_2 = −4.15764·10⁻⁵ ± 4.9·10⁻¹¹, a_1 = 0.0057125687109 ± 1.6·10⁻¹³, B = −8.21069 ± 10⁻⁵, B_3 = −1570 ± 3.
- CO.5: since (λ_2/r)² = 0.0297727 < |λ_3|/r = 0.0402794 and 10⁻³/r < |λ_3|/r, (log(s_{n+1}/(r s_n)) − B q_2ⁿ(q_2 − 1))/q_3ⁿ → B_3(q_3 − 1) ≈ 1.63·10³ ≠ 0.

## Why It Matters
Closes the a_3 ≠ 0 item DISC-0200 left open, and identifies the second-order correction rate as |λ_3|/r rather than (λ_2/r)² or the 10⁻³ inner contour. It computes a_j from the Riesz projection directly, which is a second, independent route to a_1 and a_2 (DISC-0200 got them from level-sum annihilators); the two overlap.

## Derivation
GASKET.md CO.1–CO.5 proofs. Checked by hand here:
- CO.1: maximum-principle/boundary argument (h(∂D_ρ) ⊂ Ω, C∖Ω connected and unbounded ⇒ h(D̄_ρ) ⊂ Ω) is correct; uniqueness of continuation is standard.
- CO.2: f̃_n = Σ_l f_{n+lM} and the Cauchy bound |f_n| ≤ S_ρ ρ⁻ⁿ give the stated geometric aliasing bound. Sound.
- CO.3: rank-one Riesz projection of a simple eigenvalue is (w·h)/(w·v) v; the L̃v/μ_N lift to the full operator is the usual finite-section identity. Sound given CG.2's one-eigenvalue-per-disk count.
- CO.4: margin |a_3| / error ≈ 513, so a_3 ≠ 0 is not near the enclosure boundary.
- CO.5: three-term expansion of log(s_{n+1}/(r s_n)); the (λ_2/r)² cross term and e_k are o(q_3ⁿ) by the certified inequalities. Sound; no explicit n_0 claimed (the repo says so).

## Assumptions
CE.1–CE.3; CG.2–CG.3 eigenvalue enclosures and simplicity; CN.1's box V and boundary argument (box checks re-run); CN.2's circles (re-run). Textbook facts only.

## New Results
Exact second-order asymptotics of the level-sum ratios; B sharpened 50×; a_1, a_2 obtained by a method independent of CN.3 and consistent with it (CO a_2 −4.15764·10⁻⁵ lies in CN's −4.158·10⁻⁵ ± 4.4·10⁻⁹; CO B −8.21069 lies in CN's −8.211 ± 5·10⁻⁴).

## Prior Art
- Riesz projections and spectral expansions of transfer operators: Ruelle; Baladi, "Positive Transfer Operators and Decay of Correlations" (2000).
- Krawczyk (1969); validated eigenvector enclosures (Rump; Neumaier).
- Trapezoid rule aliasing for analytic periodic functions: Trefethen & Weideman, SIAM Review 56 (2014).
Mechanism standard; no prior statement about this specific operator found, which is expected for a repository-specific object.

## Novelty Analysis
Method KNOWN. Specific: certified nonvanishing of a_3 and the second-order rate for this gasket level-sum operator. Not a first in any general sense.

## Falsification Attempts
- Repo witness: see Evidence Log.
- Independent script `mathematics/scripts/indep_theorem_CO.py` (mpmath, no repo imports; CC's printed 12-digit s_4..s_14, CG's r, λ_2, λ_3 midpoints), 14/14 PASS: q_3 = −0.0402794, q_2² < |q_3|, 10⁻³/r < |q_3|; B = −8.210691, B_3 = −1570.22, B_3(q_3 − 1) = 1633.5, a_3/a_1 = −0.004133; the three-term model with CO's a_j leaves residual −2.2·10⁻⁷ at n = 4 (1% of |a_3|) and < 10⁻¹² for n ≥ 6, while dropping a_3 leaves exactly ≈ a_3 at n = 4. A weighted least-squares fit of s_4..s_14 with a float fourth eigenvalue λ_4 ≈ −2.16·10⁻⁴ (not certified) gives a_3 = −2.36116·10⁻⁵, a_2 = −4.157639·10⁻⁵, a_1 = 0.0057125687109, a_4 ≈ −2.2·10⁻⁷, matching CO to all printed digits. The Observation values 1672.9, 1624.4, 1639.2, 1629.5, 1636.4, 1631.2 for n = 4..9 are reproduced to ±0.5.
- Caveats on my own check: (i) it is a float fit, not a proof; DISC-0200/CN.3 showed level sums to n = 13 cannot certify a_3 alone. (ii) A first attempt without the λ_4 term missed a_3 by 1.2% because the a_4 term (−2.2·10⁻⁷) sits in s_4; that was my model error, not the repo's. (iii) For n = 10..12 my normalized residuals (1727, 1038, −24874) are noise from 12-digit inputs (q_3¹² ≈ 2·10⁻¹⁷); the repo's own Observation already warns that n = 12 is a sanity check only.
- Logic attacked: whether a_3 could be an artefact of truncation N = 80 (bounded by ε_80 = 1.741·10⁻¹⁷ via the resolvent identity; error 3.4·10⁻⁸ ≪ |a_3|); whether the wrong eigenvector could be picked (CG.2 disk isolation). No break found.

## Experimental Validation
Computational only.

## Mathematical Status
Theorem (computer-assisted constants; CE/CG/CN enclosures imported).

## Patent Relevance
None. Pure spectral asymptotics; repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0200 → DISC-0201 (mathematical): CN's open a_3 ≠ 0 item answered; B sharpened. DISC-0191 → DISC-0201: λ_3 from CG.2 now shown to carry nonzero weight in the level sums. The C^k-spectrum chain DISC-0194 → … → DISC-0199 is not changed.

## Open Questions
Explicit n_0 and constant in CO.5; λ_4 and a_4; C_G in CF.3; eigenvalues on |z| = ρ(L_k); rate for inf R_n → ρ(L_1); closed forms of r, λ_2, B, B_3.

## Next Experiments
Certify λ_4 (float −2.16·10⁻⁴) and a_4 by the same projection route (the float fit above suggests a_4 ≈ −2.2·10⁻⁷, i.e. a_4 ≠ 0 is likely but unproved); give explicit n_0 in CO.5.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at 888d3bee13fa; `pip install python-flint mpmath sympy numpy`; run `python3 scripts/gasket_fractional_profile_level_third.py` (about 2–3 min; exits nonzero on any failed check). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_CO.py` in this repo.

## Evidence Log
- 2026-10-30 ~12:05 EDT: repo witness `python3 scripts/gasket_fractional_profile_level_third.py` at 888d3bee13fa EXIT 0 (147.3 s script time, wall 2m28s), 21 `ok` checks, ends "all Theorem CO checks passed"; a_3 = [−2.36e-5 ± 4.57e-8], B = [−8.21069 ± 8.28e-6], B_3 = [−1.57e3 ± 2.50], B_3(q_3 − 1) = [1.63e3 ± 5.84]. Independent check 14/14 PASS.

## Change History
- 2026-10-30: created from IFI 888d3bee13fa.
- 2026-10-30: note added (status unchanged); open item "explicit n_0 in CO.5" answered by DISC-0202.

## Note (2026-10-30, appended; text above unchanged)
The open item "explicit n_0 and constant in CO.5" is answered by IFI Theorem CP at f7845ada80f95ebb7af3a4d77664a073abc4d561: sign T_n = (−1)ⁿ for every n ≥ 4 with 1360.9|q_3|ⁿ ≤ |T_n| ≤ 1906.1|q_3|ⁿ, and CO.5's limit is approached at the exact rate λ_2²/(r|λ_3|) = 0.7391538. See DISC-0202.
