import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

import javax.annotation.processing.FilerException;

public class Hotel {
    public static void main(String[] args) {
        try {
            var input = new Scanner(new File("data.txt"));
            var services = new HashSet<String>();
            var entries = new ArrayList<Entry>();

            try {
                while (input.hasNext()) {
                    var lineScanner = new Scanner(input.nextLine());
                    lineScanner.useDelimiter(";");

                    var name = lineScanner.next();
                    var service = lineScanner.next();
                    var price = lineScanner.nextDouble();
                    var date = lineScanner.next();

                    services.add(service);
                    entries.add(new Entry(name, service, price, date));
                }
            } catch (Exception e) {
                System.out.println("Formato del file non valido");
            } finally {
                input.close();
            }

            for (var service : services) {
                double total = 0;

                for (var entry : entries)
                    if (entry.service.equals(service))
                        total += entry.price;

                System.out.printf("%s: %.2f\n", service, total);
            }
        } catch (FileNotFoundException e) {
            System.out.println("File non esiste");
        }

    }
}

class Entry {
    public final String name, service, date;
    public final double price;

    public Entry(String name, String service, double price, String date) {
        this.name = name;
        this.service = service;
        this.price = price;
        this.date = date;
    }
}
