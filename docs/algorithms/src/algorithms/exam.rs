use std::cmp::Ordering::{Equal, Greater, Less};

pub fn find_subarray_sum(array: &[usize], sum: usize) -> Option<(usize, usize)> {
    let mut start = 0;
    let mut end = 0;
    let mut total = 0;

    while end < array.len() {
        match (total + array[end]).cmp(&sum) {
            Equal => return Some((start, end)),
            Less => {
                total += array[end];
                end += 1;
            }
            Greater => {
                total -= array[start];
                start += 1;
            }
        };
    }

    None
}
