use std::{collections::VecDeque, vec};

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

fn dfs(graph: &Vec<Vec<usize>>, x: usize, visited: &mut Vec<bool>) {
    visited[x] = true;
    for &y in &graph[x] {
        if !visited[y] {
            dfs(graph, y, visited)
        }
    }
}

fn dfs_a(graph: &[[usize]], x: usize, visited: &mut [bool]) {
    visited[x] = true;
    for &y in &graph[x] {
        if !visited[y] {
            dfs(graph, y, visited)
        }
    }
}

fn dfs_iter(graph: &mut Vec<Vec<usize>>, x: usize) -> Vec<bool> {
    let mut stack = VecDeque::from([x]);
    let mut visited = vec![false; graph.len()];

    while let Some(&x) = stack.back() {
        if let Some(&y) = graph[x].last() {
            if !visited[y] {
                stack.push_back(y);
                visited[y] = true;
            }

            graph[x].pop();
        } else {
            stack.pop_back();
        }
    }

    visited
}

mod ex1 {
    pub fn run(graph: &Vec<Vec<usize>>) -> Vec<usize> {
        let mut partitions = vec![0; graph.len()];
        let mut partition = 1;

        for x in 0..graph.len() {
            if partitions[x] == 0 {
                partitions[x] = partition;
                dfs(graph, x, &mut partitions, partition);
                partition += 1;
            }
        }

        partitions
    }

    fn dfs(graph: &Vec<Vec<usize>>, x: usize, partitions: &mut Vec<usize>, partition: usize) {
        partitions[x] = partition;
        for &y in &graph[x] {
            if partitions[y] == 0 {
                dfs(graph, y, partitions, partition)
            }
        }
    }
}

mod ex2 {
    use std::collections::VecDeque;

    pub fn run(graph: &Vec<Vec<usize>>) -> Vec<usize> {
        let mut partitions = vec![0; graph.len()];
        let mut partition = 1;

        for x in 0..graph.len() {
            if partitions[x] == 0 {
                partitions[x] = partition;
                dfs(&graph, x, &mut partitions, partition);
                partition += 1;
            }
        }

        partitions
    }

    fn dfs(graph: &Vec<Vec<usize>>, x: usize, partitions: &mut Vec<usize>, partition: usize) {
        let mut stack = VecDeque::from([x]);

        let mut index = 0;
        while let Some(&x) = stack.back() {
            if let Some(&y) = graph[x].get(index) {
                if partitions[y] == 0 {
                    stack.push_back(y);
                    partitions[y] = partition;
                }

                index += 1;
            } else {
                stack.pop_back();
                index = 0;
            }
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

fn main() {
    let g1 = vec![vec![1, 2], vec![0, 4], vec![0, 3], vec![2, 4], vec![3, 1]];
    let g2 = vec![vec![1, 2], vec![2, 4], vec![3, 4], vec![2, 4], vec![]];
    let g3 = vec![
        vec![1],
        vec![0],
        vec![3],
        vec![2],
        vec![5, 6],
        vec![4],
        vec![4],
    ];

    println!("{:?}", find_cycle(&g1, 0));
    println!("{:?}", find_cycle(&g1, 3));

    // println!("{:?}", find_cycle(&g2, 0));
    // println!("{:?}", find_cycle(&g2, 2));

    let mut visited = vec![false; g3.len()];
    dfs(&g3, 0, &mut visited);
    println!("{:?}", visited);

    println!("{:?}", dfs_iter(&mut g1.clone(), 0));
    println!("{:?}", dfs_iter(&mut g3.clone(), 0));

    println!("{:?}", ex1::run(&g3));
    println!("{:?}", ex2::run(&g3));

    let mut visited = vec![false; g2.len()];
    let mut t = vec![(0, 0); g2.len()];
    exercise::dfs(&g2, 0, &mut visited, &mut t, 0);

    let mut avanti: Vec<(usize, usize)> = vec![];
    let mut indietro: Vec<(usize, usize)> = vec![];
    let mut attraversamento: Vec<(usize, usize)> = vec![];
    for (i, x) in g2.iter().enumerate() {
        for &y in x {
            if t[y].0 > t[i].1 {
                attraversamento.push((i, y));
            }
            // } else if etc.. 3 cases
        }
    }

    println!("{:?}", t);
}
