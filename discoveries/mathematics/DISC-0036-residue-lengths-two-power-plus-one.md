# Discovery: Residue sums are nonzero for every chain length 2^j + 1

## Discovery ID

DISC-0036

## Status

THEOREM

## Date Discovered

2026-10-08 (America/New_York). Archive pass after DISC-0031..0035.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives, branch main, commit bd212e6da68d4c71940c977400c66c507b40862a. Paths: README.md "Residue condition: lengths 2^j + 1 and the limits of the subfield test" → Derivation (pairing identity, Lemma) and Corollary; CLAIM_STATUS.md row "Residue sums S_k ≠ 0 for every chain when k = 2^j + 1 (all j ≥ 1); exact h_n formula for 3 ≤ n ≤ 35 — CLAIMED (theorem + finite exact computation)"; COMPLETION_LOG.md "fifth run: residue lengths 2^j + 1"; scripts/check_residue_p_plus_one.py.

## Original Evidence

README Lemma (lengths 2^j + 1) with a complete proof in the repository, plus the supporting exhaustive script in GF(2^64) for k ≤ 14 (not a test).

## Discovery

Let N(x) = x² + x on the algebraic closure of F_2 and z_0 = 1, N(z_i) = z_{i−1}. For every j ≥ 1, p = 2^j, and every chain, S_{p+1} = Σ_{i=1}^{p+1} 1/z_i ∉ GF(2^p); in particular S_{p+1} ≠ 0.

## Why It Matters

Via DISC-0028 it removes the chain lengths 2^j + 1 from the residue conjecture (DISC-0030). With DISC-0029 and the k ≤ 31 enumeration, S_k ≠ 0 for every k ≤ 33, so the smallest open length is 34, a coincidental hit needs n ≥ 36, and h_n = 1 − μ_exc(n) − 5·2^n/(3^{n+1}+3) holds exactly for 3 ≤ n ≤ 35 (previously n ≤ 34).

## Derivation

Repository proof, checked line by line in this archive:
1. Pairing identity. z_i(z_i + 1) = z_{i−1}, so 1/z_i + 1/(z_i + 1) = (z_i + 1 + z_i)/z_{i−1} = 1/z_{i−1} in characteristic 2. Hence 1/z_{i−1} + 1/z_i = 1/(z_i + 1).
2. At i = p + 1: S_{p+1} = S_{p−1} + 1/z_p + 1/z_{p+1} = S_{p−1} + 1/w with w = z_{p+1} + 1.
3. As in DISC-0029, E_j = ker N^p = GF(2^p) and z_i ∈ E_j iff i + 1 ≤ p, so S_{p−1} ∈ E_j.
4. N is additive and N(1) = 0, so N^p(w) = N^p(z_{p+1}) = z_1, and z_1 ≠ 0 because z_1² + z_1 = 1. So w ∉ E_j, hence 1/w ∉ E_j (E_j is a field), and S_{p+1} ∉ E_j.
No gap found. Each step uses only Frobenius linearity and subfield closure.

## Assumptions

Elementary finite-field facts only. No W, no physics input.

## New Results

Archive-side independent checks (2026-10-08), different field models and a different enumeration from the repository:
- GF(2^16) = F_2[x]/(x^16 + x^5 + x^3 + x + 1): every nonzero element is the top z_k of exactly one chain with k ≤ 15, so walking down from all 65,535 elements enumerates every chain of length ≤ 15 without any quadratic solver. Pairing identity holds on every link; S_k ≠ 0 on every chain; S_3, S_5, S_9 lie outside GF(4), GF(16), GF(256) on all 8, 32, 512 chains.
- GF(2^32) = F_2[x]/(x^32 + x^22 + x^2 + x + 1), Rabin-checked irreducible, own F_2-linear solver for y² + y = c: exhaustive k = 17 (all 131,072 chains), S_17 ≠ 0 and S_17 ∉ GF(2^16) on every chain. This is beyond the repository's script range (k ≤ 14).
- GF(2^64) = F_2[x]/(x^64 + x^4 + x^3 + x^2 + 1), own solver: 300 random chains to k = 63 (18,900 (chain, k) pairs), S_k ≠ 0 throughout, and S_{p+1} ∉ GF(2^p) for p = 2, 4, 8, 16, 32 on every sampled chain (k = 33 included).
- Repository script rerun at bd212e6da68d4c71940c977400c66c507b40862a: scripts/check_residue_p_plus_one.py exit 0, counts as recorded.

## Prior Art

Not searched. The argument is elementary. The repository states that no literature was opened and that no novelty is claimed. This archive also claims none.

