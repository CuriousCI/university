use std::ops::{Index, IndexMut};

use super::binary_tree::BinaryTree;

pub struct ParentTree<T> {
    buf: Box<[T]>,
    parents: Box<[Option<usize>]>,
}

impl<T> ParentTree<T> {
    pub fn depth(&self) -> usize {
        // TODO: O(n) better calculation
        self.buf.len()
    }

    pub fn parent_of(&mut self, index: usize, parent: Option<usize>) {
        self.parents[index] = parent;
    }
}

impl<T> From<Vec<T>> for ParentTree<T> {
    fn from(value: Vec<T>) -> Self {
        Self {
            parents: vec![None; value.len()].into_boxed_slice(),
            buf: value.into_boxed_slice(),
        }
    }
}

impl<T> Index<usize> for ParentTree<T> {
    type Output = T;

    fn index(&self, index: usize) -> &Self::Output {
        self.buf.index(index)
    }
}

impl<T> IndexMut<usize> for ParentTree<T> {
    fn index_mut(&mut self, index: usize) -> &mut Self::Output {
        self.buf.index_mut(index)
    }
}

impl<'a, T> IntoIterator for &'a ParentTree<T> {
    type Item = (&'a T, &'a Option<usize>);
    type IntoIter = ParentTreeIntoIterator<'a, T>;

    fn into_iter(self) -> Self::IntoIter {
        Self::IntoIter {
            tree: &self,
            index: 0,
        }
    }
}

pub struct ParentTreeIntoIterator<'a, T> {
    tree: &'a ParentTree<T>,
    index: usize,
}

impl<'a, T> Iterator for ParentTreeIntoIterator<'a, T> {
    type Item = (&'a T, &'a Option<usize>);

    fn next(&mut self) -> Option<Self::Item> {
        if self.index == self.tree.buf.len() {
            return None;
        }

        let result = (
            self.tree.buf.get(self.index).unwrap(),
            self.tree.parents.get(self.index).unwrap(),
        );

        self.index += 1;

        Some(result)
    }
}

// Pdf 16, Slide 32, Ex 2
impl<T: Copy + Default> From<BinaryTree<T>> for ParentTree<T> {
    fn from(value: BinaryTree<T>) -> Self {
        let mut tree = ParentTree::from(vec![T::default(); value.into_iter().count()]);

        for (index, (_, value)) in value.into_iter().enumerate() {
            tree[index] = value;
            tree.parent_of(
                index,
                if index == 0 {
                    None
                } else {
                    Some((index - 1) / 2)
                },
            )
        }

        tree
    }
}
