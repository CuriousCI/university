package algorithms;

import java.util.List;

public abstract class Search {

    public static <T extends Comparable<? super T>> Boolean binarySearch(List<T> list, T toFind) {
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

    public static <T extends Comparable<? super T>> Boolean search(List<T> list, T toFind) {
        for (var item : list)
            if (item.compareTo(toFind) == 0)
                return true;

        return false;
    }

    public static <T extends Comparable<? super T>> Integer upperBound(List<T> list, T toFind) {
        int jump = list.size() - 1, index = 0;

        while (jump > 0) {
            while (index + jump < list.size() && list.get(index + jump).compareTo(toFind) <= 0)
                index += jump;

            jump /= 2;
        }

        return index;
    }

    public static <T extends Comparable<? super T>> Integer lowerBound(List<T> list, T toFind) {
        int jump = list.size() - 1, index = list.size() - 1;

        while (jump > 0) {
            while (index - jump >= 0 && list.get(index - jump).compareTo(toFind) >= 0)
                index -= jump;

            jump /= 2;
        }

        return index;
    }
}
