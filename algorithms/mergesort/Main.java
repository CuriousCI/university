import static java.util.Arrays.asList;

import java.util.ArrayList;
import java.util.List;

class Main {
    public static void main(String[] args) {
        var list = asList(new Integer[] { -1, -22, 8, 128, 201, -123, 2, 9090, 2, -1190, 0 });
        // var list = asList(new Integer[] { 2, 0, 8, 3, 1, -2, 6 });
        print(list);
        mergeSort(list, 0, list.size());
        print(list);
    }

    public static <T> void print(List<T> list) {
        for (var item : list)
            System.out.printf("%s ", item);
        System.out.println();
    }

    public static <T extends Comparable<T>> void mergeSort(List<T> list, Integer start, Integer end) {
        var middle = (int) Math.floor((end + start) / 2);

        if (end - start == 1)
            return;

        mergeSort(list, start, middle);
        mergeSort(list, middle, end);
        merge(list, start, middle, end);
    }

    public static <T extends Comparable<T>> void merge(List<T> list, Integer start, Integer middle, Integer end) {
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
