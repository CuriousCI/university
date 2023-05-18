import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		var numbers = new Double[100];

		Double max = null, min = null;
		var input = new Scanner(System.in);
		try {
			for (var index = 0; index < numbers.length; index++) {
				numbers[index] = input.nextDouble();

				if (max == null || numbers[index] > max)
					max = numbers[index];
				if (min == null || numbers[index] < min)
					min = numbers[index];
			}
		} catch (Exception e) {
		} finally {
			input.close();
		}

		System.out.printf("max: %f\nmin: %f\n", max, min);
		for (var number : numbers)
			if (number != null)
				System.out.printf("%f ", number);
	}
}