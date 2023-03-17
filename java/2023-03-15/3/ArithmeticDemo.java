
import java.util.Scanner;

public class ArithmeticDemo {
    public static void main(String[] args) {

        var input = new Scanner(System.in);
        int x1, x2;

        try {
            x1 = input.nextInt();
            x2 = input.nextInt();
        } finally {
            input.close();
        }

        System.out.println(x1 + x2);
        System.out.println(x1 - x2);
        System.out.println(x1 * x2);
        System.out.println("average " + ((x1 + x2) / 2));
        System.out.println("distance " + Math.abs(x1 - x2));
        System.out.println("maximum " + Math.max(x1, x2));
        System.out.println("minimum " + Math.min(x1, x2));

    }
}
