import java.io.FileReader;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        var stdin = new Scanner(System.in);

        try {
            var fileName = stdin.next();

            try {
                var file = new Scanner(new FileReader(fileName));

                var columns_total = new Double[] { 0.0, 0.0 };
                var rows = 0;

                try {
                    while (file.hasNextDouble()) {
                        columns_total[0] += file.nextDouble();
                        if (file.hasNextDouble())
                            columns_total[1] += file.nextDouble();

                        rows++;
                    }
                } finally {
                    file.close();
                }

                System.out.println(columns_total[0] / rows);
                System.out.println(columns_total[1] / rows);

            } catch (Exception e) {
                System.err.println("File not found! Are you sure it exists?" + e);
            }

        } finally {
            stdin.close();
        }
    }
}
