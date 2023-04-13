import static java.util.Arrays.asList;

import util.LinkedList;
import util.DoubleLinkedList;

class Main {
    public static void main(String[] args) {
        var list = asList(new Integer[] { 13, 2, 4, 5, 80, 12 });

        System.out.println("Linked List\n");
        var ll = new LinkedList<Integer>();
        for (var number : list)
            ll.append(number);

        System.out.println(ll);

        System.out.println(ll.search(13));
        System.out.println(ll.min().value);
        System.out.println(ll.max().value);

        ll.insert(ll.min(), 40);
        System.out.println(ll);

        ll.remove(ll.min());
        ll.remove(ll.min());
        ll.remove(ll.max());
        System.out.println(ll);

        ll.remove(ll.index(2));
        System.out.println(ll);

        System.out.println("\n\nDouble Linked List\n");
        var dll = new DoubleLinkedList<Integer>();
        for (var number : list)
            dll.append(number);

        System.out.println(dll);

        System.out.println(dll.search(13));
        System.out.println(dll.min().value);
        System.out.println(dll.max().value);

        dll.insert(dll.min(), 40);
        System.out.println(dll);

        dll.remove(dll.min());
        dll.remove(dll.min());
        dll.remove(dll.max());
        System.out.println(dll);

        dll.remove(dll.index(2));
        System.out.println(dll);
    }
}
