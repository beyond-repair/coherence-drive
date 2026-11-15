# Independent check of IFI Theorem DB values (not interval; mpmath Chebyshev collocation, own code).
import mpmath as mp, sys
mp.mp.dps=int(sys.argv[2]) if len(sys.argv)>2 else 60
M=int(sys.argv[1]) if len(sys.argv)>1 else 60
a,b=mp.sqrt(5)/2,mp.mpf(5)/2
nodes=[(a+b)/2+(b-a)/2*mp.cos(mp.pi*(j+mp.mpf(1)/2)/M) for j in range(M)]
def bary_w():
    return [(-1)**j*mp.sin(mp.pi*(j+mp.mpf(1)/2)/M) for j in range(M)]
W=bary_w()
def interp_row(x):
    for j,n in enumerate(nodes):
        if x==n: r=[0]*M; r[j]=1; return r
    t=[W[j]/(x-nodes[j]) for j in range(M)]; s=sum(t); return [v/s for v in t]
def op(k):
    Lm=mp.matrix(M,M); sc=mp.mpf(3)**(k+1)
    for i,s in enumerate(nodes):
        s1,s2=mp.sqrt(mp.mpf(15)/4-s),mp.sqrt(mp.mpf(15)/4+s)
        w1=(s+mp.mpf(1)/2)/(2*s*(mp.mpf(7)/2-s)); w2=(s-mp.mpf(1)/2)/(2*s*(s+mp.mpf(7)/2))
        u1=sc*w1/(2*s1)**k; u2=sc*w2/(2*s2)**k
        r1,r2=interp_row(s1),interp_row(s2)
        for j in range(M): Lm[i,j]=u1*r1[j]+u2*r2[j]
    return Lm
G_rep={13:(0.887577,2.53383),20:(1.331403,3.9330),28:(1.82873,5.469)}
Q_rep={13:-0.349942106203,20:-0.338508371108,28:-0.334370141255}
kapm=mp.mpf('0.370860305428934')
ok=0;tot=0
for k in (13,20,28):
    Lm=op(k); E,ER=mp.eig(Lm,left=False,right=True); EL=mp.inverse(ER)
    idx=sorted(range(M),key=lambda i:-abs(E[i])); i0,i1=idx[0],idx[1]
    rho=mp.re(E[i0]); nu=mp.re(E[i1]); q=nu/rho
    one=mp.matrix([1]*M)
    A=[mp.re(ER[i,i0]*sum(EL[i0,j] for j in range(M))) for i in range(M)]
    B=[mp.re(ER[i,i1]*sum(EL[i1,j] for j in range(M))) for i in range(M)]
    # max over X: evaluate B/A on a fine grid by interpolation
    grid=[a+(b-a)*mp.mpf(t)/400 for t in range(401)]
    def ev(v,x): r=interp_row(x); return sum(r[j]*v[j] for j in range(M))
    BA=[ev(B,x)/ev(A,x) for x in grid]
    Gp=max(BA); Gm=max(-v for v in BA)
    rp,rm=G_rep[k]
    print(k,'q',mp.nstr(q,13),'rep',Q_rep[k],'Gp',mp.nstr(Gp,8),'rep',rp,'Gm',mp.nstr(Gm,8),'rep',rm,
          'ratio+',mp.nstr(Gp/((2*k+3)/mp.mpf(12)*kapm),6),'ratio-',mp.nstr(Gm/((2*k+3)/mp.mpf(12)*3*kapm),6))
    for c in (abs(q-Q_rep[k])<1e-10, abs(Gp-rp)<1e-4*max(1,rp), abs(Gm-rm)<1e-3*rm):
        tot+=1; ok+=bool(c)
print(f'{ok}/{tot} PASS')
