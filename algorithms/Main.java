import static java.util.Arrays.asList;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        var list = asList(new Integer[] { 10, 20, 1902, 190, 290, 10, 128810, 812001, -12982, -122198, 124 });
        System.out.println(hasDuplicates(list));
    }

    public static <T extends Comparable<? super T>> Boolean hasDuplicates(List<T> list) {

        for (var value : list)
            System.out.printf("%s ", value);
        System.out.println();
        return false;
    }
}
