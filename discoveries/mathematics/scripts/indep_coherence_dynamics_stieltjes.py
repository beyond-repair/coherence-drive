import mpmath as mp
mp.mp.dps=40
def S(rho,k): return mp.quad(lambda s: rho(s)/(k**2+s),[0,1,10,100,mp.inf])
def I(rho,k): return k*mp.diff(lambda kk: S(rho,kk),k)/S(rho,k)
ok=True
dens={'exp':lambda s:mp.e**(-s),'compact':lambda s:1 if s<3 else 0,'gamma2':lambda s:s**2*mp.e**(-s),'pow0.5':lambda s:1/(1+s)**mp.mpf(0.5)}
for n,r in dens.items():
  for k in [0.3,1,3,10]:
    v=I(r,k); good=(-2<v<0); ok&=good
    print(n,k,mp.nstr(v,12),good)
# J limit = 2 M1/M0 for exp (M1/M0=1) and gamma2 (M1/M0=3)
for n,r,ratio in [('exp',dens['exp'],1),('gamma2',dens['gamma2'],3)]:
  k=mp.mpf(300); J=k**2*(I(r,k)+2); print('J',n,mp.nstr(J,10),'2M1/M0=',2*ratio); ok&=abs(J-2*ratio)<0.01*ratio
# alpha=0.5 -> I -> -1
v=I(dens['pow0.5'],mp.mpf(10)**4); print('alpha0.5 I(1e4)=',mp.nstr(v,8)); ok&=abs(v+1)<0.02
# signed counterexample: rho = e^{-s} - 2 e^{-2s}*... choose rho=delta-like: 2e^{-2s}-e^{-s}? M0=0
r=lambda s: 3*mp.e**(-3*s)-mp.e**(-s)*0.9
v=I(r,mp.mpf(1)); print('signed I(1)=',mp.nstr(v,8)); ok&= not(-2<v<0)
print('ALL PASS' if ok else 'FAIL')
