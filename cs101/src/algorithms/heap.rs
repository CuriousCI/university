use std::cmp::Ordering;

pub struct Heap<'a, T> {
    array: &'a mut [T],
    size: usize,
}

impl<'a, T: Ord> Heap<'a, T> {
    pub fn new(array: &'a mut [T]) -> Self {
        let size = array.len();
        let mut instance = Self { array, size };
        instance.build_heap();
        instance
    }

    fn build_heap(&mut self) {
        for node in (0..(self.array.len() / 2) + 1).rev() {
            self.heapify(node);
        }
    }

    fn heapify(&mut self, index: usize) {
        let value = self.array.get(index).unwrap();

        match (self.left(index), self.right(index)) {
            (Some((x_index, x)), Some((y_index, y))) => {
                if value < x || value < y {
                    match x.cmp(y) {
                        Ordering::Greater => {
                            self.array.swap(x_index, index);
                            self.heapify(x_index);
                        }
                        _ => {
                            self.array.swap(y_index, index);
                            self.heapify(y_index);
                        }
                    }
                }
            }
            (Some((x_index, x)), None) => match value.cmp(x) {
                Ordering::Greater => self.array.swap(x_index, index),
                _ => (),
            },
            _ => (),
        };
    }

    pub fn pop(&mut self) -> Option<&T> {
        if self.size == 0 {
            return None;
        }

        self.array.swap(0, self.size - 1);
        self.size -= 1;
        self.heapify(0);

        self.array.get(self.size)
    }

    fn left(&self, node: usize) -> Option<(usize, &T)> {
        let i = 2 * node + 1;

        if i >= self.size {
            return None;
        }

        match self.array.get(i) {
            Some(v) => Some((i, v)),
            None => None,
        }
    }

    fn right(&self, node: usize) -> Option<(usize, &T)> {
        let i = 2 * node + 2;

        if i >= self.size {
            return None;
        }

        match self.array.get(i) {
            Some(v) => Some((i, v)),
            None => None,
        }
    }
}

pub fn heap_sort<T: Ord>(heap: &mut Heap<T>) {
    while heap.pop().is_some() {}
}
