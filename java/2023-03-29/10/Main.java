import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        var input = new Scanner(System.in);
        char[] word;

        try {
            word = input.next().toCharArray();
        } finally {
            input.close();
        }

        for (int left = 0, right = word.length - 1; left < right; left++, right--) {
            var temp = word[left];
            word[left] = word[right];
            word[right] = temp;
        }

        System.out.println(word);
    }
}
