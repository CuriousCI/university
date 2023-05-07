use std::ops::{Index, IndexMut};

pub struct BinaryTree<T> {
    buf: Box<[T]>,
}

impl<T> BinaryTree<T> {
    // pub fn from(buf: Box<[T]>) -> Self {
    //     Self { buf }
    // }

    // pub fn get(&self, index: usize) -> Option<&T> {
    //     self.nodes.get(index)
    // }

    // pub fn len(&self) -> usize {
    //     self.nodes.len()
    // }

    // pub fn left(&self, index: usize) -> Option<usize> {
    //     self.child(index, 1)
    // }
    //
    // pub fn right(&self, index: usize) -> Option<usize> {
    //     self.child(index, 2)
    // }
    //
    // fn child(&self, index: usize, offset: usize) -> Option<usize> {
    //     let index = index * 2 + offset;
    //
    //     if index >= self.nodes.len() {
    //         return None;
    //     }
    //
    //     Some(index)
    // }
}

impl<T> From<Vec<T>> for BinaryTree<T> {
    fn from(value: Vec<T>) -> Self {
        Self {
            buf: value.into_boxed_slice(),
        }
    }
}

impl<T> Index<usize> for BinaryTree<T> {
    type Output = T;

    fn index(&self, index: usize) -> &Self::Output {
        self.buf.index(index)
    }
}

impl<T> IndexMut<usize> for BinaryTree<T> {
    fn index_mut(&mut self, index: usize) -> &mut Self::Output {
        self.buf.index_mut(index)
    }
}

pub mod exercises {
    use super::BinaryTree;
    use crate::tree::parent_tree::ParentTree;

    impl<T: Copy + Default> From<ParentTree<T>> for BinaryTree<T> {
        fn from(value: ParentTree<T>) -> Self {
            let btree_size = 2_usize.pow(value.depth() as u32) - 1;

            let mut tree = BinaryTree::from(vec![T::default(); btree_size]);

            // TODO: type F, Option<T>
            for (index, (value, parent)) in value.into_iter().enumerate() {
                match parent {
                    Some(parent) => {
                        let child = parent * 2 + 1;

                        if tree.get(child) == Some(def) {}
                    }
                    None => tree[0] = *value,
                }
            }

            // BinaryTree::from(Box::from([]))
            // for (i, p) in value.parents.iter().enumerate() {
            //     match p {
            //         Some(v) => {
            //             let mut idx = v * 2 + 1;
            //             if t.get(idx).is_some() {
            //                 idx += 1;
            //             }
            //
            //             t[idx] = value.nodes[i];
            //         }
            //         None => t[0] = value.nodes[0],
            //     }
            // }

            tree
        }
    }
}
