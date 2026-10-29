# Discovery: Theorem BZ, Q_∞ continues meromorphically off a Lebesgue-null Julia-type set, so BX's spectral measure has no absolutely continuous part; 311 certified atoms per period; ρ_k has no limit

## Discovery ID

DISC-0180

## Status

THEOREM in the mathematical sense only (repository proof plus a computer-assisted arb/acb certificate). Method KNOWN (quadratic-polynomial Julia set, spectral decimation, Stieltjes inversion, Dirichlet simultaneous approximation). Constants and atom locations: novelty UNRESOLVED (not searched). Whether ν is pure point: open in the repository; prior-art lead recorded below. Not thrust.

## Date Discovered

2026-10-29 (America/New_York), ~6:01am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit f9942d98a5fa5e535f07b83e6362bde6344af6f0 (committed 2026-10-29 5:30am EDT).

## Original Evidence

GASKET.md Theorem BZ (heading line 3181; Kept Failure BZ.6 line 3212; Kept Failure BZ.5 line 3214; What stays open line 3218; Remark line 3222; NOT THIS line 3224; witness paragraph line 3226), CLAIM_STATUS.md new row (line 82), README.md (line 1140), scripts/gasket_fractional_profile_atoms.py (new, 356 lines), scripts/cli.py, tests/test_cli.py.

## Discovery

Setting as in DISC-0177 (Theorem BX): p(z)=z(z+5), c(z)=(z+6)/((z+2)(z+5)), e(z)=2z/(2+z), D=1/r_∞, ψ(v)=lim p^k(5^−k v), Q_∞(u)=∫dν(λ)/(λ+u) with ν(5A)=3ν(A), m=λ^−γ ν periodic in t=log_5 λ, m(T)=c_R(γ)/2, ρ_k=|m̂_k|/m̂_0.

