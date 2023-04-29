// TODO: implement IntoIter instead of Iterator, for reusability!
pub struct Heap<'a, T> {
    buffer: &'a mut [T],
    size: usize,
}

impl<'a, T: 'a + Ord> Heap<'a, T> {
    pub fn new(buffer: &'a mut [T]) -> Self {
        let mut heap = Self {
            size: buffer.len(),
            buffer,
        };

        heap.build();
        heap
    }

    fn build(&mut self) {
        (0..self.buffer.len() / 2)
            .rev()
            .for_each(|index| self.heapify(index))
    }

    fn heapify(&mut self, index: usize) {
        let value = self.buffer.get(index).unwrap();

        match (self.child(index, 1), self.child(index, 2)) {
            (Some(left), Some(right)) => {
                let (v, child) = if left > right { left } else { right };
                if value < v {
                    self.buffer.swap(child, index);
                    self.heapify(child);
                }
            }
            (Some((x, x_index)), None) => {
                if value < x {
                    self.buffer.swap(x_index, index);
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

        self.buffer
            .get(index)
            .and_then(|value| Some((value, index)))
    }
}

impl<'a, T: 'a + Ord + Copy> Iterator for Heap<'a, T> {
    type Item = &'a T;

    fn next(&mut self) -> Option<Self::Item> {
        if self.size == 0 {
            return None;
        }

        self.buffer.swap(0, self.size - 1);
        self.size -= 1;
        self.heapify(0);

        None
        // self.buffer.get(self.size)
    }
}

pub fn heap_sort<T: Ord + Copy>(array: &mut [T]) {
    Heap::new(array).into_iter().for_each(drop);
}

// Pdf 11, Slide 26
pub mod exercises {
    use super::*;

    // Ex 1, O(n) for MaxHeap, O(1) for MinHeap
    pub fn min<'a, T: Ord + Copy>(heap: &mut Heap<'a, T>) -> Option<&'a T> {
        heap.last()
    }

    // Ex 2, Build a MinHeap struct
    pub struct MinHeap<'a, T> {
        heap: Heap<'a, T>,
    }

    impl<'a, T: Ord> MinHeap<'a, T> {
        pub fn new(array: &'a mut [T]) -> Self {
            Self {
                heap: Heap::new(array),
            }
        }
    }

    impl<'a, T: 'a + Ord + Copy> Iterator for MinHeap<'a, T> {
        type Item = &'a T;

        fn next(&mut self) -> Option<Self::Item> {
            self.heap.next()
        }
    }

    // Ex 3, insert in Heap with available space
    impl<'a, T: Ord> Heap<'a, T> {
        pub fn insert(&mut self, value: T) -> Result<(), &'static str> {
            if self.size >= self.buffer.len() {
                return Err("Array is full");
            }

            self.buffer[self.size] = value;
            self.size += 1;
            self.build();

            Ok(())
        }
    }
}

// mod exam {
//     use std::ops::Mul;
//
//     pub struct MulHeap<'a> {
//         buffer: Vec<i64>,
//         size: usize,
//     }
//
//     impl<'a, T> MulHeap<'a> {
//         pub fn new(array: &'a mut [i64], len: usize) {
//             Self {
//                 size: buffer.len(),
//                 buffer,
//             }
//         }
//     }
// }
