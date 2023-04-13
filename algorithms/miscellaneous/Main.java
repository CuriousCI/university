import static java.util.Arrays.asList;

import java.util.ArrayList;
import java.util.List;

class Main {
    public static void main(String[] args) {
        // var array = new Integer[] { -1, -22, 8, 128, 201, -123, 2, 9090, 2, -1190, 0
        // };
        // var list = asList(new Integer[] { 2, 1, 2 });
        var list = asList(new Integer[] { 2, 0, 8, 3, 12, -2, 6, 1 });
        System.out.println(hasDuplicates(list, 0, list.size()));
    }

    public static <T extends Comparable<T>> Boolean hasDuplicates(List<T> list, Integer start, Integer end) {
        var middle = (int) Math.floor((end + start) / 2);

        if (end - start == 1)
            return false;

        return hasDuplicates(list, start, middle) ||
                hasDuplicates(list, middle, end) ||
                merge(list, start, middle, end);
    }

    public static <T extends Comparable<T>> Boolean merge(List<T> list, Integer start, Integer middle, Integer end) {
        var merge = new ArrayList<T>();
        Integer left = start, right = middle;

        while (left < middle && right < end) {
            var comparison = list.get(left).compareTo(list.get(right));
            if (comparison == 0)
                return true;

            if (comparison < 0)
                merge.add(list.get(left++));
            else
                merge.add(list.get(right++));
        }

        while (left < middle) {
            if (left < middle - 1)
                if (list.get(left).compareTo(list.get(left + 1)) == 0)
                    return true;
            merge.add(list.get(left++));
        }

        while (right < end) {
            if (right < end - 1)
                if (list.get(right).compareTo(list.get(right + 1)) == 0)
                    return true;
            merge.add(list.get(right++));
        }

        for (var index = 0; start + index < end; index++)
            list.set(start + index, merge.get(index));

        return false;
    }

}
