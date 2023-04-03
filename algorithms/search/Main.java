import static java.util.Arrays.asList;
import static java.util.Collections.sort;
import java.util.List;

import java.util.ArrayList;

class Main {
    public static void main(String[] args) {
        var array = asList(new Integer[] { 1, 98, 109, 22, 12, 2, 44, 12, 0, 9, 12, -8, -10 });

        var list = new ArrayList<Integer>(array);
        sort(list);

        System.out.printf("Does unsorted have %d? %s\n", 22, search(array, 22));
        System.out.printf("Does unsorted have %d? %s\n", -28, search(array, -28));
        System.out.printf("Does soted have %d? %s\n", 22, binarySearch(list, 22));
        System.out.printf("Does sorted have %d? %s\n", -28, binarySearch(list, -28));
        System.out.printf("Does sorted have %d? %s\n", 109, binarySearch(list, 109));
        System.out.printf("Does sorted have %d? %s\n", 12, binarySearch(list, 12));

        System.out.println("\n\nCount\n");
        System.out.printf("Count %d in unsorted - %d\n", 12, countOccurences(array, 12));
        for (var item : list)
            System.out.printf("%d ", item);
        System.out.println();

        System.out.printf("Count %d in sorted - %d\n", 12, upperBound(list, 12) - lowerBound(list, 12) + 1);
        System.out.printf("Count %d in sorted - %d\n", 3, upperBound(list, 3) - lowerBound(list, 3) + 1);
        System.out.printf("upperBound %d in sorted %d\n", 3, upperBound(list, 3));
        System.out.printf("lowerBound %d in sorted %d\n", 3, lowerBound(list, 3));
        System.out.printf("Count %d in sorted - %d\n", 1024, upperBound(list, 1024) - lowerBound(list, 1024) + 1);
        System.out.printf("upperBound %d in sorted %d\n", 1024, upperBound(list, 1024));
        System.out.printf("lowerBound %d in sorted %d\n", 1024, lowerBound(list, 1024));
        System.out.printf("Count occurences in range [%d, %d] in unsorted - %d\n", 3, 100, countRange(array, 3, 100));
        System.out.printf("Count occurences in range [%d, %d] in sorted - %d\n", 3, 100,
                upperBound(list, 100) - lowerBound(list, 3) + 1);
    }

    public static <T> Boolean search(List<T> list, T toFind) {
        for (var item : list)
            if (item == toFind)
                return true;

        return false;
    }

    public static <T extends Comparable<T>> Boolean binarySearch(List<T> list, T toFind) {
        int jump = list.size() - 1, index = 0;

        while (jump > 0) {
            while (index + jump < list.size() && list.get(index + jump).compareTo(toFind) <= 0) {
                var comparison = list.get(index + jump).compareTo(toFind);

                if (comparison < 0)
                    index += jump;
                if (comparison == 0)
                    return true;
            }

            jump /= 2;
        }

        return false;
    }

    public static <T> Integer countOccurences(List<T> list, T toCount) {
        int occurences = 0;

        for (var item : list)
            if (item == toCount)
                occurences++;

        return occurences;
    }

    public static <T extends Comparable<T>> Integer upperBound(List<T> list, T toFind) {
        int jump = list.size() - 1, index = 0;

        while (jump > 0) {
            while (index + jump < list.size() && list.get(index + jump).compareTo(toFind) <= 0)
                index += jump;

            jump /= 2;
        }

        return index;
    }

    public static <T extends Comparable<T>> Integer lowerBound(List<T> list, T toFind) {
        int jump = list.size() - 1, index = list.size() - 1;

        while (jump > 0) {
            while (index - jump >= 0 && list.get(index - jump).compareTo(toFind) >= 0)
                index -= jump;

            jump /= 2;
        }

        return index;
    }

    public static <T extends Comparable<T>> Integer countRange(List<T> list, T lowerBound, T upperBound) {
        var occurences = 0;
        for (var item : list)
            if (item.compareTo(lowerBound) >= 0 && item.compareTo(upperBound) <= 0)
                occurences++;

        return occurences;
    }
}
