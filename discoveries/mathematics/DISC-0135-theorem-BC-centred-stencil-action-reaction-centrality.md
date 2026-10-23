# Discovery: Theorem BC, on the frozen 0.45 gasket action–reaction is centrality, no vertex admits an odd stencil, and the centred (Green–Gauss) stencil leaves κ_n unchanged

## Discovery ID

DISC-0135

## Status

THEOREM in the mathematical sense only (repository proof; levels 1–4 constants interval-certified by the repository, mpmath.iv). Method KNOWN (S3/D3 equivariance, reflection projection, Green–Gauss vertex gradient, telescoping recursion). Novelty of the constants and of the specific statement: UNRESOLVED, not searched. Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~5:05pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit c7a0cf681bf54979d31ff5c28c8ef9b0dad530b9. Paths: README.md "Theorem BC" (BC.1–BC.5, DERIVED torus-mechanism paragraph, Kept Failure BC.1, Conjecture BC.2, NOT THIS), CLAIM_STATUS.md Theorem BC row, GASKET.md Stage 2 OPEN item (appended sentences), README OPEN paragraph (appended sentences), scripts/mesh_centred_stencil.py, scripts/cli.py, tests/test_cli.py.

## Original Evidence

Every figure below is quoted from README Theorem BC at c7a0cf681bf5 or from the archive check log; archive-only numbers are labelled.

## Discovery

