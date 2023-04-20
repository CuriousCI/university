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

pub fn binary_search<T: Ord>(vector: Vec<T>, value: T) -> Option<usize> {
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

#[test]
fn test_binary_search_found() {
    assert_ne!(
        None,
        binary_search(
            vec![10, 20, 30, 40, 50, 60, 80, 80, 80, 85, 90, 100, 120, 12901, 9012901],
            80
        )
    );
}

#[test]
fn test_binary_search_not_found() {
    assert_eq!(
        None,
        binary_search(
            vec![10, 20, 30, 40, 50, 60, 80, 85, 90, 100, 120, 12901, 9012901],
            75
        )
    );
}
// TODO: upper bound
// TODO: lower bound
