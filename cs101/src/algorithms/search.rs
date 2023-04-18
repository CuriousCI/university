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

// pub fn binary_search<T: Eq, L>(iterable: L, value: T) -> Option<usize>
// where
//     for<'a> &'a L: IntoIterator<Item = &'a T>,
// {
//     let mut step = iterable.into_iter().size_hint();
//     let mut index = 0;
//
//     Some(index)
//     // None
// }

// TODO: upper bound
// TODO: lower bound
