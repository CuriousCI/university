package bugs;

public class Moth {
    private double position;

    public Moth(double position) {
        this.position = position;
    }

    public void moveToLight(double light) {
        position += (light - position) / 2;

    }

    public double getPosition() {
        return position;
    }
}
