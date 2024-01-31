# Problema degli accoppiamenti

Dato $ (\Omega, \mathbb{P}) $ uno schema probabilistico.
Sia $ f : \{ 1, 2, ..., n\} \to \{ 1, 2, ..., n \} $ biettiva, allora $i \in \{ 1, 2, ..., n \} $ è un **punto fisso** se $ f(i) = i $, 
calcolare la probabilità che una permutazione casuale **non abbia punti fissi**.

- $ \Omega = \{ (\omega_1, \omega_2, ..., \omega_n) \mid \omega_i \in \{1, 2, ..., n\} \land i \neq j \implies \omega_i \neq \omega_j \} \implies |\Omega| = n! $
- $ \mathbb{P} $ è la probabilità uniforme su $ \Omega $

Codifichiamo l'evento di cui si vuole calcolare la probabilità

$$
E = \{ (\omega_1, \omega_2, ..., \omega_n) \mid \omega_i \in \{1, 2, ..., n\} \land i \neq j \implies \omega_i \neq \omega_j \land \omega_i \neq i \}
$$

Questo è un problema per cui il passaggio a complemento si pone come una buona soluzione, per cui

$$
A = E^{\complement} = \{ (\omega_1, \omega_2, ..., \omega_n) \mid \omega_i \in \{1, 2, ..., n\} \land \exists i \in \{1, 2, ..., n\} : \omega_i = i \}
$$

Ora è possibile scrivere 

$$
A = \bigcup\limits_{k = 1}^{n} A_k \mid A_k = \{ (\omega_1, \omega_2, ..., \omega_n) \mid \omega_i \in \{1, 2, ..., n\} \land i \neq j \implies \omega_i \neq \omega_j \land \omega_k = k \}
$$

Dato che, per simmetria, gli eventi $ A_k $ hanno la stessa cardinalità, basta calcolare $ |A_1| $

$$
A_1 = \{ (\omega_1, \omega_2, ..., \omega_n) \mid \omega_i \in \{1, 2, ..., n\} \land i \neq j \implies \omega_i \neq \omega_j \land \omega_1 = 1 \} \implies \\
\implies |A_1| = (n - 1)! 
\implies \mathbb{P}(A_1) = \frac{|A_1|}{|\Omega|} = \frac{(n - 1)!}{n!} = \frac{1}{n} 
$$

Il problema è che gli eventi $A_1, A_2, ..., A_n $ **non sono disgiunti**, quindi bisogna usare il **PIE** per calcolare la cardinalità dell'unione, per cui servono le intersezioni

$$
A_1 \cap A_2 = \\
= \{ (\omega_1, \omega_2, ..., \omega_n) \mid \omega_i \in \{1, 2, ..., n\} \land i \neq j \implies \omega_i \neq \omega_j \land \omega_1 = 1 \land \omega_2 = 2\} \implies \\
\implies |A_1 \cap A_ 2| = (n - 2)! \implies \\
\implies \mathbb{P}(A_1 \cap A_2) = \frac{|A_1 \cap A_2|}{|\Omega|} = \frac{(n - 2)!}{n!} = \frac{1}{n(n-1)} 
$$

È possibile generalizzare per l'intersezione di $A_1, A_2, ..., A_{\mu}$ eventi, con $ \mu \leq n $
<!-- \bigcap\limits_{l = 1}^{\mu} A_l = \\ -->

$$
A_{\mu} = \bigcap\limits_{1 \leq l_1 \lt l_2 \lt \cdots \lt l_{\mu} \leq n} A_{l_i}  \\
= \{ (\omega_1, \omega_2, ..., \omega_n) \mid \omega_i \in \{1, 2, ..., n\} \land i \neq j \implies \omega_i \neq \omega_j \land \omega_{l_i} = l_i\} \implies \\
\implies |A_{\mu}| = (n - \mu)! \implies \\
\implies \mathbb{P}(A_{\mu}) = \frac{|A_{\mu}|}{|\Omega|} = \frac{(n - \mu)!}{n!} = \frac{1}{n(n-1)\cdots(n - \mu + 1)}
$$

Ora è possibile usare il **PIE** per ricavare la sommatoria completa

$$
\mathbb{P(A)} = 
$$

> TODO: completare
