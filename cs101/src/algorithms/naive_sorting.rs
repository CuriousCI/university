pub fn insertion_sort<T: Ord>(vector: &mut Vec<T>) {
    for position in 1..vector.len() {
        for j in (1..position).rev() {
            match (vector.get(j - 1), vector.get(j)) {
                (Some(l), Some(r)) => {
                    if l > r {
                        vector.swap(j - 1, j)
                    }
                }
                _ => break,
            }
        }
    }
}
