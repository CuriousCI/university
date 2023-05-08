use super::tree_node::TreeNode;
use std::cmp::{max, Ordering};

// pub enum Tree<T> {
//     TreeNode(TreeNode<T>),
//     BinaryTree(BinaryTree<T>),
//     ParentTree(ParentTree<T>),
// }

pub fn height<T>(tree: &TreeNode<T>) -> usize {
    1 + max(
        tree.left
            .as_ref()
            .and_then(|l| Some(height(l)))
            .unwrap_or(0),
        tree.right
            .as_ref()
            .and_then(|r| Some(height(r)))
            .unwrap_or(0),
    )
}

pub fn nodes_at_height<T>(tree: &TreeNode<T>, height: usize) -> usize {
    count_nodes_at_height(tree, height, 0)
}

fn count_nodes_at_height<T>(tree: &TreeNode<T>, height: usize, level: usize) -> usize {
    match level.cmp(&height) {
        Ordering::Less => {
            tree.left
                .as_ref()
                .and_then(|l| Some(count_nodes_at_height(l, height, level + 1)))
                .unwrap_or(0)
                + tree
                    .right
                    .as_ref()
                    .and_then(|r| Some(count_nodes_at_height(r, height, level + 1)))
                    .unwrap_or(0)
        }

        Ordering::Equal => 1,
        Ordering::Greater => 0,
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
