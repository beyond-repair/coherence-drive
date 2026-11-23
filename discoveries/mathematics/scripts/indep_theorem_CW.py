# Independent check of IFI Theorem CW (572ca675ce2e). mpmath only, no repo code.
from mpmath import mp, mpf, sqrt, log, exp, linspace
import random, sys
mp.dps=40
P=F=0
def chk(name,c):
    global P,F
    if c: P+=1
    else: F+=1; print("FAIL",name)
s1=lambda s: sqrt(mpf(15)/4-s); s2=lambda s: sqrt(mpf(15)/4+s)
w1=lambda s:(s+mpf(1)/2)/(2*s*(mpf(7)/2-s)); w2=lambda s:(s-mpf(1)/2)/(2*s*(s+mpf(7)/2))
J=200
def PhiPsi(s):
    x=mpf(s);Ph=Ps=mpf(0)
    for _ in range(J):
        y=s1(x); Ph-=log(2*y/3); Ps+=log(3*w1(x)); x=y
    return Ph,Ps
lo,hi=sqrt(5)/2,mpf(5)/2
def BG(s):
    a,b=PhiPsi(s); c,d=PhiPsi(s2(s))
    return 3/(2*s2(s))*exp(c-a), 3*w2(s)*exp(d-b)
# 1. fixed point facts
chk("s*", abs(s1(mpf(3)/2)-mpf(3)/2)<mpf(10)**-35); chk("w1(s*)=1/3",abs(w1(mpf(3)/2)-mpf(1)/3)<mpf(10)**-35)
chk("s2 fixed 5/2",abs(s2(mpf(5)/2)-mpf(5)/2)<1e-35)
# 2. identity L_k h_k/h_k = 3^{-k-1}(1+G B^k) at random s, several real k
random.seed(1)
for _ in range(12):
    s=lo+(hi-lo)*mpf(random.random()); k=mpf(random.choice([0,0.5,1,3,7.3,12,25]))
    h=lambda t: exp(k*PhiPsi(t)[0]+PhiPsi(t)[1])
    lhs=(w1(s)/(2*s1(s))**k*h(s1(s))+w2(s)/(2*s2(s))**k*h(s2(s)))/h(s)
    B,G=BG(s); rhs=mpf(3)**(-k-1)*(1+G*B**k)
    chk("identity",abs(lhs/rhs-1)<mpf(10)**-25)
# 3. grid extremes of B,G (floats sanity vs certified bracket)
Bs=[];Gs=[]
for s in linspace(lo,hi,801):
    B,G=BG(s); Bs.append(B); Gs.append(G)
print("grid B",float(min(Bs)),float(max(Bs)),"G",float(min(Gs)),float(max(Gs)))
chk("B in bracket",0.5999<min(Bs) and max(Bs)<0.8352); chk("G in bracket",0.1999<min(Gs) and max(Gs)<0.2873)
chk("B(5/2)=3/5",abs(BG(hi)[0]-mpf(3)/5)<1e-30); chk("G(5/2)=1/5",abs(BG(hi)[1]-mpf(1)/5)<1e-30)
# 4. power iteration rho(L_k) on a fine grid (Chebyshev-free: direct composition of exact branches, depth n) vs bracket
def rho_est(k,n=18):
    # L_k^n 1 evaluated exactly at s via 2^n path sums, ratio estimate
    def Ln1(s,n):
        if n==0: return mpf(1)
        return w1(s)/(2*s1(s))**k*Ln1(s1(s),n-1)+w2(s)/(2*s2(s))**k*Ln1(s2(s),n-1)
    s=mpf(3)/2
    return Ln1(s,n)/Ln1(s,n-1)
mp.dps=20
known={1:mpf('0.1343549829703998131'),2:mpf('0.0430703112227101271'),3:mpf('0.0139192547691468646'),4:mpf('0.0045264690852562123'),5:mpf('0.0014792559239634748'),12:mpf('6.359658135257e-7')}
for k,r in known.items():
    v=mpf(3)**(k+1)*r-1
    chk(f"known k={k} inside",0.1999*0.5999**k<=v<=0.2873*0.8352**k)
for k in [1,2,13,20]:
    r=rho_est(k); v=mpf(3)**(k+1)*r-1
    print("k",k,"path-sum rho est",mp.nstr(r,12),"3^(k+1)rho-1",mp.nstr(v,6))
    chk(f"path-sum k={k} inside",0.1999*0.5999**k<=v<=0.2873*0.8352**k)
    if k in known: chk(f"path-sum matches k={k}",abs(r/known[k]-1)<1e-6)
print("PASS",P,"FAIL",F); sys.exit(1 if F else 0)
