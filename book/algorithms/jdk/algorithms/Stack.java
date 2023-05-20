package algorithms.struct;

import java.util.Optional;

public class Stack<T> {
    Node<T> top;

    public void push(T value) {
        top = new Node<T>(value, top);
    }

    // Use Optional?
    public Optional<T> pop() {
        if (top == null)
            return Optional.empty();

        var result = top.value;
        top = top.next;
        return Optional.of(result);
    }
}

// @Override
// public String toString() {
// var stackPointer = top;
// var result = "";
//
// while (stackPointer != null) {
// result += stackPointer + " ";
// stackPointer = stackPointer.next;
// }
//
// return result;
// }
