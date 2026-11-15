# Independent check of IFI Theorem DD (commit 1630b8a08515) -- written from GASKET.md text only, numpy + mpmath.
import numpy as np, itertools, mpmath as mp
mp.mp.dps=40
a=23.5; lo,hi=np.sqrt(5)/2,2.5
w1=lambda s:(s+.5)/(2*s*(3.5-s)); w2=lambda s:(s-.5)/(2*s*(s+3.5))
sig=[lambda s:np.sqrt(3.75-s), lambda s:np.sqrt(3.75+s)]; W=[w1,w2]
res=[]
def ok(c,m): res.append(c); print(('PASS ' if c else 'FAIL ')+m)
N=1601; x=np.linspace(lo,hi,N)
# maps stay in X_s
ok(all(((s(x)>=lo-1e-12)&(s(x)<=hi+1e-12)).all() for s in sig),"sigma_i map X_s into X_s")
best=(-1,None)
for w in itertools.product([0,1],repeat=5):
    y=x.copy(); lw=np.zeros(N)
    for i in w: lw+=np.log(W[i](y)); y=sig[i](y)
    M=(lw[:,None]-lw[None,:]+a*np.abs(y[:,None]-y[None,:])).max()
    if M>best[0]: best=(M,w)
Vpt,ww=best
print("pointwise pair max",Vpt,"word",''.join(str(i+1) for i in ww))
ok(Vpt<=0.73438 and Vpt>0.73,"pointwise pairwise max <= V_D=0.73438 and close (%.8f)"%Vpt)
ok(ww==(0,0,0,0,0),"maximiser word 11111")
# floor V_low: osc of log Lt^5 e^{+-as}
def L5log(s,sg):
    def rec(s,n):
        if n==0: return mp.e**(sg*a*s)
        return sum(Wi(s)*rec(mp.sqrt(mp.mpf(15)/4+(-1 if i==0 else 1)*s),n-1) for i,Wi in enumerate([lambda t:(t+mp.mpf(1)/2)/(2*t*(mp.mpf(7)/2-t)),lambda t:(t-mp.mpf(1)/2)/(2*t*(t+mp.mpf(7)/2))]))
    return mp.log(rec(s,5))
pts=[mp.sqrt(5)/2+(mp.mpf(5)/2-mp.sqrt(5)/2)*j/256 for j in range(257)]
Vl=max(max(v)-min(v) for v in [[L5log(p,sg) for p in pts] for sg in (1,-1)])
print("V_low (257 pts)",Vl)
ok(abs(Vl-0.51383489)<2e-3 and Vl<=0.5138349+1e-9,"V_low ~ 0.51383 (sampled, below certified)")
ok(Vl<=Vpt,"floor <= upper bound")
b5=mp.mpf('2.078593340'); A=mp.mpf(47)/2
Dl=2*mp.log((A+b5)/(A-b5))+2*mp.mpf('0.73437493'); th=mp.tanh(Dl/4)
print("Delta",Dl,"theta",th,"theta^1/5",th**0.2)
ok(Dl<1.82349 and th<0.42672 and th**0.2<0.84339,"Delta_D, theta_D, rate")
thCF=mp.tanh((2*mp.log((A+b5)/(A-b5))+2*mp.mpf('1.0426526'))/4)
ok(abs(thCF-0.5441333)<1e-6,"CF theta reproduced 0.5441333 (%s)"%mp.nstr(thCF,10))
ratios={k:(thCF/th)**((k-4)//5) for k in (9,14,24,54)}; print(ratios)
ok(all(abs(ratios[k]-v)/v<1e-3 for k,v in {9:1.2752,14:1.6261,24:2.6441,54:11.368}.items()),"DC.3/DD.3 ratios")
CD=mp.mpf('0.28154093')*th**(-mp.mpf(8)/5); print("C_D",CD); ok(CD<=1.09984,"C_D <= 1.09984")
ok(all(th**((k-4)//5)<=th**(mp.mpf(k)/5-mp.mpf(8)/5)+mp.mpf(10)**-30 for k in range(4,200)),"floor form <= C_D theta^(k/5)")
# r by power iteration on Chebyshev nodes (float), check theta^1/5 r
from numpy.polynomial import chebyshev as C
n=60; t=np.cos(np.pi*(np.arange(n)+.5)/n); s=(lo+hi)/2+(hi-lo)/2*t
V=C.chebvander(t,n-1); Vi=np.linalg.inv(V)
def ev(sv): return C.chebvander((sv-(lo+hi)/2)/((hi-lo)/2),n-1)@Vi
Lm=np.diag(w1(s))@ev(sig[0](s))+np.diag(w2(s))@ev(sig[1](s))
eg=sorted(np.abs(np.linalg.eigvals(Lm)))[::-1]; r=eg[0]; print("r",r,"|l2|/r",eg[1]/r)
ok(abs(eg[1]/r-0.1725)<5e-4,"spectral ratio 0.1725 (CG)")
ok(float(th**0.2)*r<0.3575,"theta_D^(1/5) r < 0.3575 (%.6f)"%(float(th**0.2)*r))
print(sum(res),"/",len(res))
