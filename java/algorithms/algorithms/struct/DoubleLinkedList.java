package algorithms.struct;

/**
 * Comparable is needed for search, min and max
 */
public class DoubleLinkedList<T extends Comparable<T>> {
    Node<T> list;

    public void append(T value) {
        if (list == null)
            list = new Node<T>(value);
        else {
            var node = new Node<T>(value, list);
            list.prev = node;
            list = node;
        }
    }

    public void insert(Node<T> node, T value) {
        var item = new Node<T>(value, node.next);
        node.next = item;
    }

    public void remove(Node<T> node) {
        if (node.prev != null)
            node.prev.next = node.next;
        if (node.next != null)
            node.next.prev = node.prev;
    }

    public Node<T> index(Integer index) throws IndexOutOfBoundsException {
        var node = list;
        while (index-- > 0) {
            if (node.next == null)
                throw new IndexOutOfBoundsException();
            node = node.next;
        }

        return node;
    }

    public Node<T> search(T value) {
        var node = list;
        while (node != null) {
            if (node.value.compareTo(value) == 0)
                return node;
            node = node.next;
        }

        return null;
    }

    public Node<T> min() {
        var node = list;
        var min = node;

        while (node != null) {
            if (min.value.compareTo(node.value) > 0)
                min = node;
            node = node.next;
        }

        return min;
    }

    public Node<T> max() {
        var node = list;
        var max = node;

        while (node != null) {
            if (max.value.compareTo(node.value) < 0)
                max = node;
            node = node.next;
        }

        return max;
    }

    @Override
    public String toString() {
        var string = "[";
        var node = list;

        while (node != null) {
            string += node.toString() + ", ";
            node = node.next;
        }

        return string + "null]";
    }
}
