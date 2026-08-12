# Live-source boundary for twelve Bala-census records

**Audit date:** August 12, 2026  
**Status:** record-level source reconciliation; no novelty claim

The 110-record campaign is a search census, not a list of 110 open
conjectures. This note records the live-OEIS and primary-source check for
twelve entries that were once either queued or recorded as wholly open. It
prevents three different objects from being conflated:

1. a proved supercongruence;
2. a proved baseline followed by a stronger open refinement; and
3. a page returned by the search although it contains no live Bala
   supercongruence conjecture.

## 1. Published-source closures

### A002895: Domb numbers

Put

```math
D(N)=\sum_{k=0}^{N}
\binom Nk^2\binom{2k}{k}\binom{2N-2k}{N-k}.
```

This is [A002895](https://oeis.org/A002895). Theorem 1.1 of
[Osburn--Sahu](https://arxiv.org/abs/1201.6195) proves, more generally,

```math
D(mp^r,A,B,C)\equiv D(mp^{r-1},A,B,C)\pmod {p^{3r}}
```

for `p > 3`, `A >= 2`, and `B,C >= 1`. Taking `A=2` and `B=C=1`
is exactly A002895. The record is therefore source-closed, not a new proof
target.

### A005258: the zeta(2) Apery numbers

[A005258](https://oeis.org/A005258) is the classical Apery sequence

```math
A(N)=\sum_{k=0}^{N}\binom Nk^2\binom{N+k}{k}.
```

Coster's Apery supercongruence gives its ordinary cubic adjacent-level
tower for primes at least 5. The campaign uses this as published
infrastructure; it does not relabel the classical theorem as a repository
result. Exact thesis numbering remains a bibliographic check, not a proof
obligation.

### A183204: Cooper's s_7 sequence

The live page identifies [A183204](https://oeis.org/A183204) as Cooper's
`s_7` sequence. The cubic tower for `s_7` is one of the published
sporadic-sequence congruences in
[Osburn--Sahu--Straub](https://arxiv.org/abs/1312.2195). Thus the standard
odd-prime tower is source-closed. The repository's separate small-prime
notes concern sharper binary and ternary boundary statements and do not
turn this classical closure into a new claim.

## 2. Published cubic baseline, enhanced refinement still open

For

```math
U_q(N)=\sum_{k=0}^{N}\binom{N+k}{k}^{q},
```

Coster's theorem supplies the shifted cubic tower at indices `mp^r-1`.
The live pages ask for more:

- [A112028](https://oeis.org/A112028), `q=3`, asks for modulus `p^5` at
  `p-1` and `p^(3r+3)` at later pure prime-power levels;
- [A219562](https://oeis.org/A219562), `q=4`, asks for the same enhanced
  exponents.

The published `p^(3r)` statement is therefore evidence for `partial`, not
for `published-source`: the extra three powers remain a genuine target.

### A108628: shifted multivariate Apéry coefficient

With the page's original offset, [A108628](https://oeis.org/A108628) is

```math
a(n)=B(n+1,n,n+1),
```

where \(B(n_1,n_2,n_3)\) is the multivariate coefficient in Straub's
equation (24). With offset one, the claimed tower concerns
\(B(N,N-1,N)\). More directly, the OEIS identity below expresses it through
the ordinary and shifted diagonal Apéry sequences. Straub's theorem and
his shifted corollary give cubic towers for both when \(p\geq5\); division
by the \(p\)-adic unit \(5\) proves the offset-one A108628 tower only when
`p>5`.

The live OEIS statement also includes four separate half-index vanishing
congruences. The repository's corrected
[prime-five source audit](StraubPrimeFiveCoefficientPacket.md) records that
Straub's theorem already includes `p=5`, but passing through the displayed
identity

```math
a(n)=\frac{2B(n+1)-B(n)}5
```

loses one factor of \(5\), so the source theorem does not automatically
prove this affine shifted boundary. Accordingly A108628 is `partial`: its
ordinary `p>5` tower is source-closed, while the `p=5` shifted boundary and
the half-index packet remain explicit proof obligations.

### A208675: a shifted multivariate Apery coefficient

The live page identifies [A208675](https://oeis.org/A208675) exactly as

```math
a(n)=B(n,n-1,n-1)
```

in Straub's equation (24), and explicitly attributes its cubic tower for
all primes `p >= 5` to that multivariate theorem. This is an exact
published-source match, not a new finite-sum proof. The three coefficient
representations separately labelled conjectural on the OEIS page do not
alter the status of the supercongruence itself.

### A212334: ordinary tower closed, enhanced defect open

For [A212334](https://oeis.org/A212334), the live identity

```math
a(n)=\frac{A(n)+7A(n-1)}{12}
```

expresses the word-count sequence through the ordinary and shifted
fourth-order Apery sequence `A=A005259`. Their published cubic towers imply
the ordinary A212334 tower for every `p >= 5`, since `12` is a `p`-adic
unit throughout that range. The same page asks for the strictly stronger

```math
a(p)\equiv1\pmod {p^5},
\qquad
a(p^r)\equiv a(p^{r-1})\pmod {p^{3r+3}}
\quad(r\ge2).
```

Those enhanced pure-prime congruences do not follow from the cubic
baseline, so A212334 is `partial` rather than `published-source`.

## 3. Search-corpus records with no live open target

The following records remain useful anchors for formulas and
cross-references, but their live pages contain no Bala supercongruence
conjecture:

- [A001850](https://oeis.org/A001850), the central Delannoy numbers;
- [A006318](https://oeis.org/A006318), the large Schroder numbers;
- [A036917](https://oeis.org/A036917), the elliptic-integral coefficient
  sequence `1,8,88,...`; and
- [A143583](https://oeis.org/A143583), whose page states an ordinary
  `p^r` Gauss congruence but no stronger Bala conjecture.

These are labelled `no-explicit-open`. That label is deliberately narrow:
it says only that the reproducible live-page audit found no target to prove.
It does not assert that every arithmetic question about the sequence is
settled.

## 4. Ledger effect

This audit and its follow-ups remove twelve false starts from the open-work
columns:

- four move to `published-source`;
- four move to `partial`; and
- four move to `no-explicit-open`.

No finite experiment is used for any promotion.
