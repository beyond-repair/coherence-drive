"""Independent float check of Theorem DN (a=2): slopes of log F0, log Lt F0 and Theta_2(F0, Lt F0) by dense direct pairs."""
import sys, math, numpy as np
sys.path.insert(0,'/workspace/ifi-repo/scripts')
import gasket_fractional_profile_level_birkhoff as bk
from flint import arb, ctx
ctx.prec=120; S,f=bk.taylor_data(); T=bk.Taylor(f,S); F=lambda s: float(T.val(arb(s)).mid())
def v(s):
    w1=(s+.5)/(2*s*(3.5-s)); w2=(s-.5)/(2*s*(s+3.5)); return w1*F(math.sqrt(3.75-s))+w2*F(math.sqrt(3.75+s))
lo,hi=math.sqrt(5)/2,2.5; a=2.0
N=1601; xs=np.linspace(lo,hi,N); U=np.array([F(x) for x in xs]); V=np.array([v(x) for x in xs])
lu=np.log(U); lv=np.log(V); du=np.gradient(lu,xs); dv=np.gradient(lv,xs)
print(f"(logF0)' [{du.min():.6f},{du.max():.6f}]  (logLtF0)' [{dv.min():.6f},{dv.max():.6f}]")
P=[]
P.append(("slopeF0 in (0.035291,0.77334)", 0.035291<du.min() and du.max()<0.77334))
P.append(("slopeLtF0 in (0.17682,0.79038)", 0.17682<dv.min() and dv.max()<0.79038))
X,Y=np.meshgrid(xs,xs,indexing='ij'); E=np.exp(a*np.abs(X-Y)); m=X!=Y
Q=((E*V[None,:]-V[:,None])/(E*U[None,:]-U[:,None]))[m]
# near-diagonal limit pairs: add tiny-offset pairs at each grid point
d=1e-6; ext=[]
for x in xs:
    for y in (x+d,x-d):
        if lo<=y<=hi:
            e=math.exp(a*d); ext.append((e*v(y)-v(x))/(e*F(y)-F(x)))
Q=np.concatenate([Q,ext]); t=math.log(Q.max()/Q.min())
print(f"Theta_2 sampled {t:.6f}")
P.append(("Theta sampled in (0.1440,0.14473)", 0.1440<t<0.14473))
P.append(("Theta >= 2.2 x 0.064975 (DN.4)", t>2.2*0.064975))
for n,ok in P: print(("PASS " if ok else "FAIL ")+n)
print(sum(ok for _,ok in P),"/",len(P))
