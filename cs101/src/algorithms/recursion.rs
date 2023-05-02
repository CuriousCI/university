use std::{
    cmp::Ordering::{Equal, Greater},
    fmt::Debug,
};

pub fn linear_search<T: Eq>(array: &[T], value: T, index: usize) -> Option<usize> {
    if index == array.len() {
        return None;
    }

    if let Some(v) = array.get(index) {
        if *v == value {
            return Some(index);
        }
    }

    linear_search(array, value, index + 1)
}

pub fn binary_search<T: Ord>(array: &[T], value: T, start: usize, end: usize) -> Option<usize> {
    if start == end {
        return None;
    }

    let mid = (end - start) / 2;

    if let Some(v) = array.get(mid) {
        match value.cmp(v) {
            Equal => Some(mid),
            Greater => binary_search(array, value, mid + 1, end),
            _ => binary_search(array, value, start, mid),
        };
    }

    None
}

pub fn factorial(number: usize) -> usize {
    if number == 0 {
        return 1;
    }

    number * factorial(number - 1)
}

pub fn fibonacci(nth: usize) -> usize {
    if nth == 0 || nth == 1 {
        return 1;
    }

    fibonacci(nth - 1) + fibonacci(nth - 2)
}

// Ex 1, kth power of n
pub fn pow(base: usize, exponent: usize) -> usize {
    if exponent == 0 {
        return 1;
    }

    base * pow(base, exponent - 1)
}

// Ex 2, sum of elements
pub fn sum(array: &[usize], index: usize) -> usize {
    if let Some(x) = array.get(index) {
        return x + sum(array, index + 1);
    }

    0
}

// Ex 3, find min
pub fn min<T: Ord>(array: &[T], index: usize) -> Option<&T> {
    if index == array.len() {
        return None;
    }

    std::cmp::min(array.get(index), min(array, index + 1))
}

// Ex 4, palindrome
pub fn is_palindrome<T: Eq>(array: &[T], index: usize) -> bool {
    false
}

// Ex 5, reverse print
pub fn reverse_print<T: Debug>(array: &[T], index: usize) {
    if let Some(t) = array.get(index) {
        print!("{:?}", t);
        reverse_print(array, index - 1)
    }
}

// Ex 6, print in order
pub fn print<T: Debug>(array: &[T], index: usize) {
    if let Some(t) = array.get(index) {
        print!("{:?}", t);
        print(array, index + 1)
    }
}

// Ex 7, hanoi

// Pdf 5, Slide 37
pub mod exercises {
    // Ex 1, binomial

    // Ex 2, GCD
    pub fn gcd(x: usize, y: usize) -> usize {
        if y == 0 {
            return x;
        }

        gcd(y, x % y)
    }
}
