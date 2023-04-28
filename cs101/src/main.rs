use std::{cmp::Reverse, time::Instant};

use algorithms::heap::Heap;

fn main() {
    let a = [1, 2, 4, 190, -20, -2980, 29, -902, 90];
    let heap = Heap::new(&mut a);
    for value in heap {
        println!("{:?}", value);
    }
}

pub fn bench(f: impl Fn()) {
    let now = Instant::now();
    f();
    println!("{:.2?}", now.elapsed());
}
