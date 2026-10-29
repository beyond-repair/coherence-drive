"""Independent checks of informational-flux-identity Theorem CC (commit cb00b500b900).
No repository code imported. Checks: CC.2 transfer weight T=(2-t)/(6-t), T(-5)=7/11,
nonnegative branch weights on p^-1([-5,0]), partial fractions, regular remainder,
k=1/c; CC.1 Cauchy-Schwarz lemma Im(1/r)>=Im z on random probability measures;
CC.4 level counts of p^-k(-3) in (psi(-5), psi(-1)] for k<=14 (psi endpoints as printed)."""
import random, sys
import numpy as np, sympy as sp
from mpmath import mp, mpf, sqrt
y, t, z = sp.symbols('y t z')
k = (y+2)*(y+5)/(y+6); p = y**2+5*y; dp = sp.diff(p, y)
roots = sp.solve(sp.Eq(p, t), y)
T = sp.factor(sp.simplify(sum(k.subs(y, r)/dp.subs(y, r) for r in roots)))
ok = sp.simplify(T-(t-2)/(t-6)) == 0 and T.subs(t, -5) == sp.Rational(7, 11) and T.subs(t, 0) == sp.Rational(1, 3)
ok &= sp.simplify(sp.diff(T, t) + 4/(6-t)**2) == 0
w = [float((k.subs(y, r)/dp.subs(y, r)).subs(t, tv)) for tv in np.linspace(-5, -1e-9, 101) for r in roots]
ok &= min(w) >= -1e-12
ok &= sp.simplify(1/(t-(z**2+5*z)) - sum(1/(dp.subs(y, r)*(r-z)) for r in roots)) == 0
ok &= sp.simplify((k.subs(y, z)-k)/(y-z) + (y*z+6*y+6*z+32)/((y+6)*(z+6))) == 0
ok &= sp.simplify(1/((z+6)/((z+2)*(z+5))) - k.subs(y, z)) == 0
print('CC.2 sympy checks', ok)
bad = 0
for _ in range(5000):
    n = random.randint(1, 8); wt = np.random.rand(n); wt /= wt.sum(); l = np.random.rand(n)*8
    zz = complex(random.uniform(-12, 12), random.uniform(1e-4, 6))
    if (1/sum(wt/(l+zz))).imag < zz.imag*(1-1e-9): bad += 1
print('CC.1 Cauchy-Schwarz violations', bad); ok &= bad == 0
mp.dps = 50
a, b = mpf('-3.850061912530890'), mpf('-0.950826643829326')
lev = [mpf(-3)]; counts = []
for _ in range(15):
    counts.append(sum(1 for x in lev if a < x <= b))
    lev = [c for s in lev for c in (-mpf(5)/2+sqrt(mpf(25)/4+s), -mpf(5)/2-sqrt(mpf(25)/4+s))]
print('CC.4 level counts', counts, sum(counts))
ok &= counts == [1, 0, 1, 3] + [5*2**(j-4) for j in range(4, 15)]
print('PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
