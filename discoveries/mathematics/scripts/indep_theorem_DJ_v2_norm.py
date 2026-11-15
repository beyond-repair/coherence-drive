"""v2 addendum: v1's individual rho values depend on how each functional is scaled (only the sum is invariant).
Re-express rho(P,P') relative to the constant function 1: rho - log(l_P(L^9 1)/l_P'(L^9 1))."""
import importlib.util, math, sys, io, contextlib
spec=importlib.util.spec_from_file_location("v1","indep_theorem_DJ.py"); m=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
one=lambda P: sum(c for c,_ in m.functional(P))
d=1e-6; P1=(m.hi-d,m.hi); P2=(m.lo,m.lo+d)
r12=m.rho(P1,P2)-math.log(one(P1)/one(P2)); r21=m.rho(P2,P1)-math.log(one(P2)/one(P1))
print(f"normalised rho(P1,P2)={r12:.7f} rho(P2,P1)={r21:.7f} sum={r12+r21:.9f}")
ok=abs(r12-0.0070018)<3e-7 and abs(r21-0.0069963)<3e-7
print("PASS" if ok else "FAIL","normalised values vs repo 0.0070018 / 0.0069963")
