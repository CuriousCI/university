# Assimoatica della probabilità

La probabilità si basa sugli assiomi introdotti da Andrey Kolmogorov nel 1933.
Uno schema probabilistico, o modello probabilistico, è composto da 3 oggetti \\((\Omega, \mathcal{A}, \mathbb{P})\\). 

1. \\( \Omega = \\{ \text{possibili risultati di un esperimento} \\} \\)
2. \\( \mathcal{A} = \\{ E \mid E \subseteq \Omega \\} = \mathcal{P}(\Omega) \\) 
    - \\( |\Omega| = n \implies |A| = 2^n \\)
    - \\( (\mathcal{A}, \cap, \cup, \complement) \\)
3. \\( \mathbb{P} : \mathcal{A} \to [0, 1] \\)
    - \\( \mathbb{P}(\emptyset) = 0 \\)
    - \\( \mathbb{P}(\Omega) = 1 \\)
    - \\( A, B \in \mathcal{A} \land A \cap B = \emptyset \implies \mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B)\\)

In alternativa al punto 3.

- \\( \mathbb{P} : \mathcal{A} \to [0, 1] \\)
    - \\( \forall E \in \mathcal{A}, \mathbb{P}(E) \in \mathbb{R} \land \mathbb{P}(E) \geq 0 \\)
    - \\( \mathbb{P}(\Omega) = 1 \\) 
    - \\( E\_1, E\_2, ..., E\_n \in \mathcal{A} \\)
        - \\( i \neq j \implies E\_i \cap E\_j = \emptyset \\)
        - \\( \mathbb{P}( \bigcup\limits_{i = 1}^n E\_i ) = \sum\limits_{i = 1}^n \mathbb{P}(E\_i) \\) 



\\( \Omega \\) è chiamato spazio degli eventi elementari _(o spazio campionario)_
\\(E \subseteq \Omega\\) è un evento, ovvero, una domanda _binaria_ sull'esito dell'esperimento
\\(\mathcal{A}\\) è l'algebra degli eventi 
\\( \mathbb{P} \\) è la probabilità
<!-- (per chiarire, se l'esperimento produce \\(12\\), la domanda è: "12 sta fra gli eventi elementari che sto considerando nel mio evento?") -->

## Conseguenze degli assiomi

> TODO: dimostrare le proprietà sotto

Monotonicità \\( A, B \in \mathcal{A}, A \subseteq B \implies \mathbb{P}(A) \leq \mathbb{P}(B) \\)

Probabilità dell'insieme vuoto \\( \mathbb{P}(\emptyset) = 0 \\)

Regola del complemento \\( E \in \mathcal{A}, \mathbb{P}(E^{\complement}) = 1 - \mathbb{P}(E)) \\)

Limite numerico \\( \forall E \in \mathcal{A}, 0 \leq \mathbb{P}(E) \leq 1 \\)

Altre conseguenze \\( A, B \in \mathcal{A}, \mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B) \\)

## Costruzione di \\( \mathbb{P} \\)

Sia \\( p : \Omega \to [0, 1] \\) ottenuta restringendo \\( \mathbb{P} \\) agli eventi elementari
\\( \forall \omega \in \Omega, p(\omega) := \mathbb{P}(\\{\omega\\}) : \\)
- \\( \forall \omega \in \Omega, 0 \leq p(\omega) \leq 1 \\)
- \\( \sum\limits_{\omega \in \Omega} p(\omega) = 1 \\)

Per il terzo assioma 
\\( \sum\limits_{\omega \in \Omega} p(\omega) = \sum\limits_{\omega \in \Omega} \mathbb{P}(\\{\omega\\}) = \mathbb{P}(\bigcup\limits_{\omega \in \Omega} \omega ) = \mathbb{P}(\Omega) = 1 \\)

## Probabilità uniforme

Si ha probabilità uniforme quando \\( p(\omega) = \frac{1}{|\Omega|} \implies \mathbb{P}(A = \bigcup\limits_{i=1}^{k} \\{\omega\_i\\}, k \leq |\Omega| ) = \frac{|A|}{|\Omega|} \\)
