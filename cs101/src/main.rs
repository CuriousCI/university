use algorithms::search::{binary_search, search};

fn main() {
    println!(
        "{}",
        match search(vec![10, 21, 2123, 25, 80, 91, 290], 80) {
            Some(index) => format!("Item found at index {}", index),
            None => String::from("Item not found"),
        }
    );

    println!(
        "{}",
        match binary_search(
            vec![10, 20, 30, 40, 50, 60, 80, 85, 90, 100, 120, 12901, 9012901],
            80
        ) {
            Some(index) => format!("Item found at index {}", index),
            None => String::from("Item not found"),
        }
    );
}
