pub struct Heap<'a, T> {
    array: &'a mut [T],
    size: usize,
}

impl<'a, T: Ord> Heap<'a, T> {
    pub fn new(array: &'a mut [T]) -> Self {
        let size = array.len();
        let mut heap = Self { array, size };

        heap.build();
        heap
    }

    fn build(&mut self) {
        for node in (0..(self.array.len() / 2) + 1).rev() {
            self.heapify(node);
        }
    }

    fn heapify(&mut self, index: usize) {
        let value = self.array.get(index).unwrap();

        match (self.child(index, 1), self.child(index, 2)) {
            (Some((x_index, x)), Some((y_index, y))) => {
                if value < x || value < y {
                    let child = if x > y { x_index } else { y_index };

                    self.array.swap(child, index);
                    self.heapify(child);
                }
            }
            (Some((x_index, x)), None) => {
                if value > x {
                    self.array.swap(x_index, index);
                }
            }
            _ => (),
        };
    }

    fn child(&self, index: usize, offset: usize) -> Option<(usize, &T)> {
        let index = 2 * index + offset;

        if index >= self.size {
            return None;
        }

        self.array.get(index).and_then(|v| Some((index, v)))
    }
}

impl<'a, T: Ord + Copy> Iterator for Heap<'a, T> {
    type Item = T;

    fn next(&mut self) -> Option<T> {
        if self.size == 0 {
            return None;
        }

        self.array.swap(0, self.size - 1);
        self.size -= 1;
        self.heapify(0);

        Some(self.array[self.size])
    }
}

pub fn heap_sort<T: Ord + Copy>(array: &mut [T]) {
    Heap::new(array).into_iter().for_each(drop);
}
