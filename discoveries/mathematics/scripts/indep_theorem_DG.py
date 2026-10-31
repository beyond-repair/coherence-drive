"""Independent float/mpmath cross-check of IFI Theorem DG (347ea08d1560). Own code; not a certificate."""
import math, numpy as np, mpmath as mp
A=100.0; N=8
def orbit(s):
    # returns list of (point, wt, dlogwt/ds, dpoint/ds) for 256 words, first letter applied first
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
    # max sum n f / sum w f over f>0 with |log f_{k+1}-log f_k| <= A*(p_{k+1}-p_k): Dinkelbach + exact DP
    gap=A*np.diff(pts); Ep=np.exp(gap); Em=np.exp(-gap)
    t=0.0
    for _ in range(100):
        c=n-t*w
        # maximise sum c f with f0 free scale: track best path value with f_last=1 backwards
        V=c[-1]; choice=[]
        for k in range(len(c)-2,-1,-1):
            m=Ep[k] if V>=0 else Em[k]; choice.append(m); V=c[k]+m*V
        choice=choice[::-1]
        f=np.ones(len(c))
        for k in range(1,len(c)): f[k]=f[k-1]*choice[k-1]
        tn=(n@f)/(w@f)
        if abs(tn-t)<1e-15: break
        t=tn
    return t,f
def slopes(s):
    L=orbit(s); p=np.array([r[0] for r in L]); w=np.array([r[1] for r in L])
    dl=np.array([r[2] for r in L]); J=np.abs([r[3] for r in L])
    assert np.all(np.diff(p)>0)
    dp,_=supratio(w*(dl+A*J),w,p); dm,_=supratio(w*(A*J-dl),w,p)
    return dp,dm
s0,s1=math.sqrt(5)/2,2.5
res=[(s,)+slopes(s) for s in np.linspace(s0,s1,1025)]
Dp=max(r[1] for r in res); Dm=max(r[2] for r in res)
ok=lambda c,m: print(("PASS " if c else "FAIL ")+m)
ok(Dp<0.76155 and Dp>0.74, f"grid max D+ = {Dp:.6f} (claimed certified < 0.76155; within 2.5%)")
ok(Dm< -0.15311 and Dm>-0.17, f"grid max D- = {Dm:.6f} (claimed < -0.15311)")
# finite-difference spot check of slope formula on f = exp(100*phi)
def LT8(f,s):
    L=orbit(s); return sum(r[1]*f(r[0]) for r in L)
for f,name in ((lambda x:1.0,'1'),(lambda x:math.exp(100*x),'e^{100s}'),(lambda x:math.exp(-100*x),'e^{-100s}'),(lambda x:math.exp(100*abs(x-1.8)),'v')):
    for s in (1.3,1.9,2.4):
        h=1e-6; d=(math.log(LT8(f,s+h))-math.log(LT8(f,s-h)))/(2*h)
        ok(-Dm-1e-6<=d<=Dp+1e-6, f"f={name} s={s}: (log Lt^8 f)' = {d:.5f} in [{-Dm:.4f},{Dp:.4f}]")
# factor lemma monotonicity g(d) <= g(0+) both orientations, with high precision
mp.mp.dps=50; a=mp.mpf(100)
for al,be in ((mp.mpf(Dp),mp.mpf(Dm)),(mp.mpf(Dm),mp.mpf(Dp))):
    g0=(a+be)/(a-al); worst=max(((mp.e**(a*d)-mp.e**(-be*d))/(mp.e**(a*d)-mp.e**(al*d)))/g0 for d in [mp.mpf(10)**(k/4) for k in range(-60,8)])
    ok(worst<=1, f"factor lemma g(d)/g(0+) max {mp.nstr(worst,12)} for (alpha,beta)=({mp.nstr(al,5)},{mp.nstr(be,5)})")
# chain arithmetic with the claimed certified constants
Dpc,Dmc=mp.mpf('0.76155'),mp.mpf('-0.15311')
K=max((a+Dmc)/(a-Dpc),(a+Dpc)/(a-Dmc)); cone=2*mp.log(K)
ok(cone<mp.mpf('0.012225'), f"2 log K from claimed D+- = {mp.nstr(cone,8)} < 0.012225")
Delta=cone+mp.mpf('0.04451'); th=mp.tanh(Delta/4); rate=th**(mp.mpf(1)/8)
ok(Delta<mp.mpf('0.056735') and th<mp.mpf('0.014183') and rate<mp.mpf('0.58745'), f"Delta {mp.nstr(Delta,8)}, theta {mp.nstr(th,8)}, rate {mp.nstr(rate,8)}")
mu=rate*mp.mpf('0.27288')/mp.mpf('0.64398')  # |mu| scales as rate*r; DF used rate_F*r
ok(mu<mp.mpf('0.24893'), f"|mu| via rate_G/rate_F * DF bound = {mp.nstr(mu,8)} < 0.24893")
for k in (12,20,52): print(f"   gain DF/DG at k={k}: {mp.nstr((mp.mpf('0.02958')/th)**((k-4)//8),5)}")
