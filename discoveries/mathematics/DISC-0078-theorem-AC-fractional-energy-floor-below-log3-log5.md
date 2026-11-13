# Discovery: Fractional energy floor for every α < log3/log5 on the gasket (Theorem AC)

## Discovery ID

DISC-0078

## Status

THEOREM

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0076 / DISC-0077.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 51789b3ef3c56d6e678f9df35dd276a1c8657a87. Paths: GASKET.md "Theorem AC. The energy floor holds for every α < log 3/log 5" (Assumption incl. ESTABLISHED network facts, Theorem AC, Proof: Cells / Low modes are flat / Spectral mass / Gap / Layer cake / Duality, Witness, Kept Failure AC.1, NOT THIS); GASKET.md item 4 now cites AA–AC; scripts/gasket_fractional_capacity_floor.py (new); scripts/cli.py; CLAIM_STATUS.md (new row "Fractional energy floor for every α<log3/log5" VERIFIED; the α<1/2 row now says the window [1/2, log3/log5) is closed by AC; α=0.45 OPEN row extended); README.md Sequel paragraph.

## Original Evidence

For every α∈(0,γ), γ=log3/log5≈0.682606, and every level n≥1: Q_α(u_n) ≥ (9/4)/C_AC(α), C_AC(α)=(2γ/(γ−α))·40^{α/γ}, hence ‖F_frac(n,α)‖=Q_α√21/7 ≥ 9√21/(28 C_AC). With Theorem K, γ is the exact threshold for a level-uniform floor; α=γ undecided. Theorem AB item 4 (‖F‖→0 ⇔ ρ_n→0) extends to every α<γ. Constants: C_AC(0.45)≈66.790994, floors 0.033687 (α=0.45, weaker than AA's 0.128335), 0.020184 (0.50), 0.005319 (0.60), 0.000109 (0.68).

## Discovery

A level-uniform bound R_α(n)=v^T(L^α)^+v ≤ C_AC(α) for v=e_a−e_b, from (i) cell resistance diameter ≤(8/3)(5/3)^k, (ii) low-mode flatness ⇒ spectral mass μ((0,s]) ≤ 80 s^γ, (iii) spectral gap λ_1(G_n) ≥ 5^{−n}/4, (iv) layer-cake integration split at s_*=40^{−1/γ}; then Cauchy–Schwarz duality with u_a−u_b=3/2.

## Why It Matters

Closes the window α∈[1/2,γ) left open by DISC-0072 (AA's path comparison has spectral dimension 1); with DISC-0076 the α=0.45 question remains exactly lim ρ_n. Does not bound combinatorial ‖F‖ or ρ_n from below; DISC-0034 stays OPEN. Not thrust.

## Derivation

Repository proof, checked step by step in this archive (no gap found):
1. Corner-to-corner resistance of G_k is (2/3)(5/3)^k (G_0 triangle: 2/3; Kigami renormalization 5/3).
2. Nested-corner chain + triangle inequality + Rayleigh: R(x,c_k) ≤ Σ_{j<k}(2/3)(5/3)^j=(5/3)^k−1; diameter of a level-k cell measured in G_n ≤ 2((5/3)^k−1)+(2/3)(5/3)^k ≤ (8/3)(5/3)^k.
3. If E(g)≤s‖g‖² then (g(x)−g(y))² ≤ R_k s‖g‖²; averaging g(x)² ≤ 2g(y)²+2(g(x)−g(y))² over the N(k)=(3^{k+1}+3)/2 vertices of the cell gives max g² ≤ K_s‖g‖², K_s=2/N(k)+2R_k s.
4. g=P_{(0,s]}v: ‖g‖²=g(a)−g(b) ≤ 2√K_s‖g‖ ⇒ μ((0,s]) ≤ 4K_s; for s∈[5^{−(k+1)},5^{−k}), 2/N(k) ≤ (4/3)3^{−k}, 2R_k s ≤ (16/3)3^{−k}, and 3^{−k}=(5^{−k})^γ ≤ 3s^γ ⇒ μ ≤ 80 s^γ.
5. Σ_{x,y}(f(x)−f(y))² = 2N‖f‖² ≤ N²R_nE(f) for f⊥𝟙 ⇒ λ_1 ≥ 2/(N R_n) ≥ 2/(8·5^n)=5^{−n}/4 > 5^{−(n+1)}, so μ vanishes below 5^{−(n+1)} and μ ≤ min(2,80s^γ) for all s.
6. λ^{−α}=α∫_λ^∞ s^{−α−1}ds and Tonelli ⇒ R_α = α∫ s^{−α−1}μ((0,s])ds ≤ 80α s_*^{γ−α}/(γ−α)+2s_*^{−α} = (2γ/(γ−α))s_*^{−α}; s_*^{−α}=40^{α/γ}; finite iff α<γ.
7. Duality: (3/2)² = (u^T v)² ≤ Q_α(u)·R_α(n).

## Assumptions

Spectral calculus (GASKET item 4); corner data (1,−1/2,0); standard network facts (effective resistance is a metric, Rayleigh monotonicity, corner resistance (2/3)(5/3)^k); Theorem K pairing (DISC-0032). No Löwner–Heinz needed.

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_AC.log` (repository witness at 51789b3ef, EXIT 0, 101 PASS, 0 FAIL) and `/workspace/scratch-ifi/indep_theorem_AC.py` / `indep_theorem_AC.log` (own builder `/workspace/scratch-ifi/sg_indep_common.py`, no repo import; 143 PASS, ARCHIVE_INDEP_THEOREM_AC_PASS), dense through level 7 (N=3282; level 7 not in repo):
- corner resistance (2/3)(5/3)^k exact to 1e−8 for k=0..7 (G_7: 23.814967); max_x min_corner R ≤ (5/3)^k−1 (G_7: 13.098 ≤ 34.722); diameter ≤ (8/3)(5/3)^k (G_7: 23.815 ≤ 95.260); in-G_n level-k cell diameters ≤ 0.23·bound at level 7;
- λ_1 ≥ 2/(N·diam) ≥ 5^{−n}/4 at every level (level 7: 2.3119e−4 ≥ 2.56e−5 ≥ 3.2e−6; λ_1·5^n → ≈18.06);
- per eigenvalue s ≥ 5^{−(n+1)}: max g²/(K_s‖g‖²) ≤ 1, μ/(4K_s) ≤ 1, μ ≤ min(2,80s^γ); max_{s<1} μ/s^γ = 0, 1.1814, 1.0362, 0.9796, 0.9606, 0.9544, 0.9523 (levels 1–7);
- C_AC reproduced by independent mpmath quadrature of α∫s^{−α−1}min(2,80s^γ)ds for α∈{0.05,…,0.682}; GASKET constants match to 5e−7;
- R_α(n) ≤ C_AC and Q ≥ (9/4)/R ≥ floor for α∈{0.10,0.25,0.45,0.50,0.55,0.60,0.65,0.68,0.682}, n=1..7 (e.g. R_0.45(7)=2.400, Q_0.45(7)=0.972232; R_0.682(7)=4.314 vs C_AC=89789);
- level-6 R and Q match GASKET; at α=γ, R_γ(n) grows ≈0.517 per level (log-divergent), so the route gives nothing at the endpoint — consistent with "α=γ undecided";
- AA vs AC: both valid lower bounds; crossovers at α≈0.2072 and ≈0.4936 (AC stronger below 0.2072 and on (0.4936,1/2), AA stronger between); no inconsistency with DISC-0072 constants.

## Prior Art

Kigami resistance renormalization 5/3 on the Sierpinski gasket; resistance-form Poincaré / Nash-type spectral bounds; Weyl-type spectral counting with exponent d_s/2=log3/log5 (Fukushima–Shima, Kigami–Lapidus); layer-cake / Tonelli; Cauchy–Schwarz duality. The proof is a classical-ingredient argument applied to this repository's audit functional. Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only (complete proof in the repository, verified here). Derivative of classical SG analysis in technique; not a novelty claim and not a Stage-1 / claim-level raise. Constant 80 is crude (repo and archive both see ≤1.19).

## Falsification Attempts

Rebuilt independently through level 7; checked each inequality per eigenvalue rather than only the end bound; probed α→γ and α=γ. Found one witness-text inaccuracy only: GASKET says "max_{s<1} μ((0,s])/s^γ ≤ 0.98" through level 6, but levels 2 and 3 give 1.1814 and 1.0362 (the repo's own log shows the same). The proof uses 80, so this does not affect the theorem.

## Experimental Validation

None (pure mathematics / finite numerical witness).

## Mathematical Status

Proved in-repo; proof and witness verified. Scope change for an existing row, recorded as a graph edge only: DISC-0072's "window α∈[1/2, log3/log5] stays OPEN" is superseded for [1/2,γ) by this row; DISC-0072's status and text are not edited. DISC-0034 unchanged (OPEN).

## Patent Relevance

None.

## Related Discoveries

- DISC-0072. Mathematical. Theorem AA (α<1/2); scope extended here.
- DISC-0076. Mathematical. Theorem AB item 4 extended to α<γ.
- DISC-0079. Failed hypothesis. No floor above γ.
- DISC-0032. Mathematical. Theorems J/K/L (pairing; K gives the upper threshold).
- DISC-0034. Conjecture. Combinatorial α=0.45 limit still OPEN.

## Open Questions

Floor at α=γ exactly. Combinatorial ‖F(n,0.45)‖ / lim ρ_n zero vs positive (OPEN).

## Next Experiments

None from the archive.

## Reproduction Instructions

`git checkout 51789b3ef3c56d6e678f9df35dd276a1c8657a87 && python3 scripts/gasket_fractional_capacity_floor.py`. Archive: `python3 /workspace/scratch-ifi/indep_theorem_AC.py 7`. Logs: `/workspace/scratch-ifi/repo_theorem_AC.log`, `/workspace/scratch-ifi/indep_theorem_AC.log`.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Theorem AC at 51789b3ef3c56d6e678f9df35dd276a1c8657a87; repo witness EXIT 0; independent check ARCHIVE_INDEP_THEOREM_AC_PASS. Repository description still matches its claim fence.

## Change History

- 2026-10-15. Initial archive entry.
