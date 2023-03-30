import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        var input = new Scanner(System.in);
        var numbers = "";

        try {
            var last = -1;
            while (input.hasNextInt()) {
                var number = input.nextInt();
                if (number == last)
                    numbers += number + " ";
                last = number;
            }
        } finally {
            input.close();
        }

        System.out.printf("Adjacent numbers: %s\n", numbers);
    }
}
