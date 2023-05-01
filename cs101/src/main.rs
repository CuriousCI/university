use std::time::Instant;

use algorithms::linear::{counting_sort, stable_counting_sort, IntoIndex};

#[derive(Debug, Clone, Copy)]
struct User<'a> {
    #[allow(dead_code)]
    name: &'a str,
    age: usize,
}

impl<'a> User<'a> {
    pub fn new(name: &'a str, age: usize) -> Self {
        Self { name, age }
    }
}

impl<'a> IntoIndex for User<'a> {
    fn into_index(&self) -> usize {
        self.age
    }
}

impl<'a> Default for User<'a> {
    fn default() -> Self {
        Self { name: "", age: 0 }
    }
}

impl<'a> Eq for User<'a> {}

impl<'a> PartialEq for User<'a> {
    fn eq(&self, other: &Self) -> bool {
        self.age == other.age
    }
}

impl<'a> PartialOrd for User<'a> {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        self.age.partial_cmp(&other.age)
    }
}

impl<'a> Ord for User<'a> {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.age.cmp(&other.age)
    }
}

fn main() {
    // let mut array = [10, 2, 12, 4, 5, 5, 6, 1, 2, 3, 2, 5, 5, 8];
    let mut users = [
        User::new("Marco", 12),
        User::new("Gianni", 12),
        User::new("Sara", 10),
        User::new("Pasta", 12),
        User::new("Pippa", 9),
        User::new("Cocaina", 8),
        User::new("Peppa", 12),
        User::new("Pig", 2),
        User::new("Manu Chao", 14),
    ];
    stable_counting_sort(&mut users);

    bench(|| {
        let mut users = [
            User::new("Marco", 12),
            User::new("Gianni", 12),
            User::new("Sara", 10),
            User::new("Pasta", 12),
            User::new("Pippa", 9),
            User::new("Cocaina", 8),
            User::new("Peppa", 12),
            User::new("Pig", 2),
            User::new("Manu Chao", 14),
        ];
        stable_counting_sort(&mut users);
    });

    bench(|| {
        let mut users = [
            User::new("Marco", 12),
            User::new("Gianni", 12),
            User::new("Sara", 10),
            User::new("Pasta", 12),
            User::new("Pippa", 9),
            User::new("Cocaina", 8),
            User::new("Peppa", 12),
            User::new("Pig", 2),
            User::new("Manu Chao", 14),
        ];
        users.sort();
    })
}

pub fn bench(f: impl Fn()) {
    let now = Instant::now();
    f();
    println!("{:.2?}", now.elapsed());
}
