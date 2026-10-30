#!/usr/bin/env python3
"""Placed in coherence-drive discoveries/mathematics/scripts; needs python-flint 0.9, mpmath. Part B needs F0FILE from
indep_theorem_CR_CS_dump_f0.py (otherwise skipped). Run log 2026-10-30: v1 aborted (c, R built at 53 bits: l_5 moved
3e-15, mu_6 to -1.4e-10 -- shows the non-normality); v2 31/34 (three tolerance errors of mine, see comments); v3 38/38.
Independent check of IFI Theorems CR (f847490267b1) and CS (9cb3b84d6b28).
Own matrix builder for M_N (closed-form weights/branches, DFT on |u|=1 in acb at 600-700 bits), own eigen-solver
(block subspace iteration + Rayleigh-Ritz, mpmath eig on the 8x8 Ritz matrix), no repo imports for the CR eigenvalue
part.  The a_5^N cross-check (part B) reuses the REPO's F0 Taylor coefficients (dumped by dump_f0.py from
co.taylor_coeffs / cn.F0_bound) and c0 = 3 sigma_-3 from the repo; only eigenvectors, projections and the point
evaluation are my own.  CS checks are interval-free arithmetic on stated constants and CC's 12-digit level sums.
Floats/approximations only: this is a falsification attempt, not a certificate.
"""
import sys, os, time
import mpmath
from mpmath import mp, mpf
from flint import acb, acb_mat, arb, arb_mat, ctx

ok = tot = 0
def chk(name, cond, info=""):
    global ok, tot
    tot += 1; ok += bool(cond)
    print(("PASS " if cond else "FAIL ") + name + (("  [" + info + "]") if info else ""), flush=True)

def build(N, K):
    c = arb(83) / 50; R = arb(8) / 5   # v1 bug: built at import (53-bit) -> l_5 moved 3e-15, mu_6 ~ -1.4e-10 (non-normality); see indep_v1_lowprec_c.log
    V = acb_mat(K, N + 1)
    for j in range(K):
        u = acb(arb(2 * j) / K).exp_pi_i(); s = c + R * u          # NB acb.exp_pi_i(arb) segfaults in flint 0.9
        v1 = ((arb(15) / 4 - s).sqrt() - c) / R; v2 = ((arb(15) / 4 + s).sqrt() - c) / R
        w1 = (s + arb(1) / 2) / (2 * s * (arb(7) / 2 - s)); w2 = (s - arb(1) / 2) / (2 * s * (s + arb(7) / 2))
        p1 = acb(1); p2 = acb(1)
        for n in range(N + 1):
            V[j, n] = w1 * p1 + w2 * p2; p1 *= v1; p2 *= v2
    F = acb_mat(N + 1, K)
    for m in range(N + 1):
        for j in range(K):
            F[m, j] = acb(arb((-2 * m * j) % (2 * K)) / K).exp_pi_i() / K
    A = F * V; n = N + 1
    Ar = arb_mat(n, n); mi = 0.0
    for i in range(n):
        for j in range(n):
            Ar[i, j] = A[i, j].real.mid(); mi = max(mi, abs(float(A[i, j].imag.mid())))
    return Ar, mi

def subspace(Ar, p=8, its=25):
    n = Ar.nrows()
    def orth(X):
        Q = []
        for j in range(p):
            v = [X[i, j].mid() for i in range(n)]
            for _ in range(2):
                for q in Q:
                    d = sum((a * b for a, b in zip(v, q)), arb(0)).mid(); v = [(a - d * b).mid() for a, b in zip(v, q)]
            nr = sum((a * a for a in v), arb(0)).sqrt().mid(); Q.append([(a / nr).mid() for a in v])
        Y = arb_mat(n, p)
        for i in range(n):
            for j in range(p): Y[i, j] = Q[j][i]
        return Y
    X = arb_mat(n, p)
    for i in range(n):
        for j in range(p): X[i, j] = arb(((i * 7 + j * 13) % 11) - 5 + (3 if i == j else 0))
    X = orth(X)
    for _ in range(its): X = orth(Ar * X)
    H = X.transpose() * Ar * X
    Hm = mpmath.matrix(p, p)
    for i in range(p):
        for j in range(p): Hm[i, j] = mpf(H[i, j].mid().str(mp.dps + 5, radius=False))
    E, Rv = mpmath.eig(Hm, left=False, right=True)
    order = sorted(range(p), key=lambda k: -abs(E[k]))
    Xm = mpmath.matrix(n, p)
    for i in range(n):
        for j in range(p): Xm[i, j] = mpf(X[i, j].mid().str(mp.dps + 5, radius=False))
    vecs = [Xm * Rv[:, k] for k in order]
    return [E[k] for k in order], vecs

