# Independent check of IFI Theorem CZ (3e743609c293). No repo code imported.
# Reuses my own frame collocation (ifi-cy-indep/indep_cy2.py, v2) for q^(k); b1,g1,kappa by mpmath, own definitions.
import numpy as np, mpmath as m
m.mp.dps=90
exec(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'indep_theorem_CY.py')).read().split("s=np.linspace")[0])  # defs only (base, frame_eigs, Bf, Gf...)
ok2=[];chk2=lambda n,c,i="":(ok2.append(bool(c)),print(("PASS " if c else "FAIL ")+n,i))
# mp versions
S1=lambda s: m.sqrt(m.mpf(15)/4-s); S2=lambda s: m.sqrt(m.mpf(15)/4+s)
W1=lambda s:(s+m.mpf(1)/2)/(2*s*(m.mpf(7)/2-s)); W2=lambda s:(s-m.mpf(1)/2)/(2*s*(s+m.mpf(7)/2))
def PP(s,f,J=140):
    p=m.mpf(1);x=s
    for _ in range(J): p*=f(x); x=S1(x)
    return p
P0m=lambda s:PP(s,lambda x:3*W1(x)); P1m=lambda s:PP(s,lambda x:3/(2*S1(x)))
Bm=lambda s:3/(2*S2(s))*P1m(S2(s))/P1m(s); Gm=lambda s:3*W2(s)*P0m(S2(s))/P0m(s)
ss=m.mpf(3)/2; t=S2(ss)
chk2("t=sqrt(21)/2",abs(t-m.sqrt(21)/2)<1e-35)
Bs,Gs=Bm(ss),Gm(ss); b1=m.diff(Bm,ss)/Bs; g1=m.diff(Gm,ss)/Gs
def kap(s,n=75):
    x=s
    for _ in range(n): x=S1(x)
    return (-3)**n*(x-ss)
kt=kap(t); kpt=m.diff(kap,t)
chk2("kappa'(s*)=1",abs(m.diff(kap,ss)-1)<1e-20)
for nm,v,r in (("B*",Bs,0.777376027633332),("G*",Gs,0.287065241760389),("b1",b1,-0.199881602332293),("g1",g1,0.0376598834730586),("kappa(t)",kt,0.856781269828647),("kappa'(t)",kpt,1.18746149669128)):
    chk2(f"CZ.1 {nm}={m.nstr(v,16)}",abs(v-r)<5e-14)
al=Gs*b1*kt; ga=Gs*(g1*kt+kpt/(2*t)+m.mpf(1)/3)
chk2(f"CZ.1 alpha*={m.nstr(al,16)}",abs(al+0.0491613043141717)<5e-15)
chk2(f"CZ.1 gamma*={m.nstr(ga,16)}",abs(ga-0.179336821291891)<5e-15)
al,ga,Bf_=float(al),float(ga),float(Bs)
q={};lam0={}
for k in range(20,101):
    e=frame_eigs(90,k); q[k]=(e[1]/e[0]).real; lam0[k]=e[0].real
Err={24:0.4151,30:0.1316,40:0.02475,50:0.005054,60:0.001086}
for k,E in Err.items():
    d=(q[k]+1/3)/Bf_**k-(al*k+ga)
    chk2(f"CZ.3 k={k} |(q+1/3)/B*^k-(a*k+g*)|={abs(d):.3e} <= Err={E}",abs(d)<=E, f"resid/Err={abs(d)/E:.3f}")
for k,(c,rr) in {30:(-6.7822e-4,6.9e-5),40:(-7.5405e-5,1.1e-6),60:(-7.5928e-7,3.0e-10)}.items():
    chk2(f"CZ.3 example k={k}: q+1/3={q[k]+1/3:.5e} in {c}±{rr}",abs(q[k]+1/3-c)<=rr)
for k,w0 in {24:0.1058,30:0.03606,40:0.006823,50:0.001357,60:0.0002737}.items():
    ck=(lam0[k]-1)/(float(Gs)*Bf_**k); chk2(f"CZ.2 k={k} |c_k-1|={abs(ck-1):.2e} <= {w0}",abs(ck-1)<=w0)
chk2("CZ.4 float: q<-1/3 for k=24..100",all(q[k]<-1/3 for k in range(24,101)))
chk2("CZ.5 float: |q| strictly decreasing k=23..100 (to rounding)",all(abs(q[k+1])<abs(q[k]) for k in range(23,70)))
for k,v in zip(range(24,30),(-0.3357008,-0.3352657,-0.3349069,-0.3346119,-0.3343701,-0.3341726)):
    chk2(f"CZ.6 q^({k})={q[k]:.8f} vs {v}",abs(q[k]-v)<=9e-8+1e-10)
r=[(q[k]+1/3)/(k*Bf_**k) for k in (60,80,100)]
print("float (q+1/3)/(k B*^k) at k=60,80,100:",r," alpha*=",al)
print("float sign change of alpha* k+gamma* at",ga/-al)
print("ALL PASS" if all(ok2) else "SOME FAIL",sum(ok2),"/",len(ok2))
