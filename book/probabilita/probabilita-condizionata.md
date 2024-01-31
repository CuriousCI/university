# Probabilità condizionata

Sia $(\Omega, \mathbb{P})$ uno schema probabilistico e $ A, B \subseteq \Omega $ eventi, si definisce la probabilità condizionata come:

$$
\mathbb{P}(B \mid A) := \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(A)}
$$

Sia $ \mathbb{P} $ la probabilità uniforme, allora

$$
\mathbb{P}(B \mid A) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(A)} = \frac{\frac{|A \cap B|}{|\Omega|}}{\frac{|A|}{|\Omega|}} = \frac{|A \cap B|}{|A|}
$$

## Probabilità composte

Sia $(\Omega, \mathbb{P})$ uno schema probabilistico, e siano $ A_1, A_2, ..., A_k \subseteq \Omega $ eventi

$$
\mathbb{P}(\bigcap\limits_{i = 1}^{k} A_i) = \\
= \mathbb{P}(A_1)\mathbb{P}(A_2 \mid A_1)\mathbb{P}(A_3 \mid A_2 \cap A_1) \cdots \mathbb{P}(A_k \mid \bigcap\limits_{i = 1}^{k - 1} A_i) = \\
= \mathbb{P}(A_1)\frac{\mathbb{P}(A_2 \cap A_1)}{\mathbb{P}(A_1)}\frac{\mathbb{P}(A_3 \cap A_2 \cap A_1)}{\mathbb{P}(A_2 \cap A_1)} \cdots \frac{\bigcap\limits_{i = 1}^{k} A_i}{\mathbb{P}(\bigcap\limits_{i = 1}^{k - 1} A_i)} = \\
= \mathbb{P}(\bigcap\limits_{i = 1}^{k} A_i)
$$

## Probabilità totali

Sia $ (\Omega, \mathbb{P}) $ uno schema probabilistico, e siano $ D_1, D_2, ..., D_n \subseteq \Omega \mid \bigcup\limits_{i = 1}^{n} D_i = \Omega \land i \neq j \implies D_i \neq D_j $ 

## Formula di Bayes
