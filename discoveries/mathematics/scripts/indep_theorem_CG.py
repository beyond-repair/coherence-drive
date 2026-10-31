"""Independent re-check of IFI Theorem CG (commit 8364d9497c57), no repo imports.
Method differs from the repo (H^2 Taylor matrix + arb resolvents): Chebyshev collocation in t on [-5,0]
at two sizes in mpmath (160 bits), plus symbolic fixed-point trace and power-iteration deviation ratios."""
import mpmath as mp, sympy as sp, numpy as np
mp.mp.prec = 160
ok = True
def chk(c, m):
    global ok; ok &= bool(c); print(("PASS " if c else "FAIL ") + m)
def spec(N):
    x = [mp.cos(mp.pi*(j+mp.mpf(1)/2)/N) for j in range(N)]
    t = [mp.mpf(-5)/2 + mp.mpf(5)/2*xi for xi in x]
    def T(u):  # Chebyshev values T_0..T_{N-1} at u in [-1,1]
        v = [mp.mpf(1), u]
        for n in range(2, N): v.append(2*u*v[-1]-v[-2])
        return v[:N]
    V = mp.matrix([T(xi) for xi in x]); B = mp.matrix(N, N)
    for i, ti in enumerate(t):
        s = mp.sqrt(ti + mp.mpf(25)/4)
        w1 = (s+mp.mpf(1)/2)/(2*s*(mp.mpf(7)/2-s)); w2 = (s-mp.mpf(1)/2)/(2*s*(s+mp.mpf(7)/2))
        a1 = T((-mp.mpf(5)/2 - s + mp.mpf(5)/2)/(mp.mpf(5)/2)); a2 = T((-mp.mpf(5)/2 + s + mp.mpf(5)/2)/(mp.mpf(5)/2))
        for n in range(N): B[i, n] = w1*a1[n] + w2*a2[n]
    E = mp.eig(mp.inverse(V)*B, left=False, right=False)
    return sorted(E, key=lambda e: -abs(e))
E1, E2 = spec(48), spec(64)
for k in range(5): print(f"  mu_{k+1}: N=48 {mp.nstr(mp.re(E1[k]),20)}  N=64 {mp.nstr(mp.re(E2[k]),20)}  |Im|={mp.nstr(abs(mp.im(E2[k])),3)}")
r_cert = mp.mpf('0.42373128696260793985253216132843923')
l2, l3 = mp.mpf('-0.0731138175123995805'), mp.mpf('-0.0170676440626237159')
chk(abs(E2[0]-r_cert) < 1e-14, "top eigenvalue = CE's r within 1e-14")
chk(abs(E2[1]-l2) < 1e-13, "lambda_2 inside repo disk (+-1e-13)")
chk(abs(E2[2]-l3) < 1e-12, "lambda_3 inside repo disk (+-1e-12)")
chk(all(abs(mp.im(E2[k])) < 1e-20 for k in range(3)), "top three real")
chk(abs(E2[3]) < 1e-3 and abs(E2[3]) > 1e-4, f"4th eigenvalue {mp.nstr(mp.re(E2[3]),8)} in 1e-4<|mu|<1e-3 (repo float -2.1645e-4)")
chk(abs(E1[1]-E2[1]) < 1e-25, "lambda_2 stable across N=48,64")
chk(abs(mp.re(E2[1])/r_cert - mp.mpf('-0.172547602129')) < 1e-11, "lambda_2/r = -0.172547602129")
chk(abs(mp.re(E2[2])/r_cert - mp.mpf('-0.0402794048676')) < 1e-11, "lambda_3/r = -0.0402794048676")
# trace identity via fixed points (s-coordinate)
s = sp.symbols('s', positive=True)
w1 = (s+sp.Rational(1,2))/(2*s*(sp.Rational(7,2)-s)); w2 = (s-sp.Rational(1,2))/(2*s*(s+sp.Rational(7,2)))
g1 = sp.sqrt(sp.Rational(15,4)-s); g2 = sp.sqrt(sp.Rational(15,4)+s)
x1 = sp.solve(sp.Eq(s**2+s-sp.Rational(15,4),0), s); x2 = sp.solve(sp.Eq(s**2-s-sp.Rational(15,4),0), s)
x1 = [v for v in x1 if v > 0][0]; x2 = [v for v in x2 if v > 0][0]
tr = sp.nsimplify(w1.subs(s,x1)/(1-sp.diff(g1,s).subs(s,x1)) + w2.subs(s,x2)/(1-sp.diff(g2,s).subs(s,x2)))
chk((x1, x2, tr) == (sp.Rational(3,2), sp.Rational(5,2), sp.Rational(1,3)), f"fixed points 3/2, 5/2, holomorphic trace {tr}")
chk(abs(mp.fsum(E2) - mp.mpf(1)/3) < 1e-25, f"sum of collocation eigenvalues = 1/3 (dev {mp.nstr(mp.fsum(E2)-mp.mpf(1)/3,3)})")
# deviation ratio of L^m 1 at t=-3 tends to lambda_2/r with alternating sign
def L(f):
    def g(t):
        sv = mp.sqrt(t + mp.mpf(25)/4)
        return (sv+0.5)/(2*sv*(3.5-sv))*f(-2.5-sv) + (sv-0.5)/(2*sv*(sv+3.5))*f(-2.5+sv)
    return g
def Lm1(t, m):
    if m == 0: return mp.mpf(1)
    sv = mp.sqrt(t + mp.mpf(25)/4)
    return (sv+0.5)/(2*sv*(3.5-sv))*Lm1(-2.5-sv, m-1) + (sv-0.5)/(2*sv*(sv+3.5))*Lm1(-2.5+sv, m-1)
v = [Lm1(mp.mpf(-3), m) for m in range(15)]
d = [mp.log(v[m+1]/v[m]) - mp.log(r_cert) for m in range(14)]
rat = d[13]/d[12]; print("  deviation ratio m=12->13:", mp.nstr(rat, 12))
chk(abs(rat - mp.mpf('-0.172547602129')) < 1e-4, "power-iteration deviation ratio approaches lambda_2/r")
print("ALL PASS" if ok else "SOME FAIL")
