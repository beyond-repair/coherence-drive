"""Independent float check of Theorem DK (IFI 261803687762). Own code: weights, maps, 9-fold image expansion
with complex-step derivatives, m-functional ratio programme (f' at image points chosen locally in [-a f, a f],
then DJ-style bang-bang backward recursion + bisection), and a search over Q = (t, s). No repo import."""
import math, cmath, numpy as np
a=100.0; n=9; lo,hi=math.sqrt(5)/2,2.5; h=1e-20
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
im=images(2.0); check("images",len(im)==512 and all(lo-1e-12<=p<=hi+1e-12 for _,_,p,_ in im),"512 images in X_s")
# DK.2: |f'|<=a f closure: m^s_t(Lf) >= 0 needs a + s*lambda >= ... ; check min effective a*W + s*W' - a|W p'| > 0 per word
mn=min(min(a*W+s*Wd-a*abs(W*pd) for W,Wd,_,pd in images(t))/1 for t in np.linspace(lo,hi,9) for s in (1,-1))
check("positivity",mn>0,f"min word coefficient a W + s W' - a|W p'| = {mn:.3e} > 0")
C=((hi,1),(lo,1)); D=rho(C[0],C[1])+rho(C[1],C[0]); print(f"corner ((5/2,+),(sqrt5/2,+)) sum = {D:.8f}")
check("corner",abs(D-0.01399809)<2e-7,"matches repo's relaxed corner 0.01399809")
Dn=rho(C[0],C[1],False)+rho(C[1],C[0],False); print(f"without f' term: {Dn:.5f}")
check("drop f'",abs(Dn-0.01382)<1e-4 and Dn<0.013997,"matches repo's 0.01382, below DJ floor")
# search over Q pairs: endpoints, grid, random
ts=list(np.linspace(lo,hi,13)); rng=np.random.default_rng(11); ts+=list(rng.uniform(lo,hi,12))
Qs=[(t,s) for t in ts for s in (1,-1)]; mx=0; arg=None; cnt=0
for i in range(len(Qs)):
    for j in range(i+1,len(Qs)):
        v=rho(Qs[i],Qs[j])+rho(Qs[j],Qs[i]); cnt+=1
        if v>mx: mx,arg=v,(Qs[i],Qs[j])
print(f"search over {cnt} pairs: max {mx:.8f} at {arg}")
check("search<=0.014000",mx<=0.014000,"no sampled pair exceeds DK.3's bound")
check("search>=floor",mx>0.013997,"sampled max above DJ.2 floor (consistent)")
th=math.tanh(0.014/4); check("DK.4",th<0.0035 and th**(1/9)<0.53349,f"tanh={th:.10f} rate={th**(1/9):.8f}")
print(f"{sum(res)}/{len(res)} PASS")
