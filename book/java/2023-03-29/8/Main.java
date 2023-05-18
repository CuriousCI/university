import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        var input = new Scanner(System.in);
        String word;

        try {
            word = input.next();
        } finally {
            input.close();
        }

        for (var ch : word.toCharArray()) {
            System.out.println(ch);
        }
    }
}
