# Esercizi

## Ciclo in un grafo 

- `input` un grafo $G \mid \forall v \in V(G), \deg(v) \geq 2$
- `output` un ciclo un grafo _(come elenco di vicini)_
- `complessità` $O(n + m)$

```rust
{{#include ./src/main.rs:3:25 }}
```

## Cammino da $x$ a $y$

- `input` un grafo $G$ e $x, y \in V(G)$ 
- `output` $x \sim y ?$ 
- `complessità` $O(n + m)$

<!-- dato un grafo G, esiste un cammino da X a Y? Si fa con una visita! -->

```rust
{{#include ./src/main.rs:27:35 }}
```

```rust
{{#include ./src/main.rs:37:56 }}
```

```rust
fn path(graph: &Vec<Vec<usize>>, x: usize, y: usize) -> bool {
    dfs_iterative(graph, x)[y]
}
```

## Componenti di $G$

- `input` un grafo $G$
- `output` l'elenco di archi in **avanti**, **indietro** e di **attraversamento** 
- `complessità` $O(n + m)$

```rust
{{#include ./src/main.rs:58:85 }}
```

## Classificazione archi 

- `input` un grafo $G$
- `output` le componenti di $G$ 
- `complessità` $O(n + m)$
