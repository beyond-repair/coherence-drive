"""Independent float check of Theorem DL (IFI 7b88a6d98f10), adapted from the DK check. Own code: weights, maps, 9-fold image expansion
with complex-step derivatives, m-functional ratio programme (f' at image points chosen locally in [-a f, a f],
then DJ-style bang-bang backward recursion + bisection), and a search over Q = (t, s). No repo import."""
import math, cmath, numpy as np
import os
a=2.0; n=int(os.environ.get("N","7")); lo,hi=math.sqrt(5)/2,2.5; h=1e-20
w=[lambda s:(s+.5)/(2*s*(3.5-s)), lambda s:(s-.5)/(2*s*(s+3.5))]
sg=[lambda s:cmath.sqrt(3.75-s), lambda s:cmath.sqrt(3.75+s)]
def images(t):
    z=complex(t,h); out=[(1.0+0j,z)]
    for _ in range(n): out=[(c*w[i](p),sg[i](p)) for c,p in out for i in (0,1)]
    # (W, W', point, point')
    return [(c.real,c.imag/h,p.real,p.imag/h) for c,p in out]
cache={}
def mfun(Q,use_fp=True):
    t,s=Q
    if (t,use_fp) not in cache: cache[(t,use_fp)]=images(t)
    # m^s_t(Lf) = sum a W f(p) + s (W' f(p) + W p' f'(p))  -> (point, coef of f, coef of f')
    return [(p, a*W+s*Wd, (s*W*pd if use_fp else 0.0)) for W,Wd,p,pd in cache[(t,use_fp)]]
def G0(b,pts):
    G=b[-1]
    for k in range(len(b)-2,-1,-1):
        d=pts[k+1]-pts[k]; G=b[k]+(math.exp(a*d)*G if G>0 else math.exp(-a*d)*G)
    return G
def rho(Q1,Q2,use_fp=True):
    A=mfun(Q1,use_fp); B=mfun(Q2,use_fp)
    allp=sorted(set(p for p,_,_ in A+B)); ix={p:i for i,p in enumerate(allp)}; N=len(allp)
    cA=np.zeros(N); dA=np.zeros(N); cB=np.zeros(N); dB=np.zeros(N)
    for p,c,d in A: cA[ix[p]]+=c; dA[ix[p]]+=d
    for p,c,d in B: cB[ix[p]]+=c; dB[ix[p]]+=d
    one=lambda c: c.sum()  # value on f = const 1 (f'=0), for normalisation
    nA,nB=one(cA),one(cB)
    cA,dA,cB,dB=cA/nA,dA/nA,cB/nB,dB/nB
    eff=lambda t: (cA-t*cB)+a*np.abs(dA-t*dB)
    lo_t,hi_t=0.5,2.0
    assert G0(eff(lo_t),allp)>0 and G0(eff(hi_t),allp)<0
    for _ in range(80):
        m=math.sqrt(lo_t*hi_t)
        if G0(eff(m),allp)>0: lo_t=m
        else: hi_t=m
    return math.log(lo_t)
res=[]
def check(name,ok,msg): res.append(ok); print(("PASS" if ok else "FAIL"),name,msg)
im=images(2.0); check("images",len(im)==2**n and all(lo-1e-12<=p<=hi+1e-12 for _,_,p,_ in im),"32 images in X_s")
mn=min(a*W+s*Wd-a*abs(W*pd) for t in np.linspace(lo,hi,9) for s in (1,-1) for W,Wd,_,pd in images(t))
check("positivity",mn>0,f"min a W + s W' - a|W p'| = {mn:.3e} > 0")
lam=max(abs(Wd/W) for t in np.linspace(lo,hi,41) for W,Wd,_,_ in images(t)); bp=max(abs(pd) for t in np.linspace(lo,hi,41) for _,_,_,pd in images(t))
print(f"sup|lambda_w| ~ {lam:.4f}, sup|b_w'| ~ {bp:.3e}"); BP={7:5.80e-4,9:6.45e-5}[n]; check("DM.2 b'",bp<BP,f"sampled |b_w'| below {BP}")
phi=14/15+2/math.sqrt(5); check("DL.1 phi",phi<1.8278,f"14/15+2/sqrt5 = {phi:.6f}")
corners={}
for s1 in (1,-1):
  for s2 in (1,-1):
    C=((hi,s1),(lo,s2)); corners[(s1,s2)]=rho(C[0],C[1])+rho(C[1],C[0])
    C=((lo,s1),(hi,s2)); corners[(s1,s2,'r')]=rho(C[0],C[1])+rho(C[1],C[0])
for k,v in corners.items(): print("corner",k,f"{v:.8f}")
mxc=max(corners.values()); FL,UB={7:(0.0044106,0.004411),9:(0.00044485,0.0004449)}[n]; check("corner",FL<mxc<=UB,f"max endpoint corner {mxc:.10f} in ({FL},{UB}]")
K=int(os.environ.get("K","17")); ts=list(np.linspace(lo,hi,K)); rng=np.random.default_rng(7); ts+=list(rng.uniform(lo,hi,K-1))
Qs=[(t,s) for t in ts for s in (1,-1)]; mx=0; arg=None; cnt=0
for i in range(len(Qs)):
    for j in range(i+1,len(Qs)):
        v=rho(Qs[i],Qs[j])+rho(Qs[j],Qs[i]); cnt+=1
        if v>mx: mx,arg=v,(Qs[i],Qs[j])
print(f"search over {cnt} pairs: max {mx:.8f} at {arg}")
check("search<=UB",mx<=UB,"no sampled pair exceeds DL.4's bound")
check("search>=floor",mx>FL,"sampled max above DL.3 floor")
T,R,M={7:(0.0011028,0.378005,0.16018),9:(0.00011123,0.363655,0.15410)}[n]; RL={7:0.377999,9:0.363650}[n]
th=math.tanh(UB/4); r=0.42373128696; thf=math.tanh(FL/4)
check("DM.5",th<T and th**(1/n)<R and th**(1/n)*r<M and thf**(1/n)>RL,f"tanh={th:.10f} rate={th**(1/n):.8f} floor-rate={thf**(1/n):.8f} mu={th**(1/n)*r:.8f}")
# DM.1 lemma: chord/tangent bounds and corner attainment of a ratio of affine-in-delta positive functions
rng=np.random.default_rng(1); okc=True; okm=True
for _ in range(20000):
    x=rng.normal()*3; hh=rng.uniform(1e-4,0.3); d=rng.uniform(-hh,hh)
    if abs(x)*hh<1: okc&=(1+x*d<=math.exp(x*d)<=math.cosh(x*hh)+d/hh*math.sinh(x*hh)+1e-15)
    p=rng.uniform(.5,2,(4,)); q=rng.normal(size=4)*.1  # v2 (v1 used .1: non-positive denominators, my test bug); q=rng.normal(size=4)*.1
    f=lambda d1,d2:((p[0]+q[0]*d1)/(p[1]+q[1]*d1))*((p[2]+q[2]*d2)/(p[3]+q[3]*d2))
    g=np.linspace(-1,1,21); inner=max(f(u,v) for u in g for v in g); cor=max(f(u,v) for u in (-1,1) for v in (-1,1))
    okm&=inner<=cor*(1+1e-12)
check("DM.1 lemma",okc and okm,"chord/tangent + corner-max of product of linear-fractionals (20000 random)")
print(f"{sum(res)}/{len(res)} PASS")
