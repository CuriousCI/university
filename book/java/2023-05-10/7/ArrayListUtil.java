import java.util.ArrayList;

public class ArrayListUtil {
    public static <T> boolean isPalindrome(ArrayList<T> list) {
        var start = 0;
        var end = list.size() - 1;

        while (start < end) {
            if (!list.get(start++).equals(list.get(end--)))
                return false;
        }

        return true;
    }

}
