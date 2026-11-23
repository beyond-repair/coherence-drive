"""Independent float/mpmath cross-check of IFI Theorem DH (a273479fb361). Own code from GASKET.md text; not a certificate."""
import math, numpy as np, mpmath as mp, itertools, time
A=100.0; N=9; lo,hi=math.sqrt(5)/2,2.5
res=[]
def ok(c,m): res.append(bool(c)); print(("PASS " if c else "FAIL ")+m, flush=True)
def orbit(s):
    L=[(s,1.0,0.0,1.0)]
    for _ in range(N):
        nx=[]
        for p,w,dl,J in L:
            for sg in (-1,1):
                t=math.sqrt(3.75+sg*p)
                if sg<0: wt=(p+.5)/(2*p*(3.5-p)); lw=1/(p+.5)-1/p+1/(3.5-p)
                else:    wt=(p-.5)/(2*p*(p+3.5)); lw=1/(p-.5)-1/p-1/(p+3.5)
                nx.append((t,w*wt,dl+lw*J,J*sg/(2*t)))
        L=nx
    L.sort(key=lambda r:r[0]); return L
def supratio(n,w,pts):
    # v2: bisection on the exact chain DP (v1's Dinkelbach iteration stalled below the sup near s = 2.5; my bug)
    d=np.diff(pts); l,h=-10.0,10.0
    for _ in range(80):
        m=0.5*(l+h); c=n-m*w; V=c[-1]
        for k in range(len(c)-2,-1,-1): V=c[k]+max(math.exp(A*d[k])*V, math.exp(-A*d[k])*V)
        if V>0: l=m
        else: h=m
    return h
def slopes(s):
    L=orbit(s); p=np.array([r[0] for r in L]); w=np.array([r[1] for r in L])
    dl=np.array([r[2] for r in L]); J=np.abs([r[3] for r in L]); assert len(p)==512 and np.all(np.diff(p)>0)
    return supratio(w*(dl+A*J),w,p), supratio(w*(A*J-dl),w,p)
t0=time.time(); R=[slopes(s) for s in np.linspace(lo,hi,129)]
Dp=max(r[0] for r in R); Dm=max(r[1] for r in R); print(f"slope grid {time.time()-t0:.0f}s")
ok(0.74356<=Dp<0.74455, f"N=9 grid max D+ = {Dp:.6f} in [floor 0.74356, cert 0.74455)")
ok(-0.16376<=Dm<-0.16327, f"N=9 grid max D- = {Dm:.6f} in [floor -0.16376, cert -0.16327)")
# finite-difference slope of log Lt^9 f for explicit f
for f,name in ((lambda x:1.0,'1'),(lambda x:math.exp(100*x),'e^100s'),(lambda x:math.exp(100*abs(x-1.8)),'v')):
    for s in (1.3,2.4):
        h=1e-6; g=lambda q: math.log(sum(r[1]*f(r[0]) for r in orbit(q))); d=(g(s+h)-g(s-h))/(2*h)
        ok(-Dm-1e-5<=d<=Dp+1e-5, f"f={name} s={s}: (log Lt^9 f)' = {d:.5f}")
# joint term W via own chain DP with bisection (Lt^9: 1024-point line)
W1=lambda s:(s+.5)/(2*s*(3.5-s)); W2=lambda s:(s-.5)/(2*s*(s+3.5)); SG=[lambda s:math.sqrt(3.75-s),lambda s:math.sqrt(3.75+s)]; WF=[W1,W2]
words=list(itertools.product([0,1],repeat=N))
def pts(x):
    P=[];Wt=[]
    for w in words:
        y=x; lw=1.0
        for i in w: lw*=WF[i](y); y=SG[i](y)
        P.append(y); Wt.append(lw)
    return np.array(P),np.array(Wt)
def V1(t,Av,Bv,d):
    c=Av-t*Bv; V=c[-1]
    for k in range(len(c)-2,-1,-1): V=c[k]+max(math.exp(A*d[k])*V, math.exp(-A*d[k])*V)
    return V
