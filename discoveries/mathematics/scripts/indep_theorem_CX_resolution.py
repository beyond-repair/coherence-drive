# v3: resolve v2's N-stability failures (k>=32, N=40 vs 56) by N=72 vs 56
import sys; sys.argv=['x']
exec(open(__file__.replace('_resolution','')).read().split('D1=build(40)')[0])
D2=build(56); D3=build(72); bad=0
for k in range(30,41):
    e2=3**(k+1)*rho(k,D2)-1; e3=3**(k+1)*rho(k,D3)-1; d=abs(e2/e3-1)
    print(k,mp.nstr(e3/(Gst*Bst**k),10),mp.nstr(d,3)); bad+= d>mpf(10)**-6
print("N56-vs-72 unstable count",bad); sys.exit(1 if bad else 0)
