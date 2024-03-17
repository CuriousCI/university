#![allow(dead_code)]

use std::{collections::VecDeque, vec};

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

fn dfs_iterative(graph: &[Vec<usize>], x: usize) -> Vec<bool> {
    let mut stack = Vec::from([x]);
    let mut visited = vec![false; graph.len()];
    let mut adjacent = vec![0; graph.len()];

    while let Some(&x) = stack.last() {
        if let Some(&y) = graph[x].get(adjacent[x]) {
            if !visited[y] {
                stack.push(y);
                visited[y] = true;
            }

            adjacent[x] += 1;
        } else {
            stack.pop();
        }
    }

    visited
}

pub fn find_components(graph: &[Vec<usize>]) -> Vec<usize> {
    let mut components = vec![0; graph.len()];
    let mut component = 1;

    for x in 0..graph.len() {
        if components[x] == 0 {
            dfs_components(graph, x, &mut components, component);
            component += 1;
        }
    }

    components
}

fn dfs_components(graph: &[Vec<usize>], x: usize, components: &mut Vec<usize>, component: usize) {
    components[x] = component;

    for &y in &graph[x] {
        if components[y] == 0 {
            dfs_components(graph, y, components, component)
        }
    }
}

// let mut visited = vec![false; graph.len()];
// if !visited[x] {
// dfs_components(graph, x, &mut visited, &mut components, component);
// visited: &mut Vec<bool>,
// visited[x] = true;
// if !visited[y] {
// dfs_components(graph, y, visited, components, component)

fn bridges(graph: &[Vec<usize>]) -> Vec<(usize, usize)> {
    let mut first_visit = vec![0; graph.len()];
    let mut bridges: Vec<(usize, usize)> = vec![];
    let mut visit = 0;

    dfs_bridges(graph, 0, 0, &mut visit, &mut first_visit, &mut bridges);

    bridges
}

fn dfs_bridges(
    graph: &[Vec<usize>],
    x: usize,
    z: usize,
    visit: &mut usize,
    first_visit: &mut Vec<usize>,
    bridges: &mut Vec<(usize, usize)>,
) -> usize {
    *visit += 1;
    first_visit[x] = *visit;
    let mut back = *visit;

    for &y in &graph[x] {
        if y == z {
            back = back.min(match first_visit[y] {
                0 => dfs_bridges(graph, y, x, visit, first_visit, bridges),
                v => v,
            })
        }
    }

    if back == first_visit[x] && x != z {
        bridges.push((z, x));
    }

    back
}

// if first_visit[y] == 0 {
//     back = back.min(dfs_bridges(graph, y, x, visit, first_visit, bridges))
// } else if first_visit[y] < back && y != z {
//     back = first_visit[y]
// }

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

fn to_dag(graph: &[Vec<usize>]) -> Vec<Vec<usize>> {
    let mut visited = vec![false; graph.len()];
    let mut signed = vec![false; graph.len()];
    let mut new_graph = vec![Vec::new(); graph.len()];

    dag_dfs(graph, 0, &mut visited, &mut signed, &mut new_graph);

    new_graph
}

fn dag_dfs(
    graph: &[Vec<usize>],
    x: usize,
    visited: &mut Vec<bool>,
    signed: &mut Vec<bool>,
    new_graph: &mut [Vec<usize>],
) {
    visited[x] = true;

    for &y in &graph[x] {
        if !visited[y] {
            new_graph[x].push(y);
            dag_dfs(graph, y, visited, signed, new_graph)
        } else if !signed[x] {
            new_graph[y].push(x);
            signed[x] = true;
        }
    }
}

fn cutvertexes(graph: &[Vec<usize>]) -> Vec<usize> {
    let mut first_visit = vec![0; graph.len()];
    let mut cutvertexes = vec![];
    let mut visit = 0;

    dfs_cutvertexes(graph, 0, &mut visit, &mut first_visit, &mut cutvertexes);

    cutvertexes
}

fn dfs_cutvertexes(
    graph: &[Vec<usize>],
    x: usize,
    visit: &mut usize,
    first_visit: &mut Vec<usize>,
    cutvertexes: &mut Vec<usize>,
) -> usize {
    *visit += 1;
    first_visit[x] = *visit;

    let mut back = *visit;

    for &y in &graph[x] {
        back = back.min(match first_visit[y] {
            0 => dfs_cutvertexes(graph, y, visit, first_visit, cutvertexes),
            _ => first_visit[y],
        })
    }

    if back == first_visit[x] && *visit > 1 {
        cutvertexes.push(x);
    }

    back
}

