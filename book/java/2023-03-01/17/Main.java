import geometry.Rectangle;

class Main {
    public static void main(String[] args) {
        var r1 = new Rectangle(12.12, 89.1);
        var r2 = new Rectangle(72.29, 129.1);
        var r3 = new Rectangle(92.1, 76.1);

        System.out.println(r1.perimenter() + r2.perimenter() + r3.perimenter());
        System.out.println(r1.area() + r2.area() + r3.area());

        r1.scale(89, 299);
        System.out.println(r1.perimenter() + r2.perimenter() + r3.perimenter());
        System.out.println(r1.area() + r2.area() + r3.area());
    }
}
