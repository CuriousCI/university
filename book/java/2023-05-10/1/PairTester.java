public class PairTester {
    public static void main(String[] args) {
        Pair<Integer> p = new Pair<>(17, 19);
        System.out.println(p.getFirst());
        System.out.println("Expected: 17");
        System.out.println(p.getSecond());
        System.out.println("Expected: 19");
    }
}
