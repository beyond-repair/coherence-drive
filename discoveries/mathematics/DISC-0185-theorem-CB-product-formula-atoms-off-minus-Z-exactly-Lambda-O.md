# Discovery: Theorem CB, closed product form of the corner resolvent and of 1/Q_∞; atoms of ν off −Z are exactly Λ_O

## Discovery ID

DISC-0185

## Status

THEOREM (mathematical sense only, as proved in the repository; partly computer-assisted). Method KNOWN-like (spectral-decimation product, Fukushima–Shima / Teplyaev type; identification not verified). Novelty of the explicit constants UNRESOLVED.

## Date Discovered

2026-10-29 (America/New_York), ~10:00am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 0d9944c015fb1ab192f9abe98096dfa8e1060b2c (pushed 2026-10-29 9:06am EDT).

## Original Evidence

GASKET.md Theorem CB (line 3277 onward; NOT THIS paragraph line 3319); CLAIM_STATUS.md new row; README.md summary paragraph; scripts/gasket_fractional_profile_product.py (364 lines); tests/test_cli.py (+20).

## Discovery

With the setting of DISC-0180/DISC-0182 (p(z)=z(z+5), c(z)=(z+6)/((z+2)(z+5)), e(z)=2z/(2+z), D=1/r_∞, ψ, Π, Z=ψ^−1(K_p)):

- CB.1: H_n=1/r_n−s/2 obeys H_(n+1)=c·H_n∘p, so 1/r_n(s)=(s/2)[1+(1+6/p^n(s))∏_(j<n)(p^j s+6)/(p^j s+2)] at every level.
- CB.2: 1/r_∞(z)=(z/2)(1+P(z)), P=∏_(j≥0)(p^j z+6)/(p^j z+2), meromorphic on ℂ∖K_p.
- CB.3: BZ.3's sum S equals Πψ/2, so 1/Q_∞=Π·(ψ/2)·P(ψ) on ℂ∖Z.
- CB.4: for u<0 off Z, f(u)=0 iff ψ(5^k u)=−3 for some k; atoms of ν in (0,∞)∖(−Z) are exactly Λ_O; no point of the −2 branch is an atom.
- CB.5: closed product form of each atom mass (e.g. ν({3.6152567198877…})=0.47964069292900347340…).

## Why It Matters

It replaces BZ's sum-plus-far-field formula by a single product, proves Conjecture CA.6 (DISC-0184) away from −Z, extends Kept Failure CA.5 (DISC-0183) from one point to the whole −2 branch, and gives the masses in closed form.

## Derivation

The key step is the identity c·p/2−e=z/2 (already re-derived for DISC-0182), which turns D=c·D∘p−e into the homogeneous law H=c·H∘p for H=D−z/2, together with c(w)p(w)/w=(w+6)/(w+2); telescoping gives CB.1 and, in the limit, CB.2. CB.3 follows by substituting CB.2 into BZ.3; CB.4 by reading off factor orders (on the −2 branch the zero of x_i+6 cancels the pole at x_(i−1)=−2, since p+6=(z+2)(z+3)); CB.5 by differentiating at a simple zero.

## Assumptions

As stated in the repository, not re-run there: AQ (1)–(3), BD.4, BJ.6, BS.1, BX.1–BX.2 (BX.1 rests on Assumption BX, the classical Stieltjes characterisation, see DISC-0177), BZ.1–BZ.4, CA.1–CA.2. No literature assumption.

## New Results

Relative to DISC-0182/0184: the converse of CA.2 holds off −Z. Still open: atoms on −Z and ν(−Z)=0 (pure point).

## Prior Art

Infinite-product formulas for resolvents/spectral functions under spectral decimation on the Sierpinski gasket are of a known type (Fukushima–Shima 1992; Teplyaev 1998); the repository itself says so ("no literature comparison made or used"). Identification of this exact corner-resolvent product in the literature not verified.

## Novelty Analysis

Mechanism is classical in kind. What may be specific: the exact constants, the corner vector, and the use of the product to settle the atom set off −Z. UNRESOLVED pending a literature check.

## Falsification Attempts

1. Repository witness: `python3 scripts/gasket_fractional_profile_product.py` at 0d9944c015fb1ab192f9abe98096dfa8e1060b2c, EXIT 0, 10.0 s, all CB checks pass.
2. Independent archive script /workspace/scratch-ifi/indep_theorem_CB.py (no repository code; copy at discoveries/mathematics/scripts/indep_theorem_CB.py):
   - sympy: H-law identity and c·p/z=(w+6)/(w+2) PASS; CB.1 closed form equals the recursion D_(n+1)=c·D_n∘p−e from D_0=3+z exactly for n=0..4 PASS.
   - CB.2 product versus the finite recursion at z=6, 1, 0.3, 2+i, −5.5: agreement 1e−35 to 1e−58. 1/r_∞(6)=7.76877219881627244576…, 1/r_∞(1)=2.35452252176188372890… (repo prints 7.7687721988162724457, truncated rather than rounded in the last digit; not an error in the claim).
   - CB.3/CB.4 via the finite-level route of DISC-0182 (f≈(5/3)^M D_(M+K)(5^−M u), M=110, no Π/S/product): |f(−λ_1)|=6e−53 at λ_1=3.6152567198877032728; f=2.197946759591264 at the ψ=−2 point u=−2.2421331852464538632; f=1.3187680557548 at ψ=(−5+√17)/2, u=−0.44842663704929077265. All match the repository.
   - CB.5: 1/f'(−λ_1)=0.4796406929290034734083466 by numerical differentiation of the independent route, all 25 printed digits equal the repository's mass.
   Nothing broke.

## Experimental Validation

Computational only (above). No physical experiment applies.

## Mathematical Status

Theorem (repository proof, partly computer-assisted; interval enclosures not re-certified here).

## Patent Relevance

None. The repository's NOT THIS paragraph: a resolvent on a graph, not a flux, not thrust; Stage 1 untouched.

## Related Discoveries

DISC-0182 (Theorem CA, the forward direction), DISC-0184 (Conjecture CA.6, now SPLIT), DISC-0183 (Kept Failure CA.5, extended), DISC-0180 (Theorem BZ, S now explicit), DISC-0177, DISC-0175.

## Open Questions

Atoms on −Z and ν(−Z)=0; accumulation at even-order critical points of ψ in Z; closed forms of ψ, F, G*, t_max, t_min; exact limsup/liminf ρ_k.

## Next Experiments

Use the product to test ν(−Z)=0 numerically: sum the CB.5 masses over enumerated Λ_O up to depth k and compare with m's total c_R(γ)/2; a deficit tending to 0 supports pure point. Literature match to Teplyaev 1998 remains the cheapest way to decide the −Z part.

## Reproduction Instructions

Clone beyond-repair/informational-flux-identity at 0d9944c015fb1ab192f9abe98096dfa8e1060b2c; `python3 scripts/gasket_fractional_profile_product.py` (~10 s, needs python-flint, sympy). Independent: `python3 indep_theorem_CB.py` (sympy, mpmath; ~2 s).

## Evidence Log

- 2026-10-29 ~10:00am EDT. Indexed; repo witness EXIT 0; independent check PASS.

## Change History

- 2026-10-29. Initial archive entry.
