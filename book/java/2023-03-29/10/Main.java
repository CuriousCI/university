import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        var input = new Scanner(System.in);

        try {
            var vowels = 0;

            for (var letter : input.nextLine().toCharArray())
                if (isVowel(letter))
                    vowels++;

            System.out.printf("%d vowel(s)", vowels);
        } finally {
            input.close();
        }
    }

    public static boolean isVowel(char letter) {
        for (var vowel : "aeiouAEIOU".toCharArray())
            if (letter == vowel)
                return true;
        return false;
    }
}
