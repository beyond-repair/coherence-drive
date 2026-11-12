import numpy as np, math
rng=np.random.default_rng(0); ok=True
# DP.1 on positive-function cone: Theta(u,v)=log(max(u/v)/min(u/v))
for _ in range(2000):
    h=rng.uniform(0.5,2,50); phi=rng.normal(size=50); 
    s0=max(-(phi/h).min(),0); s1=max((phi/h).max(),0)  # min s with s h +/- phi >=0
    s0=-(phi/h).min(); s1=(phi/h).max()
    t=rng.uniform(0,0.9)/max(abs(s0),abs(s1))
    u=h+t*phi; th=math.log((u/h).max()/(u/h).min())
    ok&=abs(th-math.log((1+t*s1)/(1-t*s0)))<1e-12 and s0+s1>=(phi/h).max()-(phi/h).min()-1e-12
print("DP.1 positive cone identity", ok)
# DP.2: random positive matrix, Birkhoff tau = tanh(diam/4) >= |mu|/rho for real eigenvalues
ok2=True
for _ in range(300):
    A=rng.uniform(0.1,1,(6,6)); ev=np.linalg.eigvals(A); rho=max(abs(ev))
    # diam of A K (K=positive orthant) = max over columns pairs
    cols=A.T; D=max(math.log(max(c1/c2)/min(c1/c2)) for c1 in cols for c2 in cols)
    tau=math.tanh(D/4)
    for m in ev:
        if abs(m.imag)<1e-12 and abs(abs(m)-rho)>1e-9: ok2&= tau>=abs(m)/rho-1e-12
print("DP.2 tau >= |mu|/rho (real mu)", ok2)
q=0.1343549/ (0.1343549/0.3170757)
for n,f in [(5,0.0435818),(7,0.0044106),(9,0.00044485)]:
    print(n, 4*math.atanh(0.317076185**n), "< floor", f)
print("DM.5/cap", 0.363655/0.3170757, "DK.4/cap", 0.53349/0.3170757, "cap/spectral", 0.3170757/0.1725476)
