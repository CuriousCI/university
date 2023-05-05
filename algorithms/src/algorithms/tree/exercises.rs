// use super::trees::{BinaryTree, ParentTree};
//
// fn depth<T>(tree: &ParentTree<T>) -> usize {
//     5
//     // tree.parents.len()
// }
//
// impl<T: Copy> From<ParentTree<T>> for BinaryTree<T> {
//     fn from(value: ParentTree<T>) -> Self {
//         let size = 2_u32.pow(depth(&value) as u32) - 1;
//         println!("{}", size);
//
//         let mut t = BinaryTree::from(vec![None; size as usize].into_boxed_slice());
//
//         for (i, p) in value.parents.iter().enumerate() {
//             match p {
//                 Some(v) => {
//                     let mut idx = v * 2 + 1;
//                     if t.get(idx).is_some() {
//                         idx += 1;
//                     }
//
//                     t[idx] = value.nodes[i];
//                 }
//                 None => t[0] = value.nodes[0],
//             }
//         }
//
//         t
//     }
// }
//
// fn count_nodes<T: Clone + Copy>(tree: &BinaryTree<T>, node: usize) -> usize {
//     tree.get(node)
//         .and_then(|_| {
//             Some(
//                 1 + tree
//                     .left(node)
//                     .and_then(|l| Some(count_nodes(tree, l)))
//                     .unwrap_or(0)
//                     + tree
//                         .right(node)
//                         .and_then(|r| Some(count_nodes(tree, r)))
//                         .unwrap_or(0),
//             )
//         })
//         .unwrap_or(0)
// }
//
// fn move_into<T: Clone + Copy>(
//     parent: &mut ParentTree<T>,
//     tree: &BinaryTree<T>,
//     node: usize,
//     index: usize,
//     p: Option<usize>,
// ) -> usize {
//     if let Some(v) = tree.get(node) {
//         parent[index] = Some(v);
//         parent.parent_of(index, p);
//
//         let next_index = tree
//             .left(node)
//             .and_then(|l| Some(move_into(parent, tree, l, index + 1, Some(index))))
//             .unwrap_or(index);
//
//         let next_index = tree
//             .right(node)
//             .and_then(|r| Some(move_into(parent, tree, r, next_index + 1, Some(index))))
//             .unwrap_or(next_index);
//
//         return next_index;
//     };
//
//     index
// }
//
// impl<T: Copy> From<BinaryTree<T>> for ParentTree<T> {
//     fn from(value: BinaryTree<T>) -> Self {
//         let mut tree = ParentTree::from(vec![None; count_nodes(&value, 0)].into_boxed_slice());
//         move_into(&mut tree, &value, 0, 0, None);
//         tree
//     }
// }
