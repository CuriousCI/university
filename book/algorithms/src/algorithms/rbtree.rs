use std::rc::Rc;

pub enum Color {
    Red,
    Black,
}

pub struct RBTree<T: Ord> {
    value: T,
    color: Color,
    left: Option<Rc<RBTree<T>>>,
    right: Option<Rc<RBTree<T>>>,
    parent: Option<Rc<RBTree<T>>>,
}

impl<T: Ord> RBTree<T> {}
