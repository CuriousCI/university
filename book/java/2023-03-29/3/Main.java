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

        var vocals = 0;
        for (var letter : word.toCharArray()) {
            if ("aeiou".contains(String.valueOf(letter)))
                vocals++;
        }

        System.out.println(vocals);
    }
}
