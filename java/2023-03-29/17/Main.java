import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        var input = new Scanner(System.in);
        int side;

        try {
            side = input.nextInt();
        } finally {
            input.close();
        }

        for (int y = 0; y < side; y++)
            System.out.println(line(side));

        System.out.println();

        System.out.println(line(side));
        for (int y = 1; y < side - 1; y++)
            System.out.println(empty_line(side));
        System.out.println(line(side));
    }

    public static String line(int length) {
        var builder = new StringBuilder();
        for (int x = 0; x < length; x++)
            builder.append("#");

        return builder.toString();

    }

    public static String empty_line(int length) {
        var builder = new StringBuilder();
        for (int x = 0; x < length; x++)
            if (x == 0 || x == length - 1)
                builder.append("#");
            else
                builder.append(" ");

        return builder.toString();
    }
}