def to_mp(Ar):
    n = Ar.nrows(); B = mpmath.matrix(n, n)
    for i in range(n):
        for j in range(n): B[i, j] = mpf(Ar[i, j].str(mp.dps + 5, radius=False))
    return B

t0 = time.time()
# ------------------------------------------------------------------ Part A: CR eigenvalues (own builder + solver)
chk("branches: Re(15/4 -+ s) > 0 on |s - c| = R (principal sqrt analytic)", 15/4 - (83/50 + 8/5) > 0)
ctx.prec = 600; mp.dps = 170
runs = {}
for (N, K) in ((140, 1024), (140, 2048), (200, 2048)):
    Ar, mi = build(N, K)
    E, _ = subspace(Ar)
    runs[(N, K)] = E
    print(f"  N={N} K={K}: " + ", ".join(mpmath.nstr(z.real, 25) for z in E[:6]) + f"  (max |Im entry| {mi:.1e}, {time.time()-t0:.0f}s)", flush=True)
E = runs[(200, 2048)]
r, l2, l3, l4, l5, l6 = [z.real for z in E[:6]]
chk("top six Ritz values real", all(abs(z.imag) < mpf('1e-40') for z in E[:6]))
chk("r, l_2, l_3 match CG.3 / CN mids", abs(r - mpf('0.42373128696260793985253216132843923')) < mpf('1e-30')
    and abs(l2 - mpf('-0.0731138175123995805')) < mpf('1e-19') and abs(l3 + mpf('0.01706764406262')) < mpf('1e-13'))
chk("l_4 inside CQ.3's -0.00021644655283736 +- 1.53e-18", abs(l4 + mpf('0.00021644655283736')) < mpf('1.53e-18'), mpmath.nstr(l4, 22))
chk("mu_5 matches CR.1's mu_5^300 = -4.550141188008649836529478e-8 to 1e-31",
    abs(l5 + mpf('4.550141188008649836529478e-8')) < mpf('1e-31'), mpmath.nstr(l5, 28))
chk("l_5 inside CR.3's -4.550141188009e-8 +- 4.51e-21", abs(l5 + mpf('4.550141188009e-8')) < mpf('4.51e-21'),
    "diff " + mpmath.nstr(abs(l5 + mpf('4.550141188009e-8')), 3))
chk("l_5 stable N=140 vs 200 and K=1024 vs 2048 (to 1e-30)",
    abs(runs[(140, 1024)][4] - runs[(200, 2048)][4]) < mpf('1e-30') and abs(runs[(140, 2048)][4] - runs[(140, 1024)][4]) < mpf('1e-30'))
chk("|l_5|/r = 1.073827052e-7 (+-1.93e-17 + rounding 5e-17)", abs(abs(l5) / r - mpf('1.073827052e-7')) < mpf('7e-17'), mpmath.nstr(abs(l5)/r, 15))
chk("|l_5|/|l_4| = 0.0002102200810", abs(abs(l5 / l4) - mpf('0.0002102200810')) < mpf('1e-13'), mpmath.nstr(abs(l5/l4), 13))
chk("next Ritz value |mu_6| < 1e-8 (repo: mpmath ~ -2.07e-15, uncertified)", abs(l6) < mpf('1e-8') and abs(abs(l6) / mpf('2.07e-15') - 1) < 0.01, mpmath.nstr(l6, 6))
chk("exactly five Ritz values with |z| > 1e-8 (of 8)", sum(1 for z in E if abs(z) > mpf('1e-8')) == 5)
# CR.5 / CR.6 arithmetic with the stated rounded constants (conservative: eps0 upper, |a5| lower)
th = mpf('1e-8') / abs(l5)
chk("rho_in/|l_5| = 0.21977", abs(th - mpf('0.21977')) < mpf('5e-6'), mpmath.nstr(th, 8))
k0 = next(k for k in range(400) if mpf('6.79e20') * th ** k < mpf('2.1323e-11') - mpf('7.9e-16'))
chk("CR.5 threshold k_0 = 48 from eps_0'' <= 6.79e20, |a_5| >= 2.1323e-11 - 7.9e-16", k0 == 48, f"k0={k0}; k=47 value {mpmath.nstr(mpf('6.79e20')*th**47,4)}")
chk("sign(a_5 l_5^k) = (-1)^(k+1) for a_5 < 0, l_5 < 0 (k < 60)", all(mpmath.sign(mpf('-2.1323e-11') * l5 ** k) == (-1) ** (k + 1) for k in range(60)))
chk("CR.6: N=300 gains ~1e21 over N=200 (eps_200/eps_300 = 1.03e-42/1.141e-63)", 5e20 < 1.03e-42 / 1.141e-63 < 2e21
    and 2.55e5 > 2.13e-11 and 2.83e-16 < 2.13e-11)

