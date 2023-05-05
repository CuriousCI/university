// use super::trees::TreeNode;
// use crate::queue::Queue;
//
// pub fn bfs<T: Default + Clone>(tree: &TreeNode<T>) {
//     let mut nodes = Queue::from(vec![&TreeNode::default(); 1000].into_boxed_slice());
//
//     nodes.enqueue(tree).unwrap();
//
//     while let Some(v) = nodes.dequeue() {
//         if let Some(l) = v.left {
//             nodes.enqueue(l.as_ref());
//         }
//     }
// }
