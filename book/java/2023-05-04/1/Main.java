import java.io.File;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try {
            var input = new Scanner(new File("./hello.txt"));
            System.out.println(input.nextLine());
        } catch (Exception e) {
            System.out.println("Li mortacci tua e chi non te lo dice in Si bemolle");
        }

    }
}
