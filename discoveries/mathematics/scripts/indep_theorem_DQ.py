import numpy as np, math, sympy as sp
x=sp.symbols('x'); w=sp.Function('w'); s=sp.Function('s'); f=sp.Function('f')
L=w(x)*f(s(x)); d2=sp.diff(L,x,2)
rhs=w(x)*sp.diff(s(x),x)**2*sp.Subs(sp.diff(f(x),x,2),x,s(x)).doit() + sp.diff(w(x),x,2)*f(s(x)) \
    + (2*sp.diff(w(x),x)*sp.diff(s(x),x)+w(x)*sp.diff(s(x),x,2))*sp.Subs(sp.diff(f(x),x),x,s(x)).doit()
print("DQ.1 chain-rule identity", sp.simplify(d2.doit()-rhs)==0)
# sigma = sqrt-type branch: sigma'^2 = 1/(4 sigma^2) holds for sigma=sqrt(x+c)
c=sp.symbols('c'); sg=sp.sqrt(x+c); print("sigma'^2=1/(4 sigma^2)", sp.simplify(sp.diff(sg,x)**2-1/(4*sg**2))==0)
# DQ.3 finite analog: positive matrix, tau(A^n)^(1/n) -> |l2|/rho (Birkhoff rate = spectral ratio)
rng=np.random.default_rng(1); worst=0
for _ in range(50):
    A=rng.uniform(0.05,1,(5,5)); ev=sorted(abs(np.linalg.eigvals(A)))[::-1]; ratio=ev[1]/ev[0]
    B=np.linalg.matrix_power(A/ev[0],12); cols=B.T
    D=max(math.log(max(c1/c2)/min(c1/c2)) for c1 in cols for c2 in cols)
    worst=max(worst,abs(math.tanh(D/4)**(1/12)/ratio-1) if ratio>0.05 else 0)
print("finite analog rel. gap at n=12 (should be small, ->0)", round(worst,3))
print("cap/limit", 0.3170757/0.172547602, "> 1.83761")
print("implied r from L1:", 0.1343549/0.317076185, 0.1343551/0.317075713, " from l2:", 0.0731138175124/0.172547602)
for n,t in [(1,0.5523034),(2,0.1538736),(3,0.03342037)]: print("DQ.5 n",n,"per level",t**(1/n),"> cap",t**(1/n)>0.3170762)
print("rho(L2) < |l2| < rho(L1):", 0.0430704<0.0731138175124<0.1343549)
# convergence of the finite analog in n (median over 50 matrices)
for n in (4,6,9,12,15):
    gaps=[]
    rng=np.random.default_rng(1)
    for _ in range(50):
        A=rng.uniform(0.05,1,(5,5)); ev=np.linalg.eigvals(A); ev=ev[np.argsort(-abs(ev))]; ratio=abs(ev[1])/abs(ev[0])
        if ratio<0.05 or ratio**n<1e-9: continue
        B=np.linalg.matrix_power(A/abs(ev[0]),n); cols=B.T
        D=max(math.log(max(c1/c2)/min(c1/c2)) for c1 in cols for c2 in cols)
        gaps.append(abs(math.tanh(D/4)**(1/n)/ratio-1))
    if gaps: print("n",n,"median gap",round(float(np.median(gaps)),4),"max",round(max(gaps),4))

# --- float spectrum of Lt and M_1 by Chebyshev collocation (operator from GASKET.md CE/CF setting) ---
from numpy.polynomial import chebyshev as C
a,b=np.sqrt(5)/2,2.5
w1=lambda s:(s+.5)/(2*s*(3.5-s)); w2=lambda s:(s-.5)/(2*s*(s+3.5))
s1=lambda s:np.sqrt(3.75-s); s2=lambda s:np.sqrt(3.75+s)
t=lambda s:(2*s-(a+b))/(b-a)
for N in (30,50,80):
    k=np.arange(N); xs=np.cos(np.pi*(k+.5)/N); ss=(xs*(b-a)+a+b)/2
    V=C.chebvander(xs,N-1)
    M=w1(ss)[:,None]*C.chebvander(t(s1(ss)),N-1)+w2(ss)[:,None]*C.chebvander(t(s2(ss)),N-1)
    ev=np.linalg.eigvals(np.linalg.solve(V,M)); ev=ev[np.argsort(-abs(ev))]
    print(N, np.round(ev[:6],7))
    # M_1 with sign: sigma_1' = -1/(2 sqrt), sigma_2' = +1/(2 sqrt)
    d1=-1/(2*s1(ss)); d2=1/(2*s2(ss))
    M1=(w1(ss)*d1)[:,None]*C.chebvander(t(s1(ss)),N-1)+(w2(ss)*d2)[:,None]*C.chebvander(t(s2(ss)),N-1)
    e1=np.linalg.eigvals(np.linalg.solve(V,M1)); e1=e1[np.argsort(-abs(e1))]
    print("   M_1", np.round(e1[:4],6))
