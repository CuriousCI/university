use std::time::Instant;

use algorithms::heap::{Category, Heap};

fn main() {
    let mut array = [190, 901, -1290, 2, 2901, 9200, -124590, -90, 2];
    let mut min_heap = Heap::new(&mut array, Category::Min);
    min_heap.insert(290);
    for value in min_heap {
        println!("{}", value);
    }
    array.iter().min();
}

pub fn bench(f: impl Fn()) {
    let now = Instant::now();
    f();
    println!("{:.2?}", now.elapsed());
}
