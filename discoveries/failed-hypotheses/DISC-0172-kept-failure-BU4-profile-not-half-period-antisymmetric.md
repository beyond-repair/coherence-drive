# Discovery: Kept Failure BU.4, the log-periodic profile F=θ is not half-period antisymmetric (F(t+1/2)≠2⟨F⟩−F(t))

## Discovery ID

DISC-0172

## Status

REJECTED (the hypothesis that F(t+1/2)=2⟨F⟩−F(t), t=log_5 u). Certified witness in the repository; independently confirmed in floats.

## Date Discovered

2026-10-23 (America/New_York), ~5:58pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit ad459e306e19ac3ac4f1e3a74f6e7738ac9b5195.

## Original Evidence

GASKET.md Kept Failure BU.4 (line 2950), float evidence (line 2958), scripts/gasket_fractional_profile_fourier.py.

## Discovery

The hypothesis was suggested by the certified extremal nodes sitting exactly half a period apart on the grid (98534−32998=2^16 of 2^17 in BT.4; 197068−65996=2^17 of 2^18 in BU.3) and holds for every profile with only odd harmonics (e.g. AU.1's single cosine). It forces max F+min F=2⟨F⟩. Certified: (max F+min F)/2−⟨F⟩ ∈ [2.4340, 2.9084]e−11 > 0 from BU.3's brackets alone. It is also implied by BU.1 with AU's |θ̂_2|>0.

## Why It Matters

It rules out the simplest symmetric model of the oscillation and shows the second harmonic is visible in the extremes, not only in the Fourier table.

## Derivation

Arithmetic on three certified brackets (repository); alternative route via θ̂_2≠0.

## Assumptions

BU.3's brackets (DISC-0171).

## New Results

The grid coincidence of the extremal nodes is a resolution artefact: my float refinement at depth 5^−44 puts the extremes 0.4999998376 periods apart, not 1/2.

## Prior Art

Not applicable (a rejected symmetry of a specific function).

## Novelty Analysis

Not a novelty claim.

## Falsification Attempts

Tried to break the rejection: recomputed the lower bracket end from the printed outward brackets (exactly 2.4340e−11>0); float max|F(t)+F(t+1/2)−2⟨F⟩| on 4096 nodes is 5.4e−11; float a_2=−1.3472e−11≠0. The rejection stands.

## Experimental Validation

Archive /workspace/scratch-ifi/indep_theorem_BU.py (3 checks for BU.4, all PASS).

## Mathematical Status

Counterexample (certified).

## Patent Relevance

None.

## Related Discoveries

DISC-0171 (Theorem BU), DISC-0170 (BT.4 nodes that suggested it), DISC-0116 (AU, |θ̂_2|>0).

## Open Questions

The exact half-period offset of argmax and argmin.
- 2026-10-23 note (no status change): the weaker extremal-placement hypothesis is refuted separately as DISC-0174 (Theorem BV, cec4aff731ce); (max F+min F)/2−⟨F⟩=2.6909742749436036e−11 certified inside BU.4's bracket.

## Next Experiments

Certify the location of the extremes.

## Reproduction Instructions

As for DISC-0171.

## Evidence Log

- 2026-10-23 ~5:58pm EDT. Indexed with DISC-0171.

## Change History

- 2026-10-23. Initial archive entry.
- 2026-10-23 ~6:56pm EDT. Note added under Open Questions (DISC-0173/DISC-0174); original text unchanged.