# ------------------------------------------------------------------ Part B: a_5^N with own eigenvectors + repo's F0
fpath = os.environ.get("F0FILE", "f0_M4096_N300.txt")
if os.path.exists(fpath):
    lines = open(fpath).read().split("\n")
    c0 = mpf([l for l in lines if l.startswith("C0")][0].split()[1])
    f = [mpf(l) for l in lines if l and not l.startswith("C0")]
    N = int(os.environ.get('NB', '300'))
    Ar, _ = build(N, 2048)
    Er, Vr = subspace(Ar); El, Wl = subspace(Ar.transpose())
    x0 = mpmath.sqrt(13) / 2; cc, RR = mpf(83) / 50, mpf(8) / 5
    def poly(v, s):
        u = (s - cc) / RR; acc = mpf(0)
        for i in reversed(range(len(v))): acc = acc * u + v[i]
        return acc
    def lt_eval(v, y):
        w1 = (y + mpf(1) / 2) / (2 * y * (mpf(7) / 2 - y)); w2 = (y - mpf(1) / 2) / (2 * y * (y + mpf(7) / 2))
        return w1 * poly(v, mpmath.sqrt(mpf(15) / 4 - y)) + w2 * poly(v, mpmath.sqrt(mpf(15) / 4 + y))
    a = []
    for i in range(5):
        v = [Vr[i][k].real for k in range(N + 1)]
        j = min(range(8), key=lambda k: abs(El[k] - Er[i])); w = [Wl[j][k].real for k in range(N + 1)]
        wv = mpmath.fsum(w[k] * v[k] for k in range(N + 1)); wf = mpmath.fsum(w[k] * f[k] for k in range(N + 1))
        a.append(c0 * wf / wv * lt_eval(v, x0) / Er[i].real)
    print("  a_1..a_5 (own eigvecs, repo F0): " + ", ".join(mpmath.nstr(t, 12) for t in a), flush=True)
    chk("a_1^N vs CN.3 a_1 = 0.00571256871089 +- 1.2e-15", abs(a[0] - mpf('0.00571256871089')) < mpf('1e-14'))
    chk("a_2^N, a_3^N vs CN/CO: -4.158e-5 +- 4.4e-9, -2.36116e-5 +- 4.6e-8", abs(a[1] + mpf('4.158e-5')) < mpf('4.4e-9') and abs(a[2] + mpf('2.36116e-5')) < mpf('4.6e-8'))
    chk("a_4^N vs CQ.4 a_4 = -2.204e-7 +- 5.54e-11", abs(a[3] + mpf('2.204e-7')) < mpf('5.54e-11'))
    chk("a_5^N negative and = CR.4's a_5 = -2.1323e-11 +- 7.9e-16", a[4] < 0 and abs(a[4] + mpf('2.1323e-11')) < mpf('7.9e-16'), mpmath.nstr(a[4], 15))
    chk("a_5^N agrees with CR.4's printed a_5^N = -2.13234993568815e-11 to 1e-22 (same N = 300)",
        abs(a[4] - mpf('-2.13234993568815e-11')) < mpf('1e-22'), mpmath.nstr(a[4] - mpf('-2.13234993568815e-11'), 3))
    s4 = mpf('0.00564716030397')
    # v2 used tolerance 1e-16 and FAILED (-4.13e-15): s_4 is given to 14 decimals (half-ulp 5e-15), so 1e-16 was my error.
    chk("a_1+..+a_5 = s_4 within the data rounding 5e-15 of '0.00564716030397'", abs(sum(a) - s4) <= mpf('5e-15'), mpmath.nstr(sum(a) - s4, 3))
    AN = a
