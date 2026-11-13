# Independent float check of IFI Theorem CV (00df4a6ea6d7). Different method from the repo (arb H^2(D) Galerkin M_180,
# Krawczyk, Neumann): Chebyshev collocation on the real interval X for the spectrum of L_k f = u1 f(s1) + u2 f(s2),
# u_i = w_i/(2 s_i)^k, and Chebyshev-interpolant power iteration for h_n, R_n. No repo code imported.
import numpy as np
a,b=np.sqrt(5)/2,2.5
s1=lambda s: np.sqrt(3.75-s); s2=lambda s: np.sqrt(3.75+s)
w1=lambda s:(s+.5)/(2*s*(3.5-s)); w2=lambda s:(s-.5)/(2*s*(s+3.5))
ok=[];chk=lambda name,c,info="":(ok.append(bool(c)),print(("PASS " if c else "FAIL ")+name,info))
C={5:(0.0014792559239634748,-0.0005161358132104635,0.416558,1.129942,8.31196e-4,2.254676e-3,1/5000),
 6:(0.0004853393939726874,-0.0001723958039714274,0.471227,1.283207,3.09943e-4,8.44010e-4,1/12500),
 7:(0.0001597483711719488,-0.0000572111535546882,0.526963,1.442049,1.143297e-4,3.12866e-4,1/35000),
 8:(0.0000527169494750854,-0.0000189167039184835,0.583993,1.607694,4.18335e-5,1.151650e-4,1/1e5),
 9:(0.0000174329038013139,-0.0000062429809833751,0.642394,1.78057,1.520924e-5,4.21566e-5,1/3e5),
 10:(0.0000057745266397710,-0.0000020588085310616,0.702119,1.96047,5.49994e-6,1.53570e-5,1/9e5),
 11:(0.0000019153320627478,-0.0000006789469804583,0.763030,2.14668,1.979512e-6,5.56909e-6,1/2.6e6),
 12:(0.0000006359658135257,-0.0000002240022214049,0.824925,2.33819,7.09409e-7,2.01077e-6,1/7.8e6)}
PRIOR_Q={1:0.2440800701,2:0.2895670639,3:0.3189949783,4:0.3376293000}
PRIOR_R={1:0.1343549829703998131,2:0.0430703112227101271,3:0.0139192547691468646,4:0.0045264690852562123}
def ops(N,k):
    x=np.cos(np.pi*(2*np.arange(N)+1)/(2*N)); s=(a+b)/2+(b-a)/2*x
    T=lambda y: np.cos(np.outer(np.arccos(np.clip(y,-1,1)),np.arange(N)))
    Vi=np.linalg.inv(T(x)); y=lambda t:(2*t-(a+b))/(b-a)
    L=np.diag(w1(s)/(2*s1(s))**k)@T(y(s1(s)))@Vi+np.diag(w2(s)/(2*s2(s))**k)@T(y(s2(s)))@Vi
    return L,Vi,T,y
def eigs(N,k): return np.array(sorted(np.linalg.eigvals(ops(N,k)[0]),key=lambda z:-abs(z)))
xs=np.linspace(a,b,2001)
aq={};t3={}
for k in range(1,17):
    e1,e2=eigs(60,k),eigs(80,k); rho,nu=e2[0].real,e2[1].real
    aq[k]=abs(nu/rho); t3[k]=3**k*rho
    if k in C:
        rC,nC,gp,gm,cp,cm,rin=C[k]; print(f"--- k={k}", e2[:3])
        chk(f"k={k} rho",abs(rho/rC-1)<1e-11,rho/rC-1); chk(f"k={k} nu_2",abs(nu/nC-1)<1e-10,nu/nC-1)
        chk(f"k={k} both real, nu_2<0",nu<0 and abs(e2[0].imag)+abs(e2[1].imag)<1e-18)
        chk(f"k={k} N=60 vs 80",abs(e1[0]/e2[0]-1)<1e-12 and abs(e1[1]/e2[1]-1)<1e-11)
        chk(f"k={k} |nu_3| < rho_in < |nu_2|",abs(e2[2])<rin<abs(nu),(abs(e2[2]),rin))
        L,Vi,T,y=ops(80,k); f=np.ones(80); q=nu/rho; G={}  # v2: own collocation rho,nu (v1 used claimed rho: N=80 discretization floor ~6e-14 rel at k=12 broke Gamma_- by 1.6e-4)
        Tx=T(y(xs))
        for n in range(0,23):
            g=L@f; R=(Tx@Vi@g)/(Tx@Vi@f)
            if n in (20,21): G[n]=(rho-R.min())/(rho*(1-q)*abs(q)**n)
            f=g/np.abs(g).max()
        chk(f"k={k} Gamma_+ (n=20)",abs(G[20]-gp)<1e-4,G[20]); chk(f"k={k} Gamma_- (n=21)",abs(G[21]-gm)<1e-4,G[21])
        chk(f"k={k} c_+-=rho(1-q)Gamma_+-",abs(rC*(1-q)*gp/cp-1)<2e-5 and abs(rC*(1-q)*gm/cm-1)<2e-5)
for k in range(1,5): chk(f"k={k} collocation matches prior |q|, rho",abs(aq[k]-PRIOR_Q[k])<1e-9 and abs(3**k*PRIOR_R[k]/t3[k]-1)<1e-12)
chk("CV.6 |q| up k=1..8, down k=8..12",all(aq[k+1]>aq[k] for k in range(1,8)) and all(aq[k+1]<aq[k] for k in range(8,12)),[round(aq[k],10) for k in range(1,13)])
chk("CV.6 gap |q8|-|q9| > 7e-4",aq[8]-aq[9]>7e-4,aq[8]-aq[9])
chk("CV.7 3^k rho decreasing k=1..12, > 1/3",all(t3[k+1]<t3[k] for k in range(1,12)) and min(t3[k] for k in range(1,13))>1/3,[round(t3[k],8) for k in range(1,13)])
print("observation k=13..16 (float, not claimed): |q|",[round(aq[k],8) for k in range(13,17)]," 3^k rho",[round(t3[k],8) for k in range(13,17)])
print("ALL PASS" if all(ok) else "SOME FAIL", sum(ok),"/",len(ok))
