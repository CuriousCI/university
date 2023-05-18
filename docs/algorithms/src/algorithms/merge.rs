pub fn merge<T: Ord + Copy>(array: &mut [T], start: usize, middle: usize, end: usize) {
    let mut i = start;
    let mut j = middle;
    let mut buffer: Vec<T> = Vec::with_capacity(end - start);

    while i < middle && j < end {
        if array[i] < array[j] {
            buffer.push(array[i]);
            i += 1;
        } else {
            buffer.push(array[j]);
            j += 1;
        }
    }

    while i < middle {
        buffer.push(array[i]);
        i += 1;
    }

    while j < end {
        buffer.push(array[j]);
        j += 1;
    }

    for (i, &v) in buffer.iter().enumerate() {
        array[start + i] = v;
    }
}

pub fn merge_sort<T: Ord + Copy>(array: &mut [T]) {
    sort(array, 0, array.len());
}

fn sort<T: Ord + Copy>(array: &mut [T], start: usize, end: usize) {
    if end - start == 1 {
        return;
    }

    let middle = (end + start) / 2;
    sort(array, start, middle);
    sort(array, middle, end);
    merge(array, start, middle, end);
}

// Pdf 9, Slide 18
pub mod exercises {
    use super::merge as iterative_merge;
    use std::fmt::Debug;

    // Ex 1, Iterative Merge Sort
    pub fn merge_sort<T: Ord + Copy + Debug>(array: &mut [T]) {
        let mut offset = 1;
        // let mut mid = 1;

        while offset <= array.len() {
            let mut start = 0;
            while start + offset <= array.len() {
                iterative_merge(
                    array,
                    start,
                    start + offset,
                    std::cmp::min(start + offset * 2, array.len()),
                );
                start += offset;
            }

            offset *= 2;
        }
    }

    // Ex 2, Recursive Merge Function
    pub fn merge<T: Ord + Copy>(array: &mut [T], start: usize, middle: usize, end: usize) {
        // choose which pointer to move (left or right)
        // after move, recopy item into original array at pointer!
        // test by using instead of iterative_merge
    }

    // Ex 3, Merge Sort which divides array into 4 parts

    // Ex 4, Computational Cost of MS4

    // Ex 5, K Merge Sort which divides array into K parts
}
