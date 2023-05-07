pub struct LinkedList<T> {
    value: T,
    next: Option<Box<LinkedList<T>>>,
}

impl<T> LinkedList<T> {
    pub fn new(value: T) -> Self {
        Self { value, next: None }
    }
}
