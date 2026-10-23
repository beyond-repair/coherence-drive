# Discovery: Theorem BA, the Maxwell-form reading on the frozen 0.45 mesh leaves a nonzero integrated residual D = κ_n(α) Q(d)

## Discovery ID

DISC-0129

## Status

THEOREM in the mathematical sense only (repository proof; BA.3 computer-assisted, interval-certified at levels 1–4). Method KNOWN (discrete action–reaction split of a pair force, S3 Schur reduction, Krylov/interval spectral calculus). Novelty of the constants κ_n(0.45): UNRESOLVED. Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~1:57pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit fe388f3b633ff0cafbfd653758afde0ab7284b93. Paths: README.md "THEOREM BA" (with Assumption BA), CLAIM_STATUS.md Theorem BA row, GASKET.md Stage 2 OPEN item, scripts/mesh_maxwell_residual.py, tests/test_cli.py.

## Original Evidence

Assumption BA: level-n gasket, A=L^0.45 (combinatorial Laplacian L), Ψ=u the A-Dirichlet extension of corner data d, charge q=Au (supported on corners C, neutral), corner-cell affine gradient g_c, discrete divergence f_c=−q_c g_c, Green kernel G=A⁺, pair force φ_ck=−q_c q_k g_c[G e_k], Maxwell piece φ^M=(φ_ck−φ_kc)/2, residual φ^R=(φ_ck+φ_kc)/2.

Theorem BA: (1) Σφ^M=0 and cut form on every vertex set; G(S) depends only on S∩C; G(S)=D for every S⊇C. (2) D_n(d)=κ_n(α)Q(d), Q(d)=Σ_c(d_c−d̄)²(P_c−P̄), |Q|=|d−d̄|²/(2√3). (3) certified κ_1=−4.0427396046867839149…, κ_2=−6.6139165202761608886…, κ_3=−10.738239541819965987…, κ_4=−18.526339511158477727… (widths ≤3e−37); level-4 D for d=(1,−½,−½) is (6.9473773166844291477…, 4.0110701639496550916…). (4) κ_n(1)=−9((18/25)^n−(6/25)^n). (5) translation-invariant even kernel plus odd stencil gives D=0.

## Discovery

Under Assumption BA the deferred Stage 2 question ("Σ div ≠ 0 after the Maxwell piece is removed on the 0.45 mesh?") has answer yes at levels 1–4 for every nonconstant corner data. The repository itself (Kept Failure BA.1, DISC-0130) rejects reading that residual as an informational signal.

## Why It Matters

It is the first concrete mesh computation for the GASKET.md Stage 2 OPEN item that every continuum reading (DISC-0042/0043 Theorem N, DISC-0044, DISC-0118, DISC-0120, DISC-0123) had deferred. It closes the item for this specific reading only.

## Derivation

As in the repository. BA.1 is antisymmetry plus linearity of g_c (f_c=Σ_kφ_ck because g_c kills constants and u=Gq+const). BA.2 is shift invariance plus S3 equivariance: a quadratic, S3-equivariant map from the 2-dim standard representation to the plane is one scalar times Q. BA.4 diagonalises the harmonic-extension matrix.

## Assumptions

Assumption BA as listed (gradient rule, charge q=Au not Lu, device = Dirichlet corners, quadratic reading of Theorem N). Other gradient rules keep BA.1–BA.2 but change κ_n.

## New Results

None beyond the repository. The archive reproduces it independently (below).

## Prior Art

Discrete action–reaction decomposition, Schur's lemma for S3, fractional graph Laplacians on the Sierpinski gasket, Krylov minimal polynomials and Krawczyk enclosures are all classical. The specific constants κ_n(0.45) were not found in a quick search; no exhaustive search was done.

## Novelty Analysis

The mechanism is known; only the numbers are specific to this freeze. UNRESOLVED for the constants. No novelty claim for the residual as physics (see DISC-0130).

## Falsification Attempts

Archive script /workspace/scratch-ifi/indep_theorem_BA.py (own gasket construction, own eigendecomposition for L^α and A⁺, own affine-gradient solve; float64): 20/20 PASS. κ_1..κ_4 match the certified values to ≤3e−12; interior harmonicity, neutrality, Σφ^M=0, Σφ^R=D and D∥Q hold to 1e−9; κ_n is the same for d=(0.3,2,−1); α=1 matches −9((18/25)^n−(6/25)^n) for n=1..4; level-4 D matches; self part κ^self_4=−18.530321; floats κ_5=−33.5613065, κ_6=−62.8346482 (2^−nκ_n=−1.04879, −0.98179) match the repo. Repository witness python3 scripts/mesh_maxwell_residual.py: EXIT 0, "all Theorem BA checks passed" (61 s). The torus control (BA.5, Kept Failure witness i) was taken from the repository log, not re-implemented.

## Experimental Validation

None (pure mathematics / numerics).

## Mathematical Status

Theorem (repository proof; BA.3 computer-assisted).

## Patent Relevance

None.

## Related Discoveries

DISC-0042, DISC-0043 (Theorem N quadratic reading) → DISC-0129 (mathematical: the mesh version of ∂_iΨΔΨ). DISC-0118, DISC-0120, DISC-0123 (continuum readings that deferred the mesh) → DISC-0129 (conceptual). DISC-0129 → DISC-0130 (failed hypothesis), DISC-0129 → DISC-0131 (conjecture).

## Open Questions

Which gradient rule the freeze intends; combinatorial current Lu as charge; certified levels ≥5.

## Next Experiments

Certify κ_5, κ_6; repeat with a centred or symmetric gasket gradient rule and see whether κ_n changes sign or vanishes.

## Reproduction Instructions

git clone https://github.com/beyond-repair/informational-flux-identity && git checkout fe388f3b633ff0cafbfd653758afde0ab7284b93 && python3 scripts/mesh_maxwell_residual.py. Archive check: python3 indep_theorem_BA.py (numpy only, ~30 s).

## Evidence Log

- 2026-10-22. Repo witness EXIT 0; archive 20/20 PASS (/workspace/scratch-ifi/indep_theorem_BA.py, .log).

## Change History

- 2026-10-22. Initial archive entry.
