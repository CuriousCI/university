# Problema degli accoppiamenti

Dato \\( (\Omega, \mathbb{P}) \\) uno schema probabilistico.
Sia \\( f : \\{ 1, 2, ..., n\\} \to \\{ 1, 2, ..., n \\} \\) biettiva, allora \\(i \in \\{ 1, 2, ..., n \\} \\) è un **punto fisso** se \\( f(i) = i \\), 
calcolare la probabilità che una permutazione casuale **non abbia punti fissi**.

- \\( \Omega = \\{ (\omega\_1, \omega\_2, ..., \omega\_n) \mid \omega\_i \in \\{1, 2, ..., n\\} \land i \neq j \implies \omega\_i \neq \omega\_j \\} \implies |\Omega| = n! \\)
- \\( \mathbb{P} \\) è la probabilità uniforme su \\( \Omega \\)

Codifichiamo l'evento di cui si vuole calcolare la probabilità

$$
E = \\{ (\omega\_1, \omega\_2, ..., \omega\_n) \mid \omega\_i \in \\{1, 2, ..., n\\} \land i \neq j \implies \omega\_i \neq \omega\_j \land \omega\_i \neq i \\}
$$

Questo è un problema per cui il passaggio a complemento si pone come una buona soluzione, per cui

$$
A = E^{\complement} = \\{ (\omega\_1, \omega\_2, ..., \omega\_n) \mid \omega\_i \in \\{1, 2, ..., n\\} \land \exists i \in \\{1, 2, ..., n\\} : \omega\_i = i \\}
$$

Ora è possibile scrivere 

$$
A = \bigcup\limits_{k = 1}^{n} A\_k \mid A\_k = \\{ (\omega\_1, \omega\_2, ..., \omega\_n) \mid \omega\_i \in \\{1, 2, ..., n\\} \land i \neq j \implies \omega\_i \neq \omega\_j \land \omega\_k = k \\}
$$

Dato che, per simmetria, gli eventi \\( A\_k \\) hanno la stessa cardinalità, basta calcolare \\( |A\_1| \\)

$$
A\_1 = \\{ (\omega\_1, \omega\_2, ..., \omega\_n) \mid \omega\_i \in \\{1, 2, ..., n\\} \land i \neq j \implies \omega\_i \neq \omega\_j \land \omega\_1 = 1 \\} \implies \\\\
\implies |A\_1| = (n - 1)! 
\implies \mathbb{P}(A\_1) = \frac{|A\_1|}{|\Omega|} = \frac{(n - 1)!}{n!} = \frac{1}{n} 
$$

Il problema è che gli eventi \\(A\_1, A\_2, ..., A\_n \\) **non sono disgiunti**, quindi bisogna usare il **PIE** per calcolare la cardinalità dell'unione, per cui servono le intersezioni

$$
A\_1 \cap A\_2 = \\\\
= \\{ (\omega\_1, \omega\_2, ..., \omega\_n) \mid \omega\_i \in \\{1, 2, ..., n\\} \land i \neq j \implies \omega\_i \neq \omega\_j \land \omega\_1 = 1 \land \omega\_2 = 2\\} \implies \\\\
\implies |A\_1 \cap A\_ 2| = (n - 2)! \implies \\\\
\implies \mathbb{P}(A\_1 \cap A\_2) = \frac{|A\_1 \cap A\_2|}{|\Omega|} = \frac{(n - 2)!}{n!} = \frac{1}{n(n-1)} 
$$

È possibile generalizzare per l'intersezione di \\(A\_1, A\_2, ..., A\_{\mu}\\) eventi, con \\( \mu \leq n \\)
<!-- \bigcap\limits_{l = 1}^{\mu} A\_l = \\\\ -->

$$
A\_{\mu} = \bigcap\limits_{1 \leq l\_1 \lt l\_2 \lt \cdots \lt l\_{\mu} \leq n} A\_{l\_i}  \\\\
= \\{ (\omega\_1, \omega\_2, ..., \omega\_n) \mid \omega\_i \in \\{1, 2, ..., n\\} \land i \neq j \implies \omega\_i \neq \omega\_j \land \omega\_{l\_i} = l\_i\\} \implies \\\\
\implies |A\_{\mu}| = (n - \mu)! \implies \\\\
\implies \mathbb{P}(A\_{\mu}) = \frac{|A\_{\mu}|}{|\Omega|} = \frac{(n - \mu)!}{n!} = \frac{1}{n(n-1)\cdots(n - \mu + 1)}
$$

Ora è possibile usare il **PIE** per ricavare la sommatoria completa

$$
\mathbb{P(A)} = 
$$

> TODO: completare
