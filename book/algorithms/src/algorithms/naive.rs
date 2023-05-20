pub fn insertion_sort<T: Ord>(vector: &mut [T]) {
    for i in 1..vector.len() {
        for j in (1..=i).rev() {
            if vector[j - 1] < vector[j] {
                break;
            }

            vector.swap(j - 1, j);
        }
    }
}

pub fn selection_sort<T: Ord>(vector: &mut [T]) {
    for i in 0..vector.len() - 1 {
        let (j, _) = (&vector[i..])
            .iter()
            .enumerate()
            .min_by(|&(_, x), &(_, y)| x.cmp(y))
            .unwrap();

        vector.swap(i, j + i);
    }
}

pub fn bubble_sort<T: Ord>(vector: &mut [T]) {
    for i in 0..vector.len() {
        for j in (i + 1..vector.len()).rev() {
            if vector[j] < vector[j - 1] {
                vector.swap(j, j - 1)
            }
        }
    }
}

// Pdf 8, Slide 35
pub mod exercises {
    use std::ops::Range;

    // Ex 1, pt. 1
    pub fn reversed_bubble_sort<T: Ord>(vector: &mut [T]) {
        for i in (0..vector.len() - 1).rev() {
            for j in 0..=i {
                if vector[j] < vector[j + 1] {
                    vector.swap(j, j + 1)
                }
            }
        }
    }

    // Ex 1, pt. 2, Which are stable?
    // Insertion Sort - stable
    // Selection Sort - stable
    // Bubble Sort - unstable

    // Ex 1, pt. 3, Cost if sorted? Cost if all equal?
    // Insertion Sort - sorted O(n) - equal O(n)
    // Selection Sort - sorted O(n^2) - equal O(n^2)
    // Bubble Sort - sorted O(n^2) - equal O(n^2)

    // Ex 2, pt. 1, Write an insertion_sort using a separate function for min
    pub fn min_in_range<T: Ord>(vector: &[T], r: Range<usize>) -> usize {
        let (index, _) = (&vector[r])
            .iter()
            .enumerate()
            .min_by(|&(_, x), &(_, y)| x.cmp(y))
            .unwrap();

        index
    }

    pub fn min_selection_sort<T: Ord>(vector: &mut [T]) {
        for i in 0..vector.len() - 1 {
            let j = min_in_range(vector, i..vector.len());
            vector.swap(i, i + j);
        }
    }

    // Ex 2, pt. 2, Check if array has_duplicates, based on naive sorting algorithms
    pub fn has_duplicates<T: Eq>(vector: &[T]) -> bool {
        for (index, value) in vector.iter().enumerate() {
            if (vector[index + 1..]).iter().filter(|&x| x == value).count() > 0 {
                return true;
            }
        }

        false
    }
}
