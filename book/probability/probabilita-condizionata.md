# Probabilità condizionata

Sia \\((\Omega, \mathbb{P})\\) uno schema probabilistico e \\( A, B \subseteq \Omega \\) eventi, si definisce la probabilità condizionata come:

$$
\mathbb{P}(B \mid A) := \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(A)}
$$

Sia \\( \mathbb{P} \\) la probabilità uniforme, allora:

$$
\mathbb{P}(B \mid A) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(A)} = \frac{\frac{|A \cap B|}{|\Omega|}}{\frac{|A|}{|\Omega|}} = \frac{|A \cap B|}{|A|}
$$

## Probabilità composte

Sia \\((\Omega, \mathbb{P})\\) uno schema probabilistico, e siano \\( A\_1, A\_2, ..., A\_k \subseteq \Omega \\) eventi

$$
\mathbb{P}(\bigcap_{i = 1}^{k} A\_i) = \\\\
= \mathbb{P}(A\_1)\mathbb{P}(A\_2 \mid A\_1)\mathbb{P}(A\_3 \mid A\_2 \cap A\_1) \cdots \mathbb{P}(A\_k \mid \bigcap_{i = 1}^{k - 1} A\_i) = \\\\
= \mathbb{P}(A\_1)\frac{\mathbb{P}(A\_2 \cap A\_1)}{\mathbb{P}(A\_1)}\frac{\mathbb{P}(A\_3 \cap A\_2 \cap A\_1)}{\mathbb{P}(A\_2 \cap A\_1)} \cdots \frac{\bigcap_{i = 1}^{k} A\_i}{\mathbb{P}(\bigcap_{i = 1}^{k - 1} A\_i)} = \\\\
= \mathbb{P}(\bigcap_{i = 1}^{k} A\_i)
$$

Sia \\((\Omega, \mathbb{P})\\) uno schema probabilistico, e siano \\( D\_1, D\_2, ..., D\_n \subseteq \Omega \mid \bigcup_{i = 1}^{n} D\_i = \Omega \land i \neq j \implies D\_i \neq D\_j \\) 
