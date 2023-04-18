package algorithms.struct;

public class ArrayQueue<T> {
    Object[] queue;
    Integer head, tail;

    public ArrayQueue(Integer size) {
        queue = new Object[size];
        head = 0;
        tail = 0;
    }

    // public Boolean isFull() {
    // return Math.abs(head - tail) == 1;
    // }

    public void enqueue(T value) throws IndexOutOfBoundsException {
        // if (isFull())
        // throw new IndexOutOfBoundsException();

        queue[tail] = value;
        tail++;
        if (tail >= queue.length)
            tail = 0;
    }

    public Object pop() throws IllegalAccessException {
        // if (top == 0)
        // throw new IllegalAccessException();

        var result = queue[head];
        head++;
        if (head >= queue.length)
            head = 0;
        return result;
    }

    @Override
    public String toString() {
        var result = "";

        for (var value : queue)
            result += value + " ";

        return result;
    }
}
