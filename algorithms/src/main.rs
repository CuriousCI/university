// use algorithms::merge::exercises::merge_sort;
// use algorithms::merge::merge_sort;

use algorithms::quick::quick_sort;
fn main() {
    let mut arr = [80, 28091, 289, 48, 281, 201, 802];
    println!("{:?}", arr);
    quick_sort(&mut arr);
    println!("{:?}", arr);
}

pub fn bench(f: impl Fn()) {
    use std::time::Instant;

    let now = Instant::now();
    f();
    println!("{:.2?}", now.elapsed());
}

// use algorithms::tree::{
//     operations::{height, nodes_at_height},
//     trees::TreeNode,
// };
// let tree: TreeNode<i32> = TreeNode {
//     value: 10,
//     left: Some(Box::new(TreeNode {
//         value: 20,
//         left: None,
//         right: None,
//     })),
//     right: Some(Box::new(TreeNode {
//         value: 20,
//         left: Some(Box::new(TreeNode {
//             value: 3,
//             left: None,
//             right: None,
//         })),
//         right: None,
//     })),
// };
//
// println!("{:?}", nodes_at_height(&tree, 3))
// 1, 12, 829, 8, 99, 902, 902, 892
// 1
// 12 829
// 8 99, 902, 902
// 892
