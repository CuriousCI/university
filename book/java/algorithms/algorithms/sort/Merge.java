package algorithms.sort;

import static algorithms.sort.Naive.insertionSort;
import java.util.ArrayList;
import java.util.List;

public abstract class Merge {
    static final double BASE_2 = Math.log(2);

    public static <T extends Comparable<? super T>> void timSort(List<T> list, Integer start, Integer end) {
        var middle = (int) Math.floor((end + start) / 2);

        if (end - start == 1)
            return;

        if (end - start > Math.log(list.size()) / BASE_2) {
            timSort(list, start, middle);
            timSort(list, middle, end);
            merge(list, start, middle, end);
        } else
            insertionSort(list, start, end);

    }

    public static <T extends Comparable<T>> void mergeSort(List<T> list, Integer start, Integer end) {
        var middle = (int) Math.floor((end + start) / 2);

        if (end - start == 1)
            return;

        mergeSort(list, start, middle);
        mergeSort(list, middle, end);
        merge(list, start, middle, end);
    }

    static <T extends Comparable<? super T>> void merge(List<T> list, Integer start, Integer middle, Integer end) {
        var merge = new ArrayList<T>();
        Integer left = start, right = middle;

        while (left < middle && right < end)
            if (list.get(left).compareTo(list.get(right)) < 0)
                merge.add(list.get(left++));
            else
                merge.add(list.get(right++));

        while (left < middle)
            merge.add(list.get(left++));

        while (right < end)
            merge.add(list.get(right++));

        for (var index = 0; start + index < end; index++)
            list.set(start + index, merge.get(index));
    }
}
