pub struct ParentTree<T> {
    buf: Box<[T]>,
    parents: Box<[Option<usize>]>,
}

impl<T> ParentTree<T> {
    pub fn depth(&self) -> usize {
        self.buf.len()
    }
}

impl<T> From<Vec<T>> for ParentTree<T> {
    fn from(value: Vec<T>) -> Self {
        Self {
            buf: value.into_boxed_slice(),
            parents: vec![None; value.len()].into_boxed_slice(),
        }
    }
}

impl<'a, T> IntoIterator for &'a ParentTree<T> {
    type Item = (&'a T, &'a Option<usize>);
    type IntoIter = ParentTreeIntoIterator<'a, T>;

    fn into_iter(self) -> Self::IntoIter {
        Self::IntoIter {
            tree: &self,
            index: 0,
        }
    }
}

pub struct ParentTreeIntoIterator<'a, T> {
    tree: &'a ParentTree<T>,
    index: usize,
}

impl<'a, T> Iterator for ParentTreeIntoIterator<'a, T> {
    type Item = (&'a T, &'a Option<usize>);

    fn next(&mut self) -> Option<Self::Item> {
        if self.index == self.tree.buf.len() {
            return None;
        }

        let result = (
            self.tree.buf.get(self.index).unwrap(),
            self.tree.parents.get(self.index).unwrap(),
        );

        self.index += 1;

        Some(result)
    }
}

// impl<T: Copy> ParentTree<T> {
//     pub fn get(&self, index: usize) -> Option<T> {
//         self.nodes.get(index).and_then(|v| *v)
//     }
// }
//
// impl<T> ParentTree<T> {
//     pub fn from(nodes: Box<[Option<T>]>) -> Self {
//         Self {
//             parents: vec![None; nodes.len()].into_boxed_slice(),
//             nodes,
//         }
//     }
//
//     pub fn parent_of(&mut self, index: usize, value: Option<usize>) {
//         self.parents[index] = value;
//     }
//
//     pub fn parent(&self, index: usize) -> Option<usize> {
//         self.parents[index]
//     }
// }
//
// impl<T> Index<usize> for ParentTree<T> {
//     type Output = Option<T>;
//
//     fn index(&self, index: usize) -> &Self::Output {
//         self.nodes.index(index)
//     }
// }
//
// impl<T> IndexMut<usize> for ParentTree<T> {
//     fn index_mut(&mut self, index: usize) -> &mut Self::Output {
//         self.nodes.index_mut(index)
//     }
// }
