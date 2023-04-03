import static java.util.Arrays.asList;
import java.util.List;

class Main {
    public static void main(String[] args) {
        var list = asList(new Integer[] { 2, 0, 8, 3, 1, -2, 6 });
        printList(list);
        insertionSort(list); // stable - best case o(n), as it doesn't do any swap
        selectionSort(list); // unstable - best case is o(n^2) (due to min)
        bubbleSort(list); // stable - best case with check is o(n)
        printList(list);
    }

    public static <T extends Comparable<T>> void insertionSort(List<T> list) {
        for (var index = 1; index < list.size(); index++) {
            var left = index;
            while (left > 0 && list.get(left).compareTo(list.get(left - 1)) < 0) {
                // swap
                var temp = list.get(left);
                list.set(left, list.get(left - 1));
                list.set(left - 1, temp);

                left--;
            }
        }
    }

    // TODO: binaryInsertionSort

    public static <T extends Comparable<T>> void selectionSort(List<T> list) {
        for (int index = 0; index < list.size(); index++) {
            var minIndex = min(list, index);

            var temp = list.get(index);
            list.set(index, list.get(minIndex));
            list.set(minIndex, temp);
        }
    }

    public static <T extends Comparable<T>> Integer min(List<T> list, Integer from) {
        var index = from;

        for (var offset = 1; from + offset < list.size(); offset++)
            if (list.get(from + offset).compareTo(list.get(index)) < 0)
                index = from + offset;

        return index;
    }

    public static <T extends Comparable<T>> void bubbleSort(List<T> list) {
        for (var left = 0; left < list.size(); left++)
            for (var right = left; right < list.size(); right++)
                if (list.get(left).compareTo(list.get(right)) > 0) {
                    var temp = list.get(left);
                    list.set(left, list.get(right));
                    list.set(right, temp);
                }
    }

    public static <T> void printList(List<T> list) {
        for (var item : list)
            System.out.printf("%s ", item);
        System.out.println();
    }
}