def rho(x,y):
    px,ax=pts(x); py,by=pts(y); s=np.concatenate([px,py]); o=np.argsort(s)
    Av=np.concatenate([ax,0*ax])[o]; Bv=np.concatenate([0*by,by])[o]; d=np.diff(s[o])
    l,h=0.0,1.0
    while V1(h,Av,Bv,d)>0: h*=2
    for _ in range(80):
        m=0.5*(l+h)
        if V1(m,Av,Bv,d)>0: l=m
        else: h=m
        if h-l<1e-14*h: break
    return math.log(h)
t0=time.time(); e=rho(lo,hi)+rho(hi,lo); print(f"endpoint joint {e:.7f} ({time.time()-t0:.0f}s)")
ok(0.013764<=e<0.0142, f"endpoint joint term {e:.7f} in [W_low 0.013764, W_H 0.0142)")
X=np.linspace(lo,hi,7); Wg=max(rho(x,y)+rho(y,x) for i,x in enumerate(X) for y in X[i+1:])
ok(Wg<0.0142, f"7-point grid sup joint term {Wg:.7f} < 0.0142")
# DH.1 asymmetric factor lemma: per orientation (e^{ad}-e^{-beta_v d})/(e^{ad}-e^{alpha_u d}) <= (a+beta_v)/(a-alpha_u)
mp.mp.dps=50; a=mp.mpf(100); b0=mp.mpf('0.77333706'); B0=mp.mpf('1.2791803')
for au,bv in ((b0,B0),(B0,b0),(mp.mpf('0.74455'),mp.mpf('0.16327')),(mp.mpf('0.0'),mp.mpf('99'))):
    g0=(a+bv)/(a-au); worst=max(((mp.e**(a*d)-mp.e**(-bv*d))/(mp.e**(a*d)-mp.e**(au*d)))/g0 for d in [mp.mpf(10)**(k/4) for k in range(-60,8)])
    ok(worst<=1+mp.mpf(10)**-30, f"factor g(d)/g(0+) max {mp.nstr(worst,10)} (alpha_u,beta_v)=({mp.nstr(au,5)},{mp.nstr(bv,5)})")
# chain arithmetic
Dpc,Dmc=mp.mpf('0.74455'),mp.mpf('-0.16327')
K=max((a+Dmc)/(a-Dpc),(a+Dpc)/(a-Dmc)); cone=2*mp.log(K); ok(cone<mp.mpf('0.011679'), f"2 log K = {mp.nstr(cone,8)} < 0.011679")
D=cone+mp.mpf('0.0142'); th=mp.tanh(D/4); rate=th**(mp.mpf(1)/9)
ok(D<mp.mpf('0.025879') and th<mp.mpf('0.0064696') and rate<mp.mpf('0.57117'), f"Delta {mp.nstr(D,8)} theta {mp.nstr(th,8)} rate {mp.nstr(rate,8)}")
r0=mp.mpf('0.42373128696260814'); ok(rate*r0<mp.mpf('0.24203'), f"|mu| <= rate*r = {mp.nstr(rate*r0,8)} < 0.24203")
LR=mp.mpf('0.063592701'); TH=mp.log((a+B0)/(a-b0))+mp.log((a+b0)/(a-B0))+LR; TG=2*mp.log((a+B0)/(a-B0))+LR
ok(TH<mp.mpf('0.10465') and abs(TH-LR-mp.mpf('0.0410521'))<2e-7, f"Theta_H' = {mp.nstr(TH,9)} (cone part {mp.nstr(TH-LR,7)}), Theta_G' = {mp.nstr(TG,8)}")
thG=mp.mpf('0.014183')
DG4=lambda k: TG*thG**((k-4)//8); DH5=lambda k: TH*min(thG**((k-4)//8), th**((k-4)//9))
rr=[DG4(k)/DH5(k) for k in range(4,400)]; ok(min(rr)>=mp.mpf('1.0966'), f"min DG.4/DH.5 over k<400 = {mp.nstr(min(rr),6)}")
print({k:mp.nstr(DG4(k)/DH5(k),5) for k in (13,22,104)})
cnt=sum(1 for k in range(4,200) if th**((k-4)//9) < thG**((k-4)//8)); big=all(th**((k-4)//9) < thG**((k-4)//8) for k in range(200,600))
print("9-block smaller count k in 4..199:",cnt,"; all 200..599:",big)
print(sum(res),"/",len(res))
