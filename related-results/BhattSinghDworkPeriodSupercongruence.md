# A Bhatt--Singh seam: Dwork periods and multinomial scaling

**Status:** complete elementary deduction from the multinomial scaling lemma;
exact checks pass. This note makes no novelty claim. A literature-priority
search is still required.

## 1. Geometric source

Bhatt and Singh determine the \(F\)-pure-threshold tower of a smooth
Calabi--Yau hypersurface in characteristic \(p\). In their notation,

```math
\operatorname{fpt}(f)=1-\frac{h}{p},
\qquad
G_f(z)=\sum_{e\ge0}\mu_f(p^e)z^e
=\frac{1-hz}{1-pz}.
\qquad\text{(1)}
```

For the Fermat hypersurface of degree \(d\) in
\(\mathbf P^{d-1}\), their Example 4.2 gives

```math
h\equiv p-1\pmod d,\qquad 0\le h\le d-2.
\qquad\text{(2)}
```

The associated diagonal period sequence is the equal-part multinomial

```math
A_d(n)=\frac{(dn)!}{(n!)^d}.
\qquad\text{(3)}
```

It is also a constant-term sequence:

```math
A_d(n)=\operatorname{CT}
\left(
\frac{(x_1+\cdots+x_d)^d}{x_1\cdots x_d}
\right)^n.
\qquad\text{(4)}
```

The geometry motivates the sequence. The supercongruence below is an
elementary consequence of multinomial arithmetic.

## 2. An all-prime adjacent-scale bound

For a prime \(p\), put

```math
\epsilon_p=
\begin{cases}
2,&p=2,\\
1,&p=3,\\
0,&p\ge5.
\end{cases}
```

### Theorem

For every \(d\ge2\), \(n\ge1\), \(r\ge1\), and prime \(p\),

```math
v_p\!\left(A_d(np^r)-A_d(np^{r-1})\right)
\ge
3\bigl(r+v_p(n)\bigr)-\epsilon_p+s_p(n)v_p(d!).
\qquad\text{(5)}
```

In particular,

```math
A_d(np^r)\equiv A_d(np^{r-1})
\pmod {p^{\,3r-\epsilon_p+v_p(d!)}}.
\qquad\text{(6)}
```

The digit-sensitive term \(s_p(n)v_p(d!)\) comes from divisibility already
present in the lower-scale period. Since \(s_p(n)\ge1\), it supplies the
uniform gain \(v_p(d!)\) displayed in (6).

### Proof

Set \(m=np^{r-1}\). The multinomial scaling lemma used in the A183068 proof
gives

```math
v_p\!\left(\frac{A_d(pm)}{A_d(m)}-1\right)
\ge 3\bigl(v_p(m)+1\bigr)-\epsilon_p
=3\bigl(r+v_p(n)\bigr)-\epsilon_p.
\qquad\text{(7)}
```

The sign qualification at \(p=2\) causes no problem. When \(v_2(m)\ge1\)
the exceptional sign cannot occur in the equal-index specialization; when
\(v_2(m)=0\), the modulus supplied by (7) is \(2\), where
\(-1\equiv1\).

It remains to record a uniform lower bound for \(A_d(m)\). Let \(s_p(a)\)
be the sum of the base-\(p\) digits of \(a\). Legendre's formula gives

```math
v_p(A_d(m))
=\frac{d\,s_p(m)-s_p(dm)}{p-1}.
\qquad\text{(8)}
```

Writing \(m\) as a sum of \(s_p(m)\) powers of \(p\), with repetition,
and using subadditivity of digit sums gives

```math
s_p(dm)\le s_p(d)s_p(m).
```

Since multiplication by \(p^{r-1}\) only appends zero digits,
\(s_p(m)=s_p(n)\). Consequently,

```math
\begin{aligned}
v_p(A_d(m))
&\ge
s_p(m)\frac{d-s_p(d)}{p-1}\\
&=s_p(n)v_p(d!).
\end{aligned}
\qquad\text{(9)}
```

Finally,

```math
A_d(pm)-A_d(m)
=A_d(m)\left(\frac{A_d(pm)}{A_d(m)}-1\right).
```

Adding the bounds (7) and (9) proves (5). \(\square\)

## 3. Small-prime consequences

The theorem makes the small-prime compensation explicit:

| Degree | \(p=2\) exponent | \(p=3\) exponent | \(p\ge5\) exponent |
| ---: | ---: | ---: | ---: |
| \(d=2\) | \(3(r+v_2(n))-1\) | \(3(r+v_3(n))-1\) | \(3(r+v_p(n))\) |
| \(d=3\) | \(3(r+v_2(n))-1\) | \(3(r+v_3(n))\) | \(3(r+v_p(n))\) |
| \(d=4\) | \(3(r+v_2(n))+1\) | \(3(r+v_3(n))\) | \(3(r+v_p(n))\) |

These are lower bounds, not assertions of exact valuation.

## 4. What this does and does not add

Bhatt--Singh already prove the threshold formula (1) and record the Fermat
case (2). Classical Jacobsthal--Kazandzidis theory supplies (7). The
contribution of this note is the short synthesis producing the
digit-sensitive \(s_p(n)v_p(d!)\) gain in (5), its uniform corollary (6),
and their placement next to the Calabi--Yau threshold tower.

The more ambitious target is not (5), which is termwise. It is a
first-order Cartier lift for the full Dwork-family period and its Hasse
polynomial, analogous to the rank-one level-\(11\) target in the Cooper
note. That problem requires aggregate Frobenius cancellation and is not
proved here.

## References

- B. Bhatt and A. K. Singh,
  [*The \(F\)-pure threshold of a Calabi--Yau hypersurface*](https://arxiv.org/abs/1307.1171),
  especially Theorem 4.1 and Example 4.2.
- G. S. Kazandzidis,
  [*Congruences on the binomial coefficients*](https://eudml.org/doc/238547).
- [A183068 proof, Lemma 2](../PROOF.md#3-multinomial-scaling).

## Reproducibility

Run

```text
python verification/related/verify_dwork_period_supercongruence.py
```

The script checks the digit-sum identity, the digit-sensitive lower bound,
and (5) by exact integer arithmetic in a finite grid.
