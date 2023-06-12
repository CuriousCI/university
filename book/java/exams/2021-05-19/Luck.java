import java.util.Random;

public class Luck {
    public static void main(String[] args) {
        var random = new Random();
        var array = new int[20];

        for (int index = 0; index < array.length; index++)
            array[index] = random.nextInt(6) + 1;

        int maxLength = 0, maxStart = 0, maxEnd = 0;

        int start = 0, end = 0;
        while (start < array.length) {
            end = start;

            while (end < array.length && array[end] == array[start])
                end++;

            if (end - start > maxLength) {
                maxStart = start;
                maxEnd = end;
                maxLength = end - start;
            }

            start = end;
        }

        for (int index = 0; index < array.length; index++) {
            if (index == maxStart)
                System.out.print('(');

            System.out.print(array[index]);

            if (index == maxEnd - 1)
                System.out.print(')');

            System.out.print(' ');
        }

        int count;

        System.out.println();
        // F
        count = 0;
        for (int i = -10; i <= 10; i = i + 2) {
            count += 1;
            System.out.println(i);
        }
        System.out.println("f): " + count); // non termina
    }
}
