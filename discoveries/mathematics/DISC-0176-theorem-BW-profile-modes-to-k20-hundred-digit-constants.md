# Discovery: Theorem BW, AU's certified mode routine re-run deeper and with a finer sandwich certifies θ̂_k≠0 for every k≤20 (BV: k≤11), ⟨F⟩ and c_R(γ) to 1e−113, and G*, min F to 1.3e−109

## Discovery ID

DISC-0176

## Status

THEOREM in the mathematical sense only (repository proof = AU (3)'s proof with new parameters; computer-assisted with outward mpmath.iv and python-flint arb). Method KNOWN (same certified routine as DISC-0116/DISC-0173, parameters changed). The specific constants: novelty UNRESOLVED (not searched). Closed form of F=θ, G*, t_max, t_min: UNRESOLVED. Not thrust.

## Date Discovered

2026-10-29 (America/New_York), ~1:00am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 14686342bd14cbabadfe7d13f742dfc4c446532c (committed 2026-10-29 12:29am EDT).

## Original Evidence

GASKET.md Theorem BW (heading line 3046; BW.1 line 3052, coefficient table lines 3054–3064; BW.2 line 3067; BW.3 line 3076; proof line 3088; Observation (no claim) line 3090; open list from line 3092; NOT THIS fence line 3096), CLAIM_STATUS.md new row (line 79), README.md, scripts/gasket_fractional_profile_modes.py (new, 149 lines), scripts/cli.py, tests/test_cli.py.

## Discovery

Setting as in BT/BU/BV (DISC-0170, DISC-0171, DISC-0173): F(t)=5^((1−γ)t)Q_∞(5^t)=θ(5^t), 1-periodic, θ̂_k its Fourier coefficients, G*=max F.

- BW.1: AU (3)'s routine (AQ (4) node enclosures, AS (2) sandwich, AT.1 orbit lemma, AU's ψ and endpoint corrections) imported unchanged with period [5^−261,5^−260], 1024 cells, sandwich orders b=u=32/33, mpmath.iv outward at 300 digits, node cap 1e240, gives ⟨F⟩ to ±1.0e−113 and a_k, b_k for k≤20 to ±2.0e−113 (BV.4: 8.2e−63). Every k≤20 has a_k or b_k certified nonzero, so θ̂_k≠0 for 1≤|k|≤20, AU (2)'s Mellin transform has genuine poles at 1−γ±iωk for these k, and F is not a trigonometric polynomial of degree <20. |θ̂_k|≤B_k (BV.3) and |θ̂_k|e^(2π²k/ln5)∈[0.60,0.93] for every k≤20 (certified; evidence for Conjecture BV.6, not a proof).
- BW.2: ⟨F⟩=0.600954251168773607823705150099994267971838996065279645275563… and c_R(γ)=(2 sin πγ/π)ln5⟨Θ⟩=0.517165834630505243925980485673127200453783829877158701845373… (±1e−113), inside AU's 34-digit enclosures.
- BW.3: BV.5's argument with the 20-mode sum and BV.3's tail from k=21 (|F−S|≤7.46e−110, 4096 cells, arb) again gives exactly one max and one min per period; G*=0.600961578597101089042056184134616926770040525917258197021856877160250655142022957500717…, min F=0.600946923794265612104226188172129248411629691787677697008509741029502767706538876230717… (±1.3e−109), t_max, t_min to ±5.6e−104; Kept Failure BV.5's offset t_max−t_min−1/2=−1.6240189637007127354426…e−7 reproduced.
- No new Kept Failure and no new Conjecture in BW.

## Why It Matters

Answers BV's (DISC-0173) open "θ̂_k≠0 for k≥12" up to k=20 and pushes G* (the sharp BI.4 constant, DISC-0151/0170) from ~60 to ~109 digits. It also adds nine more certified data points to Conjecture BV.6 (DISC-0175), all inside the same band [0.60,0.93].

## Derivation

Repository proof (GASKET.md line 3088): AU (3)'s proof with new parameters (E_DEPTH=260, K_PER=1024, ORD=32, cap 1e240), AS (2) allowing any sandwich order, every correction of AU (3) evaluated at the new depth by the same code; a nonzero lower bound on |a_k| or |b_k| gives θ̂_k≠0. BW.3 is BV.5's critical-point count with a 20-mode trig polynomial plus BV.3's tail bound.

## Assumptions

As stated in the repository and not re-run there: AQ (3), BN.1, BS.1, BT.2, BU.1, BU.3 (G*≤0.6009615785983), BV.3; AU (3)'s certified routine; AU's and BV's tables and BV.5's digits used for consistency only.

## New Results

- Certified θ̂_12..θ̂_20 (moduli from 8.11e−65 down to 2.70e−107), normalised moduli 0.6542–0.9141 for k=12..20.
- G* and min F to ~109 digits; ⟨F⟩ and c_R(γ) to 113 digits.
- Observation of mine (floats, not a repo claim): k=21 gives |θ̂_21|≈9.935e−113 and normalised modulus ≈0.713, still inside [0.60,0.93]. Beyond the certified range; supports BV.6 as data only.

## Prior Art

As for DISC-0173: analyticity of the periodic factor in a strip and exponentially decaying Fourier coefficients of log-periodic fluctuations are KNOWN in kind (Grabner–Woess 1997 on the Sierpinski graph; Mellin–Perron/Flajolet-style analyses). Re-running a certified routine at higher precision is standard. No search for these specific constants.

