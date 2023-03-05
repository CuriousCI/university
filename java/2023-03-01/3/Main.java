import range.RangeInput;

class Main {
    public static void main(String[] args) {
        var range = new RangeInput(5, 10);
        System.out.println(range.value());

        for (int i = 0; i < 100; i++)
            range.up();
        System.out.println(range.value());

        for (int i = 0; i < 300; i++)
            range.down();
        System.out.println(range.value());

        range.up();
        range.up();
        System.out.println(range.value());
    }
}
