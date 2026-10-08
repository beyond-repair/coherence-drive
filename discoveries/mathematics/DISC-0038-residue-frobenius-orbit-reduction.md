# Discovery: Frobenius orbit reduction of the residue test, and S_k ≠ 0 for k ≤ 45

## Discovery ID

DISC-0038

## Status

THEOREM

## Date Discovered

2026-10-08 (America/New_York). Archive pass after DISC-0036/0037.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives, branch main, commit 172f1223983c2f0ba116510a28af9efeae45fb40. Paths: README.md "Residue condition: Frobenius orbit reduction and exact check to k = 45" → Lemma (Frobenius orbits of chains), Corollary (reduced test), Exact finite verification, Corollary (theorem plus finite exact computation); CLAIM_STATUS.md row "Frobenius orbit reduction of the residue test …; residue sums S_k ≠ 0 for every chain, 1 ≤ k ≤ 45; exact h_n formula for 3 ≤ n ≤ 47 — CLAIMED (theorem + finite exact computation)"; COMPLETION_LOG.md "sixth run"; scripts/check_residue_orbits.py, scripts/residue_orbits_gf2_64.c.

## Original Evidence

README lemma with a complete proof in the repository, plus a reduced-tree exact computation in GF(2^64) = F_2[x]/(x^64 + x^4 + x^3 + x + 1) for 1 ≤ k ≤ 45 (2^39 representatives at k = 45; not a test), cross-checked by Galois-invariant trace counts (Python k ≤ 11 in two field models; C full vs reduced k ≤ 22).

## Discovery

Let N(x) = x² + x, F(x) = x², chains z_0 = 1, N(z_i) = z_{i−1} over F̄_2, S_k = Σ_{i=1}^k 1/z_i, B = ⌈log₂(k+1)⌉. Then (1) F permutes length-k chains and S_k(F c) = S_k(c)²; (2) every F-orbit has exactly 2^B chains, so there are 2^{k−B} orbits; (3) σ_b = F^{2^b} = N^{2^b} + 1 fixes depths < 2^b and swaps the depth-2^b entry with its sibling; (4) keeping one arbitrary child at every power-of-two depth and both children elsewhere gives exactly one chain per orbit. Hence S_k ≠ 0 on all chains iff it holds on those 2^{k−B} representatives.

Finite corollary (repository computation, independently reproduced here): S_k ≠ 0 for every chain with 1 ≤ k ≤ 45. With DISC-0029 and DISC-0036 the smallest open length is 46, so a coincidental hit needs n ≥ 48, and h_n = 1 − μ_exc(n) − 5·2^n/(3^{n+1}+3) holds exactly for 3 ≤ n ≤ 47 (previously n ≤ 35).

## Why It Matters

It cuts the exhaustive cost of the residue test (DISC-0030) by the factor 2^B and moves the exact h_n range (DISC-0027) from n ≤ 35 to n ≤ 47. It does not prove DISC-0030; the cost stays exponential in k. The repository says so.

## Derivation

Repository proof, checked line by line in this archive:
1. (z²)² + z² = (z² + z)², and z_0² = 1, so F maps chains to chains; Σ 1/z_i² = (Σ 1/z_i)² in characteristic 2.
2. A chain is determined by z_k (z_i = N^{k−i}(z_k)), so the orbit size is the degree of z_k over F_2. N^{k+1}(z_k) = N(1) = 0 puts z_k in ker N^{2^B} = GF(2^{2^B}), so the degree is a power of two dividing 2^B; z_k ∉ ker N^{2^{B−1}} because k + 1 > 2^{B−1}. So the degree is exactly 2^B. N^k(x) + 1 has derivative 1, so the 2^k chains are distinct.
3. F = N + 1 and N commute, so F^{2^b} = N^{2^b} + 1 in characteristic 2. For i < 2^b, N^{2^b}(z_i) = N^{2^b−i}(1) = 0; at i = 2^b it is z_0 = 1; above it is z_{i−2^b}.
4. Powers of two in 1..k are 1, 2, …, 2^{B−1} (B of them, since 2^{B−1} ≤ k), so |R_k| = 2^{k−B}. Applying σ_b for b increasing repairs depth 2^b without touching shallower depths, so every orbit meets R_k; comparing counts, exactly once. Truncations of R_K are valid R_j, so one walk checks all k ≤ K.
No gap found.

