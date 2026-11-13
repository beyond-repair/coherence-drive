# Independent check of IFI Theorem CN using CC's certified level sums (printed by CC witness, 12 sig digits)
from mpmath import mp, mpf, log, matrix, lu_solve
mp.dps=30
s={4:'0.00564716030397',5:'0.00242403694245',6:'0.00102545231951',7:'0.000434629687783',8:'0.000184158071629',
   9:'7.80341278693e-5',10:'3.30654582556e-5',11:'1.40108723364e-5',12:'5.93684473586e-6',13:'2.51562687729e-6',14:'1.06594981300e-6'}
s={k:mpf(v) for k,v in s.items()}
r=mpf('0.4237312869626079'); q=mpf('0.172547602129')
l2=-q*r
ok=0;tot=0
def chk(name,c):
    global ok,tot; tot+=1; ok+=bool(c); print('PASS' if c else 'FAIL',name)
# alternation for n=4..13
chk('sign(s_{n+1}/s_n - r) = (-1)^n, n=4..13', all(((s[n+1]/s[n]-r)>0)==(n%2==0) for n in range(4,14)))
vals={n:log(s[n+1]/(r*s[n]))/(l2/r)**n for n in range(4,14)}
for n in vals: print(n, mp.nstr(vals[n],8))
chk('|log|/q^n <= 14.60 for n=4..13', all(abs(v)<=14.60 for v in vals.values()))
chk('max at n=4 approx 14.595', abs(abs(vals[4])-mpf('14.5952'))<0.01)
chk('normalized log near B(l2/r-1)=9.628 for n=9..12', all(abs(vals[n]-mpf('9.628'))<0.05 for n in range(9,13)))
# fit a1,a2,a3 with lambda3 unknown: use a1,a2 from levels 10..13 (lambda3 negligible) by least squares
A=matrix([[r**(n-4), l2**(n-4)] for n in range(9,14)]); b=matrix([s[n] for n in range(9,14)])
AtA=A.T*A; Atb=A.T*b; x=lu_solve(AtA,Atb); a1,a2=x[0],x[1]
print('a1',a1,'a2',a2)
chk('a1 ~ 0.00571256871089', abs(a1-mpf('0.00571256871089'))<1e-11)
chk('a2 ~ -4.158e-5 (rel 2%)', abs(a2+mpf('4.158e-5'))<1e-6)
B=(a2/a1)/(l2/r)**4; print('B',B)
chk('B ~ -8.211 (+-0.05)', abs(B+mpf('8.211'))<0.05)
a3=s[4]-a1-a2; print('implied a3 (lambda3 term at n=4)',a3)
chk('|implied a3| <= 1.125e-4', abs(a3)<=mpf('1.125e-4'))
print(f'{ok}/{tot} PASS')
