# Discovery: Theorem AS, certified digits of the gasket audit limit and proof of Conjecture J.2

## Discovery ID

DISC-0111

## Status

THEOREM (mathematical sense only; computer-assisted, conditional on DISC-0106's decimation and power ceiling as re-certified in-repo). Novelty UNRESOLVED. Not thrust.

## Date Discovered

2026-10-22 (America/New_York), corpus-discovery slice ~4:56am EDT.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit a6e6c74b680d6ef126b5e4b7cc1de3a939c2dcc7 (2026-10-22 04:13:12 −0400). Paths: GASKET.md "Theorem AS" and "KEPT FAILURE AS.1"; GASKET.md J.2 header "Status of J.2 below: PROVED by Theorem AS (5)"; CLAIM_STATUS.md row "Certified digits of the audit limit and Conjecture J.2 — VERIFIED"; scripts/gasket_fractional_limit_digits.py (new, 358 lines); scripts/cli.py; README.md.

## Original Evidence

GASKET.md Theorem AS (1)–(5): limit integrals R_∞=(2 sin πα/π)J_r, σ_∞=(sin πα/π)J_w, 𝓛=(√21/6)J_w/J_r with J_f=∫₀^∞ s^(−α) f_∞ ds; complete monotonicity of r_n=Σc_i/(λ_i+s) and w_n=1−s r_n (c_i≥0, Σc_i=1), passing to the pointwise limits; Newton-remainder interpolation sandwich sign(f−p)=(−1)^b; certified table on geometric nodes x_k=2^(−250)(17/16)^k up to 1e25 (3831 nodes, b=u=10 floor / 11 ceiling).

## Discovery

Certified enclosures: 𝓛(0.45)∈[0.82113862713346, 0.82113862713352] (AQ bracket width 3.7e−3 → 5e−14), R_∞(0.45)∈[2.51594623787706, 2.51594623787714], σ_∞(0.45)∈[1.35247562325228, 1.35247562325233]; 𝓛(0.10)∈[1.410638933063, 1.410638933065]; also α=0.25, 0.49, 0.55 (0.55 width 2.6e−8, set by the head term). Consequence (5): Conjecture J.2 (‖F(n,0.10)‖≥1.410 ∀n) is true, because AQ (3) gives strict decrease to 𝓛(0.10)>1.410.

## Why It Matters

Closes the last open item of the former DISC-0034 (J.2 → DISC-0108 now THEOREM), and replaces the 3-digit bracket of DISC-0106 with 13 certified digits. It also sharpens the test of the archive-derived scaling law DISC-0035.

## Derivation

As in the repository. (1) monotone convergence for r_n↑ and dominated convergence 0≤w_n≤3/(3+s). (2) the order-k divided difference of a Stieltjes sum has sign (−1)^k and is a finite linear combination of values, so it passes to pointwise limits. (3) f−p = f[x_1..x_m,x]∏(x−x_i), signs (−1)^(b+u)·(−1)^u = (−1)^b. (4) on a geometric grid the cell integral is x_c^(1−α)Σ W_m f(x_(c+m)) with interval Lagrange weights; node values enclosed by AQ (4) T^k r_0 ≤ r_∞ ≤ T^k(1/σ); head via monotonicity and the power ceiling r_∞≤Bs^(−0.35) (B≈0.892577, re-certified); tail via the moments 2, 6. Archive re-read the derivation; no gap found in (1)–(3). (4) is a computation and was not independently re-certified in interval arithmetic in this slice (see Falsification Attempts).

## Assumptions

Theorem AQ (1)–(4) (DISC-0106) and its power ceiling (C1)–(C3); correctness of mpmath.iv outward rounding; the repo enclosure uses the double nearest 0.45 (as in DISC-0106; immaterial at these widths but noted).

## New Results

- J.2 proved (DISC-0108 CONJECTURE → THEOREM).
- DISC-0035: certified 𝓛(0.45)=0.8211386271335… and 𝓛(0.10)=1.4106389330… against the law's predictions ≈0.8211 and ≈1.4106; agreement to the law's stated digits, but the law's exact affine form is still not proved (stays CONJECTURE, edge only).

## Prior Art

Interpolation bounds for completely monotone / Stieltjes functions via divided-difference sign (Bernstein; standard in validated numerics) and spectral decimation on the Sierpinski gasket (Rammal–Toulouse, Fukushima–Shima, Strichartz, Teplyaev) are classical. The specific audit norm is repository-defined. No targeted literature search for these constants.

## Novelty Analysis

Method: KNOWN components. Certified constants for this repository-defined quantity: UNRESOLVED (no search for prior numerical values of fractional corner resistances on the gasket).

## Falsification Attempts

Archive /workspace/scratch-ifi/indep_theorem_AS.py (mpmath only, no repo import): (A) own 30-digit quadrature of the decimation recursion at n=60 and n=80 for α∈{0.10,0.25,0.45,0.49}; every ‖F(80)‖ lies above or within ρ^n of the AS enclosure and ‖F(60)‖≥‖F(80)‖ (α=0.45: ‖F(60)‖=0.8211386272249 reproduces the repo's consistency value, ‖F(80)‖=0.8211386271335 inside the enclosure); (B) J.2 margin ‖F(80,0.10)‖−1.410=6.389e−4; (C) sign rule f−p=(−1)^b on 240 random completely monotone Stieltjes sums at 60 digits, b∈{2,3,10,11}, zero violations; (D) AS.1 numbers reproduced; (E) J.2 statement text identical at HEAD and parent 3ec0a064caa5. Not broken. Limitation: no independent interval re-certification of (4) this slice; the independent evidence is high-precision floating quadrature, consistent to ~1e−13.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Theorem (computer-assisted).

## Patent Relevance

None identified.

## Related Discoveries

- DISC-0106 → DISC-0111. Mathematical (recursion, ceilings, monotonicity).
- DISC-0109 → DISC-0111. Computational (AR's ρ used in AS.1).
- DISC-0111 → DISC-0108. Mathematical (proves J.2; status change).
- DISC-0111 → DISC-0034. Historical (closes the original J.1/J.2 record).
- DISC-0111 → DISC-0035. Computational (certified digits vs law prediction; law stays CONJECTURE).
- DISC-0111 → DISC-0112. Mathematical (Kept Failure AS.1).

## Open Questions

Closed forms of 𝓛, R_∞, σ_∞; certified c_R(0.45), c_S(0.45); certificates for α≥0.65; independent interval re-certification.

## Next Experiments

Independent mpmath.iv re-certification of 𝓛(0.10) with a different grid ratio and node count; test DISC-0035's affine law against certified 𝓛 at several α.

## Reproduction Instructions

`git -C informational-flux-identity checkout a6e6c74b680d6ef126b5e4b7cc1de3a939c2dcc7 && python3 scripts/gasket_fractional_limit_digits.py` (~45 s, EXIT 0). Archive: `python3 /workspace/scratch-ifi/indep_theorem_AS.py` (~80 s, EXIT 0).

## Evidence Log

- 2026-10-22. Repo witness EXIT 0, 25 PASS (log /workspace/scratch-ifi/repo_theorem_AS.log). Archive indep EXIT 0, 9 PASS (log /workspace/scratch-ifi/indep_theorem_AS.log).

## Change History

- 2026-10-22. Initial archive entry.