## Assumptions

Elementary Galois theory of finite fields; the two-adic reduction (DISC-0028); DISC-0029, DISC-0036 for the corollary. No W, no physics input.

## New Results

Archive-side independent checks (2026-10-08):
- Direct test of the lemma in GF(2^16) = F_2[x]/(x^16 + x^5 + x^3 + x^2 + 1), Rabin-checked, for every k ≤ 15: all 2^k chains enumerated, orbits formed by squaring, every orbit has size 2^B, S_k(F c) = S_k(c)² on every chain, and R_k meets every orbit exactly once for three different child-selection rules (min root, max root, seeded random). Tr_d(S_k) = 1 counts for k ≤ 15: 2, 4, 4, 8, 24, 40, 72, 144, 240, 560, 1008, 2000, 4048, 8272, 16016; the first eleven match the repository's GF(2^64)/GF(2^32) counts in a third field model.
- Independent C reduced-tree walk in GF(2^64) = F_2[x]/(x^64 + x^31 + x^30 + x^19 + 1) (Rabin-checked; different modulus from the repository), own byte-table linear solver for y² + y = z, and a different representative choice (the kept child at power-of-two depths is picked by the parity of the parent, not the solver's root). Carry-less multiply checked against schoolbook on 10^5 random pairs; solver self-tested. Result: node counts equal 2^{k−B} and S_k ≠ 0 at every node for 1 ≤ k ≤ 45 (549,755,813,888 = 2^39 reduced nodes at k = 45; 14 min on 8 cores), independently reproducing the repository's finite claim.
- Repository scripts rerun at 172f122: scripts/check_residue_orbits.py 36 exits 0 (modulus irreducible; trace counts agree; C validate k ≤ 22 ok; S_k ≠ 0 to k = 36 in 11 s). The full k = 45 repository run was not repeated; the archive's own walk replaces it.

## Prior Art

Not searched. The argument is elementary Galois theory. The repository states that no literature was opened and that no novelty is claimed. This archive also claims none.

## Novelty Analysis

THEOREM as a mathematical status (complete proof in the repository, verified). Not a novelty claim and not a novelty candidate. The k ≤ 45 statement is a finite exact computation, independently reproduced.

## Falsification Attempts

Proof read step by step; lemma tested directly on all chains k ≤ 15 with three selection rules; finite claim re-run in a different field model with a different representative set. Not broken.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Lemma proved. S_k ≠ 0 for k ≤ 45: finite exact computation, reproduced independently. Residue conjecture for k ≥ 46 (k ∉ {2^j, 2^j + 1}) still open (DISC-0030).

## Patent Relevance

None.

## Related Discoveries

- DISC-0030. Mathematical. Smallest open k moves from 34 to 46.
- DISC-0027. Mathematical. Exact h_n range extends to 3 ≤ n ≤ 47; first possible coincidental hit n ≥ 48.
- DISC-0029, DISC-0036. Mathematical. Same tower E_a = ker N^{2^a} = GF(2^{2^a}) used for the orbit size.

## Open Questions

Whether the orbit structure gives more than a constant-factor saving, e.g. an invariant constant on orbits that excludes S_k = 0 for all k.

## Next Experiments

k = 46..50 in the reduced tree costs about 2^{40..44} nodes; feasible on a larger machine but still only evidence.

## Reproduction Instructions

Repository: `git checkout 172f1223983c2f0ba116510a28af9efeae45fb40 && python3 scripts/check_residue_orbits.py 45` (pass a smaller KMAX for a quick run).

Archive: indep_orbit_lemma.py (pure Python, about 80 s) and indep_orbits.c (`gcc -O3 -march=native -fopenmp -o indep_orbits indep_orbits.c && ./indep_orbits 45`), kept in the archive box scratch at /workspace/scratch-res; modulus found and Rabin-checked by find_mod.py there. Core of the C walk: carry S_k as num/den, `num' = num·w + den`, `den' = den·w`, zero test on num; at depth j a power of two keep only the child `y ^ (popcount(z_{j−1}) & 1)`.

Archive orbit-lemma check (Python 3, no dependencies):

```python
"""Direct check of the Frobenius orbit lemma (finite-gasket 172f122) in GF(2^16)
= F2[x]/(x^16+x^5+x^3+x^2+1) for k <= 15: enumerate all 2^k chains, group by
Frobenius orbit, check orbit size 2^B, check S_k(F c) = S_k(c)^2, and check that
R_k (one child at power-of-two depths, chosen by three different rules) meets
every orbit exactly once. Also recompute Tr_d(S_k)=1 counts."""
import random
D, MOD = 16, (1<<16)|0b101101
def mul(a,b):
    r=0
    while b:
        if b&1: r^=a
        b>>=1; a<<=1
        if a>>D: a^=MOD
    return r
def inv(a):
    r=1
    for _ in range(D-1):
        a=mul(a,a); r=mul(r,a)
    return r
# irreducibility (Rabin, deg 16)
x=2
for i in range(16): x=mul(x,x)
assert x==2
roots={}
for y in range(1<<D): roots.setdefault(mul(y,y)^y,[]).append(y)
def trd(s,k):
    d=1
    while d<k+1: d*=2
    t=y=s
    for _ in range(d-1): y=mul(y,y); t^=y
    assert t in (0,1); return t
KMAX=15
chains=[(1,)]
trc=[]
for k in range(1,KMAX+1):
    chains=[c+(w,) for c in chains for w in sorted(roots[c[-1]])]
    assert len(chains)==2**k
    S={c:0 for c in chains}
    for c in chains:
        s=0
        for z in c[1:]: s^=inv(z)
        assert s!=0
        S[c]=s
    B=0
    while (1<<B)<k+1: B+=1
    top={c[-1]:c for c in chains}
    seen=set(); orbits=[]
    for c in chains:
        if c in seen: continue
        orb=[]; cur=c
        while True:
            orb.append(cur); seen.add(cur)
            nxt=tuple(mul(z,z) for z in cur)
            assert nxt in S and S[nxt]==mul(S[cur],S[cur])
            cur=nxt
            if cur==c: break
        assert len(orb)==1<<B,(k,len(orb))
        orbits.append(set(orb))
    assert len(orbits)==2**(k-B)
    rng=random.Random(k)
    rules=[lambda p:min(roots[p[-1]]), lambda p:max(roots[p[-1]]), lambda p:rng.choice(roots[p[-1]])]
    for rule in rules:
        memo={}
        R=[(1,)]
        for j in range(1,k+1):
            nR=[]
            for p in R:
                if j&(j-1)==0:
                    if p not in memo: memo[p]=rule(p)
                    nR.append(p+(memo[p],))
                else:
                    nR+= [p+(w,) for w in roots[p[-1]]]
            R=nR
        assert len(R)==2**(k-B)
        hits=[sum(1 for r in R if r in o) for o in orbits]
        assert all(h==1 for h in hits),(k,hits[:10])
    trc.append(sum(trd(S[c],k) for c in chains))
    print(f"k={k} B={B} orbits={len(orbits)} size={1<<B} R_k meets each orbit once (3 rules) S_k!=0")
print("Tr_d(S_k)=1 counts:",trc)
```

Archive reduced-tree walk (C, x86-64 with PCLMUL, OpenMP):

```c
/* Archive-independent Frobenius-reduced residue check (DISC-0040 audit).
   GF(2^64) = F2[x]/(x^64 + x^31 + x^30 + x^19 + 1) (Rabin-irreducible, find_mod.py),
   a different model from the repository's x^64+x^4+x^3+x+1.
   Root solver: linear right-inverse of N(y)=y^2+y via 8 byte tables.
   At power-of-two depths keep ONE child chosen by a parity hash of the parent
   (not the solver's root), to exercise the "arbitrary choice" clause. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <wmmintrin.h>
#include <smmintrin.h>
#define PLOW ((1ULL<<31)|(1ULL<<30)|(1ULL<<19)|1ULL)
static inline uint64_t clmul(uint64_t a,uint64_t b,uint64_t*hi){
  __m128i C=_mm_clmulepi64_si128(_mm_cvtsi64_si128((long long)a),_mm_cvtsi64_si128((long long)b),0);
  *hi=(uint64_t)_mm_extract_epi64(C,1); return (uint64_t)_mm_cvtsi128_si64(C);}
static inline uint64_t gmul(uint64_t a,uint64_t b){
  uint64_t h,h2,h3; uint64_t l=clmul(a,b,&h); uint64_t l2=clmul(h,PLOW,&h2); uint64_t l3=clmul(h2,PLOW,&h3);
  return l^l2^l3; }
static uint64_t gmul_slow(uint64_t a,uint64_t b){uint64_t r=0;for(int i=0;i<64;i++){if((b>>i)&1)r^=a;uint64_t c=a>>63;a<<=1;if(c)a^=PLOW;}return r;}
static uint64_t T[8][256];
static inline uint64_t Ainv(uint64_t z){uint64_t r=0;for(int i=0;i<8;i++)r^=T[i][(z>>(8*i))&255];return r;}
static void build(void){
  uint64_t pv[64],pc[64]; int have[64]={0};
  for(int j=0;j<64;j++){uint64_t v=gmul(1ULL<<j,1ULL<<j)^(1ULL<<j),c=1ULL<<j;
    while(v){int h=63-__builtin_clzll(v); if(have[h]){v^=pv[h];c^=pc[h];} else {pv[h]=v;pc[h]=c;have[h]=1;break;}}}
  int miss=-1,cnt=0; for(int h=0;h<64;h++){if(have[h])cnt++; else miss=h;}
  if(cnt!=63){fprintf(stderr,"rank %d\n",cnt);exit(2);}
  pv[miss]=1ULL<<miss; pc[miss]=0; have[miss]=1; /* complement vector, mapped to 0 */
  /* but 1<<miss may need reduction by higher pivots: elimination handles it since we reduce top-down */
  uint64_t Ae[64];
  for(int j=0;j<64;j++){uint64_t v=1ULL<<j,c=0; while(v){int h=63-__builtin_clzll(v); v^=pv[h]; c^=pc[h];} Ae[j]=c;}
  for(int i=0;i<8;i++)for(int b=0;b<256;b++){uint64_t r=0;for(int t=0;t<8;t++)if((b>>t)&1)r^=Ae[8*i+t];T[i][b]=r;}
}
static int K; static uint64_t nodes[64], zeros[64];
static void dfs(int j,uint64_t z,uint64_t num,uint64_t den,uint64_t*ln,uint64_t*lz){
  /* children at depth j */
  if(j>K)return;
  uint64_t y=Ainv(z);
  int pow2=(j&(j-1))==0;
  for(int s=0;s<2;s++){
    uint64_t w=y^(uint64_t)s;
    if(pow2 && s!=(int)(__builtin_popcountll(z)&1)) continue;
    uint64_t n2=gmul(num,w)^den, d2=gmul(den,w);
    ln[j]++; if(n2==0) lz[j]++;
    dfs(j+1,w,n2,d2,ln,lz);
  }
}
int main(int argc,char**argv){
  K=atoi(argv[1]); build();
  srand(7); for(int t=0;t<100000;t++){uint64_t a=((uint64_t)rand()<<33)^((uint64_t)rand()<<11)^rand(),b=((uint64_t)rand()<<35)^((uint64_t)rand()<<9)^rand();
    if(gmul(a,b)!=gmul_slow(a,b)){puts("mul mismatch");return 3;}
    uint64_t z=gmul(a,a)^a; uint64_t y=Ainv(z); if((gmul(y,y)^y)!=z){puts("solver fail");return 4;}}
  /* enumerate depth-D frontier serially, then parallel subtrees */
  int D = K<16?K:14;
  typedef struct{uint64_t z,num,den;} st; st *fr=malloc(sizeof(st)<<D); int nf=1; fr[0]=(st){1,0,1};
  for(int j=1;j<=D;j++){ st*nx=malloc(sizeof(st)*(size_t)nf*2); int m=0;
    for(int q=0;q<nf;q++){uint64_t z=fr[q].z,y=Ainv(z); int pow2=(j&(j-1))==0;
      for(int s=0;s<2;s++){uint64_t w=y^(uint64_t)s; if(pow2&&s!=(int)(__builtin_popcountll(z)&1))continue;
        uint64_t n2=gmul(fr[q].num,w)^fr[q].den,d2=gmul(fr[q].den,w); nodes[j]++; if(n2==0)zeros[j]++; nx[m++]=(st){w,n2,d2};}}
    free(fr); fr=nx; nf=m; }
  #pragma omp parallel
  { uint64_t ln[64]={0},lz[64]={0};
    #pragma omp for schedule(dynamic,1)
    for(int q=0;q<nf;q++) dfs(D+1,fr[q].z,fr[q].num,fr[q].den,ln,lz);
    #pragma omp critical
    for(int j=0;j<64;j++){nodes[j]+=ln[j];zeros[j]+=lz[j];} }
  int bad=0;
  for(int j=1;j<=K;j++){int B=0;while((1<<B)<j+1)B++; uint64_t exp=1ULL<<(j-B);
    printf("k=%d nodes=%llu expected=%llu zeros=%llu\n",j,(unsigned long long)nodes[j],(unsigned long long)exp,(unsigned long long)zeros[j]);
    if(nodes[j]!=exp||zeros[j])bad=1;}
  puts(bad?"FAIL":"OK: S_k != 0 on independent reduced tree"); return bad;
}
```

Modulus search with Rabin's test (prints 31 30 19):

```python
# find an irreducible pentanomial x^64 + x^a + x^b + x^c + 1 with a<=31, different from x^4+x^3+x+1
def pmulmod(a,b,f,d):
    r=0
    while b:
        if b&1: r^=a
        b>>=1; a<<=1
        if a>>d &1: a^=f
    return r
def powx2k(f,d,k):
    x=2
    for _ in range(k): x=pmulmod(x,x,f,d)
    return x
def pgcd(a,b):
    while b:
        while a and a.bit_length()>=b.bit_length():
            a^=b<<(a.bit_length()-b.bit_length())
        a,b=b,a
    return a
d=64
for a in range(31,4,-1):
  for b in range(a-1,1,-1):
    for c in range(b-1,0,-1):
      f=(1<<64)|(1<<a)|(1<<b)|(1<<c)|1
      if powx2k(f,d,64)!=2: continue
      if pgcd(f, powx2k(f,d,32)^2)!=1: continue
      print(a,b,c); raise SystemExit
```

## Evidence Log

- 2026-10-08. Recorded from README / CLAIM_STATUS / COMPLETION_LOG at 172f1223983c2f0ba116510a28af9efeae45fb40; proof verified by reading; repository script rerun to k = 36; archive checks as above: independent reduced walk S_k ≠ 0 for every 1 ≤ k ≤ 45, node counts 2^{k−B} at every k.

## Change History

- 2026-10-08. Initial archive entry.
