package algorithms.sort;

import java.util.List;

import algorithms.struct.Heap;

public abstract class Standard {
    public static <T extends Comparable<? super T>> void heapSort(Heap<T> heap) {
        while (heap.hasItems())
            heap.pop();
    }

    public static <T extends Comparable<? super T>> void quickSort(List<T> list, Integer low, Integer high) {
        if (low < high) {
            var pi = partition(list, low, high);
            quickSort(list, low, pi - 1);
            quickSort(list, pi + 1, high);
        }
    }

    static <T extends Comparable<? super T>> Integer partition(List<T> list, Integer low, Integer high) {
        var pivot = list.get(high);
        Integer i = (low - 1);
        for (int j = low; j < high; j++) {
            if (list.get(j).compareTo(pivot) <= 0) {
                i++;
                var temp = list.get(i);
                list.set(i, list.get(j));
                list.set(j, temp);
            }
        }
        var temp = list.get(i + 1);
        list.set(i + 1, list.get(high));
        list.set(high, temp);

        return i + 1;
    }
}
