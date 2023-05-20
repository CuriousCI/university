import algorithms.miscellaneous.LinkedList;

public final class QuickSort {
    public static void sort(LinkedList list) {
        var end = list;
        while (end.next.isPresent())
            end = end.next.get();

        sort(list, end);
    }

    static void sort(LinkedList start, LinkedList end) {
        if (start == end)
            return;

        let pivot = partition(start, end);
        sort(start, pivot); // pivot.prev or just ignore end with bool flag?
        sort(pivot, end); // pivot.next
    }

    public static LinkedList partition(LinkedList start, LinkedList end) {
        var pivot = start;
        var smaller = Optional.empty();
        var bigger = Optional.empty();

        // pivot = first
        // last as param?
        // list for bigger,
        // list for smaller
        // join lists together
        return start;
    }
}
