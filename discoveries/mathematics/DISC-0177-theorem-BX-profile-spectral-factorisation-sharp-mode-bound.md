# Discovery: Theorem BX, the log-periodic profile F=θ is one explicit kernel convolved with a positive periodic spectral measure m of mass c_R(γ)/2, so θ̂_k=(π/ln5)·m̂_k/sin π(γ+iωk) exactly, giving a sharp mode bound and an equivalent form of Conjecture BV.6

## Discovery ID

DISC-0177

## Status

THEOREM in the mathematical sense only (repository proof; BX.1 rests on Assumption BX, the classical Nevanlinna/Krein–Kac characterisation of Stieltjes functions, cited from the literature and not proved in the repository; BX.4 computer-assisted with python-flint arb using BW's certified routine). Method KNOWN (Stieltjes representation + Mellin convolution + Carathéodory–Toeplitz positivity are standard tools). Application to this profile and the specific constants: novelty UNRESOLVED (not searched). Closed form of F=θ, G*, t_max, t_min: UNRESOLVED. Not thrust.

## Date Discovered

2026-10-29 (America/New_York), ~1:57am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 06eddfa7560014a0f40341be0a6f89a0e4863eb4 (committed 2026-10-29 1:30am EDT).

## Original Evidence

GASKET.md Theorem BX (heading line 3104; BX.1 line 3110; BX.2 line 3111; BX.3 line 3116; BX.4 and ρ_k table from line 3121; proof line 3133; Kept Failure BX.5 line 3135, see DISC-0178; Observation (no claim) line 3137; open list line 3139; NOT THIS fence line 3143; witness description line 3145), CLAIM_STATUS.md new row (line 80), README.md, scripts/gasket_fractional_profile_spectral.py (new, 269 lines), scripts/cli.py, tests/test_cli.py.

## Discovery

Setting as in BT–BW (DISC-0170, 0171, 0173, 0176): F(τ)=5^((1−γ)τ)Q_∞(5^τ)=θ(5^τ), γ=log3/log5, ω=2π/ln5, θ̂_k=a_k−ib_k.

- BX.1: BV.2's locally uniform limits keep Im z·Im f≤0, so (Assumption BX) Q_∞(u)=∫_(0,∞) dν(λ)/(λ+u) with ν≥0; BS.1's Q_∞(5u)=(3/5)Q_∞(u) and uniqueness of the representation force no a/u term, no constant, and ν(5A)=3ν(A).
- BX.2: σ=λ^(−γ)ν is 1-periodic in t=log_5 λ (3·5^(−γ)=1); with K(x)=5^(γx)/(5^x+1), F(τ)=∫K(t−τ)dσ(t), and Fubini plus ∫_0^∞v^(a−1)/(1+v)dv=π/sin πa give θ̂_k=(π/ln5)·m̂_k/sin π(γ+iωk) for every k, where m is σ restricted to one period. At k=0, m(T)=⟨F⟩ ln5 sin(πγ)/π=c_R(γ)/2=0.258582917315252621962990242836563600226891914938579350922687… (±4.3e−114).
- BX.3: |m̂_k|≤m̂_0 gives |θ̂_k|≤⟨F⟩ sin πγ/|sin π(γ+iωk)| ≤ (πc_R(γ)/ln5)·e^(−2π²|k|/ln5)/(1−e^(−4π²|k|/ln5)); so limsup|θ̂_k|e^(2π²k/ln5)≤πc_R(γ)/ln5=1.00949802052668788…, removing BV.3's linearly growing factor. Exactly, |θ̂_k|e^(2π²k/ln5)=(πc_R/ln5)ρ_k(1+O(e^(−4π²k/ln5))) with ρ_k=|m̂_k|/m̂_0, so Conjecture BV.6 holds iff ρ_k converges to a nonzero limit, and θ̂_k≠0 iff m̂_k≠0.
- BX.4: with BW's enclosures, ρ_k∈[0.60,0.92] for every k≤20 (radius ≤1.1e−6; ≤6.2e−12 for k≤19), the BX.3 bound holds and is 12.7 (k=1) to 252.7 (k=20) times below B_k, and the Toeplitz section T_17=(m̂_(i−j)) is certified positive definite (smallest LDL* pivot of T_17−2εI 5.96e−14, ε=3.4e−28).

## Why It Matters

It is the first structural description of the profile in this chain: F is no longer just a certified function but a positive-measure transform with an explicit kernel, so every mode question reduces to the Fourier coefficients of one positive measure on the scale circle. It sharpens BV.3 (DISC-0173) to the correct constant, gives the exact meaning of Conjecture BV.6 (DISC-0175), and connects AR/AU's slope constant c_R(γ) to the spectral mass per scale period (c_R=2m(T)). It also yields DISC-0178: no closed form of F as ≤16 self-similar pole series.

## Derivation

Repository proof (GASKET.md line 3133), checked by hand here: the kernel identity 5^((1−γ)τ)λ^γ/(λ+5^τ)=K(t−τ) for λ=5^t; θ̂_k=∫∫K(t−τ)e^(−2πikτ)dσ(t)dτ, substitute x=t−τ to get m̂_k·∫K(x)e^(2πikx)dx with m̂_k=∫e^(−2πikt)dm; v=5^x turns the last integral into (1/ln5)∫v^(γ+iωk−1)/(1+v)dv=π/(ln5 sin π(γ+iωk)), valid since 0<Re a=γ<1. |sin π(γ+iy)|²=sin²πγ+sinh²πy gives BX.3. Sign conventions consistent with AU's θ̂_k=a_k−ib_k.

## Assumptions

Assumption BX (literature): a function holomorphic on C\(−∞,0], nonnegative on (0,∞), with Im z·Im f(z)≤0, is a Stieltjes function a/z+b+∫dν/(λ+z), uniquely; and a Stieltjes transform continues across (−∞,0) exactly off −supp ν, with poles at isolated atoms. As stated in the repository and not re-run there: AQ (3), BN.1, BS.1, BT.2, BU.1, BV.2, AU (1); BW's certified routine.

## New Results

- Exact factorisation θ̂_k=(π/ln5)m̂_k/sin π(γ+iωk); c_R(γ)=2m(T).
- Sharp asymptotic constant πc_R(γ)/ln5=1.00949802052668788… for the normalised mode moduli.
- ρ_1..ρ_20 table (0.6009–0.9181), and m has at least 17 support points per period (DISC-0178).
- Observation of mine (floats, not a repo claim): ρ_21≈0.70637 (uncertified, consistent with DISC-0176's float 0.713 normalised by 1.0095); float smallest eigenvalues of T_16..T_19 are 3.2e−20, 1.8e−21, 5.1e−23, 1.2e−24, matching the repository's observed drop of ~20–50 per step.

## Prior Art

KNOWN tools: Stieltjes/Nevanlinna representation (Krein–Kac; see e.g. Schilling–Song–Vondraček, Bernstein Functions, ch. 2 and 7); Mellin convolution and π/sin πa (Euler's beta integral); Carathéodory–Toeplitz rank of positive measures with r atoms. Log-periodic oscillations with exponentially small Fourier modes in Sierpinski-gasket Green functions/transition probabilities are KNOWN in kind (Grabner–Woess 1997). Pure point spectrum of Laplacians on infinite Sierpinski gaskets (Teplyaev 1998) is the relevant known result for the open atomicity question; the repository notes it is suggestive and not used. No search for these specific constants or this exact factorisation of this profile.

## Novelty Analysis

Each ingredient is KNOWN; the combination is a clean structural result for this particular log-periodic corner profile. Whether this factorisation of the gasket corner resolvent's log-periodic factor appears in the literature (e.g. Grabner–Woess or Teplyaev-style spectral decimation work) was not searched: UNRESOLVED.

## Falsification Attempts

Independent mpmath script /workspace/scratch-ifi/indep_theorem_BX.py on the box (own η-series r_∞ as in DISC-0176's check, no repo code imported, 260 digits, depth 5^−380, 72-node rectangle rule), 14/14 PASS:
- m(T)=c_R(γ)/2 as an identity (<1e−200) and against all 60 printed digits.
- Kernel Fourier transform at complex a: independent mpmath quadrature of ∫K(x)e^(2πikx)dx on [−400,1200] matches π/(ln5 sin π(γ+iωk)) to 1e−40 (k=1) and 2e−37 (k=2).
- Full convolution formula on an independent toy: ν=Σ_n 3^n δ_(λ_0 5^n), λ_0=5^0.3 (so m=λ_0^(−γ)δ_0.3), F computed by direct summation, modes k=0,1,3 match the factorisation to ≤6e−26 relative (this checks phase convention as well as normalisation, unlike the repository's m=δ_0 toy).
- ρ_1..ρ_20 reproduce every printed digit of the BX.4 table; band [0.60,0.92]; πc_R/ln5=1.0094980205266878835; |θ̂_k| below the BX.3 bound for k≤20; improvement factors 12.669 (k=1) and 252.7 (k=20); ρ_1<0.7696418615.
- T_17 positive definite in floats (smallest eigenvalue 1.8e−21, far above the ~1e−28 error of m̂_k for k≤16).
- Harness failures on my side, fixed before the pass: an oscillatory quadrature truncated at |x|≤60 (tail 5^(−19) swamps the 1e−11 k=2 value), and a toy normalisation where I double-counted λ_0^(−γ). Neither is a repository defect.
- Attack on the logic: BX.5-type rank argument and BX.3 equality case checked by hand; the BX.1 step needs BV.2's locally uniform convergence on C\(−∞,0], which is imported, and Assumption BX, which is classical. No contradiction found. No erratum: the printed ρ_k are 12-digit values with certified radius ≤6.2e−12 and m(T)'s 60 digits match.

## Experimental Validation

Not applicable (pure mathematics on a graph). Computational: repo witness scripts/gasket_fractional_profile_spectral.py (see Evidence Log); archive indep_theorem_BX.py 14/14 PASS. Repo reports pytest -k "not reproduce": 37 passed (not re-run here).

## Mathematical Status

Theorem (repository proof) conditional only on a classical literature characterisation (Assumption BX) and imported earlier results; BX.4 constants computer-assisted (interval enclosures not re-certified here; reproduced in 260-digit floats).

## Patent Relevance

None. Pure mathematics on a graph; the repository's NOT THIS fence says m is not a flux and its mass is not a force.

## Related Discoveries

DISC-0173 (Theorem BV; BX.3 sharpens BV.3's bound), DISC-0175 (Conjecture BV.6; reformulated as ρ_k→ρ_∞>0), DISC-0176 (Theorem BW; its enclosures feed BX.4), DISC-0178 (Kept Failure BX.5), DISC-0116 (Theorem AU; c_R(γ) and the Mellin poles), DISC-0168/0170/0171 (BS/BT/BU setting).

## Open Questions

Conjecture BV.6 as ρ_k→ρ_∞>0 (the repository remarks that for several atoms in general position ρ_k oscillates, so BV.6 as worded may be too strong); whether ν is purely atomic (poles of Q_∞); m̂_k≠0 for k≥21; identification of ν with the corner spectral measure of the blown-up Laplacian; closed form of F, G*, t_max, t_min; the carried-over list.

## Next Experiments

Locate the zeros of 2+s−2η(s) on the negative axis (poles of r_∞, hence atoms of ν) and compare with the Toeplitz eigenvalue decay; test the observed phase drift of m̂_5, m̂_10, m̂_15, m̂_20 (concentration near a coset of (1/5)Z) against an atomic model; certify T_18 at higher precision.

## Reproduction Instructions

```
git clone https://github.com/beyond-repair/informational-flux-identity
git -C informational-flux-identity checkout 06eddfa7560014a0f40341be0a6f89a0e4863eb4
cd informational-flux-identity && python3 scripts/gasket_fractional_profile_spectral.py   # needs mpmath, python-flint, sympy; ~7 min
```

## Evidence Log

- 2026-10-29 ~1:57am EDT. Indexed; independent checks 14/14 PASS; repo witness scripts/gasket_fractional_profile_spectral.py EXIT 0 (380 s, 19 ok lines, "all Theorem BX checks passed"; T_17 pivot 5.961e−14 with ‖E‖_F≤3.38e−28, T_18 not certified, as stated). Archive: /workspace/scratch-ifi/repo-ifi-BX, repo_theorem_BX.log, indep_theorem_BX.py/.log on the box.

- 2026-10-29 ~4:54am EDT. Note: Theorem BY (IFI 4e57bb8631cd, DISC-0179) extends BX.4 to k=21 (ρ_21=0.70637…) and the Toeplitz certificate from T_17 to T_20; no status change.

## Change History

- 2026-10-29. Initial archive entry.
- 2026-10-29. Note added for DISC-0179 (history above kept unchanged).
