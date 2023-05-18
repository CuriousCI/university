import java.util.Scanner;

class Rectangle {
    public static void main(String[] args) {
        var input = new Scanner(System.in);
        double width, height;

        try {
            width = input.nextDouble();
            height = input.nextDouble();
        } finally {
            input.close();
        }

        System.out.printf("area: %f\n", width * height);
        System.out.printf("perimeter: %f\n", (width + height) * 2);
        System.out.printf("diagonal: %f\n", Math.sqrt(width * width + height * height));

    }
}
