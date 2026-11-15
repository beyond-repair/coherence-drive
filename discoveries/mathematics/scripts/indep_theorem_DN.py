"""v2: direct endpoint pairs over logspaced offsets, plus coarse interior scan with logspaced offsets (a=2)."""
import sys, math, numpy as np
sys.path.insert(0,'/workspace/ifi-repo/scripts')
import gasket_fractional_profile_level_birkhoff as bk
from flint import arb, ctx
ctx.prec=120; S,f=bk.taylor_data(); T=bk.Taylor(f,S); F=lambda s: float(T.val(arb(s)).mid())
def v(s):
    w1=(s+.5)/(2*s*(3.5-s)); w2=(s-.5)/(2*s*(s+3.5)); return w1*F(math.sqrt(3.75-s))+w2*F(math.sqrt(3.75+s))
lo,hi=math.sqrt(5)/2,2.5; a=2.0
Q=lambda x,y:(math.exp(a*abs(x-y))*v(y)-v(x))/(math.exp(a*abs(x-y))*F(y)-F(x))
ds=np.logspace(-7,0.2,200); qs=[]
for d in ds:
    for x,y in ((hi-d,hi),(lo+d,lo),(hi,hi-d),(lo,lo+d)):
        if lo<=x<=hi and lo<=y<=hi: qs.append(Q(x,y))
for x in np.linspace(lo,hi,41):
    for d in np.logspace(-6,0,40):
        for y in (x+d,x-d):
            if lo<=y<=hi: qs.append(Q(x,y))
t=math.log(max(qs)/min(qs)); print(f"beta {max(qs):.10f} alpha {min(qs):.10f} Theta {t:.7f}")
print(("PASS" if 0.14444<t<0.14473 else "FAIL"), f"direct pairs {t:.7f} between certified floor 0.14444 and upper 0.14473")
