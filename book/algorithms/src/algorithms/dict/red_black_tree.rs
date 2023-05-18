pub enum Color {
    Red,
    Black,
}

pub struct RedBlackTree<K, V> {
    key: K,
    value: V,
    color: Color,
    left: Option<Box<RedBlackTree<K, V>>>,
    right: Option<Box<RedBlackTree<K, V>>>,
    parent: Option<Box<RedBlackTree<K, V>>>,
}

// impl<K, V> From<Vec<(K, V)>> for RedBlackTree<K, V> {
//     fn from(value: Vec<(K, V)>) -> Self {}
// }

impl<K, V> RedBlackTree<K, V> {
    // rotate left
    // rotate right
    //
}
