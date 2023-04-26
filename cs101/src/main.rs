use std::time::Instant;

use algorithms::heap::{heap_sort, Heap};

fn main() {
    let mut a = [190, 901, -1290, 2, 2901, 9200, -124590, -90, 2];
    heap_sort(&mut Heap::new(&mut a));
    println!("{:?}", a);
}

pub fn bench(f: impl Fn()) {
    let now = Instant::now();
    f();
    println!("{:.2?}", now.elapsed());
}
