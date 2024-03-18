pub fn find_direct_cycle(graph: &[Vec<usize>]) -> Vec<usize> {
    vec![]
}

fn is_bipartite(graph: &[Vec<usize>]) -> bool {
    let mut visited = vec![false; graph.len()];
    let mut parts = vec![false; graph.len()];

    for x in 0..graph.len() {
        if !visited[x] && !dfs_bipartite(graph, x, &mut visited, true, &mut parts) {
            return false;
        }
    }

    true
}

fn dfs_bipartite(
    graph: &[Vec<usize>],
    x: usize,
    visited: &mut Vec<bool>,
    part: bool,
    parts: &mut Vec<bool>,
) -> bool {
    visited[x] = true;
    parts[x] = part;

    for &y in &graph[x] {
        if !visited[y] {
            if !dfs_bipartite(graph, y, visited, !part, parts) {
                return false;
            }
        } else if parts[y] == part {
            return false;
        }
    }

    true
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
            v => v,
        })
    }

    if back == first_visit[x] && *visit > 1 {
        cutvertexes.push(x);
    }

    back
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

