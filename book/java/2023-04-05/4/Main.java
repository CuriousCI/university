import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        var numbers = new Double[100];

        var input = new Scanner(System.in);
        try {
            for (var index = 0; index < numbers.length; index++)
                if (input.hasNextDouble())
                    numbers[index] = input.nextDouble();
                else
                    break;
        } finally {
            input.close();
        }

        Double sum = 0.0, min = numbers[0];
        for (var number : numbers) {
            if (number == null)
                continue;

            if (number < min)
                min = number;
            sum += number;
        }
        System.out.println(sum - min);
    }
}
