import static java.util.Arrays.asList;

import util.Heap;

class Main {
    public static void main(String[] args) {
        var list1 = asList(new Integer[] { 10, 22, 12, 4901, 9801, 2901, 901, 1980, 9100, 9058879, 28, 2980, -12980,
                -2980, 2, -1 });

        var heap = new Heap<Integer>(list1);
        heapSort(heap);

        for (var item : list1)
            System.out.printf("%s ", item);

    }

    public static <T extends Comparable<? super T>> void heapSort(Heap<T> heap) {
        while (heap.hasItems())
            heap.pop();
    }
}
