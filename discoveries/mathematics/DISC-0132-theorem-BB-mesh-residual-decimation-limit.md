# Discovery: Theorem BB, the mesh residual constant κ_n decimates exactly and 2^−nκ_n(α) → −4σ_∞/R_∞² for α<log3/log5

## Discovery ID

DISC-0132

## Status

THEOREM in the mathematical sense only (repository proof resting on GASKET Theorems AQ–AS as stated; K(0.45) enclosure computer-assisted, mpmath.iv). Method KNOWN (spectral decimation of the gasket resolvent, Woodbury elimination, Stieltjes/Balakrishnan representation λ^−α=(sin πα/π)∫s^−α(s+λ)^−1ds). Novelty of the constant K(0.45): UNRESOLVED, not searched. Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~3:55pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 3b98cd7aa7c102a5b9c44cedeef3ed123c53f23d. Paths: README.md "Theorem BB" (BB.1–BB.5, DERIVED rate, Kept Failure BB.1, Conjecture BB.2, NOT THIS), CLAIM_STATUS.md Theorem BB row, GASKET.md Stage 2 OPEN item (appended sentence), README Conjecture BA.2 status line, scripts/mesh_maxwell_limit.py, tests/test_cli.py.

## Original Evidence

See Discovery and Derivation below; every figure is quoted from README Theorem BB at 3b98cd7aa7c1 or from the repository witness log.

## Discovery

