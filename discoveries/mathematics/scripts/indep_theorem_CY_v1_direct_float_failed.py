# Independent float check of IFI Theorem CY (54ed04084f2e). Chebyshev collocation on X=[sqrt5/2,5/2] of the
# rescaled operator 3^(k+1) L_k (no repo code imported), plus direct checks of CY's product construction.
import numpy as np, cmath
a,b=np.sqrt(5)/2,2.5
s1=lambda s: np.sqrt(3.75-s); s2=lambda s: np.sqrt(3.75+s)
w1=lambda s:(s+.5)/(2*s*(3.5-s)); w2=lambda s:(s-.5)/(2*s*(s+3.5))
ok=[];chk=lambda n,c,i="":(ok.append(bool(c)),print(("PASS " if c else "FAIL ")+n,i))
def eigs(N,k):
    x=np.cos(np.pi*(2*np.arange(N)+1)/(2*N)); s=(a+b)/2+(b-a)/2*x
    T=lambda y: np.cos(np.outer(np.arccos(np.clip(y,-1,1)),np.arange(N)))
    Vi=np.linalg.inv(T(x)); y=lambda t:(2*t-(a+b))/(b-a)
    sc=3.0**(k+1)
    L=np.diag(sc*w1(s)/(2*s1(s))**k)@T(y(s1(s)))@Vi+np.diag(sc*w2(s)/(2*s2(s))**k)@T(y(s2(s)))@Vi
    return np.array(sorted(np.linalg.eigvals(L),key=lambda z:-abs(z)))
CY5=[0.34994211,0.34774936,0.34571357,0.34387052,0.34223383,0.34080237,0.33956578,0.33850837,0.33761188,0.33685728,0.33622604]
q={};lam={}
for k in range(8,61):
    e=eigs(70,k); e2=eigs(90,k)
    lam[k]=e2; q[k]=(e2[1]/e2[0]).real
    if k<=40: chk(f"k={k} N70 vs N90 stable",abs(e[1]/e[0]-e2[1]/e2[0])<1e-9 and abs(e2[0].imag)+abs(e2[1].imag)<1e-10)
for i,k in enumerate(range(13,24)): chk(f"CY.5 |q^({k})|",abs(abs(q[k])-CY5[i])<2e-8,(abs(q[k]),CY5[i]))
chk("CY.5 rho(L_13)",abs(lam[13][0].real/3**14/2.113436488714e-7-1)<1e-9)
chk("CY.5 nu2(L_23)",abs(lam[23][1].real/3**24/-1.1915215e-12-1)<1e-6)
chk("CY.6 |q| decreasing k=8..23, >1/3",all(abs(q[k+1])<abs(q[k]) for k in range(8,23)) and all(abs(q[k])>1/3 for k in range(8,24)))
for k in range(24,61):
    bd=4.8271*0.8529**k+0.2873/3*0.8352**k
    chk(f"CY.3 k={k} |q+1/3|={q[k]+1/3:.3e} <= {bd:.3e}",abs(q[k]+1/3)<=bd)
    chk(f"CY.3 k={k} third eig |nu|<9/40 (scaled)",abs(lam[k][2])<9/40,abs(lam[k][2]))
for k,v in ((23,-2.893e-3),(30,-6.783e-4),(40,-7.542e-5)): chk(f"Observation q+1/3 at k={k}",abs((q[k]+1/3)/v-1)<2e-3,q[k]+1/3)
print("float observation sign of q+1/3 for k=24..60 all negative:",all(q[k]+1/3<0 for k in range(24,61)))
print("ratios (q+1/3)_{k+1}/(q+1/3)_k at k=40,50:",(q[41]+1/3)/(q[40]+1/3),(q[51]+1/3)/(q[50]+1/3))
# product construction on complex points of D=|s-9/5|<4/5
def orbit(s,J=80):
    xs=[s]
    for _ in range(J): xs.append(cmath.sqrt(3.75-xs[-1]))
    return xs
def kap(s):
    p=s-1.5
    for x in orbit(s)[:-1]: p*=3/(cmath.sqrt(3.75-x)+1.5)
    return p
pts=[1.8+0.79*cmath.exp(1j*t) for t in np.linspace(0,2*np.pi,7)[:-1]]+[1.5,2.0+0.3j]
chk("kappa o sigma1 = -kappa/3 on D",max(abs(kap(cmath.sqrt(3.75-s))+kap(s)/3) for s in pts)<1e-12)
h=1e-6; chk("kappa'(3/2)=1",abs((kap(1.5+h)-kap(1.5-h))/(2*h)-1)<1e-8)
def P1(s): 
    p=1
    for x in orbit(s)[:-1]: p*=3/(2*cmath.sqrt(3.75-x))
    return p
def Bf(s): return 3/(2*cmath.sqrt(3.75+s))*P1(cmath.sqrt(3.75+s))/P1(s)
chk("B(3/2)=B*",abs(Bf(1.5)-0.77737602763333190375)<1e-12,Bf(1.5))
sb=max(abs(Bf(1.8+0.8*cmath.exp(1j*t))) for t in np.linspace(0,2*np.pi,2000))
chk("sup_dD |B| ~0.85279 (<0.8529)",sb<0.8529 and sb>0.85,sb)
print("ALL PASS" if all(ok) else "SOME FAIL",sum(ok),"/",len(ok))
