"""v2 of my DI cross-check: v1's 1601-point pair grid (spacing 7.8e-4, a*d = 0.078) cannot reach the x -> y one-sided
limits where the extremes sit, so it gave only a lower bound 0.064906 (below the floor; not a contradiction). v2 adds
(i) my own one-sided limits R(y)(a -+ q1)/(a -+ q0) with finite-difference slopes at 2049 points and (ii) direct
pairs near the diagonal (|x-y| from 1e-7 to 1e-1, log-spaced) at 257 base points. Black box: repo F0 evaluator."""
import sys, math, numpy as np
import os; sys.path.insert(0, os.environ.get('IFI_SCRIPTS', 'scripts'))
import gasket_fractional_profile_level_birkhoff as bk
from flint import arb, ctx
ctx.prec=120; S,f=bk.taylor_data(); T=bk.Taylor(f,S)
F=lambda s: float(T.val(arb(s)).mid())
def v(s):
    w1=(s+.5)/(2*s*(3.5-s)); w2=(s-.5)/(2*s*(s+3.5)); return w1*F(math.sqrt(3.75-s))+w2*F(math.sqrt(3.75+s))
lo,hi=math.sqrt(5)/2,2.5; a=100.0; res=[]
def ok(c,m): res.append(bool(c)); print(("PASS " if c else "FAIL ")+m,flush=True)
def sl(g,x,h=1e-6):
    if x-h<lo: return (-3*math.log(g(x))+4*math.log(g(x+h))-math.log(g(x+2*h)))/(2*h)
    if x+h>hi: return (3*math.log(g(x))-4*math.log(g(x-h))+math.log(g(x-2*h)))/(2*h)
    return (math.log(g(x+h))-math.log(g(x-h)))/(2*h)
Y=np.linspace(lo,hi,2049); B=-1; Al=9
for k,y in enumerate(Y):
    R=v(y)/F(y); q0=sl(F,y); q1=sl(v,y); c=[R]
    if k<len(Y)-1: c.append(R*(a-q1)/(a-q0))
    if k>0: c.append(R*(a+q1)/(a+q0))
    B=max(B,*c); Al=min(Al,*c)
fl=math.log(B/Al); print("own one-sided-limit floor",fl,B,Al)
ok(abs(fl-0.064975528)<5e-7, f"own one-sided-limit floor {fl:.9f} ~ repo floor 0.064975528")
ok(fl<0.064982, "floor below certified upper bound 0.064982")
# direct pairs near diagonal
Bd=-1; Ad=9
for x in np.linspace(lo,hi,257):
    for dd in np.logspace(-7,-1,61):
        for y in (x-dd,x+dd):
            if not(lo<=y<=hi): continue
            d=abs(x-y); e=math.exp(a*d); q=(e*v(y)-v(x))/(e*F(y)-F(x)); Bd=max(Bd,q); Ad=min(Ad,q)
td=math.log(max(Bd,B)/min(Ad,Al)); print("direct near-diagonal",Bd,Ad,td)
ok(td<0.064982, f"direct near-diagonal sup/inf with limits: Theta = {td:.9f} < 0.064982 (no pair exceeds the bound)")
ok(math.log(Bd/Ad)>0.06497, f"direct pairs alone reach {math.log(Bd/Ad):.9f} (approach floor from below)")
print(f"{sum(res)}/{len(res)} PASS")
