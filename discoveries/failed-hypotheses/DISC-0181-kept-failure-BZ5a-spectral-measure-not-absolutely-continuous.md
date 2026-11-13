# Discovery: Kept Failure BZ.5(a), the spectral measure ν behind F=θ is not absolutely continuous

## Discovery ID

DISC-0181

## Status

REJECTED (the hypothesis; the repository's own Kept Failure with a certified witness and a proof). Method KNOWN. Not thrust.

## Date Discovered

2026-10-29 (America/New_York), ~6:01am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit f9942d98a5fa5e535f07b83e6362bde6344af6f0.

## Original Evidence

GASKET.md Kept Failure BZ.5 (line 3214), BZ.4 and BZ.5 in Theorem BZ (line 3181 onward); scripts/gasket_fractional_profile_atoms.py.

## Discovery

Claim tested: "ν (equivalently m) is absolutely continuous". False, twice over: BZ.4 removes every absolutely continuous part (Q_∞ meromorphic off the null set Z), and independently the certified atom λ=3.615256719887703… carries ν({λ})=0.479640692929…>0.

## Why It Matters

Closes one of the two alternatives DISC-0177/0179 left open (a.c. versus atomic); the stall of BY's Toeplitz certificates (DISC-0179) is explained by singularity (Szegő, cited by the repository as context only).

## Derivation

See DISC-0180 (BZ.3–BZ.5).

## Assumptions

As DISC-0180.

## New Results

None beyond DISC-0180.

## Prior Art

Spectral measures of gasket Laplacians are known to be singular in related settings (Teplyaev 1998, see DISC-0180 Prior Art). KNOWN in kind; identification of this specific measure not verified.

## Novelty Analysis

Not novel as a kind of result; the specific measure's identification with the literature is UNRESOLVED.

## Falsification Attempts

My independent finite-level recursion (/workspace/scratch-ifi/indep_theorem_BZ.py) finds the same atom at 3.615256719887703 with mass 0.479640692929 at M=40 and M=60. The witness stands.

## Experimental Validation

Not applicable.

## Mathematical Status

Rejected hypothesis (certified counter-witness).

## Patent Relevance

None.

## Related Discoveries

DISC-0180 (Theorem BZ), DISC-0177 (Theorem BX), DISC-0178 (Kept Failure BX.5, the other half of Kept Failure BZ.5), DISC-0179.

## Open Questions

Whether ν has a singular continuous part on −Z.

## Next Experiments

See DISC-0180.

## Reproduction Instructions

As DISC-0180.

## Evidence Log

- 2026-10-29 ~6:01am EDT. Indexed.

## Change History

- 2026-10-29. Initial archive entry.
