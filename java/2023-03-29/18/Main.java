import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        var input = new Scanner(System.in);
        double rate, dollars;

        try {
            rate = input.nextDouble();
            dollars = input.nextDouble();
        } finally {
            input.close();
        }

        System.out.printf("%.6f", rate * dollars);

    }

}