Under Assumption BC (Assumption BA with the one-sided corner-cell gradient replaced by the Green–Gauss vertex average, which on the triangular lattice is the centred six-neighbour stencil of BA.1's torus witness): (BC.1) for every S3-equivariant linear gradient rule that kills constants, H_kc=R_ck H_ck and H_cc=s(P_c−P̄), so the Maxwell (antisymmetric) piece is exactly the chord-parallel central pair force and κ_n=−(4/R_n²)(s+2√3h_⊥), κ^self=−4s/R_n², κ^cross=−8√3h_⊥/R_n²; action–reaction iff s=h_⊥=0. (BC.2) No vertex of V_n has an odd stencil: offsets lie in a closed half-plane; the isometry group is D3 with no half-turn. (BC.3) At the corners the Green–Gauss rule equals the one-sided cell rule and all charge sits there, so κ^GG_n=κ_n for every n, α (re-certified κ^GG_4(0.45)=−18.526339511158477727…). (BC.4) h_∥=2^(n−1)(E_n+Y_n), h_⊥=(√3/6)2^n(E_n−3Y_n), s=2^n(σ_n−E_n); certified tanθ_1..4=−0.3917585210483279…, −0.277452251033554…, −0.2247945906847502…, −0.2038773766517652…, s_1..4=2.62859242109…, 5.37968631401…, 10.8101556491…, 21.6368071437…. (BC.5) lim_{s→0} e_n(s)/y_n(s)=2·3^n/(3^n+1) by telescoping τ_{m+1}=3τ_m−1.

## Why It Matters

It explains, as a proved symmetry statement, why the torus cancellation of DISC-0130 (BA.5) does not transfer: on the torus a half-turn swaps two charges with linear part −I, forcing an odd stencil and H_kc=−H_ck; on the gasket the only corner swap is a reflection, so only the chord-parallel part is forced antisymmetric. Newton's third law is a condition (s=h_⊥=0), not a consequence. It closes the centred-stencil rescue of an exact zero for this reading.

## Derivation

Repository proofs of BC.1–BC.5 (README). BC.1: equivariance g_{σc}[w∘T_σ^−1]=R_σg_c[w] and S3-invariance of G give H_{σc,σk}=R_σH_ck; σ=(c k) gives the reflection law; the stabiliser of c forces H_cc onto its axis; ½(I−R_ck) is the chord projection; two sympy sums. BC.2: cells are upward translates; role offset pairs listed; checked at every vertex to n=6; isometries preserve degree, so permute the three degree-2 corners. BC.3: |C(c)|=1 at corners plus supp q=C (Theorem H). BC.4: BB.1's gradient split substituted. BC.5: BB's recursions give a ratio product; at s=0, t_{m+1}=t_m/(3−t_m). Consistency check (archive, algebraic): substituting BC.4 into BC.1 gives κ_n=−(4/R_n²)2^n(σ_n−E_n+E_n−3Y_n)=2^n(4/R_n²)(3Y_n−σ_n), BB.1 exactly; and tanθ=(r−3)/(√3(r+1)) with r=E/Y→2 gives −1/(3√3).

## Assumptions

Assumption BC (one stated reading; centred Green–Gauss vertex gradient). Assumption BA items (1),(2),(4),(5). Theorem H (charge on corners), Theorem BB recursions and AQ–AS as stated in the repository (not independently re-proved here).

## New Results

The pair force on the gasket under any S3-equivariant linear gradient rule splits into central Maxwell part plus self term plus a non-central cross term; the non-central angle is certified nonzero at levels 1–4. A closed small-s ratio 2·3^n/(3^n+1).

## Prior Art

Equivariant discretisation, Green–Gauss gradient reconstruction (finite-volume practice), and the link between discrete momentum conservation and centred/odd stencils are standard. Spectral decimation on the Sierpiński gasket is classical (Rammal–Toulouse; Fukushima–Shima; Strichartz). The specific constants were not searched.

## Novelty Analysis

Tools KNOWN. The statement that the gasket admits no odd stencil because its isometry group lacks a half-turn is elementary. Constants UNRESOLVED as to prior occurrence. No novelty claim is made.

## Falsification Attempts

(1) Attacked the κ formula against direct pair-force sums on an independently built mesh at n=1..6: agreement 1e−8. (2) Attacked BC.2 by enumerating every vertex's neighbour offsets at n=1..5 (odd-closure, zero sum, half-plane test over 721 directions): no exception. (3) Attacked BC.5 by direct resolvent solves at s=1e−4,1e−5: agreement within the O(s) drift. (4) Algebraic consistency with BB.1 (above). (5) Attacked the claimed signs: s>0 and tanθ<0 also hold at archive levels 5–6, outside the certified range. No break found.

## Experimental Validation

See Evidence Log. Required: independent interval certification of tanθ_n, s_n outside the repository code; a proof of E_n<3Y_n for all n.

## Mathematical Status

Theorem (repository proof; constants computer-assisted at levels 1–4).

## Patent Relevance

None. A discrete stencil-symmetry statement on a fractal mesh is not a device mechanism. Not thrust.

## Related Discoveries

- DISC-0129 → DISC-0135 (mathematical). Same residual under a centred gradient rule.
- DISC-0130 → DISC-0135 (failed hypothesis). Explains why the torus cancellation (BA.5) does not transfer.
- DISC-0132 → DISC-0135 (mathematical). BC.4 reproduces BB.1; κ^GG_n inherits the limit K(0.45).
- DISC-0135 → DISC-0136 (failed hypothesis). Kept Failure BC.1.
- DISC-0135 → DISC-0137 (mathematical). Conjecture BC.2.
- DISC-0133 → DISC-0137 (mathematical). E_n<3Y_n for all n would extend BB.1's κ^cross>0 to every level.

## Open Questions

Prove E_n<3Y_n for all n; other gradient rules that are not S3-equivariant (excluded by the freeze); the combinatorial-current charge.

## Next Experiments

Interval-certify tanθ_5, tanθ_6; run the repo's E/Y recursion independently to n=30.

## Reproduction Instructions

Repository: `cd informational-flux-identity && git checkout c7a0cf6 && python3 scripts/mesh_centred_stencil.py` (repo says about 1.5 min; log /workspace/scratch-ifi/repo_BC_run.log). Archive: `cd /workspace/scratch-ifi && python3 indep_theorem_BC.py` (about 80 s; 28/28 PASS, log indep_theorem_BC.log; reuses the own gasket build of indep_theorem_BA.py / indep_theorem_BB.py, not repository code).

## Evidence Log

- 2026-10-22 ~5:05pm EDT. Recorded from IFI c7a0cf681bf54979d31ff5c28c8ef9b0dad530b9. Archive independent float check (own gasket build and dense spectral calculus): the BC.1 formula κ_n=−(4/R_n²)(s+2√3h_⊥) with BC.4's s=2^n(σ_n−E_n), h_⊥=(√3/6)2^n(E_n−3Y_n) equals the direct pair-force κ_n to 1e−8 at α=0.45, n=1..6; s>0 and tanθ_n<0 at n=1..6; tanθ_1..4 and s_1..4 match the certified values to 1e−9 / 1e−8; archive floats tanθ_5=−0.1963417480579, tanθ_6=−0.1937567642745 (moving toward −1/(3√3)=−0.19245009); no vertex has an odd stencil and every vertex's neighbour offsets lie in a closed half-plane at n=1..5 (N=6..366); BC.5 small-s ratio e_n/y_n at s=1e−5 matches 2·3^n/(3^n+1) to 1e−5 at n=1..4; E_n/Y_n increases toward 2 from below at α=0.25, 0.6, 0.8 (n=4..6), with (2−E/Y)3^n=4.443, 3.194, 2.565 at n=6, consistent with the repo's n=16 values 4.4720, 3.2076, 2.5724. 28/28 PASS. Not independently certified in intervals; the level 1–4 certification and the sympy identities rest on the repository witness. Repository witness scripts/mesh_centred_stencil.py EXIT 0 (121.3 s, "all Theorem BC checks passed").

## Change History

- 2026-10-22. Initial archive entry.
