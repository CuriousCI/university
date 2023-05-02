use std::io::{self, BufRead};

fn main() {
    let mut buffer = String::new();
    let mut handle = io::stdin().lock();

    handle.read_line(&mut buffer).unwrap();
    let (jack, jill) = buffer.trim().split_once(" ").unwrap();

    let jack: u32 = jack.parse().unwrap();
    let jill: u32 = jill.parse().unwrap();

    let mut cds: Vec<String> = vec![];
    for _ in 0..jack + jill {
        buffer.clear();
        handle.read_line(&mut buffer).unwrap();
        cds.push(String::from(buffer.trim()));
    }

    let tot = cds.len();

    cds.sort();
    cds.dedup();

    println!("{}", tot - cds.len());
}
