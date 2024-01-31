# Variabile aleatoria geometrica 

Usata tipicamente in [teoria dell'affidabilità](https://it.wikipedia.org/wiki/Teoria_dell%27affidabilit%C3%A0). Si ipotizza un macchinario che opera a cicli, e la trovi anche [qui](https://it.wikipedia.org/wiki/Distribuzione_geometrica).

Siano
- $p$ la probabilità di rottura ad ogni ciclo
- $X$ il tempo di rottura _(dopo quanti cicli si è rotto)_

Per cui $\Omega = \{ 0, 1 \}^{\mathbb{N}} $, quindi la v.a. geometrica è uno schema di Bernoulli con infiniti lanci e $\mathbb{P}$ probabilità prodotto, $X \sim \text{Geom}(p), p \in (0, 1)$

## Distribuzione

$
\Im(X) = \{ 1, 2, 3, ..., n, ... \} = \mathbb{N} \setminus \{ 0 \} = \mathbb{N}^* \\
\mathbb{P}(X=k) = \mathbb{P}(\{(\omega_1, \omega_2, ..., \omega_k) \mid \omega_1 = \omega_2 = \cdots = \omega_{k - 1} = 0 \land \omega_k = 1\}) = (1 - p)^{k - 1}p
$

## Valore di attesa

$
\mathbb{E}(X) = \frac{1}{p}
$

### Dimostrazione

$
\mathbb{E}(X) = \sum\limits_{k = 1}^{\infty} \mathbb{E}(X_i = k) = 
\sum\limits_{k = 0}^{\infty} \mathbb{E}(X_i = k) = \\
\sum\limits_{k = 0}^{\infty} k(1-p)^{k - 1}p =
p\sum\limits_{k = 0}^{\infty} k(1-p)^{k - 1} = 
p\sum\limits_{k = 0}^{\infty} \frac{d}{d(1-p)}(1-p)^{k} = \\
= p\frac{d}{d(1-p)}\sum\limits_{k = 0}^{\infty} (1-p)^{k} = 
p\frac{d}{d(1-p)}\sum\limits_{k = 0}^{\infty} (1-p)^{k} = \\
= p \frac{d}{d(1-p)}\biggl(\frac{1}{1 - (1-p)}\biggl) = p (\frac{1}{p})^2 = \frac{1}{p}
$

## Varianza

$
\mathbb{V}(X) = \frac{(1-p)}{p^2} 
$

## Perdita di memoria

Sia $G(n) = (1 - p)^n$ la **funzione di sopravvivenza** tale che 

$$
G(n) = \mathbb{P}(\text{la macchina sopravvive i primi } n \text{ cicli}) = \\
= \mathbb{P}(X > n) = \sum\limits_{k = n + 1}^{\infty} \mathbb{P}(X=k) = \sum\limits_{k = n + 1}^{\infty} (1-p)^{k - 1}p \implies \\
\implies h = k - n - 1 \implies \sum\limits_{h = 0}^{\infty} (1-p)^{h + n}p = \\
= p(1 - p)^n \sum\limits_{h = 0}^{\infty} p(1-p)^h = (1 - p)^n
$$

Ora possiamo determinare che $\mathbb{P}(X = n + l \mid X > n) = \mathbb{P}(X = l)$, dato che

$$
\mathbb{P}(X = n + l \mid X > n) = \\
= \frac{\mathbb{P}(X = n + l, X > n)}{\mathbb{P}(X > n)} = 
\frac{\mathbb{P}(X = n + l)}{\mathbb{P}(X > n)} =
\frac{(1 - p)^{n + l - 1}p}{(1 - p)^n} = \\
= (1 - p)^{l - 1}p = \mathbb{P}(X = l)
$$
