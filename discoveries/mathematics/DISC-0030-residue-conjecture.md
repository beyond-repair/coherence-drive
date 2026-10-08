# Discovery: Residue conjecture in characteristic 2 (sufficient for exact h_n for all n)

## Discovery ID

DISC-0030

## Status

CONJECTURE

## Date Discovered

2026-10-08 (America/New_York). Same archive pass as DISC-0028.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives, branch main, commit 7856c09ad9d566ab1cd6f10598aab660d352f635. Paths: README.md "Residue condition: power-of-two lemma and exhaustive check to k = 31" → Still open; CLAIM_STATUS.md rows "Residue sums S_k ≠ 0 for every chain, 1 ≤ k ≤ 31 — CLAIMED (theorem + finite exact computation)" and "Exact h_n formula for all n — NOT CLAIMED"; scripts/check_residue_extension.py; scripts/residue_chains_gf2_32.c.

## Original Evidence

CLAIM_STATUS at 7856c09ad9d566ab1cd6f10598aab660d352f635: "the residue conjecture Σ_{i≤k} 1/z_i ≠ 0 for all k ≥ 33 not a power of two would suffice (not known to be necessary)". The repository enumerates all 2^k chains in GF(2^32) = F_2[x]/(x^32 + x^7 + x^3 + x^2 + 1) for every k ≤ 31.

## Discovery

Conjecture: for every k ≥ 1 and every chain z_0 = 1, z_{i−1} = z_i² + z_i over F̄_2, S_k = Σ_{i=1}^k 1/z_i ≠ 0. Known: k ≤ 31 (exhaustive), k = 32 and every power of two (DISC-0029), and every k = 2^j + 1 (DISC-0036, from bd212e6), so all k ≤ 33; extended to all k ≤ 45 by the Frobenius-orbit-reduced exact computation at 172f122 (DISC-0038). Open: k ≥ 46 with k not of the form 2^j or 2^j + 1. By DISC-0028 it implies DISC-0027 (no coincidental hits, exact h_n for all n ≥ 3); the converse is not known.

## Why It Matters

It is now the only obstruction on file to a closed form for h_n on build_gasket(n) for all n.

## Derivation

None. Open statement.

## Assumptions

As DISC-0028.

## New Results

Archive-side independent evidence (2026-10-08), by a different route from the repository: instead of solving y² + y = z_{i−1} upward, walk down from every top element z via N(x) = x² + x until reaching 1, then test every prefix chain, keeping S as num/den so the zero test is exact.
- GF(2^16) = F_2[x]/(x^16 + x^5 + x^3 + x + 1), Rabin-checked irreducible: exhaustive, all 917,506 (chain, k) pairs with 1 ≤ k ≤ 15, zero counterexamples.
- GF(2^64) = F_2[x]/(x^64 + x^4 + x^3 + x^2 + 1), a different modulus from the repository's x^64 + x^4 + x^3 + x + 1, Rabin-checked irreducible: 4,000 random tops, 247,945 (chain, k) pairs, max k = 63, zero counterexamples. This is sampling, not a proof; it covers k from 33 to 63 only sparsely.
- Repository scripts rerun at 7856c09ad9d566ab1cd6f10598aab660d352f635: check_residue_extension.py reports all 2^k chains nonzero for 1 ≤ k ≤ 31 (exit 0).

## Prior Art

Not searched. The statement is a concrete question about iterated Artin–Schreier towers over F_2; it may be known or easy in the literature. No novelty is claimed.

## Novelty Analysis

CONJECTURE. Not a novelty candidate: no prior-art search, and the repository disclaims novelty.

## Falsification Attempts

