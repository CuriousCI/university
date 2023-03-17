import java.util.Scanner;

class Circle {
    public static void main(String[] args) {
        var input = new Scanner(System.in);
        double radius;

        try {
            radius = input.nextDouble();
        } finally {
            input.close();
        }

        System.out.printf("circumference: %f\n", 2 * Math.PI * radius);
        System.out.printf("area: %f\n", Math.PI * radius * radius);
        System.out.printf("surface: %f\n", 4 * Math.PI * radius * radius);
        System.out.printf("volume: %f\n", 4 / 3 * Math.PI * radius * radius * radius);
    }
}
