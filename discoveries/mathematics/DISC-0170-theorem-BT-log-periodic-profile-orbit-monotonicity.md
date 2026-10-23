# Discovery: Theorem BT, s^(1−γ)r_∞ is nondecreasing backwards along every p-orbit, so the log-periodic profile u^(1−γ)Q_∞ of Theorem BS equals AT.1's Θ∘ψ, is continuous, has AU's mean, and its maximum is the sharp constant sup s^(1−γ)r_∞ ∈ [0.6009615785, 0.6009631774]

## Discovery ID

DISC-0170

## Status

THEOREM in the mathematical sense only (repository proof; extremes and mean computer-assisted with python-flint arb). Method KNOWN (monotone orbit limits of a renormalisation map, Stieltjes comparison, interval cell bounds for monotone functions). Log-periodic oscillation of renormalised resolvent/Green-function quantities on the Sierpinski gasket is KNOWN in kind; this specific profile, its extremes and its closed form: novelty UNRESOLVED, closed form UNRESOLVED. Its Kept Failure BT.5 (the profile is not constant) is the same hypothesis already REJECTED as DISC-0114 (AT.1), now with a certified pointwise witness; recorded as a note on DISC-0114, not as a new ID. Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~5:01pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 48a561c16bce15b0a0992015fa063d5311ebd5d5 (committed 2026-10-23 4:10pm EDT).

## Original Evidence

GASKET.md Theorem BT (heading line 2867; Kept Failure BT.5 line 2896; proofs of BT.1–BT.4 lines 2898, 2900, 2902, 2904; "What stays open" line 2908; NOT-THIS fence line 2913; witness list line 2915), CLAIM_STATUS.md new row (line 76), README.md reproduction list, scripts/gasket_fractional_log_periodic_profile.py (new, 300 lines), scripts/cli.py, tests/test_cli.py.

## Discovery

Setting (as in AQ, AT, AU, BD, BJ, BS): p(s)=s(s+5), q=p^−1, γ=log3/log5, g(s)=s^(1−γ)r_∞(s), Q_∞(u)=lim(3/5)^M r_∞(5^−M u) (BS.1), F(u)=u^(1−γ)Q_∞(u), ψ(v)=lim p^k(5^−k v) (BD.4), Θ(s)=lim_k g(q^k s).

- BT.1 (every s>0): g(s)/g(p(s))=(5+s)^γ(2+s)/(6+s−2p(s)r_∞(p(s))) ∈ [1, (5+s)^γ(2+s)/(6+s−2Gp^γ)], the floor from 5^γ=3 and 3(2+s)−(6+s)=2s. So g(q^k s) is nondecreasing in k, Θ=sup_k g(q^k s) exists everywhere, Θ∘q=Θ, and g≤Θ≤g·e^E with E(s)≤s/4+(G/3)6^γ s^γ for s≤10^−3.
- BT.2: F(u)=Θ(ψ(u)) for every u (no AT.1 limit input), F(5u)=F(u), F continuous, and e^(−γv/10)≤F(v)/g(v)≤e^((1−γ)v/10+Y/4+(G/3)6^γY^γ), Y=ve^(v/10), v≤10^−3. Consequently the hypothesis of Theorem BS's derived paragraph holds and c_∞(α)=θ_∞^BH(α) with BH.6 as stated.
- BT.3: sup_(s>0) g = max F (BI.4's constant G is sharp at G*=max F); ⟨F⟩=⟨Θ⟩ (AU's mean).
- BT.4 (certified, outward): max F ∈ [0.6009615785, 0.6009631774] (node u=5^(98534/2^17)), min F ∈ [0.6009453250, 0.6009469238] (node u=5^(32998/2^17)), ⟨F⟩ ∈ [0.6009530801, 0.6009554223] ∋ AU's ⟨Θ⟩=0.6009542511; sup s^(1−γ)r_∞ ≤ 0.6009631774 (vs BI.4's 0.6031).
- Kept Failure BT.5: F is not constant (max F − min F ≥ 1.465480e−5), i.e. Q_∞ ≠ C u^(γ−1); BS's float evidence used that approximation, its certified brackets did not.

## Why It Matters

Theorem BS (DISC-0168) reduced c_∞, C_N, P_N, χ_∞ to one unknown log-periodic function F and identified c_∞ with BH's far-field constant only under AT.1. BT proves that identification unconditionally, gives F a pointwise-computable description (one r_∞ value at 5^−M u, error O(s^γ)), and makes BI.4's constant sharp. It does not give a closed form.

## Derivation

Repository proof (GASKET.md lines 2898–2904), checked here step by step: the orbit ratio follows from AQ (3) and s/p(s)=1/(5+s); the floor uses X>0, (5+s)^γ≥3; the rate sums the ceiling along q^k s≤5^−k s with Σ5^−k=1/4 and Σ3^−k=1/2; identification uses BN.1's comparison (w/w′)^γ≤g(w′)/g(w)≤(w′/w)^(1−γ) and q^M(ψ(u))=ψ(5^−M u); the mean equality compares ∫Θ ds/s and ∫F ds/s over one period at small u.

## Assumptions

As stated in the repository and not re-run there: AQ (3), BN.1, BI.4 (G=0.6031), BJ.1, BH.2, BD.4 with BJ.6, BS.1. AT.1's eight values, AU's ⟨Θ⟩ and |θ̂_2| floor, and BJ.3's bracket are used for consistency only.

