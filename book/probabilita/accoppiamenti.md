# Problema degli accoppiamenti

Dato \\( (\Omega, \mathbb{P}) \\) uno schema probabilistico.
Sia \\( f : \\{ 1, 2, ..., n\\} \to \\{ 1, 2, ..., n \\} \\) biettiva, allora \\(i \in \\{ 1, 2, ..., n \\} \\) è un **punto fisso** se \\( f(i) = i \\), 
calcolare la probabilità che una permutazione casuale **non abbia punti fissi**.

\\( \Omega = \\{ (\omega\_1, \omega\_2, ..., \omega\_n) \mid \omega\_i \in \\{1, 2, ..., n\\} \land i \neq j \implies \omega\_i \neq \omega\_j \\} \implies |\Omega| = n! \\), 
\\( \mathbb{P} \\) è la probabilità uniforme su \\( \Omega \\)

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

Il problema è che gli eventi \\(A\_1, A\_2, ..., A\_n \\) non sono disgiunti, quindi bisogna suare il **PIE** per calcolare la cardinalità dell'unione

$$
A\_1 \cap A\_2 = \\\\
= \\{ (\omega\_1, \omega\_2, ..., \omega\_n) \mid \omega\_i \in \\{1, 2, ..., n\\} \land i \neq j \implies \omega\_i \neq \omega\_j \land \omega\_1 = 1 \land \omega\_2 = 2\\} \implies \\\\
\implies |A\_1 \cap A\_ 2| = (n - 2)! 
\implies \mathbb{P}(A\_1 \cap A\_2) = \frac{|A\_1 \cap A\_2|}{|\Omega|} = \frac{(n - 2)!}{n!} = \frac{1}{n(n-1)} 
$$

È possibile generalizzare per \\( \mu \leq n, \bigcap\limits_{l = 1}^{\mu} A\_l = \\)
<!-- \bigcap\limits_{l = 1}^{\mu} A\_l = \\\\ -->

$$
= \\{ (\omega\_1, \omega\_2, ..., \omega\_n) \mid \omega\_i \in \\{1, 2, ..., n\\} \land i \neq j \implies \omega\_i \neq \omega\_j \land \forall l \in \\{1, 2, ..., \mu \\}, \omega\_l = l\\} \implies \\\\
\implies |\bigcap\limits_{l = 1}^{\mu} A\_l| = (n - \mu)! \implies \mathbb{P}(\bigcap\limits_{l = 1}^{\mu} A\_l ) = \frac{|\bigcap\limits_{l = 1}^{\mu} A\_l|}{|\Omega|} = \frac{(n - \mu)!}{n!} = \frac{1}{n(n-1)\cdots(n - \mu + 1)}
$$

Ora è possibile usare il **PIE** per ricavare la sommatoria completa...

> TODO: completare, il discorso è chiaro
