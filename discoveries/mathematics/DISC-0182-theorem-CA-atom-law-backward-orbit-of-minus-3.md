# Discovery: Theorem CA, the exact atom law on the backward orbit of −3 (D=z/2 there), infinitely many atoms of ν per scale period, and all 311 of Theorem BZ's atoms obey it

## Discovery ID

DISC-0182

## Status

THEOREM in the mathematical sense only (repository proof; CA.1 is exact algebra, CA.3's instance and CA.4 are computer-assisted arb certificates). Method KNOWN in structure (spectral decimation with exceptional values; the law looks like the classical "6-series" of the Sierpinski gasket, identification not verified). Atom locations and the accumulation point λ*: novelty UNRESOLVED (not searched). Not thrust.

## Date Discovered

2026-10-29 (America/New_York), ~7:59am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 0d83dde51ff38c5ec4bf8f0e8f2a854e2e033b71 (committed 2026-10-29 7:19am EDT).

## Original Evidence

GASKET.md Theorem CA (heading line 3233; Setting line 3235; CA.1 line 3244; CA.2 line 3245; CA.3 line 3246; CA.4 line 3247; proof lines 3249–3256; Kept Failure CA.5 line 3258; Conjecture CA.6 line 3260; open list line 3265; NOT THIS line 3268; witness paragraph line 3272), CLAIM_STATUS.md new row (line 83), README.md (line 1140), scripts/gasket_fractional_profile_atom_law.py (new, 330 lines), scripts/cli.py, tests/test_cli.py.

## Discovery

Setting as in DISC-0180 (Theorem BZ): p(z)=z(z+5), c(z)=(z+6)/((z+2)(z+5)), e(z)=2z/(2+z), D=1/r_∞ with D=c·D∘p−e off K_p, ψ(v)=lim p^k(5^−k v), f=1/Q_∞=Π·D(ψ)−S, Z=ψ^−1(K_p). O=⋃_k p^−k(−3), the backward orbit of −3 (one of the two points of p^−1(−6)={−2,−3}), Λ_O={λ>0: ψ(−5^k λ)∈O for some k}.

- CA.1: O⊂[−5,0]∖K_p is real and avoids −2,−5,−6; D(z)=z/2 (r_∞=2/z) on O∪{−6}.
- CA.2 (atom law): ψ(u)∈O with u<0 implies u∉Z and f(u)=0, so −u is an atom with ν({−u})=1/f'(u)>0; by ν(5A)=3ν(A), every λ∈Λ_O is an atom.
- CA.3: every sign-change point of ψ−ψ(x), x∈Z, is a limit of atoms; certified instance: atoms λ_n∈(1.054,1.055), n≥10, accumulating at λ*=1.0546444769654709152… with ψ(−λ*)=−1 (−1∈K_p since p(−1)=−4=p(−4)). n=1,2 are BZ's atoms 1.171910250998837… and 1.016316417446789…; BZ's largest atom λ_1=3.6152567198877… has ψ(−λ_1)=−3.
- CA.4: BZ.5's certificate re-run unchanged gives the same 311 atoms in (1,5), and each one is in Λ_O.

## Why It Matters

It turns DISC-0180's list of 311 numerically certified atoms into an exact rule: the atoms come from one backward orbit of the decimation map, seeded at −3 and not at −2. It answers DISC-0180's open "infinitely many atoms per period?" (yes) and carries out the next experiment that entry proposed (check whether the atoms are the renormalised exceptional "6-series").

## Derivation

Repository proof, lines 3249–3256. The key step is one line of algebra, which I re-derived with sympy: c(z)p(z)/2−e(z)=z/2 identically ((z+6)z/(2(z+2))−2z/(z+2)=z(z+2)/(2(z+2))). So z↦z/2 solves D=c·D∘p−e wherever c and e are finite. It is seeded at −6 because c(−6)=0, so D(−6)=−e(−6)=−3=−6/2 without knowing D(6) (only that it is finite). Induction along p^−k(−3) gives CA.1. CA.2 then follows by BZ.3's unrolling: the telescoped sum vanishes exactly. CA.3 uses the inverse branches g_±(w)=−5/2±√(w+25/4), |g_±'|≤1/√5 on [−5,0], g_−(−4)=−4, g_+(−4)=−1, and the IVT. CA.4 uses monotonicity of f on the certificate boxes (f'>0 on the real segment).

## Assumptions

As stated in the repository and not re-run there: AQ (1)–(3), BD.4, BJ.6, BS.1, BX.1–BX.2 (BX.1 itself rests on Assumption BX, the classical Stieltjes characterisation, see DISC-0177), BZ.1–BZ.4 (K_p pieces and |g'|≤1/√5, D=c·D∘p−e, f=Π·D(ψ)−S with tail constants, ν off −Z). BZ's inverse-Q routine and atom certificate imported unchanged. The repository states no literature assumption for CA itself.

## New Results

- ν has infinitely many atoms per scale period (DISC-0180 left this open).
- Exact description of a set of atoms (Λ_O), with the one-sided statement only (CA.2: Λ_O ⊂ atoms). The converse is Conjecture CA.6 (DISC-0184).
- Observation (the repository's script prints g_−'(−4)=−1/3; the inference is mine): λ_n−λ* alternates in sign with ratio close to −1/3, so the 5^−(n+1)/2 bound in CA.3 is valid but not sharp (|h_n+1| decays like 3^−n). Harmless to the proof.

## Prior Art

- Fukushima–Shima (1992) and Shima (1991) spectral decimation for the Sierpinski gasket Laplacian: with x=−z, the decimation map is x(5−x), the exceptional ("forbidden") values are 2, 5 and 6, and the eigenvalues of the "6-series" are generated from 6 through the preimage 3, while the other preimage 2 is forbidden. In the repository's sign convention this is exactly −6, −3 (allowed, CA.1) and −2 (where c and e have their poles, Kept Failure CA.5). So the structure of Theorem CA appears to be the corner-resolvent version of a classical fact. Not verified line by line against those papers in this run.
- Teplyaev, J. Funct. Anal. 159 (1998) 537–567, https://doi.org/10.1006/jfan.1998.3297: pure point spectrum for the Neumann infinite gasket, eigenvalues described through backward orbits of exceptional values. Bears directly on Conjecture CA.6 (DISC-0184) once the setting (boundary condition, corner vector) is matched. Same lead as DISC-0180.

## Novelty Analysis

Method and the shape of the result: KNOWN in related settings (see Prior Art). What is specific here is the statement for the repository's scaled corner Stieltjes function Q_∞ and the certified numbers (λ*, the λ_n, the check that all 311 BZ atoms lie in Λ_O). Their novelty is UNRESOLVED (not searched). Not a NOVELTY CANDIDATE on present evidence.

## Falsification Attempts

1. Repo witness, fresh clone at 0d83dde51ff38c5ec4bf8f0e8f2a854e2e033b71 on the box: `python3 scripts/gasket_fractional_profile_atom_law.py` EXIT 0 in 123 s ("all Theorem CA checks passed"; 311 certified atoms, 311 identified with Λ_O, by depth {0:1, 2:1, 3:3, 4:5, 5:10, 6:20, 7:39, 8:72, 9:94, 10:53, 11:10, 12:2, 13:1}; λ*=[1.0546444769654709152 ± 2.97e−20]; |f| at Λ_O points n=0..7 below 1e−80; CA.5 witness f(u)=[2.197946759591264 ± 2.10e−16]). Log: /workspace/ca_witness.log.
2. Algebra (sympy, independent): c·p/2−e−z/2 simplifies to 0; c(−6)=0; −e(−6)=−3. PASS.
3. Independent numerical route, /workspace/scratch-ifi/indep_theorem_CA.py (no repository code, does NOT use the Π/S formula): ψ by 200 steps of p on 5^−200 v; 1/Q_∞(u)≈(5/3)^M D_(M+K)(5^−M u) by the finite fixed-point recursion from D_0=3+z, M=90, K=24, mpmath 90 digits. Results: ψ(−λ_1)=−3 at λ_1=3.6152567198877032728; λ*=1.0546444769654709152 (all 20 printed digits); λ_n for n=0..7 solving ψ(−λ)=h_n give 0.723051343977540655, 1.17191025099883743, 1.0163164174467888, … (n=0..7 all match the repository's arb enclosures to every digit I printed), and |1/Q_∞| at every one of them is ≤7e−44, falling like 3^−M as M grows (≈1e−24 at M=50), i.e. a true zero of f, not a near miss. PASS.
4. Logical attack: CA.1 needs D(6) finite only (r_∞(6)∈(0,1/6]); the induction needs each preimage to avoid the poles −2, −5 of c and e, which the repository checks (−2∉O since p(−2)=−6∉O; −5∉O since p(−5)=0 is fixed). No gap found. CA.2 is one direction only, as the repository itself says.

Not broken.

## Experimental Validation

Not applicable (pure mathematics on a graph). Computational as above. Repository reports pytest -k 'not reproduce': 40 passed (not re-run here).

## Mathematical Status

Theorem (repository proof), CA.3 instance and CA.4 computer-assisted. Converse open (DISC-0184).

## Patent Relevance

None. The repository's NOT THIS fence: atoms of a spectral measure are not a flux and not a force; Stage 1 untouched; no W, 0.08, 0.23 or 30 μN/kW. The repository description (closed-surface identity; aft-heavy flux is not a net force) still matches its claim fence.

## Related Discoveries

DISC-0180 (Theorem BZ: 311 atoms now explained; its open "infinitely many atoms?" answered; its proposed next experiment carried out), DISC-0183 (Kept Failure CA.5: the −2 branch seeds no atom), DISC-0184 (Conjecture CA.6: atoms are exactly Λ_O, ν pure point), DISC-0181 (ν not a.c.), DISC-0177 (Theorem BX: the measure ν), DISC-0175 (ρ_k has no limit; CA.6 would give limsup ρ_k=1).

## Open Questions

The converse (Conjecture CA.6). Whether points of −Z at even-order critical points of ψ are also limits of atoms. A closed form for the masses 1/f'(u) on Λ_O. Exact limsup and liminf of ρ_k. Whether the statement matches the 6-series of Fukushima–Shima / Teplyaev exactly once the corner vector is identified.

## Next Experiments

Match AQ's corner resolvent to Teplyaev's infinite-gasket setting; if his pure-point theorem applies to the corner vector, Conjecture CA.6's "ν(−Z)=0" follows from the literature and the remaining content is that only the 6-series reaches the corner vector (5-series eigenfunctions may vanish there by symmetry; check). Derive the mass 1/f'(u) on Λ_O from BZ.3's product by differentiating at a zero.

## Reproduction Instructions

```
git clone https://github.com/beyond-repair/informational-flux-identity
git -C informational-flux-identity checkout 0d83dde51ff38c5ec4bf8f0e8f2a854e2e033b71
cd informational-flux-identity && python3 scripts/gasket_fractional_profile_atom_law.py   # needs python-flint, sympy; ~2.3 min per the repository
python3 /workspace/scratch-ifi/indep_theorem_CA.py   # archive check, mpmath only, <1 s
```

## Evidence Log

- 2026-10-29 ~7:59am EDT. Indexed; repo witness EXIT 0 (123 s). Independent algebra and finite-level numerical checks PASS (above). No erratum.

- 2026-10-29 ~10:00am EDT. Converse proved off −Z by Theorem CB (DISC-0185, 0d9944c015fb1ab192f9abe98096dfa8e1060b2c); the Next Experiment 'derive the mass 1/f\'(u) from BZ.3's product' is carried out there as CB.5. No status change.

## Change History

- 2026-10-29. Initial archive entry.
