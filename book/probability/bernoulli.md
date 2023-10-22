# Schema di Bernoulli

Lo schema di Bernoulli rappresenta un **esperimento binario** ripetutto \\(n\\) volte:
 - tradizionalmente \\(n\\) lanci di moneta non necessariamente equa
 - la trasmissione di \\(n\\) bit su un cavo con disturbi (1 mi indica che il bit è arrivato corretamente, 0 altrimenti), schema in cui la probabilità di errore (di 0) deve essere bassa 

Si codificano i risultati con \\( \\{0, 1\\} \\) (per comodità dei calcoli successivamente)

$$
\Omega = \\{ (\omega\_1, ..., \omega\_2) \mid \omega\_i \in \\{0, 1\\} \\} =\\\\
= \\{0, 1\\} \times \\{0, 1\\} \times ... \times \\{0, 1\\} = \\{0, 1\\}^n
$$

La scelta naturale è la **probabilità prodotto** su singolo lancio, dove \\(p\\) indica la "truccatura" della moneta

$$
\Omega\_1 = \\{0, 1\\}\\\\
\mathbb{P}(\\{0\\}) = 1 - p\\\\
\mathbb{P}(\\{1\\}) = p
$$

Lo schema si indica con \\( (n, p) \\)

|n|\\(\Omega\\)|
|-|-|
|1|\\(\\{0, 1\\}\\) |
|2|\\(\\{00, 01, 10, 11\\}\\) |
|3|\\(\\{000, 001, 010, 011, 100, 101, 110, 111\\}\\) |

- \\( n = 1 \\)

$$
\mathbb{P}(\\{0\\}) = 1 - p\\\\
\mathbb{P}(\\{1\\}) = p
$$

- \\( n = 2 \\)

$$
\mathbb{P}(\\{00\\}) = (1 - p)^2\\\\
\mathbb{P}(\\{01\\}) = (1 - p) \cdot p\\\\
\mathbb{P}(\\{10\\}) = p \cdot (1 - p)\\\\
\mathbb{P}(\\{11\\}) = p^2 
$$

- \\( n = 3 \\)

$$
\mathbb{P}(\\{000\\}) = (1 - p)^3\\\\
\mathbb{P}(\\{001\\}) = (1 - p)^2 \cdot p\\\\
\mathbb{P}(\\{010\\}) = (1 - p)^2 \cdot p\\\\
\mathbb{P}(\\{011\\}) = (1 - p) \cdot p^2\\\\
\mathbb{P}(\\{100\\}) = (1 - p)^2 \cdot p\\\\
\mathbb{P}(\\{101\\}) = (1 - p) \cdot p^2\\\\
\mathbb{P}(\\{110\\}) = (1 - p) \cdot p^2\\\\
\mathbb{P}(\\{111\\}) = p^3\\\\
$$

In generale

$$
\mathbb{P}(\\{ \omega\_1, ..., \omega\_n \\}) = p^{\sum_{i = 1}^{n} \omega\_i} \cdot (p - 1)^{1 - \sum_{i = 1}^{n} \omega\_i}
$$

<!-- TODO: Esempi -->

