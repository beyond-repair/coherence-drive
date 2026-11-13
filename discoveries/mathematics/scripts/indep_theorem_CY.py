# v2: v1's direct collocation of 3^(k+1)L_k loses conditioning for k>~30 (Kept Failure of v1, see indep_cy.log).
# Here: collocate CY's frame operator C1 + diag(G B^k) C2 with G,B computed from my own orbit products on X,
# cross-checked against direct collocation for k<=25. No repo code imported.
import numpy as np
from mpmath import mp, mpf, sqrt as msqrt, matrix, eig
a,b=np.sqrt(5)/2,2.5
s1=lambda s: np.sqrt(3.75-s); s2=lambda s: np.sqrt(3.75+s)
w1=lambda s:(s+.5)/(2*s*(3.5-s)); w2=lambda s:(s-.5)/(2*s*(s+3.5))
ok=[];chk=lambda n,c,i="":(ok.append(bool(c)),print(("PASS " if c else "FAIL ")+n,i))
def P(s,f,J=80):
    p=np.ones_like(s); x=s.copy()
    for _ in range(J): p=p*f(x); x=s1(x)
    return p
P0=lambda s:P(s,lambda x:3*w1(x)); P1=lambda s:P(s,lambda x:3/(2*s1(x)))
Bf=lambda s:3/(2*s2(s))*P1(s2(s))/P1(s); Gf=lambda s:3*w2(s)*P0(s2(s))/P0(s)
def base(N):
    x=np.cos(np.pi*(2*np.arange(N)+1)/(2*N)); s=(a+b)/2+(b-a)/2*x
    T=lambda y: np.cos(np.outer(np.arccos(np.clip(y,-1,1)),np.arange(N)))
    Vi=np.linalg.inv(T(x)); y=lambda t:(2*t-(a+b))/(b-a)
    return s,T(y(s1(s)))@Vi,T(y(s2(s)))@Vi
def frame_eigs(N,k):
    s,C1,C2=base(N); M=C1+np.diag(Gf(s)*Bf(s)**k)@C2
    return np.array(sorted(np.linalg.eigvals(M),key=lambda z:-abs(z)))
def direct_eigs(N,k):
    s,C1,C2=base(N); sc=3.0**(k+1)
    M=np.diag(sc*w1(s)/(2*s1(s))**k)@C1+np.diag(sc*w2(s)/(2*s2(s))**k)@C2
    return np.array(sorted(np.linalg.eigvals(M),key=lambda z:-abs(z)))
s=np.linspace(a,b,7)
chk("frame identity 3^(k+1)u1 h(s1)/h=1 (k=5)",np.allclose(3**6*w1(s)/(2*s1(s))**5*P0(s1(s))*P1(s1(s))**5/(P0(s)*P1(s)**5),1,atol=1e-12))
chk("B*=B(3/2)",abs(Bf(np.array([1.5]))[0]-0.77737602763333190375)<1e-13); chk("G*=G(3/2)",abs(Gf(np.array([1.5]))[0]-0.28706524176038901924)<1e-13)
CY5=[0.34994211,0.34774936,0.34571357,0.34387052,0.34223383,0.34080237,0.33956578,0.33850837,0.33761188,0.33685728,0.33622604]
q={}
for k in range(0,81):
    e=frame_eigs(70,k); e2=frame_eigs(90,k); q[k]=(e2[1]/e2[0]).real
    chk(f"k={k} frame N70/N90 stable, top two real",abs(e[1]/e[0]-e2[1]/e2[0])<1e-11 and abs(e2[0].imag)+abs(e2[1].imag)<1e-12)
    if k<=25: d=direct_eigs(90,k); chk(f"k={k} frame == direct collocation",abs(d[1]/d[0]-e2[1]/e2[0])<1e-9)
    if k>=24:
        bd=4.8271*0.8529**k+0.2873/3*0.8352**k
        chk(f"CY.3 k={k} |q+1/3|={abs(q[k]+1/3):.3e} <= {bd:.3e}; |lam3|={abs(e2[2]):.4f}<9/40",abs(q[k]+1/3)<=bd and abs(e2[2])<9/40 and abs(e2[0]-1)<0.5 and abs(e2[1]+1/3)<4.8271*0.8529**k)
for i,k in enumerate(range(13,24)): chk(f"CY.5 |q^({k})|",abs(abs(q[k])-CY5[i])<2e-8,(abs(q[k]),CY5[i]))
chk("CY.6 |q| strictly decreasing k=8..23 and >1/3",all(abs(q[k+1])<abs(q[k]) for k in range(8,23)) and all(abs(q[k])>1/3 for k in range(8,24)))
for k,v in ((23,-2.893e-3),(30,-6.783e-4),(40,-7.542e-5)): chk(f"Observation q+1/3 at k={k} ({q[k]+1/3:.4e} vs {v})",abs((q[k]+1/3)/v-1)<1e-3)
print("float: q+1/3<0 for all k=8..80:",all(q[k]+1/3<0 for k in range(8,81)))
print("float: ratios (q+1/3) at k=40,60,79:",[(q[k+1]+1/3)/(q[k]+1/3) for k in (40,60,79)]," B*(1+1/k):",[0.777376*(1+1/k) for k in (40,60,79)])
print("ALL PASS" if all(ok) else "SOME FAIL",sum(ok),"/",len(ok))
