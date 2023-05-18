import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Main {
    public static List<String> readFileLines(String fileName) throws IOException {
        return Files
                .lines(Paths.get(fileName))
                .map(line -> new StringBuilder(line).reverse().toString())
                .toList();
    }

    public static void main(String[] args) {
        try {
            var file = new FileWriter(args[1]);
            for (var line : readFileLines(args[0]))
                file.write(line + "\n");
            file.close();
        } catch (Exception e) {
            System.err.println("Output file not found");
        }
    }
}
