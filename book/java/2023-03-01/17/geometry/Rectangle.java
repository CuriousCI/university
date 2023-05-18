package geometry;

public class Rectangle {
    double width, height;

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    public void scale(double width, double height) {
        this.width = width;
        this.height = height;
    }

    public double perimenter() {
        return (width + height) * 2;
    }

    public double area() {
        return width * height;
    }
}
