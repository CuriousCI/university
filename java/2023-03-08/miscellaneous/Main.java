import java.util.Random;

class Main {
    public static void main(String[] args) {
        // Ex 13
        var rng = new Random();
        // for (int i = 0; i < 100; i++)
        System.out.println(rng.nextInt(1, 7));

        // Ex 14
        var price = rng.nextDouble() + rng.nextInt(100);
        System.out.printf("%.2f\n", price);

        // Ex 16
        // var day = new Day(); // LOLz must import the class
    }
}
