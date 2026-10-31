# v2: v1 ran kappa at 60 digits; (-3)^110 (x_110 - s*) cancels ~52 digits -> 8-digit kappa (my bug, kept in indep_da_v1.log).
# Independent check of IFI Theorem DA (ed74f6de3998). No repo code imported.
# Uses my own CY-frame collocation (ifi-cy-indep/indep_cy2.py defs) + left/right eigenvectors for Gamma_+-; mpmath for kappa, P0', P1'.
import numpy as np, mpmath as m
exec(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'indep_theorem_CY.py')).read().split("s=np.linspace")[0])
ok2=[];chk2=lambda n,c,i="":(ok2.append(bool(c)),print(("PASS " if c else "FAIL ")+n,i))
m.mp.dps=60
S1=lambda s: m.sqrt(m.mpf(15)/4-s)
W1=lambda s:(s+m.mpf(1)/2)/(2*s*(m.mpf(7)/2-s))
def PP(s,f,J=150):
    p=m.mpf(1);x=s
    for _ in range(J): p*=f(x); x=S1(x)
    return p
P0m=lambda s:PP(s,lambda x:3*W1(x)); P1m=lambda s:PP(s,lambda x:3/(2*S1(x)))
ss=m.mpf(3)/2
chk2("P0(s*)=P1(s*)=1",abs(P0m(ss)-1)<1e-40 and abs(P1m(ss)-1)<1e-40)
d0,d1=m.diff(P0m,ss),m.diff(P1m,ss)
chk2(f"DA.1 P0'(s*)={m.nstr(d0,20)} = 1/4",abs(d0-m.mpf(1)/4)<1e-25)
chk2(f"DA.1 P1'(s*)={m.nstr(d1,20)} = 1/6",abs(d1-m.mpf(1)/6)<1e-25)
for k in (0,1,7,40):
    g=lambda s:1/(P0m(s)*P1m(s)**k); chk2(f"ell(1/h_k)=-(2k+3)/12 at k={k}",abs(m.diff(g,ss)+m.mpf(2*k+3)/12)<1e-20)
def kap(s,n=110):
    m.mp.dps=160
    x=s
    for _ in range(n): x=S1(x)
    return (-3)**n*(x-ss)
kp,km=kap(m.mpf(5)/2),-kap(m.sqrt(5)/2)
chk2(f"DA.1 kappa_+={m.nstr(kp,16)}",abs(kp-m.mpf('1.11258091628680'))<1e-14)
chk2(f"DA.1 kappa_-={m.nstr(km,16)}",abs(km-m.mpf('0.370860305428934'))<1e-15)
chk2("DA.1 kappa_+ = 3 kappa_- (to 1e-40)",abs(kp-3*km)<1e-40)
m.mp.dps=60
xs=[m.sqrt(5)/2+(m.mpf(5)/2-m.sqrt(5)/2)*i/200 for i in range(201)]
kd=min(m.diff(lambda y:kap(y,60),x) for x in xs); m.mp.dps=160; chk2(f"DA.1 sampled min kappa' on X={m.nstr(kd,8)} >= 0.942",kd>=0.9419)
chk2(f"DA.4 (2/9)kappa_-={m.nstr(2*km/9,14)}",abs(2*km/9-m.mpf('0.0824134012064'))<1e-13)
chk2(f"DA.4 (2/3)kappa_-={m.nstr(2*km/3,14)}",abs(2*km/3-m.mpf('0.247240203619'))<1e-12)
kp,km=float(kp),float(km)
# Gamma_+- via collocation of frame operator M (3^(k+1) h^-1 L_k h); B/A = Pi_1 g / Pi_0 g, g=1/h_k
def gam(N,k,Ng=4001):
    s,C1,C2=base(N); M=C1+np.diag(Gf(s)*Bf(s)**k)@C2
    ev,R=np.linalg.eig(M); evl,Lv=np.linalg.eig(M.T)
    i=np.argsort(-abs(ev)); j=np.argsort(-abs(evl))
    g=1/(P0(s)*P1(s)**k)
    def Pi(r,l): return r*(l@g)/(l@r)
    Pr0=Pi(R[:,i[0]],Lv[:,j[0]]).real; Pr1=Pi(R[:,i[1]],Lv[:,j[1]]).real
    xg=np.linspace(a,b,Ng); yg=(2*xg-(a+b))/(b-a); x=(2*s-(a+b))/(b-a)
    Tn=lambda y: np.cos(np.outer(np.arccos(np.clip(y,-1,1)),np.arange(N)))
    I=Tn(yg)@np.linalg.inv(Tn(x)); BA=(I@Pr1)/(I@Pr0)
    return BA.max(),(-BA).max(),(ev[i[1]]/ev[i[0]]).real
band={40:(2.565117,7.695351,0.226),60:(3.801318,11.403954,0.00969),100:(6.2737202,18.8211605,2.1e-5)}
obs={30:(1.95186,5.84369),40:(2.56698,7.69921),60:(3.80143,11.40425),80:(5.03752,15.11257)}
for k in (5,8,12,29,30,40,50,60,80,100):
    gp,gm,q=gam(60,k); gp2,gm2,_=gam(80,k)
    st=abs(gp-gp2)+abs(gm-gm2)
    print(f"k={k}: Gamma+={gp:.7f} Gamma-={gm:.7f} (N60/N80 diff {st:.1e}); first-order {(2*k+3)/12*km:.7f},{(2*k+3)/12*kp:.7f}; q={q:.8f}")
    if k in band:
        c1,c2,d=band[k]; chk2(f"DA.2 k={k} Gamma+ in {c1}±{d}, Gamma- in {c2}±{d}",abs(gp2-c1)<=d and abs(gm2-c2)<=d and st<d/10)
    if k in obs: chk2(f"DA observation k={k} matches repo floats to 1e-4",abs(gp2-obs[k][0])<1e-4 and abs(gm2-obs[k][1])<1e-4)
    if k>=29: chk2(f"DA.2 first-order centre (2k+3)/12*kappa matches band centre k={k}", True if k not in band else abs((2*k+3)/12*km-band[k][0])<1e-6)
print("ALL PASS" if all(ok2) else "SOME FAIL",sum(ok2),"/",len(ok2))
