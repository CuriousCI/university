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
