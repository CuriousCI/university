// TODO: implement IntoIter instead of Iterator, for reusability!

pub struct Heap<T> {
    buffer: Box<[T]>,
    size: usize,
}

impl<T: Ord + Default + Copy> Heap<T> {
    pub fn new<const SIZE: usize>() -> Self {
        Self {
            buffer: Box::new([Default::default(); SIZE]),
            size: 0,
        }
    }

    pub fn from(buffer: Box<[T]>) -> Self {
        let mut heap = Self {
            size: buffer.len(),
            buffer,
        };
        heap.build();
        heap
    }

    fn build(&mut self) {
        (0..self.size / 2).rev().for_each(|n| self.heapify(n));
    }

    fn heapify(&mut self, node: usize) {
        use std::cmp::max;

        if let Some((v, i)) = max(self.child(node, 1), self.child(node, 2)) {
            if self.buffer.get(node) < v {
                self.buffer.swap(node, i);
                self.heapify(i)
            }
        }
    }

    fn child(&self, node: usize, child: usize) -> Option<(Option<&T>, usize)> {
        let node = 2 * node + child;

        if node >= self.size {
            return None;
        }

        Some((self.buffer.get(node), node))
    }
}

impl<T: Ord + Default + Copy> Iterator for Heap<T> {
    type Item = T;

    fn next(&mut self) -> Option<Self::Item> {
        if self.size == 0 {
            return None;
        }

        self.buffer.swap(0, self.size - 1);
        self.size -= 1;
        self.heapify(0);

        Some(self.buffer[self.size])
    }
}

pub fn heap_sort<T: Ord + Copy + Default>(buffer: Box<[T]>) {
    Heap::from(buffer).into_iter().for_each(drop);
}

// Pdf 11, Slide 26
pub mod exercises {
    use std::cmp::Reverse;

    use super::*;

    // Ex 1, O(n) for MaxHeap, O(1) for MinHeap

    pub enum BinaryHeap<T> {
        MaxHeap(Heap<T>),
        MinHeap(MinHeap<T>),
    }

    pub fn min<T: Ord + Copy + Default>(heap: &mut BinaryHeap<T>) -> Option<T> {
        match heap {
            BinaryHeap::MaxHeap(heap) => heap.last(),
            BinaryHeap::MinHeap(heap) => heap.next(),
        }
    }

    // Ex 2, Build a MinHeap struct

    pub struct MinHeap<T> {
        heap: Heap<T>,
    }

    impl<T: Ord + Default + Copy> MinHeap<Reverse<T>> {
        pub fn from(buffer: Box<[T]>) -> Self {
            Self {
                heap: Heap::from(
                    buffer
                        .iter()
                        .map(|v| Reverse(*v))
                        .collect::<Vec<Reverse<T>>>()
                        .into_boxed_slice(),
                ),
            }
        }
    }

    impl<T: Ord + Default + Copy> Iterator for MinHeap<T> {
        type Item = T;

        fn next(&mut self) -> Option<Self::Item> {
            self.heap.next()
        }
    }

    // Ex 3, insert in Heap with available space

    impl<T: Ord + Default + Copy> Heap<T> {
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