Under Assumption BA (DISC-0129), with G=(L^α)^+, R_n=vᵀGv, σ_n=½vᵀL^{1−α}v, Y_n=G_{p'c'}−G_{p'c''}, E_n=G_{p'c'}+G_{p'c''}−G_{cc'}−G_{cc''}: (BB.1) q_c=2x_c/R_n, κ_n=2^n(4/R_n²)(3Y_n−σ_n), κ^self_n=−2^n(4/R_n²)(σ_n−E_n), κ^cross_n=2^n(4/R_n²)(3Y_n−E_n); (BB.2) y_n(s)=r_n(s)∏_{j<n}(5+p^j(s))^−1, p(s)=s(s+5), so 0<Y_n≤5^−nR_n/2; (BB.3) e_n=s g_n with an explicit g recursion, g_n≤(3/20)^n/s², 0<E_n≤(sin πα/π)(3/20)^{n(1−α)}(1/(3(1−α))+1/α); (BB.4) for α<γ=log3/log5, lim 2^−nκ_n=K(α)=−4σ_∞/R_∞²≤−8·4^−α/R_∞²<0, with K(0.45)∈[−0.854646905120924,−0.854646905120848] from R_∞∈[2.51594623787707,2.51594623787714], σ_∞∈[1.35247562325228,1.35247562325232]; limit 0 for α≥γ; (BB.5) κ^cross_n→0 for α<α*=1−log2/log(20/3)≈0.6346, so both the 2^n growth and the limit are self-force. DERIVED (not certified): 2^−nκ_n−K∼−1.083020ρ^n at 0.45, ρ=5^α/3.

## Why It Matters

It proves DISC-0131 (Conjecture BA.2) and corrects its float estimate (≈−0.86 was 0.005 low). It also turns DISC-0130's interpretive reading (the residual is a discrete self-force/stencil defect) into a proved split: the surviving limit is entirely self-force. It does not answer the Stage 2 question for any other reading.

## Derivation

Repository proofs of BB.1–BB.5 (README). BB.1 from S3 symmetry of the corner block (x=(R_n/2)q), LG=L^{1−α} on 1^⊥ (corner current I_c=σ_nq_c), the one-sided corner-cell gradient, the reflection identity u_{p'}−u_{p''}=Y_n(q_{c'}−q_{c''}), and a sympy −3Q identity. BB.2 by eliminating midpoints (AQ (1)), Woodbury on corner modes and the midpoint value w_{b'}/(5+s). BB.3 by the corner row, the two Woodbury factors, entrywise positivity (t_n≤1), AQ (3) (p r_n(p)≤1) and the polynomial identity 3(5+s)(4+s)²−20(6+s)(2+s)=3s³+19s²+8s. BB.4 from BB.1–BB.2, monotone σ_n↓σ_∞, R_n↑R_∞ (AQ–AS). BB.5 from BB.2–BB.3. The archive did not re-derive the Woodbury algebra symbolically; it checked the resulting identities numerically.

## Assumptions

Assumption BA (one stated reading: Maxwell form f_c=q_cE_c, q=L^αu on the corners, one-sided corner-cell gradient, Green kernel A^+). GASKET Theorems AQ (1)–(3), AR (3)–(4), AS (1),(4), AZ, AT as stated in the repository (not independently re-proved here). Entrywise positivity of (L_n+s)^−1 (Theorem J).

## New Results

Conjecture BA.2 proved for every α<γ; K(0.45)=−0.85464690512… certified; limit 0 for α≥γ with explicit asymptotics κ_n(γ)∼−4σ_∞2^n/(c_R(γ)n)², and for α>γ κ_n∼−4σ_∞((ρ−1)/c_R)²(2/ρ²)^n (α=1 reproduces BA.4's −9(18/25)^n). The repo also derives that no centred corner stencil exists on the gasket (every vertex lies in the closed 60° wedge at a corner), so dropping the self term is the only analogue of the torus symmetrisation.

## Prior Art

Spectral decimation for the Sierpiński gasket (Rammal–Toulouse; Fukushima–Shima; Strichartz), Woodbury/Schur elimination, and Balakrishnan's integral for fractional powers are classical. Renormalising a divergent discrete self-energy by the inverse lattice spacing is standard practice. The specific constant K(0.45) and the cross/self split for this reading were not searched.

## Novelty Analysis

What appears specific: the closed decomposition of κ_n through the AQ–AS corner resolvent and the tangential decimation product. The tools are known; the constants are UNRESOLVED as to prior occurrence. No novelty claim is made.

## Falsification Attempts

(1) Attacked BB.1 by computing κ_n and κ^self_n directly from pair forces on an independently built mesh at three α values; agreement to 1e−8. (2) Attacked BB.2/BB.3 on direct resolvent solves; agreement to 1e−12 and bounds hold. (3) Attacked BB.4's sign/value: floats at n≤6 are below K and increasing, as BB.4 requires; a Richardson guess with ρ alone from n=4..6 gives about −0.81 to −0.83, which is not decisive because the μ^n and 5^−n corrections are comparable there, so the archive leaves the value to the repository's n=40 recursion and interval sandwich. (4) α=0.75 (>γ): the repo shows 2^−nκ_n→0, consistent with BB.4's dichotomy. No break found.

## Experimental Validation

Repository witness EXIT 0; archive float check 64/64 PASS. Required: an independent interval enclosure of R_∞, σ_∞ (AS sandwich) outside the repository code.

## Mathematical Status

Theorem (repository proof; one constant interval-certified). Rate constant −1.083020 is DERIVED, not certified.

## Patent Relevance

None. A discrete self-force renormalisation constant is not a device mechanism. Not thrust.

## Related Discoveries

- DISC-0129 → DISC-0132 (mathematical). Decimates BA's κ_n.
- DISC-0132 → DISC-0131 (mathematical). Proves Conjecture BA.2; status CONJECTURE → THEOREM.
- DISC-0132 → DISC-0130 (failed hypothesis). Proves that the surviving limit is self-force.
- DISC-0132 → DISC-0133 (failed hypothesis). Kept Failure BB.1.
- DISC-0132 → DISC-0134 (mathematical). Conjecture BB.2.
- Uses the AQ–AT/AZ corner-resolvent chain (DISC-0106 onward, DISC-0116, DISC-0127).

## Open Questions

Certified rate constant; other gradient rules; the combinatorial-current charge; any continuum D.

## Next Experiments

Independent interval re-run of the AS sandwich; extend the archive recursion check to n=10, 20, 40.

## Reproduction Instructions

Repository: `cd informational-flux-identity && git checkout 3b98cd7 && python3 scripts/mesh_maxwell_limit.py` (about 4 min; archive run EXIT 0, log /workspace/scratch-ifi/repo_BB.log). Archive: `cd /workspace/scratch-ifi && python3 indep_theorem_BB.py` (about 50 s; 64/64 PASS, log indep_theorem_BB.log; reuses the own gasket build of indep_theorem_BA.py).

## Evidence Log

- 2026-10-22 ~3:55pm EDT. Recorded from IFI 3b98cd7aa7c102a5b9c44cedeef3ed123c53f23d. Repository witness scripts/mesh_maxwell_limit.py EXIT 0 (231.5 s). Archive independent float check (own gasket build, own dense spectral calculus, not the repository code): BB.1 κ_n and κ^self_n formulas equal the direct pair-force sums to 1e−8 relative at α=0.45 levels 1–6 and α=0.25, 0.6 levels 1–4; 0<Y_n≤5^−nR_n/2 and 0<E_n≤ the BB.3 bound at every one of those 14 (α,n); cross constants at 0.45 match the certified κ^cross_1..4 to 1e−9; BB.2 tangential decimation y_n(s)=r_n(s)∏(5+p^j(s))^−1 and BB.3 e_n=s g_n, g_n≤(3/20)^n/s² hold on direct resolvent solves at n=1,2,3, s∈{0.5,3,1.4}. 64/64 PASS. Floats 2^−nκ_n=−2.0214,−1.6535,−1.3423,−1.1579,−1.0488,−0.9818 (n=1..6) increase toward K from below, consistent with the repo's recursion values −0.880867 (n=10), −0.855254 (n=20), −0.854647 (n=40). The archive did NOT independently certify K or reproduce the n=10–40 recursion; those rest on the repository witness (EXIT 0).

## Change History

- 2026-10-22. Initial archive entry.
