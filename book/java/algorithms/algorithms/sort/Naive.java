package algorithms.sort;

import java.util.List;

public abstract class Naive {
    public static <T extends Comparable<? super T>> void insertionSort(List<T> list) {
        insertionSort(list, 0, list.size());
    }

    static <T extends Comparable<? super T>> void insertionSort(List<T> list, Integer start, Integer end) {
        for (var index = start + 1; index < end; index++) {
            var left = index;
            while (left > start && list.get(left).compareTo(list.get(left - 1)) < 0) {
                // swap
                var temp = list.get(left);
                list.set(left, list.get(left - 1));
                list.set(left - 1, temp);

                left--;
            }
        }
    }

    public static <T extends Comparable<? super T>> void selectionSort(List<T> list) {
        for (int index = 0; index < list.size(); index++) {
            var minIndex = min(list, index);

            var temp = list.get(index);
            list.set(index, list.get(minIndex));
            list.set(minIndex, temp);
        }
    }

    public static <T extends Comparable<? super T>> void bubbleSort(List<T> list) {
        for (var left = 0; left < list.size(); left++)
            for (var right = left; right < list.size(); right++)
                if (list.get(left).compareTo(list.get(right)) > 0) {
                    var temp = list.get(left);
                    list.set(left, list.get(right));
                    list.set(right, temp);
                }
    }

    static <T extends Comparable<? super T>> Integer min(List<T> list, Integer from) {
        var index = from;

        for (var offset = 1; from + offset < list.size(); offset++)
            if (list.get(from + offset).compareTo(list.get(index)) < 0)
                index = from + offset;

        return index;
    }
}
