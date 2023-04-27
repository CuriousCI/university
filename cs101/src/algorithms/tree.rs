// pub struct NodeTree<T> {
//     value: T,
//     left: Option<Box<NodeTree<T>>>,
//     right: Option<Box<NodeTree<T>>>,
// }
//
// impl<T> Tree<T, NodeTree<T>> for NodeTree<T> {}
// impl<T> Iterator for NodeTree<T> {
//     type Item = T;
// }
//
// pub struct ArrayTree<'a, T> {
//     array: &'a [Option<T>],
// }
//
// impl<'a, T> ArrayTree<'a, T> {
//     // left() & right()
// }
//
// impl<T> Tree<T, usize> for ArrayTree<T> {}
//
// pub struct ParentTree<'a, T> {
//     vertices: &'a [(T, Option<usize>)],
// }
//
// impl<T> Tree<T, usize> for ParentTree<T> {}
//
// pub trait Tree<T, L> {
//     fn father_of(id: L) -> T;
//     fn countChildren_of(id: L) -> usize;
//     fn distance_from_root(id: L) -> usize;
// }
//
// // impl
// // get father of()
// // number of children of (v) (0, 1 or 2)
// // distance from father
// // impl iterator
// //
// //
// // TODO: bfs
// // TODO: dfs
