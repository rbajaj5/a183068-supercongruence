# Cryptography connections: affine privacy amplification and residue collisions

**Status:** Classical application and elementary deduction, with exact finite
checks. The residue-collision deduction depends on the core A183068 proof
draft. Neither part claims a new cryptographic primitive or literature priority.

**Scope:** This note connects the repository's
[affine hashing law](AffineSpectrumHashing.md) to privacy amplification for
an explicit source model, and identifies a collision obstruction to using
[A183068 residues](../PROOF.md) as a hash. It supplies proofs, boundary cases,
and a small reproducible experiment; it does not establish practical
cryptographic performance.

Reproduce from the repository root:

    python verification/related/verify_cryptography_connections.py

## 1. The useful connection: compressing an affine source

Let X be uniform on a fixed affine space a+V in F_2^n, with dim V=r.
Choose a uniformly random linear map L:F_2^n -> F_2^t independently of X
and the choice of a+V. The matrix L is a public seed, not a secret key.
Write K=rank(L restricted to V).

For each fixed L, the image LX is uniform on the affine space L(a)+L(V).
Indeed, every image point has exactly 2^(r-K) preimages. Its support therefore
has 2^K points. If U_t is uniform on F_2^t, the total variation distance is

$$
\Delta(LX,U_t\mid L)=1-2^{K-t}.                         \tag{1}
$$

Here total variation means one half of the sum of absolute probability
differences. The total excess probability on the image support is
1-2^(K-t); the total missing probability outside it is the same.
Thus (1) is an exact calculation, not an asymptotic estimate.

The notation in (1) conditions on a particular seed value. For the joint
distributions, with U_t independent of L,

$$
\Delta((L,LX),(L,U_t))=\mathbb E_L[1-2^{K-t}].           \tag{2}
$$

This public-seed statement matters: averaging the output distribution while
concealing L would measure a different quantity.

### Exact rank distribution

After choosing a basis of V, the restriction of L is a uniform t by r
binary matrix. Its probability of rank k is N_(t,r)(k)/2^(tr), where

$$
N_{t,r}(k)=
\prod_{i=0}^{k-1}
\frac{(2^t-2^i)(2^r-2^i)}{2^k-2^i},
\qquad 0\le k\le\min(t,r),                              \tag{3}
$$

and the empty product N_(t,r)(0) is 1.
To count these matrices, write a rank-k matrix as A B with A full column
rank and B full row rank. The numbers of choices are respectively
the two numerator products. Each matrix is represented once for each
change of basis in its k-dimensional intermediate space, giving the
denominator |GL(k,2)|.

Combining (2) and (3) gives the exact seeded distance

$$
\epsilon_{r,t}=
2^{-tr}\sum_{k=0}^{\min(t,r)}
N_{t,r}(k)(1-2^{k-t}).                                 \tag{4}
$$

If t<=r, the probability that a seed gives a perfectly uniform output is

$$
\Pr[K=t]=\prod_{j=0}^{t-1}(1-2^{j-r}).                  \tag{5}
$$

Consequently, for t>=1,

$$
\epsilon_{r,t}
\le 1-\prod_{j=0}^{t-1}(1-2^{j-r})
\le (2^t-1)2^{-r}<2^{t-r}.                             \tag{6}
$$

Equation (6) is only asserted for t<=r. If t>r, every output lies on at
most 2^r points and its distance from uniform is at least 1-2^(r-t).
For t=0, the output is empty and the distance is zero. For r=0, the source
is deterministic and the distance is 1-2^(-t).

### A small fully checkable example

For r=3 and t=2 there are 64 possible restriction matrices. Their rank
counts are 1, 21, and 42 at ranks 0, 1, and 2. Therefore

$$
\Pr[K=2]=21/32,\qquad
\epsilon_{3,2}=\frac{1(3/4)+21(1/2)}{64}=\frac{45}{256}.
$$

The chance of drawing a deficient matrix and the average statistical
distance are different quantities.

## 2. A concrete privacy-amplification model with linear leakage

Suppose a raw string W is uniform on F_2^n and an observer learns Z=B W,
where B is a fixed public binary matrix of rank n-r. Conditional on any
possible Z=z, W is uniform on an affine coset of ker B of dimension r.
Choose L independently of (W,Z) as above. Then the same calculation gives

$$
\Delta((L,Z,LW),(L,Z,U_t))=\epsilon_{r,t},               \tag{7}
$$

with U_t independent of (L,Z). For each z, the offset of the coset changes
but its dimension and the rank of L on ker B do not. Averaging (1) first
over z and then over L proves (7).

For example, let n=3, reveal Z=W_0+W_1 modulo 2, and extract one bit using
a uniformly random one-row L. The remaining affine dimension is r=2.
Among the four possible restrictions to ker B, one is zero and three
have rank one, so the exact joint distance is (1/4)(1/2)=1/8.
The checker computes that distance directly from the joint distribution.

