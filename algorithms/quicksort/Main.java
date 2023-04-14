import java.util.ArrayList;
import java.util.List;

import static java.util.Arrays.asList;
import static java.util.Collections.sort;

class Main {
    public static void main(String args[]) {
        var dualArray = new Integer[] { 0, 2, 0, 0, 2, 0, 2, 0, 2, 0, 0 };
        System.out.println("= Before =");
        printArray(dualArray);

        // dualSort(dualArray);
        quickSort(asList(dualArray), 0, dualArray.length - 1);
        System.out.println("\n= After =");
        printArray(dualArray);

        var list = asList(new Item[] {
                new Item(2, 0),
                new Item(12, 0),
                new Item(-3, 0),
                new Item(-30, 0),
                new Item(1, 0),
                new Item(12, 1),
                new Item(1902, 0),
                new Item(1829, 0),
                new Item(2, 1),
                new Item(12, 2),
        });
        quickSort(list, 0, list.size() - 1);
        printArray(list);

        // var worstCase = new Integer[] { 0, 1, 2, 3, 4, 5, 6, 7 };

        // Equal elements
        // O(n^2) because all elements are on the left, or on the right

        // Already sorted, both ways
        // O(n^2)

        Integer[][] matrix = { { -1, 9, 2 }, { 4, -21, 9 }, { 121, 8, 7 } };
        System.out.println("\n\n= Before =");
        for (var row : matrix)
            printArray(row);

        matrixSort(matrix);
        System.out.println("\n= After =");
        for (var row : matrix)
            printArray(row);
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
        // array[i + 1] = array[high];
        //
        // array[high] = temp;
        return (i + 1);
    }

    static <T extends Comparable<? super T>> void quickSort(List<T> list, Integer low, Integer high) {
        if (low < high) {
            var pi = partition(list, low, high);
            quickSort(list, low, pi - 1);
            quickSort(list, pi + 1, high);
        }
    }

    public static void matrixSort(Integer[][] matrix) {
        var numbers = new ArrayList<Integer>();
        for (var row : matrix)
            for (var number : row)
                numbers.add(number);

        sort(numbers);

        for (var y = 0; y < matrix.length; y++)
            for (var x = 0; x < matrix[y].length; x++)
                matrix[y][x] = numbers.get(y * matrix[y].length + x);

    }

    public static int dualSort(Integer[] array) {
        var iterations = 0;

        for (int start = 0, end = array.length - 1; start < end; iterations++) {
            if (array[start] > array[end]) {
                // swap
                final var temp = array[start];
                array[start] = array[end];
                array[end] = temp;
            }

            if (array[end] == 2)
                end--;
            else
                start++;
        }

        return iterations;
    }

    public static <T> void printArray(List<T> array) {
        for (var item : array)
            System.out.printf("%s ", item);
        System.out.println();
    }

    public static <T> void printArray(T[] array) {
        for (var item : array)
            System.out.printf("%d ", item);
        System.out.println();
    }
}

class Item implements Comparable<Item> {
    Integer first, second;

    Item(Integer first, Integer second) {
        this.first = first;
        this.second = second;
    }

    @Override
    public int compareTo(Item item) {
        return first.compareTo(item.first);
    }

    @Override
    public String toString() {
        return String.format("first: %d - second: %d\n", first, second);
    }
}
