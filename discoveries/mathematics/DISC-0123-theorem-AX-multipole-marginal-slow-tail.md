# Discovery: Theorem AX, marginal slow-tail readings of a 2^ℓ-pole are exactly G=Mc on every enclosing sphere

## Discovery ID

DISC-0123

## Status

THEOREM (mathematical sense only; written all-ℓ proof in the repository, sympy exact for ℓ≤5). Method KNOWN (homogeneity, multipole decomposition P=Σ|ξ|^(2j)H_(ℓ−2j), spherical-harmonic moments); the explicit constants are not searched, novelty UNRESOLVED. Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~11:01am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit e81b8148608b360254f88c0534e71ace97c54783. Paths: README.md Theorem AX; CLAIM_STATUS.md Theorem AX row; scripts/multipole_marginal_flux.py; tests/test_cli.py; scripts/cli.py.

## Original Evidence

Point source ρ̃=4πP(∂)δ, Φ=P(∂)C_τ r^(2τ−1), Maxwell form T[Φ,Φ]. AX.1: G(S_(c,R))=∫_(S²) f(ω)(ρ^k−R^k)/k dω, k=4τ−2−2ℓ, so G=R^(4τ−3−2ℓ)M_τ c+O(|c|³R^(4τ−5−2ℓ)). AX.2: at τ_ℓ=(3+2ℓ)/4, G=Mc exactly for every R>|c|; τ_ℓ−(1+ℓ)/2=¼, so the literal reading never exists there. AX.3: M=Σ_j 𝓜_(ℓ−2j)[H_(ℓ−2j)], 𝓜_m[H]=8/(π(2m+3)²)((N/2)I−4/(4m²−1)B), tr 𝓜_m=−4N/(π(2m−1)(2m+3)); quadrupole M=(16/81)(trA)²I+(32/735)tr(A0²)I−(512/2205)A0². AX.4: M≠0 without an |ξ|^ℓ part and for every quadrupole; M=0 for P*=H4+(4√11/385)|ξ|⁴. AX.5: with the next moment, G=Mc+g0+½ln(1−|c|²/R²)v+M′c/(R²−|c|²) exactly.

## Discovery

The marginal exponent of DISC-0120 extends to every multipole order with an explicit centre-response matrix M, and M can vanish (ℓ=4).

## Why It Matters

It proves the repository's Conjecture AW.4 (DISC-0122) and closes the pure-multipole case of the slow-tail family. It does not create a force: the value is linear in the audit centre and 0 on centred spheres.

## Derivation

Repository proof (README Theorem AX). Archive sanity re-derivation of AX.1's key step: f=∇Φ ΔΦ is homogeneous of degree k−3 and supported off the source, so the vacuum volume integral between S_(c,R) and the centred sphere reduces radially to ∫f(ω)∫_R^ρ s^(k−1)ds dω=(ρ^k−R^k)/k; at k=1 this is ρ−R, linear in c to all orders on a sphere because ∫f(ω)(√(R²−|c|²+(ω·c)²)−R)dω vanishes by parity (f odd). Consistent with the repo.

## Assumptions

Assumption AW (static massless Ψ=A0, 4πε0=1, isolated device), finite-part kernel C_τ r^(2τ−1) where the literal reading diverges, Maxwell form only, point source (extended-device asymptotics DERIVED, not fully proved).

## New Results

Archive independent check `/workspace/scratch-ifi/indep_theorem_AX.py` / `.log` (11/11 PASS; does not import the repo script; sympy gradients of P(∂)C_τ r^(2τ−1), own 200×400 Gauss–Legendre sphere quadrature and own 200² cube-face quadrature): ℓ=1 recovers AW's 16/75(|p|²I−8pp^T) to 3e−14; random symmetric A at τ=7/4 gives G=M_closed c on R=0.9,1.7,4,11 to 6e−15, linear in c, 0 on centred spheres; control τ=1.6 not radius-free; ℓ=3 H=xyz at τ=9/4 radius-free (spread 3e−17) and trace formula matches to 1e−10; P* at τ=11/4 gives |G|=1e−16 on off-centre spheres while H4 alone gives |Mc|=1.36e−3.

## Prior Art

Homogeneous-kernel scaling, harmonic decomposition and Funk–Hecke-type sphere moments are classical; Riesz/finite-part kernels as in DISC-0120. The explicit M constants were not searched; no novelty claimed.

## Novelty Analysis

Method KNOWN; the specific marginal-reading constants and the M=0 symbol P* are UNRESOLVED (not searched).

## Falsification Attempts

Attacked radius independence, linearity in c, the quadrupole closed form on a random non-axisymmetric A, the ℓ=3 trace law, and the M=0 claim with a control (H4 alone). All survived. Off-marginal control confirmed radius dependence.

## Experimental Validation

None; mathematical result only.

## Mathematical Status

Theorem (repository proof, archive numerical confirmation ℓ≤4). Extended-device part AX.5 asymptotics are DERIVED, not fully proved.

## Patent Relevance

None.

## Related Discoveries

- DISC-0120. Theorem AW (ℓ=0,1 marginal cases).
- DISC-0122. Conjecture AW.4, proved here (status CONJECTURE → THEOREM).
- DISC-0124. Kept Failure AX.1.

## Open Questions

Classification of M=0 symbols for even ℓ≥4; r^(2j)ln r kernels; non-Maxwell slow-tail tensors; Ψ_info≠A0; the 0.45 mesh.

## Next Experiments

Archive check of AX.5's exact log term for a quadrupole+octupole point source; sympy check of 𝓜_m for m=4,5.

## Reproduction Instructions

`python3 scripts/multipole_marginal_flux.py` in IFI at e81b8148608b (EXIT 0, 58 ok, ~50 s); `python3 /workspace/scratch-ifi/indep_theorem_AX.py` (~3 s).

## Evidence Log

- 2026-10-22 ~11:01am EDT. Repo witness EXIT 0 (58 ok, 0 FAIL), log /workspace/scratch-ifi/repo_theorem_AX.log; archive 11/11 PASS.

## Change History

- 2026-10-22. Initial archive entry.
