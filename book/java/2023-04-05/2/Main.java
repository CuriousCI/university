import java.util.Random;

class Main {
	public static void main(String[] args) {
		var numbers = new Integer[100];
		var random = new Random();

		for (var index = 0; index < numbers.length; index++)
			numbers[index] = random.nextInt(0, 100);

		// Even index numbers
		for (var index = 0; index < numbers.length; index += 2)
			System.out.printf("%d ", numbers[index]);
		System.out.println();

		// Odd value numbers
		for (var index = 0; index < numbers.length; index++)
			if (numbers[index] % 2 == 1)
				System.out.printf("%d ", numbers[index]);
		System.out.println();

		// Numbers in reverse order
		for (var index = numbers.length - 1; index >= 0; index--)
			System.out.printf("%d ", numbers[index]);
		System.out.println();

		// Numbers in first and last position
		System.out.println(numbers[0]);
		System.out.println(numbers[numbers.length - 1]);
	}
}