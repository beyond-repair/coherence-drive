# Discovery: Theorem BJ, the ρ^−N cell modulus of Theorem BI is sharp (optimal Hölder exponent at the corners)

## Discovery ID

DISC-0153

## Status

THEOREM in the mathematical sense only (computer-assisted constants). Method KNOWN; constants novelty UNRESOLVED. Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~1:02am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 815003f22507fa34258d8b917a0e3a776340b16a (pushed 2026-10-23 12:29am EDT). Files: GASKET.md Theorem BJ (BJ.1–BJ.6), CLAIM_STATUS.md new row, README.md, scripts/gasket_fractional_corner_sharpness.py (new, 398 lines), scripts/cli.py, tests/test_cli.py.

## Original Evidence

- BJ.1: the AQ step is affine in the reciprocal, 1/r_(k+1)(s)=β(s)/r_k(ps)−e(s); with r_0=1/(3+z) and 1/r_∞=2+z−2η (BH.2), exactly 1/r_n(s)−1/r_∞(s)=∏_(i<n)β(p^i s)(1+2η(p^n s)) ∈ (0,3(3/5)^n].
- BJ.2: 1/(τ^(1−γ)/g(5^−nτ)+3) ≤ R_n(τ) ≤ τ^(γ−1)g(5^−nτ), g=s^(1−γ)r_∞.
- BJ.3: certified g ∈ [0.600945014,0.600963487] on (0,p(1e−12)] (arb, 160946 nodes plus two-sided p-orbit bootstrap); AU's ⟨Θ⟩=0.6009542511 lies inside.
- BJ.4: data-free corner deficit δ_N=κ_α∫τ^−α R(1−η_N(ψ(5^−Nτ))).
- BJ.5: ρ^N δ_N ≥ c_−(α)>0 for every N, α∈(γ,1); certified c_−(0.75)≥0.7282, c_−(0.8)≥0.6208, c_−(0.9)≥0.3630. With BI's upper bound (K_0.8/c_−≤75.88), ρ^−N is the exact order and the Hölder exponent (α−γ)/(1−γ) cannot be raised.
- BJ.6: liminf, limsup ρ^N δ_N(0.8) ∈ [1.135890346,1.135938783] (391460 arb cells).

## Discovery

Matching lower bound to DISC-0151: the modulus of continuity of the supercritical limit ū at the gasket corners is exactly of order ρ^−N = (3/5)^(N(α−γ)/(1−γ)), with a five-digit enclosure of the corner constant at α=0.8.

## Why It Matters

Settles the regularity question left by Theorem BI (Conjecture BI.7, items 1–2). It is a statement about one continuous function on the combinatorial gasket, not a field, flux or force; the repository says so explicitly ("Not thrust").

## Derivation

As in GASKET.md Theorem BJ. The key step is that the decimation map is a Möbius map whose reciprocal is affine, so the level-n defect against the fixed point telescopes into a product of β factors (each ≤3/5). The resolvent bracket then sandwiches the rescaled resistance between explicit functions of g, and the corner deficit integral is bounded below by an integral with no level dependence.

## Assumptions

Theorems AQ, BH (η enclosure), BI (upper bound and BI.4 bootstrap), AZ's A_0.8 as stated in the repository. The limit c_corner(α) existing is stated as derived from AT.1 and is not independently checked here.

## New Results

Conjecture BI.7 (DISC-0152) items 1–2 proved: DISC-0152 CONJECTURE → THEOREM for sharpness and optimal exponent; its rate item becomes Conjecture BJ.7 (DISC-0154).

## Prior Art

Optimal Hölder regularity at the resistance scale for harmonic-type functions on p.c.f. fractals and Möbius/renormalisation maps for the gasket resolvent are KNOWN techniques (Kigami; Strichartz; Teplyaev-type spectral decimation). The specific L^α Dirichlet extension and its constants were not searched.

## Novelty Analysis

Method KNOWN. Constants (g bracket, c_−, the 1.1359 band) novelty UNRESOLVED.

## Falsification Attempts

Archive script indep_theorem_BJ.py (own gasket graph, own η series, mpmath at 30 digits): BJ.1 identity at levels 0–6 and s∈{1e−5,…,40} holds to ≤5e−12 of 1/r_n, with 0<RHS≤3(3/5)^n; float g on one p-period from 1e−12 is in [0.6009469,0.6009616], inside the certified bracket, containing AU's ⟨Θ⟩; BJ.2 bracket holds for n=1..6, τ∈[1e−3,1e4]; K_0.8/c_− = 75.88 consistent. 6/6 PASS. No contradiction found. The arb enclosures (c_−, M_α integral) were not re-certified independently.

## Experimental Validation

Repo witness scripts/gasket_fractional_corner_sharpness.py (see Evidence Log). Repo floats ρ^Nδ_N^(100)=1.135914525 (N=10), 1.135914308 (N=20), inside the certified band.

## Mathematical Status

Theorem (computer-assisted constants).

## Patent Relevance

None.

## Related Discoveries

DISC-0151 → DISC-0153 (mathematical: matching lower bound); DISC-0149 → DISC-0153 (computational: η enclosure, r_∞ formula); DISC-0106 → DISC-0153 (mathematical: AQ step); DISC-0153 → DISC-0152 (proves sharpness, CONJECTURE → THEOREM); DISC-0153 → DISC-0154 (rate conjecture).

## Open Questions

Closed form for c_corner(α); a rate for u_n→ū (DISC-0154); a continuum equation for ū.

## Next Experiments

Independent arb re-certification of c_−(0.8)≥0.6208 and the [12.104976020,12.105120109] integral.

## Reproduction Instructions

git -C informational-flux-identity checkout 815003f22507fa34258d8b917a0e3a776340b16a; python3 scripts/gasket_fractional_corner_sharpness.py (needs sympy, mpmath, python-flint). Archive: python3 indep_theorem_BJ.py (~3 min).

## Evidence Log

- 2026-10-23 ~1:02am EDT. Repo witness: EXIT 0 (22 ok, 358 s; /workspace/scratch-ifi/repo_theorem_BJ.log). Archive /workspace/scratch-ifi/indep_theorem_BJ.py 6/6 PASS.

## Change History

- 2026-10-23. Initial archive entry.
