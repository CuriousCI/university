
import java.util.Scanner;

public class ArithmeticDemo {

    public static void main(String[] args) {

        var input = new Scanner(System.in);
        long x1, x2;

        try {
            x1 = input.nextInt();
            x2 = input.nextInt();
        } finally {
            input.close();
        }

        System.out.println(x1 + x2);
        System.out.println(x1 - x2);
        System.out.println(x1 * x2);
        System.out.printf("average %.2f\n", ((x1 + x2) / 2.0f));
        System.out.printf("distance %8d\n", Math.abs(x1 - x2));
        System.out.printf("maximum %8d\n", Math.max(x1, x2));
        System.out.printf("minimum %8d\n", Math.min(x1, x2));

    }
}
