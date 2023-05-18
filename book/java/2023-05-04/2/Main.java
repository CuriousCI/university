import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        var stdin = new Scanner(System.in);

        try {
            var fileName = stdin.next();
            var file = new Scanner(new File(fileName));

            var content = "";
            while (file.hasNextLine()) {
                var line = file.nextLine();
                if (line.trim().length() > 0)
                    content += line + '\n';
            }
            file.close();

            var writer = new BufferedWriter(new FileWriter(fileName));

            writer.write(content);
            writer.close();
        } catch (Exception e) {
        } finally {
            stdin.close();
        }

    }
}
