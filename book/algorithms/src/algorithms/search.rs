use std::cmp::Ordering::{Equal, Greater, Less};

pub fn linear_search<T: Eq>(array: &[T], value: T) -> Option<usize> {
    array
        .iter()
        .enumerate()
        .find_map(|(i, v)| if *v == value { Some(i) } else { None })
}

pub fn binary_search<T: Ord>(array: &[T], value: T) -> Option<usize> {
    let mut step = array.len();
    let mut index = 0;

    while step > 0 {
        let next = index + step;

        while next < array.len() {
            let cmp = match array.get(next) {
                Some(v) => v.cmp(&value),
                None => break,
            };

            match cmp {
                Equal => return Some(next),
                Less => index = next,
                Greater => break,
            }
        }

        step /= 2;
    }

    None
}

pub fn upper_bound<T: Ord>(array: &Vec<T>, value: T) -> Option<usize> {
    let mut step = array.len();
    let mut index = 0;

    if array.first().unwrap() > &value {
        return None;
    }

    while step > 0 {
        let next = index + step;

        while next < array.len() {
            let cmp = match array.get(next) {
                Some(v) => v.cmp(&value),
                None => break,
            };

            match cmp {
                Greater => break,
                _ => index = next,
            }
        }

        step /= 2;
    }

    Some(index)
}

pub fn lower_bound<T: Ord>(vector: &Vec<T>, value: T) -> Option<usize> {
    let mut step = vector.len();
    let mut index = vector.len() - 1;

    if vector.last().unwrap() < &value {
        return None;
    }

    while step > 0 {
        while step <= index {
            let cmp = match vector.get(index - step) {
                Some(v) => v.cmp(&value),
                None => break,
            };

            match cmp {
                Less => break,
                _ => index -= step,
            }
        }

        step /= 2;
    }

    Some(index)
}

// Pdf 4, Slide 4
pub mod exercises {
    use super::*;

    // Ex 1, find all items inside an array with value between lower and upper (included)

    pub fn count_in_range<T: Ord>(vector: Vec<T>, lower: T, upper: T) -> usize {
        let lower = lower_bound(&vector, lower);
        let upper = upper_bound(&vector, upper);

        if let (Some(l), Some(u)) = (lower, upper) {
            return match l.cmp(&u) {
                Greater => 0,
                _ => u.abs_diff(l) + 1,
            };
        }

        0
    }
}
