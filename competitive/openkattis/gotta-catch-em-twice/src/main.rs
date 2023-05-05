use std::io::{self, BufRead};

fn main() {
    let mut buf = String::new();
    let mut handle = io::stdin().lock();

    handle.read_line(&mut buf).unwrap();

    let pokemons_number: i32 = buf.trim().parse().unwrap();
    let mut pokemons: Vec<String> = vec![];
    for _ in 0..pokemons_number {
        buf = String::new();
        handle.read_line(&mut buf).unwrap();
        pokemons.push(String::from(buf.trim()))
    }

    pokemons.sort();
    pokemons.dedup();
    println!("{}", pokemons.len() + 1);
}
