use std::rc::Rc;

#[derive(Debug)]
pub struct LinkedList<T> {
    pub value: T,
    pub next: Option<Rc<LinkedList<T>>>,
}

impl<T> LinkedList<T> {
    pub fn next_clone(&self) -> Option<Rc<LinkedList<T>>> {
        match &self.next {
            Some(v) => Some(Rc::clone(&v)),
            None => None,
        }
    }
}

impl<T> LinkedList<T> {
    pub fn new(value: T) -> Self {
        Self { value, next: None }
    }
}

pub mod exercises {
    use super::LinkedList;
    use std::rc::Rc;

    pub fn search<T: Eq>(list: Rc<LinkedList<T>>, value: T) -> Option<Rc<LinkedList<T>>> {
        let mut node = Some(list.clone());

        while node.is_some() {
            if node.as_ref().unwrap().value == value {
                return Some(node.unwrap().clone());
            }

            node = node.unwrap().next_clone();
        }

        node
    }
}
