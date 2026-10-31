# Independent float check of IFI Theorem CU (8ea4fbef2a4c). Different method from the repo (which uses an H^2(D)
# Taylor/Galerkin matrix M_120 in arb): Chebyshev collocation on the real interval X for the spectrum of
# L_k f = u1 f(s1) + u2 f(s2), u_i = w_i/(2 s_i)^k, and exact path-sum iteration of L_k pointwise for h_n, R_n.
# No repo code imported.
import numpy as np
a,b=np.sqrt(5)/2,2.5
s1=lambda s: np.sqrt(3.75-s); s2=lambda s: np.sqrt(3.75+s)
w1=lambda s:(s+.5)/(2*s*(3.5-s)); w2=lambda s:(s-.5)/(2*s*(s+3.5))
ok=[];chk=lambda name,c,info="":(ok.append(bool(c)),print(("PASS " if c else "FAIL ")+name,info))
CLAIM={ # k: rho, nu2, |q|, Gp, Gm, c+, c-, n0, CL.3 interval, even interval(n>=), odd interval(n>=), osc const, rho_in
 2:(0.0430703112227101271,-0.0124717435618530418,0.2895670639,0.2546354,0.6796090,0.01414298,0.03774688,7,(0.0430702,0.0430704),(0.0120710,0.0162149,8),(0.0248320,0.0506618,7),0.0518899,1/500),
 3:(0.0139192547691468646,-0.0044401723728826436,0.3189949783,0.3087743,0.8310494,0.00566892,0.01525759,9,(0.0139192,0.0139193),(0.00459104,0.00674680,10),(0.0104718,0.0200434,9),0.02092651,1/1000),
 4:(0.0045264690852562123,-0.0015282685887826225,0.3376293000,0.3625752,0.9801676,0.002195297,0.00593466,12,(0.0045264,0.0045265),(0.00117440,0.00321619,12),(0.00566745,0.00620186,13),0.00812996,1/2500)}
def colloc(N,k):
    x=np.cos(np.pi*(2*np.arange(N)+1)/(2*N)); s=(a+b)/2+(b-a)/2*x
    T=lambda y: np.cos(np.outer(np.arccos(np.clip(y,-1,1)),np.arange(N)))
    Vi=np.linalg.inv(T(x)); y1=(2*s1(s)-(a+b))/(b-a); y2=(2*s2(s)-(a+b))/(b-a)
    L=np.diag(w1(s)/(2*s1(s))**k)@T(y1)@Vi+np.diag(w2(s)/(2*s2(s))**k)@T(y2)@Vi
    return np.array(sorted(np.linalg.eigvals(L),key=lambda z:-abs(z)))
xs=np.linspace(a,b,401)
def hseq(nmax,k):
    P=xs[:,None].copy(); W=np.ones_like(P); H=[W.sum(1)]
    for n in range(nmax):
        P,W=np.concatenate([s1(P),s2(P)],1),np.concatenate([W*w1(P)/(2*s1(P))**k,W*w2(P)/(2*s2(P))**k],1)
        H.append(W.sum(1))
    return np.array(H)
qs={}
for k,(rC,nC,qC,gp,gm,cp,cm,n0,cl3,ev,od,osc,rin) in CLAIM.items():
    print(f"--- k={k}")
    e40,e60=colloc(40,k),colloc(60,k); rho,nu=e60[0].real,e60[1].real
    print("colloc eigs",e60[:4])
    chk(f"k={k} rho collocation",abs(rho-rC)<1e-13*max(1,1),rho-rC)
    chk(f"k={k} nu_2 collocation",abs(nu-nC)<1e-13,nu-nC)
    chk(f"k={k} nu_2<0, both real",nu<0 and abs(e60[0].imag)+abs(e60[1].imag)<1e-15)
    chk(f"k={k} third |eig| < rho_in",abs(e60[2])<rin,abs(e60[2]))
    chk(f"k={k} N=40 vs 60 agree",abs(e40[0]-e60[0])<1e-15 and abs(e40[1]-e60[1])<1e-15)
    q=nu/rho; qs[k]=abs(q); chk(f"k={k} |q|",abs(abs(q)-qC)<1e-10,abs(q))
    chk(f"k={k} rho in CL.3 interval",cl3[0]<=rC<=cl3[1])
    H=hseq(17,k); R=H[1:]/H[:-1]; qX=nC/rC
    chk(f"k={k} inf R_n<=rho<=sup R_n, n<=16",all(R[n].min()<=rC*(1+1e-13) and rC<=R[n].max()*(1+1e-13) for n in range(17)))
    bad=[]
    for n in range(n0,17):
        d=rC-R[n].min(); c=d/abs(qX)**n; lo,hi,nn=ev if n%2==0 else od
        if n>=nn and not(lo<=c<=hi): bad.append((n,c))
        print(n,"(rho-infR)/|q|^n=%.8f  G=%.7f argmin s=%.4f"%(c,c/(rC*(1-qX)),xs[R[n].argmin()]))
    chk(f"k={k} CU.5 bounds n0..16 (both parities)",not bad,bad)
    ne=16; no=15
    Ge=(rC-R[ne].min())/(rC*(1-qX)*abs(qX)**ne); Go=(rC-R[no].min())/(rC*(1-qX)*abs(qX)**no)
    chk(f"k={k} Gamma_+ (n=16)",abs(Ge-gp)<2e-5,Ge); chk(f"k={k} Gamma_- (n=15)",abs(Go-gm)<2e-5,Go)
    chk(f"k={k} c_+=rho(1-q)Gamma_+",abs(rC*(1-qX)*gp-cp)<1e-8,rC*(1-qX)*gp)
    chk(f"k={k} c_-=rho(1-q)Gamma_-",abs(rC*(1-qX)*gm-cm)<1e-8,rC*(1-qX)*gm)
    chk(f"k={k} c_+ in even interval and c_- in odd interval",ev[0]<=cp<=ev[1] and od[0]<=cm<=od[1])
    chk(f"k={k} argmin at sqrt5/2 (even) / 5/2 (odd) for n>=8",all((abs(xs[R[n].argmin()]-a)<1e-9) if n%2==0 else (abs(xs[R[n].argmin()]-b)<1e-9) for n in range(8,17)))
    O=(R[16].max()-R[16].min())/abs(qX)**16
    chk(f"k={k} oscillation constant",abs(O-osc)<1e-6,O)
    chk(f"k={k} bases <1 (|q|, rho_in/rho, rho_in/|nu|)",qC<1 and rin/rC<1 and rin/abs(nC)<1,(rin/rC,rin/abs(nC)))
# k=1 pattern (CT): |q|=0.2440800701; monotone in k as the Observation states
chk("|q| increasing k=1..4 (k=1 from CT)",0.2440800701<qs[2]<qs[3]<qs[4],qs)
print("ALL PASS" if all(ok) else "SOME FAIL", sum(ok),"/",len(ok))
