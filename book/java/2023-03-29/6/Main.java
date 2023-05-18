import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        var input = new Scanner(System.in);
        var min = Integer.MAX_VALUE;

        try {
            while (input.hasNextInt()) {
                var number = input.nextInt();
                min = Math.min(min, number);
            }
        } finally {
            input.close();
        }

        System.out.printf("The minimum value was: %d\n", min);
    }
}