Independent exhaustive search k ≤ 15 in a second field model, random-top search up to k = 63 in a second degree-64 modulus, rerun of the repository's k ≤ 31 enumeration. Not broken. The repository also records that the trace of S_k and the N-level of S_k vary across chains (k ≤ 13, k ≤ 12), so neither is an invariant that proves it.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Open. Exhaustive k ≤ 31; all powers of two (DISC-0029) and all 2^j + 1 (DISC-0036) proved; smallest open k is 34; sparse random evidence to k = 63. Updated again 2026-10-08 from 172f1223983c2f0ba116510a28af9efeae45fb40: all k ≤ 45 by the orbit-reduced walk (DISC-0038, independently reproduced); smallest open k is 46. Updated 2026-10-08 from bd212e6da68d4c71940c977400c66c507b40862a: CLAIM_STATUS now says the conjecture for k ≥ 34 not of the form 2^j or 2^j + 1 would suffice.

## Patent Relevance

None.

## Related Discoveries

- DISC-0028. Mathematical. The reduction.
- DISC-0029. Mathematical. The proved power-of-two case.
- DISC-0027. Mathematical. The h_n statement it would settle.
- DISC-0038. Computational. Orbit reduction; S_k ≠ 0 for all k ≤ 45.

## Open Questions

The subfield argument covers r = 0 and r = 1 (DISC-0029, DISC-0036) and provably does not cover k = 6, 11, 13, 14, 15 (DISC-0037). Find a different invariant, e.g. the repository's norm reformulation G_k(1, 0) = 1 (checked k ≤ 7).

## Next Experiments

Done through k = 45 (DISC-0038). Next: k ≥ 46 in the reduced tree (about 2^40 representatives at k = 46).

## Reproduction Instructions

Repository: `git checkout 7856c09ad9d566ab1cd6f10598aab660d352f635 && python scripts/check_residue_extension.py` (compiles scripts/residue_chains_gf2_32.c).

Archive independent check (Python 3, no dependencies):

```python
import random
def mul(a,b,m,deg):
    r=0
    while b:
        if b&1: r^=a
        b>>=1; a<<=1
        if a>>deg&1: a^=m
    return r
def run(deg,m,tops):
    tested=zeros=0
    for z in tops:
        orbit=[z]
        while orbit[-1]!=1:
            orbit.append(mul(orbit[-1],orbit[-1],m,deg)^orbit[-1])
            assert orbit[-1]!=0
        num,den=0,1
        for zi in orbit[-2::-1]:          # z_1, z_2, ..., z_K
            num,den=mul(num,zi,m,deg)^den, mul(den,zi,m,deg)
            tested+=1; zeros+=(num==0)
    return tested,zeros
print(run(16,(1<<16)|0b101011,range(1,1<<16)))           # (917506, 0)
rng=random.Random(1)
print(run(64,(1<<64)|0x1d,(rng.getrandbits(64) or 1 for _ in range(4000))))  # (247945, 0)
```

(Irreducibility of both moduli was checked separately with Rabin's test.)

## Evidence Log

- 2026-10-08. Recorded from CLAIM_STATUS / README at 7856c09ad9d566ab1cd6f10598aab660d352f635; repository k ≤ 31 rerun OK; archive independent checks as above.

- 2026-10-08 (later). finite-gasket-spectral-derivatives bd212e6da68d4c71940c977400c66c507b40862a proves k = 2^j + 1 (DISC-0036) and records that the subfield test fails for k = 6, 11, 13, 14, 15 (DISC-0037). Open set narrowed to k ≥ 34, k ∉ {2^j, 2^j + 1}. Status unchanged.
- 2026-10-08 (later still). finite-gasket-spectral-derivatives 172f1223983c2f0ba116510a28af9efeae45fb40: Frobenius orbit reduction (proved; DISC-0038) and reduced exact walk S_k ≠ 0 for k ≤ 45. Archive independent walk in a different GF(2^64) model with different representatives: S_k ≠ 0 for all k ≤ 45 (2^39 reduced nodes at k = 45). Open set narrowed to k ≥ 46, k ∉ {2^j, 2^j + 1}. Status unchanged.

## Change History

- 2026-10-08. Initial archive entry.
- 2026-10-08 (later). Known/open ranges narrowed after bd212e6; status unchanged.
- 2026-10-08 (later still). Known/open ranges narrowed after 172f122 (DISC-0038); status unchanged.
