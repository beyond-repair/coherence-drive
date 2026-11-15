# Independent check of IFI Theorem CD (09936074caa8): count O_k=p^-k(-3) in I=(p(a),a], a=psi(-1)
# Uses only p(z)=z(z+5) and the repo's printed value of a; mpmath 60 digits; no repo imports.
import mpmath as mp
mp.mp.dps=60
a=mp.mpf('-0.95082664382932600')  # repo CD.2 value (17 sig digits; margins checked below)
p=lambda z:z*(z+5)
a1=p(a)
lvl=[mp.mpf(-3)]; N=[]; minmargin=mp.inf
for k in range(0,21):
    if k>0:
        nxt=[]
        for t in lvl:
            s=mp.sqrt(t+mp.mpf(25)/4); nxt+= [-mp.mpf(5)/2-s, -mp.mpf(5)/2+s]
        lvl=nxt
    cnt=sum(1 for t in lvl if a1<t<=a)
    minmargin=min(minmargin,min(min(abs(t-a1),abs(t-a)) for t in lvl))
    N.append(cnt)
exp=[1,0,1,3]+[5*2**(k-4) for k in range(4,21)]
print(N); print('match',N==exp,'min margin to endpoints',mp.nstr(minmargin,5))
print('orbit',[mp.nstr(x,12) for x in [a1,p(a1),p(p(a1)),p(p(p(a1)))]])
assert N==exp and minmargin>1e-12
