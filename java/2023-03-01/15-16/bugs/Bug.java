package bugs;

public class Bug {
    private int position;
    private int direction;

    public Bug(int position) {
        this.position = position;
        direction = 1;
    }

    public void move() {
        position += direction;
    }

    public void turn() {
        direction = -1 * direction;
    }

    public int getPosition() {
        return position;
    }
}
