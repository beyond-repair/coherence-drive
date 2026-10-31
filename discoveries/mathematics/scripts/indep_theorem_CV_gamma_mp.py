# High-precision follow-up: Gamma_- for k=11,12 from Chebyshev-interpolant iteration in mpmath (60 digits), n up to 51.
import mpmath as mp, sys
mp.mp.dps=60
a,b=mp.sqrt(5)/2,mp.mpf(5)/2
s1=lambda s: mp.sqrt(mp.mpf(15)/4-s); s2=lambda s: mp.sqrt(mp.mpf(15)/4+s)
w1=lambda s:(s+mp.mpf(1)/2)/(2*s*(mp.mpf(7)/2-s)); w2=lambda s:(s-mp.mpf(1)/2)/(2*s*(s+mp.mpf(7)/2))
N=70
x=[mp.cos(mp.pi*(2*j+1)/(2*N)) for j in range(N)]; S=[(a+b)/2+(b-a)/2*t for t in x]
y=lambda t:(2*t-(a+b))/(b-a)
T=lambda ys: mp.matrix([[mp.cos(m*mp.acos(yy)) for m in range(N)] for yy in ys])
Vi=T(x)**-1
C={11:(mp.mpf('0.0000019153320627478'),mp.mpf('-0.0000006789469804583'),0.763030,2.14668),
   12:(mp.mpf('0.0000006359658135257'),mp.mpf('-0.0000002240022214049'),0.824925,2.33819)}
pts=[a+(b-a)*i/400 for i in range(401)]
Tp=T([y(p) for p in pts])*Vi
for k in map(int,sys.argv[1:]):
    U1=mp.diag([w1(s)/(2*s1(s))**k for s in S]); U2=mp.diag([w2(s)/(2*s2(s))**k for s in S])
    L=U1*T([y(s1(s)) for s in S])*Vi+U2*T([y(s2(s)) for s in S])*Vi
    rho,nu,gp,gm=C[k]; q=nu/rho; f=mp.matrix([1]*N)
    for n in range(0,52):
        g=L*f
        if n>=19 and n%2==1 or n in (20,30,40,50):
            hf=Tp*f; hg=Tp*g; Rm=min(hg[i]/hf[i] for i in range(len(pts)))
            G=(rho-Rm)/(rho*(1-q)*abs(q)**n); print(k,n,mp.nstr(G,9),"claim",gm if n%2 else gp,flush=True)
        f=g/max(abs(v) for v in g)
