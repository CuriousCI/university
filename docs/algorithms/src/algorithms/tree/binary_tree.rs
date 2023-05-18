use std::ops::{Index, IndexMut};

use crate::stack::Stack;

pub struct BinaryTree<T> {
    buf: Box<[Option<T>]>,
}

impl<T> From<Vec<Option<T>>> for BinaryTree<T> {
    fn from(value: Vec<Option<T>>) -> Self {
        Self {
            buf: value.into_boxed_slice(),
        }
    }
}

impl<T> Index<usize> for BinaryTree<T> {
    type Output = Option<T>;

    fn index(&self, index: usize) -> &Self::Output {
        self.buf.index(index)
    }
}

impl<T> IndexMut<usize> for BinaryTree<T> {
    fn index_mut(&mut self, index: usize) -> &mut Self::Output {
        self.buf.index_mut(index)
    }
}

impl<'a, T: Copy> IntoIterator for &'a BinaryTree<T> {
    type Item = (usize, T);
    type IntoIter = BinaryTreeIterator<'a, T>;

    fn into_iter(self) -> Self::IntoIter {
        let mut stack = Stack::from(vec![0; self.buf.len()]);
        stack.push(0).unwrap();
        Self::IntoIter { tree: self, stack }
    }
}

pub struct BinaryTreeIterator<'a, T> {
    tree: &'a BinaryTree<T>,
    stack: Stack<usize>,
}

impl<'a, T: Copy> Iterator for BinaryTreeIterator<'a, T> {
    type Item = (usize, T);

    fn next(&mut self) -> Option<Self::Item> {
        if self.stack.len() == 0 {
            return None;
        }

        if let Some(&index) = self.stack.pop() {
            // let result = self.tree.buf.get(index).unwrap().unwrap();

            let children = index * 2;
            if let Some(l) = self.tree.buf.get(children + 1) {
                if let Some(_) = l {
                    self.stack.push(children + 1).unwrap();
                }
            }
            if let Some(r) = self.tree.buf.get(children + 2) {
                if let Some(_) = r {
                    self.stack.push(children + 2).unwrap();
                }
            }

            return Some((index, self.tree.buf[index].unwrap()));
            // return result.and_then(|v| Some((index, v)));
        }

        None
    }
}

pub mod exercises {
    use super::BinaryTree;
    use crate::{stack::Stack, tree::parent_tree::ParentTree};

    // Pdf 16, Slide 32, Ex 1
    impl<T: Copy> From<ParentTree<T>> for BinaryTree<T> {
        fn from(value: ParentTree<T>) -> Self {
            // get depth
            // generate positions array from parents with stack
            // create array with values and associated parents, using nodes number
            let btree_size = 2_usize.pow(value.depth() as u32) - 1;
            let mut tree = BinaryTree::from(vec![None; btree_size]);

            let parent_tree: Vec<(&T, &Option<usize>)> = value.into_iter().collect();
            let mut positions: Vec<Option<usize>> = vec![None; parent_tree.len()];

            for (mut index, (_, &parent)) in parent_tree.iter().enumerate() {
                match parent {
                    Some(parent) => {
                        if let Some(position) = positions[parent] {
                            positions[index] = Some(position * 2 + 1);
                        } else {
                            let mut visited_nodes = Stack::from(vec![0; parent_tree.len()]);

                            while positions[index].is_none() {
                                visited_nodes.push(index).unwrap();
                                index = parent_tree[index].1.unwrap();
                            }

                            for position in visited_nodes {
                                positions[position] = Some(
                                    positions[parent_tree[position].1.unwrap()].unwrap() * 2 + 1,
                                );
                            }
                        }
                    }
                    None => positions[index] = Some(0), // Root
                }
            }

            for (&position, (&value, _)) in positions.iter().zip(parent_tree) {
                let mut position = position.unwrap();

                if let Some(value) = tree.buf.get(position) {
                    if value.is_some() {
                        position += 1;
                    }
                }
                tree.buf[position] = Some(value);
            }

            tree
        }
    }
}
