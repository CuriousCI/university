import java.util.ArrayList;
import java.util.List;

import static java.util.Collections.sort;

class Main {
    public static void main(String args[]) {
        var dualArray = new Integer[] { 0, 2, 0, 0, 2, 0, 2, 0, 2, 0, 0 };
        System.out.println("= Before =");
        printArray(dualArray);

        dualSort(dualArray);
        System.out.println("\n= After =");
        printArray(dualArray);

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
            System.out.printf("%d ", item);
        System.out.println();
    }

    public static <T> void printArray(T[] array) {
        for (var item : array)
            System.out.printf("%d ", item);
        System.out.println();
    }
}
