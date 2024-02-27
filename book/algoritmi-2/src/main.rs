use std::collections::VecDeque;

fn find_cycle(graph: Vec<Vec<usize>>, x: usize) -> Vec<usize> {
    let mut cycle: VecDeque<usize> = VecDeque::new();
    cycle.push_back(x);

    let mut visited: Vec<bool> = vec![false; graph.len()];

    let mut current = x;
    let mut next = graph[x][0];

    visited[current] = true;
    visited[next] = true;

    while !visited[graph[next][1]] {
        cycle.push_back(next);
        current = next;
        visited[current] = true;
        next = graph[current][1];
    }

    cycle.into_iter().collect()
}

fn main() {
    let g = vec![vec![1, 2], vec![0, 4], vec![0, 3], vec![2, 4], vec![3, 1]];

    let cycle = find_cycle(g, 0);
    println!("{:?}", cycle);
}