// back = back.min(if first_visit[y] == 0 {
//     dfs_cutvertexes(graph, y, visit, first_visit, cutvertexes)
// } else {
//     first_visit[y]
// });

fn main() {
    let g1 = vec![
        vec![1, 2],
        vec![0, 4, 5],
        vec![0, 3, 4],
        vec![2, 4],
        vec![1, 2, 3, 5],
        vec![1, 4],
    ];

    let g2 = vec![vec![4], vec![2, 3], vec![1], vec![1, 4], vec![0, 3]];
    let g3 = vec![
        vec![1, 2],
        vec![0, 2],
        vec![0, 1, 3],
        vec![2, 4, 5],
        vec![3],
        vec![3],
    ];

    println!("{:?}", bridges(&g2));
    println!("{:?}", bridges(&g3));

    println!("{:?}", cutvertexes(&g1));
    println!("{:?}", cutvertexes(&g2));
    println!("{:?}", cutvertexes(&g3));
}

// println!("{:?}", to_dag(&g1));
// println!("{:?}", find_cycle(&g1, 0));
// println!("{:?}", find_cycle(&g1, 3));
// println!("{:?}", find_cycle(&g2, 0));
// println!("{:?}", find_cycle(&g3, 2));

// println!("Is bipartite? {}", is_bipartite(&g1));
// println!("Is bipartite? {}", is_bipartite(&g2));
// println!("Does path exist? {}", does_path_exist(&g1, 1, 2));
// println!("Does path exist? {}", does_path_exist(&g1, 1, 6));
// println!("Does path exist? {}", does_path_exist(&g2, 1, 2));
// println!("Does path exist? {}", does_path_exist(&g2, 0, 2));
// print!("Components {:?}", find_components(&g1));
// print!("Components {:?}", find_components(&g2));

// mod exercise {
//     pub fn dfs(
//         graph: &Vec<Vec<usize>>,
//         x: usize,
//         visited: &mut Vec<bool>,
//         t: &mut Vec<(usize, usize)>,
//         counter: usize,
//     ) -> usize {
//         visited[x] = true;
//         let mut last = counter;
//
//         for &y in &graph[x] {
//             if !visited[y] {
//                 last = dfs(graph, y, visited, t, counter + 1)
//             }
//         }
//
//         t[x] = (counter, last);
//         last
//     }
// }

// G = (V, E)
// diretto
// aciclico \iff non ha cicli diretti
// pseudo codice per controllare se è aciclico o no con DFS
// si può fare in n + m?
// <<<<<<< HEAD

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

fn find_cycle(graph: &[Vec<usize>], mut x: usize) -> Vec<usize> {
    let mut cycle = vec![];
    let mut visited = vec![false; graph.len()];

    let mut z = x;
    while !visited[x] {
        cycle.push(x);
        visited[x] = true;

        let next = if graph[x][0] == z { 1 } else { 0 };
        z = x;
        x = graph[x][next];
    }

    cycle.into_iter().skip_while(|&y| y != x).collect()
}

fn categorize_edges(
    graph: &[Vec<usize>],
) -> (
    Vec<(usize, usize)>,
    Vec<(usize, usize)>,
    Vec<(usize, usize)>,
) {
    let mut forward = vec![];
    let mut backward = vec![];
    let mut traversal = vec![];

    let mut visited = vec![false; graph.len()];
    let mut first_visit = vec![0; graph.len()];
    let mut last_visit = vec![0; graph.len()];

    dfs_edges(
        graph,
        0,
        &mut visited,
        1,
        &mut first_visit,
        &mut last_visit,
        &mut forward,
        &mut backward,
        &mut traversal,
    );

    (forward, backward, traversal)
}

fn dfs_edges(
    graph: &[Vec<usize>],
    x: usize,
    visited: &mut Vec<bool>,
    visited_count: usize,
    first_visit: &mut Vec<usize>,
    last_visit: &mut Vec<usize>,
    forward: &mut Vec<(usize, usize)>,
    backward: &mut Vec<(usize, usize)>,
    traversal: &mut Vec<(usize, usize)>,
) -> usize {
    first_visit[x] = visited_count;
    let mut closing_time = visited_count;

    for &y in &graph[x] {
        if !visited[y] {
            closing_time = closing_time.max(dfs_edges(
                graph,
                y,
                visited,
                visited_count + 1,
                first_visit,
                last_visit,
                forward,
                backward,
                traversal,
            ))
        } else {
            // classifica l'arco!
        }
    }

    last_visit[x] = closing_time;

    closing_time
}

