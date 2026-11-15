"""Independent check of IFI Theorem DC (commit 4996a9fca878); no repo imports.
Part A: mpmath (200-bit) arithmetic on DC.1/DC.3/DC.4 constants. Part B: falsification of DC.1(ii)'s general-f bound
on random log-Lipschitz f via the full branch tree of L~ (float64, own operator from CE's closed form)."""
import mpmath as mp, numpy as np, random
mp.mp.prec = 200
ok = tot = 0
def chk(c, m):
    global ok, tot; tot += 1; ok += bool(c); print(("PASS " if c else "FAIL ") + m, flush=True)
a = mp.mpf(47)/2; M1 = mp.mpf(14)/15; c1 = 1/mp.sqrt(5); c2 = 1/(2*mp.sqrt(mp.mpf(15)/4 + mp.sqrt(5)/2))
s = mp.sqrt(5)/2; M2 = abs(mp.diff(lambda x: mp.log((x-mp.mpf(1)/2)/(2*x*(x+mp.mpf(7)/2))), s))
Xs = (5 - mp.sqrt(5))/2; bst = M1/(1-c1); theta = mp.mpf('0.5441333187')  # CF.2 (reproduced in my CF check)
phi = lambda b: max(M1 + c1*b, M2 + c2*b)
def K(beta):
    B = max(beta, phi(beta)); return 2*mp.log((a+B)/(a-B)) + (beta + phi(beta))*Xs
chk(abs(M2 - mp.mpf('0.50706443')) < 1e-8 and abs(c2 - mp.mpf('0.22661737')) < 1e-8, f"M2={mp.nstr(M2,10)}, c2={mp.nstr(c2,10)}")
chk(abs(bst - mp.mpf('1.688415861')) < 1e-9 and abs(Xs - mp.mpf('1.381966')) < 1e-6, f"b*={mp.nstr(bst,12)}, |Xs|={mp.nstr(Xs,8)}")
chk(abs(M2 + c2*bst - mp.mpf('0.88968880')) < 1e-8 and M2 + c2*bst < bst and M2 < M1 and c2 < c1, "DC.1(i) inequalities")
for b, val in [(0, '1.44879'), (M1, '3.38668'), (bst, '4.95456'), (10, '23.1076'), (23, '56.356')]:
    k = K(mp.mpf(b)); chk(k <= mp.mpf(val) and k > mp.mpf(val) - mp.mpf('1e-3')*mp.mpf(val), f"K({mp.nstr(b,6)})={mp.nstr(k,10)} <= {val}")
chk(K(0) > mp.mpf('0.765085'), "K(0) bounds CF.4's Theta_0")
for b, j, bet, kv in [(100, 2, '21.351', '50.068'), (10**4, 8, '17.686', '40.577')]:
    js = [jj for jj in range(40) if bst + c1**jj*(b - bst) < a]; j0 = js[0]; beta = bst + c1**j0*(b - bst)
    chk(j0 == j and beta <= mp.mpf(bet) and K(beta) <= mp.mpf(kv), f"b={b}: j0={j0}, beta={mp.nstr(beta,8)}, K={mp.nstr(K(beta),8)}")
