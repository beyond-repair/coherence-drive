# Independent check of IFI Theorem DE (commit 8cbaea3aa21f) -- from GASKET.md text only.
# Joint term via linear-fractional LP (Charnes-Cooper, scipy HiGHS), not the repo's DP.
import numpy as np, itertools, mpmath as mp
from scipy.optimize import linprog
a=23.5; lo,hi=np.sqrt(5)/2,2.5
w1=lambda s:(s+.5)/(2*s*(3.5-s)); w2=lambda s:(s-.5)/(2*s*(s+3.5))
sig=[lambda s:np.sqrt(3.75-s), lambda s:np.sqrt(3.75+s)]; Wf=[w1,w2]
words=list(itertools.product([0,1],repeat=5))
res=[]
def ok(c,m): res.append(c); print(('PASS ' if c else 'FAIL ')+m, flush=True)
def pts(x):
    P=[];Wt=[]
    for w in words:
        y=x; lw=1.0
        for i in w: lw*=Wf[i](y); y=sig[i](y)
        P.append(y); Wt.append(lw)
    return np.array(P),np.array(Wt)
def rho(x,y):
    px,ax=pts(x); py,by=pts(y)
    s=np.concatenate([px,py]); A=np.concatenate([ax,0*ax]); B=np.concatenate([0*by,by])
    o=np.argsort(s); s,A,B=s[o],A[o],B[o]; n=len(s); d=np.diff(s); e=np.exp(a*d)
    G=np.zeros((2*(n-1),n))
    for k in range(n-1):
        G[2*k,k+1]=1;G[2*k,k]=-e[k]; G[2*k+1,k]=1;G[2*k+1,k+1]=-e[k]
    r=linprog(-A,A_ub=G,b_ub=np.zeros(2*(n-1)),A_eq=B[None,:],b_eq=[1],bounds=[(0,None)]*n,method='highs')
    if r.status!=0: r=linprog(-A,A_ub=G,b_ub=np.zeros(2*(n-1)),A_eq=B[None,:],b_eq=[1],bounds=[(0,None)]*n,method='highs-ipm')
    if r.status!=0: print("LP status",r.status,r.message,x,y); return np.nan
    return np.log(-r.fun)
# images pairwise disjoint (check on dense grid hulls)
g=np.linspace(lo,hi,2001); H=sorted((pts_ := None) or [ (min(v),max(v)) for v in np.array([pts(t)[0] for t in g]).T ])
ok(all(H[i][1]<H[i+1][0] for i in range(31)),"32 images sigma_w(X_s) disjoint (sampled hulls)")
r_end=rho(lo+1e-9,hi-1e-9)+rho(hi-1e-9,lo+1e-9); print("joint at endpoints",r_end)
ok(0.29009<=r_end<=0.29040,"endpoint joint term in [W_low, W_E] (%.8f)"%r_end)
N=41; X=np.linspace(lo,hi,N); R=np.array([[rho(x,y) if i!=j else 0 for j,y in enumerate(X)] for i,x in enumerate(X)])
nbad=np.isnan(R).sum(); print("LP failures",nbad); J=R+R.T; Wg=np.nanmax(J); i,j=np.unravel_index(np.nanargmax(J),J.shape); print("grid max joint",Wg,"at",X[i],X[j])
ok(Wg<=0.29040,"41x41 grid sup of joint term <= W_E=0.29040 (%.8f)"%Wg)
ok(Wg>=0.29009,"grid sup >= W_low")
print("grid max single rho",np.nanmax(R)); ok(np.nanmax(R)>=0.66531 and np.nanmax(R)<=0.73438,"single-function osc in [0.66531, V_D] (%.6f)"%np.nanmax(R))
b5=mp.mpf('2.0785933'); A_=mp.mpf(47)/2; WE=mp.mpf('0.29039894')
D=2*mp.log((A_+b5)/(A_-b5))+WE; th=mp.tanh(D/4); print("cone term",2*mp.log((A_+b5)/(A_-b5)),"Delta",D,"theta",th,"rate",th**0.2)
ok(D<0.64513 and th<0.15990 and th**0.2<0.69306,"Delta_E, theta_E, rate")
CE=mp.mpf('0.28154093')*th**(-mp.mpf(8)/5); print("C_E",CE); ok(CE<5.28923,"C_E < 5.28923")
thD=mp.mpf('0.4267121774'); rr={k:(thD/th)**((k-4)//5) for k in (9,14,24,54)}; print(rr)
ok(all(abs(rr[k]-v)/v<2e-3 for k,v in {9:2.6687,14:7.1219,24:50.722,54:1.83e4}.items()),"DD.3/DE.4 ratios")
r0=0.42373128696260814; ok(float(th**0.2)*r0<0.29367,"theta_E^(1/5) r < 0.29367 (%.6f)"%(float(th**0.2)*r0))
print(sum(res),"/",len(res))
