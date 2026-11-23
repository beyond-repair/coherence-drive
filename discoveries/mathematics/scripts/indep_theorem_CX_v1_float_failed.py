# Independent check of IFI Theorem CX (4dc70c635d0b). numpy+mpmath only, no repo code.
import numpy as np, sys
from mpmath import mp, mpf, sqrt, log, exp
mp.dps=40; P=F=0
def chk(n,c):
    global P,F
    if c: P+=1
    else: F+=1; print("FAIL",n)
s1=lambda s: sqrt(mpf(15)/4-s); s2=lambda s: sqrt(mpf(15)/4+s)
w1=lambda s:(s+mpf(1)/2)/(2*s*(mpf(7)/2-s))
def Phi(s):
    x=mpf(s);v=mpf(0)
    for _ in range(200): y=s1(x); v-=log(2*y/3); x=y
    return v
def Psi(s):
    x=mpf(s);v=mpf(0)
    for _ in range(200): v+=log(3*w1(x)); x=s1(x)
    return v
w2=lambda s:(s-mpf(1)/2)/(2*s*(s+mpf(7)/2))
sst=mpf(3)/2
Bst=3/(2*s2(sst))*exp(Phi(s2(sst))-Phi(sst)); Gst=3*w2(sst)*exp(Psi(s2(sst))-Psi(sst))
print("B*",mp.nstr(Bst,20),"G*",mp.nstr(Gst,20))
chk("B*",abs(Bst-mpf('0.77737602763333190375'))<1e-19); chk("G*",abs(Gst-mpf('0.28706524176038901924'))<1e-19)
chk("B* closed form",abs(Bst-3/sqrt(21)*exp(Phi(sqrt(21)/2)))<1e-30)
chk("theta0",abs((3-sqrt(5))/2-1/(s1(mpf(5)/2)+mpf(3)/2))<1e-30)  # worst contraction at x=5/2? sigma1(5/2)=sqrt5/2
# Chebyshev collocation for rho(L_k) on X, float
a,b=np.sqrt(5)/2,2.5; N=48
x=np.cos(np.pi*(np.arange(N)+0.5)/N); t=(a+b)/2+(b-a)/2*x
def interp(pts):
    y=(2*pts-(a+b))/(b-a); T=np.cos(np.outer(np.arccos(np.clip(y,-1,1)),np.arange(N)))
    Tn=np.cos(np.outer(np.arccos(x),np.arange(N))); return T@np.linalg.inv(Tn)
S1=np.sqrt(3.75-t); S2=np.sqrt(3.75+t); W1=(t+.5)/(2*t*(3.5-t)); W2=(t-.5)/(2*t*(t+3.5))
I1=interp(S1); I2=interp(S2)
def rho(k):
    M=(W1/(2*S1)**k)[:,None]*I1+(W2/(2*S2)**k)[:,None]*I2
    return max(abs(np.linalg.eigvals(M)))
B=float(Bst); G=float(Gst)
br={0:(0.916881,0.966669),1:(0.911993,0.956446),12:(0.995044,0.999926),13:(0.996648,1.001488),20:(1.000366,1.002947),39:(1.000050,1.000199),40:(1.000042,1.000169)}
known={1:0.1343549829703998131,12:6.359658135257e-7}
for k,r in known.items(): chk(f"colloc rho k={k}",abs(rho(k)/r-1)<1e-9)
vals=[3**k*rho(k) for k in range(0,41)]
c=[(3*v-1)/(G*B**k) for k,v in enumerate(vals)]
for k,(lo,hi) in br.items():
    print("k",k,"c_k",round(c[k],7),"bracket",lo,hi); chk(f"c_{k} in bracket",lo<c[k]<hi)
chk("monotone 3^k rho k<=40",all(vals[i]>vals[i+1] for i in range(40)))
chk("all > 1/3",all(v>1/3 for v in vals))
chk("c_k<1 k<=12",all(c[k]<1 for k in range(13))); chk("c_k>1 20..40",all(c[k]>1 for k in range(20,41)))
r13=rho(13); chk("rho13 bracket",2.113399e-7<r13<2.113510e-7); print("rho13",r13,"rho20",rho(20))
chk("rho20 bracket",9.577739e-11<rho(20)<9.577786e-11)
print("ratios eps_{k+1}/eps_k max",max((3*vals[k+1]-1)/(3*vals[k]-1) for k in range(40)))
print("PASS",P,"FAIL",F); sys.exit(1 if F else 0)
