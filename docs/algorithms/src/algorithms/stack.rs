pub struct Stack<T> {
    buf: Box<[T]>,
    len: usize,
}

impl<T> From<Vec<T>> for Stack<T> {
    fn from(value: Vec<T>) -> Self {
        Self {
            buf: value.into_boxed_slice(),
            len: 0,
        }
    }
}

impl<T> Stack<T> {
    pub fn len(&self) -> usize {
        self.len
    }

    pub fn push(&mut self, value: T) -> Result<(), &'static str> {
        if self.len == self.buf.len() {
            return Err("Pirla, non hai piu' spazio per i piatti!");
        }

        self.buf[self.len] = value;
        self.len += 1;

        Ok(())
    }

    pub fn pop(&mut self) -> Option<&T> {
        if self.len == 0 {
            return None;
        }

        self.len -= 1;
        self.buf.get(self.len)
    }
}

impl<T: Copy> Iterator for Stack<T> {
    type Item = T;

    fn next(&mut self) -> Option<Self::Item> {
        self.pop().and_then(|&v| Some(v))
    }
}
