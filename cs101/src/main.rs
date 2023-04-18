use algorithms::search::search;

fn main() {
    println!(
        "{}",
        match search(vec![10, 21, 2123, 25, 80, 91, 290], 80) {
            Some(index) => format!("Item found at index {}", index),
            None => String::from("Item not found"),
        }
    )
}
