package algorithms.struct;

public class Queue<T> {
    Node<T> head, tail;

    public void enqueue(T value) {
        var node = new Node<T>(value);

        if (tail == null) {
            head = node;
            tail = node;
        } else {
            tail.next = node;
            tail = tail.next;
        }
    }

    public T dequeue() throws IllegalAccessException {
        if (head == null)
            throw new IllegalAccessException();

        var result = head.value;
        head = head.next;
        if (head == null)
            tail = null; // Queue is empty
        return result;
    }

    @Override
    public String toString() {
        var stackPointer = head;
        var result = "";

        while (stackPointer != null) {
            result += stackPointer + " ";
            stackPointer = stackPointer.next;
        }

        return result;
    }
}
