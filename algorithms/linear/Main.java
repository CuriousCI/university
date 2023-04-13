import static java.util.Arrays.asList;

import java.util.ArrayList;
import java.util.List;

class Main {
    public static void main(String[] args) {
        var numbers = asList(new Integer[] { 0, 6, 7, 2, 5, 6, 1, 0, 4, 4, 1, 6 });

        print(numbers);
        // countingSort(numbers);
        stableCountingSort(numbers); // There's no need for demonstrations baby, it's stable!
        print(numbers);

        // bucketSort - worst case O(n^2) if insertion sort is used for buckets, because
        // in the worst case, a bucket has size O(n)
        // This algorithm can be used with countingSort,
        // considering that each bucket contain
        // numbers t, such that a < t < b, where 0 < b - a < k
        // but I have to know a and b in advance for each bucket, so it must be fixed

    }

    public static void countingSort(List<Integer> numbers) {
        // find max
        var max = numbers.get(0);
        for (var number : numbers)
            max = Math.max(max, number);

        // create emtpy counter array
        var counter = new ArrayList<Integer>(max);
        for (var index = 0; index <= max; index++)
            counter.add(0);

        // count numbers
        for (var number : numbers)
            counter.set(number, counter.get(number) + 1);

        // rearrange numbers
        var index = 0;
        for (var number = 0; number < counter.size(); number++)
            while (counter.get(number) > 0) {
                counter.set(number, counter.get(number) - 1);
                numbers.set(index, number);
                index++;
            }
    }

    public static void stableCountingSort(List<Integer> numbers) {
        // find max
        var max = numbers.get(0);
        for (var number : numbers)
            max = Math.max(max, number);

        // create emtpy counter array
        var counter = new ArrayList<Integer>(max);
        for (var index = 0; index <= max; index++)
            counter.add(0);

        // count numbers
        for (var number : numbers)
            counter.set(number, counter.get(number) + 1);

        // add up numbers
        for (var index = 1; index < counter.size(); index++)
            counter.set(index, counter.get(index - 1) + counter.get(index));

        // auxiliary array
        var aux = new ArrayList<Integer>(numbers.size());
        for (var index = 0; index < numbers.size(); index++)
            aux.add(0);

        // rearrange numbers in aux
        for (var index = numbers.size() - 1; index >= 0; index--) {
            var position = counter.get(numbers.get(index)) - 1;
            counter.set(numbers.get(index), position);
            aux.set(position, numbers.get(index));
        }
    }

    public static <T> void bucketSort(List<T> list) {
    }

    public static <T> void print(List<T> list) {
        for (var item : list)
            System.out.printf("%s ", item);
        System.out.println();
    }
}
