# Placed in coherence-drive discoveries/mathematics/scripts.
# Uses the REPO's F0 point evaluator (cn.F0_bound via co.taylor_coeffs) -- F0 is a shared input, not independent.
# Usage: IFI_SCRIPTS=/path/to/informational-flux-identity/scripts python3 indep_theorem_CR_CS_dump_f0.py 4096 300
# (IFI at 9cb3b84d6b28; about 80 s) -> f0_M4096_N300.txt, read by indep_theorem_CR_CS.py part B via F0FILE.
import sys,time,os
sys.path.insert(0,os.environ.get('IFI_SCRIPTS','scripts'))
import gasket_fractional_profile_level_third as co
from flint import arb
M=int(sys.argv[1]); Nc=int(sys.argv[2])
t=time.time()
f=co.taylor_coeffs(arb(1),M=M,Nc=Nc)
import gasket_fractional_profile_level_ratio as ce
c0=3*ce.sigma_closed(arb(-3),0)
open(f'f0_M{M}_N{Nc}.txt','w').write('\n'.join(x.mid().str(60,radius=False) for x in f)+'\nC0 '+c0.mid().str(60,radius=False)+'\n')
print('time',time.time()-t)
