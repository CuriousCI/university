use std::cmp::Ordering::{Equal, Greater, Less};
use std::fmt::Debug;
use std::ops::Index;

// Priority Queue
#[derive(Clone, Debug)]
pub struct BinarySearchTree<K, V> {
    key: K,
    value: V,
    left: Option<Box<BinarySearchTree<K, V>>>,
    right: Option<Box<BinarySearchTree<K, V>>>,
    parent: Option<Box<BinarySearchTree<K, V>>>,
}

impl<K, V> From<(K, V)> for BinarySearchTree<K, V> {
    fn from(value: (K, V)) -> Self {
        Self {
            key: value.0,
            value: value.1,
            left: None,
            right: None,
            parent: None,
        }
    }
}

impl<K: Clone + Ord, V: Clone> From<Vec<(K, V)>> for BinarySearchTree<K, V> {
    fn from(value: Vec<(K, V)>) -> Self {
        let nodes: Vec<BinarySearchTree<K, V>> =
            value.into_iter().map(BinarySearchTree::from).collect();

        let mut root = nodes.get(0).unwrap().to_owned();
        for node in nodes.iter().skip(1) {
            root.insert(node.clone());
        }

        root
    }
}

impl<K: Ord, V> BinarySearchTree<K, V> {
    pub fn search(&self, key: K) -> Option<&V> {
        match key.cmp(&self.key) {
            Equal => Some(&self.value),
            Less => self.left.as_ref().and_then(|l| l.search(key)),
            Greater => self.right.as_ref().and_then(|r| r.search(key)),
        }
    }

    // Option<V>
    pub fn min(&self) -> (&K, &V) {
        self.left
            .as_ref()
            .and_then(|l| Some(l.min()))
            .unwrap_or((&self.key, &self.value))
    }

    pub fn max(&self) -> (&K, &V) {
        self.right
            .as_ref()
            .and_then(|r| Some(r.max()))
            .unwrap_or((&self.key, &self.value))
    }

    pub fn predecessor(&self) {
        match &self.left {
            Some(l) => (), // Most right in left
            None => (),    // First left parent
        }
    }

    pub fn successor() {}

    pub fn insert(&mut self, tree: BinarySearchTree<K, V>) {
        if tree.key < self.key {
            if let Some(l) = &mut self.left {
                l.insert(tree);
            } else {
                self.left = Some(Box::new(tree));
            }
        } else {
            if let Some(r) = &mut self.right {
                r.insert(tree)
            } else {
                // tree.parent = Some(Box::new(self));
                self.right = Some(Box::new(tree));
                // self.right.unwrap().parent = Some(Box::new(self));
            }
        }
    }

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

pub mod exercises {
    use super::BinarySearchTree;

    pub fn join<K, V>(
        x: BinarySearchTree<K, V>,
        y: BinarySearchTree<K, V>,
    ) -> BinarySearchTree<K, V> {
        x
    }
}
