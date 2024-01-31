# Recurrence Equations

We'll analyzer the computational cost of the following **recursive search** algorithm.

```python
def search(list, value, index=0):
    if list[index] == value:
        return index;

    if index == len(list) - 1:
        return None

    return search(list, value, index + 1)
```

The first step, requires writing out a system of the **equation** and the **base case** of the algorithm.

$$
\begin{equation}
    \begin{cases}
        T(n) = T(n-1) + \theta(1) \\
        T(1) = \theta(1)
    \end{cases}
\end{equation}
$$

Now let's solve the equation, in **four different methods**.

## Iterative

**Idea**: 
    - develop the equation and express it as sum of terms depending on $n$ and the _base case_.

**Difficulty**: 
    - many algebric calculations to do.

$$
T(n) = T(n-1) + \theta(1) \implies \\
T(n) = [T(n-2) + \theta(1)] + \theta(1) \implies \\
T(n) = \set{[T(n-3) + \theta(1)] + \theta(1)} + \theta(1) \implies \\
T(n) = T(n-k) + k\theta(1) \\
$$

Then we calculate the equation when $n-k \rightarrow 1$, the base case.

$$
n-k = 1 \implies k = n - 1 \implies \\
T(n) = T(1) + (n-1)\theta(1) \implies \\
T(n) = \theta(1) + n\theta(1) - \theta(1) \implies \\
T(n) = \theta(n)
$$


## Tree

> TODO: draw trees in markdown!


## Substitution

**Idea**:
    - ipothize a solution for the given recurrence equation
    - verify _(by induction)_ wether it works

**Difficulty**:
    - it's hard to find a solution as close as possible to the real solution
    - it's used mainly in demonstrations

Let's suppose $T(n) = cn$, and $T(1) = d$, where $c$ and $d$ are fixed constants. 

$$
T(n) = cn = c(n-1) + \theta(1) \implies \\
cn = cn - c + \theta(1) \implies \\
c = \theta(1)
$$

This doesn't mean that T(1), which is a $\theta(1)$ is the same as $c$, so we need two constants.

$$
\begin{equation}
    \begin{cases}
        T(n) = T(n-1)+c \\
        T(1) = d 
    \end{cases}
\end{equation}
$$

Now we have to prove that $kn$ is a $O(n)$ and a $\omega(n)$ using **induction**.

### $O(n)$

$T(n) = O(n) \implies T(n) \le kn$ where k is to be determined.


#### Base Case

First, check for which values the base case is verified.

$T(1) \le k\cdot1 \implies d \le k \implies k \ge d$

#### Induction

Then check if the general case is covered by the base case.

$ T(n) \le k(n-1) + c = kn - k + c \le kn \implies k \gt c $

We get that $k \ge d \land k \ge c$, we can always find constants $c$ and $d$ so that $\exists k$ greater than both, so the induction is verified. 

### $\omega(n)$

$T(n) = \omega(n) \implies T(n) \ge kn $ where k is to be determined.


#### Base Case

First, check for which values the base case is verified.

$T(1) \ge k\cdot1 \implies d \ge k \implies k \le d$


#### Induction

Then check if the general case is covered by the base case.

$ T(n) = k(n-1) + c = kn - k + c \ge kn \implies k \le c $

We get that $k \le d \land k \le c$, we can always find constants $c$ and $d$ so that $\exists k$ smaller than both, so the induction is verified. 


## Main

**Idea**:
    - It's a set of formulas to solve a recurrence equation 

**Difficulty**:
    - works only when the equation is in the form $T(n) = aT(\frac{n}{b}) + f(n)$ with $T(1) = \theta(1)$

### Theorem

Given 
- $a \ge 1, b \ge 1$
- $f : R \to R$
- $\lim\limits_{n\to+\infty} f(n) \ge 0$ 

The equation:

$$
\begin{equation}
    \begin{cases}
        T(n) = aT(\frac{n}{b}) + f(n) \\
        T(1) = \theta(1)
    \end{cases}
\end{equation}
$$

There are three cases that can generate by comparing $f(n)$ with $n^{\log_{b}{a}}$:

1. $f(n) = O(n^{\log_{b}{a}-\epsilon}), \epsilon>0 \implies T(n) = \theta(n^{\log_{b}{a}})$
2. $f(n) = \theta(n^{\log_{b}{a}}), \implies T(n) = \theta(n^{\log_{b}{a}}\log{n})$
3. $f(n) = \omega(n^{\log_{b}{a}+\epsilon}), \epsilon>0 \land a\cdot f(\frac{n}{b}) \le cf(n), c<1, n>>1 \implies T(n) = \theta(f(n))$

The comparison must be polynomial, by an order of $n^\epsilon$. 

### Where not to apply it? 

In the following examples, the main method cannot be applied.

#### Ex 1

$$
\begin{equation}
    \begin{cases}
        T(n) = 2T(\frac{n}{2}) + \theta(n\log{n}) \\
        T(1) = \theta(1)
    \end{cases}
\end{equation}
$$

- $a=2, b=2$
- $f(n)=\theta(n\log{n})$
- $n^{\log_{b}{a}} = n^{\log_{2}{2}} = n$

In this case, $f(n)$ is asintotically bigger than n, but not plynomially bigger. In fact $\log{n} < n^\epsilon, \epsilon > 0$

#### Ex 2

$$
\begin{equation}
    \begin{cases}
        T(n) = 2T(\frac{n}{2}) + \theta(\frac{n}{\log{n}}) \\
        T(1) = \theta(1)
    \end{cases}
\end{equation}
$$

- $a=2, b=2$
- $f(n)=\theta(\frac{n}{\log{n}})$
- $n^{\log_{b}{a}} = n^{\log_{2}{2}} = n$

In this case, $f(n)$ is asintotically smaller than n, but not plynomially smaller. In fact $\log{n} < n^\epsilon, \epsilon > 0$
