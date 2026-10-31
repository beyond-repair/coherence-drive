# Discovery: Theorem CW — a bound on ρ(L_k) uniform in k, 0.1999·0.5999^k ≤ 3^(k+1)ρ(L_k) − 1 ≤ 0.2873·0.8352^k, proving 3^k ρ(L_k) → 1/3

## Discovery ID
DISC-0209

## Status
THEOREM (mathematical sense only; exact construction plus interval-certified bounds in the source repository) for CW.1–CW.3; CW.4 is a consistency check. Method: KNOWN (positive test function built as an orbit-sum coboundary along the attracting fixed point of σ_1, then a Collatz–Wielandt bracket). Constants: UNRESOLVED as to novelty; no claim of a mathematical first. This proves the 3^k ρ(L_k) → 1/3 observation recorded in DISC-0208; q^(k) → −1/3 stays a HEURISTIC (not proved by CW). Not a flux, not thrust.

## Date Discovered
2026-10-30 (indexed ~10:10 PM EDT; source commit 2026-10-30 21:12:52 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 572ca675ce2eaabe5bfa09657d7e3728b26bb85e

## Original Evidence
- GASKET.md, new section "Theorem CW" (line 4345; NOT THIS paragraph line 4379), +42 lines.
- CLAIM_STATUS.md, new row at line 105.
- scripts/gasket_fractional_profile_level_uniform_k.py (new, 252 lines, standalone, python-flint); scripts/cli.py (+1); tests/test_cli.py (+28); README.md (+2).

## Discovery
Setting as in DISC-0206–0208: (L_k f)(s) = u_1 f(σ_1 s) + u_2 f(σ_2 s) on C(X), X = [√5/2, 5/2], σ_{1,2}(s) = √(15/4 ∓ s), u_i = w̃_i/(2σ_i)^k, w̃_1 = (s+½)/(2s(7/2−s)), w̃_2 = (s−½)/(2s(s+7/2)). σ_1 has fixed point s* = 3/2 with 2σ_1(s*) = 3 and w̃_1(s*) = 1/3.

With x_0 = s, x_{j+1} = σ_1(x_j), Φ(s) = −Σ_j log(2σ_1(x_j)/3), Ψ(s) = Σ_j log(3w̃_1(x_j)), h_k = e^{kΦ+Ψ} > 0:

  L_k h_k / h_k = 3^{−k−1} (1 + G(s) B(s)^k), B = (3/(2σ_2)) e^{Φ(σ_2 s) − Φ(s)}, G = 3w̃_2 e^{Ψ(σ_2 s) − Ψ(s)}.

- CW.1 (exact): σ_1 is a 1/√5-contraction on X' = [1172343/2^20, 5/2] ⊃ X; Φ, Ψ converge uniformly; tails after 120 terms ≤ 8.4e-43 and 6.3e-42.
- CW.2 (arb, 160 bits, 1967-interval adaptive cover): 0.5999 < B < 0.8352, 0.1999 < G < 0.2873 on X.
- CW.3 (Collatz–Wielandt): for every real k ≥ 0, 0.1999·0.5999^k ≤ 3^{k+1}ρ(L_k) − 1 ≤ 0.2873·0.8352^k. Hence 3^k ρ(L_k) > 1/3 for all k, 3^k ρ(L_k) → 1/3, ρ(L_{k+1})/ρ(L_k) → 1/3; e.g. ρ(L_13) ∈ [2.0913e-7, 2.1486e-7], ρ(L_50) ∈ [4.64318e-25, 4.64335e-25].
- CW.4: CE's r (k = 0) and CT/CU/CV's ρ(L_k), k ≤ 12, lie strictly inside.

## Why It Matters
First statement in the corpus about L_k that holds for all k. It turns DISC-0208's k → ∞ observation for ρ into a proof with an explicit geometric error, and extends the lower half of CV.7 (3^k ρ > 1/3) from k ≤ 12 to every real k ≥ 0.

## Derivation
Checked here by hand. σ_1 branch: h_k(σ_1 s)/h_k(s) = (2σ_1/3)^k/(3w̃_1), times u_1 = w̃_1/(2σ_1)^k gives exactly 3^{−k−1}. σ_2 branch: u_2 h_k(σ_2 s)/h_k(s) = 3^{−k−1}·[(3/(2σ_2))e^{ΔΦ}]^k·[3w̃_2 e^{ΔΨ}] = 3^{−k−1} G B^k. With G, B > 0, inf and sup of 1 + GB^k over X are bounded by (min G)(min B)^k and (max G)(max B)^k; for a positive operator, m h ≤ L h ≤ M h with h > 0 continuous gives m ≤ ρ(L) ≤ M. The proof is correct as written.

## Assumptions
None beyond the setting for CW.1–CW.3 (the repo says the same). CW.4 uses CE, CT.3, CU.3, CV.3 as stated (consistency only).

## New Results
Explicit two-sided geometric bracket for 3^{k+1}ρ(L_k) − 1, valid for all real k ≥ 0; explicit enclosures of ρ(L_k) for k ≥ 13. Observation (floats, not claimed): min B = 3/5 and min G = 1/5 at s = 5/2 (fixed point of σ_2), max B ≈ 0.835144 at √5/2; the true decay ratio ≈ 0.779 at k = 10, 11.

## Prior Art
Collatz–Wielandt bounds for positive operators (Collatz 1942; Wielandt 1950; Krasnosel'skii's cone version); building the test function as an orbit-sum coboundary along an attracting fixed point is the standard Koenigs/Schröder-type conjugation used for weighted composition operators (cf. Cowen–MacCluer). No literature search for these constants was done.

## Novelty Analysis
Method KNOWN. Constants are specific to this repository's operators; novelty UNRESOLVED.

## Falsification Attempts
- Repo witness at 572ca675ce2e: EXIT 0, 2.3 s, ends "all Theorem CW checks passed". Repo tests `pytest tests/test_cli.py -k uniform`: 3 passed.
- Algebra attack: rederived the identity branch by branch (above). Survived.
- Independent script `mathematics/scripts/indep_theorem_CW.py` (mpmath, 40 digits, no repo code): 31/31 PASS on first run.
  - Fixed-point facts: σ_1(3/2) = 3/2, w̃_1(3/2) = 1/3, σ_2(5/2) = 5/2.
  - Identity L_k h_k/h_k = 3^{−k−1}(1+GB^k) checked by direct evaluation (J = 200 orbit terms) at 12 random s with k ∈ {0, 0.5, 1, 3, 7.3, 12, 25}: relative error < 1e-25.
  - 801-point grid: B ∈ [0.6, 0.835144], G ∈ [0.2, 0.287279], inside CW.2; B(5/2) = 3/5, G(5/2) = 1/5 to 1e-30.
  - Certified ρ(L_k) from DISC-0206–0208 (k = 1, 2, 3, 4, 5, 12) lie inside CW.3's bracket.
  - Exact 2^n path-sum ratios at s = 3/2 (n = 18) for k = 1, 2, 13, 20 lie inside the bracket; k = 1, 2 match CT/CU to < 1e-6 relative; k = 13 estimate 2.11344e-7 ∈ [2.0913e-7, 2.1486e-7], k = 20 estimate 9.57775e-11 ∈ [9.55998e-11, 9.63483e-11].
- Not checked independently: the 160-bit arb cover itself (only a float grid, which cannot certify extremes between grid points).

## Experimental Validation
Computational only.

## Mathematical Status
Theorem (exact construction + interval-certified constants, computer-assisted).

## Patent Relevance
None. The repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0208 → DISC-0209 (mathematical): CV's "nothing uniform in k" open item addressed for ρ; CV's 3^k ρ → 1/3 observation proved; CV.7 lower half extended. DISC-0207, DISC-0206 → DISC-0209 (mathematical): CW.4 consistency with CU.3/CT.3. DISC-0190s (CE's r, k = 0) → DISC-0209 (mathematical): CW.4.

## Open Questions
q^(k) → −1/3 (HEURISTIC); uniform-in-k rate for inf R_n^(k); the exact geometric rate of 3^{k+1}ρ(L_k) − 1 (bracketed in [0.5999, 0.8352]; this h_k cannot do better); monotonicity of 3^k ρ(L_k) for k ≥ 13; circle eigenvalues; CF.3's general-f constant; λ_6, a_6; Ψ_info / Stage 2 still blocked.

## Next Experiments
Iterate the construction (use h_k + c·L_k h_k or a second-order coboundary through σ_2) to tighten the bracket towards the float ratio ≈ 0.779; a perturbation bound for ν_2^(k) around the single-branch operator to attack q^(k) → −1/3.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at 572ca675ce2e; `pip install python-flint mpmath`; `python3 scripts/gasket_fractional_profile_level_uniform_k.py` (about 3 s). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_CW.py` (about 60 s, mpmath).

## Evidence Log
- 2026-10-30 ~10:05 PM EDT: repo witness EXIT 0 (2.3 s); e.g. CW.3 ρ(L_20) ∈ [9.559976274e-11, 9.634826847e-11]; observation ratios 0.77968, 0.77910 at k = 10, 11. Repo tests 3 passed.
- Independent check 31/31 PASS (first run).

## Change History
- 2026-10-30: created from IFI 572ca675ce2e.

## Note (2026-10-30, added after DISC-0210)
IFI 4dc70c635d0b (Theorem CX) collapses this record's rate bracket [0.5999, 0.8352] to the exact rate B* = B(3/2) = 0.7773760276… with (3^{k+1}ρ(L_k) − 1)/(G* B*^k) → 1, and proves 3^k ρ(L_k) strictly decreasing for every k (this record's open item k ≥ 13). See DISC-0210. The text above is preserved unchanged; q^(k) → −1/3 is still HEURISTIC.
