import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try {
            File file = new File(getFileName());
            SuperMarket superMarket = SuperMarket.fromFile(file);

            System.out.printf("Highest price product %s\n\n", superMarket.getHighestPriceProduct());

            System.out.println("Average products prices");
            for (double p : superMarket.getAveragePrice()) {
                System.out.println(p);
            }

            System.out.println("\nFinished products:");
            for (Product p : superMarket.getFinishedProducts()) {
                System.out.println(p);
            }
        } catch (FileNotFoundException e) {
            System.err.println("File doesn't exist");
        } catch (Exception e) {
            System.err.println("File doesn't have the correct format");
        }

    }

    public static String getFileName() throws InputMismatchException {
        Scanner stdin = new Scanner(System.in);
        String filename = "";

        System.out.println("File name: ");
        try {
            filename = stdin.next();
        } finally {
            stdin.close();
        }

        return filename;
    }
}

class SuperMarket {
    private List<Product> products;

    private SuperMarket() {
        this.products = new ArrayList<>();
    }

    public static SuperMarket fromFile(File file)
            throws Exception, FileNotFoundException {
        SuperMarket superMarket = new SuperMarket();

        Scanner f = new Scanner(file);
        try {
            while (f.hasNext()) {
                Scanner line = new Scanner(f.nextLine());
                String code = line.next();
                String name = line.next();
                int quantity = line.nextInt();
                double unitPrice = line.nextDouble();

                superMarket.add(new Product(code, name, quantity, unitPrice));
            }
        } finally {
            f.close();
        }

        return superMarket;
    }

    public void add(Product p) {
        this.products.add(p);
    }

    public Product getHighestPriceProduct() {
        double highestPrice = 0;
        Product highestPriceProduct = null;

        for (Product p : this.products) {
            if (p.getUnitPrice() > highestPrice) {
                highestPrice = p.getUnitPrice();
                highestPriceProduct = p;
            }
        }

        return highestPriceProduct;
    }

    public List<Double> getAveragePrice() {
        List<Double> averagePrices = new ArrayList<>();

        for (Product p : this.products) {
            averagePrices.add(p.getAveragePrice());
        }

        return averagePrices;
    }

    public List<Product> getFinishedProducts() {
        List<Product> finished = new ArrayList<>();

        for (Product p : this.products) {
            if (p.getQuantity() == 0) {
                finished.add(p);
            }
        }

        return finished;
    }
}

class Product {
    private String code;
    private String name;
    private int quantity;
    private double unitPrice;

    public Product(String code, String name, int quantity, double unitPrice) {
        this.code = code;
        this.name = name;
        this.quantity = quantity;
        this.unitPrice = unitPrice;
    }

    public String getCode() {
        return this.code;
    }

    public String getName() {
        return this.name;
    }

    public int getQuantity() {
        return this.quantity;
    }

    public double getUnitPrice() {
        return this.unitPrice;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getAveragePrice() {
        if (this.quantity == 0)
            return 0;

        return this.unitPrice / this.quantity;
    }

    public void decreaseQuantity(int amount) throws Exception {
        if (amount > this.quantity)
            throw new Exception("There aren't enough items!");

        this.quantity -= amount;
    }

    public void setPrice(double price) throws Exception {
        if (price < 0)
            throw new Exception("The price must be positive!");

        this.unitPrice = price;
    }

    @Override
    public String toString() {
        return String.format(
                "Product: %s (%s)\n- quantity: %d\n- unitPrice: %.2f",
                this.name,
                this.code,
                this.quantity,
                this.unitPrice);
    }
}