fn main() {
    let g1 = vec![
        vec![1, 2],
        vec![0, 4, 5],
        vec![0, 3, 4],
        vec![2, 4],
        vec![1, 2, 3, 5],
        vec![1, 4],
    ];

    let g2 = vec![vec![4], vec![2, 3], vec![1], vec![1, 4], vec![0, 3]];
    let g3 = vec![
        vec![1, 2],
        vec![0, 2],
        vec![0, 1, 3],
        vec![2, 4, 5],
        vec![3],
        vec![3],
    ];
    let g4 = vec![
        vec![1, 5],
        vec![0, 2],
        vec![1, 3],
        vec![2, 4],
        vec![3, 5],
        vec![4, 0],
    ];

    println!("{:?}", find_cycle(&g1, 0));
    println!("{:?}", find_cycle(&g1, 3));
    println!("{:?}", find_cycle(&g4, 0));
    println!("{:?}", find_cycle(&g4, 3));
    // println!("{:?}", find_cycle(&g2, 0));
    // println!("{:?}", find_cycle(&g3, 2));

    // println!("{:?}", bridges(&g2));
    // println!("{:?}", bridges(&g3));

    // println!("Is bipartite? {}", is_bipartite(&g1));
    // println!("Is bipartite? {}", is_bipartite(&g2));
    // println!("Does path exist? {}", does_path_exist(&g1, 1, 2));
    // println!("Does path exist? {}", does_path_exist(&g1, 1, 6));
    // println!("Does path exist? {}", does_path_exist(&g2, 1, 2));
    // println!("Does path exist? {}", does_path_exist(&g2, 0, 2));
    // print!("Components {:?}", find_components(&g1));
    // print!("Components {:?}", find_components(&g2));
}
=======
//
// fn dfs_cycles(graph: &[Vec<usize>], node: usize) -> bool {
//     let mut stack = VecDeque::from([node]);
//     let mut visited = vec![false; graph.len()];
//     let mut indexes = vec![0; graph.len()];
//     let mut first_visit = vec![0; graph.len()];
//
//     let mut visited_nodes = 0;
//
//     while let Some(&node) = stack.back() {
//         if let Some(&neighbour) = graph[node].get(indexes[node]) {
//             if !visited[neighbour] {
//                 stack.push_back(neighbour);
//                 visited[neighbour] = true;
//                 visited_nodes += 1;
//                 first_visit[neighbour] = visited_nodes;
//             } else if first_visit[neighbour] < first_visit[node]
//                 && first_visit[neighbour] < visited_nodes
//             {
//                 return true;
//             }
//
//             indexes[node] += 1;
//         } else {
//             stack.pop_back();
//         }
//     }
//
//     false
// }
//
// // G = (V, E) non diretto si dice bipartito se
// // V = U u W
// // U n W = vuoto
// // (u, V) in E, u in U, v in W o viceverso
// // G è bipartito \iff G non ha cicli dispari O(n + m)
//
// fn is_bipartite(graph: &[Vec<usize>]) -> bool {
//     let mut visited = vec![false; graph.len()];
//     let mut partitions = vec![false; graph.len()];
//
//     for x in 0..graph.len() {
//         if !visited[x] && !dfs_bipartite(graph, x, &mut visited, &mut partitions, true) {
//             return false;
//         }
//     }
//
//     true
// }
//
// fn dfs_bipartite(
//     graph: &[Vec<usize>],
//     x: usize,
//     visited: &mut Vec<bool>,
//     partitions: &mut Vec<bool>,
//     partition: bool,
// ) -> bool {
//     visited[x] = true;
//     partitions[x] = partition;
//
//     for &y in &graph[x] {
//         if !visited[y] {
//             if !dfs_bipartite(graph, y, visited, partitions, !partition) {
//                 return false;
//             }
//         } else if partitions[y] == partition {
//             return false;
//         }
//     }
//
//     true
// }
//
// // G = (V, E) grafo:
//
// fn find_cycle(graph: &[Vec<usize>], mut x: usize) -> Vec<usize> {
//     let mut cycle = vec![];
//     let mut visited = vec![false; graph.len()];
//
//     let mut z = x;
//     while !visited[x] {
//         cycle.push(x);
//         visited[x] = true;
//
//         let next = if graph[x][0] == z { 1 } else { 0 };
//         z = x;
//         x = graph[x][next];
//     }
//
//     cycle.into_iter().skip_while(|&y| y != x).collect()
// }
// >>>>>>> 5e70d2e959233cc1990e85479a11f9d901fb3601
