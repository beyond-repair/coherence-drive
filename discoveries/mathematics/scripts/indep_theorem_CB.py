# Independent check of IFI Theorem CB (0d9944c015fb); no repository code imported.
import sympy as sp, mpmath as mp
z=sp.symbols('z')
p=lambda w: w*(w+5); c=lambda w:(w+6)/((w+2)*(w+5)); e=lambda w:2*w/(2+w)
# CB.1 algebra: H=D-z/2 ; D_{n+1}=c D_n(p)-e  =>  H_{n+1}=c H_n(p)
H=sp.Function('H')
assert sp.simplify(c(z)*(sp.Symbol('Hp')+p(z)/2)-e(z)-z/2 - c(z)*sp.Symbol('Hp'))==0
assert sp.simplify(c(z)*p(z)/z-(z+6)/(z+2))==0
# closed form vs recursion for n<=4
D=3+z
def closed(n,s):
    pr=1
    for j in range(n): pr*= (p_n(j,s)+6)/(p_n(j,s)+2)
    return s/2*(1+(1+6/p_n(n,s))*pr)
def p_n(n,s):
    for _ in range(n): s=p(s)
    return s
Dn=3+z
for n in range(0,5):
    assert sp.simplify(sp.together(Dn-closed(n,z)))==0, n
    Dn=sp.together(c(z)*Dn.subs(z,p(z))-e(z))
print("CB.1 closed form == recursion, n=0..4 (symbolic): PASS")
mp.mp.dps=80
def Dinf_product(s,J=60):
    pr=mp.mpf(1); w=mp.mpc(s)
    for j in range(J):
        if abs(w)>1e30: break
        pr*=(w+6)/(w+2); w=w*(w+5)
    return s/2*(1+pr)
def Dinf_rec(s,K=40):
    # D_K(s) via finite recursion evaluated pointwise: D_n(s)=c(s)D_{n-1}(p(s))-e(s)
    pts=[mp.mpc(s)]
    for _ in range(K): pts.append(pts[-1]*(pts[-1]+5))
    # base D_0=3+z at deepest point, unroll is huge; use finite level n= K with D_0
    val=3+pts[K]
    for k in range(K-1,-1,-1):
        w=pts[k]; val=(w+6)/((w+2)*(w+5))*val-2*w/(2+w)
    return val
for s in [6,1,mp.mpf('0.3'),mp.mpc(2,1),-mp.mpf('5.5')]:
    a=Dinf_product(s); b=Dinf_rec(s,K=8)
    print(s, mp.nstr(a,25), mp.nstr(abs(a-b),3))
print("1/r_inf(6) =",mp.nstr(Dinf_product(6),20),"(repo 7.7687721988162724457)")
print("1/r_inf(1) =",mp.nstr(Dinf_product(1),20),"(repo 2.3545225217618837289)")
# CB.3/CB.4/CB.5: f=1/Q_inf by the finite-level route of indep_theorem_CA.py (no Pi/S, no product)
mp.mp.dps=110
def f_route(u,M=110,K=24):
    return (mp.mpf(5)/3)**M*Dinf_rec(mp.mpf(5)**(-M)*u,K=M+K)
def psi(v,N=230):
    w=mp.mpf(5)**(-N)*v
    for _ in range(N): w=w*(w+5)
    return w
lam1=mp.findroot(lambda l: psi(-l)+3, 3.6152567)
print("lam1 =",mp.nstr(lam1,20)," |f(-lam1)| =",mp.nstr(abs(f_route(-lam1)),3))
u2=mp.findroot(lambda u: psi(u)+2, -2.2421331852)
print("psi=-2 point u =",mp.nstr(u2,20)," f =",mp.nstr(f_route(u2),16),"(repo 2.1979467595912..13)")
u3=mp.findroot(lambda u: psi(u)-(-5+mp.sqrt(17))/2, -0.4484266370)
print("psi=(-5+sqrt17)/2 point u =",mp.nstr(u3,20)," f =",mp.nstr(f_route(u3),14),"(repo 1.31876805575...)")
d=mp.diff(lambda u: f_route(u), -lam1)
print("f'(-lam1) =",mp.nstr(d,25)," 1/f' =",mp.nstr(1/d,25),"(repo atom mass 0.4796406929290034734083466)")
