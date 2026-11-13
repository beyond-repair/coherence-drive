# Discovery: Theorem BE, the 3^−n non-centrality constant c(α) is strictly decreasing on (0,1), with c(1^−)=2 (certified slope) and a finite certified c(0^+)

## Discovery ID

DISC-0141

## Status

THEOREM in the mathematical sense only (complete proof in the repository, verified here). Method KNOWN (exponential-tilt / monotone-likelihood-ratio ordering, i.e. the Chebyshev-type covariance inequality for the family x^−α m(dx); dominated convergence; interval enclosures). Novelty of the constants 3S and c(0^+) UNRESOLVED. Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~7:15pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 3b3ec0fef920f85fa1098074e22ee3bdafe73a26 (2026-10-22 18:16 EDT). Paths: README.md "Theorem BE" (BE.1–BE.4, Kept Failure BE.1, Conjecture BE.2, NOT THIS), CLAIM_STATUS.md new Theorem BE row and edited Theorem BD row, GASKET.md Stage 2 OPEN item, scripts/mesh_noncentrality_monotone.py (new, 178 lines, imports mesh_noncentrality_limit), scripts/cli.py, tests/test_cli.py (test_theorem_be_monotone_constant).

## Original Evidence

Quoted from README Theorem BE and CLAIM_STATUS at 3b3ec0fef920; archive-only numbers are labelled.

## Discovery

Notation of Theorem BD (DISC-0138): d_n(α)=2−E_n/Y_n=⟨t_n⟩ under s^−α y_n(s) ds; T, 𝒴 the scaling limits of 3^n t_n(5^−nτ), 3^n y_n(5^−nτ); c(α)=∫τ^−α T𝒴/∫τ^−α 𝒴.

1. Tilt identity: for a positive measure m and nondecreasing f, Z_αZ_β(⟨f⟩_α−⟨f⟩_β)=(1/2)∬(f(x)−f(y))(x^−αy^−β−x^−βy^−α) m(dx)m(dy)≥0 for α<β, the kernel (xy)^−α(y^(α−β)−x^(α−β)) having the sign of x−y; strict unless f is m-a.e. constant.
2. BE.1: d_n(α) strictly decreasing in α at every level n≥1 (m=y_n ds, f=t_n strictly increasing Stieltjes), so E_n/Y_n and tanθ_n strictly increase with α.
3. BE.2: c(α) strictly decreasing on (0,1) (m=𝒴 dτ, f=T nondecreasing and non-constant: T(0^+)=2, T≥T_1=2+(τ−10)/(20+τ)>2 for τ>10).
4. BE.3: c(1^−)=2 (B_α=O(1−α), J_1=(125/4)ln5), and (c(α)−2)/(1−α)→3S, S=∫(T−2)𝒴 dτ/τ, certified 3S∈[2.70632481,2.70903118] (S∈[0.9021082713,0.9030103931], 12903 cells).
5. BE.4: c(0^+)=c_0=∫T𝒴/∫𝒴 finite, certified c_0∈[5.48553067,5.50249013] (13485 cells); sup over (0,1) of c is c_0.

## Why It Matters

Decides Conjecture BD.2 (DISC-0140) in part: the monotone direction and the endpoint at 1 are proved; the endpoint guess c(0^+)=∞ is refuted (DISC-0142). The finite-level non-centrality of the corner-cell pair force is smaller at larger α. A refinement-rate statement, not a force on a device.

## Derivation

Repository proof, checked: the identity is the symmetrisation of ∬f(x)(x^−αy^−β−x^−βy^−α) (expand Z_αZ_β⟨f⟩_α−Z_αZ_β⟨f⟩_β); BE.1 uses BD.2 (t_n strictly increasing, y_n>0); BE.2 uses T as a monotone limit of the nondecreasing T_n with BD.4's dominations; BE.3 splits c−2=N/D, N→S by dominated convergence ((T−2)/τ≤1/6), (1−α)D→1/3 from 1/3−Cτ≤𝒴≤1/3 near 0; the S certificate uses concavity of T (so (T−2)/τ nonincreasing) and 𝒴 nonincreasing for outward endpoint bounds; BE.4 is dominated convergence with 𝒴≤τ/(3ψ_6(τ)) decaying faster than any power, certificate = BD.4's enclosure at α=0.

## Assumptions

Assumption BA/BC (Maxwell-form reading, corner-cell gradient, Green kernel), combinatorial Laplacian of the gasket graph, α∈(0,1); BD.2–BD.4 (DISC-0138).

## New Results

Strict monotonicity of d_n(α) and c(α) in α; c(1^−)=2 with slope −3S; finite c(0^+).

## Prior Art

