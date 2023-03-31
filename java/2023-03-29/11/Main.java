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

        for (int start = 0; start < word.length(); start++)
            for (int offset = start; offset < word.length(); offset++)
                System.out.println(word.substring(start, offset));

    }
}
