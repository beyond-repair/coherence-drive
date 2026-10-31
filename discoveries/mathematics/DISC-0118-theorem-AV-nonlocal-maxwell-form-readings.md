# Discovery: Nonlocal (convolution and fractional) Maxwell-form readings are zero only for the local kernel, otherwise surface-dependent, never surface-independent nonzero (Theorem AV)

## Discovery ID

DISC-0118

## Status

KNOWN

## Date Discovered

2026-10-22 (America/New_York), ~7:58am EDT corpus slice. Preferential unread: IFI commit 9fc8c7a (Theorem AV) landed at 07:16:30 −0400, after Theorem AU (b036dcf, indexed as DISC-0116..0117).

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 9fc8c7a3e2d680395a095c36f0daf90df776d043 (2026-10-22 07:16:30 −0400). Paths: README.md "Theorem AV. Nonlocal (convolution and fractional) readings: zero only for the local kernel, otherwise surface-dependent, never a surface-independent nonzero value" (Assumption AV, AV.1–AV.4, Proofs, Kept Failure AV.1, Witness, NOT THIS); README.md Stage-2 OPEN bullet extended; CLAIM_STATUS.md Theorem AV row (VERIFIED, not thrust); scripts/nonlocal_reading_flux.py (new, 321 lines); scripts/cli.py.

## Original Evidence

Readings T[Φ1,Φ2]^{ij}=½(∂^iΦ1∂^jΦ2+∂^iΦ2∂^jΦ1)−½δ^{ij}∇Φ1·∇Φ2 with Φ_a=K_a*Ψ (K a finite Borel measure: heat kernel, Yukawa smearing, ball/shell averages) or Φ=(−Δ)^{s/2}Ψ, 0<s<2, under C5 and static massless C6 (Ψ_info=A_0), effective sources σ_a=−ΔΦ_a. AV.1: div T=−½(σ2∇Φ1+σ1∇Φ2) off shell; under (H) G(S)=½∫_ext S(σ2∇Φ1+σ1∇Φ2); ∫_{ℝ³}div T=0 (Newton's third law, k=0 Fourier mode). AV.2: any reading with T∈C¹, ∮_{|x|=R}|T|→0 and div T∈L¹ near infinity has G(S_k)→0 under dilation, so no surface-independent nonzero value. AV.3: for finite radial K, div T=0 on the vacuum for every source ⇔ G(S)=0 on every vacuum surface ⇔ K=cδ. AV.4: one radial source, sphere offset b: G=π ê_b∫_{R−b}^{R+b} m m′(1−u0²)/r² dr; point charge with (−Δ)^{1/2}: G=−(64/3π)q²R³b/(R²−b²)⁴ ê_b; with (−Δ)^{1/4}: G=−(3/5)q²b(5R²−b²)/(R²−b²)³ ê_b; heat/Yukawa positive with tail-decaying ceiling.

## Discovery

Classical electrostatics applied to the repository's reading family: a smoothed or fractionally filtered potential has an effective charge σ that leaks into the vacuum, so its Maxwell stress is not divergence-free there; the closed-surface flux is the force between the parts of the smeared charge on either side of the surface, which depends on the surface, sums to zero over all space (Newton's third law / vanishing static self-force), and vanishes under dilation. Only K=cδ (the local Maxwell reading) is conserved on the vacuum.

## Why It Matters

It closes the "nonlocal kernels" gap that Theorems V, Y, and Z listed as OPEN (see DISC-0119). It does not compute Ψ_info on the frozen 0.45 mesh and is not thrust.

## Derivation

Checked line by line. AV.1: product rule, the δ term cancels the two Hessian terms; exterior form by divergence theorem between S and S_R with o(1) surface term; interior form by Fubini and oddness of ∇𝒩. AV.2: dominated convergence on shrinking exteriors. AV.3: (b)/(c)⇒(a) uses a test function separating K from cδ, mollified radial sources, Newton's shell theorem (div T=σM x/(4πr³) for the self reading), and a bump surface ∂(B_{r1}∪B_δ(x0)) inside the vacuum. AV.4: cap integral ∫_cap ŷ dA=−ê_b πr²(1−u0²) with cap {ŷ·ê_b<u0}; sign and cap orientation re-derived independently and agree. Fractional constant C_s=(2/π)Γ(s)sin(πs/2) equals the Riesz constant. No gap found. Minor: the interior/Newton form needs σ∈L¹∩L^∞; the README says so and uses the exterior form for point charges under fractional readings.

## Assumptions

