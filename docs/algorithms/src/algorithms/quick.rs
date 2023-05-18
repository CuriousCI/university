pub fn partition<T: Ord + Copy>(array: &mut [T], start: usize, end: usize) -> usize {
    // pick a pivot
    let mut pivot = start;
    let mut to_left = false;

    let mut left = start;
    let mut right = end - 1;

    while left < right {
        if to_left {
            if array[left] > array[pivot] {
                array.swap(left, pivot);
                pivot = left;
                to_left = !to_left;
            }

            left += 1;
        } else {
            if array[pivot] > array[right] {
                array.swap(right, pivot);
                pivot = right;
                to_left = !to_left;
            }

            right -= 1;
        }
    }

    // shift stuff
    pivot
}

pub fn quick_sort<T: Ord + Copy>(array: &mut [T]) {
    sort(array, 0, array.len());
}

fn sort<T: Ord + Copy>(array: &mut [T], start: usize, end: usize) {
    if end <= start + 1 {
        return;
    }

    let pivot_index = partition(array, start, end);
    if pivot_index > 0 {
        sort(array, start, pivot_index - 1);
    }
    if pivot_index + 1 < end {
        sort(array, pivot_index + 1, end);
    }
}

// Pdf 10, Slide
pub mod exercises {
    // Ex 1, pt. 1, Sort Array with only 0s and 2s
    pub fn dual_sort(array: &mut [u8]) {
        let mut left = 0;
        let mut right = array.len() - 1;

        while left < right {
            if array[right] == 2 {
                right -= 1;
            } else if array[left] > array[right] {
                array.swap(left, right);
            } else {
                left += 1;
            }
        }
    }

    // Ex 1, pt. 2 Worst Case Permutation of [0, 1, 2, 3, 4, 5, 6, 7] for Quick Sort
    // Permutation 1: [0, 1, 2, 3, 4, 5, 6, 7]
    // Permutation 2: [7, 6, 5, 4, 3, 2, 1, 0]

    // Ex 1, pt. 3 Quick Sort Cost
    // Equal elements: O(n^2), Pivot is alwasy at start or end
    // Sorted Array: O(n^2)

    // Ex 2, Sort rows and columns in Matrix
    pub fn matrix_sort<T: Copy + Ord>(matrix: &mut Vec<Vec<T>>) {
        let mut values: Vec<T> = matrix.iter().flatten().map(|v| *v).collect();
        values.sort();
        let mut index: usize = 0;

        for row in matrix.iter_mut() {
            for col in 0..row.len() {
                row[col] = values[index];
                index += 1;
            }
        }
    }
}
