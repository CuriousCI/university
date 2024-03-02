# Algoritmi II

Un **grafo** è una coppia $(V, E)$, e si dice
\\(O(n)\\)

- **semplice** se ogni coppia di nodi è collegata con al massimo un arco, e non ci sono cappi
- *diretto* se gli archi sono orientati
- **connesso** se ogni coppia di nodi è collegata da una passeggiata

Due **nodi** si dicono _adiacenti_ se sono collegati da un arco, e l'arco si dice _incidente_ rispetto ai due nodi

Una **passeggiata** in un grafo $(V, E)$ è definita come una sequenza $V_0 e_1 V_1 e_2 V_2 e_3 V_3$ dove $e_i$ collega $V_{i - 1}$ a $V_i$

Una passeggiata si dice **euleriana** se attraversa ogni arco del grafo esattamente una volta

TEOREMA (di Eulero)

$\exists$ una passeggiata euleriana $\iff$ il grafo è connesso ed esistono al massimo 2 vertici di grado dispari

> TODO: complessità ricerca etc...

$O(n) + O(\sum\limits_{v \in V(G)} \deg(v))$

> PROBLEMA

input: grafo con ogni vertice di grado $\geq 2$
output: un ciclo un grafo _(come elenco di vicini)_
complessità: $O(n + m)$

DEF un **cammino è una passeggiata che non ripete vertici _(quindi neanche archi)_


- **fortemente connesso**: per ogni coppia di vertici esiste un cammino da x a y e viceversa

> PROBLEMA

dato un grafo G, esiste un cammino da X a Y?

> DFS

> PROBLEMA

dato un grafo G, determinare tutte le 
```rust
{{#include ./src/main.rs:3:25 }}
```
