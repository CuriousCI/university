package counter;

public class LimitedCounter {
    private int value, limit;

    public LimitedCounter() {
        this.value = 0;
    }

    public void setLimit(int limit) {
        this.limit = limit;
    }

    public void click() {
        if (value < limit)
            value++;
    }

    public void reset() {
        value = 0;
    }

    public void undo() {
        if (value > 0)
            value--;

        // value = Math.max(value - 1, 0);
    }

    public int getValue() {
        return value;
    }
}
