# Higher-degree finite-field box polynomials

**Status:** complete elementary theorem; exact finite-field checks; literature
priority unchecked.

## 1. Motivation

Kalinin's Gaussian Wolstenholme paper asks for analogues over extensions
of $\mathbb F_p$ of degree greater than two.  The $p$-adic
Wolstenholme question remains difficult, but the polynomial part admits
a uniform answer in every degree.

The result below contains the inert Gaussian identity

$$
\frac{X^{p^2-1}-1}{X^{2(p-1)}-1}
$$

as its two-dimensional case.

## 2. Statement

Let $K/\mathbb F_p$ be a finite extension of degree $d$, and fix an
ordered $\mathbb F_p$-basis

$$
\mathcal B=(e_1,\ldots,e_d).
$$

For $J\subseteq[d]$, put

$$
V_J=\operatorname{span}_{\mathbb F_p}\{e_j:j\in J\},
\qquad
L_J(X)=\prod_{v\in V_J}(X-v).
\tag{1}
$$

Thus $L_J$ is the subspace polynomial of $V_J$; in particular it is
a $p$-linearized polynomial.  Define the nonzero-coordinate box

$$
D_{\mathcal B}
=
\left\{
\sum_{j=1}^d a_je_j:a_j\in\mathbb F_p^\times
\right\}
\tag{2}
$$

and its root polynomial

$$
G_{\mathcal B}(X)=\prod_{z\in D_{\mathcal B}}(X-z).
\tag{3}
$$

### Theorem

In $K(X)$,

$$
G_{\mathcal B}(X)
=
\prod_{J\subseteq[d]}
L_J(X)^{\,(-1)^{d-|J|}}.
\tag{4}
$$

The rational expression on the right is therefore a polynomial.  More
explicitly,

$$
G_{\mathcal B}(X)
\prod_{\substack{J\subseteq[d]\\d-|J|\ {\rm odd}}}L_J(X)
=
\prod_{\substack{J\subseteq[d]\\d-|J|\ {\rm even}}}L_J(X).
\tag{5}
$$

## 3. Proof

Every $x\in K$ has a support

$$
\operatorname{supp}_{\mathcal B}(x)
=
\{j:\text{the $e_j$-coordinate of $x$ is nonzero}\}.
$$

The factor $X-x$ occurs in $L_J(X)$ precisely when
$\operatorname{supp}_{\mathcal B}(x)\subseteq J$.  Its total exponent
on the right side of (4) is consequently

$$
\sum_{J\supseteq\operatorname{supp}_{\mathcal B}(x)}
(-1)^{d-|J|}
=
\begin{cases}
1,&\operatorname{supp}_{\mathcal B}(x)=[d],\\
0,&\text{otherwise}.
\end{cases}
\tag{6}
$$

This is Boolean-lattice Möbius inversion.  Exactly the elements with
full support survive, proving (4).

## 4. The Gaussian and cubic cases

For $d=2$,

$$
G_{\mathcal B}(X)
=
\frac{L_{\{1,2\}}(X)L_\varnothing(X)}
{L_{\{1\}}(X)L_{\{2\}}(X)}.
\tag{7}
$$

Take $K=\mathbb F_p[i]$ with $p\equiv3\pmod4$ and
$\mathcal B=(1,i)$.  Then

$$
\begin{aligned}
L_{\{1,2\}}(X)&=X^{p^2}-X,\\
L_{\{1\}}(X)&=X^p-X,\\
L_{\{2\}}(X)&=X^p+X,\\
L_\varnothing(X)&=X.
\end{aligned}
$$

Equation (7) becomes

$$
G_{\mathcal B}(X)
=
\frac{X^{p^2-1}-1}{X^{2(p-1)}-1},
\tag{8}
$$

the polynomial formula used in the Gaussian Wolstenholme note.

For $d=3$, (4) reads

$$
G_{\mathcal B}(X)
=
\frac{
L_{\{1,2,3\}}(X)
L_{\{1\}}(X)L_{\{2\}}(X)L_{\{3\}}(X)}
{
L_\varnothing(X)
L_{\{1,2\}}(X)L_{\{1,3\}}(X)L_{\{2,3\}}(X)}.
\tag{9}
$$

This gives an explicit starting point for cubic-extension reciprocal
and product congruences.  The remaining $p$-adic problem is to choose
compatible characteristic-zero lifts and control the first few
reciprocal moments of a complete residue block.

## 5. Verification

The companion script constructs finite fields from irreducible
polynomials and checks (5) by direct polynomial multiplication in:

- $\mathbb F_9/\mathbb F_3$, with basis $(1,\alpha)$;
- $\mathbb F_{27}/\mathbb F_3$, with basis
  $(1,\alpha,\alpha^2)$.

Run:

```text
python verification/related/verify_higher_degree_box_polynomial.py
```

## 6. Scope

Equation (4) is an exact finite-field factorization, not yet a
higher-degree Wolstenholme supercongruence.  Its likely value is as the
correct algebraic interface for that harder question.  Because
subspace polynomials and Boolean Möbius inversion are classical, the
identity's literature priority should be treated as low until checked.
