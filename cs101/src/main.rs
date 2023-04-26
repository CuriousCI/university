use std::time::Instant;

use algorithms::heap::heap_sort;

fn main() {
    let mut array = [190, 901, -1290, 2, 2901, 9200, -124590, -90, 2];
    heap_sort(&mut array);
    println!("{:?}", array)
}

pub fn bench(f: impl Fn()) {
    let now = Instant::now();
    f();
    println!("{:.2?}", now.elapsed());
}
