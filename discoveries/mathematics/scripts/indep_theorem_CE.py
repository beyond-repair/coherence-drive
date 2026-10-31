# Independent check of IFI Theorem CE (a056d01a): weights, identities, Kept Failure CE.6, spectral radius r.
import mpmath as mp, sympy as sp
mp.mp.dps=50
t,y,s=sp.symbols('t y s',real=True)
p=lambda z: z*(z+5)
w=lambda z:(z+2)*(z+5)/((z+6)*(2*z+5))
ok=True
# twisted weights from w(phi)q(phi)/q(t)
for phi,claim in [(-sp.Rational(5,2)-s,(s+sp.Rational(1,2))/(2*s*(sp.Rational(7,2)-s))),(-sp.Rational(5,2)+s,(s-sp.Rational(1,2))/(2*s*(s+sp.Rational(7,2))))]:
    tt=s**2-sp.Rational(25,4)
    assert sp.simplify(p(phi)-tt)==0
    d=sp.simplify(w(phi)*(-phi)/(-tt)-claim); print('tilde_w diff',d); ok&=(d==0)
tw1=lambda S:(S+0.5)/(2*S*(3.5-S)); tw2=lambda S:(S-0.5)/(2*S*(S+3.5))
S=sp.symbols('S'); ssum=sp.simplify((S+sp.Rational(1,2))/(2*S*(sp.Rational(7,2)-S))+(S-sp.Rational(1,2))/(2*S*(S+sp.Rational(7,2)))-4/(6-(S**2-sp.Rational(25,4))))
print('sum identity',ssum); ok&=(ssum==0)
print('tw(0)',tw1(mp.mpf(5)/2),tw2(mp.mpf(5)/2)); ok&= abs(tw1(mp.mpf(5)/2)-mp.mpf(3)/5)<1e-40 and abs(tw2(mp.mpf(5)/2)-mp.mpf(1)/15)<1e-40
print('w(0),w(-5)',w(sp.Integer(0)),w(sp.Integer(-5))); ok&= w(sp.Integer(0))==sp.Rational(1,3) and w(sp.Integer(-5))==0
# spectral radius by Chebyshev collocation (own implementation, N nodes)
def radius(N):
    nodes=[ -2.5+2.5*mp.cos(mp.pi*(2*j+1)/(2*N)) for j in range(N)]
    def basis(x):  # Lagrange via Chebyshev barycentric
        xs=[(x+mp.mpf(2.5))/mp.mpf(2.5)]
        return xs[0]
    xn=[(n+mp.mpf(2.5))/mp.mpf(2.5) for n in nodes]
    wts=[(-1)**j*mp.sin(mp.pi*(2*j+1)/(2*N)) for j in range(N)]
    def lag(x):
        X=(x+mp.mpf(2.5))/mp.mpf(2.5)
        for j in range(N):
            if abs(X-xn[j])<mp.mpf(10)**-45: return [1 if k==j else 0 for k in range(N)]
        c=[wts[j]/(X-xn[j]) for j in range(N)]; sc=sum(c); return [ci/sc for ci in c]
    A=mp.matrix(N,N)
    for i,x in enumerate(nodes):
        S_=mp.sqrt(x+mp.mpf(25)/4)
        for phi,wt in [(-mp.mpf(5)/2-S_,tw1(S_)),(-mp.mpf(5)/2+S_,tw2(S_))]:
            l=lag(phi)
            for j in range(N): A[i,j]+=wt*l[j]
    ev=mp.eig(A,left=False,right=False)
    ev=sorted(ev,key=lambda e:-abs(e))
    return ev[0],ev[1]
for N in (40,60):
    r,l2=radius(N); print(N,'r=',mp.nstr(mp.re(r),40),'lambda2=',mp.nstr(l2,15))
claim=mp.mpf('0.42373128696260793985253216132843923')
print('|r-claim|',abs(mp.re(r)-claim)); ok&= abs(mp.re(r)-claim)<1e-30
print('PASS' if ok else 'FAIL')
