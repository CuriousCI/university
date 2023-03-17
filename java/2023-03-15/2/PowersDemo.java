
import java.util.Scanner;

public class PowersDemo {

    public static void main(String[] args) {
        var input = new Scanner(System.in);
        double value;

        try {
            value = input.nextDouble();
        } finally {
            input.close();
        }

        for (int exponent = 2; exponent <= 4; exponent++)
            System.out.println(value + " power of " + exponent + " " + Math.pow(value, exponent));
    }
}
