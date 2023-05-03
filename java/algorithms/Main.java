// import static java.util.Arrays.asList;

// import java.util.List;

import algorithms.struct.Node;
import algorithms.struct.Queue;
import algorithms.struct.LinkedList;

public class Main {
    public static void main(String[] args) {
        var a = new Queue();
        a.enqueue(10);
        a.enqueue(20);
        a.enqueue(7);

        var b = a;
        b.enqueue(28);
        b.enqueue(28);

        a.enqueue(12);

        System.out.println(a);
        // var n = a.dequeue();
        // while (n.isPresent()) {
        // System.out.println(n);
        // }

    }

    // public static <T extends Comparable<? super T>> Boolean hasDuplicates(List<T>
    // list) {
    //
    // for (var value : list)
    // System.out.printf("%s ", value);
    // System.out.println();
    // return false;
    // }

    public static <T extends Comparable<? super T>> Node<T> merge(Node<T> left, Node<T> right) {
        Node<T> head = new Node<T>(left.value);
        Node<T> merged = head;

        while (left != null && right != null) {
            if (left.value.compareTo(right.value) <= 0) {
                var next = left.next;
                merged.next = left;
                merged = merged.next;
                left = next;
            } else {
                var next = right.next;
                merged.next = right;
                merged = merged.next;
                right = next;
            }
        }

        merged.next = left == null ? right : left;
        return head.next;
    }

    public static <T extends Comparable<? super T>> Node<T> merge2(Node<T> left, Node<T> right) {
        Node<T> head = new Node<T>(left.value);
        Node<T> merged = head;

        while (left != null && right != null) {
            if (left.value.compareTo(right.value) <= 0) {
                merged.next = left;
                left = left.next;
            } else {
                merged.next = right;
                right = right.next;
            }

            merged = merged.next;
        }

        merged.next = left == null ? right : left;
        return head.next;
    }
}
