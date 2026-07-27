# Constant-spectrum convolution towers: determinant and Pfaffian

## Status

This note upgrades the determinant and Pfaffian character-sum theorems to
every additive convolution power. The proof is elementary Fourier inversion.
It produces two infinite sharp supercongruence families and an exact mixing
law.

The one-invariant character sums and the finite Fourier machinery are
classical or proved in the preceding notes. The all-convolution formulas and
their sharp adjacent-extension valuations are new deductions within this
repository. Literature priority is preliminary.

## Orbit-spectrum compression

The determinant, Pfaffian, and hyperdeterminant examples are instances of one
finite Fourier principle.

Let a finite group \(K\) act by automorphisms on a finite abelian group \(G\),
and let \(c:G\to\mathbf C\) be constant on the \(K\)-orbits. The induced
action on the character group \(\widehat G\) partitions it into orbits
\(\Omega_1,\ldots,\Omega_s\). Choose \(\gamma_i\in\Omega_i\). If
\(\mathcal O_1,\ldots,\mathcal O_t\) are the orbits in \(G\), choose
\(x_j\in\mathcal O_j\) and put

\[
\mathcal A_{ji}
=
\sum_{\gamma\in\Omega_i}\gamma(-x_j).
\tag{A}
\]

### Proposition (orbit-spectrum convolution compiler)

For every \(\ell\geq1\),

\[
\boxed{
c^{*\ell}(x_j)
=
\frac1{|G|}
\sum_{i=1}^{s}
\mathcal A_{ji}\widehat c(\gamma_i)^\ell.
}
\tag{B}
\]

### Proof

The invariance of \(c\) makes \(\widehat c\) constant on each dual orbit.
Group Fourier inversion gives

\[
c^{*\ell}(x_j)
=
\frac1{|G|}
\sum_{\gamma\in\widehat G}
\gamma(-x_j)\widehat c(\gamma)^\ell.
\]

Grouping the characters by \(\Omega_i\) proves (B). \(\square\)

Once the orbit matrix \(\mathcal A\) and the \(s\) spectral values are known,
the compressed representation of \(c^{*\ell}\) requires \(s\) scalar
exponentiations and a \(t\)-by-\(s\) matrix multiplication. Repeated
squaring gives arithmetic cost

\[
O(s\log\ell+st),
\tag{C}
\]

independent of \(|G|\), apart from the cost of writing out all \(|G|\)
individual values. This is an exact structured-convolution shortcut, not an
improvement to the general FFT.

For the additive group of \(\mathbf F_q\), determinant and Pfaffian use the
full multiplicative action and have two orbits: zero and nonzero. The
hyperdeterminant uses the square subgroup and has three: zero, nonzero
square, and nonsquare. Thus the three invariant families are one
orbit-spectrum calculation with different orbit matrices and low-degree
polynomials.

## 1. A constant-spectrum theorem

Let \(V_q\) be a finite set of size \(q^D\), let

\[
f_q:V_q\longrightarrow\mathbf F_q,
\]

and fix a nontrivial additive character \(\psi\). Suppose that

\[
\mathcal S(q)
=
\sum_{x\in V_q}\psi(af_q(x))
\tag{1}
\]

is independent of \(a\in\mathbf F_q^\times\). Assume further that

\[
\mathcal S(q)=q^E U(q),
\qquad
U(X)\in\mathbf Z[X],
\qquad
U(0)\in\{1,-1\},
\tag{2}
\]

and \(D>E\).

For \(\ell\geq1\), define

\[
N_{\ell,t}(q)
=
\#\left\{
(x_1,\ldots,x_\ell)\in V_q^\ell:
f_q(x_1)+\cdots+f_q(x_\ell)=t
\right\}.
\tag{3}
\]

### Theorem 1 (constant-spectrum convolution compiler)

For every prime power \(q\),

\[
\boxed{
N_{\ell,0}(q)
=
\frac{q^{D\ell}+(q-1)\mathcal S(q)^\ell}{q},
}
\tag{4}
\]

whereas every \(t\neq0\) has the same fiber

\[
\boxed{
N_{\ell,t}(q)
=
\frac{q^{D\ell}-\mathcal S(q)^\ell}{q}.
}
\tag{5}
\]

For every prime \(p\) and \(r\geq2\), both fiber classes satisfy

