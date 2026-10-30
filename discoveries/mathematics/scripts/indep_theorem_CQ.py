# Placed in coherence-drive discoveries/mathematics/scripts; standalone (numpy, mpmath), no repo imports.
# Independent float check of IFI Theorem CQ (cae1d855f3c7): own matrix builder (FFT Taylor coefficients on |u|=1),
# numpy eig at several N; compares l_4, |l_4|/r, gap to next eigenvalues, sign logic, and a_4 vs data-LSQ.
import numpy as np
from mpmath import mp, mpf, matrix, lu_solve
c,R=83/50,8/5; K=8192
th=2*np.pi*np.arange(K)/K; u=np.exp(1j*th); s=c+R*u
v1=(np.sqrt(15/4-s)-c)/R; v2=(np.sqrt(15/4+s)-c)/R
w1=(s+.5)/(2*s*(3.5-s)); w2=(s-.5)/(2*s*(s+3.5))
def M(N):
    A=np.zeros((N+1,N+1),complex); p1=np.ones(K,complex); p2=np.ones(K,complex)
    for n in range(N+1):
        A[:,n]=np.fft.fft(w1*p1+w2*p2)[:N+1]/K; p1*=v1; p2*=v2
    return A.real
ok=tot=0
def chk(n,cnd):
    global ok,tot; tot+=1; ok+=bool(cnd); print('PASS' if cnd else 'FAIL',n)
# branch sanity: principal sqrt must be the analytic branch on |u|<=1 (15/4 -+ s stays off the negative axis)
chk('15/4 - s, 15/4 + s avoid (-inf,0] on |u|=1', min((15/4-s).real)>0 and min((15/4+s).real)>0)
res={}
for N in (60,100,140,180):
    ev=np.linalg.eigvals(M(N)); ev=ev[np.argsort(-abs(ev))]; res[N]=ev[:8]
    print(N,[f'{z.real:.12e}{z.imag:+.2e}j' for z in ev[:7]])
r=res[140][0].real; l4=res[140][3]
chk('r = 0.42373128696', abs(r-0.4237312869626079)<1e-11)
chk('l_2, l_3 match CG/CO floats', abs(res[140][1].real+0.172547602129*r)<1e-10 and abs(res[140][2].real+0.01706764406262)<1e-12)
chk('l_4 real, = -2.1644655284e-4 to 1e-13', abs(l4.imag)<1e-14 and abs(l4.real+2.1644655283736e-4)<1e-13)
# v1 demanded 1e-15 and FAILED: double-precision eig scatters l_4 by ~2e-14 across N (float noise, not a CQ defect)
chk('l_4 stable across N=60..180 to 5e-14 (double eig noise floor)', max(abs(res[N][3]-l4) for N in (60,100,180))<5e-14)
chk('|l_4|/r = 0.0005108108830', abs(abs(l4.real)/r-0.0005108108830)<1e-12)
nxt=abs(res[140][4]); print('|5th| =',nxt, res[140][4:7])
chk('exactly one eigenvalue in 5e-5<|z|<1e-3 (float, N=140)', sum(1 for z in res[140] if 5e-5<abs(z)<1e-3)==1)
# v1 tried to reproduce the repo's 5th-eigenvalue floats (-1.744e-7, pair -1.16e-8+-1.55e-7i) and FAILED: in double
# precision the eigenvalues of size ~1e-7 move with N (non-normal matrix, below the float noise floor). CQ does not
# claim them (kept limit: only bounded by 5e-5). What is checkable in float is the CQ.2 bound itself:
chk('every eigenvalue beyond the top 4 has |mu|<5e-5 at N=60,100,140,180', all(max(abs(res[N][4:]))<5e-5 for N in res))
chk('5th-eigenvalue floats not stable across N (documents why they stay unclaimed)', np.std([abs(res[N][4]) for N in res])>1e-8)
# a_4 sign logic: sign(a_4 l_4^k) = (-1)^(k+1) iff a_4<0, l_4<0
a4=-2.204e-7
chk('sign(a_4 l_4^k) = (-1)^(k+1)', all(np.sign(a4*l4.real**k)==(-1)**(k+1) for k in range(30)))
# a_4 from data (CC certified level sums, 12 digits) with certified r,l2,l3 and CQ's l4: weighted LSQ (independent of CQ.4)
mp.dps=30
S={4:'0.00564716030397',5:'0.00242403694245',6:'0.00102545231951',7:'0.000434629687783',8:'0.000184158071629',
   9:'7.80341278693e-5',10:'3.30654582556e-5',11:'1.40108723364e-5',12:'5.93684473586e-6',13:'2.51562687729e-6',14:'1.06594981300e-6'}
S={k:mpf(v) for k,v in S.items()}
lam=[mpf('0.4237312869626079'),-mpf('0.172547602129')*mpf('0.4237312869626079'),mpf('-0.01706764406262'),mpf('-0.00021644655283736')]
A=matrix([[l**(n-4)/S[n] for l in lam] for n in range(4,15)]); b=matrix([1 for n in range(4,15)])
x=lu_solve(A.T*A,A.T*b); print('LSQ a1..a4',[mp.nstr(t,6) for t in x])
chk('data-LSQ a_4 within 5% of CQ a_4 = -2.204e-7', abs(x[3]/mpf(a4)-1)<0.05)
# CO's a_1..a_3 fixed: a_4 from the n=4 residual alone
a1,a2,a3=mpf('0.0057125687109'),mpf('-4.15764e-5'),mpf('-2.36116e-5')
e4=S[4]-(a1+a2+a3); print('e_0 = s_4 - a1-a2-a3 =',e4)
chk('n=4 residual sign/size consistent with a_4 (|e_0-a_4|<5e-9 limited by a_2,a_3 digits)', abs(e4-mpf(a4))<5e-9)
print(f'{ok}/{tot} PASS')
