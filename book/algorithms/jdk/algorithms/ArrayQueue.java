package algorithms;

import java.util.Optional;

public class ArrayQueue<T> {
    Object[] queue;
    Integer head = 0, tail = 0, size = 0;

    public ArrayQueue(Integer size) {
        queue = new Object[size];
    }

    public void enqueue(T value) throws IndexOutOfBoundsException {
        if (size == queue.length)
            throw new IndexOutOfBoundsException();

        queue[tail] = value;
        tail++;
        if (tail >= queue.length)
            tail = 0;
    }

    public Optional<Object> pop() {
        if (size == 0)
            return Optional.empty();

        var result = queue[head];
        head++;
        if (head >= queue.length)
            head = 0;
        return Optional.of(result);
    }
}

// if (isFull())
// throw new IndexOutOfBoundsException();
// public Boolean isFull() {
// return Math.abs(head - tail) == 1;
// }
// if (top == 0)
// throw new IllegalAccessException();
// @Override
// public String toString() {
// var result = "";
//
// for (var value : queue)
// result += value + " ";
//
// return result;
// }
