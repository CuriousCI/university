import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        var input = new Scanner(System.in);
        var largest = 0;

        try {
            while (input.hasNextInt()) {
                var number = input.nextInt();
                largest = Math.max(number, largest);
            }
        } finally {
            input.close();
        }

        System.out.println(largest);
    }
}
