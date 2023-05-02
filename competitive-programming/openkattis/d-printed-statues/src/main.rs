use std::io::{self, BufRead};

fn main() {
    let mut buffer = String::new();
    let mut handle = io::stdin().lock();

    handle.read_line(&mut buffer).unwrap();

    let statues: u32 = buffer.trim().parse().unwrap();

    let mut day = 0;
    let mut result = statues;
    while 2 << day <= statues {
        let printers = 2 << day;
        result =
            result.min(1 + day + statues / printers + if statues % printers > 0 { 1 } else { 0 });
        day += 1;
    }

    println!("{}", result);
}
