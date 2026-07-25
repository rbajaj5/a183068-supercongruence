# Gaussian citation network: boundary report

**Status:** rigorous reductions and exact search, not a solution of the
remaining global problems.

This note records what survived attempts on the two highest-risk branches
of the Gaussian power-sum citation network.  Its purpose is to prevent
partial observations from being confused with solved conjectures.

## 1. Gaussian Erdős--Moser equation

Fortuny Ayuso, Grau, and Oller-Marcén propose the Gaussian analogue

```math
G_k(m-1)=(m+mi)^k,
\qquad
G_k(n)=\sum_{1\leq a,b\leq n}(a+bi)^k.
\tag{1}
```

Their search for $k,m<100$ found only $(k,m)=(2,3)$.

Put $n=m-1$.  Their Gaussian von Staudt theorem determines
$G_k(n)\pmod n$, while the right side of (1) is congruent to
$(1+i)^k\pmod n$.  This gives the following elementary restrictions.

### Proposition 1

If (1) holds, then:

1. there is no solution with $k=1$;
2. if $k>1$ is odd, then
   ```math
   m-1=2^a\quad\text{for some }a\geq2;
   \tag{2}
   ```
3. if $k\equiv2\pmod4$, then $m-1$ is a power of $2$, and
   ```math
   m-1\leq2^{k/2}.
   \tag{3}
   ```

### Proof

For odd $k>1$, the Gaussian von Staudt formula gives

```math
G_k(n)\equiv
\begin{cases}
\dfrac n2(1+i)\pmod n,&n\equiv2\pmod4,\\
0\pmod n,&\text{otherwise}.
\end{cases}
\tag{4}
```

If $n\equiv2\pmod4$, the two components on the first line are odd
modulo $2$, while the two components of $(1+i)^k$ are even; hence
this case is impossible.  Otherwise, (4) implies that $n$ divides
both components of

```math
(1+i)^k=\pm2^{(k-1)/2}(1\pm i).
```

Thus $n$ is a power of $2$.  The case $n=1$ would assert
$(1+i)^k=2^k(1+i)^k$, so $a\geq2$.  The case $k=1$ follows
directly from

```math
G_1(n)=\frac{n^2(n+1)}2(1+i).
```

If $k\equiv2\pmod4$, the von Staudt residue is real, while
$(1+i)^k$ is purely imaginary with nonzero component
$\pm2^{k/2}$.  Therefore $n\mid2^{k/2}$, proving (3).

### Proposition 2

The only solution with $k=2$ is $(k,m)=(2,3)$.

### Proof

A direct power-sum calculation gives

```math
G_2(n)
=
2i\left(\sum_{a=1}^n a\right)^2
=
\frac{i n^2(n+1)^2}{2}.
\tag{5}
```

The right side of (1) is $2i(n+1)^2$.  Equality is therefore
equivalent to $n^2=4$, so $n=2$ and $m=3$.

Finally, the triangle inequality excludes a complementary region:

```math
|G_k(n)|
\leq
n^2(\sqrt2\,n)^k
<
(\sqrt2(n+1))^k
\tag{6}
```

whenever

```math
k>\frac{2\log n}{\log(1+1/n)}.
\tag{7}
```

The companion search verifies that $(2,3)$ remains the only solution
for $1\leq k,m\leq180$.  None of these observations resolves the
cases $k\equiv0\pmod4$ or the surviving power-of-two families.

## 2. Wolstenholme-prime branch

Kalinin--Zottor prove, for $p\equiv3\pmod4$,

```math
v_p(\mathcal G_p(p))\geq6
\quad\Longleftrightarrow\quad
p\mid\operatorname{num}(B_{p-3}).
\tag{8}
```

The right side is exactly the classical definition of a Wolstenholme
prime.  Only

```math
16843,\qquad2124679
```

are known, and Booker--Hathi--Mossinghoff--Trudgian found no further
examples below $10^{11}$.

Thus (8) supplies a useful Gaussian interpretation but not an
independent low-complexity attack.  Searching farther or proving
infinitude would be a major computational or Bernoulli-distribution
project, not a continuation of the affine-orbit method.

## 3. Review recommendation

- Keep the Gaussian Erdős--Moser reduction as a research lead, not a
  paper claim.
- Do not allocate proof-review time to the Wolstenholme-prime branch
  without a genuinely new Bernoulli or search algorithm.
- Concentrate review on the solved polynomial and Gaussian Lucas
  conjectures, whose proofs are finite and independently auditable.

## 4. Sources

- P. Fortuny Ayuso, J. M. Grau, and A. M. Oller-Marcén,
  *A von Staudt-type result for sums of powers in
  $\mathbb Z_n[i]$*, *Monatshefte für Mathematik* 178 (2015).
- A. R. Booker, S. Hathi, M. J. Mossinghoff, and T. S. Trudgian,
  *Wolstenholme and Vandiver primes*, arXiv:2101.11157.
- N. Kalinin and F. S. Zottor, arXiv:2602.00206.
