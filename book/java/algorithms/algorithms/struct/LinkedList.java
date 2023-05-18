package algorithms.struct;

import java.util.Optional;

/**
 * Comparable is needed for has, min and max
 */
public class LinkedList<T extends Comparable<? super T>> {
    public Node<T> head, tail;

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

    public void join(LinkedList<T> list) {
        // TODO
        head.next = list.head;
        head = list.head;
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

    public Optional<Node<T>> removeLast() {
        if (head == null)
            return Optional.empty();

        if (head.next == null) {
            head = null;
            return Optional.empty();
        }

        var node = head;
        while (node.next.next != null)
            node = node.next;

        node.next = null;
        return Optional.of(head);
    }

    public void splitList() {
        Node<T> even = null, odd = null, node = head;
        var isEven = true;

        while (node != null) {
            var next = node.next;

            if (isEven) {
                node.next = even;
                even = node;
            } else {
                node.next = odd;
                odd = node;
            }

            node = next;
            isEven = !isEven;
        }

        node = even;
        while (node != null) {
            System.out.print(node + " ");
            node = node.next;
        }

        System.out.println();

        node = odd;
        while (node != null) {
            System.out.print(node + " ");
            node = node.next;
        }
    }

    public void countDuplicates() {

    }

    public Integer countOccurences(T value) {
        var occurences = 0;

        var node = head;
        while (node != null) {
            if (node.value == value)
                occurences++;
            node = node.next;
        }

        return occurences;
    }

    // TODO: reverse list?
    public Optional<T> last() {
        if (head == null)
            return Optional.empty();

        var node = head;
        while (node.next != null)
            node = node.next;

        return Optional.of(node.value);
    }

    // TODO: reverse list?
    public Optional<T> penultimate() {
        if (head == null)
            return Optional.empty();

        if (head.next == null)
            return Optional.empty();

        var node = head;
        while (node.next.next != null)
            node = node.next;

        return Optional.of(node.value);
    }

    // of(size)?
    public static Optional<LinkedList<Integer>> generateList(Integer size) {
        if (size == 0)
            return Optional.empty();

        var list = new LinkedList<Integer>();
        list.push(size);
        var result = generateList(size - 1);
        if (result.isPresent())
            list.join(result.get());
        return Optional.of(list);
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

    public String reverse(Node<T> node) {
        if (node == null)
            return "";
        return reverse(node.next) + " " + node.value;
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
