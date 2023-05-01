pub fn counting_sort<'a>(array: &'a mut [usize]) {
    let mut counter: Vec<usize> = vec![0; *array.iter().max().unwrap_or(&mut 0) + 1];

    for n in array.iter() {
        counter[*n] += 1;
    }

    let mut index = 0;
    for (number, &count) in counter.iter().enumerate() {
        for _ in 0..count {
            array[index] = number;
            index += 1;
        }
    }
}

pub trait IntoIndex {
    fn into_index(&self) -> usize;
}

pub fn stable_counting_sort<'a, T: Clone + Copy + IntoIndex + Default>(array: &'a mut [T]) {
    let mut counter: Vec<usize> = vec![0; array.iter().map(T::into_index).max().unwrap_or(0) + 1];
    for n in array.iter().map(T::into_index) {
        counter[n] += 1;
    }

    let mut positions = counter;
    for i in 1..positions.len() {
        positions[i] += positions[i - 1];
    }

    let mut tmp: Vec<T> = vec![T::default(); array.len()];
    for k in array.iter().rev() {
        tmp[positions[k.into_index()] - 1] = *k;
        positions[k.into_index()] -= 1;
    }

    for (i, k) in tmp.iter().enumerate() {
        array[i] = *k;
    }
}

// TODO bucket_sort

// Pdf 12, Slide 15
mod exercises {
    // Ex 1, Is stable_counting_sort stable? Yes

    // Ex 2, Worst case for bucket_sort? O(n^2) if insertion_sort is used for buckets, O(n) if
    // counting sort is used

    // Ex 3, bucket_sort using counting_sort for buckets, hypotesis on k?
}
