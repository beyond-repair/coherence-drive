# Discovery: Theorem BD, exact identity e_n=(2−t_n)y_n proves E_n/Y_n→2 on the frozen 0.45 gasket, with a certified α-dependent 3^−n constant

## Discovery ID

DISC-0138

## Status

THEOREM in the mathematical sense only (complete proof in the repository, verified here). Method KNOWN (Stieltjes/spectral representation of resolvent entries, decimation recursions, interval enclosures). Novelty of the constants c(α) UNRESOLVED. Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~6:05pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 30bee3aab038a818c28144ef7d9787eaccdedf5a. Paths: README.md "Theorem BD" (BD.1–BD.4, Kept Failure BD.1, Conjecture BD.2, NOT THIS), CLAIM_STATUS.md new Theorem BD row, GASKET.md Stage 2 OPEN item, scripts/mesh_noncentrality_limit.py (new, 354 lines), scripts/cli.py, tests/test_cli.py (test_theorem_bd_noncentrality_limit).

## Original Evidence

Quoted from README Theorem BD and CLAIM_STATUS at 30bee3aab038; archive-only numbers are labelled.

## Discovery

For s>0 on the level-n gasket, with y_n(s)=[(L_n+s)^−1]_{p'c'}−[(L_n+s)^−1]_{p'c''}, e_n(s)=s g_n(s), t_n(s)=s[(L_n+s)^−1 1_C]_c:

1. Exact identity e_n(s)=(2−t_n(s))y_n(s) for every n and s (induction on BB/BC recursions, base Q_0=1).
2. t_n(s)=(1/3)Σ_λ‖P_λ1_C‖² s/(λ+s), increasing and concave, t_n(0+)=2/(3^n+1), t_n'(0)=3^n(5^n−1)/(6(3^n+1)²), t_n<1.
3. Hence 1<E_n/Y_n<2·3^n/(3^n+1), κ^cross_n=2^n(4/R_n²)Y_n(1+d_n)>0 at every level and every α, tanθ_n=−1/(3√3)−4d_n/(3√3(3−d_n)) from below, and for n≥2, 2/(3^n+1)<2−E_n/Y_n≤2/(3^n+1)+B_α3^−n with B_0.45=115.196453544…. So E_n/Y_n→2 and tanθ_n→−1/(3√3) for every α∈(0,1): Conjecture BC.2 (DISC-0137) is proved.
4. c(α)=lim 3^n(2−E_n/Y_n) exists, 2<c≤2+B_α; certified c(0.45)∈[3.72198897,3.72914181], c(0.8)∈[2.57126273,2.57352573].

## Why It Matters

Closes DISC-0137 and extends DISC-0133's "self-force-removed residual is nonzero" from certified levels 1–4 to every level. The non-centrality angle of the corner-cell pair force is a geometric constant arctan(1/(3√3))=10.893395° independent of α. Not a force on a device.

## Derivation

Repository proof, checked: BD.1 is the one-line algebraic induction (6+s)(2−t)/(6+s−2t)=2−(2+s)t/(6+s−2t); BD.2 uses S3 transitivity on the corners so P_λ1_C is constant on C; the λ=0 term is 3/N_n=2/(3^n+1); BD.3/BD.4 integrate against s^−α y_n ds and pass to scaling limits T_n(τ)=3^n t_n(5^−nτ)↑T, 3^n y_n(5^−nτ)→𝒴 with dominated convergence; constants by mpmath.iv outward Riemann bounds (13485 cells, explicit tails).

## Assumptions

Assumption BA/BC (Maxwell-form reading, corner-cell gradient, Green kernel); combinatorial Laplacian of the gasket graph; α∈(0,1).

## New Results

Every level has κ^cross_n>0; rate 2−E_n/Y_n=Θ(3^−n) with α-dependent constant.

## Prior Art

Spectral decimation on the Sierpinski gasket (Fukushima–Shima, Strichartz) and Stieltjes representations of resolvent entries are standard. Constants c(α) not searched.

## Novelty Analysis

Method KNOWN. Constants specific to this repository's construction; novelty UNRESOLVED.

## Falsification Attempts

Archive independent float attack (/workspace/scratch-ifi/indep_theorem_BD.py, own gasket builder sg_indep_common.py, no repository code), 45/45 PASS: identity e_n=(2−t_n)y_n and e_n=s g_n at seven s values, n=1..5 (max rel err 1.2e−10); spectral formula with the 1/3 factor; t_n(0+)=2/(3^n+1) and t_n'(0) closed form exact to 1e−8, n=1..5; t_n increasing and <1 on a 400-point log grid; pointwise e/y≤2·3^n/(3^n+1); for α=0.45 and 0.8 at n=2..7 (N up to 3282, dense fractional pseudo-inverse), 1<E/Y<2·3^n/(3^n+1), 2−E/Y>2/(3^n+1), Y>0; tanθ_2 from the BD formula matches BC's certified −0.277452251033554 to 1e−10; 3^n(2−E/Y) at n=5..7 is 3.66686, 3.70597, 3.71905 (0.45) and 2.54942, 2.56476, 2.56985 (0.8), increasing, with Aitken extrapolation 3.725636 and 2.572380 inside the certified brackets. No counterexample found.

## Experimental Validation

Repository witness plus archive floats. Interval certification rests on the repository witness.

## Mathematical Status

Theorem (repository proof, archive float verification).

## Patent Relevance

None. Not thrust.

## Related Discoveries

- DISC-0138 → DISC-0137 (mathematical): proves Conjecture BC.2, status CONJECTURE → THEOREM.
- DISC-0138 → DISC-0133 (mathematical): κ^cross_n>0 at every level.
- DISC-0135 → DISC-0138, DISC-0132 → DISC-0138 (mathematical): uses BC's kernel and BB's recursions.
- DISC-0138 → DISC-0139 (failed hypothesis), DISC-0138 → DISC-0140 (mathematical).

## Open Questions

Monotonicity and closed form of c(α) (Conjecture BD.2, DISC-0140).

## Next Experiments

Independent interval enclosure of c(α) at several α; test c(1^−)=2.

## Reproduction Instructions

Repository: `cd informational-flux-identity && git checkout 30bee3a && python3 scripts/mesh_noncentrality_limit.py` (log /workspace/scratch-ifi/repo_BD_run.log). Archive: `cd /workspace/scratch-ifi && python3 indep_theorem_BD.py` (about 160 s; log indep_theorem_BD.log).

## Evidence Log

- 2026-10-22 ~6:05pm EDT. Recorded from IFI 30bee3aab038a818c28144ef7d9787eaccdedf5a. Archive 45/45 PASS as above. Repository witness scripts/mesh_noncentrality_limit.py EXIT 0 (351 s, 25 ok, "all Theorem BD checks passed; nothing here is thrust"). Interval certification of c(0.45), c(0.8) and of E_n/Y_n at levels 1–3 rests on that witness, not re-certified independently.

## Change History

- 2026-10-22. Initial archive entry.
