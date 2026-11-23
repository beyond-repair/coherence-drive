"""Independent float/mpmath cross-check of IFI Theorem DI (b33223d2efb5). F0 values taken from the repo's Taylor
evaluator (black box, the one input not rebuilt); slopes, the Hilbert quotient (direct definition, not DI.1), and all
arithmetic are my own code. Not a certificate."""
import sys, math, time, numpy as np, mpmath as mp
import os; sys.path.insert(0, os.environ.get('IFI_SCRIPTS', 'scripts'))
import gasket_fractional_profile_level_birkhoff as bk
from flint import arb, ctx
ctx.prec = 120
res=[]
def ok(c,m): res.append(bool(c)); print(("PASS " if c else "FAIL ")+m, flush=True)
S,f=bk.taylor_data(); T=bk.Taylor(f,S)
F=lambda s: float(T.val(arb(s)).mid())
def wts(s):  # my own weights from the CF/DH setting
    return (s+.5)/(2*s*(3.5-s)), (s-.5)/(2*s*(s+3.5))
def u(s): return F(s)
def v(s):
    w1,w2=wts(s); return w1*F(math.sqrt(3.75-s))+w2*F(math.sqrt(3.75+s))
# check my weights against the repo's
s=1.7; w1,w2=bk.wts(arb(s)); ok(abs(float(w1.mid())-wts(s)[0])<1e-14 and abs(float(w2.mid())-wts(s)[1])<1e-14, "own weights == repo weights")
lo,hi=math.sqrt(5)/2,2.5; a=100.0
t0=time.time(); M=1601; X=np.linspace(lo,hi,M); U=np.array([u(x) for x in X]); V=np.array([v(x) for x in X]); print(f"grid {time.time()-t0:.0f}s")
# finite-difference log slopes (central, h=1e-5, interior points + one-sided at ends)
def slope(g,x,h=1e-5):
    if x-h<lo: return (math.log(g(x+h))-math.log(g(x)))/h
    if x+h>hi: return (math.log(g(x))-math.log(g(x-h)))/h
    return (math.log(g(x+h))-math.log(g(x-h)))/(2*h)
Xs=np.linspace(lo,hi,401); q0=np.array([slope(u,x) for x in Xs]); q1=np.array([slope(v,x) for x in Xs])
print("q0 range",q0.min(),q0.max(),"q1 range",q1.min(),q1.max())
ok(q0.min()>0.035291-1e-4 and q0.max()<0.77334, f"(log F0)' grid range [{q0.min():.6f},{q0.max():.6f}] within certified [0.035291,0.77334]")
ok(q1.min()>0.17682-1e-4 and q1.max()<0.79038, f"(log Lt F0)' grid range [{q1.min():.6f},{q1.max():.6f}] within [0.17682,0.79038]")
ok(abs(q0.min()-0.035291)<2e-4 and abs(q0.max()-0.77334)<2e-4 and abs(q1.min()-0.17682)<2e-4 and abs(q1.max()-0.79038)<2e-4, "slope bounds tight (<2e-4) to grid extremes")
ok(np.all(np.diff(q0)>0) and np.all(np.diff(q1)>0), "q0, q1 increasing on grid (stated: both strictly increasing — check reading)")
R=V/U; lr=math.log(R.max()/R.min()); ok(0.0633864-1e-6<lr<0.063387, f"log(sup R/inf R) grid {lr:.8f} in [0.0633864, 0.063387)")
# direct Hilbert quotient Phi_v/Phi_u over all grid pairs (definition), plus R
D=np.abs(X[:,None]-X[None,:]); E=np.exp(a*D)
Pu=E*U[None,:]-U[:,None]; Pv=E*V[None,:]-V[:,None]; mask=D>0
assert np.all(Pu[mask]>0)
Q=Pv[mask]/Pu[mask]; beta=max(Q.max(),R.max()); alpha=min(Q.min(),R.min())
Th=math.log(beta/alpha); print("beta",beta,"alpha",alpha)
ok(0.064975-2e-6<Th<0.064982, f"direct-definition grid Theta_100(f0,Lt f0) = {Th:.8f} in [floor 0.064975, cert 0.064982)")
# identity DI.1 numerically
I=R[None,:]+(R[None,:]-R[:,None])/(E*U[None,:]/U[:,None]-1)
ok(np.max(np.abs(I[mask]-Pv[mask]/Pu[mask])/np.abs(Pv[mask]/Pu[mask]))<1e-9, "DI.1 identity matches direct quotient on all pairs")
ok(abs(beta-0.434749363)<2e-5 and abs(alpha-0.407397144)<2e-5, f"beta {beta:.9f} ~ 0.434749363, alpha {alpha:.9f} ~ 0.407397144")
# where extremes sit
i,j=np.unravel_index(np.argmax(np.where(mask,Pv/np.where(mask,Pu,1),-1)),D.shape); print("argmax pair",X[i],X[j])
# DI.3 arithmetic from signed slopes (DG.1(i) per orientation, DH.1 form)
mp.mp.dps=40; A=mp.mpf(100); c0,d0,c1,d1=map(mp.mpf,('0.03529120','0.77333705','0.17682394','0.79037964'))
# x>y: alpha_u=sup q0, beta_v=-inf q1 ; x<y: alpha_u=-inf q0, beta_v=sup q1 ; and u,v exchanged
up=max((A-c1)/(A-d0),(A+d1)/(A+c0)); dn=max((A-c0)/(A-d1),(A+d0)/(A+c1))
TS=mp.log(up)+mp.log(dn)+mp.mpf('0.0633865095'); print("my DI.3 =",mp.nstr(TS,10),"cone",mp.nstr(mp.log(up)+mp.log(dn),8))
ok(TS<mp.mpf('0.078489') and abs(TS-mp.mpf('0.078488607'))<1e-6, f"DI.3 reconstructed {mp.nstr(TS,10)} ~ 0.078488607")
ok(mp.mpf('0.10465')/mp.mpf('0.064982')>=mp.mpf('1.6104'), f"DH.5/DI ratio {mp.nstr(mp.mpf('0.10465')/mp.mpf('0.064982'),8)} >= 1.6104")
print(f"{sum(res)}/{len(res)} PASS")
