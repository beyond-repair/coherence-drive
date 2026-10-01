# Discovery: Two-mode factor two

## Discovery ID

DISC-0004

## Status

DERIVATIVE

## Date Discovered

2026-10-01. This is the date of the archive pass.

## Source Repositories

beyond-repair/bloch-coherence-factor2 at HEAD 52ff29d6dea7e2f4361ce04fdadc34128d9c88e0. The proof file is TWO_MODE_PROOF.md.

## Original Evidence

The two-mode matrix with V = Delta/2 gives Omega_- squared = epsilon_star + Delta/2. At the saddle Delta = the absolute value of epsilon_star, Omega_- squared = epsilon_star / 2, which is negative. Therefore phi_stable squared over phi_saddle squared equals 2. The proof is the 2 by 2 diagonalization in TWO_MODE_PROOF.md. The result is exact only on that reduction.

The same repository sets universal_constant to false, thrust to false, and ware_constant_0p08 to false.

## Discovery

On that two-mode reduction, the stable and saddle amplitudes stand in the ratio 2, in the sense phi_stable squared / phi_saddle squared = 2. The factor is a property of the 2 by 2 diagonalization. It is not a thrust input and it is not a derivation of 0.08.

## Why It Matters

The factor 2 sits in the same W family as the other notes, but the repository flags say it is not universal, not thrust, and not the constant 0.08. It therefore stands beside the other rows instead of feeding DISC-0002.

## Derivation

The derivation is the 2 by 2 diagonalization already written in TWO_MODE_PROOF.md. This archive does not rewrite the matrix algebra.

## Assumptions

The identity uses the two-mode matrix with V = Delta/2 and the saddle Delta = the absolute value of epsilon_star. It is exact only on that reduction.

## New Results

None.

## Prior Art

The proof is the in-repo 2 by 2 diagonalization. No external citation was fetched from TWO_MODE_PROOF.md for this pass, so none is named here.

## Novelty Analysis

There is no novelty claim. The status is a model proof on a reduction, not a theorem about a device.

## Falsification Attempts

The repository already sets thrust, the universal-constant flag, and the 0.08 flag to false. Those flags are the recorded refusal to export the factor.

## Experimental Validation

None.

## Mathematical Status

Model proof.

## Patent Relevance

None established.

## Related Discoveries

DISC-0004 stands beside DISC-0001, DISC-0002, DISC-0003, and DISC-0005. The edge label is mathematical. It is the same W family and it is not a thrust input.

## Open Questions

The factor is not known outside the two-mode reduction. The repository does not say it is a universal constant.

## Next Experiments

Do not insert the factor 2 into a thrust formula. Read TWO_MODE_PROOF.md at the named HEAD before any later use.

## Reproduction Instructions

Check out beyond-repair/bloch-coherence-factor2 at 52ff29d6dea7e2f4361ce04fdadc34128d9c88e0. Read TWO_MODE_PROOF.md and the flags universal_constant=false, thrust=false, and ware_constant_0p08=false.

## Evidence Log

- 2026-10-01. Indexed from the verified audit facts for HEAD 52ff29d6dea7e2f4361ce04fdadc34128d9c88e0.
- The GitHub description fetched the same day says "Bloch Coherence Phase — Factor-of-Two Stability Bound. Narrow, falsifiable theorem: the classical W+λφ⁴ modulated saddle supplies exactly half the Bloch gap required for spectral stability." That description is provenance only. The status in this archive follows the in-repo flags, which set thrust, the universal constant, and 0.08 to false. The description was not edited.

## Change History

- 2026-10-01. Initial archive entry. No existing file was changed.
