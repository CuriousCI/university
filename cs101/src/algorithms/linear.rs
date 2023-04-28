// Into<usize> is not good! Numbers can't be converted into usize!
pub fn counting_sort<'a, T: Ord + Copy + Into<usize>>(array: &'a mut [T]) {
    let mut counter = vec![0; T::into(*array.iter().max().unwrap())];
    for value in array.iter() {
        counter[T::into(*value)] += 1;
    }

    for index in 1..counter.len() {
        counter[index] += counter[index - 1]
    }

    println!("{:?}", counter);
}

// TODO counting_sort for numbers only!
// TODO bucker_sort
