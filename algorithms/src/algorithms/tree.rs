use std::ops::{Index, IndexMut};

pub struct TreeNode<T> {
    pub value: T,
    pub left: Option<Box<TreeNode<T>>>,
    pub right: Option<Box<TreeNode<T>>>,
}

pub struct BinaryTree<T> {
    nodes: Box<[Option<T>]>,
}

impl<T: Clone + Copy> BinaryTree<T> {
    pub fn new<const SIZE: usize>() -> Self {
        Self {
            nodes: Box::from([None; SIZE]),
        }
    }

    pub fn from(nodes: Box<[Option<T>]>) -> Self {
        Self { nodes }
    }

    pub fn left(&self, index: usize) -> Option<usize> {
        self.child(index, 1)
    }

    pub fn right(&self, index: usize) -> Option<usize> {
        self.child(index, 2)
    }

    fn child(&self, index: usize, offset: usize) -> Option<usize> {
        let index = index * 2 + offset;

        if index > self.nodes.len() {
            return None;
        }

        Some(index)
    }
}

impl<T> Index<usize> for BinaryTree<T> {
    type Output = Option<T>;

    fn index(&self, index: usize) -> &Self::Output {
        self.nodes.index(index)
    }
}

impl<T> IndexMut<usize> for BinaryTree<T> {
    fn index_mut(&mut self, index: usize) -> &mut Self::Output {
        self.nodes.index_mut(index)
    }
}

pub struct ParentTree<T> {
    nodes: Box<[Option<T>]>,
    parents: Box<[Option<usize>]>,
}

impl<T: Clone + Copy> ParentTree<T> {
    pub fn new<const SIZE: usize>() -> Self {
        Self {
            nodes: Box::from([None; SIZE]),
            parents: Box::from([None; SIZE]),
        }
    }

    pub fn from(nodes: Box<[Option<T>]>) -> Self {
        Self {
            parents: vec![None; nodes.len()].into_boxed_slice(),
            nodes,
        }
    }

    pub fn parent_of(&mut self, index: usize) -> &mut Option<usize> {
        self.parents.index_mut(index)
    }
}

impl<T> Index<usize> for ParentTree<T> {
    type Output = Option<T>;

    fn index(&self, index: usize) -> &Self::Output {
        self.nodes.index(index)
    }
}

impl<T> IndexMut<usize> for ParentTree<T> {
    fn index_mut(&mut self, index: usize) -> &mut Self::Output {
        self.nodes.index_mut(index)
    }
}

// pub trait Tree<T, L> { ??
//     fn father_of(id: L) -> T;
//     fn countChildren_of(id: L) -> usize;
//     fn distance_from_root(id: L) -> usize;
// }
//
// impl
// get father of()
// number of children of (v) (0, 1 or 2)
// distance from father
// impl iterator
//
// TODO: bfs
// TODO: dfs

pub mod exercises {
    use super::{BinaryTree, ParentTree};

    impl<T: Copy> From<ParentTree<T>> for BinaryTree<T> {
        fn from(value: ParentTree<T>) -> Self {
            BinaryTree::new::<10>()
        }
    }

    impl<T: Copy> From<BinaryTree<T>> for ParentTree<T> {
        fn from(value: BinaryTree<T>) -> Self {
            ParentTree::new::<10>()
        }
    }
}
