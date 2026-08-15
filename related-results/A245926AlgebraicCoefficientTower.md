# The algebraic coefficient identity and quadratic tower for A245926

**Status:** complete elementary proof candidate; exact checks pass;
independent review and literature priority remain open.

**Source boundary:** [OEIS A245926](https://oeis.org/A245926) gives the
algebraic generating function, records the Legendre-polynomial formula, and
conjectures both the coefficient representation and the supercongruence
proved below. The argument is self-contained and does not assume the
conjectural representation.

## 1. Statement

Let

~~~math
A(z)=\sqrt{
\frac{1-z+\sqrt{1-14z+z^2}}
     {2(1-14z+z^2)}}
=\sum_{N\geq0}a(N)z^N,
\qquad A(0)=1.
\tag{1}
~~~

Thus \(a(N)\) is OEIS A245926. Put

~~~math
\Phi(x)=
\frac{(1+x+x^2)(1+x)^2}{(1-x)^2}.
\tag{2}
~~~

### Theorem

For every \(N\geq0\),

~~~math
\boxed{
a(N)=[x^N]\Phi(x)^N.
}
\tag{3}
~~~

Consequently, for every prime \(p\geq5\) and positive integers \(n,r\),

~~~math
\boxed{
a(np^r)\equiv a(np^{r-1})\pmod {p^{2r}}.
}
\tag{4}
~~~

This proves both the previously conditional coefficient formula and the
quadratic supercongruence stated on A245926.

## 2. A diagonal-to-reversion lemma

We use a standard form of Lagrange inversion, included here to fix every
normalization. Let \(\phi(x)\in1+x\mathbb Q[[x]]\), and let \(y=y(z)\) be
the unique solution of

~~~math
y=z\phi(y).
\tag{5}
~~~

Then

~~~math
\sum_{N\geq0}[x^N]\phi(x)^N z^N
=\frac{z y'(z)}{y(z)}.
\tag{6}
~~~

Indeed, Lagrange--Bürmann inversion gives

~~~math
\log\frac{y(z)}z
=\sum_{N\geq1}\frac{z^N}{N}[x^N]\phi(x)^N.
\tag{7}
~~~

Applying \(z\,d/dz\) to (7), and then adding the constant term, gives (6).

## 3. Proof of the coefficient identity

Apply the lemma with \(\phi=\Phi\). Make the rational change of variable

~~~math
u=\frac{1+y}{1-y},
\qquad v=u^2.
\tag{8}
~~~

Since \(y=(u-1)/(u+1)\), direct simplification of \(y=z\Phi(y)\) gives

~~~math
z=\frac{v-1}{v(3v+1)}.
\tag{9}
~~~

Equivalently,

~~~math
3zv^2+(z-1)v+1=0,
\tag{10}
~~~

where the branch selected by \(y(0)=0\) satisfies \(v(0)=1\). If

~~~math
D=1-14z+z^2,
\tag{11}
~~~

then (10) yields

~~~math
v=\frac{1-z-\sqrt D}{6z}.
\tag{12}
~~~

Let

~~~math
B(z)=\sum_{N\geq0}[x^N]\Phi(x)^N z^N.
~~~

By (6), \(B=zy'/y\). Differentiating \(y=(u-1)/(u+1)\), using \(v=u^2\),
and then differentiating (9), gives

~~~math
B(z)
=\frac{zv'}{\sqrt v\,(v-1)}
=\frac{\sqrt v\,(3v+1)}{1+6v-3v^2}.
\tag{13}
~~~

The following two identities are immediate from (9):

~~~math
D=\frac{(3v^2-6v-1)^2}{v^2(3v+1)^2},
\qquad
\sqrt D=-\frac{3v^2-6v-1}{v(3v+1)}.
\tag{14}
~~~

The signs in (14) are fixed by \(v(0)=1\) and \(\sqrt D=1+O(z)\).
Squaring (13) and substituting (9) and (14) now gives

~~~math
B(z)^2=\frac{1-z+\sqrt D}{2D}.
\tag{15}
~~~

Both \(A\) and \(B\) have constant term one, so (1) and (15) imply \(A=B\).
This proves (3).

## 4. A cyclotomic-support lemma

The congruence uses only the following elementary coefficient principle.

### Lemma

Let

~~~math
\phi(x)=\prod_{d\in S}(1-x^d)^{e_d},
\qquad e_d\in\mathbb Z,
\tag{16}
~~~

where \(S\) is a finite set of positive integers. Fix integers \(c\geq0\)
and \(s\geq1\), and put

~~~math
C(N)=[x^{cN}]\phi(x)^{sN}.
\tag{17}
~~~

If \(p\geq3\) is prime and \(p\nmid d\) for every \(d\in S\), then

~~~math
C(np^r)\equiv C(np^{r-1})\pmod {p^{2r}}
\tag{18}
~~~

for all positive \(n,r\).

### Proof

Write

~~~math
U_p(t)=\sum_{\substack{j\geq1\\p\nmid j}}\frac{t^j}{j},
\qquad
L_p(x)=-s\sum_{d\in S}e_dU_p(x^d).
\tag{19}
~~~

Cancellation of the terms indexed by multiples of \(p\) gives the exact
formal identity

~~~math
\frac{\phi(x)^{sp}}{\phi(x^p)^s}=\exp\bigl(pL_p(x)\bigr).
\tag{20}
~~~

Set \(N=np^r\), \(M=N/p\), and \(G(x)=x^{-c}\phi(x)^s\). Then

~~~math
C(N)-C(M)
=\operatorname{CT}G(x^p)^M
 \left(\exp\bigl(NL_p(x)\bigr)-1\right).
\tag{21}
~~~

Every exponent in \(G(x^p)^M\) is divisible by \(p\). On the other hand,
every exponent \(dj\) in \(L_p\) is prime to \(p\), because \(p\nmid d\)
and \(p\nmid j\). The linear term in (21) therefore has constant term zero.

For every \(h\geq2\),

~~~math
v_p\!\left(\frac{N^h}{h!}\right)
\geq hr-(h-2)
=2r+(h-2)(r-1)
\geq2r.
\tag{22}
~~~

Here \(v_p(h!)\leq h-2\) for \(p\geq3\). The coefficients of \(L_p\) are
\(p\)-integral, so every term of exponential degree at least two in (21)
is divisible by \(p^{2r}\). Only finitely many degrees can contribute to
the constant term, and (18) follows. \(\square\)

## 5. Application to A245926

The kernel in (2) has the cyclotomic factorization

~~~math
\Phi(x)
=\frac{(1-x^3)(1-x^2)^2}{(1-x)^5}.
\tag{23}
~~~

Use the lemma with

~~~math
S=\{1,2,3\},
\qquad(e_1,e_2,e_3)=(-5,2,1),
\qquad c=s=1.
~~~

Every prime \(p\geq5\) is prime to all three step sizes. Equations
(3), (18), and (23) therefore prove (4).

The exclusion of the small primes is sharp at the first level. Indeed,

~~~math
a(2)-a(1)=46\not\equiv0\pmod4,
\qquad
a(3)-a(1)=582\not\equiv0\pmod9.
\tag{24}
~~~

This matches the support obstruction: at \(p=2\) or \(3\), one of the
cyclotomic steps in (23) lands on the \(p\)-sublattice, so the exact linear
vanishing used above is unavailable.

## 6. Verification

Run

~~~text
python verification/related/verify_a245926_algebraic_coefficient.py
~~~

The exact checker verifies the published initial values, the two kernel
factorizations, the coefficient identity against the algebraic recurrence,
the rational identities used in the reversion calculation, the support and
factorial-valuation lemmas, adjacent towers through level three on a
prime/index grid, and the exact failures at two and three. These calculations
are regression evidence; the proof
above establishes the general theorem.
