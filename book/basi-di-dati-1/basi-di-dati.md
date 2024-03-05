<!-- --- -->
<!-- marp: true -->
<!-- paginate: true -->
<!-- math: katex -->
<!-- footer: "**Sapienza** università di Roma, **Dipartimento di Informatica**" -->
<!-- --- -->

<!-- https://www.compart.com/en/unicode/U+2288 -->

<!-- <style> -->
<!-- 	section { -->
<!-- 		font-size: 1.5rem; -->
<!-- 	} -->
<!---->
<!-- 	section.first > h1 { -->
<!-- 		align-self: center; -->
<!-- 	} -->
<!---->
<!-- 	section.first::after, section.first > header, section.first > footer { -->
<!-- 		color: white !important; -->
<!-- 	} -->
<!---->
<!-- 	section:not(.first) { -->
<!-- 		justify-content: flex-start; -->
<!-- 	} -->
<!---->
<!-- 	section.first > footer { -->
<!-- 		font-family: unset; -->
<!-- 		font-size: 1.2rem -->
<!-- 	} -->
<!---->
<!-- 	header, footer  { -->
<!-- 		font-family: "Felix Titling"; -->
<!-- 		font-size: 1rem -->
<!-- 	} -->
<!---->
<!-- 	h1 { -->
<!-- 		color: #822433; -->
<!-- 	} -->
<!---->
<!-- 	code { -->
<!-- 		font-family: "CascadiaCode Nerd Font"; -->
<!-- 		tab-size: 4; -->
<!-- 	} -->
<!---->
<!-- 	table { -->
<!-- 		align-self: center; -->
<!-- 	} -->
<!---->
<!-- 	/* table, marp-pre { -->
<!-- 		margin-top: 1rem; -->
<!-- 		margin-bottom: 2rem; -->
<!-- 	} */ -->
<!---->
<!-- 	marp-pre { -->
<!-- 		margin-top: 1rem; -->
<!-- 		margin-bottom: 2rem; -->
<!-- 	} -->
<!---->
<!-- 	th > p { -->
<!-- 		margin: 0; -->
<!-- 		padding: 0; -->
<!-- 	} -->
<!-- </style> -->

# Databases 



<img alt="xkcd drop table meme" src="https://imgs.xkcd.com/comics/exploits_of_a_mom.png"/>

Download the [introduction presentation](./dbms.pdf)

