pub enum Category {
    Max,
    Min,
}

pub struct Heap<'a, T> {
    array: &'a mut [T],
    size: usize,
    category: Category,
}

impl<'a, T: Ord> Heap<'a, T> {
    pub fn new(array: &'a mut [T], category: Category) -> Self {
        let size = array.len();
        let mut heap = Self {
            array,
            size,
            category,
        };

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
            (Some(left), Some(right)) => {
                let (v, child) = if match self.category {
                    Category::Max => left > right,
                    Category::Min => left < right,
                } {
                    left
                } else {
                    right
                };

                if match self.category {
                    Category::Max => value < v,
                    Category::Min => value > v,
                } {
                    self.array.swap(child, index);
                    self.heapify(child);
                }
            }
            (Some((x, x_index)), None) => {
                if match self.category {
                    Category::Max => value < x,
                    Category::Min => value > x,
                } {
                    self.array.swap(x_index, index);
                }
            }
            _ => (),
        };
    }

    fn child(&self, index: usize, offset: usize) -> Option<(&T, usize)> {
        let index = 2 * index + offset;

        if index >= self.size {
            return None;
        }

        self.array.get(index).and_then(|v| Some((v, index)))
    }
}

impl<'a, T: Ord + Copy> Iterator for Heap<'a, T> {
    type Item = T;

    fn next(&mut self) -> Option<Self::Item> {
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
    Heap::new(array, Category::Max).into_iter().for_each(drop);
}

// Pdf 11, Slide 26
pub mod exercises {
    use super::*;

    // Ex 1, O(n) for MaxHeap, O(1) for MinHeap
    pub fn min<'a, T: Ord + Copy>(heap: &mut Heap<'a, T>) -> Option<T> {
        match heap.category {
            Category::Max => heap.last(),
            Category::Min => heap.next(),
        }
    }

    // Ex 2, Build a MinHeap struct
    pub struct MinHeap<'a, T> {
        heap: Heap<'a, T>,
    }

    impl<'a, T: Ord> MinHeap<'a, T> {
        pub fn new(array: &'a mut [T]) -> Self {
            Self {
                heap: Heap::new(array, Category::Min),
            }
        }
    }

    impl<'a, T: Ord + Copy> Iterator for MinHeap<'a, T> {
        type Item = T;

        fn next(&mut self) -> Option<Self::Item> {
            self.heap.next()
        }
    }

    // Ex 3, insert in Heap with available space
    impl<'a, T: Ord> Heap<'a, T> {
        pub fn insert(&mut self, value: T) -> Result<(), &'static str> {
            if self.size >= self.array.len() {
                return Err("Array is full");
            }

            self.array[self.size] = value;
            self.size += 1;
            self.build();
            Ok(())
        }
    }
}
