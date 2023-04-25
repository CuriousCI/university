pub fn insertion_sort<T: Ord>(vector: &mut Vec<T>) {
    for i in 1..vector.len() {
        for j in (1..=i).rev() {
            if vector[j - 1] < vector[j] {
                break;
            }

            vector.swap(j - 1, j);
        }
    }
}

pub fn selection_sort<T: Ord>(vector: &mut Vec<T>) {
    for i in 0..vector.len() - 1 {
        let (j, _) = (&vector[i..])
            .iter()
            .enumerate()
            .min_by(|&(_, x), &(_, y)| x.cmp(y))
            .unwrap();

        vector.swap(i, j + i);
    }
}

pub fn bubble_sort<T: Ord>(vector: &mut Vec<T>) {
    for i in 0..vector.len() {
        for j in (i + 1..vector.len()).rev() {
            if vector[j] < vector[j - 1] {
                vector.swap(j, j - 1)
            }
        }
    }
}

pub mod exercises {
    pub fn reversed_bubble_sort<T: Ord>(vector: &mut Vec<T>) {
        for i in (0..vector.len() - 1).rev() {
            for j in 0..=i {
                if vector[j] < vector[j + 1] {
                    vector.swap(j, j + 1)
                }
            }
        }
    }

    pub fn min<T: Ord>(vector: &Vec<T>, from: usize) -> usize {
        let (index, _) = (&vector[from..])
            .iter()
            .enumerate()
            .min_by(|&(_, x), &(_, y)| x.cmp(y))
            .unwrap();

        from + index
    }

    pub fn min_selection_sort<T: Ord>(vector: &mut Vec<T>) {
        for i in 0..vector.len() - 1 {
            let j = min(vector, i);
            vector.swap(i, j);
        }
    }

    pub fn has_duplicates<T: Eq>(vector: &Vec<T>) -> bool {
        for (index, value) in vector.iter().enumerate() {
            if (vector[index + 1..]).iter().filter(|&x| x == value).count() > 0 {
                return true;
            }
        }

        false
    }
}