- BZ.1: p+5/2=(z+5/2)²−15/4; the filled Julia set K_p is a Cantor subset of [−5,0] of Lebesgue measure 0.
- BZ.2: D(z)=c(z)D(p(z))−e(z); r_∞ is meromorphic on C∖K_p.
- BZ.3: 1/Q_∞(u)=Π(u)D(ψ(u))−S(u), Π=∏_(j≥1)(5/3)c(ψ(5^−j u)), S=Σ_k(5/3)^k e(ψ(5^−k u))Π(5^−k u); Q_∞ continues meromorphically to C∖Z, Z=ψ^−1(K_p) closed, null, 5Z=Z.
- BZ.4: ν (and m) has no absolutely continuous part.
- BZ.5: 311 certified atoms in (1,5) (largest λ=3.615256719887703… with ν({λ})=0.479640692929…); they carry all of m(T) except δ≤4.03e−5.
- BZ.6: limsup ρ_k≥1−2δ/m(T)≥0.99968 and liminf ρ_k≤(|a_35^cert|+δ)/m(T)≤0.59497, so ρ_k has no limit; limsup|θ̂_k|e^(2π²k/ln5)∈[1.00918,1.0094980205] (BX.3's bound attained to 3.2e−4); F continues to no strip wider than |Im t|<π/ln5.
- Kept Failure BZ.6 decides Conjecture BV.6 (DISC-0175): asymptotic part false, sharp-rate and maximal-strip parts true.
- Kept Failure BZ.5: (a) ν absolutely continuous, false (DISC-0181); (b) ν carried by ≤310 geometric series, false (DISC-0178's hypothesis widened, stays REJECTED).
- Remark (derived): T_n≻0 for every n≤311, which settles BY's open T_21 (DISC-0179).

## Why It Matters

It changes the route: instead of the Toeplitz certificates that were stalling (DISC-0179), the decimation itself gives the structure of the spectral measure. It decides the repository's open Conjecture BV.6 (one part false, two parts true) and explains why the certified band [0.60,0.92] for ρ_k, k≤21, was not a long-run range.

## Derivation

Repository proof (GASKET.md lines 3204–3210, "Proof" paragraph): BZ.1 by conjugacy to ζ²−15/4 and contraction of the inverse branches (|g'|≤1/√5); BZ.2 by Vitali and unrolling the fixed point until |p^N z|>144; BZ.3 by telescoping X_k=(5/3)^k D(x_k) along x_j=ψ(5^−j u) and a squeeze for u>0, then analytic continuation; BZ.4 by Stieltjes inversion across intervals of (−∞,0)∖Z (simple poles from |Q_∞(x+iy)|=O(1/|y|)); BZ.5 by an outward arb/acb enclosure of 1/Q_∞ via BZ.3 with sign change plus a Cauchy-estimate enclosure of the derivative; BZ.6 by Bohr almost periodicity of the atomic coefficients a_k and Dirichlet's theorem, with |m̂_k−a_k|≤m_c(T)=δ.

I checked the BZ.6 inequality chain by hand: |m̂_τ|≥a_0−ε−δ=m(T)−2δ−ε for arbitrarily large τ, and |m̂_(35+τ)|≤|a_35|+ε+δ, so the two printed bounds follow from δ and |a_35^cert| alone. 1−2·4.03e−5/0.2585829=0.9996883; 0.59481+4.03e−5/0.2585829=0.5949658≤0.59497; 1.0094980205×0.9996883=1.0091834≥1.00918. All consistent and rounded in the safe direction.

## Assumptions

As stated in the repository and not re-run there: AQ (1)–(3), BD.4, BJ.6, BS.1, BX.1–BX.3 (BX.1 itself rests on Assumption BX, the classical Nevanlinna/Stieltjes characterisation, see DISC-0177); BW's digits and BY's ρ_1..ρ_5 for consistency only. No new literature assumption. The sentence in BZ.3 that 1/𝓡=Π(3+ψ)−S is entire-meromorphic is algebra on stated results and is flagged by the repository as not re-run.

## New Results

- Conjecture BV.6 (DISC-0175) decided: "ρ_k converges" is false; the rate e^(−2π²k/ln5) is exact along a subsequence; the strip |Im t|<π/ln5 is maximal.
- ν singular; at least 311 atoms per scale period; the six largest carry about 98% of m (repository observation).
- T_n≻0 for n≤311 (closes DISC-0179's open T_21; my float λ_min(T_21)≈2.1e−27>0 recorded there agrees).
- θ̂_k≠0 for infinitely many k (ρ_k≥0.9996 infinitely often), not yet for every k.

## Prior Art

- Spectral decimation for the Sierpinski gasket (Rammal–Toulouse 1983; Fukushima–Shima 1992) gives exactly this structure: eigenvalues via the inverse branches of λ↦λ(5−λ) (here p(z)=z(z+5) with z=−λ), exceptional values at 2 and 5 (the poles of c here), and a Julia-set (Cantor) part of the spectrum. Method KNOWN.
- Teplyaev, "Spectral Analysis on Infinite Sierpiński Gaskets", J. Funct. Anal. 159 (1998) 537–567, https://doi.org/10.1006/jfan.1998.3297: the Neumann Laplacian on the infinite gasket with one boundary point has pure point spectrum with complete compactly supported eigenfunctions; false for the Dirichlet condition. Teplyaev's 2022 survey (https://alexander-teplyaev.uconn.edu/wp-content/uploads/sites/1703/2022/05/teplyaev-2022-IHP.pdf) also mentions a singularly continuous component supported on the preimage of the Julia set in some infinite-gasket settings. If Q_∞ is the corner spectral function of one of these blow-up Laplacians (plausible from the construction, NOT verified here: the boundary condition and the vector v must be matched), the repository's open question "ν(−Z)=0, i.e. pure point" may already be answered in the literature, either way depending on the setting. This is the most important remaining prior-art item.
- Log-periodic oscillation in fractal spectral asymptotics (Kigami–Lapidus 1993; Grabner–Woess 1997 for Sierpinski graphs) is KNOWN in general; the specific non-convergence of ρ_k and its constants were not searched.

## Novelty Analysis

Method KNOWN. The singularity of the spectral measure is consistent with (and may be implied by) the cited infinite-gasket literature once the identification is made. The certified atoms, the mass bound δ≤4.03e−5 and the ρ_k limsup/liminf constants: novelty UNRESOLVED (not searched).

## Falsification Attempts

1. Repo witness, fresh clone at f9942d98a5fa5e535f07b83e6362bde6344af6f0 on the box: `python3 scripts/gasket_fractional_profile_atoms.py` EXIT 0 in 123 s ("all Theorem BZ checks passed"; prints limsup ρ_k≥0.99968837, liminf ρ_k≤0.59496047 from k=35; atom λ=[3.61525671988770 ± 3.28e−15], ν=[0.4796406929 ± 2.91e−11]). Log: /workspace/scratch-ifi/repo_theorem_BZ.log.
2. Independent route, /workspace/scratch-ifi/indep_theorem_BZ.py (no repo code, does NOT use the Π/S formula): 1/Q_∞(u)≈(5/3)^M D_(M+K)(5^−M u) by the finite fixed-point recursion with D_0=3+z, M=40 and 60, K=12, mpmath 80 digits. The three largest printed atoms and masses are reproduced: |Δλ|≤4.3e−16 and |Δν|≤2.2e−14 (the printed digits). The three carry 94.8% of m(T). PASS. (An earlier attempt with K=0, i.e. r_M instead of r_∞, found no zero near 3.615; that was my error, not the repository's: Q_∞ is built from r_∞.)
3. Independent coarse scan, /workspace/scratch-ifi/indep_theorem_BZ_scan.py (float64 grid of 400000 cells, mpmath refinement, not interval-certified): 10 atoms capturing m(T) up to 4.2e−3. Even this weaker atom set reproduces the dichotomy on its own: argmin_(k≤100)|a_k| is again k=35 with |a_35|/m(T)=0.5862, so liminf ρ_k≤0.6025<0.9675≤limsup ρ_k; ρ_1 from these atoms is 0.766 against the certified 0.76964 (within the uncaptured mass). So Kept Failure BZ.6 survives an independent, non-certified attack. m(T) was taken from BX.2 in both of my scripts.
4. Logical attack on BZ.6: the argument needs only δ, a_0 and one |a_k|; the almost periodicity of a finite atomic sum and Dirichlet's theorem are standard. No gap found.

Not broken.

## Experimental Validation

Not applicable (pure mathematics on a graph). Computational as above. Repo reports pytest -k "not reproduce": 39 passed (not re-run here).

## Mathematical Status

Theorem (repository proof) with computer-assisted certified constants (interval enclosures not re-certified here; three leading atoms reproduced by an independent finite-level route).

## Patent Relevance

None. The repository's NOT THIS fence: atoms of a spectral measure are not a flux and not a force; Stage 1 untouched; no W, 0.08, 0.23 or 30 μN/kW.

## Related Discoveries

DISC-0175 (Conjecture BV.6: asymptotic part REJECTED, sharp-rate and maximal-strip parts proved here), DISC-0177 (Theorem BX; ν singular answers part of its open "purely atomic" question), DISC-0178 (Kept Failure BX.5; r≤310 now, stays REJECTED), DISC-0179 (Theorem BY; T_21 settled by the Remark), DISC-0181 (Kept Failure BZ.5(a): ν not absolutely continuous), DISC-0173 (strip of holomorphy now maximal), DISC-0116 (Theorem AU).

## Open Questions

ν(−Z)=0 (pure point)? Infinitely many atoms per period? Exact limsup ρ_k (=1 if pure point) and liminf ρ_k? θ̂_k≠0 for every k≥22? Closed forms of the atoms (λ_1=3.6152567…, λ_2=1.1719102…), of F, G*, t_max, t_min. Identification of Q_∞ with Teplyaev's Neumann or Dirichlet infinite-gasket corner spectral function.

## Next Experiments

Match AQ's corner resolvent r_n=½v^T(L_n+s)^−1v to Teplyaev's setting (boundary condition, vector) and check whether his pure-point theorem applies to the corner vector. Check whether the certified atoms λ_j are 5^n-renormalised limits of the exceptional eigenvalue series born at 2, 5 (poles of c) and 6 (the repository's "6-series"); that would give closed-form atom locations.

## Reproduction Instructions

```
git clone https://github.com/beyond-repair/informational-flux-identity
git -C informational-flux-identity checkout f9942d98a5fa5e535f07b83e6362bde6344af6f0
cd informational-flux-identity && python3 scripts/gasket_fractional_profile_atoms.py   # needs python-flint, sympy; ~2 min
```

## Evidence Log

- 2026-10-29 ~6:01am EDT. Indexed; repo witness EXIT 0 (123 s); independent finite-level reproduction of the three leading atoms PASS; independent coarse scan reproduces the BZ.6 dichotomy. No erratum. Presentation note: GASKET.md's original Conjecture BV.6 text (in the Theorem BV section, around line 3019 at cec4aff731ce) is not annotated in place as decided; the decision is recorded in Theorem BZ and CLAIM_STATUS.md line 82. Not a contradiction (the file is append-only by convention).

## Change History

- 2026-10-29. Initial archive entry.
