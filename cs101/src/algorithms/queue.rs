pub struct Queue<'a, T> {
    buffer: &'a mut [T],
    start: usize,
    end: usize,
    size: usize,
}

impl<'a, T> Queue<'a, T> {
    pub fn new(buffer: &'a mut [T]) -> Self {
        Self {
            buffer,
            start: 0,
            end: 0,
            size: 0,
        }
    }

    pub fn enqueue(&mut self, value: T) -> Result<(), &'static str> {
        if self.size == self.buffer.len() {
            return Err("Pirla la coda e' piena");
        }

        self.buffer[self.end] = value;
        self.size += 1;
        self.end = (self.end + 1) % self.buffer.len();

        Ok(())
    }

    pub fn dequeue(&mut self) -> Option<&T> {
        if self.size == 0 {
            return None;
        }

        let result = self.buffer.get(self.start);

        self.start = (self.start + 1) % self.buffer.len();
        self.size -= 1;

        result
    }
}

impl<'a, T: Copy> Iterator for Queue<'a, T> {
    type Item = T;

    fn next(&mut self) -> Option<Self::Item> {
        self.dequeue().and_then(|&v| Some(v))
    }
}
