#![allow(dead_code)]

use std::{collections::VecDeque, vec};

// enum Graph {
//     Directed,
//     Undirected,
// }
// fn generate_graph(graph_type: Graph) {
//     match graph_type {
//         Graph::Directed => (),
//         Graph::Undirected => (),
//     };
// }

fn find_cycle(graph: &[Vec<usize>], x: usize) -> Vec<usize> {
    let mut cycle: VecDeque<usize> = VecDeque::new();
    let mut visited: Vec<bool> = vec![false; graph.len()];
    cycle.push_back(x);

    let mut current = x;
    visited[current] = true;
    let mut next = graph[x][0];

    while !visited[next] {
        cycle.push_back(next);
        current = next;
        visited[current] = true;
        next = if visited[graph[current][0]] {
            graph[current][1]
        } else {
            graph[current][0]
        };
    }

    cycle.into_iter().skip_while(|&y| y != next).collect()
}

fn does_path_exist(graph: &[Vec<usize>], x: usize, y: usize) -> bool {
    let mut visited = vec![false; graph.len()];
    dfs(graph, x, &mut visited);

    visited[y]
}

fn dfs(graph: &[Vec<usize>], x: usize, visited: &mut Vec<bool>) {
    visited[x] = true;

    for &y in &graph[x] {
        if !visited[y] {
            dfs(graph, y, visited)
        }
    }
}

fn dfs_iterative(graph: &[Vec<usize>], node: usize) -> Vec<bool> {
    let mut stack = VecDeque::from([node]);
    let mut visited = vec![false; graph.len()];
    let mut indexes = vec![0; graph.len()];

    while let Some(&node) = stack.back() {
        if let Some(&neighbour) = graph[node].get(indexes[node]) {
            if !visited[neighbour] {
                stack.push_back(neighbour);
                visited[neighbour] = true;
            }

            indexes[node] += 1;
        } else {
            stack.pop_back();
        }
    }

    visited
}

pub fn find_components(graph: &Vec<Vec<usize>>) -> Vec<usize> {
    let mut visited = vec![false; graph.len()];
    let mut components = vec![0; graph.len()];
    let mut component = 0;

    for x in 0..graph.len() {
        if !visited[x] {
            dfs_components(graph, x, &mut visited, &mut components, component);
            component += 1;
        }
    }

    components
}

fn dfs_components(
    graph: &Vec<Vec<usize>>,
    x: usize,
    visited: &mut Vec<bool>,
    components: &mut Vec<usize>,
    component: usize,
) {
    visited[x] = true;
    components[x] = component;

    for &y in &graph[x] {
        if !visited[y] {
            dfs_components(graph, y, visited, components, component)
        }
    }
}

mod exercise {
    pub fn dfs(
        graph: &Vec<Vec<usize>>,
        x: usize,
        visited: &mut Vec<bool>,
        t: &mut Vec<(usize, usize)>,
        counter: usize,
    ) -> usize {
        visited[x] = true;
        let mut last = counter;

        for &y in &graph[x] {
            if !visited[y] {
                last = dfs(graph, y, visited, t, counter + 1)
            }
        }

        t[x] = (counter, last);
        last
    }
}

// G = (V, E)
// diretto
// aciclico \iff non ha cicli diretti
// pseudo codice per controllare se è aciclico o no con DFS
// si può fare in n + m?

fn dfs_cycles(graph: &[Vec<usize>], node: usize) -> bool {
    let mut stack = VecDeque::from([node]);
    let mut visited = vec![false; graph.len()];
    let mut indexes = vec![0; graph.len()];
    let mut first_visit = vec![0; graph.len()];

    let mut visited_nodes = 0;

    while let Some(&node) = stack.back() {
        if let Some(&neighbour) = graph[node].get(indexes[node]) {
            if !visited[neighbour] {
                stack.push_back(neighbour);
                visited[neighbour] = true;
                visited_nodes += 1;
                first_visit[neighbour] = visited_nodes;
            } else if first_visit[neighbour] < first_visit[node]
                && first_visit[neighbour] < visited_nodes
            {
                return true;
            }

            indexes[node] += 1;
        } else {
            stack.pop_back();
        }
    }

    false
}

// G = (V, E) non diretto si dice bipartito se
// V = U u W
// U n W = vuoto
// (u, V) in E, u in U, v in W o viceverso
// G è bipartito \iff G non ha cicli dispari O(n + m)

fn is_bipartite(graph: &[Vec<usize>]) -> bool {
    let mut visited = vec![false; graph.len()];
    let mut partitions = vec![false; graph.len()];

    for x in 0..graph.len() {
        if !visited[x] && !dfs_bipartite(graph, x, &mut visited, &mut partitions, true) {
            return false;
        }
    }

    true
}

fn dfs_bipartite(
    graph: &[Vec<usize>],
    x: usize,
    visited: &mut Vec<bool>,
    partitions: &mut Vec<bool>,
    partition: bool,
) -> bool {
    visited[x] = true;
    partitions[x] = partition;

    for &y in &graph[x] {
        if !visited[y] {
            if !dfs_bipartite(graph, y, visited, partitions, !partition) {
                return false;
            }
        } else if partitions[y] == partition {
            return false;
        }
    }

    true
}

// G = (V, E) grafo:

fn main() {
    let g1 = vec![
        vec![1, 2],
        vec![0, 4, 5],
        vec![0, 3, 4],
        vec![2, 4],
        vec![1, 2, 3],
        vec![1],
        vec![],
    ];

    let g2 = vec![vec![4], vec![2, 3], vec![1], vec![1, 4], vec![0, 3]];

    // println!("Is bipartite? {}", is_bipartite(&g1));
    // println!("Is bipartite? {}", is_bipartite(&g2));
    // println!("Does path exist? {}", does_path_exist(&g1, 1, 2));
    // println!("Does path exist? {}", does_path_exist(&g1, 1, 6));
    // println!("Does path exist? {}", does_path_exist(&g2, 1, 2));
    // println!("Does path exist? {}", does_path_exist(&g2, 0, 2));
    print!("Components {:?}", find_components(&g1));
    print!("Components {:?}", find_components(&g2));
}
