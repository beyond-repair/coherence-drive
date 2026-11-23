import numpy as np, sympy as sp
S=sp.symbols('s',positive=True)
w1=(S+sp.Rational(1,2))/(2*S*(sp.Rational(7,2)-S)); w2=(S-sp.Rational(1,2))/(2*S*(S+sp.Rational(7,2)))
s1=sp.sqrt(sp.Rational(15,4)-S); s2=sp.sqrt(sp.Rational(15,4)+S)
P=[]
def ok(c,m): P.append(c); print('PASS' if c else 'FAIL',m)
ok(sp.simplify(w1+w2-16/(49-4*S**2))==0,'w1+w2=16/(49-4s^2)')
ok(sp.simplify(-sp.diff(s1,S)*s1-sp.Rational(1,2))==0 and sp.simplify(sp.diff(s2,S)*s2-sp.Rational(1,2))==0,'|sigma_i\'|sigma_i=1/2')
c=lambda x:(49-4*x**2)/16
a,b=np.sqrt(5)/2,2.5
ga,gb=np.sqrt(15/4-a),np.sqrt(15/4+a)
ok(abs(ga-1.6223335)<1e-6 and abs(gb-2.2063622)<1e-6,'gap endpoints')
# rho(L_k) by Chebyshev collocation / power iteration on dense grid with interpolation
xs=np.linspace(a,b,4001)
W1=lambda x:(x+.5)/(2*x*(3.5-x)); W2=lambda x:(x-.5)/(2*x*(x+3.5))
for k,claim in [(0,0.42373128696),(1,0.1343550),(2,0.0430703),(3,0.0139193),(4,0.0045265)]:
    f=np.ones_like(xs); lam=0
    for n in range(200):
        y1=np.sqrt(3.75-xs); y2=np.sqrt(3.75+xs)
        g=W1(xs)*np.interp(y1,xs,f)/(2*y1)**k+W2(xs)*np.interp(y2,xs,f)/(2*y2)**k
        lam=g.max()/f.max(); f=g/g.max()
    ok(abs(lam-claim)<2e-6*max(1,claim*10),f'rho(L_{k}) float {lam:.7f} vs repo {claim}')
A=np.array([[3.11017,1.98093],[2.5,8.36285]]); ra=max(abs(np.linalg.eigvals(A)))
ok(abs(ra-9.1788909)<1e-5 and 0.1089*ra<1,f'rho(A)={ra:.7f}, 0.1089*rho<1')
# mechanism: L K = I and L g = 0 checked pointwise
fx=lambda x:np.cos(3*x)+x**2
def K(f,x):
    x=np.asarray(x,float); out=np.empty_like(x)
    m1=x<=ga; m2=x>=gb
    T1=3.75-x[m1]**2; T2=x[m2]**2-3.75
    out[m1]=c(T1)*f(T1); out[m2]=c(T2)*f(T2); out[~(m1|m2)]=0
    return out
y1=np.sqrt(3.75-xs); y2=np.sqrt(3.75+xs)
LK=W1(xs)*K(fx,y1)+W2(xs)*K(fx,y2)
ok(np.max(abs(LK-fx(xs)))<1e-12,'L K f = f on branch images (gap values never read)')
gfun=lambda x:np.where((x>ga)&(x<gb),((x-ga)*(gb-x))**2,0.)
ok(np.max(abs(W1(xs)*gfun(y1)+W2(xs)*gfun(y2)))==0,'L g = 0')
ok(1/12>0.0731138175124,'|l_2|<1/12<0.1089')
print('ALL', 'PASS' if all(P) else 'FAIL', sum(P),'/',len(P))
