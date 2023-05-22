use std::rc::Rc;

pub struct LinkedList<T> {
    pub value: T,
    pub next: Option<Rc<LinkedList<T>>>,
}

// impl<T> From<Vec<T>> for LinkedList<T> {
//     fn from(value: Vec<T>) -> Self {}
// }

impl<T> LinkedList<T> {
    pub fn new(value: T) -> Self {
        Self { value, next: None }
    }
}

pub mod exercises {
    use super::LinkedList;
    use std::rc::Rc;

    pub fn search<T: Eq>(list: Rc<LinkedList<T>>, value: T) -> Option<Rc<LinkedList<T>>> {
        let mut node = Some(Rc::clone(&list));

        while node.is_some() {
            if node.as_ref().unwrap().value == value {
                return Some(Rc::clone(&node.unwrap()));
            }

            node = node
                .as_ref()
                .unwrap()
                .next
                .and_then(|n| Some(Rc::clone(&n)));
        }

        node
    }
}
