import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        var input = new Scanner(System.in);
        var max = 0.0;
        var period = 1;

        try {
            for (int month = 1; month <= 12; month++) {
                var temperature = input.nextDouble();
                if (temperature > max) {
                    max = temperature;
                    period = month;
                }
            }
        } finally {
            input.close();
        }

        System.out.printf("Highest Month: %d\n", period);
        System.out.printf("Highest Value: %.1f\n", max);
    }
}
