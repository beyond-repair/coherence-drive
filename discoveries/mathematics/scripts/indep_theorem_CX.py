# v2: high-precision collocation (mpmath) because float eigvals are ill-conditioned for k>~25 (v1 failure kept in indep_cx.log)
import sys
from mpmath import mp, mpf, sqrt, cos, pi, acos, matrix, eig, lu_solve, inverse
mp.dps=60; P=F=0
def chk(n,c):
    global P,F
    if c: P+=1
    else: F+=1; print("FAIL",n)
Bst=mpf('0.77737602763333190375'); Gst=mpf('0.28706524176038901924')
a,b=sqrt(5)/2,mpf(5)/2
def build(N):
    x=[cos(pi*(j+mpf(1)/2)/N) for j in range(N)]; t=[(a+b)/2+(b-a)/2*xi for xi in x]
    Tn=matrix(N,N)
    for i in range(N):
        for j in range(N): Tn[i,j]=cos(j*acos(x[i]))
    Ti=inverse(Tn)
    def interp(pts):
        T=matrix(N,N)
        for i,p in enumerate(pts):
            y=(2*p-(a+b))/(b-a)
            for j in range(N): T[i,j]=cos(j*acos(y))
        return T*Ti
    S1=[sqrt(mpf(15)/4-s) for s in t]; S2=[sqrt(mpf(15)/4+s) for s in t]
    W1=[(s+mpf(1)/2)/(2*s*(mpf(7)/2-s)) for s in t]; W2=[(s-mpf(1)/2)/(2*s*(s+mpf(7)/2)) for s in t]
    return t,S1,S2,W1,W2,interp(S1),interp(S2)
def rho(k,D):
    t,S1,S2,W1,W2,I1,I2=D; N=len(t)
    M=matrix(N,N)
    for i in range(N):
        u1=3**(k+1)*W1[i]/(2*S1[i])**k; u2=3**(k+1)*W2[i]/(2*S2[i])**k
        for j in range(N): M[i,j]=u1*I1[i,j]+u2*I2[i,j]
    # power iteration (positive operator, dominant eigenvalue simple)
    v=matrix([1]*N); lam=0
    for _ in range(120):
        w=M*v; lam=w[N//2]/v[N//2]; v=w/w[N//2]
    return lam/3**(k+1)
D1=build(40); D2=build(56)
br={0:('0.916881','0.966669'),1:('0.911993','0.956446'),12:('0.995044','0.999926'),13:('0.996648','1.001488'),20:('1.000366','1.002947'),39:('1.000050','1.000199'),40:('1.000042','1.000169')}
chk("rho1",abs(rho(1,D2)/mpf('0.1343549829703998131')-1)<mpf(10)**-15)
vals=[]
for k in range(41):
    r=rho(k,D2); r1=rho(k,D1); e=3**(k+1)*r-1; e1=3**(k+1)*r1-1
    chk(f"N-stable k={k}",abs(e/e1-1)<mpf(10)**-6)
    vals.append(3**k*r); c=e/(Gst*Bst**k)
    if k in br:
        print("k",k,"c_k",mp.nstr(c,9),br[k]); chk(f"c_{k}",mpf(br[k][0])<c<mpf(br[k][1]))
    if k==13: print("rho13",mp.nstr(r,10)); chk("rho13",mpf('2.113399e-7')<r<mpf('2.113510e-7'))
    if k==39: print("rho39",mp.nstr(r,12)); chk("rho39",mpf('8.2253915e-20')<r<mpf('8.2253916e-20'))
chk("monotone",all(vals[i]>vals[i+1] for i in range(40)))
rat=max((3*vals[k+1]-1)/(3*vals[k]-1) for k in range(40)); print("max eps ratio",mp.nstr(rat,6)); chk("ratio<0.81359",rat<0.81359)
print("PASS",P,"FAIL",F); sys.exit(1 if F else 0)
