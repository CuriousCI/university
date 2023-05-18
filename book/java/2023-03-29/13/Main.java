import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        var input = new Scanner(System.in);

        try {
            var number = input.nextInt();
            while (number > 0) {
                System.out.println(number & 1);
                number /= 2;
            }
        } finally {
            input.close();
        }

    }

}
