#![allow(dead_code)]

use std::collections::VecDeque;

pub mod practice;
use practice::path;

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
    println!("{:?}", first_visit);

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
        if y != z {
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

fn bfs(graph: &[Vec<usize>], x: usize) -> Vec<bool> {
    let mut queue = VecDeque::from([x]);
    let mut visited = vec![false; graph.len()];

    while let Some(x) = queue.pop_back() {
        for &y in &graph[x] {
            if !visited[y] {
                queue.push_front(y);
                visited[y] = true;
            }
        }
    }

    visited
}

fn bfs_recursive(graph: &[Vec<usize>], x: usize) -> Vec<bool> {
    vec![]
}

fn distance(graph: &[Vec<usize>], x: usize) -> Vec<usize> {
    let mut queue = VecDeque::from([x]);
    let mut visited = vec![false; graph.len()];
    let mut distance = vec![0; graph.len()];

    while let Some(x) = queue.pop_back() {
        for &y in &graph[x] {
            if !visited[y] {
                queue.push_front(y);
                distance[y] = distance[x] + 1;
                visited[y] = true;
            }
        }
    }

    distance
}

fn count_min_paths(graph: &[Vec<usize>], x: usize) -> Vec<usize> {
    let mut queue = VecDeque::from([x]);
    let mut visited = vec![false; graph.len()];
    let mut distance = vec![0; graph.len()];
    let mut count = vec![1; graph.len()];

    while let Some(x) = queue.pop_back() {
        for &y in &graph[x] {
            if !visited[y] {
                queue.push_front(y);
                distance[y] = distance[x] + 1;
                visited[y] = true;
            } else if distance[x] < distance[y] {
                count[y] += count[x];
            }
        }
    }

    count
}

fn distance_from_big_daddy(tree: &[usize]) -> Vec<Option<usize>> {
    let mut distance: Vec<Option<usize>> = vec![None; tree.len()];

    for x in 0..tree.len() {
        distance_from_big_daddy_rec(tree, x, &mut distance);
    }

    distance
}

fn distance_from_big_daddy_rec(
    tree: &[usize],
    x: usize,
    distance: &mut Vec<Option<usize>>,
) -> usize {
    if x == tree[x] {
        distance[x] = Some(0);
        return 0;
    }

    match distance[x] {
        Some(d) => d,
        None => {
            let d = distance_from_big_daddy_rec(tree, tree[x], distance);
            distance[x] = Some(d + 1);
            d
        }
    }
}

fn subgraphs_distance(
    graph: &[Vec<usize>],
    origin: Vec<usize>,
    destination: Vec<usize>,
) -> Option<usize> {
    let mut queue = VecDeque::from(origin.clone());
    let mut distance = vec![0; graph.len()];
    let mut visited = vec![false; graph.len()];

    let mut origin_subset = vec![false; graph.len()];
    let mut destination_subset = vec![false; graph.len()];

    for x in origin {
        origin_subset[x] = true;
    }

    for y in destination {
        destination_subset[y] = true;
    }

    while let Some(x) = queue.pop_back() {
        for &y in &graph[x] {
            if !visited[y] {
                queue.push_front(y);
                visited[y] = true;

                if origin_subset[y] {
                    distance[y] = 0;
                } else {
                    distance[y] = distance[x] + 1;
                }

                if destination_subset[y] {
                    return Some(distance[y]);
                }
            }
        }
    }

    None
}

// fn bfs(graph: &[Vec<usize>], x: usize) -> Vec<bool> {
//     let mut queue = VecDeque::from([x]);
//     let mut visited = vec![false; graph.len()];
//
//     while let Some(x) = queue.pop_back() {
//         for &y in &graph[x] {
//             if !visited[y] {
//                 queue.push_front(y);
//                 visited[y] = true;
//             }
//         }
//     }
//
//     visited
// }

fn max_subarray(vec: &[isize]) -> isize {
    if vec.len() == 1 {
        return vec[0].max(0);
    }

    fn max<'a>(x: impl Iterator<Item = &'a isize>) -> isize {
        x.scan(0, |acc, &x| {
            *acc += x;
            Some(*acc)
        })
        .max()
        .unwrap()
    }

    let middle = vec.len() / 2;

    let prefix = max(vec[..middle].iter().rev());
    let suffix = max(vec[middle..].iter());

    (prefix + suffix)
        .max(max_subarray(&vec[..middle]))
        .max(max_subarray(&vec[middle..]))
}

fn solitary_number(vec: &[isize]) -> isize {
    if vec.len() == 1 || vec.len() == 2 {
        return vec[0];
    }

    let middle = vec.len() / 2;

    let left = vec[middle - 1];
    let right = vec[middle + 1];

    if vec[middle] == left {
        return solitary_number(&vec[..middle - 1]);
    }

    if vec[middle] == right {
        return solitary_number(&vec[middle + 2..]);
    }

    vec[middle]
}

fn majority_element(vec: &[usize]) -> usize {
    if vec.len() == 1 {
        return vec[0];
    }

    let middle = vec.len() / 2;

    0
}

fn main() {
    let vec = &[1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8];
    println!("{}", solitary_number(vec));
}

// let vec = &[2, 0, -2, 1, -3, 1, 0, 4, -2, 3, -1, 2, -2];
// let vec2 = &[2, 0, -2, 1];
// let vec3 = &[10, -1, 3, 1];
// println!("{}", max_subarray(vec));
// println!("{}", max_subarray(vec2));
// println!("{}", max_subarray(vec3));
