import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        var input = new Scanner(System.in);

        try {
            var exponent = input.nextInt();
            System.out.println((long) Math.pow(2, exponent));
        } finally {
            input.close();
        }

    }

}
