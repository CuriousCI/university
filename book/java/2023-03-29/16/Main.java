
class Main {
    public static void main(String args[]) {
        for (int number = 1; number <= 10; number++) {
            for (int multiple = 1; multiple <= 10; multiple++)
                System.out.printf("%d ", number * multiple);
            System.out.println();
        }

    }
}
