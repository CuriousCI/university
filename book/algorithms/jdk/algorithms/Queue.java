package algorithms.struct;

import java.util.Optional;

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

    public Optional<T> dequeue() {
        if (head == null)
            return Optional.empty();

        var result = head.value;
        head = head.next;
        if (head == null)
            tail = null; // Queue is empty

        return Optional.of(result);
    }
}

// @Override
// public String toString() {
// var stackPointer = head;
// var result = "";
//
// while (stackPointer != null) {
// result += stackPointer + " ";
// stackPointer = stackPointer.next;
// }
//
// return result;
// }
