import counter.Counter;
import counter.LimitedCounter;

class Main {
    public static void main(String[] args) {
        System.out.println("Counter Test\n");

        var obj = new Counter();

        for (int i = 0; i < 10; i++)
            obj.click();
        System.out.println(obj.getValue());

        obj.reset();
        System.out.println(obj.getValue());

        for (int i = 0; i < 299; i++)
            obj.click();
        System.out.println(obj.getValue());

        for (int i = 0; i < 1000; i++)
            obj.undo();
        System.out.println(obj.getValue());

        System.out.println("\n\nLimited Counter Test\n");

        var cnt = new LimitedCounter();
        cnt.setLimit(3);

        for (int i = 0; i < 10; i++)
            cnt.click();
        System.out.println(obj.getValue());

        cnt.reset();
        System.out.println(cnt.getValue());

        for (int i = 0; i < 299; i++)
            cnt.click();
        System.out.println(cnt.getValue());

        for (int i = 0; i < 1000; i++)
            cnt.undo();
        System.out.println(cnt.getValue());
    }
}
