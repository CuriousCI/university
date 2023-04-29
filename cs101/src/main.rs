use std::time::Instant;

fn main() {
    println!("{:?}", Some(10) > None)
}

pub fn bench(f: impl Fn()) {
    let now = Instant::now();
    f();
    println!("{:.2?}", now.elapsed());
}
