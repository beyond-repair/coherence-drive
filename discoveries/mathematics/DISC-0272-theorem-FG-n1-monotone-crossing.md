# Discovery: Theorem FG, the n = 1 step of monotonicity in n: G_2 − G_1 has exactly one zero β_c ∈ (−0.5679, −0.5677) on (−1, 1)

## Discovery ID
DISC-0272

## Status
THEOREM (mathematical sense only) for FG.1–FG.4 (Arb certificates plus FE.3 for differentiation under the integral; real α only). FG.5 OBSERVED. Method KNOWN (FF's ball evaluator, Arb rigorous integration, monotone-in-α endpoint bounds, intermediate value theorem with a derivative lower bound). Whether the constant β_c is new is UNRESOLVED (no literature search). **Status change: DISC-0271 FF.3 "sign of G_2 − G_1 on (−13/20, −3/8)" OPEN / OBSERVED → THEOREM (exactly one simple zero β_c).** No new kept failure; FF.2 stands. Monotonicity for n ≥ 11 stays OPEN.

## Date Discovered
2026-11-23. The commit is from 8:34 AM EST and was indexed at about 9:20 AM EST.

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 0a6f9431aee9f325cab7e0c8fd46928106beef9b (2026-11-23T13:34:33Z = 2026-11-23 8:34:33 AM EST). Parent: 192340ee69ca (Theorem FF, DISC-0271).

## Original Evidence
- GASKET.md §Theorem FG (+14 lines, including one Reproduce line).
- scripts/gasket_fractional_corner_h_alpha_n1_monotone_crossing.py (new, 198 lines; python-flint arb 128 bits, exit 1 on any failure; repo reports 811.5 s wall under load).
- CLAIM_STATUS.md (+1 row); tests/test_flux_identity.py (+16 lines, HAlphaN1MonotoneCrossingTests, float only).

## Discovery
With Δ(α) = G_2(α) − G_1(α) = D_1 − D_2 = ∫_0^∞ t^−α (h_1 − h_2) dt:
- FG.1: Δ(−0.5679) ∈ [−0.0005701162, −0.0003770654] < 0; Δ(−0.5677) ∈ [0.0004796669, 0.0006722563] > 0.
- FG.2: Δ′ ≥ 1.6847712 > 0 on [−13/20, −1/2] (piece bounds 10.446, 7.546, 5.390, 3.783, 2.582, 1.685), so Δ′ ≥ 3.783 on [−0.575, −0.55].
- FG.3: Δ ≥ 0.14621213 > 0 on [−1/2, −3/8].
- FG.4: with FF.2, Δ has exactly one zero β_c on (−1, 1), β_c ∈ (−0.5679, −0.5677), simple; G_2 < G_1 on (−1, β_c), G_2 > G_1 on (β_c, 1). Hence G_1 < G_2 < … < G_11 < W/2 for real α ∈ (β_c, 1). β_c ≠ α_c (FD's α_c ∈ (−0.7408, −0.7406)).
- FG.5 (OBSERVED): β_c ≈ −0.56783; Δ′ changes sign near −0.39.

## Why It Matters
It closes the n = 1 gap left open by FF, so the monotone chain starting at G_1 is now exactly delimited on real α ∈ (−1, 1): it holds precisely for α > β_c. It also separates two different thresholds (α_c for G_1 vs W/2, β_c for G_1 vs G_2).

## Derivation
Checked here, not re-derived in full. Δ = D_1 − D_2 follows from D_n = W/2 − G_n. Δ′ under the integral is FE.3 (DISC-0270), valid on −1 < Re α < 1 for n = 1, 2. The FG.2 endpoint rule is the same monotone-in-α argument as FF (for fixed t, α ↦ (−ln t) t^−α g(t) is monotone in α), so the block minimum is the min of endpoint values. FG.4 is the intermediate value theorem plus strict monotonicity on [−13/20, −1/2], with FG.3 and FF.2 excluding zeros elsewhere in (−1, 1). Simplicity follows from Δ′(β_c) ≥ 3.783 > 0. The repo's FG.5 explains why positivity on [−1/2, −3/8] is certified directly (Δ is not monotone there).

## Assumptions
As stated by the repository: FF's list (FC's FB.1, EX.1, EU.1/EU.3/EU.4, BD.4, EV.1, EV.2; FC.1's ball evaluator and FC.2's tail bounds, including f_2 ≤ 3²/(t ψ_1(t/5)) with ψ_1(t/5) ≥ (t/25)²); FF.2; FE.3. Inherits the conditional chain of earlier gasket theorems (BG.3, BI.4). Rigour of python-flint 0.9.0's integrator and real_min assumed (textbook tool). Real α only.

## New Results
A certified bracket of width 2·10^−4 for the unique n = 1 monotonicity threshold β_c, and its simplicity.

## Prior Art
Arb interval integration, monotone-parameter bounds and IVT-plus-derivative root isolation are standard. No literature search on these specific constants.

## Novelty Analysis
Method KNOWN. The constant β_c is specific to this construction; novelty UNRESOLVED.

## Falsification Attempts
- Repository script rerun on the box at 0a6f9431aee9: repo script EXIT 0 (925 s wall on the box under load ~48, 'all FG checks passed').
- Repository CI test HAlphaN1MonotoneCrossingTests: 1 passed (1.05 s).
- Independent of repository code: /workspace/corpus-discovery/ff_check.py (mpmath 30 digits, the DISC-0271 evaluator), Δ = G_2 − G_1:
  - α = −0.5679: −0.000377087291 (inside the certified interval [−0.0005701162, −0.0003770654], at its upper end). **Held.**
  - α = −0.5677: +0.000672234440 (inside [0.0004796669, 0.0006722563], at its upper end). **Held.** Linear interpolation gives β_c ≈ −0.567828, matching FG.5's −0.56783.
  - α = −0.5, −0.45, −0.4, −0.375: 0.230410, 0.295396, 0.314351, 0.313489, all ≥ 0.14621 (FG.3) ✓; Δ(−0.4) > Δ(−0.375) confirms Δ is decreasing near −0.39 (FG.5) ✓.
  - Secant slopes: [−0.65, −0.6] 11.08 (≥ 10.446 ✓), [−0.6, −0.5679] 6.52, [−0.5677, −0.5] 3.39 (all consistent with FG.2's piece lower bounds).
  - As in DISC-0271, the mpmath values sit at the upper ends of the Arb intervals; the intervals still contain them.
- Logic: checked the IVT/monotonicity chain, the exclusion of other zeros by FF.2 and FG.3, and that β_c ≠ α_c. No contradiction between commit message, GASKET.md, CLAIM_STATUS.md and the test.

## Experimental Validation
Not applicable (pure mathematics). Functions on a graph, not a flux, not thrust; the repo's Stage 2 remains blocked.

## Mathematical Status
THEOREM (FG.1–FG.4); OBSERVED (FG.5); OPEN (n ≥ 11, non-real α, α ≤ −1).

## Patent Relevance
None.

## Related Discoveries
- DISC-0271 (Theorem FF): FF.3 OPEN → THEOREM; FF.2 used to exclude zeros on (−1, −13/20]. Label: mathematical.
- DISC-0270 (Theorem FE): FE.3 justifies Δ′ under the integral. Label: mathematical.
- DISC-0269 (Theorem FD): parallel n = 1 crossing α_c; distinct threshold. Label: mathematical.
- DISC-0268 (Theorem FC): FC.1 evaluator and FC.2 tails reused. Label: computational.

## Open Questions
Monotonicity for n ≥ 11 (needs a rate for 3^n D_n → V(α)); closed form or characterization of β_c; α ≤ −1 and non-real α.

## Next Experiments
A rate for 3^n D_n → V(α) sharp enough to give m > C/3 beyond n = 11.

## Reproduction Instructions
`python3 scripts/gasket_fractional_corner_h_alpha_n1_monotone_crossing.py` at informational-flux-identity 0a6f9431aee9 (~3–14 min, python-flint 0.9.0). Independent: `python3 ff_check.py <alpha> 1` (mpmath).

## Evidence Log
- 2026-11-23 ~9:20 AM EST: commit read; logic checked; CI test passed; independent mpmath checks held; repo script rerun: repo script EXIT 0 (925 s wall on the box under load ~48, 'all FG checks passed').

## Change History
- 2026-11-23 ~9:20 AM EST: created.
