use std::collections::VecDeque;

fn find_cycle(graph: &Vec<Vec<usize>>, x: usize) -> Vec<usize> {
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

fn main() {
    let g1 = vec![vec![1, 2], vec![0, 4], vec![0, 3], vec![2, 4], vec![3, 1]];
    let g2 = vec![
        vec![1, 2],
        vec![0, 2, 4],
        vec![0, 1, 3, 4],
        vec![2, 4],
        vec![1, 2, 3],
    ];

    println!("{:?}", find_cycle(&g1, 0));
    println!("{:?}", find_cycle(&g1, 3));

    println!("{:?}", find_cycle(&g2, 0));
    println!("{:?}", find_cycle(&g2, 2));
}
