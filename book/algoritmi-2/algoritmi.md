# Algoritmi II

Un **grafo** $G$ è una coppia $(V, E)$ dove $V$ è un insieme di vertici ed $E$ un insieme di nodi; un grafo si dice
- **semplice** se ogni coppia di nodi è collegata con al massimo un arco, e non ci sono cappi
- **diretto** se gli archi sono orientati
- **connesso** se ogni coppia di nodi è collegata da una passeggiata
- **fortemente connesso** se per ogni coppia di vertici $x, y$ esiste un cammino da $x$ a $y$ e viceversa

Due **nodi** $x, y$ si dicono _adiacenti_ ($x \sim y$) se sono collegati da un arco, e l'arco si dice _incidente_ rispetto ai due nodi

## Rappresentazione

Un grafo $G = (V, E)$ si può rappresentare tramite *matrice di adiacenza* o *lista di adiacenza* 

### Matrice di adiacenza

Siano $V_1, V_2, ..., V_n$ i vertici del grafo, possiamo rappresentare il grafo come una matrice $v$ tale che 

$$
(v)_{ij} = 
\begin{cases}
1 & \text{se } V_i \text{è adiacente a } V_j\\
0 & \text{altrimenti}
\end{cases}
$$

<br />

<style>
.matrix td {
    padding: 3px 5px !important;
    text-align: center;
}

blockquote > h4 {
    margin-bottom: 0;
    margin-top: 16px;
}
</style>

<div class="matrix">

| | | | | |
|--|--|--|--|--|
| | $V_1$ | $V_2$ | ... | $V_n$ |
| $V_1$ | 0 | 1 | ... | 0 |
| $V_2$ | 1 | 0 | ... | 1 | 
| ... | ... | ... | ... | ... | 
| $V_n$ | 0 | 1 | ... | 0 |

</div>

Per verificare se $V_i \sim V_j$ il costo è $O(1)$
la dimensione della matrice è $O(n^2)$ con
- $n = |V(G)|$

### Lista di adiacenza

Siano $V_1, V_2, ..., V_n$ i vertici del grafo, possiamo indicare per ogni nodo l'insieme dei suoi vicini


<div class="matrix">

| | | 
|--|--|
| $V_1$ | $\set{V_3, V_4, ...}$ |
| $V_2$ | $\set{V_5, V_n, ...}$ | 
| ... | $\set{...}$ |
| $V_n$ | $\set{V_2, V_5, ...}$ |

</div>

Per verificare se $V_i \sim V_j$ il costo è $O(n)$
la dimensione della matrice è $O(n + m)$, con
- $n = |V(G)|$ 
- $m = \sum\limits_{v \in V(G)} \deg(v) = 2 |E(G)|$

## Teoremi

> #### Definizione
> Una **passeggiata** in un grafo $(V, E)$ è definita come una sequenza $V_0 e_1 V_1 e_2 V_2 e_3 V_3$ dove $e_i$ collega $V_{i - 1}$ a $V_i$

> #### Definizione
> Una passeggiata si dice **euleriana** se attraversa ogni arco del grafo esattamente una volta

> #### Teorema di Eulero
> $\exists$ una passeggiata euleriana $\iff$ il grafo è connesso ed esistono al massimo 2 vertici di grado dispari

> #### Definizione
> Un **cammino** è una passeggiata che non ripete vertici _(quindi neanche archi)_

> #### Definizione
> Un **ciclo** in un grafo è un **sottografo connesso** con ogni vertice di grado 2

> #### Osservazione
> Se $\exists$ una passeggiata da $x$ a $y \implies \exists$ un cammino da $x$ a $y$

si dimostra con l'algoritmo


## DFS _(depth first search)_

<!-- ```rust -->
<!-- {{#include ./src/main.rs:27:35 }} -->
<!-- ``` -->

```rust
{{#include ./src/main.rs:37:56 }}
```

Dimostrazione correttezza: bisogna dimostrare che 

> se $\exists$ un cammino da $x$ a $y \implies y \in \text{visited}$ 

per assurdo, supponiamo che $\exists y \mid x \to y \land y \notin \text{visited}$

|  |  |  |  |  |
|--|--|--|--|--|
| $V_0$ | $V_1$ | $V_2$ | ... | $V_n$ |
| $x$ | ... | ... | ... | $y$ |

Sia $i$ un indice $V_i \in \text{visited}, V_{i + 1} \notin \text{visited}$

$V_i \in \text{visited} \implies V_i$ è stato inserito nello stack $\implies$ ma se $V_i \in$ stack e $V_{i + 1} \notin$ stack $\implies$ l'algoritmo non è stato eseguito correttamente _(contraddizione!)_

> TODO: complessità $O(n + m)$

> #### Definizione
> L'**albero di visita** è un sottografo composto dagli archi che usiamo per raggiungere i vertici nuovi non ancora visitati
> - è connesso
> - è aciclico

> #### Definizione
> L'**albero di visita** di un grafo **diretto** è detto **arborescenza** 
> - diretto
> - ogni arco orientato dalla radice alle foglie

Se $G$ è un graffo connesso $\implies \text{visited}$ contiene tutti i nodi del grafo

Se $G$ non è connesso $\implies \text{visited}$ è il componennte che contiene $X$

## Ordine topologico

Consideriamo un progetto diviso in $X_1, X_2, ..., X_n$ task, con dipendenze fra i vari task (Es. $X_1$ va eseguito dopo $X_2$ e $X_3$, e $X_3$ dopo $X_2$; in questo caso l'ordine sarebbe $X_2, X_3, X_1$)

Indicando i vertici con $X_1, X_2, ..., X_n$ e gli archi con $(X_i, X_j)$ se $X_i$ dipende da $X_j$, una **programmazione dei task** corrisponde ad un ordine dei vertici con tutti gli **archi da destra verso sinistra**

Se il grafo ha un ciclo _(diretto)_, non è possibile dare un **ordine topologico**

#### Dimostrazione

Suppponiamo per assurdo che esiste un tale ordine, allora uno dei vertici deve essere per forza l'ultimo nell'ordine; ma essendo ciclico esiste un arco che va da sinistra verso destra da uno dei vertici "centrali" della sequenza all'ultimo vertice, quindi tale ordine non esiste.

> #### Definizione
> Un grafo diretto ha un **ordine topologico** se $\exists$ un ordine deivertici con tutti gli ordini degli archi da destra verso sinistra

> #### Proposizione
> Se un grafo diretto ha la proprietà che ogni vertice ha almeno un arco uscente $\implies \exists$ un ciclo

stessa dimostrazione dell'algoritmo del primo giorno: se ogni vertice  ha un arco uscente e i vertici sono finiti, alora prima o poi dovrà tornare... (creare un ciclo) 

L'implicazione $\impliedby$ non è vera!

> #### Corollario
> Se $\notexists$ un ciclo $\implies \exists$ un nodo senza archi uscenti

### Soluzione naive

> TODO: algoritmo $O(n(n + m))$ per trovare l'ordine topologico!

### Soluzione con DFS




