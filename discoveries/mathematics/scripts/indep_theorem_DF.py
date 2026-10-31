# Independent check of IFI Theorem DF (commit 3f0579e83c80) -- from GASKET.md text only.
# Joint term via Charnes-Cooper LP (scipy HiGHS) on 512 points, not the repo's DP.
import numpy as np, itertools, mpmath as mp, time, sys
from scipy.optimize import linprog
mp.mp.dps=40
a=100.0; n=8; lo,hi=np.sqrt(5)/2,2.5
w1=lambda s:(s+.5)/(2*s*(3.5-s)); w2=lambda s:(s-.5)/(2*s*(s+3.5))
sig=[lambda s:np.sqrt(3.75-s), lambda s:np.sqrt(3.75+s)]; Wf=[w1,w2]
words=list(itertools.product([0,1],repeat=n))
res=[]
def ok(c,m): res.append(bool(c)); print(('PASS ' if c else 'FAIL ')+m, flush=True)
def pts(x):
    P=[];Wt=[]
    for w in words:
        y=x; lw=1.0
        for i in w: lw*=Wf[i](y); y=sig[i](y)
        P.append(y); Wt.append(lw)
    return np.array(P),np.array(Wt)
nfail=[0]
# v2: HiGHS rejects the LP when e^(a d) > 1e20 (gaps up to 0.58, e^58); so solve the same
# linear-fractional programme by my own Dinkelbach-style bisection on a chain DP, then rebuild the
# bang-bang maximiser and evaluate the ratio explicitly as a primal check.
def chain(s,A,B):
    o=np.argsort(s); s,A,B=s[o],A[o],B[o]; d=np.diff(s); return s,A,B,d
def V1(t,A,B,d):
    c=A-t*B; V=c[-1]; ch=[]
    for k in range(len(c)-2,-1,-1):
        up=np.exp(a*d[k])*V; dn=np.exp(-a*d[k])*V
        ch.append(up>=dn); V=c[k]+max(up,dn)
    return V,ch[::-1]
def rho(x,y):
    px,ax=pts(x); py,by=pts(y)
    s,A,B,d=chain(np.concatenate([px,py]),np.concatenate([ax,0*ax]),np.concatenate([0*by,by]))
    lo_,hi_=0.0,1e30
    # upper bracket: ratio <= max over constraint-feasible u, start doubling from 1
    hi_=1.0
    while V1(hi_,A,B,d)[0]>0: hi_*=2
    for _ in range(200):
        m=0.5*(lo_+hi_)
        if V1(m,A,B,d)[0]>0: lo_=m
        else: hi_=m
        if hi_-lo_<1e-15*hi_: break
    # primal: rebuild bang-bang u at hi_ and evaluate ratio
    _,ch=V1(lo_,A,B,d); lu=np.zeros(len(A))
    for k in range(len(d)): lu[k+1]=lu[k]+(a*d[k] if ch[k] else -a*d[k])
    lu-=lu.max(); u=np.exp(lu); prim=np.log((A@u)/(B@u))
    if abs(prim-np.log(hi_))>1e-9: nfail[0]+=1; print("primal/dual gap",x,y,prim,np.log(hi_))
    return np.log(hi_)
