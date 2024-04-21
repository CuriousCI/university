pub fn find_direct_cycle(graph: &[Vec<usize>]) -> Vec<usize> {
    vec![]
}

pub fn is_bipartite(graph: &[Vec<usize>]) -> bool {
    let mut visited = vec![false; graph.len()];
    let mut parts = vec![false; graph.len()];

    for x in 0..graph.len() {
        if !visited[x] && !dfs_bipartite(graph, x, &mut visited, true, &mut parts) {
            return false;
        }
    }

    true
}

pub fn dfs_bipartite(
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

pub fn cutvertexes(graph: &[Vec<usize>]) -> Vec<usize> {
    let mut first_visit = vec![0; graph.len()];
    let mut cutvertexes = vec![];
    let mut visit = 0;

    dfs_cutvertexes(graph, 0, &mut visit, &mut first_visit, &mut cutvertexes);

    cutvertexes
}

pub fn dfs_cutvertexes(
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

pub fn to_dag(graph: &[Vec<usize>]) -> Vec<Vec<usize>> {
    let mut new_graph = vec![vec![]; graph.len()];
    let mut first_visit = vec![0; graph.len()];
    let mut visit = 1;

    dag_dfs(graph, 0, 0, &mut visit, &mut first_visit, &mut new_graph);

    new_graph
}

pub fn dag_dfs(
    graph: &[Vec<usize>],
    x: usize,
    z: usize,
    visit: &mut usize,
    first_visit: &mut Vec<usize>,
    new_graph: &mut [Vec<usize>],
) {
    first_visit[x] = *visit;
    *visit += 1;

    for &y in &graph[x] {
        if first_visit[y] == 0 {
            new_graph[x].push(y);
            dag_dfs(graph, y, x, visit, first_visit, new_graph)
        } else if first_visit[x] > first_visit[y] && y != z {
            new_graph[y].push(x);
        }
    }
}

pub fn path(graph: &[Vec<usize>]) -> Vec<(usize, usize)> {
    let mut path = vec![];
    let mut visited = vec![false; graph.len()];

    dfs_path(graph, 0, 0, &mut visited, &mut path);

    path
}

pub fn dfs_path(
    graph: &[Vec<usize>],
    x: usize,
    z: usize,
    visited: &mut Vec<bool>,
    // todo: first_visit
    path: &mut Vec<(usize, usize)>,
) {
    visited[x] = true;

    for &y in &graph[x] {
        if y != z {
            path.push((x, y));

            if !visited[y] {
                dfs_path(graph, y, x, visited, path);
            }

            path.push((y, x));
        }
    }
}
