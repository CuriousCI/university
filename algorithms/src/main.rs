use std::time::Instant;

fn main() {
    let a: [Option<&str>] = [None; 10];
}

pub fn bench(f: impl Fn()) {
    let now = Instant::now();
    f();
    println!("{:.2?}", now.elapsed());
}
