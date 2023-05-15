use algorithms::dict::binary_search_tree::BinarySearchTree;

fn main() {
    let tree = BinarySearchTree::from(vec![(2, 0), (3, 0), (5, 0), (3, 0), (1, 0)]);

    println!("{:?}", tree);
    println!("{:?}", tree.min());
}

pub fn bench(f: impl Fn()) {
    use std::time::Instant;

    let now = Instant::now();
    f();
    println!("{:.2?}", now.elapsed());
}