else:
    AN = None
    print("  part B skipped: no F0 dump", fpath)

# ------------------------------------------------------------------ Part C: CS arithmetic
mp.dps = 40
q2 = l2 / r; q3 = l3 / r
rho32 = abs(l3 / l2)
chk("CS.1: rho_32 = |l_3/l_2| = 0.23343938 +- 2.3e-9", abs(rho32 - mpf('0.23343938')) < mpf('2.3e-9'), mpmath.nstr(rho32, 12))
contr = mpf('1906.1') / mpf('1360.9') * rho32
chk("CS.2: (1906.1/1360.9) rho_32 <= 0.326960 < 1", contr <= mpf('0.326960'), mpmath.nstr(contr, 10))
theta = mpf('0.5441333187'); t5 = theta ** (mpf(1) / 5)
chk("CS.3: theta^(1/5) = 0.88540315, |q_2|/theta^(1/5) = 0.19488027 < 1", abs(t5 - mpf('0.88540315')) < mpf('5e-9') and abs(abs(q2) / t5 - mpf('0.19488027')) < mpf('5e-9'), mpmath.nstr(abs(q2)/t5, 10))
B = mpf('-8.21069'); L = B * (q2 - 1)
chk("CS.2: L = B(q_2 - 1) = 9.6274 (B = -8.21069 +- 1e-5 from CO.4)", abs(L - mpf('9.6274')) < mpf('3.6e-5'), mpmath.nstr(L, 8))
S = {4:'0.00564716030397',5:'0.00242403694245',6:'0.00102545231951',7:'0.000434629687783',8:'0.000184158071629',
     9:'7.80341278693e-5',10:'3.30654582556e-5',11:'1.40108723364e-5',12:'5.93684473586e-6',13:'2.51562687729e-6',14:'1.06594981300e-6'}
S = {k: mpf(v) for k, v in S.items()}
D = {n: mpmath.log(S[n + 1] / (r * S[n])) / q2 ** n for n in range(4, 14)}
print("  D_4..D_13 from CC 12-digit sums: " + ", ".join(mpmath.nstr(D[n], 9) for n in range(4, 14)))
stated = [14.595098, 10.753464, 9.8926798, 9.6889799, 9.6418551, 9.6307827, 9.6282103, 9.6276077, 9.6274674]
# v2 used derr = 2e-12/|q2|^n and FAILED CS.4 at n = 7 (diff 4.6e-7 vs tol 4.4e-7) and the n <= 11 monotonicity check:
# 12 significant digits mean relative error up to 5e-12 per sum, so |d log(s_(n+1)/s_n)| <= 1e-11 -> derr = 1e-11/|q2|^n.
derr = {n: mpf('1e-11') / abs(q2) ** n for n in range(4, 14)}
chk("CS.4: D_4..D_12 match the stated values within data error", all(abs(D[n] - mpf(stated[n - 4])) < max(derr[n], mpf(10) ** (-len(str(stated[n-4]).split('.')[1]))) for n in range(4, 13)))
chk("D_4 = 14.59509785 (+- data error ~2e-9)", abs(D[4] - mpf('14.59509785')) < mpf('3e-9'), mpmath.nstr(D[4], 12))
dec = [n for n in range(4, 12) if D[n] - D[n + 1] > derr[n] + derr[n + 1]]
print("  12-digit data separate D_n > D_(n+1) for n in", dec, "(the rest need CC's certified sums or the spectral route below)")
chk("D_n > D_(n+1) decided by 12-digit data for 4 <= n <= 8, no reversal anywhere it is decided", dec[:5] == [4, 5, 6, 7, 8]
    and all(not (D[n + 1] - D[n] > derr[n] + derr[n + 1]) for n in range(4, 13)))
