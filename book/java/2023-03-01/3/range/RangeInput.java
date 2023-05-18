package range;

public class RangeInput {
    int min, max, current;

    public RangeInput(int min, int max) {
        this.min = min;
        this.max = max;

        current = min;
    }

    public void up() {
        if (current < max)
            current++;
    }

    public void down() {
        if (current > min)
            current--;
    }

    public int value() {
        return current;
    }
}
