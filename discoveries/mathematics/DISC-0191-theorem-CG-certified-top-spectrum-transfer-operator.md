# Discovery: Theorem CG, certified top spectrum of CE's transfer operator on a disk of holomorphic functions

## Discovery ID
DISC-0191

## Status
THEOREM (mathematical sense only; proof in the repository with `arb` interval certificates: Pellet/Rouché count for the 80x80 truncation, resolvent-norm covers of five circles, Riesz-projection homotopy to the full operator). Method KNOWN (Galerkin/Taylor truncation of transfer operators on Hardy spaces with rigorous error bounds, cf. Jenkinson–Pollicott, Bandtlow–Jenkinson; Pellet's theorem; Riesz projections). The specific constants λ_2 = −0.0731138175124…, λ_3 = −0.0170676440626…, λ_2/r = −0.1725476021… are novelty UNRESOLVED. Not a patent candidate. Not thrust.

## Date Discovered
2026-10-29 (verified ~7:53pm EDT; documented ~8:58pm EDT after the earlier archive write did not complete)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 8364d9497c5740babd60361fde9ef10dc52b7f50 (2026-10-29 19:00:09 EDT).

## Original Evidence
- GASKET.md section "Theorem CG" (line 3528): CG.1 disk (line 3535), CG.2 matrix (line 3544), CG.3 operator (line 3545), CG.4 level-sum rate (line 3557), proof lines 3563–3565, "Kept limits" line 3569, "What stays open" line 3571, NOT THIS line 3575.
- GASKET.md line 3512/3515: CF's Observation and open item updated to point at Theorem CG (earlier wording preserved).
- scripts/gasket_fractional_profile_level_spectrum.py (new, 327 lines); scripts/cli.py, tests/test_cli.py (+32), CLAIM_STATUS.md, README.md.

## Discovery
On H² of the disk |s − 83/50| < 8/5 (s = √(t+25/4)), CE's twisted operator L̃ has exactly three eigenvalues of modulus > 10⁻³, all real and simple: r (CE's value, ±1e−14), λ_2 = −0.07311381751240 ± 1e−13 and λ_3 = −0.01706764406262 ± 1e−12. Consequently |log(s_(k+1)/(r s_k))| ≤ C·0.17255^k, replacing CF.3's proved rate 0.8855^k for the level sums (C not explicit).

## Why It Matters
Turns the float observation in DISC-0190 (λ_2 ≈ −0.0731) into a certified value and gives the true geometric rate at which the level-sum ratio converges to r.

## Derivation
As in the repository: CG.1 exact pole/real-part inequalities and a 2048-arc `arb` cover of |u|=1 bound the tail of L̃ beyond the N=80 Taylor block; CG.2 Pellet's inequality at ρ=3/100 and 1/1000 counts eigenvalues of M_80, sign changes of χ isolate three real roots; CG.3 resolvent covers (168, 980, 19, 61, 157 samples) and the homotopy T_τ = L̃P_N + τ(L̃ − L̃P_N) carry the count to L̃; reality via the conjugation symmetry; identification of the top one with r through CF.5; CG.4 via Schwarz–Pick contraction so L̃^(j0+4)G ∈ H², then spectral splitting.

## Assumptions
- CE, CF imported unchanged (DISC-0188, DISC-0190).
- Count is for holomorphic eigenfunctions on D only (repository's own kept limit).

## New Results
- Archive observation: the block-form resolvent bound ‖(z − L̃P_N)⁻¹‖ ≤ ‖(z − M_N)⁻¹‖(1 + β_N/|z|) + 1/|z| is correct for the stated lower-triangular block form.
- λ_4 is not certified (repository says the |z|=1e−4 circle would need about 4·10⁴ samples).

## Prior Art
Rigorous computation of transfer-operator spectra on Hardy/Bergman spaces with truncation error bounds is established (Jenkinson–Pollicott for Hausdorff dimension; Bandtlow–Jenkinson on analytic transfer operators; Pellet 1881; Kato/Riesz perturbation of spectral projections). No targeted search for these constants.

## Novelty Analysis
Method KNOWN. Specific operator and constants novelty UNRESOLVED.

## Falsification Attempts
- Independent script (`mathematics/scripts/indep_theorem_CG.py`, no repository imports): own Chebyshev collocation and power iteration reproduce r, λ_2, λ_3 inside the stated balls; power-iteration deviation ratio m=12→13 is −0.172547602171, matching λ_2/r; 12/12 checks PASS.
- Attack on the scope: CG does not show λ_2 is the second eigenvalue on C¹(X); the repository states this itself, so CF.5's C¹ bound stands on C¹ and only the level-sum rate is replaced. No contradiction found.

## Experimental Validation
Repo witness `python3 scripts/gasket_fractional_profile_level_spectrum.py` EXIT 0 (106.8 s). Independent check 12/12 PASS.

## Mathematical Status
Theorem (computer-assisted proof with interval arithmetic). C not explicit; λ_4 open.

## Patent Relevance
None.

## Related Discoveries
- DISC-0190 (Theorem CF): CG certifies the λ_2 that CF only observed; CF.5 is used to identify the top eigenvalue with r.
- DISC-0188 (Theorem CE): same operator and r.
- DISC-0186, DISC-0187: level structure of ν.

## Open Questions
- Explicit C; λ_4; whether λ_2 is second on C¹(X); closed form for r.

## Next Experiments
- Certify λ_4 with a finer cover or larger N; extend the count to C¹(X).

## Reproduction Instructions
`git clone https://github.com/beyond-repair/informational-flux-identity && git checkout 8364d9497c5740babd60361fde9ef10dc52b7f50 && python3 scripts/gasket_fractional_profile_level_spectrum.py`; then `python3 discoveries/mathematics/scripts/indep_theorem_CG.py` from this repository.

## Evidence Log
- 2026-10-29 ~7:53pm EDT. Verified from commit 8364d9497c5740babd60361fde9ef10dc52b7f50: repo witness EXIT 0 (106.8 s); independent check 12/12 PASS.
- 2026-10-29 ~8:58pm EDT. Archived.

## Change History
- 2026-10-29: created.
