fn main() {
    let _codici_fiscali = [0; 2 * 10_usize.pow(18)];
}

use std::time::Instant;

pub fn bench(f: impl Fn()) {
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
