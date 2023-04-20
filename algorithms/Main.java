import algorithms.struct.Node;
import algorithms.struct.LinkedList;

public class Main {
    public static void main(String[] args) {
        var left = new LinkedList<Integer>();
        var right = new LinkedList<Integer>();

        left.push(30);
        left.push(20);
        left.push(10);

        right.push(50);
        right.push(15);
        right.push(10);
        right.push(5);

        System.out.println(right);
        System.out.println(left);

        var node = merge(left.head, right.head);
        while (node != null) {
            System.out.print(node + " ");
            node = node.next;
        }

    }

    public static <T extends Comparable<? super T>> Node<T> merge(Node<T> left, Node<T> right) {
        Node<T> merged = null;

        while (left != null && right != null) {
            if (left.value.compareTo(right.value) <= 0) {
                var next = left.next;
                left.next = merged;
                merged = left;
                left = next;
            } else {
                var next = right.next;
                right.next = merged;
                merged = right;
                right = next;
            }
        }

        while (left != null) {
            var next = left.next;
            left.next = merged;
            merged = left;
            left = next;
        }

        while (right != null) {
            var next = right.next;
            right.next = merged;
            merged = right;
            right = next;
        }

        return merged;
    }

    public static <T extends Comparable<? super T>> void mergeSort(Node<T> list, Integer size) {
        if (size == 2) {
            // strange merge stuff, get all the results
        }

    }
}
