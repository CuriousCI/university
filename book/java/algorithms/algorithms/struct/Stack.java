package algorithms.struct;

public class Stack<T> {
    Node<T> top;

    public void push(T value) {
        top = new Node<T>(value, top);
    }

    // Use Optional?
    public T pop() throws IllegalAccessException {
        if (top == null)
            throw new IllegalAccessException();

        var result = top.value;
        top = top.next;
        return result;
    }

    @Override
    public String toString() {
        var stackPointer = top;
        var result = "";

        while (stackPointer != null) {
            result += stackPointer + " ";
            stackPointer = stackPointer.next;
        }

        return result;
    }
}
