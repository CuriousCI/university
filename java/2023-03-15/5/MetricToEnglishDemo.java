
import java.util.Scanner;

public class MetricToEnglishDemo {
    public static void main(String[] args) {
        var input = new Scanner(System.in);
        double distance;

        try {
            distance = input.nextDouble();
        } finally {
            input.close();
        }

        System.out.printf("miles: %f\n", distance * 0.0006213712);
        System.out.printf("feet: %f\n", distance * 3.28084);
        System.out.printf("inches: %f\n", distance * 39.37008);

    }
}
