# Variabile aleatoria di Poisson

Usata spesso in [teoria delle code](https://it.wikipedia.org/wiki/Teoria_delle_code), e la trovi anche [qui](https://it.wikipedia.org/wiki/Distribuzione_di_Poisson). 


Sia $\Delta t$ un intervallo piccolo di tempo, si ha che la probabilità

$$
\mathbb{P}(\text{cliente arrivi nell'intervallo } \Delta t) = \lambda \Delta t + o(\Delta t), \lambda \gt 0
$$

Arrivi in intervalli di tempo disgiunti sono **indipendenti**. Ora si consideri l'intervallo di tempo unitario 
$[0, 1] = \bigcup\limits_{i = 1}^n \bigl[\frac{i - 1}{n}, \frac{i}{n}\bigl]$, quindi suddiviso in $n$ intervalli

$$
X_i = \text{# di arrivi nell'intervallo } \biggl(\frac{i-1}{n}, \frac{i}{n}\biggl) = 
\begin{cases}
1 & \text{con probabilita' } & \frac{\lambda}{n} \\
0 & \text{con probabilita' } & 1 - \frac{\lambda}{n}
\end{cases} \implies \\
\implies X_i \sim \text{Bernoulli}\biggl(\frac{\lambda}{n}\biggl)
$$

Per cui 

$$
X^{(n)} = \text{# di arrivi nell'intervallo } [0, 1] = 
\sum\limits_{i = 1}^n X_i \implies X^{(n)} \sim \text{Bin}\biggl(n, \frac{\lambda}{n}\biggl)
$$

## Teorema di Poisson

Siano $\lambda \in (0, 1), X^{(n)} \sim Bin\biggl(n, \frac{\lambda}{n}\biggl)$, con $n$ grande abbastanza. 
Fissando $k = 0, 1, ..., n$, allora $\lim\limits_{n\to\infty} \mathbb{P}(X^{(n)} = k) = \frac{e^{-\lambda}\lambda^k}{k!}$

> TODO: Dimostrazione

## Distribuzione

$ \mathbb{P}(X^{(n)} = k) = \frac{e^{-\lambda}\lambda^k}{k!}$
> TODO: Dimostrazione distribuzione

## Valore di attesa

$
\mathbb{E}(X) = \lambda
$

### Dimostrazione

$ 
\mathbb{E}(X) = \sum\limits_{k = 0}^{\infty} k \mathbb{P}(X = k) = 
\sum\limits_{k = 1}^{\infty} k \mathbb{P}(X = k) = 
\sum\limits_{k = 1}^{\infty} k \frac{e^{-\lambda}\lambda^k}{k!} = 
e^{-\lambda} \sum\limits_{k = 1}^{\infty} \frac{\lambda^k}{(k - 1)!} \\
h = k - 1 \implies e^{-\lambda} \sum\limits_{h = 0}^{\infty} \frac{\lambda^{h + 1}}{h!} = 
\lambda e^{-\lambda} \sum\limits_{h = 0}^{\infty} \frac{\lambda^h}{h!} = 
\lambda e^{-\lambda} e^{\lambda} = \lambda
$

## Varianza

$
\mathbb{V}(X) = \lambda
$

### Dimostrazione

$
\mathbb{V}(X) = \lim\limits_{n \to \infty} \mathbb{V}(X^{(n)}) = \lim\limits_{n \to \infty} n\frac{\lambda}{n}\bigl(1 - \frac{\lambda}{n}\bigl) = 
\lim\limits_{n \to \infty} \lambda - \frac{\lambda^2}{n} = \lambda
$

## Complementare

> TODO