b0 = mp.mpf('0.77333706'); B0 = phi(b0); chk(B0 == M1 + c1*b0 and B0 <= mp.mpf('1.2791803'), f"B0=phi(b0)={mp.nstr(B0,10)}")
TG = 2*mp.log((a+B0)/(a-B0)) + mp.mpf('0.063592701'); chk(TG <= mp.mpf('0.28154093'), f"Theta_G recomputed {mp.nstr(TG,10)}")
osc_form = 2*mp.log((a+B0)/(a-B0)) + mp.mpf('0.48883593') + mp.mpf('0.55233653'); chk(abs(osc_form - mp.mpf('1.2591208')) < 1e-6, f"osc+osc form {mp.nstr(osc_form,9)}")
lo, hi = mp.mpf('0.4079370173'), mp.mpf('0.4347214550'); chk(mp.log(hi/lo) >= mp.mpf('0.063592701') - 1e-9, f"log(supR0/infR0) from stated enclosure {mp.nstr(mp.log(hi/lo),10)} >= certified upper (cell bounds vs envelope)")
CGB = mp.mpf('0.28154093')*theta**(-mp.mpf(8)/5); chk(CGB <= mp.mpf('0.74544057') + 1e-9, f"C_G^B={mp.nstr(CGB,10)}")
chk(all(theta**((k-4)//5) <= theta**(-mp.mpf(8)/5)*theta**(mp.mpf(k)/5) + mp.mpf(10)**-40 for k in range(4, 400)), "theta^floor((k-4)/5) <= theta^(-8/5) theta^(k/5), k=4..399")
r = mp.mpf('0.42373128696260793985'); s4 = mp.mpf('0.00564716030397'); s5 = mp.mpf('0.00242403694245')
d = abs(mp.log(s5/(r*s4))); chk(abs(d - mp.mpf('0.012937272')) < 5e-9, f"|log(s5/(r s4))|={mp.nstr(d,10)}")
chk(d <= mp.mpf('0.28154093'), "k=4 deviation below DC.3 bound")
chk(abs(mp.mpf('0.28154093')/d - mp.mpf('21.762')) < 2e-3 and mp.mpf('0.0633864')/d > mp.mpf('4.89'), f"DC.4 ratios {mp.nstr(mp.mpf('0.28154093')/d,6)}, floor/dev {mp.nstr(mp.mpf('0.0633864')/d,5)}")
chk(abs(CGB/mp.mpf('0.02105127810') - mp.mpf('35.411')) < 2e-3, f"C_G^B/C_G* = {mp.nstr(CGB/mp.mpf('0.02105127810'),6)}")
chk(lo <= r <= hi, "r in [inf R0, sup R0]")
# Part B: DC.1(ii) on random f with log f b-Lipschitz in s, branch tree in float64
th = float(theta); rf = float(r)
def Lm(f, t, m):
    if m == 0: return f(t)
    sv = np.sqrt(t + 6.25); w1 = (sv+.5)/(2*sv*(3.5-sv)); w2 = (sv-.5)/(2*sv*(sv+3.5))
    return w1*Lm(f, -2.5 - sv, m-1) + w2*Lm(f, -2.5 + sv, m-1)
random.seed(7); pts = np.linspace(-5, 0, 13); worst = 0.0; viol = 0
for trial in range(40):
    b = random.choice([0.5, 1.0, 1.6884, 5.0, 15.0, 23.0, 60.0, 300.0])
    A = [random.uniform(-1, 1) for _ in range(4)]; Fq = [random.uniform(0.5, 6) for _ in range(4)]
    L = sum(abs(A[i])*Fq[i] for i in range(4)); sc = b/L  # log f = sc*sum A_i sin(F_i s): Lipschitz const <= b in s
    f = lambda t, A=A, Fq=Fq, sc=sc: np.exp(sc*sum(A[i]*np.sin(Fq[i]*np.sqrt(t+6.25)) for i in range(4)))
    js = [jj for jj in range(60) if float(bst) + float(c1)**jj*max(b - float(bst), 0) < 23.5]; j = js[0]
    beta = float(bst) + float(c1)**j*(b - float(bst)) if b > float(bst) else (b if j == 0 else float(bst))
    if j == 0: beta = b
    Kb = float(K(mp.mpf(beta)))
    vals = [np.array([Lm(f, t, m) for t in pts]) for m in range(j, j + 15)]
    for i in range(len(vals) - 1):
        m = j + i; dev = np.max(np.abs(np.log(vals[i+1]/vals[i]) - np.log(rf))); bnd = th**((m - j)//5)*Kb
        worst = max(worst, dev/bnd); viol += dev > bnd
chk(viol == 0, f"DC.1(ii) bound holds on 40 random log-Lipschitz f, m-j<=13, 13 points (max used fraction {worst:.3f})")
print(f"{ok}/{tot} PASS")
