use std::cmp::Ordering::{Equal, Greater, Less};
use std::ops::Index;

// Priority Queue
pub struct BinarySearchTree<K, V> {
    key: K,
    value: V,
    left: Option<Box<BinarySearchTree<K, V>>>,
    right: Option<Box<BinarySearchTree<K, V>>>,
    parent: Option<Box<BinarySearchTree<K, V>>>,
}

// impl<K, V> From<Vec<(K, V)>> for BinarySearchTree<K, V> {
//     fn from(value: Vec<(K, V)>) -> Self {
// Self {
// }
//     }
// }

impl<K: Ord, V> BinarySearchTree<K, V> {
    pub fn search(&self, key: K) -> Option<&V> {
        match key.cmp(&self.key) {
            Equal => Some(&self.value),
            Less => self.left.as_ref().and_then(|l| l.search(key)),
            Greater => self.right.as_ref().and_then(|r| r.search(key)),
        }
    }

    // Option<V>
    pub fn min(&self) -> &V {
        self.left
            .as_ref()
            .and_then(|l| Some(l.min()))
            .unwrap_or(&self.value)
    }

    pub fn max(&self) -> &V {
        self.right
            .as_ref()
            .and_then(|r| Some(r.max()))
            .unwrap_or(&self.value)
    }

    pub fn predecessor(&self) {
        match &self.left {
            Some(l) => (), // Most right in left
            None => (),    // First left parent
        }
    }

    pub fn successor() {}

    pub fn insert(&self, key: K, value: V) {}

    pub fn delete() {
        // No child
        // Only left
        // Only right
    }
}

impl<K, V> Index<K> for BinarySearchTree<K, V> {
    type Output = V;
    // type Idx = K;

    fn index(&self, index: K) -> &Self::Output {
        &self.value
    }
}
