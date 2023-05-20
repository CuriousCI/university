// use algorithms::dict::binary_search_tree::BinarySearchTree;
use algorithms::recursion::linear_search;

fn main() {
    let a = [1, 3, 5, 2, 9, 3, 3, 1, 6];
    println!("{:?}", linear_search(&a, 12, 0));

    // let tree = BinarySearchTree::from(vec![(2, 0), (3, 0), (5, 0), (3, 0), (1, 0)]);

    // println!("{:?}", tree);
    // println!("{:?}", tree.min());
}

pub fn bench(f: impl Fn()) {
    use std::time::Instant;

    let now = Instant::now();
    f();
    println!("{:.2?}", now.elapsed());
}
