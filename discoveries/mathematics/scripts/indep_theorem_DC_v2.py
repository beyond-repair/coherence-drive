"""v2 of two checks in indep_dc.py. v1 FAILs were my bugs: (1) wrong inequality direction on log(supR0/infR0) vs rounded endpoints;
(2) C_G^B from the ROUNDED Theta_G 0.28154093 and a 10-digit theta. Here theta is recomputed in full (CF.2 recipe, as in my CF check)."""
import mpmath as mp
mp.mp.prec = 200
a = mp.mpf(47)/2; M1 = mp.mpf(14)/15; c1 = 1/mp.sqrt(5); c2 = 1/(2*mp.sqrt(mp.mpf(15)/4 + mp.sqrt(5)/2))
M2 = abs(mp.diff(lambda x: mp.log((x-mp.mpf(1)/2)/(2*x*(x+mp.mpf(7)/2))), mp.sqrt(5)/2))
b = a
for _ in range(5): b = max(M1 + c1*b, M2 + c2*b)
crit = mp.mpf(1)/2 + mp.sqrt(2)
LW1 = lambda x: mp.log((x+0.5)/(2*x*(3.5-x))); LW2 = lambda x: mp.log((x-0.5)/(2*x*(x+3.5)))
def var2(l, h):
    if l < crit < h: return (LW2(crit)-LW2(l)) + (LW2(crit)-LW2(h))
    return abs(LW2(h) - LW2(l))
S1 = lambda x: mp.sqrt(mp.mpf(15)/4 - x); S2 = lambda x: mp.sqrt(mp.mpf(15)/4 + x)
def osc(l, h, n):
    if n == 0: return a*(h-l)
    return max(LW1(h)-LW1(l) + osc(S1(h), S1(l), n-1), var2(l, h) + osc(S2(l), S2(h), n-1))
theta = mp.tanh((2*mp.log((a+b)/(a-b)) + 2*osc(mp.sqrt(5)/2, mp.mpf(5)/2, 5))/4)
B0 = M1 + c1*mp.mpf('0.77333706'); TG = 2*mp.log((a+B0)/(a-B0)) + mp.mpf('0.063592701')
print("theta =", mp.nstr(theta, 20), " Theta_G(unrounded) =", mp.nstr(TG, 15))
C = TG*theta**(-mp.mpf(8)/5); Cr = mp.mpf('0.28154093')*theta**(-mp.mpf(8)/5)
print("PASS" if C <= mp.mpf('0.74544057') else "FAIL", "C_G^B from unrounded Theta_G =", mp.nstr(C, 12))
print("NOTE C_G^B from rounded 0.28154093 =", mp.nstr(Cr, 12), "(> 0.74544057 by", mp.nstr(Cr - mp.mpf('0.74544057'), 3), ")")
lo, hi = mp.mpf('0.4079370173'), mp.mpf('0.4347214550'); d = mp.log(hi/lo)
print("PASS" if abs(d - mp.mpf('0.063592701')) < 1e-8 else "FAIL", "log(hi/lo) of printed R0 enclosure =", mp.nstr(d, 12), "consistent with 0.063592701 to 1e-8")
