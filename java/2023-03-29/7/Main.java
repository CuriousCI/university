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
            boolean vowel = false;
            for (var v : "aeiou".toCharArray())
                if (ch == v) {
                    vowel = true;
                    break;
                }

            System.out.print(vowel ? '_' : ch);
        }
    }
}
