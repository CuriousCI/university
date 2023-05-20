package algorithms;

import java.util.List;
import java.util.Optional;

public abstract final class Search {
    public static <T> Optional<Integer> search(T[] array, T toFind) {
        for (var index = 0; index < array.length; index++)
            if (array[index] == toFind)
                return Optional.of(index);

        return Optional.empty();
    }

    public static <T extends Comparable<? super T>> Optional<Integer> binarySearch(T[] array, T toFind) {
        int jump = array.length - 1, index = 0;

        while (jump > 0) {
            while (index + jump < array.length) {
                var comparison = array[index + jump].compareTo(toFind);

                if (comparison > 0)
                    break;

                index += jump;

                if (comparison == 0)
                    return Optional.of(index);
            }

            jump /= 2;
        }

        return Optional.empty();
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
