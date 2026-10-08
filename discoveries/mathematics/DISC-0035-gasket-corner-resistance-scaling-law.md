# Discovery: Corner-resistance scaling law for the fractional gasket audit norm (archive-derived)

## Discovery ID

DISC-0035

## Status

CONJECTURE

## Date Discovered

2026-10-08 (America/New_York). Archive-derived in the same pass as DISC-0031. Not a statement the repository makes.

## Source Repositories

Data from beyond-repair/informational-flux-identity, branch main, HEAD 81ab02b501aef7df2f5478f55d67d50f93595d56: GASKET.md recorded α = 0.45 norms for levels 1–10 (levels 8–10 from scripts/gasket_fractional_matrix_free.py, evidence commit 5ab3ec92a3f13954ca471225d1802811ef663a34) and α = 0.10 norms for levels 1–6. Archive independent dense computation for levels 1–7 at six values of α (script below).

## Original Evidence

GASKET.md Kept Failures J.2 and J.4 test gap-contraction thresholds 5^{−0.45} and log 3/log 5. Neither is the observed limit.

## Discovery

Conjecture (archive). For α ∈ (0,1), α ≠ log 3/log 5, with ρ(α) = 5^α/3,

  1/‖F(n,α)‖ = A(α) + B(α) ρ(α)^n + (smaller terms),

so the ratio of successive differences of 1/‖F‖, and equally δ_{n+1}/δ_n, tends to ρ(α). Consequences if true: for α < log 3/log 5 (ρ < 1), ‖F(n,α)‖ → 1/A(α) > 0; for α > log 3/log 5 (ρ > 1), ‖F(n,α)‖ decays like (3·5^{−α})^n. Heuristic reading: the corner current is a series combination of a local corner resistance that stays O(1) and a global resistance whose discrete scaling is (5^α/3)^n, the same dichotomy as point capacity for subordinate processes on the gasket (α d_w versus d_h, with d_w/d_h = log 5/log 3).

## Why It Matters

At α = 0.45 it predicts a positive limit L ≈ 0.8211, which would settle the repository's Conjecture J.1 (DISC-0034) in the positive direction, and it explains why Kept Failure J.4 failed: the gap ratio heads to 0.687726, just above log 3/log 5 = 0.682606 but still below 1. It also suggests the Theorem K exponent n/2 (DISC-0032) is not sharp.

## Derivation

None rigorous. A scaling heuristic plus numerical fit. Not a theorem.

## Assumptions

As DISC-0032. The heuristic assumes the discrete minimizer energy splits into a scale-invariant local part and a global part rescaled by 3·5^{−α} per level.

## New Results

Ratios of successive differences of 1/‖F‖ (archive levels 1–7; last entry is levels 5,6,7):

| α | ρ = 5^α/3 | last three ratios |
| --- | --- | --- |
| 0.10 | 0.391540 | 0.399259, 0.395458, 0.393121 |
| 0.20 | 0.459910 | 0.467448, 0.463787, 0.461489 |
| 0.30 | 0.540219 | 0.547365, 0.543952, 0.541761 |
| 0.45 | 0.687726 | 0.693880, 0.691013, 0.689121 |
| 0.55 | 0.807816 | 0.813083, 0.810639, 0.809039 |
| 0.90 | 1.418900 | 1.420659, 1.419541, 1.419149 |

At α = 0.45 with the repository's levels 1–10: 0.688256, 0.687916, 0.687792 for the last three, approaching 0.687726 from above. The ρ-dependence rules out a universal constant such as log 3/log 5.

Out-of-sample test: A and B fitted on archive levels 6 and 7 at α = 0.45 predict the repository's independently computed (matrix-free) levels 8, 9, 10 as 0.8480342, 0.8394607, 0.8336645 against recorded 0.8480245, 0.8394423, 0.8336397 (relative error 1.1·10^{−5}, 2.2·10^{−5}, 3.0·10^{−5}). Refit on recorded levels 9 and 10: L(0.45) ≈ 0.821139, predicted ‖F(11)‖ ≈ 0.829695. Fit on levels 6,7 gives limits 1.410639 (α = 0.10), 1.277132 (0.20), 1.120952 (0.30), 0.821177 (0.45), 0.548253 (0.55), and A < 0 at α = 0.90 as the law requires above the threshold.

## Prior Art

The point-capacity threshold α d_w = d_h for stable-like processes on p.c.f. fractals and the gasket spectral dimension d_s = 2 log 3/log 5 (Fukushima–Shima; Kigami–Lapidus) are classical. The affine 1/‖F‖ law for this repository's audit functional was not searched; it may be a routine renormalization consequence. No novelty claimed.

## Novelty Analysis

CONJECTURE. Archive-derived and numerically supported; no proof, no prior-art search sufficient for a novelty candidate.

## Falsification Attempts

