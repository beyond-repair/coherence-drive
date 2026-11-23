# Independent float check of IFI Theorem CT (219b29ba779b). Different method: Chebyshev collocation on X for the
# spectrum, and exact path-sum iteration of L_1 pointwise for h_n, R_n. No repo code imported.
import numpy as np, mpmath as mp
a,b=np.sqrt(5)/2,2.5
s1=lambda s: np.sqrt(3.75-s); s2=lambda s: np.sqrt(3.75+s)
w1=lambda s:(s+.5)/(2*s*(3.5-s)); w2=lambda s:(s-.5)/(2*s*(s+3.5))
u1=lambda s:w1(s)/(2*s1(s)); u2=lambda s:w2(s)/(2*s2(s))
ok=[];chk=lambda name,c,info="":(ok.append(bool(c)),print(("PASS " if c else "FAIL ")+name,info))
# 1. collocation spectrum
def cheb(N):
    k=np.arange(N); x=np.cos(np.pi*(2*k+1)/(2*N)); return x
def colloc(N):
    x=cheb(N); s=(a+b)/2+(b-a)/2*x
    def T(y): return np.cos(np.outer(np.arccos(np.clip(y,-1,1)),np.arange(N)))
    V=T(x); Vi=np.linalg.inv(V)
    y1=(2*s1(s)-(a+b))/(b-a); y2=(2*s2(s)-(a+b))/(b-a)
    L=np.diag(u1(s))@T(y1)@Vi+np.diag(u2(s))@T(y2)@Vi
    return np.array(sorted(np.linalg.eigvals(L),key=lambda z:-abs(z)))
e40,e60=colloc(40),colloc(60)
rho,nu=e60[0].real,e60[1].real
print("colloc eigs",e60[:4])
chk("rho collocation",abs(rho-0.1343549829703998131)<1e-13,rho)
chk("nu_2 collocation",abs(nu+0.0327933736640408162)<1e-13,nu)
chk("both real",abs(e60[0].imag)+abs(e60[1].imag)<1e-14)
chk("third |eig| < 1/100",abs(e60[2])<0.01,abs(e60[2]))
chk("N=40 vs 60 agree",abs(e40[0]-e60[0])<1e-14 and abs(e40[1]-e60[1])<1e-14)
q=nu/rho; chk("q",abs(q+0.244080070117426)<1e-12,q)
chk("rho in CI.1 [0.1343549,0.1343551]",0.1343549<=rho<=0.1343551)
# 2. path-sum h_n on a grid, mpmath not needed (float64 path sums)
xs=np.linspace(a,b,401)
def hseq(nmax):
    # h_n(x) = L^n 1 computed by forward branching: weights W over leaf points P
    P=xs[:,None].copy(); W=np.ones_like(P); H=[W.sum(1)]
    for n in range(nmax):
        P,W=np.concatenate([s1(P),s2(P)],1),np.concatenate([W*u1(P),W*u2(P)],1)
        H.append(W.sum(1))
    return np.array(H)
H=hseq(17)
R=H[1:]/H[:-1]
rhoX=0.1343549829703998131; qX=-0.244080070117426
norm=[]
for n in range(4,17):
    d=rhoX-R[n].min(); c=d/abs(qX)**n; g=d/(rhoX*(1-qX)*abs(qX)**n)
    norm.append((n,c,g,xs[R[n].argmin()]))
    print(n,"(rho-infR)/|q|^n=%.7f  /(rho(1-q)|q|^n)=%.7f argmin s=%.4f"%(c,g,xs[R[n].argmin()]))
chk("inf R_n <= rho <= sup R_n all n",all(R[n].min()<=rhoX+1e-15<=R[n].max()+2e-15 for n in range(17)))
for n,c,g,x in norm:
    if n>=10 and n<=15:
        lo,hi=(0.0217058,0.0451750) if n%2==0 else (0.0841585,0.0913152)
        chk(f"CT.5 bounds n={n}",lo<=c<=hi,c)
ev=[g for n,c,g,x in norm if n%2==0 and 10<=n<=14]; od=[g for n,c,g,x in norm if n%2 and 9<=n<=13]
chk("Gamma_+ ~0.2000641",abs(ev[-1]-0.20006416)<5e-6,ev[-1])
chk("Gamma_- ~0.5249040",abs(od[-1]-0.52490403)<5e-6,od[-1])
chk("argmin at sqrt5/2 (even) and 5/2 (odd)",all((abs(x-a)<1e-9) if n%2==0 else (abs(x-b)<1e-9) for n,c,g,x in norm if n>=8))
osc=[(R[n].max()-R[n].min())/(rhoX*(1-qX)*abs(qX)**n) for n in range(10,15)]
chk("oscillation constant -> 0.1211772/(rho(1-q)) i.e. Gamma_+ + Gamma_-",abs(osc[-1]*rhoX*(1-qX)-0.1211772)<1e-5,osc[-1]*rhoX*(1-qX))
print("ALL PASS" if all(ok) else "SOME FAIL", sum(ok),"/",len(ok))
