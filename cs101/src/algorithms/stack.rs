pub struct Stack<'a, T> {
    buffer: &'a mut [T],
    size: usize,
}

impl<'a, T> Stack<'a, T> {
    pub fn new(buffer: &'a mut [T]) -> Self {
        Self { buffer, size: 0 }
    }

    pub fn push(&mut self, value: T) -> Result<(), &'static str> {
        if self.size == self.buffer.len() {
            return Err("Pirla, non hai piu' spazio per i piatti!");
        }

        self.buffer[self.size] = value;
        self.size += 1;

        Ok(())
    }

    pub fn pop(&mut self) -> Option<&T> {
        if self.size == 0 {
            return None;
        }

        self.size -= 1;
        self.buffer.get(self.size)
    }
}

impl<'a, T: Copy> Iterator for Stack<'a, T> {
    type Item = T;

    fn next(&mut self) -> Option<Self::Item> {
        self.pop().and_then(|&v| Some(v))
    }
}