# DF.1(i): b_1, b_8 from CF.2 constants, recomputed in mpmath
s0=mp.sqrt(5)/2; c1=1/mp.sqrt(5); c2=1/(2*mp.sqrt(mp.mpf(15)/4+s0)); M1=mp.mpf(14)/15
lw2=lambda s: mp.log((s-mp.mpf(1)/2)/(2*s*(s+mp.mpf(7)/2))); M2=abs(mp.diff(lw2,s0))
print("c2",c2,"M2",M2)
ok(abs(M2-mp.mpf('0.50706443'))<1e-7,"M2 = (log w2)'(sqrt5/2) = 0.50706443")
phi=lambda b:max(M1+c1*b,M2+c2*b); b=mp.mpf(100); bs=[b]
for _ in range(8): bs.append(phi(bs[-1]))
print("b1",bs[1],"b8",bs[8]); ok(abs(bs[1]-mp.mpf('45.654693'))<1e-5 and bs[8]<=mp.mpf('1.8457144'),"b_1=45.654693, b_8<=1.8457144 (script docstring) (%s)"%mp.nstr(bs[8],12))
print("NOTE: GASKET.md text says b_8 <= 1.845714396 but exact b_8 =",mp.nstr(bs[8],15),"exceeds it by",mp.nstr(bs[8]-mp.mpf('1.845714396'),3))
b8=bs[8]
# images disjoint
g=np.linspace(lo,hi,401); PP=np.array([pts(t)[0] for t in g]).T; H=sorted((p.min(),p.max()) for p in PP)
gaps=[H[i+1][0]-H[i][1] for i in range(255)]; print("min sampled gap",min(gaps))
ok(min(gaps)>0,"256 images sigma_w(X_s) disjoint (sampled hulls); min gap %.3g (repo 7.95e-6)"%min(gaps))
t0=time.time(); e1=rho(lo+1e-9,hi-1e-9); e2=rho(hi-1e-9,lo+1e-9); print("endpoint joint",e1+e2,"(%.1fs)"%(time.time()-t0))
ok(0.04297<=e1+e2<=0.04451,"endpoint joint term in [W_low, W_F] (%.8f)"%(e1+e2))
NG=int(sys.argv[1]) if len(sys.argv)>1 else 17
X=np.linspace(lo,hi,NG); R=np.zeros((NG,NG))
for i,x in enumerate(X):
    for j,y in enumerate(X):
        if i!=j: R[i,j]=rho(x,y)
J=R+R.T; Wg=np.nanmax(J); i,j=np.unravel_index(np.nanargmax(J),J.shape)
print("primal/dual mismatches",nfail[0],"grid max joint",Wg,"at",X[i],X[j])
ok(Wg<=0.04451,"%dx%d grid sup of joint term <= W_F=0.04451 (%.8f)"%(NG,NG,Wg))
WF=mp.mpf('0.04449994'); cone=2*mp.log((100+b8)/(100-b8)); D=cone+WF; th=mp.tanh(D/4)
print("cone",cone,"Delta",D,"theta",th,"rate",th**(mp.mpf(1)/8))
ok(abs(cone-mp.mpf('0.07383696'))<2e-8,"cone-lemma term 0.07383696")
ok(D<0.11835 and th<0.02958 and th**(mp.mpf(1)/8)<0.64398,"Delta_F, theta_F, rate")
r0=mp.mpf('0.42373128696260814'); mu=th**(mp.mpf(1)/8)*r0; print("mu",mu); ok(mu<0.27288,"theta_F^(1/8) r < 0.27288 (%s)"%mp.nstr(mu,10))
B0=mp.mpf('1.2791803'); TG=2*mp.log((100+B0)/(100-B0))+mp.mpf('0.063592701'); print("Theta_G'",TG); ok(TG<0.11477 and abs(TG-mp.mpf('0.11476270'))<1e-7,"Theta_G' = 0.11476270")
CF=TG*th**(-mp.mpf(11)/8); print("C_F",CF); ok(CF<14.531,"C_F < 14.531")
thE=mp.tanh((2*mp.log((mp.mpf(47)/2+mp.mpf('2.0785933'))/(mp.mpf(47)/2-mp.mpf('2.0785933')))+mp.mpf('0.29039894'))/4); TGE=mp.mpf('0.28154093')
DE4=lambda k: thE**((k-4)//5)*TGE; DF4=lambda k: th**((k-4)//8)*TG
exc=[k for k in range(4,400) if DF4(k)>=DE4(k)]; print("k where DE.4 smaller:",exc)
ok(exc==[9,10,11,19],"DF.4 smaller for all k>=4 except 9,10,11,19 (checked k<400)")
rat={k:DE4(k)/DF4(k) for k in (4,9,12,20,24,54,104)}; print({k:mp.nstr(v,5) for k,v in rat.items()})
ok(all(abs(rat[k]-v)/v<3e-3 for k,v in {4:2.453,9:0.392,12:13.26,20:11.47,24:1.833,54:40.05,104:653.9}.items()),"DE.4/DF.4 ratios")
T0=2*mp.log((100+mp.mpf(14)/15)/(100-mp.mpf(14)/15))+mp.log(mp.mpf(11)/6); ok(abs(T0-mp.mpf('0.643470'))<1e-6,"Theta_0(100)=0.643470 (%s)"%mp.nstr(T0,8))
print(sum(res),"/",len(res))
