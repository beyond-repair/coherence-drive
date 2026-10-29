# Discovery: Kept Failure BX.5, the spectral measure ν behind F=θ is not carried by at most 16 geometric series λ_j·5^Z (no closed form of Q_∞ as ≤16 self-similar pole series)

## Discovery ID

DISC-0178

## Status

REJECTED (the hypothesis; the repository's own Kept Failure with a certified witness). Method KNOWN (Carathéodory–Toeplitz rank). Not thrust.

## Date Discovered

2026-10-29 (America/New_York), ~1:57am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 06eddfa7560014a0f40341be0a6f89a0e4863eb4.

## Original Evidence

GASKET.md Kept Failure BX.5 (line 3135), BX.4 Toeplitz certificate (line 3121 onward), CLAIM_STATUS.md row (line 80), scripts/gasket_fractional_profile_spectral.py.

## Discovery

Hypothesis: Q_∞(u)=Σ_(j≤r) c_j Σ_(n∈Z) 3^n/(λ_j5^n+u) with r≤16, i.e. F is a finite superposition of r self-similar pole series (r=1 being the most natural closed form F(τ)=cΣ_nK(t_0+n−τ)). Such ν makes m a sum of r atoms, so the Toeplitz section T_(r+1)=(m̂_(i−j)) has rank ≤r. But T_17 is certified positive definite (DISC-0177, BX.4), so m has at least 17 support points per period and the hypothesis fails for every r≤16. For r=1 a one-number witness: one atom forces ρ_k=1, while ρ_1≤0.7696418615.

## Why It Matters

Closes the obvious finite closed-form route for F, G*, t_max, t_min (DISC-0170/0173/0176 open item) for up to 16 pole series. It does not exclude infinitely many atoms (pure point ν), which remains open.

## Derivation

Repository argument (GASKET.md line 3135) plus sympy det T_3=0 for two symbolic atoms; the certificate is T^mid−2εI≻0 with ‖E‖_F≤ε, so T≻εI.

## Assumptions

DISC-0177's BX.1–BX.2 (positivity of m) and BX.4's enclosures.

## New Results

Lower bound of 17 on the support size of m per scale period.

## Prior Art

The rank bound for Toeplitz matrices of r-atomic measures is classical (Carathéodory–Toeplitz–Fejér). Nothing new in method.

## Novelty Analysis

Not applicable to a rejected hypothesis; the witness is specific to this profile.

## Falsification Attempts

Independent float check (/workspace/scratch-ifi/indep_theorem_BX.py): T_17 smallest eigenvalue 1.8e−21 (m̂_k for k≤16 computed to ~1e−28 or better), ρ_1=0.76964186145502<0.7696418615. Rejection stands. T_18's float smallest eigenvalue 5.1e−23 is near the repository's ε, so 18 is undecided at this precision, as the repository says.

## Experimental Validation

Not applicable. Computational as above.

## Mathematical Status

Counterexample to a hypothesis, computer-assisted certificate (not re-certified here; reproduced in floats).

## Patent Relevance

None.

## Related Discoveries

DISC-0177 (Theorem BX), DISC-0174 and DISC-0172 (earlier rejected simple-structure hypotheses on the same profile), DISC-0175 (BV.6).

## Open Questions

Is ν purely atomic with infinitely many atoms per period, or does it have a continuous part?

## Next Experiments

Certify T_18, T_19 at higher precision (needs m̂_17, m̂_18 to ~1e−24, i.e. θ̂_k to ~1e−115).

## Reproduction Instructions

As DISC-0177.

## Evidence Log

- 2026-10-29 ~1:57am EDT. Indexed; witness reproduced in floats.

- 2026-10-29 ~4:54am EDT. Note: Kept Failure BY.3 (IFI 4e57bb8631cd, GASKET.md line 3165; DISC-0179) rejects the same hypothesis for every r≤19 (T_20≻0, smallest pivot of T_20−2ε_20I 1.2e−16, ε_20≤3.0e−32), so m has ≥20 support points per period. Status unchanged (REJECTED); no new ID. Independent floats reproduce the T_18–T_20 pivots. The "Next Experiments" item above (certify T_18, T_19) is answered by BY.

## Change History

- 2026-10-29. Initial archive entry.
- 2026-10-29. Note added for DISC-0179 (history above kept unchanged).