## New Results

- c_∞=θ_∞^BH is now unconditional (given BH.6), so DISC-0150's value θ_∞(0.45)≈0.52061 lies in BR.5's certified [0.520386, 0.520825] at theorem level; DISC-0150's O(3^−k) rate clause is not addressed.
- ⟨F⟩=⟨Θ⟩ links BS's profile to AU's (DISC-0116) mean.

## Prior Art

Log-periodic oscillations in Green-function and spectral asymptotics on the Sierpinski gasket and graph are KNOWN in kind (for example Grabner–Woess 1997 on functional iterations and periodic oscillations for random walk on the Sierpinski graph; Kigami–Lapidus 1993 on log-periodic spectral counting). Monotone limits along renormalisation orbits are standard. No prior-art search for this function or these constants was done in this slice.

## Novelty Analysis

The method is KNOWN. The specific orbit-monotonicity floor for this corner resolvent, the sharp constant G* and its certified bracket have no located prior statement, but none was searched; novelty UNRESOLVED. No closed form.

## Falsification Attempts

- Independent mpmath check with my own r_∞ (η series, as in the BJ archive script), 40 digits: AQ (3) fixed point to 3.2e−35; BT.1 ratio in [1, ceiling] at 69 points s=10^−20..500 (min ratio 1.0 at tiny s); g(q^k s) nondecreasing k=0..40 at s=10^−4; log(Θ/g)≈5.7e−4 below the E bound 1.3e−3.
- F on 4097 nodes of [1,5] (M=30): grid max 0.6009615785968 at 5^0.7517 (inside the certified max bracket, above its lower end), grid min 0.6009469237946 at 5^0.2517, trapezoid mean 0.60095425116877 (matches the repo's 0.6009542511688), max−min 1.46548e−5 ≥ 1.465480e−5 (BT.5), F(5u)=F(u) (M=30 vs 31) to 1e−41, sup g over 751 points s=10^−12..10^3 is 0.6009615728 ≤ 0.6009631774, Fourier |F̂_1|=3.6637e−6, |F̂_2|=1.3487e−11.
- First independent run had one FAIL (orbit monotonicity) caused by my own script: q(s)=(−5+√(25+4s))/2 cancels catastrophically at s≈10^−30. Replaced by the cancellation-free 2s/(5+√(25+4s)); then 14/14 PASS. Not a repository defect.
- Rounding: printed 10-digit endpoints in GASKET.md are outward relative to the witness log's 12-digit enclosures (no erratum). The witness log's own one-line mean summary prints 0.6009554222 (round-to-nearest of 0.600955422217); GASKET prints the outward 0.6009554223.

## Experimental Validation

Not applicable (pure mathematics on a graph). Computational: repo witness EXIT 0 (18.8 s; /workspace/ifi-btx/repo_BT.log on the box); archive /workspace/scratch-ifi/indep_theorem_BT.py 14/14 PASS (log beside it).

## Mathematical Status

Theorem (repository proof), with computer-assisted certified constants (arb enclosures not re-certified here; independently reproduced in floats).

## Patent Relevance

None. Pure mathematics on a graph; the repository's NOT-THIS fence says it is not a flux, a force or thrust.

## Related Discoveries

DISC-0168 (Theorem BS, answered part of its closed-form question; identification now unconditional), DISC-0114 (Kept Failure AT.1, same hypothesis as BT.5), DISC-0113 (Theorem AT, Θ), DISC-0116 (Theorem AU, ⟨Θ⟩), DISC-0151 (Theorem BI, G=0.6031 now sharp at G*), DISC-0153 (Theorem BJ, BJ.1/BJ.3), DISC-0150 (Conjecture BH.7, value part now theorem-level bracketed).

## Open Questions

Closed form of F (hence of c_∞, C_N, P_N, χ_∞, G*); F̂_k=θ̂_k for k≥1 and θ̂_k≠0 for every k; narrower max/min brackets; Conjecture BS.4 (DISC-0169).
- 2026-10-23 note (no status change): DISC-0171 (Theorem BU, ad459e306e19) answers F̂_k=θ̂_k for every k (F=θ identically) and narrows the max/min brackets to [0.6009615785971,0.6009615785983] and [0.6009469237907,0.6009469237943]; the extremes being exactly half a period apart is REJECTED as a symmetry (DISC-0172).

## Next Experiments

Finer cells near u=5^0.7518 and 5^0.2518 to narrow max F and min F; a proof that F̂_k=θ̂_k (the floats sit on AU's |θ̂_2| floor).

## Reproduction Instructions

```
git clone https://github.com/beyond-repair/informational-flux-identity
git -C informational-flux-identity checkout 48a561c16bce15b0a0992015fa063d5311ebd5d5
cd informational-flux-identity && python3 scripts/gasket_fractional_log_periodic_profile.py   # needs sympy, python-flint
```

## Evidence Log

- 2026-10-23 ~5:01pm EDT. Indexed; repo witness EXIT 0 (18.8 s); independent checks 14/14 PASS after fixing my own q(s) cancellation; no erratum.

## Change History

- 2026-10-23. Initial archive entry.
- 2026-10-23 ~5:58pm EDT. Note added under Open Questions (answered by DISC-0171); original text unchanged.
