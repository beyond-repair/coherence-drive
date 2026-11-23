"""v3 addendum: v2's direct-pair sampler never put y exactly at an endpoint (x = base, y = x +- d), so it missed the
extremal cells (beta at y = 5/2 from x < y, alpha at y = sqrt5/2 from x > y). Direct quotient there, own code."""
import sys, math, numpy as np
import os; sys.path.insert(0, os.environ.get('IFI_SCRIPTS', 'scripts'))
import gasket_fractional_profile_level_birkhoff as bk
from flint import arb, ctx
ctx.prec=120; S,f=bk.taylor_data(); T=bk.Taylor(f,S); F=lambda s: float(T.val(arb(s)).mid())
def v(s):
    w1=(s+.5)/(2*s*(3.5-s)); w2=(s-.5)/(2*s*(s+3.5)); return w1*F(math.sqrt(3.75-s))+w2*F(math.sqrt(3.75+s))
lo,hi=math.sqrt(5)/2,2.5; a=100.0
Q=lambda x,y:(math.exp(a*abs(x-y))*v(y)-v(x))/(math.exp(a*abs(x-y))*F(y)-F(x))
ds=np.logspace(-8,-1,141); b=max(Q(hi-d,hi) for d in ds); al=min(Q(lo+d,lo) for d in ds)
t=math.log(b/al); print(f"beta_direct {b:.10f} alpha_direct {al:.10f} Theta_direct {t:.9f}")
print(("PASS" if 0.06497<t<0.064982 else "FAIL"), f"endpoint direct pairs give {t:.9f}, between 0.06497 and certified 0.064982 (floor 0.064975528)")
