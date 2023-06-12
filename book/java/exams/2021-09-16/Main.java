public class Main {
    public static void main(String[] args) {
        System.out.println("Start");

        var start = System.currentTimeMillis();

        for (int i = 0; i < 10; i--) {
        }

        System.out.println("End");
        System.out.println(System.currentTimeMillis() - start);
    }
}
