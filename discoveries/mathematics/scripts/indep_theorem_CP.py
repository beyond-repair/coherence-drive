# Independent mpmath re-derivation of IFI Theorem CP (f7845ada80f9) tail constants from stated inputs
from mpmath import mp, mpf, log
mp.dps=40
r=mpf('0.4237312869626079'); q2=-mpf('0.172547602129'); l2=q2*r
l3=mpf('-0.01706764406262'); q3=l3/r
a1=mpf('0.00571256871089104'); a2=mpf('-4.15763912993700e-5'); a3=mpf('-2.36115967884500e-5')
da3=mpf('4.6e-8'); eps0=mpf('2.9e4'); rho=mpf('1e-3'); n0=12
ok=tot=0
def chk(n,c):
    global ok,tot; tot+=1; ok+=bool(c); print('PASS' if c else 'FAIL',n)
B=(a2/a1)/q2**4; B3=(a3/a1)/q3**4
w=q2**2/q3; th=rho/(r*abs(q3))
chk('w = -0.73915380', abs(w+mpf('0.73915380'))<1e-7)
chk('theta = 0.058590', abs(th-mpf('0.058590'))<1e-6)
lim=B3*(q3-1); dlim=(da3/a1)/abs(q3)**4*abs(q3-1)
print('B3(q3-1)',lim,'+-',dlim)
chk('B3(q3-1) lower >= 1630.28', lim-dlim>=mpf('1630.28')-0.01)
E=(eps0/a1)*(r/rho)**4
Gs=abs(B3)+abs(da3/a1/q3**4)+E*th**n0
Bs=abs(B)+mpf('1e-5')+Gs*abs(q3/q2)**n0
print('E',E,'G*',Gs,'B*',Bs)
chk('G* <= 1845', Gs<=1845); chk('B* <= 8.2108', Bs<=mpf('8.2108'))
bb=Bs*abs(q2)**n0; chk('|beta_m| <= 5.72e-9', bb<=mpf('5.72e-9'))
P1=E*(1+rho/r); P2=(abs(B)+mpf('1e-5'))*Gs*(1+abs(q2*q3)); P3=Gs**2*(1+q3**2)/2; P4=Bs**3*(1+abs(q2)**3)/(3*(1-bb))
print('P',P1,P2,P3,P4)
chk('P1 <= 1.6405e17',P1<=mpf('1.6405e17')); chk('P2 <= 1.53e4',P2<=mpf('1.53e4'))
chk('P3 <= 1.70e6',P3<=mpf('1.70e6')); chk('P4 <= 185.461',P4<=mpf('185.461'))
c2=B**2/2*(1-q2**2); print('B^2/2(1-q2^2)',c2); chk('= 32.7041 +- 1e-4', abs(c2-mpf('32.7041'))<2e-4)
E2=lambda n: P1*th**n+P2*abs(q2)**n+P3*abs(q3)**n+P4*(abs(q2)**3/abs(q3))**n
E1=lambda n: c2*abs(w)**n+E2(n)
print('E1(11)',E1(11),'E1(12)',E1(12))
chk('E1(12) <= 269.33 < 1630.28', E1(12)<=mpf('269.33'))
chk('E1(11) ~ 4583 exceeds limit (n0=12 is needed by this bound)', E1(11)>lim and abs(E1(11)-4583)<5)
bases=[th/abs(w),abs(q2)/abs(w),abs(q3)/abs(w),abs(q2)**3/abs(q3)/abs(w)]
print('bases',[mp.nstr(b,4) for b in bases])
chk('all bases of E2/|w|^n < 1', all(b<1 for b in bases))
chk('E2(15)/|w|^15 <= 5.028 < 32.704', E2(15)/abs(w)**15<=mpf('5.028'))
print('E2(14)/|w|^14',E2(14)/abs(w)**14)
chk('E2(14)/|w|^14 ~ 63.4 > c2', abs(E2(14)/abs(w)**14-mpf('63.4'))<0.5)
chk('two-sided 1360.9 / 1906.1', lim-dlim-E1(12)>=mpf('1360.9') and lim+dlim+E1(12)<=mpf('1906.1'))
chk('rate l2^2/(r|l3|) = 0.7391537958', abs(l2**2/(r*abs(l3))-mpf('0.7391537958'))<1e-9)
# Taylor remainder sanity: |x-log(1+x)-x^2/2| <= |x|^3/(3(1-|x|))
chk('Taylor remainder bound on grid', all(abs(x-log(1+x)-x**2/2)<=abs(x)**3/(3*(1-abs(x))) for x in [mpf(k)/100 for k in range(-90,91) if k]))
# CP.1 data sign check from CC level sums (12 sig. digits; only n<=9 resolvable)
s={4:'0.00564716030397',5:'0.00242403694245',6:'0.00102545231951',7:'0.000434629687783',8:'0.000184158071629',9:'7.80341278693e-5',10:'3.30654582556e-5'}
s={k:mpf(v) for k,v in s.items()}
T={n:log(s[n+1]/(r*s[n]))-B*q2**n*(q2-1) for n in range(4,10)}
chk('sign T_n = (-1)^n for n=4..9 (float data)', all((T[n]>0)==(n%2==0) for n in T))
chk('|T_n|/|q3|^n in [1360.9,1906.1] n=4..9', all(1360.9<=abs(T[n])/abs(q3)**n<=1906.1 for n in T))
print(f'{ok}/{tot} PASS')