## Novelty Analysis

THEOREM as a mathematical status (complete proof in the repository, verified). Not a novelty claim and not a novelty candidate: textbook method, literature not checked.

## Falsification Attempts

Proof read step by step. Independent exhaustive checks k ≤ 15 (GF(2^16)) and k = 17 (GF(2^32)), random k = 33 in a second degree-64 model. Not broken.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Proved.

## Patent Relevance

None.

## Related Discoveries

- DISC-0029. Mathematical. Same subfield method for k = 2^j; this answers its open question for r = 1.
- DISC-0030. Mathematical. Removes k = 2^j + 1 from the open set; smallest open k is now 34.
- DISC-0027. Mathematical. Exact h_n range extends to 3 ≤ n ≤ 35.
- DISC-0037. Mathematical. The same subfield test fails for other k, so this route does not prove DISC-0030.

## Open Questions

Whether a different invariant (for example the norm reformulation G_k(1, 0) = 1 recorded in the repository) extends to k = 2^j + r, r ≥ 2.

## Next Experiments

See DISC-0030 and DISC-0037.

## Reproduction Instructions

Repository: `git checkout bd212e6da68d4c71940c977400c66c507b40862a && python scripts/check_residue_p_plus_one.py`.

Archive GF(2^16) check (Python 3, no dependencies, under 1 s; prints per-k chain count, zero count, and subfield count):

```python
# Archive-side independent check of finite-gasket bd212e6 (residue lengths 2^j+1, subfield-test counts).
# Field GF(2^16) = F2[x]/(x^16+x^5+x^3+x+1) (different model from repo's GF(2^64)); every chain of
# length k<=15 lies in GF(2^16) because z_k in ker N^16 iff k+1<=16. Walk DOWN from every nonzero
# element (each is the top z_k of exactly one chain), so enumeration is exhaustive and independent
# of any quadratic solver.
M=(1<<16)|0b101011; D=16
def mul(a,b):
    r=0
    while b:
        if b&1: r^=a
        b>>=1; a<<=1
        if a>>D&1: a^=M
    return r
# find generator, build log tables
ORD=(1<<16)-1
fac=[3,5,17,257]
def pw(a,e):
    r=1
    while e:
        if e&1: r=mul(r,a)
        a=mul(a,a); e>>=1
    return r
g=next(c for c in range(2,1000) if all(pw(c,ORD//q)!=1 for q in fac))
exp=[0]*(2*ORD); log=[0]*(1<<16); x=1
for i in range(ORD):
    exp[i]=x; log[x]=i; x=mul(x,g)
for i in range(ORD,2*ORD): exp[i]=exp[i-ORD]
inv=lambda a: exp[(ORD-log[a])%ORD]
fm=lambda a,b: 0 if a==0 or b==0 else exp[log[a]+log[b]]
def frob(a,p):
    if a==0: return 0
    return exp[(log[a]*pow(2,p,ORD))%ORD]
from collections import Counter
total=Counter(); inside=Counter(); zeros=Counter(); pair_bad=0
for top in range(1,1<<16):
    orbit=[top]
    while orbit[-1]!=1:
        orbit.append(fm(orbit[-1],orbit[-1])^orbit[-1])
    k=len(orbit)-1          # orbit = z_k, z_{k-1}, ..., z_0=1
    if k==0: continue
    zs=orbit[::-1]          # z_0..z_k
    for i in range(1,k+1):  # pairing identity 1/z_{i-1}+1/z_i = 1/(z_i+1)
        if inv(zs[i-1])^inv(zs[i])!=inv(zs[i]^1): pair_bad+=1
    S=0
    for i in range(1,k+1): S^=inv(zs[i])
    total[k]+=1; zeros[k]+=(S==0)
    if k&(k-1):
        p=1<<(k.bit_length()-1)
        inside[k]+=(frob(S,p)==S)
print("pairing failures:",pair_bad)
for k in sorted(total):
    print(k,total[k],"zeros",zeros[k],"S_k in GF(2^p):",inside.get(k,"-"))
```

The GF(2^32) k = 17 and GF(2^64) random checks use the same S = num/den bookkeeping as DISC-0030 with an F_2-linear solver for y² + y = c built by Gaussian elimination on the matrix of N; S ∈ GF(2^p) is tested as num^(2^p)·den = num·den^(2^p).

## Evidence Log

- 2026-10-08. Recorded from README / CLAIM_STATUS / COMPLETION_LOG at bd212e6da68d4c71940c977400c66c507b40862a; proof verified by reading; repository script rerun OK; archive checks as above.

## Change History

- 2026-10-08. Initial archive entry.