Assumption AV; C5; static massless C6 with Ψ_info=A_0; ρ a finite compactly supported charge measure; Ψ the Newtonian potential (→0 at infinity); d=3; translation-invariant kernels of the two stated kinds; hypothesis (H) for the exterior form; vacuum surfaces enclosing supp ρ; no design parameter (W, χ_vac, κ, m) enters.

## New Results

Repository script `scripts/nonlocal_reading_flux.py` at 9fc8c7a: 102 "ok" lines, 0 FAIL, "all Theorem AV checks passed; nothing here is thrust", EXIT 0, 20.5 s (archive `/workspace/scratch-ifi/repo_theorem_AV.log`). Archive `/workspace/scratch-ifi/indep_theorem_AV.py` / `indep_theorem_AV.log` (23/23 PASS; does not import the repo script; mpmath 30 digits plus numpy): C_s equals the Riesz constant at s=¼,½,1,3/2,7/4 to <1e−25; the AV.4 1D integral equals both closed forms (s=1 and s=½) and the README rationals −65536/(151875π), −512/(243π), −9/(64π), −632/5625, −19/45, −33/640 to <1e−20; own 200×400 Gauss–Legendre surface quadrature of T·n (not the 1D formula) reproduces all eight heat (t=¼) and Yukawa (μ=1) single-charge values to <1e−10 with transverse components <1e−16 and zero on the centred sphere; direct surface quadrature of the s=1 field reproduces −0.1373547766317 at (R,b)=(2,½); heat ceiling 0<G≤π(1−m(R−b))/(R−b)² holds at R=2,3,6. Coulomb-cluster values and dilation series were not independently recomputed (repository witness only).

## Prior Art

Classical: Maxwell stress tensor and its divergence identity; Newton's third law / zero static self-force of a bounded charge distribution; Newton's shell theorem; Gaussian and Yukawa smeared potentials; Riesz potentials and the fractional Laplacian constant (Riesz 1949; Stein). The off-centre-sphere closed forms are elementary integrals. No prior-art comparison in the repository warrants THEOREM elevation; none invented here.

## Novelty Analysis

None. Classical identities applied to the repository's nonlocal reading family (same pattern as DISC-0059 / DISC-0061 / DISC-0068 / DISC-0070).

## Falsification Attempts

Attacked the AV.4 sign and cap orientation by re-deriving the exterior cap; checked the 1D formula against a direct 3D surface quadrature that never uses it; checked closed forms against exact rationals; checked C_s against the Riesz constant; checked the positive-kernel ceiling; checked that the centred sphere gives zero and that transverse components vanish. Checked AV.2 decay hypotheses for the fractional case (σ∇Φ∼r^{−5−2s}∈L¹, |T|R²∼R^{−2−2s}→0). No contradiction with the theorem statement.

## Experimental Validation

None.

## Mathematical Status

Classical results; proof correct. Classified KNOWN (not THEOREM elevation): continuum reduction matching the Q–Z pattern.

## Patent Relevance

None.

## Related Discoveries

- DISC-0070 / DISC-0071. Theorem Z (pseudotensor first-derivative readings), whose NOT THIS listed nonlocal kernels.
- DISC-0068 / DISC-0069, DISC-0061 / DISC-0062, DISC-0059 / DISC-0060. Theorems Y, V, U.
- DISC-0057 / DISC-0058. Theorem T (screened readings); Yukawa-type decay of the remainder.
- DISC-0049. P.2 undifferentiated-reading flux; nonlocal undifferentiated pieces not reopened.
- DISC-0119. Failed hypothesis. Kept Failure AV.1.

## Open Questions

Slow-tail smoothing kernels ((−Δ)^{−τ}, τ≥½) outside (H); nonlocal Hessian or higher-derivative nonlinear functionals beyond AV.2's decay no-go; nonlocal undifferentiated pieces; time-dependent fields; Ψ_info ≠ A_0; Stage 2 0.45 mesh (still OPEN). Claim ceiling unchanged.

## Next Experiments

Independent recomputation of the Coulomb-cluster and dilation figures (not done in this pass).

## Reproduction Instructions

`git checkout 9fc8c7a3e2d680395a095c36f0daf90df776d043 && python3 scripts/nonlocal_reading_flux.py`. Archive logs: `/workspace/scratch-ifi/repo_theorem_AV.log`, `/workspace/scratch-ifi/indep_theorem_AV.log`.

## Evidence Log

- 2026-10-22 ~7:58am EDT. Repo witness EXIT 0; independent check 23/23 PASS. Repository description still matches its claim fence. Only other push since the previous slice: mend fix/mend-playtest-rc 0bcafb4 / 82aa8d4 / b6d1877 (combat UI wrap fix H14 and QA docs; no research claim).

## Change History

- 2026-10-22. Initial archive entry.
