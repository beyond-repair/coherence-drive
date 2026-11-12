"""Independent float check of Theorem DO (IFI c7264aec2f70): iterate L~ on a Chebyshev table, then Theta_a(F_m,F_m+1) by pair sampling and osc log R_m."""
import sys, math, numpy as np
sys.path.insert(0,'/workspace/ifi-repo/scripts')  # point at an informational-flux-identity checkout's scripts/ (only CO's Taylor data is imported)
import gasket_fractional_profile_level_birkhoff as bk
from flint import arb, ctx
from numpy.polynomial import chebyshev as C
ctx.prec=120; S,f=bk.taylor_data(); T=bk.Taylor(f,S); F0=lambda s: float(T.val(arb(s)).mid())
lo,hi=math.sqrt(5)/2,2.5
def Lt(F):
    def v(s):
        w1=(s+.5)/(2*s*(3.5-s)); w2=(s-.5)/(2*s*(s+3.5)); return w1*F(math.sqrt(3.75-s))+w2*F(math.sqrt(3.75+s))
    return v
def tab(g,deg=60):
    xs=np.cos(np.pi*(np.arange(deg+1)+.5)/(deg+1)); ss=lo+(hi-lo)*(xs+1)/2
    c=C.chebfit(xs,[g(s) for s in ss],deg); return lambda s: float(C.chebval(2*(s-lo)/(hi-lo)-1,c))
Fs=[F0]; 
for m in range(7): Fs.append(tab(Lt(Fs[-1])))
# check table accuracy for m=1 against direct
err=max(abs(Fs[1](s)-Lt(F0)(s))/abs(Lt(F0)(s)) for s in np.linspace(lo,hi,101)); print("table rel err m=1",err)
def theta(F,G,a):
    Q=lambda x,y:(math.exp(a*abs(x-y))*G(y)-G(x))/(math.exp(a*abs(x-y))*F(y)-F(x))
    qs=[]
    for d in np.logspace(-6,0.2,120):
        for x,y in ((hi-d,hi),(lo+d,lo),(hi,hi-d),(lo,lo+d)):
            if lo<=x<=hi and lo<=y<=hi: qs.append(Q(x,y))
    for x in np.linspace(lo,hi,31):
        for d in np.logspace(-5,0,30):
            for y in (x+d,x-d):
                if lo<=y<=hi: qs.append(Q(x,y))
    return math.log(max(qs)/min(qs))
grid=np.linspace(lo,hi,2001)
for m in range(7):
    h=1e-6; sl=[(math.log(Fs[m](s+h))-math.log(Fs[m](s-h)))/(2*h) for s in grid[1:-1]]
    print(f"m={m} (log F_m)' range [{min(sl):.6f},{max(sl):.6f}]")
for m in range(6):
    R=[Fs[m+1](s)/Fs[m](s) for s in grid]; osc=math.log(max(R)/min(R))
    print(f"m={m} Theta2 {theta(Fs[m],Fs[m+1],2.0):.7g} Theta100 {theta(Fs[m],Fs[m+1],100.0):.7g} osclogR {osc:.7g}")
