package algorithms.struct;

public class Node<T> {
    public T value;
    Node<T> next;
    Node<T> prev;

    Node(T value) {
        this.value = value;
    }

    Node(T value, Node<T> next) {
        this(value);
        this.next = next;
    }

    Node(T value, Node<T> next, Node<T> prev) {
        this(value, next);
        this.prev = prev;
    }

    @Override
    public String toString() {
        return value.toString();
    }
}
