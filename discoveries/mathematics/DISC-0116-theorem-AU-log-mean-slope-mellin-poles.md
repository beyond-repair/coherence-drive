# Discovery: Theorem AU, the critical slope is the log-mean of the corner profile, and the Mellin poles of r_∞

## Discovery ID

DISC-0116

## Status

THEOREM (mathematical sense only). Parts (1) and (2) have a complete written proof in the repository, conditional on Theorems AQ, AR, AS, AT and Kept Failure AT.1 (DISC-0106, DISC-0109, DISC-0111, DISC-0113, DISC-0114). Part (3) is computer-assisted (outward-rounded interval enclosures). Novelty UNRESOLVED. Not thrust.

## Date Discovered

2026-10-22 (America/New_York), corpus-discovery slice ~7:02am EDT.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit b036dcfb89e66ffa51ebf8407c08996d7fa3d17e (2026-10-22 06:11:25 −0400). Paths: GASKET.md "Theorem AU", "KEPT FAILURE AU.1", Conjecture AT.2 header now "Status: PROVED by Theorem AU"; CLAIM_STATUS.md new row "Slope of R_γ(n) at γ=log3/log5 as a log-mean (Conjecture AT.2); Mellin poles of r_∞ — VERIFIED (Theorem AU, Kept Failure AU.1)"; scripts/gasket_fractional_log_mean.py (new, 309 lines); scripts/cli.py; README.md.

## Original Evidence

GASKET.md Theorem AU (1)–(3), proof, witness list, Kept Failure AU.1, OPEN, NOT THIS at b036dcfb89e66ffa51ebf8407c08996d7fa3d17e.

## Discovery

With r_∞ the limiting corner resolvent, γ=log3/log5, g(s)=s^(1−γ)r_∞(s), Θ its log-periodic profile, ψ the Koenigs coordinate of q=p^(−1) (p(s)=s(s+5)) and θ=Θ∘ψ^(−1) exactly 5-periodic:

1. ∫₀^∞ s^(−γ) r_m ds = m ln5 ⟨Θ⟩ + O(1), hence c_R(γ) = (2 sin πγ/π) ln5 ⟨Θ⟩ (Conjecture AT.2, DISC-0115, proved).
2. M(z)=∫ s^(z−1) r_∞ ds continues meromorphically to 1−γ−0.65 < Re z < 1 with at most simple poles at z_k = 1−γ + 2πik/ln5, residue θ̂_(−k); lim_(α↑γ)(γ−α)R_∞(α) = c_R(γ)/ln5.
3. Certified: ⟨Θ⟩ ∈ [0.6009542511687736078237051500999942, …9943]; c_R(γ) ∈ [0.5171658346305052439259804856731271, …1273] (inside DISC-0113's independent enclosure, 16 more digits); Fourier modes k=1..4 certified nonzero (|θ̂_1|≥3.66370e−6, |θ̂_2|≥1.34873e−11, |θ̂_3|≥8.82462e−17, |θ̂_4|≥4.26825e−22), so M has genuine complex poles at k=±1..±4.

## Why It Matters

Closes the repository's own Conjecture AT.2 and turns the critical-exponent slope into a period average of a self-similar profile; identifies the complex-dimension (Mellin pole) structure of the corner resolvent.

## Derivation

As in the repository proof: split J_m at 5^(−m) and 1; head ≤ 1/(3(1−γ)) because (5/3)5^(γ−1)=1; tail ≤ 1/γ; defect bounded by 5^(mε)Σ_(j≥m)∫s^(−(γ−ε))δ_(j+1) = O(1) via AR at γ−ε; middle term in the Koenigs coordinate is m periods of a 5-periodic bounded θ plus O(1). Part (2) is the standard geometric-series Mellin argument ∫₀^X x^w θ dx/x = F(w)/(1−5^(−w)), F entire.

## Assumptions

Theorem AQ (1)–(4), AR (2), AS (2), AT (4a) at γ (or only R_γ(n)=c_R(γ)n+o(n)), Kept Failure AT.1's orbit lemma (|g−Θ|≤Cs^0.65), continuity and positivity of Θ. Part (3) relies on the repository's outward-rounded arithmetic, not re-certified here with intervals.

## New Results

Archive (float) observation, not certified: |θ̂_5| ≈ 1.698e−27, continuing the ≈4–6e−6 ratio between successive modes the repository reports (order e^(−2π²/ln5)≈4.7e−6).

## Prior Art

Log-periodic oscillations and the resulting complex poles of Mellin transforms are classical (Flajolet–Gourdon–Dumas Mellin asymptotics; Kigami–Lapidus and Lapidus–van Frankenhuijsen complex dimensions; Derfel–Grabner–Vogl for self-similar spectral functions; Koenigs linearization). The method is KNOWN; the specific constants for this resolvent were not searched.

## Novelty Analysis

UNRESOLVED for the constants; DERIVATIVE in method.

## Falsification Attempts

- Proof read: each of the four split terms is bounded as stated; (i) uses r_m ≤ r_m(0) and the exact identity 5^γ/3=1; (iii) needs AR's sequence at γ−ε bounded, which AR (2) supplies. No gap found.
- Archive independent check /workspace/scratch-ifi/indep_theorem_AU.py (mpmath 60 digits, own decimation recursion r_200, no repo import): 128-point periodic trapezoid over s∈5^(−141)[1,5) gives ⟨Θ⟩=0.600954251168773607823705150099994268 (inside the AU enclosure), slope c_R(γ)=0.5171658346305052439259804856731272 (inside DISC-0113's enclosure and AU's 34-digit one); a shifted period gives the same mean to 36 digits; DFT Fourier modes k=1..4 match the table to all printed digits (k=3,4 abs dev 1.5e−35, within the stated ±2e−35); J_20 − 20 ln5⟨Θ⟩ = 1.3148755974009 (repo 1.31487559740). 11 PASS, EXIT 0. A first tolerance (1e−30 absolute) failed only because the table prints 22 significant digits; the check was rerun with the table's stated precision.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Theorem (parts 1–2 proof; part 3 computer-assisted).

## Patent Relevance

None.

## Related Discoveries

- DISC-0113 → DISC-0116, DISC-0114 → DISC-0116 (mathematical); DISC-0116 proves DISC-0115; DISC-0116 → DISC-0117 (Kept Failure AU.1).

## Open Questions

Closed forms for ⟨Θ⟩, θ̂_k, c_R, c_S, C_γ, 𝓛; certified C_γ≈0.70307046242184; whether every θ̂_k≠0 and the exact decay rate; the c_S-side analogue.

## Next Experiments

Interval certificate for C_γ; certified θ̂_5 (float ≈1.7e−27) to test the e^(−2π²/ln5) decay observation.

## Reproduction Instructions

`git -C informational-flux-identity checkout b036dcfb89e66ffa51ebf8407c08996d7fa3d17e && python3 scripts/gasket_fractional_log_mean.py` (~16 s, EXIT 0). Archive: `python3 /workspace/scratch-ifi/indep_theorem_AU.py` (~4 s, EXIT 0, 11 PASS).

## Evidence Log

- 2026-10-22. Repo witness EXIT 0 (16 PASS lines, log /workspace/scratch-ifi/repo_theorem_AU.log); archive EXIT 0 (11 PASS, /workspace/scratch-ifi/indep_theorem_AU.log). IFI repository description still matches its claim fence.

## Change History

- 2026-10-22. Initial archive entry.
