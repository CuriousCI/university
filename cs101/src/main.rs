use std::time::Instant;

use algorithms::naive_sorting::exercises::has_duplicates;

fn main() {
    let v = vec![190, 901, -1290, 2, 2901, 920000, -124590, -90, 2];
    println!("{}", has_duplicates(&v));
}

pub fn bench(f: impl Fn()) {
    let now = Instant::now();
    f();
    println!("{:.2?}", now.elapsed());
}
