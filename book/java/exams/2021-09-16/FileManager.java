import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.HashSet;

public class FileManager {
    public static void main(String[] args) {

        var words = new HashSet<String>();
        words.add("ciao");
        words.add("come");
        words.add("va");
        words.add("ciao");
        words.add(new String("va"));

        for (var w : words) {
            System.out.println(w);
        }

        var file = new File("test.txt");
        try {
            var writer = new PrintWriter(file);
            try {
                for (var w : words)
                    writer.println(w);
            } finally {
                writer.close();
            }
        } catch (FileNotFoundException e) {
            System.err.println("File not found");
        }

    }

    // public static File getFile() {
    //
    // }
    //
    // public Set<String> getUniqueWords(File file) {
    //
    // }
    //
    // public void saveWords(File file, Set<String> uniqueWords) {
    //
    // }
}
