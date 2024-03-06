use std::{collections::VecDeque, vec};

fn find_cycle(graph: &[Vec<usize>], x: usize) -> Vec<usize> {
    let mut cycle: VecDeque<usize> = VecDeque::new();
    cycle.push_back(x);

    let mut current = x;
    let mut next = graph[x][0];

    let mut visited: Vec<bool> = vec![false; graph.len()];
    visited[current] = true;

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

    cycle.into_iter().collect()
}

fn dfs(graph: &[Vec<usize>], node: usize, visited: &mut Vec<bool>) {
    visited[node] = true;

    for &neighbour in &graph[node] {
        if !visited[neighbour] {
            dfs(graph, neighbour, visited)
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

fn dfs_components(
    graph: &Vec<Vec<usize>>,
    node: usize,
    components: &mut Vec<usize>,
    component: usize,
) {
    components[node] = component;
    for &neighbour in &graph[node] {
        if components[neighbour] == 0 {
            dfs_components(graph, neighbour, components, component)
        }
    }
}

pub fn components(graph: &Vec<Vec<usize>>) -> Vec<usize> {
    let mut components = vec![0; graph.len()];
    let mut component = 1;

    for node in 0..graph.len() {
        if components[node] == 0 {
            components[node] = component;
            dfs_components(graph, node, &mut components, component);
            component += 1;
        }
    }

    components
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

fn bipartition(graph: &[Vec<usize>]) -> bool {
    let mut visited = vec![false; graph.len()];

    for node in 0..graph.len() {
        if !visited[node] {
            let mut partitions = vec![false; graph.len()];
            if !dfs_bipartito(graph, node, &mut visited, &mut partitions, true) {
                return false;
            }
        }
    }

    true
}

fn dfs_bipartito(
    graph: &[Vec<usize>],
    node: usize,
    visited: &mut Vec<bool>,
    partitions: &mut Vec<bool>,
    partition: bool,
) -> bool {
    visited[node] = true;
    partitions[node] = partition;

    for &neighbour in &graph[node] {
        if !visited[neighbour] && !dfs_bipartito(graph, neighbour, visited, partitions, !partition)
        {
            return false;
        }

        if partitions[node] == partition {
            return false;
        }
    }

    true
}

// G = (V, E) grafo: 

fn main() {
    let g1 = vec![vec![1, 4], vec![3, 2], vec![3], vec![], vec![]];
    let g2 = vec![vec![1, 4], vec![3, 2], vec![3], vec![1], vec![]];
    println!("{}", dfs_cycles(&g1, 0));
    println!("{}", dfs_cycles(&g2, 0));

    // let g1 = vec![vec![1, 2], vec![0, 4], vec![0, 3], vec![2, 4], vec![3, 1]];
    // let g2 = vec![vec![1, 2], vec![2, 4], vec![3, 4], vec![2, 4], vec![]];
    // let g3 = vec![
    //     vec![1],
    //     vec![0],
    //     vec![3],
    //     vec![2],
    //     vec![5, 6],
    //     vec![4],
    //     vec![4],
    // ];
    //
    // let g4 = vec![
    //     vec![1, 7],
    //     vec![0],
    //     vec![3],
    //     vec![2],
    //     vec![5, 6],
    //     vec![4],
    //     vec![4],
    //     vec![0],
    // ];
    //
    // let mut visited = vec![false; g3.len()];
    // dfs(&g3, 0, &mut visited);
    // println!("{:?}", visited);
    //
    // let mut visited = vec![false; g1.len()];
    // dfs(&g1, 0, &mut visited);
    // println!("{:?}", visited);
    // let mut visited = vec![false; g3.len()];
    // dfs(&g3, 0, &mut visited);
    // println!("{:?}", visited);
    // println!("{:?}", dfs_iterative(&g1, 0));
    // println!("{:?}", dfs_iterative(&g3, 0));
    //
    // println!("{:?}", components(&g3));
    // println!("{:?}", components(&g4));
    //
    // // println!("{:?}", ex2::run(&g3));
    //
    // // let mut visited = vec![false; g2.len()];
    // // let mut t = vec![(0, 0); g2.len()];
    // // exercise::dfs(&g2, 0, &mut visited, &mut t, 0);
    //
    // // let mut avanti: Vec<(usize, usize)> = vec![];
    // // let mut indietro: Vec<(usize, usize)> = vec![];
    // // let mut attraversamento: Vec<(usize, usize)> = vec![];
    // // for (i, x) in g2.iter().enumerate() {
    // //     for &y in x {
    // //         if t[y].0 > t[i].1 {
    // //             attraversamento.push((i, y));
    // //         }
    // //         // } else if etc.. 3 cases
    // //     }
    // // }
    //
    // // println!("{:?}", t);
}
