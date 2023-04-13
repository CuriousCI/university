package util;

public class Node<T> {
    public T value;
    Node<T> next;
    Node<T> previous;

    Node(T value) {
        this.value = value;
    }

    Node(T value, Node<T> next) {
        this.value = value;
        this.next = next;
    }

    Node(T value, Node<T> next, Node<T> previous) {
        this.value = value;
        this.next = next;
        this.previous = previous;
    }

    @Override
    public String toString() {
        return value.toString();
    }
}
