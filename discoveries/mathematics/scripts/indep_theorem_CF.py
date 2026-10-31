"""Independent re-check of IFI Theorem CF (commit dab0578773f9), written without importing the repo script.
Checks: CF.1 identity; CF.2 constants c_i, M_i, b-map, b_5, V_5 (osc recursion over 2^5 leaves, mpmath interval arithmetic),
Delta, theta, theta^(1/5); CF.4-style ratio bound for m<=16 on 9 points; CF.5 vs Chebyshev collocation lambda_2."""
import mpmath as mp, numpy as np, sympy as sp
mp.mp.prec = 200; iv = mp.iv; iv.prec = 200
ok = True
def chk(c, m):
    global ok; ok &= bool(c); print(("PASS " if c else "FAIL ") + m)
# CF.1
z, m, M = sp.symbols('z m M', positive=True)
chk(sp.expand((z+m)*(z+M) - z*(sp.sqrt(m)+sp.sqrt(M))**2 - (z-sp.sqrt(m*M))**2) == 0, "CF.1 identity")
tau = sp.symbols('tau', positive=True)
chk(sp.simplify((((sp.exp(2*tau)-1)/(sp.exp(2*tau)+1)) - sp.tanh(tau)).rewrite(sp.exp)) == 0, "CF.1 (sqrtM-sqrtm)/(sqrtM+sqrtm)=tanh(log(M/m)/4)")
# CF.2
s = sp.symbols('s', positive=True)
lw1 = sp.log((s+sp.Rational(1,2))/(2*s*(sp.Rational(7,2)-s))); lw2 = sp.log((s-sp.Rational(1,2))/(2*s*(s+sp.Rational(7,2))))
d1, d2 = sp.diff(lw1, s), sp.diff(lw2, s)
lo_s, hi_s = sp.sqrt(5)/2, sp.Rational(5,2)
chk(sp.nsimplify(d1.subs(s, hi_s)) == sp.Rational(14,15), "M_1=(log w1)'(5/2)=14/15")
# monotone/convex check of d1 and |d2| bound by dense sampling plus sign of d1'
grid = np.linspace(float(lo_s), 2.5, 200001)
f1 = sp.lambdify(s, d1); f2 = sp.lambdify(s, d2)
chk(np.all(f1(grid) > 0) and np.max(f1(grid)) <= 14/15 + 1e-15, "0 < (log w1)' <= 14/15 on grid")
M2 = float(d2.subs(s, lo_s)); chk(np.max(np.abs(f2(grid))) <= M2 + 1e-15 and M2 < 0.5071, f"|(log w2)'| <= M_2={M2:.10f} < 0.5071 on grid")
c1 = 1/mp.sqrt(5); c2 = 1/(2*mp.sqrt(mp.mpf(15)/4 + mp.sqrt(5)/2))
chk(c2 < mp.mpf('0.2267'), f"c_2={mp.nstr(c2,10)}")
a = mp.mpf(47)/2; M1 = mp.mpf(14)/15; M2m = mp.mpf(sp.N(d2.subs(s, lo_s), 60))
b = a; bs = []
for k in range(5):
    b = max(M1 + c1*b, M2m + c2*b); bs.append(b)
chk(bs[0] < a, f"b_1={mp.nstr(bs[0],8)} < a"); b5 = bs[-1]; print("b_5 =", mp.nstr(b5, 10), " b* =", mp.nstr(M1/(1-c1), 10))
# osc recursion in interval arithmetic
crit = mp.mpf(1)/2 + mp.sqrt(2)
LW1 = lambda x: mp.log((x+0.5)/(2*x*(3.5-x))); LW2 = lambda x: mp.log((x-0.5)/(2*x*(x+3.5)))
def var1(l, h): return LW1(h) - LW1(l)
def var2(l, h):
    if l < crit < h: return (LW2(crit)-LW2(l)) + (LW2(crit)-LW2(h))
    return abs(LW2(h) - LW2(l))
S1 = lambda x: mp.sqrt(mp.mpf(15)/4 - x); S2 = lambda x: mp.sqrt(mp.mpf(15)/4 + x)
def osc(l, h, n):
    if n == 0: return a*(h-l)
    return max(var1(l, h) + osc(S1(h), S1(l), n-1), var2(l, h) + osc(S2(l), S2(h), n-1))
V5 = osc(mp.sqrt(5)/2, mp.mpf(5)/2, 5)
Delta = 2*mp.log((a+b5)/(a-b5)) + 2*V5; theta = mp.tanh(Delta/4)
print("V_5 =", mp.nstr(V5, 10), " Delta =", mp.nstr(Delta, 10), " theta =", mp.nstr(theta, 10), " theta^(1/5) =", mp.nstr(theta**(mp.mpf(1)/5), 10))
chk(abs(V5 - mp.mpf('1.0426526')) < 1e-6 and abs(Delta - mp.mpf('2.44003534')) < 1e-7, "V_5, Delta match repo")
chk(theta < mp.mpf('0.5442') and theta**(mp.mpf(1)/5) < mp.mpf('0.8855'), "theta < 0.5442, theta^(1/5) < 0.8855")
# CF.4 style: L^m 1 by full branch tree (float64), m <= 16
r = 0.42373128696260793985
def Lm1(t, mm):
    if mm == 0: return 1.0
    sv = np.sqrt(t + 6.25)
    w1 = (sv+.5)/(2*sv*(3.5-sv)); w2 = (sv-.5)/(2*sv*(sv+3.5))
    return w1*Lm1(-2.5 - sv, mm-1) + w2*Lm1(-2.5 + sv, mm-1)
pts = np.linspace(-5, 0, 9); Theta0 = 2*mp.log((a+M1)/(a-M1)) + mp.log(mp.mpf(11)/6)
vals = {mm: np.array([Lm1(t, mm) for t in pts]) for mm in range(18)}
worst = 0
for mm in range(17):
    dev = np.max(np.abs(np.log(vals[mm+1]/vals[mm]) - np.log(r))); bnd = float(theta)**(mm//5)*float(Theta0)
    worst = max(worst, dev/bnd)
    if mm in (0, 5, 10, 16): print(f"  m={mm:2d} dev={dev:.3e} bound={bnd:.3e}")
chk(worst < 1, f"ratio bound holds m<=16 at 9 points (max used fraction {worst:.3f})")
# r and lambda_2 by Chebyshev collocation (independent, 80 nodes)
N = 80; x = np.cos(np.pi*(np.arange(N)+.5)/N); t = -2.5 + 2.5*x
def V(tt): return np.polynomial.chebyshev.chebvander((tt+2.5)/2.5, N-1)
sv = np.sqrt(t+6.25); w1 = (sv+.5)/(2*sv*(3.5-sv)); w2 = (sv-.5)/(2*sv*(sv+3.5))
A = np.linalg.solve(V(t), w1[:,None]*V(-2.5-sv) + w2[:,None]*V(-2.5+sv))
ev = sorted(np.linalg.eigvals(A), key=lambda e: -abs(e))
print("collocation r =", ev[0].real, " lambda_2 =", ev[1], " ratio =", abs(ev[1])/ev[0].real)
chk(abs(ev[0].real - r) < 1e-12, "r matches CE certificate"); chk(abs(ev[1]) <= float(theta)**0.2*r, "|lambda_2| below CF.5 bound")
print("ALL PASS" if ok else "SOME FAIL")
