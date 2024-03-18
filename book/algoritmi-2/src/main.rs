#![allow(dead_code)]

pub mod practice;

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

// Do iterative?

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

fn universal_sink(graph: &[Vec<usize>]) -> Option<usize> {
    None
}

fn topological_order(graph: &[Vec<usize>]) -> Vec<usize> {
    vec![]
}

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

fn daddies(tree: &[usize], mut x: usize) -> Vec<usize> {
    let mut daddies = vec![];

    while x != tree[x] {
        x = tree[x];
        daddies.push(x);
    }

    daddies
}

fn common_daddies(tree: &[usize], mut x: usize, mut y: usize) -> Vec<usize> {
    let mut daddies = vec![];

    let mut x_daddies = vec![false; tree.len()];

    while x != tree[x] {
        x = tree[x];
        x_daddies[x] = true;
    }

    while y != tree[y] {
        y = tree[y];
        if x_daddies[y] {
            daddies.push(y);
        }
    }

    daddies
}

fn first_common_daddy(tree: &[usize], mut x: usize, mut y: usize) -> usize {
    let mut x_daddies = vec![false; tree.len()];

    while x != tree[x] {
        x = tree[x];
        x_daddies[x] = true;
    }

    while y != tree[y] {
        y = tree[y];
        if x_daddies[y] {
            return y;
        }
    }

    x
}

// Tarjan's algorithm
fn strongly_connected_components(graph: &[Vec<usize>]) -> Vec<usize> {
    vec![]
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

    let d = vec![3, 1, 1, 4, 1, 2, 4, 4, 2, 5];
    println!("{:?}", daddies(&d, 0));
    println!("{:?}", common_daddies(&d, 0, 9));
    println!("{:?}", common_daddies(&d, 5, 8));
    println!("{:?}", common_daddies(&d, 9, 8));
    println!("{:?}", first_common_daddy(&d, 0, 9));
    println!("{:?}", first_common_daddy(&d, 5, 8));
    println!("{:?}", first_common_daddy(&d, 9, 8));

    // 1
    // 2 4
    // 5 8, 3 6 7
    // 9, , 0
}
