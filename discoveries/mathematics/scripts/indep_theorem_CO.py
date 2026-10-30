# Independent float/mpmath check of IFI Theorem CO (888d3bee13fa) from CC's certified level sums (12 sig digits); no repo imports
from mpmath import mp, mpf, log, matrix, lu_solve
mp.dps=30
s={4:'0.00564716030397',5:'0.00242403694245',6:'0.00102545231951',7:'0.000434629687783',8:'0.000184158071629',
   9:'7.80341278693e-5',10:'3.30654582556e-5',11:'1.40108723364e-5',12:'5.93684473586e-6',13:'2.51562687729e-6',14:'1.06594981300e-6'}
s={k:mpf(v) for k,v in s.items()}
r=mpf('0.4237312869626079'); q2=-mpf('0.172547602129'); l2=q2*r
l3=mpf('-0.01706764406262'); q3=l3/r
a1=mpf('0.0057125687109'); a2=mpf('-4.15764e-5'); a3=mpf('-2.36116e-5')
ok=0;tot=0
def chk(n,c):
    global ok,tot; tot+=1; ok+=bool(c); print('PASS' if c else 'FAIL',n)
chk('q3 = -0.0402794', abs(q3+mpf('0.0402794'))<1e-7)
chk('q2^2 = 0.0297727 < |q3|', abs(q2**2-mpf('0.0297727'))<1e-7 and q2**2<abs(q3))
chk('1e-3/r = 0.00236 < |q3|', mpf('1e-3')/r<abs(q3))
B=(a2/a1)/q2**4; B3=(a3/a1)/q3**4
print('B',B,'B3',B3,'B3(q3-1)',B3*(q3-1))
chk('B = -8.21069 +- 1e-4', abs(B+mpf('8.21069'))<1e-4)
chk('B3 = -1570 +- 5', abs(B3+1570)<5)
chk('B3(q3-1) = 1.63e3', abs(B3*(q3-1)-1633)<10)
chk('a3/a1 = -0.004133', abs(a3/a1+mpf('0.004133'))<2e-6)
# 3-term model residual vs data: should be small (4th eigenvalue ~ -2.16e-4 => next term ~ a4*(2e-4)^k)
res={n:s[n]-(a1*r**(n-4)+a2*l2**(n-4)+a3*l3**(n-4)) for n in range(4,15)}
for n in res: print(n, mp.nstr(res[n],5), mp.nstr(res[n]/s[n],3))
chk('3-term residual at n=4 < 1% of |a3|', abs(res[4])<0.01*abs(a3))
chk('3-term residual decays: |res_n|<1e-12 for n>=6', all(abs(res[n])<1e-12 for n in range(6,15)))
# drop a3 -> residual at n=4,5 is ~a3, so a3 != 0 is visible in the data
res2={n:s[n]-(a1*r**(n-4)+a2*l2**(n-4)) for n in (4,5)}
chk('2-term residual at n=4 ~ a3 (within 1%)', abs(res2[4]/a3-1)<0.01)
# independent least squares for (a1,a2,a3) on s_4..s_14
# include float 4th eigenvalue l4 ~ -2.16e-4 (CO kept-limits float, not certified); a 3-term fit is biased by the a4 term at n=4
l4=mpf('-2.16e-4')
A=matrix([[r**(n-4),l2**(n-4),l3**(n-4),l4**(n-4)] for n in range(4,15)]); b=matrix([s[n] for n in range(4,15)])
W=matrix([[1/s[n]] for n in range(4,15)])
for i in range(A.rows):
    for j in range(4): A[i,j]*=W[i]
    b[i]*=W[i]
x=lu_solve(A.T*A,A.T*b); print('LSQ a1,a2,a3,a4',x[0],x[1],x[2],x[3])
chk('LSQ a3 within 1% of CO a3', abs(x[2]/a3-1)<0.01)
chk('LSQ a2 within 0.1% of CO a2', abs(x[1]/a2-1)<1e-3)
# Observation: normalised second-order residual n=4..12
obs=[1672.9,1624.4,1639.2,1629.5,1636.4,1631.2,1634.4,1629.5,1622.2]
v=[(log(s[n+1]/(r*s[n]))-B*q2**n*(q2-1))/q3**n for n in range(4,13)]
print([mp.nstr(t,6) for t in v])
chk('Observation values n=4..9 reproduced to 1', all(abs(v[i]-obs[i])<1.0 for i in range(6)))
# n>=10 needs more than the 12 digits of s used here (repo itself warns at n=12); only n<=9 tested
chk('Observation values n=4..9 within 3% of 1633', all(abs(t-1633)/1633<0.03 for t in v[:6]))
print(f'{ok}/{tot} PASS')
