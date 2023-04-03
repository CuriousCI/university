import java.util.ArrayList;

class Main {
    public static void main(String[] args) {
        // var array = new Integer[] { -1, -22, 8, 128, 201, -123, 2, 9090, 2, -1190, 0
        // };
        var array = new Integer[] { 2, 0, 8, 3, 1, -2, 6 };
        System.out.println(hasDuplicates(array, 0, array.length - 1));
        for (var item : array)
            System.out.print(item + " ");
        System.out.println();

    }

    public static <T extends Comparable<? super T>> Boolean hasDuplicates(T[] array, int start, int end) {
        if (start == end)
            return false;

        var middle = (int) Math.floor((start + end) / 2);
        if (hasDuplicates(array, start, middle) ||
                hasDuplicates(array, middle + 1, end) ||
                merge(array, start, middle, end))
            return true;

        return false;
    }

    public static <T extends Comparable<? super T>> Boolean merge(
            T[] array,
            int left_start,
            int middle,
            int right_end) {

        int left_end = middle, right_start = middle + 1;
        var start = left_start;
        var merge = new ArrayList<T>();

        while (left_start < left_end && right_start < right_end) {
            var comparison = array[left_start].compareTo(array[right_start]);
            if (comparison == 0) {
                return true;
            } else if (comparison < 0) {
                merge.add(array[left_start]);
                left_start++;
            } else {
                merge.add(array[right_start]);
                right_start++;
            }
        }

        while (left_start < left_end) {
            merge.add(array[left_start]);
            if (left_start + 1 < left_end)
                if (array[left_start].compareTo(array[left_start + 1]) == 0)
                    return true;
            left_start++;
        }

        while (right_start < right_end) {
            merge.add(array[right_start]);
            if (right_start + 1 < right_end)
                if (array[right_start].compareTo(array[right_start + 1]) == 0)
                    return true;
            right_start++;
        }

        for (var index = left_start; index < right_end - 1; index++)
            array[index] = merge.get(index - left_start);

        return false;
    }
}
