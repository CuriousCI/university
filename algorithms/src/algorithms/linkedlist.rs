pub struct LinkedList<T> {
    value: T,
    next: Option<Box<LinkedList<T>>>,
}

// impl<T> From<Vec<T>> for LinkedList<T> {
//     fn from(value: Vec<T>) -> Self {
//     }
// }

impl<T> LinkedList<T> {
    pub fn new(value: T) -> Self {
        Self { value, next: None }
    }
}
