import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		var numbers = new Integer[10];

		var input = new Scanner(System.in);
		try {
			for (var index = 0; index < numbers.length; index++)
				numbers[index] = input.nextInt();
		} finally {
			input.close();
		}
	}
}
