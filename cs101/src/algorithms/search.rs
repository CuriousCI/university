use std::cmp::Ordering::{Equal, Greater, Less};

pub fn search<T: Eq, L>(iterable: L, value: T) -> Option<usize>
where
    for<'a> &'a L: IntoIterator<Item = &'a T>,
{
    for (i, v) in iterable.into_iter().enumerate() {
        if *v == value {
            return Some(i);
        }
    }
    None
}

pub fn binary_search<T: Ord>(vector: &Vec<T>, value: T) -> Option<usize> {
    let mut step = vector.len();
    let mut index = 0;

    while step > 0 {
        while index + step < vector.len() {
            let cmp = match vector.get(index + step) {
                Some(v) => v.cmp(&value),
                None => break,
            };

            match cmp {
                Equal => return Some(index + step),
                Less => index += step,
                Greater => break,
            }
        }

        step /= 2;
    }

    None
}

pub fn upper_bound<T: Ord>(vector: &Vec<T>, value: T) -> Option<usize> {
    let mut step = vector.len();
    let mut index = 0;

    if vector.first().unwrap() > &value {
        return None;
    }

    while step > 0 {
        while index + step < vector.len() {
            let cmp = match vector.get(index + step) {
                Some(v) => v.cmp(&value),
                None => break,
            };

            match cmp {
                Greater => break,
                _ => index += step,
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

pub mod exercises {
    use super::*;

    pub fn count_in_range<T: Ord>(vector: Vec<T>, lower: T, upper: T) -> usize {
        let lower = lower_bound(&vector, lower);
        let upper = upper_bound(&vector, upper);

        match (lower, upper) {
            (Some(l), Some(u)) => match l.cmp(&u) {
                Greater => 0,
                _ => u.abs_diff(l) + 1,
            },
            _ => 0,
        }
    }
}
