package algorithms.struct;

/**
 * Comparable is needed for has, min and max
 */
public class LinkedList<T extends Comparable<? super T>> {
    Node<T> head;

    public void push(T value) {
        head = new Node<T>(value, head);
    }

    public Boolean has(T value) {
        var node = head;

        while (node != null) {
            if (node.value.compareTo(value) == 0)
                return true;
            node = node.next;
        }

        return false;
    }

    public T min() {
        var node = head;
        var min = head.value;

        while (node != null) {
            if (min.compareTo(node.value) > 0)
                min = node.value;
            node = node.next;
        }

        return min;
    }

    public T max() {
        var node = head;
        var max = head.value;

        while (node != null) {
            if (max.compareTo(node.value) < 0)
                max = node.value;
            node = node.next;
        }

        return max;
    }

    void insertAfter(Node<T> node, T value) {
        node.next = new Node<T>(value, node.next);
    }

    void remove(Node<T> toRemove) {
        var prev = head;

        while (prev.next != toRemove)
            prev = prev.next;

        prev.next = toRemove.next;
    }

    Node<T> nodeAt(Integer index) throws IndexOutOfBoundsException {
        var node = head;

        while (index-- > 0) {
            if (node.next == null)
                throw new IndexOutOfBoundsException();
            node = node.next;
        }

        return node;
    }

    @Override
    public String toString() {
        var string = "[";
        var node = head;

        while (node != null) {
            string += node.toString() + ", ";
            node = node.next;
        }

        return string + "null]";
    }
}
