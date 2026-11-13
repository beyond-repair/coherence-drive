"""Independent float check of Theorem DJ (IFI 3c24c1135b02). Own code for weights, maps, the 9-fold image
expansion, the signed ratio programme (backward recursion + bisection) and all arithmetic. No repo import."""
import math, itertools, numpy as np
a=100.0; n=9; lo,hi=math.sqrt(5)/2,2.5
w=[lambda s:(s+.5)/(2*s*(3.5-s)), lambda s:(s-.5)/(2*s*(s+3.5))]
sg=[lambda s:math.sqrt(3.75-s), lambda s:math.sqrt(3.75+s)]
def images(z):
    out=[(1.0,z)]
    for _ in range(n):
        out=[(c*w[i](p),sg[i](p)) for c,p in out for i in (0,1)]
    return out
def functional(P):
    if isinstance(P,tuple):
        x,y=P; E=math.exp(a*abs(x-y))
        return [(E*c,p) for c,p in images(y)]+[(-c,p) for c,p in images(x)]
    return images(P)
def G0(b,pts):
    G=b[-1]
    for k in range(len(b)-2,-1,-1):
        d=pts[k+1]-pts[k]; G=b[k]+(math.exp(a*d)*G if G>0 else math.exp(-a*d)*G)
    return G
def rho(P,Q):
    A=functional(P); B=functional(Q)
    allp=sorted(set(p for _,p in A+B)); ix={p:i for i,p in enumerate(allp)}
    cA=np.zeros(len(allp)); cB=np.zeros(len(allp))
    for c,p in A: cA[ix[p]]+=c
    for c,p in B: cB[ix[p]]+=c
    sA=np.sum(np.abs(cA)); cA/=sA; cB/=np.sum(np.abs(cB))
    # find t* with G0(cA - t cB) = 0; ratio of normalised; log ratio returned with normalisation restored
    lo_t,hi_t=1e-6,1e6
    assert G0(cA-lo_t*cB,allp)>0 and G0(cA-hi_t*cB,allp)<0
    for _ in range(200):
        m=math.sqrt(lo_t*hi_t)
        if G0(cA-m*cB,allp)>0: lo_t=m
        else: hi_t=m
    return math.log(lo_t)+math.log(sA)-math.log(np.sum(np.abs([c for c,_ in B])))
res=[]
def check(name,ok,msg): res.append(ok); print(("PASS" if ok else "FAIL"),name,msg)
pt=images(2.0); check("images",len(pt)==512 and all(lo-1e-12<=p<=hi+1e-12 for _,p in pt),"512 images inside X_s")
d=1e-6; P1=(hi-d,hi); P2=(lo,lo+d)
r12=rho(P1,P2); r21=rho(P2,P1); D=r12+r21
print(f"rho(P1,P2)={r12:.7f} rho(P2,P1)={r21:.7f} sum={D:.9f}")
check("DJ.2 pair",abs(r12-0.0070018)<2e-7 and abs(r21-0.0069963)<2e-7 and D>0.013997,"matches repo's 0.0070018/0.0069963, sum>0.013997")
check("DJ.2 upper",D<0.025879,"below Delta_H")
th=math.tanh(0.013997/4); check("DJ.3",th>0.0034992 and th**(1/9)>0.53342,f"tanh={th:.8f} rate={th**(1/9):.6f}")
# W-type (point) pair at endpoints vs DH.3 diagonal floor
Wp=rho(hi,lo)+rho(lo,hi); print(f"point pair (5/2, sqrt5/2): {Wp:.7f}")
check("point<=pair",Wp<=D+1e-9,"point functionals give less than near-diagonal end pairs")
# attack: random/structured search for larger values (would contradict the float observation, not the theorem)
rng=np.random.default_rng(7); best=D; arg=None
cands=[]
for _ in range(60):
    x1,x2=rng.uniform(lo,hi,2); d1,d2=10**rng.uniform(-6,-1,2)
    P=(x1,min(hi,x1+d1)) if rng.random()<.5 else (min(hi,x1+d1),x1)
    Q=(x2,max(lo,x2-d2)) if rng.random()<.5 else (max(lo,x2-d2),x2)
    cands.append((P,Q))
for dd in (1e-8,1e-7,1e-5,1e-4,1e-3):
    cands+= [((hi-dd,hi),(lo,lo+dd)),((hi,hi-dd),(lo+dd,lo)),((hi-dd,hi),(lo+dd,lo))]
mx=0
for P,Q in cands:
    if P[0]==P[1] or Q[0]==Q[1]: continue
    v=rho(P,Q)+rho(Q,P); mx=max(mx,v)
    if v>best+1e-7: best=v; arg=(P,Q)
print(f"search max {mx:.9f}; exceeds DJ.2 by >1e-7: {arg}")
check("search<=DeltaH",mx<0.025879,"no candidate pair exceeds the DH upper bound")
print(f"{sum(res)}/{len(res)} PASS")