\[
\boxed{
v_p\!\left(
N_{\ell,\star}(p^r)-N_{\ell,\star}(p^{r-1})
\right)
=(E\ell-1)(r-1),
}
\tag{6}
\]

where \(\star\) is either \(0\) or the common nonzero class. In particular,
the exponent in (6) is sharp.

### Proof

Fourier inversion gives

\[
N_{\ell,t}(q)
=
\frac1q
\sum_{a\in\mathbf F_q}
\psi(-at)
\left(
\sum_{x\in V_q}\psi(af_q(x))
\right)^\ell.
\tag{7}
\]

The \(a=0\) term is \(q^{D\ell}\). For \(t=0\), the remaining \(q-1\)
terms all equal \(\mathcal S(q)^\ell\), proving (4). For \(t\neq0\),

\[
\sum_{a\neq0}\psi(-at)=-1,
\]

which proves (5).

Put \(L=E\ell-1\). Equations (2), (4), and (5) write either fiber as

\[
N_{\ell,\star}(q)=q^L W_\star(q)
\tag{8}
\]

with \(W_\star\in\mathbf Z[q]\) and

\[
W_\star(0)=-U(0)^\ell\in\{1,-1\}.
\tag{9}
\]

Indeed, the remaining term \(q^{D\ell-1}\) has degree strictly larger than
\(L\), because \(D>E\). Therefore

\[
\begin{aligned}
&N_{\ell,\star}(p^r)-N_{\ell,\star}(p^{r-1})\\
&\quad=
p^{L(r-1)}
\left(
p^L W_\star(p^r)-W_\star(p^{r-1})
\right).
\end{aligned}
\]

The parenthesized factor is \(-W_\star(0)\) modulo \(p\), hence is a unit.
This proves (6). \(\square\)

## 2. Determinant convolution towers

For \(n\geq2\), put

\[
D_n=n^2,
\qquad
E_n=\frac{n^2-n+2}{2},
\tag{10}
\]

and let

\[
\mathcal S_n(q)
=
\sum_{M\in M_n(\mathbf F_q)}\psi(\det M).
\]

The determinant character-sum theorem gives

\[
\mathcal S_n(q)
=q^{n^2}
-q^{E_n}\prod_{k=2}^{n}(q^k-1)
=q^{E_n}U_n(q),
\qquad
U_n(0)=(-1)^n.
\tag{11}
\]

### Corollary 2

Let \(D_{\ell,t}^{(n)}(q)\) count \(\ell\)-tuples of \(n\)-by-\(n\)
matrices whose determinants sum to \(t\). Equations (4) and (5), with
\(\mathcal S=\mathcal S_n\), give all of its fibers. Moreover,

\[
\boxed{
v_p\!\left(
D_{\ell,\star}^{(n)}(p^r)
-D_{\ell,\star}^{(n)}(p^{r-1})
\right)
=
\left(
\ell\frac{n^2-n+2}{2}-1
\right)(r-1)
}
\tag{12}
\]

for every prime \(p\), \(r\geq2\), and either fiber class.

## 3. Pfaffian convolution towers

For \(m\geq2\), put

\[
D_m^{\mathrm{alt}}=m(2m-1),
\qquad
F_m=m^2-m+1,
\tag{13}
\]

and let

\[
\mathcal P_m(q)
=
\sum_{A\in\operatorname{Alt}_{2m}(\mathbf F_q)}
\psi(\operatorname{Pf}(A)).
\]

The Pfaffian theorem gives

\[
\mathcal P_m(q)
=q^{m(2m-1)}
-q^{F_m}\prod_{j=2}^{m}(q^{2j-1}-1)
=q^{F_m}V_m(q),
\qquad
V_m(0)=(-1)^m.
\tag{14}
\]

### Corollary 3

Let \(P_{\ell,t}^{(m)}(q)\) count \(\ell\)-tuples of alternating
\(2m\)-by-\(2m\) matrices whose Pfaffians sum to \(t\). Equations (4) and
(5), with \(\mathcal S=\mathcal P_m\), give every fiber. Moreover,

\[
\boxed{
v_p\!\left(
P_{\ell,\star}^{(m)}(p^r)
-P_{\ell,\star}^{(m)}(p^{r-1})
\right)
=
\left(\ell(m^2-m+1)-1\right)(r-1)
}
\tag{15}
\]

