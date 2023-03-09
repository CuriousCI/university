import java.awt.Rectangle;

class Main {
    public static void main(String[] args) {
        // Ex 3
        var r = new Rectangle(100, 123);
        System.out.println(r.getWidth() * r.getHeight()); // Area
                                                          //
        // Ex 4
        System.out.println((r.getWidth() + r.getHeight()) * 2); // Perimeter

        // Ex 5
        var rect1 = new Rectangle(1, 42); // Area 42
        var rect2 = new Rectangle(1, 20); // Perimeter 42
        System.out.println(rect1.getWidth() + " " + rect1.getHeight());
        System.out.println(rect2.getWidth() + " " + rect2.getHeight());

        // Ex 6
        var dist = new Rectangle(16, 22, 89, 79);
        System.out.println(dist.getX() + " " + dist.getY());
        dist.add(0, 0);
        System.out.println(dist.getX() + " " + dist.getY());
    }
}
