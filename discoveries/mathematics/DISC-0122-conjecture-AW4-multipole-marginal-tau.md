# Discovery: Conjecture AW.4, a pure 2^ℓ-pole has a radius-free marginal slow-tail reading at τ_ℓ=(3+2ℓ)/4

## Discovery ID

DISC-0122

## Status

CONJECTURE (repository's own; not a claim). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~8:55am EDT corpus slice. Same pass as DISC-0120.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 7a12ab736327e6d314c2035b7c8cfb95a2025dc6. Path: README.md Theorem AW, NOT THIS paragraph, "CONJECTURE AW.4"; CLAIM_STATUS.md Theorem AW row (lists AW.4 as OPEN).

## Original Evidence

"CONJECTURE AW.4: a pure 2^ℓ-pole has G∼R^{4τ−3−2ℓ}M_{τ,ℓ}c with marginal τ_ℓ=(3+2ℓ)/4. Only scaling suggests this; it is not proved for ℓ≥2." Proved cases: ℓ=0 (τ=3/4) and ℓ=1 (τ=5/4) in DISC-0120.

## Discovery

Homogeneity of the reading suggests the marginal exponent shifts by ½ per multipole order.

## Why It Matters

It would complete the marginal-reading picture of DISC-0120 for every multipole; it would not change DISC-0121 (any such value is still linear in the audit centre).

## Derivation

None in the repository beyond scaling. Archive re-derivation of that scaling: for a pure 2^ℓ-pole, Φ=Q·∇^ℓ(C_τ r^{2τ−1}) is homogeneous of degree 2τ−1−ℓ with parity (−1)^ℓ, so T is even and homogeneous of degree 4τ−4−2ℓ and div T is odd of degree 4τ−5−2ℓ. Hence G(S_{λc,λR})=λ^{4τ−2−2ℓ}G(S_{c,R}) and G is odd in c, so if G is smooth in c, G=R^{4τ−3−2ℓ}M_{τ,ℓ}c+O(|c|³R^{4τ−5−2ℓ}), and the leading term is radius-free at τ_ℓ=(3+2ℓ)/4 (ℓ=1 gives DISC-0120's 5/4). The unproved part is M_{τ_ℓ,ℓ}≠0 (and the exact form) for ℓ≥2.

## Assumptions

As DISC-0120; 0<τ_ℓ, with τ_ℓ=(3+2ℓ)/4 never half-integer, so no log kernel.

## New Results

Archive numerical probe `/workspace/scratch-ifi/indep_conjecture_AW4.py` / `.log` (4/4 consistent; not a proof): linear quadrupole +1 at ±0.05e_z, −2 at 0 (ℓ=2), c=(0.3,0.2,0.5), 200×400 surface quadrature: τ=7/4 gives |G|=5.943580e−7, 5.943596e−7, 5.943599e−7, 5.943600e−7 at R=5,10,20,40 (radius-free to 1e−6 relative; finite-separation corrections), G(2c)=2G(c) and centred sphere 0; τ=1.6 and 1.9 give R→2R ratios 0.6596 and 1.5159 vs 2^{4τ−7}=0.6598, 1.5157. Only one axisymmetric quadrupole tested.

## Prior Art

Not searched; no novelty claimed.

## Novelty Analysis

Not applicable (open conjecture of the repository).

## Falsification Attempts

The ℓ=2 axisymmetric case survives the numerical probe. A falsifier would be a pure 2^ℓ-pole with M_{τ_ℓ,ℓ}=0 or a different scaling exponent.

## Experimental Validation

None.

## Mathematical Status

Open conjecture; numerically supported at ℓ=2 for one quadrupole only. Do not cite as a theorem.

## Patent Relevance

None.

## Related Discoveries

- DISC-0120. Theorem AW (proved ℓ=0,1 cases).
- DISC-0121. Kept Failure AW.1.

## Open Questions

General ℓ, non-axisymmetric quadrupoles, closed form of M_{τ_ℓ,ℓ}.

## Next Experiments

Symbolic cap integral for a pure quadrupole at τ=7/4; random symmetric traceless quadrupole tensors.

## Reproduction Instructions

`python3 /workspace/scratch-ifi/indep_conjecture_AW4.py` (<1 s).

## Evidence Log

- 2026-10-22 ~8:55am EDT. Recorded from IFI 7a12ab736327e6d314c2035b7c8cfb95a2025dc6; archive probe 4/4 consistent.

## Change History

- 2026-10-22. Initial archive entry.