for every prime \(p\), \(r\geq2\), and either fiber class.

The characteristic-two Pfaffian convention is the same as in the preceding
note: an alternating matrix is symmetric with zero diagonal, and the
integral Pfaffian polynomial remains valid.

## 4. Exact Fourier mixing

Let \(\mu_q\) be the distribution of \(f_q(x)\) for uniform \(x\in V_q\)
and put

\[
\beta_q=\frac{\mathcal S(q)}{q^D}.
\tag{16}
\]

Every nontrivial Fourier coefficient of \(\mu_q\) equals \(\beta_q\).
Equations (4) and (5) therefore give the exact identity

\[
\boxed{
\left\|\mu_q^{*\ell}-U_q\right\|_{\mathrm{TV}}
=
\frac{q-1}{q}|\beta_q|^\ell,
}
\tag{17}
\]

where \(U_q\) is uniform on \(\mathbf F_q\).

For determinant,

\[
\beta_q
=1-\prod_{k=2}^{n}(1-q^{-k}),
\tag{18}
\]

and for Pfaffian,

\[
\beta_q
=1-\prod_{j=2}^{m}(1-q^{-(2j-1)}).
\tag{19}
\]

Thus convolution amplifies determinant's \(q^{-2}\) bias and Pfaffian's
\(q^{-3}\) bias exponentially in \(\ell\). This is an exact scalar
pushforward mixing theorem, not a claim of cryptographic extraction or an
ambient restriction estimate.

### Algorithmic corollary

For either invariant, the pair

\[
\bigl(N_{\ell,0}(q),N_{\ell,\ne0}(q)\bigr)
\]

is the complete output distribution. After evaluating the one-sample
character sum, equations (4) and (5) compute this pair with
\(O(\log\ell)\) integer multiplications by repeated squaring. Materializing
all \(q\) output values costs \(O(q)\), which is optimal merely to write
them down; no length-\(q\) FFT is required.

The analogous hyperdeterminant packet has three output classes and the same
constant-size property. This can inform algorithms whenever a signal or
phase distribution has an exact low-orbit spectrum. It does not imply a
faster general DFT, an improved audio codec, or a circadian-clock model
without an additional application-specific reduction to such a spectrum.

## 5. Place in the supercongruence program

The original one-sample character sums supplied one sharp exponent. The
convolution compiler supplies infinitely many:

| invariant | convolution length | sharp adjacent exponent |
| --- | ---: | ---: |
| determinant \(n\times n\) | \(\ell\) | \(\bigl(\ell E_n-1\bigr)(r-1)\) |
| Pfaffian on \(\operatorname{Alt}_{2m}\) | \(\ell\) | \(\bigl(\ell F_m-1\bigr)(r-1)\) |

The subtraction of \(1\) is the Fourier-normalization cost in (4) and (5).
The rest of the exponent is additive in the number of independent invariant
outputs. This makes the connection between Fourier mixing and
supercongruence exact: the high-degree end controls Archimedean decay, while
the low-degree end controls the \(p\)-adic tower.

## 6. Verification and literature boundary

The checker
[`verify_determinant_pfaffian_convolution.py`](../verification/related/verify_determinant_pfaffian_convolution.py)
verifies:

1. cyclic convolution against the exact prime-field fibers;
2. formulas (4) and (5);
3. conservation of the full tuple count;
4. the sharp valuations (12) and (15), including \(p=2\); and
5. the exact total-variation identity (17).

Run:

```text
python verification/related/verify_determinant_pfaffian_convolution.py
```

Nearby references include:

- P. Diaconis and L. Saloff-Coste,
  [Convolution powers of complex functions on
  \(\mathbf Z\)](https://arxiv.org/abs/1205.6490), for the general
  Fourier-analysis viewpoint on repeated convolution; and
- R. Cluckers and A. Herremans,
  [The fundamental theorem of prehomogeneous vector spaces modulo
  \(p^m\)](https://doi.org/10.24033/bsmf.2543), for Fourier transforms of
  relative invariants over finite local rings.

The determinant and Pfaffian source notes cite the closer finite-field rank
and prehomogeneous-vector-space infrastructure. A targeted search for the
combined fingerprints “determinant convolution fibers,” “Pfaffian
convolution fibers,” and the displayed sharp exponents found no direct
match. This is preliminary priority evidence only.