The tilt/likelihood-ratio ordering is classical (Chebyshev's sum/covariance inequality; monotone likelihood ratio families, Karlin). Spectral decimation on the Sierpinski gasket (Fukushima–Shima, Strichartz) as in DISC-0138. Constants 3S, c_0 not searched.

## Novelty Analysis

Method KNOWN. Constants specific to this repository's construction; novelty UNRESOLVED.

## Falsification Attempts

Archive independent attack /workspace/scratch-ifi/indep_theorem_BE.py (own gasket builder sg_indep_common.py and an own cell-gluing Schur-complement recursion for (L_n+s)^−1 on {c,c′,c″,p′} in mpmath; no IFI code imported, no spectral decimation), final run 30/30 PASS (indep_theorem_BE.log, 116 s):
- tilt identity exact in sympy on a symbolic 3-atom measure (x_i^−α, x_i^−β as independent symbols) and the kernel factorisation; 2000 random discrete measures, identity to 3.8e−14 and LHS≥0 for nondecreasing f; a permuted (non-monotone) f gives a negative difference (sanity); continuous toy m=e^−x dx, f=x gives ⟨x⟩_α=1−α;
- J_α closed form vs direct integral at α=0.45 (830.97552556), J_1=(125/4)ln5, αJ_α→3125;
- dense pseudo-inverse L^−α, n=1..7 (N up to 3282): d_n(α) strictly decreasing on the 19-point grid α=0.05..0.95 and >2/(3^n+1);
- recursion = dense resolvent (y,e,t) n=1..5 to 6.1e−11; recursion moments = dense d_n at n=1,2,4 to ≤8.8e−10;
- 3^n d_n(α) at n=16,20,24 on α∈{0,0.02,0.05,0.1,0.25,0.45,0.65,0.8,0.9,0.95,0.98,0.99} strictly decreasing; n=20 vs 24 agree to 8.7e−9; c(0)≈5.494003464, c(0.25)≈4.471972512, c(0.45)≈3.725563357, c(0.8)≈2.57242943, all inside the repository's certified brackets (and BD's); 3S≈2.70767738 inside [2.70632481,2.70903118]; 3^24 y_24(0^+)=0.3333333333; (c−2)/(1−α)=2.78457, 2.74603, 2.72300, 2.71533 at α=0.9, 0.95, 0.98, 0.99, approaching 3S; c(0.99)−2=0.02715.
Earlier archive runs kept: run1 killed (sympy simplify too slow), run2 26/27 and run3 28/30 with archive tolerance/truncation errors only (indep_theorem_BE.run1/2/3.log). No counterexample to any claim of Theorem BE.

Minor discrepancy (uncertified floats only): the repository's printed float d_n(0.95) is off by 1.2e−5, 2.6e−5, 4.6e−5 relative at n=1, 2, 4 (dense 0.50981193 vs printed 0.5098179 at n=1; two independent archive methods agree with each other to 3e−13), and its 3^20 d_20(0.95)=2.13767827 vs archive 2.1373016 (1.8e−4), so the README float secant −2.8983 (0.8→0.95) is −2.90085 in the archive. All other printed alphas agree to ≤1.5e−8. This is a quadrature inaccuracy in the repository's float table near α→1; it does not touch BE.1–BE.4 (strict-ordering gaps are ≥10^−2) or the certified enclosures.

## Experimental Validation

Repository witness plus archive floats. Interval certification of 3S and c(0^+) rests on the repository witness, not re-certified independently.

## Mathematical Status

Theorem (repository proof, archive float verification).

## Patent Relevance

None. Not thrust.

## Related Discoveries

- DISC-0138 → DISC-0141 (mathematical): uses BD.2's Stieltjes t_n and BD.4's scaling limits.
- DISC-0141 → DISC-0140 (mathematical): decides Conjecture BD.2 in part (decrease and c(1^−)=2 proved).
- DISC-0141 → DISC-0142 (failed hypothesis): c(0^+)=∞ false.
- DISC-0141 → DISC-0143 (mathematical): Conjecture BE.2, convexity.

## Open Questions

Closed forms for T, 𝒴, c, S, c_0; convexity of c (DISC-0143).

## Next Experiments

Independent interval enclosure of S and c_0; interval check of the secant ordering for BE.2.

## Reproduction Instructions

Repository: `cd informational-flux-identity && git checkout 3b3ec0f && python3 scripts/mesh_noncentrality_monotone.py` (log /workspace/scratch-ifi/repo_BE_run.log); `python3 -m pytest -q tests/test_cli.py -k "theorem_be or noncentrality"`. Archive: `cd /workspace/scratch-ifi && python3 indep_theorem_BE.py` (about 2 min; log indep_theorem_BE.log).

## Evidence Log

- 2026-10-22 ~7:15pm EDT. Recorded from IFI 3b3ec0fef920f85fa1098074e22ee3bdafe73a26. Repository witness scripts/mesh_noncentrality_monotone.py EXIT 0 (294.6 s, 12 ok, 0 FAIL, "all Theorem BE checks passed; nothing here is thrust"); tests/test_cli.py -k "theorem_be or noncentrality" 3 passed (67.9 s). Archive 30/30 PASS as above.

## Change History

- 2026-10-22. Initial archive entry.