## Novelty Analysis

Method KNOWN; this is a precision/range extension of DISC-0173. The constants were not located in prior work but were not searched: UNRESOLVED.

## Falsification Attempts

Independent mpmath script /workspace/scratch-ifi/indep_theorem_BW.py on the box (own η-series r_∞, no repo code imported, 260 digits, depth 5^−380, 72-node rectangle rule; depth truncation M=380 vs 365 differs by 1.8e−175), 10/10 PASS:
- ⟨F⟩ agrees with all 60 printed digits.
- θ̂_1..θ̂_20 far above float noise; |θ̂_k|≤B_k for k≤20; normalised moduli in [0.6066,0.9268] for k≤20; |θ̂_20|=2.700829212e−107 ≥ printed 2.700826e−107.
- 20-mode sum: F′ has exactly two sign changes on a 512-grid; Newton t_max, t_min agree with the 58 printed digits to <1e−55; max F and min F agree with all 87 printed digits; BV.5's offset −1.6240189637007127354426e−7 reproduced.
- First runs failed on my side: system `python` missing (used python3), 160 digits lost ~65 digits to cancellation in 2+s−2η(s) at depth 5^−300 (raised to 260 digits), and one tolerance tighter than the printed string. None is a repository defect.

**Erratum (presentation only, does not affect any claim).** The "|θ̂_k|≥" column prints the certified lower bound with Python's `.6e` (round to nearest), so 4 of BW's 9 new rows print a value slightly above the true modulus: k=12 prints 8.112800e−65 vs float 8.11279965379e−65, k=15 8.290714e−81 vs 8.2907136442e−81, k=16 4.709507e−86 vs 4.70950665579e−86, k=18 9.168824e−97 vs 9.16882350206e−97 (excess ≤7.3e−8 relative). The commit message's "|θ̂_12|≥8.112800e−65" and "|θ̂_16|≥4.709507e−86" inherit this. The same happens in BV's table (DISC-0173) at k=6 (8.621962e−33 vs 8.6219618346e−33) and k=7 (4.321505e−38 vs 4.32150483175e−38), which my BV check (k=5, 8, 11 only) missed. Since the certified radius is 2e−113, the true values are below the printed digits, but θ̂_k≠0 and the [0.60,0.93] band are unaffected. Same pattern as the earlier BR/BS/BN erratum notes.

## Experimental Validation

Not applicable (pure mathematics on a graph). Computational: repo witness scripts/gasket_fractional_profile_modes.py (see Evidence Log for exit status and time; /workspace/scratch-ifi/repo_theorem_BW.log on the box); archive indep_theorem_BW.py 10/10 PASS plus the erratum check. Repo reports pytest -k "not reproduce": 36 passed (not re-run here).

## Mathematical Status

Theorem (repository proof) with computer-assisted certified constants (interval enclosures not re-certified here; reproduced in 260-digit floats).

## Patent Relevance

None. Pure mathematics on a graph; the repository's NOT THIS fence says it is not a flux, force or thrust.

## Related Discoveries

DISC-0173 (Theorem BV; extends BV.4's mode table from k≤11 to k≤20 and BV.5's extremes from ~60 to ~109 digits; erratum note), DISC-0174 (Kept Failure BV.5; witness reproduced, stays REJECTED), DISC-0175 (Conjecture BV.6; 9 more data points, stays CONJECTURE), DISC-0116 (Theorem AU; routine reused), DISC-0171 (Theorem BU), DISC-0151 (BI.4 constant G*).

## Open Questions

θ̂_k≠0 for k≥21 (each k costs ~5.3 more digits); Conjecture BV.6; whether Q_∞'s singularities on (−∞,0) are poles; closed form of F=θ, G*, t_max, t_min; feeding G* into BI.4/BJ; Conjecture BS.4 and the other carried-over items.

## Next Experiments

Print outward-rounded lower bounds (round toward zero) in the mode tables; locate zeros of 2+s−2η(s) on the negative axis to test whether π/ln5 is the maximal strip, which would settle the upper side of BV.6.

## Reproduction Instructions

```
git clone https://github.com/beyond-repair/informational-flux-identity
git -C informational-flux-identity checkout 14686342bd14cbabadfe7d13f742dfc4c446532c
cd informational-flux-identity && python3 scripts/gasket_fractional_profile_modes.py   # needs mpmath, python-flint; ~5 min
```

## Evidence Log

- 2026-10-29 ~1:00am EDT. Indexed; repo witness EXIT 0 (431.5 s, 12 ok lines, "all Theorem BW checks passed"; it prints the same rounded-to-nearest lower bounds); independent checks 10/10 PASS; erratum on printed lower bounds (BW k=12,15,16,18; BV k=6,7).

- 2026-10-29 ~1:57am EDT. Note: BW's enclosures are reused unchanged by Theorem BX (DISC-0177) for ρ_1..ρ_20 and the T_17 certificate; no status change.

- 2026-10-29 ~4:54am EDT. Note: Theorem BY (IFI 4e57bb8631cd, DISC-0179) certifies θ̂_21≠0 (|θ̂_21|≥9.93e−113), answering BW's open k≥21 for k=21; my float |θ̂_21|≈9.935e−113 in the New Results above agrees. No status change.

## Change History

- 2026-10-29. Initial archive entry.
- 2026-10-29. Note added for DISC-0177/0178 (history above kept unchanged).
- 2026-10-29. Note added for DISC-0179 (history above kept unchanged).