1. Six values of α on both sides of the threshold: the difference ratios approach 5^α/3 in every case (deviation at level 7 below 2·10^{−3}, shrinking over the last three levels).
2. Out-of-sample prediction of levels 8–10 at α = 0.45 from a two-level fit on a different code: agreement to 3·10^{−5}.
3. Checked the alternative "limit ratio = log 3/log 5": excluded at α = 0.45 by the recorded ratios and at every other α by the α-dependence.
Not broken.

## Experimental Validation

None (pure mathematics; numerics only).

## Mathematical Status

Open. Numerical evidence, levels ≤ 7 (six α) and ≤ 10 (α = 0.45).

## Patent Relevance

None.

## Related Discoveries

- DISC-0034. Mathematical. Would imply J.1 with L ≈ 0.821 and support J.2.
- DISC-0033. Computational. Explains why the J.2 and J.4 thresholds fail.
- DISC-0032. Mathematical. Suggests the Theorem K rate is (3·5^{−α})^n, not its square root.

## Open Questions

Prove the two-term law, or at least that Q_α(u_n) has a positive liminf for α < log 3/log 5 via a discrete point-capacity lower bound.

## Next Experiments

Repository matrix-free level 11 at α = 0.45 (falsifier: ‖F(11)‖ off 0.829695 by more than about 5·10^{−5}). Dense level 8 at other α.

## Reproduction Instructions

Python 3 with numpy only. `python3 indep_gasket.py 7 0.1,0.2,0.3,0.45,0.55,0.9` (about 6.5 minutes; level 7 dominates). Then take ratios of successive differences of 1/‖F‖.

```python
# Independent archive check of IFI GASKET.md audit norm (not repo code).
import numpy as np, sys, math, json, time
def build(n):
    # vertices as integer coords (x2^n scaled) via recursive triangle subdivision
    # use exact coords: corners A=(0,0),B=(2,0),C=(1,sqrt3) scaled by 2^n -> keys (2x, y_index)
    A=(0,0);B=(2*2**n,0);C=(2**n,2**n)  # (x in half-units, level-height units)
    tris=[(A,B,C)]
    for _ in range(n):
        new=[]
        for a,b,c in tris:
            mab=((a[0]+b[0])//2,(a[1]+b[1])//2);mbc=((b[0]+c[0])//2,(b[1]+c[1])//2);mca=((c[0]+a[0])//2,(c[1]+a[1])//2)
            new+= [(a,mab,mca),(mab,b,mbc),(mca,mbc,c)]
        tris=new
    idx={};edges=set()
    for t in tris:
        for v in t: idx.setdefault(v,len(idx))
        for i in range(3):
            u,v=idx[t[i]],idx[t[(i+1)%3]]; edges.add((min(u,v),max(u,v)))
    N=len(idx);L=np.zeros((N,N))
    for u,v in edges: L[u,v]-=1;L[v,u]-=1;L[u,u]+=1;L[v,v]+=1
    return L,[idx[A],idx[B],idx[C]]
alphas=[float(a) for a in sys.argv[2].split(',')]
out={}
for n in range(1,int(sys.argv[1])+1):
    t=time.time();L,C=build(n);N=L.shape[0]
    assert N==(3**(n+1)+3)//2
    lam,V=np.linalg.eigh(L);lam=np.clip(lam,0,None)
    I=[i for i in range(N) if i not in C]
    for a in alphas:
        La=(V*np.where(lam>1e-10,lam,0)**a)@V.T
        g=np.array([1.0,-0.5,0.0])
        u=np.zeros(N);u[C]=g
        u[I]=np.linalg.solve(La[np.ix_(I,I)],-La[np.ix_(I,C)]@g)
        nb=np.nonzero(L[C[0]]<0)[0]
        Ia=sum(1-u[j] for j in nb)
        Q=u@La@u
        Ifrac=(La@u)[C]
        out.setdefault(a,[]).append(dict(n=n,F=Ia*math.sqrt(21)/5,Q=Q,schur=(Ifrac/Ifrac[0]).tolist()))
    print(n,N,round(time.time()-t,1),flush=True)
json.dump({str(k):v for k,v in out.items()},open(f'out_{sys.argv[1]}.json','w'),indent=1)
for a,rows in out.items():
    F=[r['F'] for r in rows];Q=[r['Q'] for r in rows]
    d=[1-F[i]/F[i-1] for i in range(1,len(F))]
    print(f"alpha={a} 5^a/3={5**a/3:.6f}")
    print("  F",[f"{x:.9f}" for x in F])
    print("  Q",[f"{x:.6f}" for x in Q])
    print("  dratio",[f"{d[i]/d[i-1]:.6f}" for i in range(1,len(d))])
```

## Evidence Log

- 2026-10-08. Archive dense computation levels 1–7 (α = 0.45 matches GASKET.md to nine digits); fits and out-of-sample test as above.

## Change History

- 2026-10-08. Initial archive entry.
