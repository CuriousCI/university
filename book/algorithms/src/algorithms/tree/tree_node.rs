use std::ops::{Index, IndexMut};

#[derive(Clone)]
pub struct TreeNode<T> {
    pub value: T,
    pub left: Option<Box<TreeNode<T>>>,
    pub right: Option<Box<TreeNode<T>>>,
}

impl<T: Default> Default for TreeNode<T> {
    fn default() -> Self {
        Self {
            value: T::default(),
            left: None,
            right: None,
        }
    }
}

pub struct ParentTree<T> {
    nodes: Box<[Option<T>]>,
    parents: Box<[Option<usize>]>,
}

impl<T: Copy> ParentTree<T> {
    pub fn get(&self, index: usize) -> Option<T> {
        self.nodes.get(index).and_then(|v| *v)
    }
}

impl<T> ParentTree<T> {
    pub fn from(nodes: Box<[Option<T>]>) -> Self {
        Self {
            parents: vec![None; nodes.len()].into_boxed_slice(),
            nodes,
        }
    }

    pub fn parent_of(&mut self, index: usize, value: Option<usize>) {
        self.parents[index] = value;
    }

    pub fn parent(&self, index: usize) -> Option<usize> {
        self.parents[index]
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