This is a concrete application of classical universal hashing and privacy
amplification. It also explains a useful reversal of the repository's
existing [affine-spectrum argument](AffineSpectrumHashing.md):

- Spectrum separation wants injectivity, hence full column rank and t>=r.
- Randomness extraction wants surjectivity, hence full row rank and t<=r.

The same rank calculation answers both questions, with different goals.
For matching-phase spectra of dimension 2s, the formulas apply if the
source is explicitly uniform on that support. Knowing the support alone
does not establish that the source has this distribution.

### Assumptions and limits

The source or leakage rule must not be selected after inspecting L:
a seed-dependent source can be chosen inside ker L. The raw string in
the leakage example must actually be uniform, and the revealed information
must have the specified linear form. An arbitrary distribution, additional
side information, reuse across dependent outputs, or a complete key-agreement
protocol needs its own argument. Equation (7) makes no quantum-side-information
claim. General leftover-hashing theorems address broader models [2].

The exact formulas here are classical linear-algebra consequences.
Their contribution to this repository is an explicit application,
reproducible parameter calculation, and an explanation of its conditions.

## 3. Why direct A183068 residue hashing has easy collisions

Let a be the sequence in the core proof and consider the exploratory map

$$
H_{p,m}(n)=a(n)\bmod p^m,
$$

for public prime p and positive integer m. This is a proposed mathematical
map for analysis, not an existing deployed cryptosystem.

Set r=ceil(m/2). The core supercongruence states, for every n>=1,

$$
a(np^r)\equiv a(np^{r-1})\pmod {p^{2r}}.
$$

Since 2r>=m, it immediately follows that

$$
H_{p,m}(np^r)=H_{p,m}(np^{r-1}).                        \tag{8}
$$

Taking n=1 constructs distinct colliding inputs p^r and p^(r-1).
Their encodings have O(m log p) bits. They can be constructed in polynomial
time in that bit length without evaluating a. Thus this is an efficient
chosen-collision construction, rather than a pigeonhole observation.
Any efficiently evaluable implementation of this exact map on a domain
containing those inputs fails collision resistance.

For p=2, use the ordinary fixed-width m-bit encoding, including leading
zeros. Both 2^(r-1) and 2^r fit for every m>=2, since r<m. The boundary
m=1 must be excluded on this particular domain: a(0)=1 and a(1)=26,
so the one-bit map sends 0 to 1 and 1 to 0 and is injective.
Arbitrary restricted domains need a separate containment check.

Any deterministic postprocessing g of the residue and common parameters
preserves (8). A collision-resistant hash applied only to the residue
cannot recover the distinction already lost. Processing the original
input, unreduced a(n), or additional independent information defines a
different construction and is outside this argument.

This is an elementary consequence of the existing proof, with no novelty
claim. It does not provide inversion for arbitrary targets, an average-case
second-preimage attack, or an attack on RSA, elliptic-curve cryptography,
lattice schemes, or any deployed hash. Sparse orbit collisions alone also
do not characterize a generator's overall pseudorandomness.

## 4. What the checker establishes

The [checker](../verification/related/verify_cryptography_connections.py)
uses standard-library integer and rational arithmetic. It compares the
sequence recurrence with direct factorial sums, tests (8) across stated
small prime/modulus ranges, and checks fixed-width domain boundaries.
For small r,t it enumerates every binary matrix and every source point,
computes output probabilities directly, and compares their total variation
with (1)--(5). It also enumerates the linear-leakage example in Section 2.

Finite computations test the implementation and examples. The general
claims are the deductions written above. No implementation here generates
production keys or purports to certify a cryptographic protocol.

## 5. Provenance and sources

Prepared at Ravi Bajaj's request using AI-assisted mathematical derivation,
implementation, and separate review of the residue and affine-source
arguments. These reviews are not conventional peer review.

1. J. Lawrence Carter and Mark N. Wegman, "Universal classes of hash
   functions," Journal of Computer and System Sciences 18(2), 143--154
   (1979), [doi:10.1016/0022-0000(79)90044-8](https://doi.org/10.1016/0022-0000%2879%2990044-8).
2. Marco Tomamichel, Christian Schaffner, Adam Smith, and Renato Renner,
   "Leftover Hashing Against Quantum Side Information,"
   [arXiv:1002.2436](https://arxiv.org/abs/1002.2436),
   IEEE Transactions on Information Theory 57(8), 5524--5535 (2011).
   This is background for the broader security model, not a theorem
   established by the small affine-source checker.
3. [Core A183068 proof](../PROOF.md),
   [affine-spectrum hashing](AffineSpectrumHashing.md), and
   [matroid hashing law](MatroidHashingLaw.md).

Shared p-adic vocabulary alone does not establish an application of A183068
to encryption. For example, the published
[PIE encoding work](https://eprint.iacr.org/2023/700) uses p-adic methods
for rational encoding in homomorphic encryption; this note establishes
no performance or security transfer from the present supercongruence to PIE.