View the <a target="_blank" href="./basi-di-dati-presentazione.html">presentation on proofs</a> or [download it](./basi-di-dati.pdf). The links refer to the [slides of prof. Perelli](https://giuseppeperelli.github.io/teaching/2023-24_basi_di_dati/) and don't work on the website: you have to download the [pdf](./basi-di-dati.pdf) in the same folder with the course's slides for the links to work.

<!-- _backgroundColor: #822433 -->
<!-- _color: white -->
<!-- _class: first  -->

---

# Schema

<!-- TODO: relational algebra -->
<!-- TODO: define domain -->
<!-- TODO: define dom : names -> Domains -->
<!-- TODO: define attribute -->

An **attribute** is a $(\text{name}, \text{domain})$ pair; we can define the $dom()$ function on a set of names, which associates to each **name** a specific **domain** _(different attributes can have the same domain)_

$$
\begin{align*}
    dom : \set{\text{name}_1, ..., \text{name}_n} & \to \set{\text{domain}_1, ..., \text{domain}_k}\\
    \text{name}_i &\mapsto \text{domain}_j


\end{align*}
$$

[PDF 7 slide 2](07%20-%20functional%20dependencies.pdf#page=2)

A **relation schema** $R = \set{A_1, A_2, ..., A_n}$ is a set of attributes

---

# Tuples & instances

[PDF 7 slide 3](07%20-%20functional%20dependencies.pdf#page=3) Given a relation schema $R = A_1 A_2 ... A_n$, a **tuple** $t$ on $R$ is a function such that

$$
\begin{align*}
	t : R &\to \bigcup\limits_{i = 1}^n dom(A_i)\\
	A_i &\mapsto a \in dom(A_i)
\end{align*}
$$

Given a relation schema $R$, a subset $X \subseteq R$ and $t$ a tuple on $R$, the **reduction** of $t$ on $X$ is defined as

$$t[X] = \set{(A, t[A]) \mid A \in X}$$

<!-- $$
t : R \to \bigcup\limits_{i = 1}^n dom(A_i) : A_i \mapsto a \in dom(A_i)
$$ -->

[PDF 7 slide 4](07%20-%20functional%20dependencies.pdf#page=4) Given a relation schema $R$, a subset $X \subseteq R$ and $t_1, t_2$ tuples on $R$

$$ t_1[X] = t_2[X] \iff t_1[A] = t_2[A] \; \forall A \in X$$

<!-- If $X \subseteq R$ and $t_1$ and $t_2$ are two tuples on $R$, $t_1$ and $t_2$ coincide on $X$ $(t_1[X] = t_2[X])$ if $\forall A \in X t_1[A] = t_2[A]$ -->

<!-- If $X \subseteq R$ and $t_1$ and $t_2$ are two tuples on $R$, if $\forall A \in X, t_1[A] = t_2[A] \implies t_1[X] = t_2[X]$ -->

[PDF 7 slide 5](07%20-%20functional%20dependencies.pdf#page=5) Given a relation schema $R$ and $t_1, t_2, ..., t_k$ tuples on $R$, a set $r = \set{t_1, t_2, ..., t_k}$ is an **instance** of $R$

---

# Functional dependencies

[PDF 7 slide 6](07%20-%20functional%20dependencies.pdf#page=6)

<!-- Given a relation schema $R$, a functional dependency on $R$ is an ordered pair of non-empty subsets X, Y ⊆ R -->

<!-- Given a relation schema $R$ and $X, Y \subseteq R : X \neq \varnothing \land Y \neq \varnothing \implies (X, Y) = X \to Y$ is a functional dependency on $R$ -->

Given a relation schema $R$ and $X, Y \in \mathcal{P}(R) \setminus \set{\varnothing}$ we have that $(X, Y)$ is a **functional dependency** on $R$ _(noted as $X \to Y$)_

[PDF 7 slide 7](07%20-%20functional%20dependencies.pdf#page=7)

Given a relation schema $R$ and a functional dependency $X \to Y$ defined on $R$ we say that an **instance** $r$ of $R$ **satisfies** the functional dependency $X \to Y$ if

$$
\forall t_1, t_2 \in r \quad t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y]
$$

<!-- > NOTE: the definition of functional dependency doesn't depend on the concept of instance, as a functional dependency is just an ordered pair of non-empty subsets of $R$; it's important to understand the concept that $r$ may or may not satisfy $X \to Y$ -->

---

# Instance legality & closure

[PDF 7 slide 14](07%20-%20functional%20dependencies.pdf#page=14)

Given a relation schema $R$ and a set $F$ of functional dependencies defined on $R$, an **instance** $r$ of $R$ is **legal** if it satisfies every dependency in $F$

$$\forall X \to Y \in F \quad \forall t_1, t_2 \in r \quad t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y]$$

<!-- it satisfies all dependencies in $F$ -->

[PDF 7 slide 20](07%20-%20functional%20dependencies.pdf#page=20)

Given a relation schema $R$ and a set $F$ of functional dependencies defined on $R$, the closure of $F$ is the **set of functional dependencies** that are satisfied by every **legal instance** of $R$

$$
F^+ = \set{V \to W \mid \forall \text{ legal } r \text{ of } R, r \text{ satisfies } V \to W}
$$

> $V \to W$ doesn't necessarily have to be in $F$

---

<!-- # How big is $F^+$?

Given a relation schema $R$ such that $|R| = n$, let's consider the definition of functional dependency: we need $X, Y \in \mathcal{P}(R) \setminus \varnothing$, given that $|\mathcal{P}(R)| = 2^n$ we could have $2^n - 1$ choices for $X$ and $Y$. Given that we could pair the subsets however we want, we have $(2^n - 1)(2^n - 1) = 2^{2n} - 2\cdot 2^n + 1 = \\ =2^{2n} - 2^{n + 1} + 1$ combinations

Let's consider the smallest possible $F = \varnothing$, how many values does $F^+$ have?

--- -->

# $F \subseteq F^+$

[PDF 7 slide 21](07%20-%20functional%20dependencies.pdf#page=21)

$$F \subseteq F^+$$

## Proof

$$
F^+ = \set{V \to W \mid \forall \text{ legal } r \text{ of } R, r \text{ satisfies } V \to W}
$$

By definition $r$ is legal if it satisfies every dependency $X \to Y \in F \implies$ given $X \to Y \in F$, every legal instance of $R$ satisfies $X \to Y \implies X \to Y \in F^+$

---

# Keys

[PDF 7 slide 22](07%20-%20functional%20dependencies.pdf#page=22)

Given a relation schema $R$ and a set $F$ of functional dependencies on $R$, $K \subseteq R$ is a **key** of $R$ if

- $K \to R \in F^+$
- $\forall K' \subset K, \: K' \to R \notin F^+$

> $"\subset"$ means **proper subset**, which implies that $K \neq K'$

---

# Trivial dependencies

[PDF 7 slide 26](07%20-%20functional%20dependencies.pdf#page=26)

Given a schema $R$ and $X, Y \in \mathcal{P}(R) \setminus \set{\varnothing} : Y \subseteq X$, we have that **every instance** $r$ of $R$ **satisfies** the dependency $X \to Y$

## Proof

<!-- By definition an instance $r$ of $R$ satisfies a dependency $X \to Y$ if $\forall t_1, t_2 \in r, t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y]$ -->

Given an instance $r$ of $R, \; \forall t_1, t_2 \in r$ we have that

$t_1[X] = t_2[X] \implies$ by definition $t_1[A] = t_2[A] \; \forall A \in X \implies$ as $Y \subseteq X$ we have that  
$t_1[A'] = t_2[A'] \; \forall A' \in Y \implies$ by definition $t_1[Y] = t_2[Y]$

As $t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y]$ we have that $r$ satisfies $X \to Y$

---

# Decomposition

[PDF 7 slide 27](07%20-%20functional%20dependencies.pdf#page=27)

Given a schema $R$ and a set of functional dependencies $F$ on $R$, we have that

$$X \to Y \in F^+ \iff X \to A \in F^+ \; \forall A \in Y$$

## Proof

$X \to Y \in F^+ \implies \forall \text{ legal } r \text{ of } R \quad \forall t_1, t_2 \in r \quad t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y] \implies t_1[A] = t_2[A] \; \forall A \in Y \implies X \to A \in F^+ \; \forall A \in Y$

$X \to A \in F^+ \; \forall A \in Y \implies \forall \text{ legal } r \text{ of } R \quad \forall t_1, t_2 \in R \quad t_1[X] = t_2[X] \implies \\ t_1[A] = t_2[A] \; \forall A \in Y \implies t_1[Y] = t_2[Y] \implies X \to Y \in F^+$

---

# $F^A$

[PDF 8 slide 3](08%20-%20Closure%20of%20F.pdf#page=3) $F^A$ is a set of functional dependencies on $R$ such that

- $X \to Y \in F \implies X \to Y \in F^A$
- $Y \subseteq X \in R \implies X \to Y \in F^A$ _(refelxivity)_
- $\forall Z \in R, X \to Y \in F^A \implies ZX \to ZY \in F^A$ _(augmentation)_
- $X \to Y, Y \to Z \in F^A \implies X \to Z \in F^A$ _(transitivity)_

[PDF 8 slide 6](08%20-%20Closure%20of%20F.pdf#page=6) derivates

- $X \to Y, X \to Z \in F^A \implies X \to YZ \in F^A$ _(union)_
- $X \to Y \in F^A \land Z \subseteq Y \implies X \to Z \in F^A$ _(decomposition)_
- $X \to Y, WY \to Z \in F^A \implies WX \to Z \in F^A$ _(pseudotransitivity)_

[PDF 8 slide 8](08%20-%20Closure%20of%20F.pdf#page=8) $X \to A_1 A_2 ... A_n \in F^A \iff \forall i=1,...,n \quad X \to A_i \in F^A$

---

# Derivates _(Proofs)_

<!-- $X \to Y, X \to Z \in F^A \implies X \to YZ \in F^A$ -->

### Union

$(X)^+_F$ LaTeX

$X \to Y, X \to Z \in F^A \implies$ by augmentation $X \to XY, XY \to YZ \in F^A \implies$ by transitivity $X \to YZ \in F^A$

### Decomposition

$X \to Y \in F^A \land Z \subseteq Y \implies Y \to Z \in F^A \implies$ by transitivity $X \to Z \in F^A$

### Pseudotransitivity

$X \to Y, WY \to Z \in F^A \implies$ by augmentation $WX \to WY \in F^A \implies$ by transitivity $WX \to Z \in F^A$

---

# $(X)^+_F$

$(
[PDF 8 slide 9](08%20-%20Closure%20of%20F.pdf#page=9)

Given a relation schema $R$, a set $F$ of dependencies on $R$ and $X \subseteq R$. The **closure** of $X$ with respect to $F$, denoted $(X)^+_F$ is defined as

$$(X)^+_F = \set{A \in R \mid X \to A \in F^A}$$

We have that $X \subseteq (X)^+_F$

## Proof

$\forall A \in X$ by reflexivity $X \to A \in F^A \implies$ by definition $A \in (X)^+_F  \implies X \subseteq (X)^+_F$

> We can use Armstrong's axioms as $(X)^+_F$ is defined of $F^A$

> NOTE: $(X)^+_F$ is **NOT** defined on $F^+$

---

# Lemma of closure

[PDF 8 slide 10](08%20-%20Closure%20of%20F.pdf#page=10)

Let $R$ be a schema and $F$ a set of functional dependencies on $R$

$$ X \to Y \in F^A \iff Y \subseteq (X)^+_F $$

## Proof

$X \to Y \in F^A \implies$ by decomposition $X \to A \in F^A \; \forall A \in Y \implies$ by definition
$A \in (X)^+\_F \; \forall A \in Y \implies Y \subseteq (X)^+\_F$

>

$Y \subseteq (X)^+\_F \implies A \in (X)^+\_F \; \forall A \in Y \implies$ by definition $X \to A \in F^A \; \forall A \in Y \implies$ by union
$X \to Y \in F^A$

---

# $F^+ = F^A$

[PDF 8 slide 11](08%20-%20Closure%20of%20F.pdf#page=11)

Let $R$ be a relation schema and $F$ a set of functional dependencies on $R$ then $F^+ = F^A$

## Proof

Let $F_i$ be the value of $F$ after the $i$-th application of an Armstrong's axiom, with $F_0 = F$

---

# $F^A \subseteq F^+$

### Base case

$F_0 = F \subseteq F^+ \implies F_0 \subseteq F^+$

### Inductive step

$F_i \subseteq F^+ \implies F_{i + 1} \subseteq F^+$

Let $X \to Y \in F_{i + 1}$, either

- $X \to Y \in F_i \implies$ by HP $X \to Y \in F^+$
- $X \to Y \in F_{i + 1} \setminus F_i$, which means that $X \to Y$ has been optained through one of the axioms

---

# $F^A \subseteq F^+$

### Reflexivity

$Y \subseteq X \implies$ given that $X \to Y$ is satisfied by every instance $X \to Y \in F^+$

### Augmentation

$Z \subseteq R, X = ZV, Y = ZW \land V \to W \in F_i$ given $t_1, t_2 \in r$ legal instance of $R$ we have that $t_1[X] = t_2[X] \implies (t_1[V] = t_2[V] \implies$ by HP $t_1[W] = t_2[W]) \land t_1[Z] = t_2[Z] \implies t_1[Y] = t_2[Y]$

### Transitivity

$X \to Z, Z \to Y \in F_i \implies$ by HP $\forall \text{ legal } r \text{ of } R, \forall t_1, t_2 \in r, t_1[X] = t_2[X] \implies t_1[Z] = t_2[Z] \implies t_1[Y] = t_2[Y]$ we have that $t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y] \implies X \to Y \in F^+$

---

# $F^+ \subseteq F^A$ _(legal instance)_

Given $X \subseteq R$ we can build an instance $r = \set{t_1, t_2}$ on $R$ such that

<table>
<thead>
<tr>
<th>

$r$

</th>
<th colspan="5">

$(X)^+_F$

</th>
<th colspan="5">

$R \setminus (X)^+_F$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$t_1$

</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>...</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>...</td>
<td>1</td>
</tr>
<tr>
<td>

$t_2$

</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>...</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>...</td>
<td>0</td>
</tr>
</tbody>
</table>

Let's verify that $r$ is a legal instance. Given $V \to W \in F$, as $V, W \neq \varnothing$ by definition, we could have

- $V \nsubseteq (X)^+_F \implies \exists A \in V : A \in R \setminus (X)^+_F \implies  t_1[V] \neq t_2[V] \implies r$ satisfies $V \to W$
- $V \subseteq (X)^+_F$, we could have that
  - $W \subseteq (X)^+_F \implies t_1[V] = t_2[V] \land t_1[W] = t_2[W] \implies r$ satisfies $V \to W$
  - $W \nsubseteq (X)^+_F \implies \exists A \in W : A \in R \setminus (X)^+_F \implies t_1[V] = t_2[V] \land t_1[W] \neq t_2[W]$

---

# $F^+ \subseteq F^A$ _(legal instance)_

In the last case $r$ doesn't satisfy $V \to W$, so we have to show that it can't happen. Let's suppose that $\exists V \to W \in F$ such that $r$ doesn't satisfy $V \to W$; by construction we have that

$$V \subseteq (X)^+_F \land \exists A \in W : A \in R \setminus (X)^+_F \implies A \notin (X)^+_F$$

We have that

- $V \subseteq (X)^+_F \implies$ by the lemma of closure $X \to V \in F^A$
- $A \in W \implies$ by decomposition $V \to A \in F^A$

By transitivity $X \to A \in F^A \implies$ by the lemma of closure $A \in (X)^+_F$ which is a contraddiction

## Legality

In the first 2 cases $r$ satisfies $V \to W \in F$, case 3 can't happen $\implies r$ is a legal instance of $R$

---

# $F^+ \subseteq F^A$

Let's consider $X \to Y \in F^+$

By definition we have that $X \subseteq (X)^+_F \implies$ by construction $t_1[X] = t_2[X] \implies$ by hypotesis and given that $r$ is a legal instance $t_1[Y] = t_2[Y] \implies$ by the lemma $Y \subseteq (X)^+_F \implies X \to Y \in F^A$

# $F^+ = F^A$

Given that $F_i \subseteq F^+ \: \forall i \in \mathbb{N}$ and $F^+ \subseteq F^A$ we have that $F^+ = F^A$

---

# 3NF

[PDF 9 slide 14](09%20-%20third%20normal%20form%201.pdf#page=14)

Given a relation schema $R$ and a set of functional dependencies $F$ on $R$.

$R$ is in **3NF** if $\forall X \to A \in F^+ : A \notin X$ either

- $A$ is prime _(belongs to a key)_
- $X$ is superkey

---

# 3NF pt.2

[PDF 10 slide 4](10%20-%20third%20normal%20form%202.pdf#page=4)

Let $R$ be a relation schema and $F$ a set of functional dependencies on $R$

An attribute $A \in R$ **partially** depends on a key $K$ if

<!-- TODO check if subseteq? NOT needed because X is a proper subset of K -->

- $\exists X \subset R : A \notin X \land X \to A \in F \land X \subset K$
- $A$ isn't prime

An attribute $A \in R$ **transitively** depends on a key $K$ if

- $\exists X \subset R : A \notin X \land X \to A \in F \land K \to X \in F$
- $X$ isn't a key
- $A$ isn't prime

> $X \subset R$ means that $X \neq R$, otherwise X would be a superkey, as $R \to R \in F^A = F^+$

---

# 3NF pt.3

[PDF 10 slide 5](10%20-%20third%20normal%20form%202.pdf#page=5)

Given a schema $R$ and a set of functional dependencies $F$ on $R$, **TFAE**

- $R$ is in 3NF
- there are **no attributes that partially or transitively depend on a key**
- $\forall X \to A \in F^+ : A \notin X$ either:
  - $A$ is prime _(belongs to a key)_
  - $X$ is superkey

## Proof

> TODO: I have it, I just have to write it out in $\LaTeX$

---

<!-- PDF 10 slide 6 -->

<!-- Let $R$ be a relation schema and $F$ a set of functional dependencies on $R$. A schema $R$ is in 3NF if and only if neither partial dependencies nor transitive dependencies exist in $F$ -->

# BCNF _(Boyce-Codd)_

[PDF 10 slide 20](10%20-%20third%20normal%20form%202.pdf#page=20)

A relation schema $R$ is in **Boyce-Codd Normal Form** (BCNF) when every determinant in $F$ is a superkey. A relation that respects Boyce-Codd Normal Form is also in **3NF**, but the opposite is not true.

<!-- > TODO: example that show that not all relation schemas can be reduced to 3NF -->

---

# $(X)^+_F$

[PDF 11 slie 5](../Slide/11%20-%20closure%20of%20X.pdf)

```python
def clousure(R, F, X):
	Z = X
	S = { A ∈ R | Y → V ∈ F ∧ Y ⊆ Z ∧ A ∈ V }

	if S ⊆ Z:
		return Z

	return closure(R, F, Z ∪ S)
```

---

# $(X)^+_F$

[PDF 11 slide 8](11%20-%20closure%20of%20X.pdf#page=8)

The algorithm `closure()` correctly computes the closure of a set of attributes $X$ respectively to a set $F$ of functional dependencies on $R$

## Proof

Let's consider $Z_i, S_i$ the values of $Z$ and $S$ at the $i$-th call of the function and $Z_f, S_f \mid S_f \subseteq Z_f$ the values of $Z, S$ at the last call of the function. Let's prove by induction that $Z_i \subseteq (X)^+_F$

---

# $Z_i \subseteq (X)^+_F$

### Base case

<!-- $Z_0 = X \subseteq (X)^+_F \implies Z_0 \subseteq (X)^+_F$ -->

$Z_0 = X \subseteq (X)^+_F$

<!-- ### Inductive step -->

### Inductive step $Z_i \subseteq (X)^+_F \implies Z_{i + 1} \subseteq (X)^+_F$

<!-- We have to prove that $Z_i \subseteq (X)^+_F \implies Z_{i + 1} \subseteq (X)^+_F$ -->

<!-- and $S_i = \set{A \in R \mid Y \to V \in F \land Y \subseteq Z_i \land A \in V}$ -->

Given that $Z_{i + 1} = Z_i \cup S_i$ then if $A \in Z_{i + 1}$ either

- $A \in Z_i \implies$ by HP $A \in (X)^+_F$
- $A \in S_i \implies$ by construction $\exists Y \to V \in F \mid Y \subseteq Z_i \land A \in V \implies$ by HP $Y \subseteq (X)^+_F \implies$ by the lemma of closure $X \to Y \in F^A$ and by decomposition $Y \to A \in F^A \implies$ by transitivity $X \to A \in F^A \implies$ by definition $A \in (X)^+_F$

---

# $(X)^+_F \subseteq Z_f$ _(legal instance)_

Given $Z_f$ we can build an instance $r = \set{t_1, t_2}$ on $R$ such that

<table>
<thead>
<tr>
<th>

$r$

</th>
<th colspan="5">

$Z_f$

</th>
<th colspan="5">

$R \setminus Z_f$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$t_1$

</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>...</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>...</td>
<td>1</td>
</tr>
<tr>
<td>

$t_2$

</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>...</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>...</td>
<td>0</td>
</tr>
</tbody>
</table>

Let's verify that $r$ is a legal instance. Given $V \to W \in F$ as $V, W \neq \varnothing$ we could have either

- $V \nsubseteq Z_f \implies \exists A \in V : A \in R \setminus Z_f \implies t_1[V] \neq t_2[V] \implies r$ satisfies $V \to W$
- $V \subseteq Z_f$
  - $W \subseteq Z_f \implies$ by construction $t_1[V] = t_2[V] \land t_1[W] = t_1[W] \implies$ $r$ satisfies $V \to W$
  - $W \nsubseteq Z_f \implies$ by construction $t_1[V] = t_2[V] \land t_1[W] \neq t_2[W]$

---

# $(X)^+_F \subseteq Z_f$ _(legal instance)_

Let's suppose that $\exists V \to W \in F : r$ doesn't satisfy $V \to W \implies$ by construction

$$V \subseteq Z_f \land \exist A \in W : A \in R \setminus Z_f \implies A \notin Z_f$$

Given that $V \subseteq Z_f \land V \to W \in F \land A \in W \implies$ by construction of $S_f, \: A \in Z_f$ which is a contraddiction

## Legality

In the first 2 cases $r$ satisfies $V \to W \in F$ case 3 can't happen $\implies r$ is a legal instance of $R$

---

# $(X)^+_F \subseteq Z_f$

Let's consider $A \in (X)^+_F$

Given that $X \to A \in F^A = F^+$ and $r$ is a legal instance $\implies r$ satisfies $X \to Y$, and given that by construction $X \subseteq Z_f \implies t_1[X] = t_2[X] \implies$ by definition $t_1[A] = t_2[A] \implies$ by construction $A \in Z_f$

# $Z_f = (X)^+_F$

Given that $Z_i \subseteq (X)^+_F \; \forall i \in \mathbb{N}$ and $(X)^+_F \subseteq Z_f$, we have that $Z_f = (X)^+_F$

---

# Intersection Rule

[PDF 12 slide 19](12%20-%20Finding%20the%20keys%20of%20a%20schema.pdf#page=19)

Given a relation scheme $R$ and a set of functional dependencies $F$ on $R$

$$X := \bigcap\limits_{V \to W \in F} R-(W-V)$$

<!-- If the intersection of these sets determines $R$, then the intersection is the only key to $R$ else there are multiple keys, and ALL of them must be identified for checking 3NF -->

If $X \to R \in F^+$ then the intersection is the only key to $R$ otherwise there are multiple keys, and **ALL** of them must be identified to check if $R$ is in **3NF**

---

# Decomposition

[PDF 13 slide 8](13%20-%20preserving%20F.pdf#page=8)

Let $R$ be a relation scheme, a decomposition $\rho$ of $R$ is such that

$$\rho = \set{R_1, R_2, ..., R_k} \subseteq \mathcal{P}(R) : \bigcup\limits_{i = 1}^{k} R_i = R$$

---

# Equivalence

[PDF 13 slide 12](13%20-%20preserving%20F.pdf#page=12)

Let $F$ and $G$ be two sets of functional dependencies, we can define an equivalence relation

$$F \equiv G \iff F^+ = G^+$$

- reflexivity $F \implies F^+ = F^+ \implies F \equiv F$
- simmetry $F \equiv G \implies F^+ = G^+ \implies G^+ = F^+ \implies G \equiv F$
- transitivity $F \equiv G \land G \equiv H \implies F^+ = G^+ \land G^+ = H^+ \implies F^+ = H^+ \implies F \equiv H$

[PDF 13 slide 14](13%20-%20preserving%20F.pdf#page=14)

Let $F$ and $G$ be two sets of functional dependencies

$$F \subseteq G^+ \implies F^+ \subseteq G^+$$

---

# $F \subseteq G^+ \implies F^+ \subseteq G^+$

### Base case

$F_0 = F \subseteq G^+ \implies F_0 \subseteq G^+$

### Inductive Step

$F_i \subseteq G^+ \implies F_{i + 1} \subseteq G^+$

$X \to Y \in F_{i + 1} \implies X \to Y$ has been optained through

- reflexivity $Y \subseteq X \implies$ given that $X \to Y$ is satisfied by every instance $X \to Y \in G^+$
- augmentation $\exists Z \subseteq R, V \to W \in F_i \mid X = ZV, Y = ZW$
- transitivity

> TODO

---

# Preserving F

[PDF 13 slide 15](13%20-%20preserving%20F.pdf#page=15)

Let $R$ be a relation scheme, $F$ a set of functional dependencies on $R$ and $\rho = \set{R_1, R_2, ..., R_k}$ a decomposition of $R$, we say that $\rho$ preseves $F$ if

$$F \equiv G = \bigcup\limits_{i = 1}^{k} \pi_{R_i}(F)$$

Where

$$\pi_{R_i}(F) = \set{X \to Y \in F^+ \mid XY \subseteq R_i}$$

[PDF 13 slide 16](13%20-%20preserving%20F.pdf#page=16)

Given the definition of $G$, it will always be that $G \subseteq F^+ \implies G^+ \subseteq F^+$ so it is enough to verify that $F \subseteq G^+$

---

# Dependency preservation

[PDF 13 slide 17](13%20-%20preserving%20F.pdf#page=17)

```python
def preserves_dependencies(R, F, ρ):
	for X → Y ∈ F:
		if Y ⊈ closure_G(R, F, ρ, X):
			return false

	return true
```

This algorithm is enough as we just have to check wether $F \subseteq G^+$

Given $X \to Y \in F$ we have that $X \to Y \in G^+ = G^A \iff$ by the lemma of closure $Y \subseteq (X)^+_G$

<!-- S = { A ∈ R | Y → V ∈ F ∧ Y ⊆ Z ∧ A ∈ V } -->
<!-- # return X if S ⊆ X else closure(R, F, X ∪ S) -->

<!-- PDF 13 slide 19 -->

---

# $(X)^+_G$

```python
def clousure_G(R, F, X, ρ):
	Z = X
	S = ∅

	for P ∈ ρ:
		S = S ∪ (closure(R, F, Z ∩ P) ∩ P)

	if S ⊆ Z
		return Z

	return closure_G(R, F, Z ∪ S)
```

<!-- return X if S ⊆ X else closure_G(R, F, X ∪ S) -->

[PDF 13 slide 23](13%20-%20preserving%20F.pdf#page=23) Let $R$ be a relation schema, $F$ a set of functional dependencies on $R$ and
$\rho = \set{R_1, R_2, ..., R_k}$ a decomposition of $R$ and $X \subseteq R$ the algorithm `closure_G()` correctly computes $(X)^+_G$

---

# $Z_f \subseteq (X)^+_G$

Let $Z_i, S_i$ the values of $Z$ and $S$ at the $i$-th call of the function, with $Z_0 = X$, and $S_f \subseteq Z_f$

<!-- the final values of $Z$ and $S$ -->

### Base case

$Z_0 = X \subseteq (X)^+_G \implies Z_0 \subseteq (X)^+_G$ by HP

### Inductive step

$Z_i \subseteq (X)^+_G \implies Z_{i+1} \subseteq (X)^+_G$, given that $S_i = \bigcup\limits_{j = 1}^k (Z_i \cap R_j)^+_F \cap R_j$

Let $A \in Z_{i + 1} = Z_i \cup S_i \implies \exists j : A \in (Z_i \cap R_j) \cap R_j \implies Z_i \cap R_j \to A \in G^A$

By HP we have that $Z_i \subseteq (X)^+_G \implies X \to Z_i \in G^A$, let $Z_i = (Z_i \cap R_j) \cup V$ by decomposition we have that $X \to Z_i \cap R_j \in G^A \implies$ by transitivity $X \to A \in G^A$

---

# $X \subseteq Y \implies (X)^+_F \subseteq (Y)^+_F$

$X \subseteq Y \implies Y \to X \in F^A$ by reflexivity

Given $A \in (X)^+_F \implies$ by the lemma of closure $X \to A \in F^A \implies$ by transitivity $Y \to A \in F^A \\ \implies$ by the lemma of closure $A \in (Y)^+_F$

# $(X)^+_G \subseteq Z_f$

$X \subseteq Z_f \implies (X)^+_G \subseteq (Z_f)^+_G$, we have to prove that $Z_f = (Z_f)^+_G$

Let's consider $A \in S' = \set{A \in R \mid V \to W \in G \land V \subseteq Z_f \land A \in W} \implies \exists V \to W \in G : V \subseteq Z_f \land A \in W \implies \exists R_j \in \rho : VW \subseteq R_j \implies V \subseteq Z_f \cap R_j \land A \in R_j \implies A \in (Z_f \cap R_j)^+_F \cap R_j \implies A \in S_f \implies A \in Z_f$

---

<!-- # $X \subseteq Y \implies (X)^+_F \subseteq (Y)^+_F$ _(alternative)_

Let $X_i, Y_i$ the values of the clousure after the $i$-th application of the algorithm `closure()`

### Base case

$X_0 = X \subseteq Y = Y_0$

### Inductive step

$X_i \subseteq Y_i \implies X_{i + 1} \subseteq Y_{i + 1}$

$A \in X_{i + 1}$, given that $X_{i + 1} = X_i \cup S^X_i \land S^X_i = \set{A \mid V \to W \in F \land V \subseteq X_i \land A \in W} \implies$ by HP $V \subseteq Y_i \implies W \subseteq S^Y_i \implies$ by decomposition, and given that $Y_{i + 1} = Y_i \cup S^Y_i \implies A \in Y_{i + 1}$

--- -->

# Loseless join

<!-- If we decompose a relation schema $R$ we want the obtained decomposition $\rho = \set{R_1, R_2, ..., R_k}$ such that each legal instance $r$ of $R$ can be reconstructed through natural join from legal instnaces $r_1, r_2, ..., r_k$

ρ = R1 , R2 , ..., Rk , such that each legal instance r of R can be reconstructed through natural join from the legal instances r1 , r2 , ..., rk of the decomposition schemas R1 , R2 , ..., Rk as for reconstructing a tuple t of r it is required that t[Ri ] ∈ ri , ∀ i = 1,...,k, then we must have πRi(r) = ri , ∀ i = 1,...,k -->

[PDF 15 slide 11](15%20-%20lossless%20join.pdf#page=11) Let $R$ be a relation schema. A decomposition $\rho = \set{R_1, R_2, ..., R_k}$ of $R$ has a lossless join if $\forall r$ legal instance of $R$ we have that $r = \pi_{R_1}(r) \bowtie \pi_{R_2}(r) \bowtie ... \bowtie \pi_{R_k}(r)$

[PDF 15 slide 13](15%20-%20lossless%20join.pdf#page=13) Let $R$ be a relation schema and let $\rho = \set{R_1, R_2, ..., R_k}$ be a decomposition of $R$; for each legal instance $r$ of $R$, we denote $m_{\rho}(r) = \pi_{R_1}(r) \bowtie \pi_{R_2}(r) \bowtie ... \bowtie \pi_{R_k}(r)$

- $r \subseteq m_{\rho}(r)$
- $\pi_{R_i}(m_{\rho}(r)) = \pi_{R_i}(r)$
- $m_{\rho}(m_{\rho}(r)) = m_{\rho}(r)$

<!-- $t \in r \implies t[R_i] = \set{(A, t[A]) \mid A \in R_i}$ -->

Given $S_1, ..., S_k$ relation schemas with their instances $s_1, ..., s_k$, let's define the $\bowtie$ operator as

$\mathop{\bowtie}\limits_{i = 1}^k S_i = \set {\bigcup\limits_{i = 1}^k t_j \mid \forall s_i \; \forall t_j \in s_i \; \land \bigcup\limits_{i = 1}^k t_j \text{ is a function}}$

<!-- Let's define the $\bowtie$ operator $R \bowtie S = \set{t_1 \cup t_2 \mid t_1 \in r \land t_2 \in s \land t_1 \cup t_2 \text{ is a function}}$ -->

---

# $r \subseteq m_{\rho}(r)$

$t \in r \implies t[R_i] \in \pi_{R_i}(r) \; \forall R_i \in \rho$ by definition

$\mathop{\bowtie}\limits_{i = 1}^k \pi_{R_i}(r) = \set {\bigcup\limits_{i = 1}^k p_i[R_i] \mid p_i[R_i] \in \pi_{R_i}(r) \land \bigcup\limits_{i = 1}^k p_i[R_i] \text{ is a function}}$

$\forall t \in r, \; t = \bigcup\limits_{i = 1}^k t[R_i]$ as by definition of $\rho$ we have that $R = \bigcup\limits_{i = 1}^k R_i$

$t \in r \implies t$ is a function by definition

$t = \bigcup\limits_{i = 1}^k t[R_i] \in \mathop{\bowtie}\limits_{i = 1}^k \pi_{R_i}(r) = m_{\rho}(r) \implies t \in m_{\rho}(r)$

<!-- $\forall t \in r, \; t = \bigcup\limits_{i = 1}^k t[R_i] = \mathop{\bowtie}\limits_{i = 1}^k \set{ t[R_i] }$ -->

<!-- $t \in r \implies$ by definition $t[R_i] \in \pi_{R_i}(r) \; \forall R_i \in \rho \implies \set{ t[R_i] } \subseteq \pi_{R_i}(r) \; \forall R_i \in \rho$ -->

<!-- $t = \mathop{\bowtie}\limits_{i = 1}^k \set{ t[R_i] } \subseteq \mathop{\bowtie}\limits_{i = 1}^k \pi_{R_i}(r) = m_{\rho}(r) \implies t \in m_{\rho}(r)$ -->

<!-- $\forall t \in r$ we consider $t[R_i], \: R_i \in \rho$, we have that $t \in \set{ t[R_1] } \bowtie ... \bowtie \set{ t[R_k] } \subseteq \pi_{R_1}(r) \bowtie ... \bowtie \pi_{R_k}(r) = m_{\rho}(r)$ -->

---

# $\pi_{R_i}(m_{\rho}(r)) = \pi_{R_i}(r)$

<!-- Let's consider $t_{R_i} \in \pi_{R_i}(m_{\rho}(r))$, we have to prove that $t_{R_i} \in \pi_{R_i}(r)$ -->

$t \in r \implies$ by definition $t[R_i] \in \pi_{R_i}(r) \; \forall R_i \in \rho$
$\pi_{R_i}(m_{\rho}(r)) = \set{q[R_i] \mid q \in \mathop{\bowtie}\limits_{i = 1}^k \pi_{R_i}(r)}$

## $\pi_{R_i}(r) \subseteq \pi_{R_i}(m_{\rho}(r))$

$t \in r \implies t \in m_{\rho}(r) \implies t[R_i] \in \pi_{R_i}(m_{\rho}(r))$

## $\pi_{R_i}(m_{\rho}(r)) \subseteq \pi_{R_i}(r)$

$q \in \mathop{\bowtie}\limits_{i = 1}^k \pi_{R_i}(r) \implies$ by definition of join $q = \mathop{\bowtie}\limits_{i = 1}^k \set{ p_i[R_i] } \mid p_i \in r \implies$ given that $q$ is a function $q[R_i] = p_i[R_i]$ and $p_i \in r \implies p_i[R_i] \in \pi_{R_i}(r)$ we have that $q[R_i] \in \pi_{R_i}(r)$

<!-- $\exists p_1, p_2, ..., p_k \in r \mid p_i[R_i] \in \pi_{R_i}(r) \; \forall i = 1,..., k$ -->

<!-- $t_{R_i} \in \pi_{R_i}(m_{\rho}(r)) \iff \exists t' \in m_{\rho}(r) : t'[R_i] = t_{R_i} \iff$

$\iff \exists t_1, ..., t_k \in r : t'[R_j] = t_j[R_j] \quad \forall R_j \in \rho$ but $t_{R_i} = t[R_i] \in \pi_{R_i}(r)$ -->

---

# $m_{\rho}(m_{\rho}(r)) = m_{\rho}(r)$

$m_{\rho}(m_{\rho}(r)) = \mathop{\bowtie}\limits_{i = 1}^k \pi_{R_i}(m_{\rho}(r)) = \mathop{\bowtie}\limits_{i = 1}^k \pi_{R_i}(r) = m_{\rho}(r)$

<!-- $m_{\rho}(m_{\rho}(r)) = \pi_{R_1}(m_{\rho}(r)) \bowtie ... \bowtie \pi_{R_k}(m_{\rho}(r)) = \pi_{R_1}(r) \bowtie ... \bowtie \pi_{R_k}(r) = m_{\rho}(r)$ -->

<!-- $m_{\rho}(m_{\rho}(r)) = \pi_{R_1}(m_{\rho}(r)) \bowtie ... \bowtie \pi_{R_k}(m_{\rho}(r)) = \pi_{R_1}(r) \bowtie ... \bowtie \pi_{R_k}(r) = m_{\rho}(r)$ -->

<!-- Let's consider $t_{R_i} \in \pi_{R_i}(r)$, we have to prove that $t_{R_i} \in \pi_{R_i}(m_{\rho}(r))$ -->
<!-- Let's consider $t_{R_i} \in \pi_{R_i}(r) \land t' \in r$ with $t'[R_i]$, we have that $t'[R_i] \in t_{R_i}$ -->

---

# Loseless join pt.2

[PDF 15 slide 15](15%20-%20lossless%20join.pdf#page=15) Given $\rho = \set{R_1, R_2, ..., R_k}$, build a table $r$ with $|R|$ columns and $k$ rows. At the $i$-th row and $j$-th column put $a_j$ if $A \in R_{i}$ else $b_{ij}$

```python
def has_looseless_join(R, F, ρ):
	while !(∃ t ∈ r | ∀ A ∈ R, t[A] = a) and r changed:
		for X → Y ∈ F:
			for t1 ∈ r:
				for t2 ∈ r:
					if t1[X] = t2[X] and t1[Y] != t2[Y]:
						for A ∈ Y:
							if t1[A] = a:
								t2[A] = t1[A]
							else:
								t1[A] = t2[A]

	return ∃ t ∈ r | ∀ A ∈ R, t[A] = a
```

---

## Correctness

[PDF 15 slide 19](#page=19)

Let $R$ be a relation scheme, $F$ a set of functional dependencies on $R$ and let $\rho = \set{R_1, R_2, ..., R_k}$ be a decomposition of $R$; the algorithm correctly decides whether $\rho$ has a lossless join

$r = m_{\rho}(r) \iff r$ has a tuple with all $a$ when the algorithm termintes

> TODO: I can prove $r = m_{\rho}(r) \implies r$ has a tuple with all $a$ when the algorithm terminates, I just have to write it in $\LaTeX$

---

# Minimal cover

[PDF 17 slide 7](17%20-%20minimal%20covers.pdf#page=7)

Let $R$ be a schema and $F$ be a set of functional dependencies on $R$. A **minimal cover** of $F$ is a set of functional dependencies $G \equiv F$ such that:

- $\forall X \to Y \in G, |Y| = 1$
- $\forall X \to A \in G, \nexists X' \subset X \mid G \equiv (G - \set{X \to A}) \cup \set{X' \to A}$
- $\nexists X \to A \in G \mid G \equiv G - \set{X \to A}$

<!-- TODO: check if minimal cover is equivalent to F -->

---

# Minimal cover _(step 1)_

$F_1 = \set{X \to A \mid X \to Y \in F \land A \in Y}$

$F \overset{A}{\to} F_1$ by decomposition $F_1 \overset{A}{\to} F_1^A \implies F \subseteq F_1^A$

$F_1 \overset{A}{\to} F$ by union $F \overset{A}{\to} F^A \implies F_1 \subseteq F^A$

$F \equiv F_1$

---

# Minimal cover _(step 2)_

Given $X \to A \in F_1,  X' \subset X \land X' \to A \in F_1^+ \implies F_2 = (F_1 \setminus \set{X \to A}) \cup \set{X' \to A}$

$X' \subseteq X \implies X \to X' \in F_1^+ \land X \to X' \in F_2^+$ by reflexivity

$X \to A \in F_1$

- $X \to A \in F_2 \implies X \to A \in F_2^+$
- $X \to A \notin F_2 \implies X \to X' \in F_2^+ \land X' \to A \in F_2^+ \implies X \to A \in F_2^+$ by transitivity

$X \to A \in F_2$

- $X \to A \in F_1 \implies X \to A \in F_1^+$
- $X \to A \notin F_1 \implies X \to A \in F_1^+$ by HP

$F_2 \equiv F_1 \implies F \equiv F_2$ by transitivity of the $\equiv$ relationship

---

# Minimal cover _(step 3)_

$X \to A \in F_2, \; A \in (X)^+_{F_2 \setminus \set{X \to A}} \implies F_3 = F_2 \setminus \set{X \to A}$

$X \to A \in F_2$

- $X \to A \in F_3 \implies X \to A \in F_3^+$
- $X \to A \notin F_3 \implies X \to A \in F_3^+$ by HP as $A \in (X)^+_{F_3}$

$X \to A \in F_3$

- $X \to A \in F_2 \implies X \to A \in F_2^+$
- $X \to A \notin F_2$ is a contraddiction as $F_3 = F_2 \setminus \set{X \to A}$ by definition

$F_2 \equiv F_3 \implies F \equiv F_3$

---

# Decomposition

<!-- [PDF 19 slide 4](19%20-%20decomposition%20algorithm.pdf#page=4) -->

```python
def decomposition(R, F: minimal cover):
	S = ∅
	ρ = ∅

	for A ∈ R | ∄ X → Y ∈ F : A ∈ XY:
		S = S ∪ {A}

	if S != ∅:
		R = R - S
		ρ = ρ ∪ {S}

	if ∃ X → Y ∈ F | XY = R:
		ρ = ρ ∪ {R}
	else:
		for X → A ∈ F:
			ρ = ρ ∪ {XA}
```

---

# Decomposition pt.2

[PDF 19 slide 5](19%20-%20decomposition%20algorithm.pdf#page=5)

Let $R$ be a relational schema and $F$ a set of functional dependencies on $R$, which is a minimal cover; the algorithm `decomposition()` computes _(in polynomial time)_ a decomposition $\rho$ of $R$ such that:

- each relational schema in $\rho$ is in 3NF
- $\rho$ preserves $F$

<!-- ---

# Physical organization

- Heap
- Sequential
- Random (hashing)
- Indexed Sequential
- List Data
- Secondary Indexes _(and inverted files)_
- $B$-Tree
- $B^+$-tree

---

# Hark Disk

## Reading cost

**service time** = seek time + rotational delay + service time
response time = queueing time + **service time**

A physical organization can optimize record lookup, as we can read from the disk either **randomly** or **sequentially** _(which is faster, as we don't have to account for seek time)_

---

# Heap

New records are inserted at the end of the file

Linear search is the only option for records retrieval

The `linear_search()` function has $O(\frac{\#Blk}{2})$ average complexity

The `insert()` function has $O(1)$ complexity

---

# Sequential

Records are sorted based on key

The `binary_search()` function has $O(log_2(\#Blk))$ complexity with random access

The `linear_search()` function has $O(\frac{\#Blk}{2})$ complexity with sequential access

The `insert()` function has $O(n \cdot log_2(n))$ complexity

> TODO: Slide 20

---

# Hashing

`hash(key) -> address` function, it uses buckets. Collitions can occur. `%` is kinda cool, better if $n$ is prime

**Loading Factor**: average number of records per bucket divided by bucket size

- tradeoff between efficient use of storage capacity and retrieval performance

# ISAM (Indexed Sequential Access Method)

It's basically sequential file organization with an index before

> TODO research on loading factor

Slide 40

---

# Concorrenza

[PDF 22 slide 5](22%20-%20Il%20controllo%20della%20concorrenza.pdf#page=5)

**Transazione** - esecuzione di una parte di un programma che rappresenta un’unità logica di accesso o modifica del contenuto della base di dati

[PDF 22 slide 6](22%20-%20Il%20controllo%20della%20concorrenza.pdf#page=6)

**ACID** - Atomicity, Consistency, Isolation e Durability

[PDF 22 slide 7](22%20-%20Il%20controllo%20della%20concorrenza.pdf#page=7)

**Schedule** - (piano di esecuzione) di un insieme $T$ di transazioni ordinamento delle operazioni nelle transazioni in $T$ che conserva l’ordine che le operazioni hanno all’interno delle singole transazioni

[PDF 22 slide 8](22%20-%20Il%20controllo%20della%20concorrenza.pdf#page=8)

**Schedule seriale** - schedule ottenuto permutando le transazioni in T

---

# Schedule

[PDF 22 slide 15](22%20-%20Il%20controllo%20della%20concorrenza.pdf#page=15)

Tutti gli schedule seriali sono corretti. Uno schedule non seriale è corretto se è serializzabile, cioè se è “equivalente” ad uno schedule seriale.

**Possibili problemi**

- aggiornamento perso
- dato sporco
- aggregato non corretto

[PDF 22 slide 19](22%20-%20Il%20controllo%20della%20concorrenza.pdf#page=19)

Due schedule sono **equivalenti** se (per ogni dato modificato) producono valori uguali, dove due valori sono uguali solo se sono prodotti dalla stessa sequenza di operazioni

---

# Item

[PDF 22 slide 24](22%20-%20Il%20controllo%20della%20concorrenza.pdf#page=24)

**Item** - unità a cui l’accesso è controllato

Le **dimensioni** degli item devono essere definite in base all’uso che viene fatto della base di dati in modo tale che in media una transazione acceda a pochi item _(granularità)_

# Lock

[PDF 23 slide 2](23%20-%20Il%20meccanismo%20di%20lock%20–%20Lock%20binario.pdf#page=2)

**Lock** - privilegio di accesso ad un singolo item realizzato mediante una variabile associata all’item (variabile lucchetto) il cui valore descrive lo stato dell’item rispetto alle operazioni che possono essere effettuate su di esso

---

# Lock pt.2

[PDF 23 slide 6](23%20-%20Il%20meccanismo%20di%20lock%20–%20Lock%20binario.pdf#page=6)

Uno schedule è detto **legale** se una transazione effettua un locking ogni volta che deve leggere o scrivere un item ciascuna transazione rilascia ogni lock che ha ottenuto

[PDF 23 slide 31](23%20-%20Il%20meccanismo%20di%20lock%20–%20Lock%20binario.pdf#page=31)

Uno schedule è serializzabile se esiste uno schedule seriale
tale che per ogni item l’ordine in cui le varie transazioni fanno un lock su quell’item coincide con quello dello schedule seriale

[PDF 23 slide 32](23%20-%20Il%20meccanismo%20di%20lock%20–%20Lock%20binario.pdf#page=32)

Algoritmo 1
Dato uno schedule S
• Passo 1
• crea un grafo diretto G (grafo di serializzazione)
nodi: transazioni
archi: Ti
Tj
(con etichetta X) se in S Ti esegue un
unlock(X) e Tj esegue il successivo lock(X)
non UN successivo ma IL successivo, cioè Tj è la prima
transazione che effettua il lock di X dopo che Ti ha
effettuato l’unlock, anche se le due operazioni non sono
di seguito

---

# Serializzabilità

[PDF 23 slide 38](23%20-%20Il%20meccanismo%20di%20lock%20–%20Lock%20binario.pdf#page=38)

Uno schedule $S$ è serializzabile $\iff$ il suo grafo di serializzazione è aciclico

[PDF 23 slide 42](23%20-%20Il%20meccanismo%20di%20lock%20–%20Lock%20binario.pdf#page=42)

Una transazione obbedisce al protocollo di locking a due fasi, o più semplicemente è a due fasi, se

- prima effettua tutte le operazioni di lock (fase di
  locking) e
- poi tutte le operazioni di unlock (fase di
  unlocking)

[PDF 23 slide 43](23%20-%20Il%20meccanismo%20di%20lock%20–%20Lock%20binario.pdf#page=43)

Sia $T$ un insieme di transazioni. Se ogni transazione in $T$ è a due fasi $\implies$ ogni schedule di $T$ è serializzabile

---

# Lock a 3 valori

[PDF 24 slide 7](24%20-%20Lock%20a%20tre%20valori.pdf#page=7)

Due schedule sono equivalenti se

- producono lo stesso valore per ogni item su cui viene effettuato un wlock (le formule che danno i valori finali per ciascun item sono le stesse)
- ogni operazione rlock(X) legge lo stesso valore di X nei due schedule

Testare la serializzabilità
Algoritmo
Dato uno schedule S
• Passo 1
• crea un grafo diretto G (grafo di serializzazione)
nodi: transazioni
archi: Ti
Tj
(con etichetta X) se in S

- Ti esegue una rlock(X) o una wlock(X) e Tj è la
  transazione che esegue la successiva wlock(X)
- Ti esegue una wlock(X) e Tj esegue una
  rlock(X) dopo che Ti ha eseguito la wlock(X) e
  prima che un’altra transazione esegua una
  wlock(X).
  O Tj esegue la successiva wlock (dopo una rlock o una wlock, è indifferente)
  oppure esegue la rlock tra due wlock (potrebbero esserci più rlock tra
  due wlock e quindi più archi che partono da Ti
  )

---

# Lock a 3 valori pt.2

Una transazione nel modello a tre valori è a due fasi se nessuna operazione di lock (rlock o wlock) segue una operazione di unlock

- Se ogni transazione in un insieme T è a due fasi allora
  ogni schedule di T è serializzabile
- Solo se tutte le transazioni sono a due fasi possiamo
  avere la certezza che ogni schedule è serializzabile

[PDF 25 slide 16]
Algoritmo 2
• Dato uno schedule S
• Passo 1
• crea un poligrafo diretto P
nodi: transazioni+T0+Tf
archi
• vengono creati gli archi in accordo al vincolo 1: se una
transazione T2
legge il valore di un item X scritto da una
transazione T1
viene aggiunto l’arco T1
T2
• vengono eliminati tutti gli archi entranti in transazioni inutili
(una transazione inutile T può essere individuata facilmente
perché non c’è nessun cammino in P da T a Tf
)

---

# Deadlock

[PDF 26 slide 2](26%20-%20Deadlock%20e%20livelock%20-%20Protocollo%20di%20locking%20a%20due%20fasi%20stretto.pdf#page=2)

Un deadlock si verifica quando

- ogni transazione in un insieme T è in attesa di ottenere un lock su un item sul quale qualche altra transazione nell’insieme T mantiene un lock e quindi
- rimane bloccata e quindi
- non rilascia i lock e quindi
- può bloccare anche transazioni che non sono in T

---

# Timestamp

[PDF 27 slide 2](27%20-%20Time-stamp.pdf#page=2)

Il timestamp identifica una transazione è assegnato alla transazione dallo scheduler quando la transazione ha inizio può essere

- il valore di un contatore
- l’ora di inizio della transazione

[PDF 27 slide 4](27%20-%20Time-stamp.pdf#page=4)

Uno schedule è serializzabile se è equivalente allo schedule seriale in cui le transazioni compaiono ordinate in base al loro timestamp

---

# Timestamp pt.2

[PDF 27 slide 4](27%20-%20Time-stamp.pdf#page=5)

Quindi uno schedule è serializzabile se: per ciascun item acceduto da più di una transazione, l’ordine con cui le transazioni accedono all’item è quello imposto dai timestamp

$$
$$ -->