if AN is not None:
    # spectral reconstruction: s_(n) = sum_(i<=5) a_i^N l_i^(n-4) (remainder ~ a_6 l_6^k, |l_6| ~ 2e-15: negligible for n >= 5)
    mp.dps = 170
    lam = [z.real for z in E[:5]]
    sp = {n: mpmath.fsum(AN[i] * lam[i] ** (n - 4) for i in range(5)) for n in range(4, 60)}
    Dsp = {n: mpmath.log(sp[n + 1] / (r * sp[n])) / q2 ** n for n in range(5, 58)}
    Dsp[4] = D[4]
    Bsp = AN[1] / AN[0] * q2 ** (-4); Lsp = Bsp * (q2 - 1)
    print("  spectral D_5..D_12: " + ", ".join(mpmath.nstr(Dsp[n], 9) for n in range(5, 13)) + "; B = " + mpmath.nstr(Bsp, 10) + ", L = " + mpmath.nstr(Lsp, 10))
    chk("spectral B = (a_2/a_1) q_2^-4 within CO.4's -8.21069 +- 1e-5 and L within 9.6274 +- 3.6e-5", abs(Bsp + mpf('8.21069')) < mpf('1e-5') and abs(Lsp - mpf('9.6274')) < mpf('3.6e-5'), mpmath.nstr(Bsp, 10))
    chk("spectral D_5..D_12 match CS.4's printed values (to their last digit)", all(abs(Dsp[n] - mpf(stated[n - 4])) < mpf(10) ** (-len(str(stated[n-4]).split('.')[1])) for n in range(5, 13)))
    chk("spectral D_n strictly decreasing for 5 <= n <= 40 (model s_n = sum_(i<=5) a_i^N l_i^(n-4)) and > L", all(Dsp[n] > Dsp[n + 1] > Lsp for n in range(5, 40)))
    chk("spectral D_n - L inside [1360.9, 1906.1] rho_32^n for 5 <= n <= 40 (model s_n = sum_(i<=5) a_i^N l_i^(n-4))", all(mpf('1360.9') * rho32 ** n <= Dsp[n] - Lsp <= mpf('1906.1') * rho32 ** n for n in range(5, 41)))
chk("D_n - L inside [1360.9, 1906.1] rho_32^n for n = 4..10", all(mpf('1360.9') * rho32 ** n - derr[n] - mpf('4e-5') <= D[n] - L <= mpf('1906.1') * rho32 ** n + derr[n] + mpf('4e-5') for n in range(4, 11)))
chk("D_4 - L = 4.9677 in window [4.0413, 5.6604]", abs(D[4] - L - mpf('4.9677')) < mpf('1e-4') and abs(mpf('1360.9') * rho32 ** 4 - mpf('4.0413')) < mpf('1e-4') and abs(mpf('1906.1') * rho32 ** 4 - mpf('5.6604')) < mpf('1e-4'))
CG = abs(mpmath.log(S[5] / (r * S[4]))) * theta ** (-mpf(4) / 5)
chk("CS.3: C_G* = |log(s_5/(r s_4))| theta^(-4/5) = 0.02105127810 (+- data error ~2e-12)", abs(CG - mpf('0.02105127810')) < mpf('5e-12'), mpmath.nstr(CG, 13))
CGbar = abs(mpmath.log(S[5] / (r * S[4]))) * mpf('0.5442') ** (-mpf(4) / 5)
chk("CS.3: theta-bar = 0.5442 constant 0.0210492", abs(CGbar - mpf('0.0210492')) < mpf('1e-7'), mpmath.nstr(CGbar, 9))
chk("CS sharpens CN.4: D_4 <= 14.5952 (CN.4 C) and L < 9.626? (no: L = 9.6274 > 9.626, consistent with CN.4's lower 9.626 for n>=13)", D[4] <= mpf('14.5952') and L > mpf('9.626'))
chk("C_G* product monotone: D_k (|q_2|/theta^(1/5))^k decreasing for k = 4..13", all(D[k] * (abs(q2) / t5) ** k > D[k + 1] * (abs(q2) / t5) ** (k + 1) for k in range(4, 13)))
mp.dps = 40
print(f"{ok}/{tot} PASS  ({time.time()-t0:.0f}s)")
sys.exit(0 if ok == tot else 1)
